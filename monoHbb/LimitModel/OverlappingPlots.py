# In this at the end of filevector I am putting the dirname
# so loop over n-1 files and n will give the name of the output dir.

# In legend also the n element will give the name for the ratio plot y axis label.
#edited by Monika Mittal 
#Script for ratio plot 
import sys

import ROOT 
ROOT.gROOT.SetBatch(True)
sys.argv.append( '-b-' )


from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors
from ROOT import TH1D, TH1, TH1I
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex

import os
colors=[1,4,2,8,5,9,41,46,30,12,28,20,32]
markerStyle=[23,21,22,20,24,25,26,27,28,29,20,21,22,23]            
linestyle=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


def DrawOverlap(fileVec, histVec, titleVec,legendtext,pngname,logstatus=[0,0],xRange=[-99999,99999,1],minmax=[1000,0.1],year=[2017]):
    print(type(year[0]), year[0])
    gStyle.SetOptTitle(0)
    gStyle.SetOptStat(0)
    gStyle.SetTitleOffset(1.1,"Y");
    #gStyle.SetTitleOffset(1.9,"X");
    gStyle.SetLineWidth(3)
    gStyle.SetFrameLineWidth(3); 
    #gStyle.SetGridx()
    #gStyle.SetGridy()

    i=0

    histList_=[]
    histList=[]
    histList1=[]
    maximum=[]
    
    ## Legend    
    leg = TLegend(0.1, 0.70, 0.89, 0.89)#,NULL,"brNDC");
    leg.SetBorderSize(0)
    leg.SetNColumns(2)
    leg.SetLineColor(1)
    leg.SetLineStyle(1)
    leg.SetLineWidth(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.04)
     
    c = TCanvas("c1", "c1",0,0,500,500)
    c.SetBottomMargin(0.15)
    c.SetLogy(logstatus[1])
    c.SetLogx(logstatus[0])
    print ("you have provided "+str(len(fileVec))+" files and "+str(len(histVec))+" histograms to make a overlapping plot" )
    print "opening rootfiles"
    c.cd()
    
    ii=0    
    inputfile={}
    print str(fileVec[(len(fileVec)-1)])

    for ifile_ in range(len(fileVec)):
        print ("opening file  "+fileVec[ifile_])
        inputfile[ifile_] = TFile( fileVec[ifile_] )
        print "fetching histograms"
        for ihisto_ in range(len(histVec)):
            print ("printing histo "+str(histVec[ihisto_]))
            histo = inputfile[ifile_].Get(histVec[ihisto_])
            #status_ = type(histo) is TGraphAsymmErrors
            histList.append(histo)
            # for ratio plot as they should nt be normalize 
            histList1.append(histo)
            print histList[ii].Integral()
            #histList[ii].Rebin(xRange[2])
            #histList[ii].Scale(1.0/histList[ii].Integral())
            maximum.append(histList[ii].GetMaximum())
            maximum.sort()
            ii=ii+1

    print histList
    for ih in range(len(histList)):
        tt = type(histList[ih])
        if logstatus[1] is 1 :
            #histList[ih].SetMaximum(100) #1.4 for log
            #histList[ih].SetMinimum(0.1) #1.4 for log
            histList[ih].SetMaximum(minmax[0])
            histList[ih].SetMinimum(minmax[1])
        if logstatus[1] is 0 :
            histList[ih].SetMaximum(1.4) #1.4 for log
            histList[ih].SetMinimum(0.001) #1.4 for log
