import os 
import  sys 
from array import  array
from ROOT import TGraph, TFile, TGraphAsymmErrors
import ROOT as rt
import argparse
import csv 
import describe as dcb


class LimitPlotter:
    ''' class to perform all tasks related to the limits once datacards are prepared '''
    ''' this class exepcts that all the steps needed to prepare the datacards and prepration of its inputs are already performed '''
    
    ''' instantiation of the class is done here ''' 
    def __init__(self, model_):
        
        self.model_    = model_ 
        print "class instantiation done"
        
    ''' get the full command to be run for a given datacards '''

    def SetParameters(self, scan_dict):
        self.fileN = scan_dict["fileN"]
        self.xaxis = scan_dict["xaxis"]
        self.yaxis = scan_dict["yaxis"]
        self.legend = scan_dict["legend"]
        self.filepath = scan_dict["filepath"]
        self.rangeY = scan_dict["rangeY"]
        
        self.limit_text_file = self.filepath + "/" + self.fileN
        self.limit_root_file = self.limit_text_file.replace(".txt",".root")
        
        return 0;
        


    def TextFileToRootGraphs1D(self, scan_dict):
        self.SetParameters(scan_dict)
        
        print ("plotting limits for: ",self.fileN)
        #limit_text_file = self.filepath + "/" + self.fileN
        #filename = limit_text_file #limit_text_filename
        #limit_root_file = limit_text_file.replace(".txt",".root")
        
        f = open(self.limit_text_file,"r")
        med=array('f')
        mchi=array('f')
        expm2=array('f')
        expm1=array('f')
        expmed=array('f')
        expp1=array('f')
        expp2=array('f')
        obs=array('f')
        errx=array('f')
    
        for line in f:
            if len(line.rsplit())<8: continue
            med.append(float(line.rstrip().split()[1]))
            mchi.append(float(line.rstrip().split()[0]))
            
            expm2.append(float(line.rstrip().split()[4]) - float(line.rstrip().split()[2]) )
            expm1.append(float(line.rstrip().split()[4]) - float(line.rstrip().split()[3]) )
            expmed.append(float(line.rstrip().split()[4]))
            expp1.append(float(line.rstrip().split()[5]) - float(line.rstrip().split()[4]) )
            expp2.append(float(line.rstrip().split()[6]) - float(line.rstrip().split()[4]) )

            obs.append(float(line.rstrip().split()[7]))
            errx.append(0.0)
    
        print ('expm2: ', expm2)
        print ('expm1: ', expm1)
        print ('expmed: ', expmed)
        print ('expp1: ', expp1)
        print ('expp2: ', expp2)
    
        g_exp2  = TGraphAsymmErrors(int(len(med)), med, expmed, errx, errx, expm2, expp2 )   ;  g_exp2.SetName("exp2")
        g_exp1  = TGraphAsymmErrors(int(len(med)), med, expmed, errx, errx, expm1, expp1 )   ;  g_exp1.SetName("exp1")
        g_expmed = TGraphAsymmErrors(int(len(med)), med, expmed)   ;  g_expmed.SetName("expmed")
        g_obs    = TGraphAsymmErrors(int(len(med)), med, obs   )   ;  g_obs.SetName("obs")
    
        f1 = TFile(self.limit_root_file,'RECREATE')
        g_exp2.Write()
        g_exp1.Write()
        g_expmed.Write()
        g_obs.Write()
        f1.Write()
        f1.Close()
        return 0;

    def SaveLimitPdf1D(self):#,rootfile):
        limit_text_file = self.filepath + "/" + self.fileN
        filename = limit_text_file #limit_text_filename
        limit_root_file = limit_text_file.replace(".txt",".root")
        rootfile = limit_root_file
        
        
        setlogX=0
        yaxis=1000
        
        rt.gStyle.SetOptTitle(0)
        rt.gStyle.SetOptStat(0)
        rt.gROOT.SetBatch(1)
        c = rt.TCanvas("c","c",620, 600)
        c.SetGrid(0,0)
        c.SetLogy(1)
        c.SetLogx(setlogX)
        c.SetLeftMargin(0.12)
        #leg = rt.TLegend(.15, .65, .35, .890);
        f = rt.TFile(self.limit_root_file,"read")
        exp2s =  f.Get("exp2")
        exp2s.SetMarkerStyle(20)
        exp2s.SetMarkerSize(1.1)
        exp2s.SetLineWidth(2)
        exp2s.SetFillColor(rt.kYellow);
        exp2s.SetLineColor(rt.kYellow)
        exp2s.GetXaxis().SetTitle(self.xaxis);
        exp2s.GetYaxis().SetRangeUser(self.rangeY[0], self.rangeY[1])
        exp2s.GetXaxis().SetTitleOffset(1.1)
        #exp2s.GetYaxis().SetTitle("95% C.L. asymptotic limit on #mu=#sigma/#sigma_{theory}");
        print ("-------------",self.yaxis)
        exp2s.GetYaxis().SetTitle(self.yaxis);
        exp2s.GetYaxis().SetTitleOffset(1.7)
        exp2s.GetYaxis().SetNdivisions(20,5,0);
        #exp2s.GetXaxis().SetNdivisions(505);
        exp2s.GetYaxis().SetMoreLogLabels()
        #exp2s.GetXaxis().SetMoreLogLabels()
        #exp2s.GetXaxis().SetRangeUser(10,750)
        exp2s.Draw("A 3")

        exp1s =  f.Get("exp1")
        exp1s.SetMarkerStyle(20)
        exp1s.SetMarkerSize(1.1)
        exp1s.SetLineWidth(2)
        exp1s.SetFillColor(rt.kGreen);
        exp1s.SetLineColor(rt.kGreen)
        exp1s.Draw("3 same")
    
        exp =  f.Get("expmed")
        exp.SetMarkerStyle(1)
        exp.SetMarkerSize(1.1)
        exp.SetLineStyle(2)
        exp.SetLineWidth(3)
        exp.Draw("L same")

        obs =  f.Get("obs")
        obs.SetMarkerStyle(20)
        #obs.SetMarkerColor(4)
        obs.SetMarkerSize(1.1)
        #obs.SetLineColor(2)
        obs.SetLineWidth(3)
        #obs.Draw("L same")
    
        leg = rt.TLegend(.6, .65, .88, .890);
        leg.SetBorderSize(0);
        leg.SetFillColor(0);
        leg.SetShadowColor(0);
        leg.SetTextFont(42);
        leg.SetTextSize(0.03);
        leg.AddEntry(exp, " CL_{S}  Expected ", "LP");
        leg.AddEntry(exp1s, "CL_{S}  Expected #pm 1#sigma", "LF");
        leg.AddEntry(exp2s, " CL_{S}  Expected #pm 2#sigma", "LF");
        # leg.AddEntry(obs, "CL_{S} Observed", "LP");
    
        leg.Draw("same")
        c.Update()
        print (c.GetUxmin(),c.GetUxmax())
        line = rt.TLine(c.GetUxmin(),1.0,c.GetUxmax(),1.0);
        line.SetLineColor(rt.kRed)
        line.SetLineWidth(2)
        line.Draw('same ')
    
        latex =  rt.TLatex();
        latex.SetNDC();
        latex.SetTextFont(42);
        latex.SetTextSize(0.03);
        latex.SetTextAlign(31);
        latex.SetTextAlign(12);
        model_ = '2HDM+a'
        
        import CMS_lumi
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Preliminary"
        CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
        iPos = 11
        if( iPos==0 ): CMS_lumi.relPosX = 0.12
        
        ''' fix this
        iPeriod=int(rootfile.split("/")[-1].split(".")[0].split("_")[-1])
        CMS_lumi.CMS_lumi(c, iPeriod, iPos)
        '''
        
        category=""
        if "_R_" in rootfile: category="Resolved"
        if "_B_" in rootfile: category="Boosted"
        if "combined" in rootfile: category="R+B"
        
        if "2hdma" in self.model_:
            MA_="150"
            latex.DrawLatex(0.20, 0.77, "mono-h bb "+category);
            latex.DrawLatex(0.20, 0.72, "2HDM+a");
            if len(self.legend)>=1: latex.DrawLatex(0.15, 0.67, self.legend[0])
            if len(self.legend)>=2: latex.DrawLatex(0.17, 0.62, self.legend[1])

        if "dmsimp" in self.model_:
            MA_="600"
            latex.DrawLatex(0.21, 0.7, "DMSiMP bb+p_{T}^{miss}  "+category);
            latex.DrawLatex(0.21, 0.64, "m_{\chi} = 1 GeV");
            
                
        
        self.limit_pdf_file  = rootfile.replace(".root","_"+self.model_+".pdf").replace("bin/","plots_limit/")
        
        #c.SetLogx(1)
        c.Update()
        #c.SaveAs(name+".png")
        c.SaveAs(self.limit_pdf_file)
        c.SaveAs(self.limit_pdf_file.replace(".pdf",".png"))
        c.Close()
        
        return "pdf file is saved"
        
    def RunImpacts(self, datacard, logfilename, runmode="data"):
        workspace=datacard.replace(".txt",".root")
        
        
        if runmode=="data":
            ''' First we perform an initial fit for the signal strength and its uncertainty''' 
            os.system("combineTool.py -M Impacts -d "+workspace+" -m 200 --rMin -1 --rMax 2 --robustFit 1 --doInitialFit  -t -1 ")
            '''Then we run the impacts for all the nuisance parameters'''
            os.system("combineTool.py -M Impacts -d "+workspace+" -m 200 --rMin -1 --rMax 2 --robustFit 1 --doFits  -t -1 ")
            '''we collect all the output and convert it to a json file'''
            os.system("combineTool.py -M Impacts -d "+workspace+" -m 200 --rMin -1 --rMax 2 --robustFit 1 --output impacts.json")
            '''then make a plot showing the pulls and parameter impacts, sorted by the largest impact'''
            os.system("plotImpacts.py -i impacts.json -o impacts")
            
            
        ## run impact  asimov 
        print "do nothing for now"
        ## run impact  data 
        
        
    def SavePrePostComparison(self,run_mode, outdir, category, year):
        default_fit_root   = "fitDiagnostics.root"
        default_pull_root  = "pulls.root"
        
        ''' prepare the names of root file '''
        fit_Diagnostics = default_fit_root.replace(".root", "_"+category+"_"+year+"_"+run_mode+".root")
        pull_root       = default_pull_root.replace(".root",  "_"+category+"_"+year+"_"+run_mode+".root")
        
        print "run_mode, fit_Diagnostics, pull_root", run_mode, fit_Diagnostics, pull_root
        ''' move the rootfile to avoid ambiguity '''         

        postfix_ = "_"+category+"_"+year+"_"
        
        
        if run_mode == "cronly":
            self.PrintSpacing()
            dir_ = outdir["pulls"]
            os.system("mv "+default_fit_root+" " + fit_Diagnostics)
            os.system('root -l -b -q plotPostNuisance_combine.C\(\\"'+fit_Diagnostics+'\\",\\"'+dir_+'\\",\\"'+postfix_+'\\"\)')
            
            print ("python PlotPreFitPostFit.py "+fit_Diagnostics+" "+dir_+" "+postfix_)
            os.system("python PlotPreFitPostFit.py "+fit_Diagnostics+" "+dir_+" "+postfix_)
        
        if run_mode != "cronly":
            os.system("mv "+default_fit_root+" " + fit_Diagnostics)
            ''' get the different of nuisances ''' 
            self.PrintSpacing()
            print ("python diffNuisances.py "+fit_Diagnostics+" --abs --all -g "+pull_root)
            os.system("python diffNuisances.py "+fit_Diagnostics+" --abs --all -g "+pull_root)
            os.system("mv "+default_pull_root+" " + pull_root)
            self.PrintSpacing()
            dir_ = outdir["pulls"]
            
            print ('root -l -b -q PlotPulls.C\(\\"'+pull_root+'\\",\\"'+dir_+'\\",\\"'+postfix_+'\\"\)')
            os.system('root -l -b -q PlotPulls.C\(\\"'+pull_root+'\\",\\"'+dir_+'\\",\\"'+postfix_+'\\"\)')
            dir_ = outdir["yr"]
            self.PrintSpacing()
            print ("python yieldratio.py "+fit_Diagnostics+" "+dir_+" "+postfix_)
            os.system("python yieldratio.py "+fit_Diagnostics+" "+dir_+" "+postfix_)
            dir_ = outdir["pfitOverlay"]
            self.PrintSpacing()
            
            print ("python PlotPreFitPostFit.py "+fit_Diagnostics+" "+dir_+" "+postfix_)
            os.system("python PlotPreFitPostFit.py "+fit_Diagnostics+" "+dir_+" "+postfix_)
            
            dir_ = outdir["stack"]
            print "call the stack file"
            dir_ = outdir["tf"]
            print "call the TF file"
            

                        

    
            

    def RunPulls(self, datacard, run_mode, outdir, category, year):
        ## setup the dir structure 
        #self.setupDirs("configs/pulls_dir.txt")
        ## data fit 
        if run_mode == "data":
            self.PrintSpacing(2)
            print "performing the fit in run_mode ",run_mode
            print ("combine -M FitDiagnostics --saveShapes "+datacard+ " --saveWithUncertainties --saveNormalizations --X-rtd MINIMIZER_analytic ")
            os.system("combine -M FitDiagnostics --saveShapes "+datacard+ " --saveWithUncertainties --saveNormalizations --X-rtd MINIMIZER_analytic ")
            self.PrintSpacing(1)
            self.SavePrePostComparison("data",outdir,category, year)
        
            

        ## asimov fit 
        if run_mode == "asimov":
            self.PrintSpacing(2)
            print ("combine -M FitDiagnostics --saveShapes "+datacard + " --saveWithUncertainties --saveNormalizations --X-rtd MINIMIZER_analytic  --rMin -100 -t -1 --expectSignal 0")
            os.system("combine -M FitDiagnostics --saveShapes "+datacard + " --saveWithUncertainties --saveNormalizations --X-rtd MINIMIZER_analytic  --rMin -100 -t -1 --expectSignal 0")
            self.PrintSpacing(1)
            self.SavePrePostComparison("asimov",outdir,category,year)
        
        ## CR only fit 
        if run_mode == "cronly":
            print ("text2workspace.py "+datacard+" --channel-masks")
            os.system("text2workspace.py "+datacard+" --channel-masks")
            wsname = datacard.replace(".txt",".root")

            print("combine -M FitDiagnostics  "+wsname+" --saveShapes --saveWithUncertainties --setParameters mask_SR=1,mask_cat_1b_SR=1,mask_cat_2b_SR=1 --X-rtd MINIMIZER_analytic --cminFallbackAlgo Minuit2,0:1.0")
            os.system("combine -M FitDiagnostics  "+wsname+" --saveShapes --saveWithUncertainties --setParameters mask_SR=1,mask_cat_1b_SR=1,mask_cat_2b_SR=1 --X-rtd MINIMIZER_analytic --cminFallbackAlgo Minuit2,0:1.0")
            
            
            self.SavePrePostComparison("cronly",outdir, category,year)
        
        
