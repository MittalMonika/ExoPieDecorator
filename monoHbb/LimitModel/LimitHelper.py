import os 
import  sys 



import argparse


class RunLimits:
    ''' class to perform all tasks related to the limits once datacards are prepared '''
    ''' this class exepcts that all the steps needed to prepare the datacards and prepration of its inputs are already performed '''
    
    ''' instantiation of the class is done here ''' 
    def __init__(self, datacardtemplatename):#, runmode):
        self.datacardtemplatename_ = datacardtemplatename
        
        #self.runmode = runmode
        print "class instantiation done"
        
    ''' get the full command to be run for a given datacards '''
    def getfullcommand(self, commandpre, datacard, command_, commandpost):
        return commandpre+datacard+command_+commandpost
        
    def PrintSpacing(self, nLine=1):
        for iline in range(nLine):
            print "***************************************************************************************************************************************"
    
    def TimeFormat(self):
        from datetime import datetime
        now = datetime.now()
        date_str = ((str(now)).replace("-","_")).split(":")  
        date_format = (date_str[0]).replace(" ","_") + "_" + str(date_str[1])
        return date_format
    
    
    def setupDirs(self, txtfile):
        for idir in open(txtfile):
            os.system('mkdir -p '+idir.rstrip())
            os.system('cp index.php '+idir.rstrip())
        return 0
        
    def makedatacards(self, templatecards, allparams, region):
        
        ma =str(allparams[0])
        mA =str(allparams[1])
        tb =(str(allparams[2])).replace(".","p")
        st =(str(allparams[3])).replace(".","p")
        mdm=str(allparams[4])
        
        ## get datacard name
        datacardsname = self.datacardtemplatename_.replace("XXXMA", mA)
        datacardsname = datacardsname.replace("BBBMa",ma)
        datacardsname = datacardsname.replace("ZZZTB",tb)
        datacardsname = datacardsname.replace("YYYSP",st)
        datacardsname = datacardsname.replace("AAAMDM",mdm)
        datacardsname = datacardsname.replace("SR",region)
        
        #print 'data card name is ===',datacardsname
        os.system('rm '+datacardsname)
        fout = open(datacardsname,"a")
        for iline in open(templatecards): 

            iline  = iline.replace("XXXMA", mA)
            if region=="SR": iline  = iline.replace("SR", region)
            if region!="SR": iline  = iline.replace("SR_ggF", region)
            ## add other params 
            #iline = iline.replace("monoHbb2017_B","monoHbb2017_R")
            fout.write(iline)
        fout.close()
        return datacardsname
        
        

    def datacard_to_mparameters(self, name_):
        mparameters_ = ((name_.split("Merged_")[1]).replace(".log","")).split("_")
        mparameters_ = [mp.replace("p",".") for mp in mparameters_]
        ## ma, mA, tb, st, mdm
        return ([mparameters_[9], mparameters_[7], mparameters_[3], mparameters_[1], mparameters_[5]])

    def LogToLimitList(self, logfile):
        expected25_="" 
        expected16_="" 
        expected50_="" 
        expected84_="" 
        expected975_=""
        observed_=""
        for ilongline in open(logfile):
            if "Observed Limit: r < " in ilongline:
                observed_ = ilongline.replace("Observed Limit: r < ","").rstrip()
            if "Expected  2.5%: r < " in ilongline:
                expected25_ = ilongline.replace("Expected  2.5%: r < ","").rstrip()
            if "Expected 16.0%: r < " in ilongline:
                expected16_ = ilongline.replace("Expected 16.0%: r < ","").rstrip()
            if "Expected 50.0%: r < " in ilongline:
                expected50_ = ilongline.replace("Expected 50.0%: r < ","").rstrip()
            if "Expected 84.0%: r < " in ilongline:
                expected84_ = ilongline.replace("Expected 84.0%: r < ","").rstrip()
            if "Expected 97.5%: r < " in ilongline:
                expected975_ = ilongline.replace("Expected 97.5%: r < ","").rstrip()
        
        allparameters  = self.datacard_to_mparameters(logfile)
        towrite =  str(allparameters[0])+" "+str(allparameters[1])+" "+expected25_+" "+expected16_+" "+ expected50_+" "+ expected84_+" "+ expected975_+" "+ observed_+"\n"
        
        print towrite
        outfile="bin/limits_monoH_R_2017.txt"
        #if args.merged: outfile = 'bin/limits_monoH_B_2017.txt'
        #if args.resolved: outfile = 'bin/limits_monoH_R_2017.txt'
        #if args.combined: outfile = 'bin/limits_monoH_Combo_2017.txt'
        
        fout = open(outfile,'a')
        fout.write(towrite)
        fout.close()


    def RunImpacts(self, datacard, logfilename):
        ## run impact  asimov 
        print "do nothing for now"
        ## run impact  data 
        
        
    def SavePrePostComparison(self,run_mode):
        default_fit_root   = "fitDiagnostics.root"
        default_pull_root  = "pulls.root"
        
        ''' prepare the names of root file '''
        fit_Diagnostics = default_fit_root.replace(".root", "_"+run_mode+".root")
        pull_root       = default_pull_root.replace(".root",  "_"+run_mode+".root")
        
        print "run_mode, fit_Diagnostics, pull_root", run_mode, fit_Diagnostics, pull_root
        ''' move the rootfile to avoid ambiguity '''         
        os.system("mv "+default_fit_root+" " + fit_Diagnostics)
        os.system("mv "+default_pull_root+" " + pull_root)
        
        if run_mode == "cronly":
            self.PrintSpacing()
            os.system('root -l -b -q plotPostNuisance_combine.C\(\\"'+fit_Diagnostics+'\\"\)')
        
        if run_mode != "cronly":
            ''' get the different ce nuisances ''' 
            self.PrintSpacing()
            os.system("python diffNuisances.py "+fit_Diagnostics+" --abs --all -g "+pull_root)
            self.PrintSpacing()
            os.system('root -l -b -q PlotPulls.C\(\\"'+pull_root+'\\"\)')
            self.PrintSpacing()
            os.system("python yieldratio.py "+fit_Diagnostics)
            self.PrintSpacing()
            os.system("python PlotPreFitPostFit.py "+fit_Diagnostics)

                        

    
            

    def RunPulls(self, datacard, logfilename, run_mode="data"):
        ## setup the dir structure 
        self.setupDirs("configs/pulls_dir.txt")
        ## data fit 
        if run_mode == "data":
            self.PrintSpacing(2)
            print "performing the fit in run_mode ",run_mode
            os.system("combine -M FitDiagnostics --saveShapes "+datacard+ " --saveWithUncertainties --saveNormalizations --X-rtd MINIMIZER_analytic ")
            self.PrintSpacing(1)
            self.SavePrePostComparison("data")
        
            

        ## asimov fit 
        if run_mode == "asimov":
            self.PrintSpacing(2)
            os.system("combine -M FitDiagnostics --saveShapes "+datacard + " --saveWithUncertainties --saveNormalizations --X-rtd MINIMIZER_analytic  --rMin -100 -t -1 --expectSignal 0")
            self.PrintSpacing(1)
            self.SavePrePostComparison("asimov")
        
        ## CR only fit 
        os.system("text2workspace.py "+datacard+" --channel-masks")
        wsname = datacard.replace(".txt",".root")
        os.system("combine -M FitDiagnostics  "+wsname+" --saveShapes --saveWithUncertainties --setParameters mask_SR=1")
        self.SavePrePostComparison("cronly")
        
        