#        print "graph_status =" ,(tt is TGraphAsymmErrors)
#        print "hist status =", (tt is TH1D) or (tt is TH1F)
        if ih == 0 :      
            if tt is TGraphAsymmErrors : 
                histList[ih].Draw("APL")
            if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
                histList[ih].Draw()## removed hist   
        if ih > 0 :
            #histList[ih].SetLineWidth(2)
            if tt is TGraphAsymmErrors : 
                histList[ih].Draw("PL same")
            if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
                histList[ih].Draw("same")   ## removed hist 

        if tt is TGraphAsymmErrors :
            histList[ih].SetMaximum(minmax[0]) 
            histList[ih].SetMinimum(minmax[1]) 
            histList[ih].SetMarkerColor(colors[ih])
            histList[ih].SetLineColor(colors[ih])
            histList[ih].SetLineWidth(2)
            histList[ih].SetMarkerStyle(markerStyle[ih])
            histList[ih].SetMarkerSize(1)
            leg.AddEntry(histList[ih],legendtext[ih],"PL")
        if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
            histList[ih].SetLineStyle(linestyle[ih])
            histList[ih].SetLineColor(colors[ih])
            histList[ih].SetLineWidth(3)
            leg.AddEntry(histList[ih],legendtext[ih],"L")
        histList[ih].GetYaxis().SetTitle(titleVec[1])
        histList[ih].GetYaxis().SetTitleSize(0.052)
        histList[ih].GetYaxis().SetTitleOffset(0.98)
        histList[ih].GetYaxis().SetTitleFont(42)
        histList[ih].GetYaxis().SetLabelFont(42)
        histList[ih].GetYaxis().SetLabelSize(.052)
        histList[ih].GetXaxis().SetRangeUser(xRange[0],xRange[1])
        #     histList[ih].GetXaxis().SetLabelSize(0.0000);
        
        histList[ih].GetXaxis().SetTitle(titleVec[0])
        histList[ih].GetXaxis().SetLabelSize(0.052)
        histList[ih].GetXaxis().SetTitleSize(0.052)
        #histList[ih].GetXaxis().SetTitleOffset(1.14)
        histList[ih].GetXaxis().SetTitleFont(42)

        histList[ih].GetXaxis().SetLabelFont(42)
        histList[ih].GetYaxis().SetLabelFont(42) 
        histList[ih].GetXaxis().SetNdivisions(507)
        #histList[ih].GetXaxis().SetMoreLogLabels(); 
        #histList[ih].GetXaxis().SetNoExponent();
        #histList[ih].GetTGaxis().SetMaxDigits(3);

        i=i+1
    pt = TPaveText(0.01,0.92,0.95,0.96,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(42)
    pt.SetTextSize(0.046)
    #text = pt.AddText(0.12,0.35,"CMS Internal                     36 fb^{-1} (2016) ")
    print(year)
    if(year[0] == 2017):
        print( "i am in" , year[0])
        text = pt.AddText(0.12,0.35,"CMS Internal                     41.5 fb^{-1} (2017) ")
    if(year[0]== 2018):        
        text = pt.AddText(0.12,0.35,"CMS Internal                     59.6 fb^{-1} (2018) ")
    #text = pt.AddText(0.6,0.5,"41.5 fb^{-1} (2017) ")
    pt.Draw()
   
    

    leg.Draw()
    outputdirname = 'plots_limit/limitcomp/Optimization/'
    histname=outputdirname+pngname 
    c.SaveAs(histname+'.png')
    c.SaveAs(histname+'.pdf')
    outputname = 'cp  -r '+ histname+'*' +'       /eos/user/m/mmittal/www/MonoHbb/PlotsForSlides/1Mar2022/'
    print(outputname)
    os.system(outputname) 
    


print "calling the plotter"
'''
# zp2hdm

#RESOLVED
dirname_29='bin/AllMETHistos_monohbb_v12_07_16_unrolled_29BinsHist_ResolvedCROnly_zp2hdm_RP/'
dirname_4='bin/AllMETHistos_monohbb_v12_07_16_updatedData_zp2hdm_RP/'
dirname_15='bin/AllMETHistos_monohbb_v12_07_16_unrolled_15BinsHist_zp2hdm_RP/'
dirname_4361 ='bin/AllMETHistos_monohbb_v12_07_16_unrolled_43RVs61BRebinBinsHist_zp2hdm_RP/'
dirname_lowmet ='bin/AllMETHistos_monohbb_lowMETCat_25bins_zp2hdm_RP/'
files=[dirname_4+'limits_monoHbb_zp2hdm_R_2017.root', 
dirname_15+'limits_monoHbb_zp2hdm_R_2017.root', 
dirname_29+'limits_monoHbb_zp2hdm_R_2017.root',
dirname_4361+'limits_monoHbb_zp2hdm_R_2017.root',
dirname_lowmet+'limits_monoHbb_zp2hdm_R_2017.root'

]
legend=['4bin(R)','15bin(R)','29bin(R)','43bin(R)','lowmet(R)']
histoname1=['expmed']

xtitle='m_{Z'}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_zp2hdm_RP_resolved_only',[0,1],[300,3000],[100,0.005])

#BOOSTED
dirname_4='bin/AllMETHistos_monohbb_v12_07_16_updatedData_zp2hdm_RP/'
dirname_15='bin/AllMETHistos_monohbb_v12_07_16_unrolled_15BinsHist_zp2hdm_RP/'
dirname_45='bin/AllMETHistos_monohbb_v12_07_16_unrolled_45BinsHist_BoostedCROnly_zp2hdm_RP/'
dirname_61='bin/AllMETHistos_monohbb_v12_07_16_unrolled_61BinsHist_BoostedCROnly_zp2hdm_RP/'
dirname_4361 ='bin/AllMETHistos_monohbb_v12_07_16_unrolled_43RVs61BRebinBinsHist_zp2hdm_RP/'
dirname_lowmet ='bin/AllMETHistos_monohbb_lowMETCat_25bins_zp2hdm_RP/'
files=[dirname_4+'limits_monoHbb_zp2hdm_B_2017.root',
dirname_15+'limits_monoHbb_zp2hdm_B_2017.root',
dirname_45+'limits_monoHbb_zp2hdm_B_2017.root',
dirname_61+'limits_monoHbb_zp2hdm_B_2017.root',
dirname_4361+'limits_monoHbb_zp2hdm_B_2017.root',
dirname_lowmet+'limits_monoHbb_zp2hdm_B_2017.root'


]

#legend=['Resolved(Pho)','Boosted(Pho)','Combined(Pho)','Resolved(data)','Boosted(data)','Combined(data)']
legend=['Resolved(2bin)','Boosted(2bin)','Combined(2bin)' ,'Resolved(15bin)','Boosted(15bin)','Combined(15bin)' ]

legend=['4bin(B)','15bin(B)','45bin(B)','61bin(B)','61binImp(B)','lowmet(B)']
histoname1=['expmed']

xtitle='m_{Z'}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_zp2hdm_RP_boosted_only',[0,1],[300,3000],[100,0.005])


dirname_4='bin/AllMETHistos_monohbb_v12_07_16_updatedData_zp2hdm_RP/'
dirname_4361 ='bin/AllMETHistos_monohbb_v12_07_16_unrolled_43RVs61BRebinBinsHist_zp2hdm_RP/'
dirname_lowmet ='bin/AllMETHistos_monohbb_lowMETCat_25bins_zp2hdm_RP/'
files=[dirname_4+'limits_monoHbb_zp2hdm_combined_2017.root',
dirname_4361+'limits_monoHbb_zp2hdm_combined_2017.root',
OBdirname_lowmet+'limits_monoHbb_zp2hdm_combined_2017.root'
]
legend=['4bin','43_61bin','lowmet']
histoname1=['expmed']

xtitle='m_{Z'}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_zp2hdm_RP_combined',[0,1],[300,3000],[100,0.005])


zp2hdm_ = 'bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_zp2hdm_RP/'
files=[zp2hdm_+'limits_monoHbb_zp2hdm_R_2017.root',
zp2hdm_+'limits_monoHbb_zp2hdm_B_2017.root',
zp2hdm_+'limits_monoHbb_zp2hdm_F_2017.root',
zp2hdm_+'limits_monoHbb_zp2hdm_combined_2017.root']
legend=['Resolved','Boosted','Low met Resolved','Combined']
histoname1=['expmed']

xtitle="m_{Z'}[GeV]"
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_zp2hdm_RP_3cat_3files',[0,1],[450,3000],[100,0.005])


zp2hdm_tf = 'bin/AllMETHistos_monohbb_v12_07_09_updatedPhoVeto_zp2hdm_TF/'
files=[
zp2hdm_+'limits_monoHbb_zp2hdm_combined_2017.root',
zp2hdm_tf+'limits_monoHbb_zp2hdm_combined_2017.root'

]
legend=['Combined(TF)', 'Combined(RP)']
histoname1=['expmed']

xtitle="m_{Z'}[GeV]"
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_zp2hdm_TFvsRP_combined',[0,1],[300,3000],[5,0.005])




#zpbaryonic
zpb_='bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_zpb_RP_mchi1/'
files=[zpb_+'limits_monoHbb_zpb_R_2017.root',
zpb_+'limits_monoHbb_zpb_B_2017.root',
zpb_+'limits_monoHbb_zpb_F_2017.root',
zpb_+'limits_monoHbb_zpb_combined_2017.root']
legend=['Resolved','Boosted','Low met Resolved','Combined']
histoname1=['expmed']

xtitle="m_{Z'}[GeV]"
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_zpb_RP_3cat_3files',[0,1],[100,3500],[500,0.02])









#2018 2hdma different files
dirname_='bin/AllMETHistos_2018_monohbb_v12_07_16_2hdma_RP_fixedbug/'
files=[dirname_+'limits_monoHbb_2hdma_R_2018.root',
dirname_+'limits_monoHbb_2hdma_B_2018.root',
dirname_+'limits_monoHbb_2hdma_F_2018.root',
dirname_+'limits_monoHbb_2hdma_combined_2018.root']
legend=['Resolved', 'Boosted','low met resolved','Combined']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2018_2hdma_RP_3cat_different_files',[0,1],[200,3000],[300,0.1])


#2018 2hdma different files
dirname___='bin/AllMETHistos_2018_monohbb_v12_07_16_2hdma_RP_fixedbug/'
dirname_='bin/AllMETHistos_2018_monohbb_v12_07_16_2hdma_RP/'
dirname__='bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_2hdma_RP/'
dirname____='bin/AllMETHistos_monohbb_2018_CRbinning_2hdma_all_cat_RP/'
dirname_MCR='bin/AllMETHistos_monohbb_2017_CRbinning_2hdma_all_cat_RP/'
files=[dirname__+'limits_monoHbb_2hdma_combined_2017.root',
       dirname_+'limits_monoHbb_2hdma_combined_2018.root',
       dirname___+'limits_monoHbb_2hdma_combined_2018.root',
       dirname____+'limits_monoHbb_2hdma_combined_2018.root',
       dirname_MCR+'limits_monoHbb_2hdma_combined_2017.root'

]

legend=['Combined(2017)','Combined(2018)','Combined(2018)bug fixed','Combined(2018) multibinCR', 'Combined(2017) multibinCR']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017vs2018_2hdma_RP_3cat_different_files',[0,1],[200,3000],[300,0.1])






# comparison of 2017 1 bin vs multibin CR
dirname_2017_1bin='bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_2hdma_RP/'
dirname_2017_multibin='bin/AllMETHistos_monohbb_v12_07_18_RP_2hdma/'
dirname_2017_35bin='bin/AllMETHistos_monohbb_v12_07_18_35binsResolvedOnly_2017_2hdma_RP/'
dirname_2017_35bin_correctunc='bin/AllMETHistos_monohbb_v12_08_20_35Rvs25B_2hdma_RP/'
dirname_2017_35bin_Signal_not_normalized='bin/AllMETHistos_monohbb_v12_08_20_35Rvs25B_reNorm_pdf_scale_2hdma_RP/'
dirname_MCR='bin/AllMETHistos_monohbb_2017_CRbinning_2hdma_all_cat_RP/'
files=[dirname_2017_1bin+'limits_monoHbb_2hdma_R_2017.root',
       dirname_2017_multibin+'limits_monoHbb_2hdma_R_2017.root',
       dirname_2017_35bin+'limits_monoHbb_2hdma_R_2017.root',
       dirname_2017_35bin_correctunc+'limits_monoHbb_2hdma_R_2017.root',
       dirname_2017_35bin_Signal_not_normalized+'limits_monoHbb_2hdma_R_2017.root',
       dirname_MCR+'limits_monoHbb_2hdma_R_2017.root',

]

legend=['1bin CR', 'multibinCR', '35bin','35bin(unc_added)','35bin(pdf unc not  Signal_normalized)','35bin(pdf unc Signal_normalized)checked' ]
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_RP_1binvsmultibinCR_resloved',[0,1],[200,3000],[300,0.1])

#smaller version of up plot
dirname_2017_1bin='bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_2hdma_RP/'
dirname_2017_multibin='bin/AllMETHistos_monohbb_v12_07_18_RP_2hdma/'
dirname_2017_35bin_Signal_not_normalized='bin/AllMETHistos_monohbb_v12_08_20_35Rvs25B_reNorm_pdf_scale_2hdma_RP/'
dirname_MCR='bin/AllMETHistos_monohbb_2017_CRbinning_2hdma_all_cat_RP/'
files=[dirname_2017_1bin+'limits_monoHbb_2hdma_R_2017.root',
       dirname_2017_multibin+'limits_monoHbb_2hdma_R_2017.root',
       dirname_2017_35bin_Signal_not_normalized+'limits_monoHbb_2hdma_R_2017.root',
       dirname_MCR+'limits_monoHbb_2hdma_R_2017.root',

]

legend=['1bin CR', 'multibinCR', '35bin(pdf unc Signal_normalized)','35bin(pdf unc Signal_normalized)checked' ]
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_RP_1binvsmultibinCR_resloved_check',[0,1],[200,3000],[300,0.1])

dirname_2017_1bin='bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_2hdma_RP/'
dirname_2017_multibin='bin/AllMETHistos_monohbb_v12_07_18_RP_2hdma/'

files=[dirname_2017_1bin+'limits_monoHbb_2hdma_B_2017.root',
       dirname_2017_multibin+'limits_monoHbb_2hdma_B_2017.root']
legend=['1bin CR', 'multibinCR']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_RP_1binvsmultibinCR_boosted',[0,1],[200,3000],[300,0.1])
'''


dirname2018_='bin/AllMETHistos_2018_monohbb_v12_09_21_NoJER_reNormScale_fixedBinBug_finalcheck_2hdma/'
files=[dirname2018_+'limits_monoHbb_2hdma_R_2018.root',
dirname2018_+'limits_monoHbb_2hdma_B_2018.root',
dirname2018_+'limits_monoHbb_2hdma_combined_2018.root']

legend=['Resolved', 'Boosted','Combined']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_combined_2018_revised',[0,1],[200,3000],[300,0.1], [2018])


dirname2017_jer='bin/AllMETHistos_monohbb_v12_09_21_JEROnBKG_reNormScale_2hdma_RP/'
dirname2017='bin/AllMETHistos_monohbb_v12_08_21_UpdatedMetTrigUnc_2017_2hdma_RP_datacard_fix/'
dirname2017_jer_all='bin/AllMETHistos_2017_monohbb_v12_09_21_JER_reNormScale_v2_2hdma_RP/'
dirname2018='bin/AllMETHistos_monohbb_v12_08_21_UpdatedMetTrigUnc_2018_2hdma_RP_datacard_fix/'
dirname2018_nojer='bin/AllMETHistos_2018_monohbb_v12_09_21_NoJER_reNormScale_2hdma_RP/'
files=[dirname2017_jer+'limits_monoHbb_2hdma_R_2017.root',
dirname2017_jer+'limits_monoHbb_2hdma_B_2017.root',
dirname2017_jer+'limits_monoHbb_2hdma_combined_2017.root']

legend=['Resolved', 'Boosted','Combined']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_combined_2017_jer',[0,1],[200,3000],[300,0.1],[2017])


files=[dirname2017_jer_all+'limits_monoHbb_2hdma_combined_2017.root',
dirname2017_jer+'limits_monoHbb_2hdma_combined_2017.root',
dirname2017+'limits_monoHbb_2hdma_combined_2017.root']


legend=['Combined(JERv2)','Combined(JEROnBKG)', 'Combined(previous)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_combined_2017_jer_com',[0,1],[200,3000],[300,0.1],[2017])




###







files=[dirname2018_nojer+'limits_monoHbb_2hdma_combined_2018.root',
dirname2018+'limits_monoHbb_2hdma_combined_2018.root'
]
legend=['Combined(2018)(recent:nojer)','Combined(2018)(previous)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_combined_2018_comp',[0,1],[200,3000],[300,0.1],[2017])


#dirname2018='bin/AllMETHistos_monohbb_v12_08_21_UpdatedMetTrigUnc_2018_2hdma_RP_datacard_fix/'
dirname2018='bin/AllMETHistos_2018_monohbb_v12_08_21_addedMorePointsForZp2HDM/'
dirname2017='bin/AllMETHistos_monohbb_v12_08_21_UpdatedMetTrigUnc_2017_2hdma_RP_datacard_fix/'
files=[dirname2017+'limits_monoHbb_2hdma_combined_2017.root',
dirname2018+'limits_monoHbb_2hdma_combined_2018.root'
]
legend=['Combined(2017)','Combined(2018)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_combined_2017_2018_new',[0,1],[200,3000],[300,0.1],[2017])


'''
dirname_='bin/AllMETHistos_monohbb_2017_CRbinning_2hdma_all_cat_RP/'
dirname__='bin/AllMETHistos_monohbb_v12_08_21_UpdatedMetTrigUnc_2017_2hdma_RP_test/'
dirname___='bin/AllMETHistos_monohbb_v12_08_21_UpdatedMetTrigUnc_2018_2hdma_RP_test/'
dirname____='bin/AllMETHistos_monohbb_v12_08_21_UpdatedMetTrigUnc_2017_2hdma_RP_datacard_fix/'
dirname_____='bin/AllMETHistos_monohbb_v12_08_21_UpdatedMetTrigUnc_2018_2hdma_RP_datacard_fix/'
files=[#dirname_+'limits_monoHbb_2hdma_R_2017.root',
#dirname_+'limits_monoHbb_2hdma_B_2017.root',
#dirname_+'limits_monoHbb_2hdma_F_2017.root',
dirname_+'limits_monoHbb_2hdma_combined_2017.root',
dirname__+'limits_monoHbb_2hdma_combined_2017.root',
dirname____+'limits_monoHbb_2hdma_combined_2017.root',
dirname___+'limits_monoHbb_2hdma_combined_2018.root',
dirname_____+'limits_monoHbb_2hdma_combined_2018.root']

#legend=['Resolved', 'Boosted','low met resolved','Combined','combined(R+B)','C(2018)']
legend=['Combined(Last Presentation)','combined(R+B 2017)','new(2017)','Combined(2018)','new(2018)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_comparison_combined',[0,1],[200,3000],[300,0.1])





###comparison 2017 R 2018 R 2hdma
files=[dirname_+'limits_monoHbb_2hdma_R_2017.root',
#dirname_+'limits_monoHbb_2hdma_B_2017.root',
#dirname_+'limits_monoHbb_2hdma_F_2017.root',
#dirname_+'limits_monoHbb_2hdma_combined_2017.root',
dirname__+'limits_monoHbb_2hdma_R_2017.root',
dirname____+'limits_monoHbb_2hdma_R_2017.root',
dirname___+'limits_monoHbb_2hdma_R_2018.root',
dirname_____+'limits_monoHbb_2hdma_R_2018.root']

legend=['Resolved(Last Presenation)', 'Resolved(2017)', 'new(2017)','Resolved(2108)','new(2018)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_comparison_Resolved',[0,1],[200,3000],[300,0.1])

files=[dirname_+'limits_monoHbb_2hdma_B_2017.root',
#dirname_+'limits_monoHbb_2hdma_B_2017.root',
#dirname_+'limits_monoHbb_2hdma_F_2017.root',
#dirname_+'limits_monoHbb_2hdma_combined_2017.root',
dirname__+'limits_monoHbb_2hdma_B_2017.root',
dirname____+'limits_monoHbb_2hdma_B_2017.root',
dirname___+'limits_monoHbb_2hdma_B_2018.root',
dirname_____+'limits_monoHbb_2hdma_B_2018.root']

legend=['Boosted(Last Presenation)', 'Boosted(2017)','new(2017)', 'Boosted(2108)','new(2018)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_comparison_Boosted',[0,1],[200,3000],[300,0.1])
'''
#2HDMA
'''
#RESOLVED
dirname_29='bin/AllMETHistos_monohbb_v12_07_16_unrolled_29BinsHist_ResolvedCROnly_2hdma_RP/'
dirname_4='bin/AllMETHistos_monohbb_v12_07_16_updatedData_2hdma_RP/'
dirname_15='bin/AllMETHistos_monohbb_v12_07_16_unrolled_15BinsHist_2hdma_RP/'
dirname_lowmet='bin/AllMETHistos_monohbb_lowMETCat_25bins/'
dirname_lowmet_up='bin/AllMETHistos_monohbb_v12_07_16_lowMETCat_25bins_UpdatedMetTrig/'
files=[
dirname_4+'limits_monoHbb_2hdma_R_2017.root',
dirname_15+'limits_monoHbb_2hdma_R_2017.root',
dirname_29+'limits_monoHbb_2hdma_R_2017.root',
dirname_lowmet+'limits_monoHbb_2hdma_R_2017.root',
dirname_lowmet_up+'limits_monoHbb_2hdma_R_2017.root'
#dirname_up+'limits_monoHbb_2hdma_combined_2017.root',
#dirname+'limits_monoHbb_2hdma_B_2017.root',
]

#legend=['Resolved(Pho)','Boosted(Pho)','Combined(Pho)','Resolved(data)','Boosted(data)','Combined(data)']
#legend=['Resolved(2bin)','Boosted(2bin)','Combined(2bin)' ,'Resolved(15bin)','Boosted(15bin)','Combined(15bin)' ]
legend=['4bin(R)','15bin(R)','29bin(R)', 'lowmet(R)','metsys(R)']
histoname1=['expmed']

xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_RP_resolved_only',[0,1],[300,3000],[100,0.005])



#boosted
dirname_45='bin/AllMETHistos_monohbb_v12_07_16_unrolled_45BinsHist_BoostedCROnly_2hdma_RP/'
#dirname_29='bin/AllMETHistos_monohbb_v12_07_16_unrolled_29BinsHist_ResolvedCROnly_2hdma_RP/'
#dirname_4='bin/AllMETHistos_monohbb_v12_07_16_updatedData_2hdma_RP/'
dirname_15='bin/AllMETHistos_monohbb_v12_07_16_unrolled_15BinsHist_2hdma_RP/'
dirname_lowmet='bin/AllMETHistos_monohbb_lowMETCat_25bins/'
files=[
dirname_15+'limits_monoHbb_2hdma_B_2017.root',
dirname_45+'limits_monoHbb_2hdma_B_2017.root',
dirname_lowmet+'limits_monoHbb_2hdma_B_2017.root',
#dirname_29+'limits_monoHbb_2hdma_R_2017.root'
#dirname_up+'limits_monoHbb_2hdma_combined_2017.root',
#dirname+'limits_monoHbb_2hdma_B_2017.root',
]

#legend=['Resolved(Pho)','Boosted(Pho)','Combined(Pho)','Resolved(data)','Boosted(data)','Combined(data)']
#legend=['Resolved(2bin)','Boosted(2bin)','Combined(2bin)' ,'Resolved(15bin)','Boosted(15bin)','Combined(15bin)' ]
legend=['15bin(B)','45bin(B)', 'lowmet(B)']
histoname1=['expmed']

xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_RP_boosted_only',[0,1],[300,3000],[100,0.005])









dirname_4='bin/AllMETHistos_monohbb_v12_07_16_updatedData_2hdma_RP/'
dirname_4361 ='bin/AllMETHistos_monohbb_v12_07_16_unrolled_43RVs61BRebinBinsHist_2hdma_RP/'
dirname_lowmet='bin/AllMETHistos_monohbb_lowMETCat_25bins/'
files=[dirname_4+'limits_monoHbb_2hdma_combined_2017.root',
dirname_4361+'limits_monoHbb_2hdma_combined_2017.root',
dirname_lowmet+'limits_monoHbb_2hdma_combined_2017.root'
]
legend=['4bin','43_61bin','lowmet']
histoname1=['expmed']

xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_RP_combined',[0,1],[300,3000],[100,0.005])
'''









'''


tf_='bin/AllMETHistos_monohbb_v12_07_16_updatedData_2hdma_TF/'
rp_='bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_2hdma_RP/'
files=[tf_+'limits_monoHbb_2hdma_combined_2017.root',
rp_+'limits_monoHbb_2hdma_combined_2017.root',]
legend=['Combined(TF)','Combined(RP)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_TFvsRP_combined',[0,1],[200,3000],[300,0.1])

#TF 2hdma
dirname_='bin/AllMETHistos_monohbb_v12_07_16_updatedData_2hdma_TF/'
files=[dirname_+'limits_monoHbb_2hdma_R_2017.root',
dirname_+'limits_monoHbb_2hdma_B_2017.root',
dirname_+'limits_monoHbb_2hdma_combined_2017.root']
legend=['Resolved', 'Boosted','Combined']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_TF',[0,1],[200,3000],[300,0.1])


dirname_TF='bin/AllMETHistos_monohbb_v12_07_16_updatedData_2hdma_TF/'
dirname_RP='bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_2hdma_RP/'
files=[dirname_TF+'limits_monoHbb_2hdma_B_2017.root',
dirname_RP+'limits_monoHbb_2hdma_B_2017.root',
]
legend=[ 'Boosted(TF)','Boosted(RP)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_TFvsRP_boosted',[0,1],[200,3000],[300,0.1])

files=[dirname_TF+'limits_monoHbb_2hdma_R_2017.root',
dirname_RP+'limits_monoHbb_2hdma_R_2017.root',
]
legend=[ 'Resolved(TF)','Resolved(RP)']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_TFvsRP_resolved',[0,1],[200,3000],[300,0.1])







dirname_='bin/AllMETHisto_3separatefiles_3Cats_25Vs45Vs43_2hdma_RP/'
files=[dirname_+'limits_monoHbb_2hdma_R_2017.root',
dirname_+'limits_monoHbb_2hdma_B_2017.root',
dirname_+'limits_monoHbb_2hdma_F_2017.root',
dirname_+'limits_monoHbb_2hdma_combined_2017.root']
legend=['Resolved', 'Boosted','low met resolved','Combined']
histoname1=['expmed']
xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_RP_3cat_different_files',[0,1],[200,3000],[300,0.1])

dirname_lowmet_up='bin/AllMETHistos_monohbb_v12_07_16_lowMETCat_25bins_UpdatedMetTrig_addedmettriun_2hdma_RP/'
dirname_lowmet='bin/AllMETHistos_monohbb_v12_07_16_lowMETCat_25bins_addedmettriun_2hdma_RP/'
dirname_43='bin/AllMETHistos_monohbb_v12_07_16_unrolled_43RVs61BRebinBinsHist_addedmettriun_2hdma_RP/'
dirname_='bin/AllMETHistos_monohbb_v12_07_16_3Cats_25Vs45Vs43_2hdma_RP/'
files=[
dirname_43+'limits_monoHbb_2hdma_R_2017.root',
dirname_lowmet+'limits_monoHbb_2hdma_R_2017.root',
dirname_lowmet_up+'limits_monoHbb_2hdma_R_2017.root',
dirname_+'limits_monoHbb_2hdma_F_2017.root'

#dirname_up+'limits_monoHbb_2hdma_combined_2017.root',

#dirname+'limits_monoHbb_2hdma_B_2017.root',
]

#legend=['Resolved(Pho)','Boosted(Pho)','Combined(Pho)','Resolved(data)','Boosted(data)','Combined(data)']
#legend=['Resolved(2bin)','Boosted(2bin)','Combined(2bin)' ,'Resolved(15bin)','Boosted(15bin)','Combined(15bin)' ]
legend=['43bin(R)', 'lowmet(R)','metsys(R)','lowmet combinedfile']
histoname1=['expmed']

xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_2hdma_RP_resolved_withcorr_metsys',[0,1],[200,3000],[300,0.1])


'''


'''
files=[dirname+'/AllMETHistos_monohbb_v12_07_07_NoddbOnZCR/limits_monoHbb_2hdma_B_2017.root', dirname+'/AllMETHistos_monohbb_v12_07_07_NoddbOnZCR_pdf20per/limits_monoHbb_2hdma_B_2017.root', dirname+'/AllMETHistos_monohbb_v12_07_07_NoddbOnZCR_pdf10per/limits_monoHbb_2hdma_B_2017.root']
legend=['shape', '20%', '10%']

histoname1=['expmed']

xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_monoHbb_2017_Boosted_pdfSyst_comparison',[0,1],[100,1600])

dirname='bin/'
files=[dirname+'/AllMETHistos_monohbb_v12_07_07_NoddbOnZCR/limits_monoHbb_2hdma_B_2017.root', dirname+'/AllMETHistos_monohbb_v12_07_07_NoddbOnZCR/limits_monoHbb_2hdma_R_2017.root', dirname+'/AllMETHistos_monohbb_v12_07_07_NoddbOnZCR/limits_monoHbb_2hdma_all_combined_2017.root']
legend=['Boosted', 'Resolved', 'Combined']

histoname1=['expmed']

xtitle='m_{A}[GeV]'
ytitle='#mu'
axistitle = [xtitle, ytitle]
DrawOverlap(files,histoname1,axistitle,legend,'limit_bbDM_2017_MET_comparison',[0,1],[100,1600])
'''


