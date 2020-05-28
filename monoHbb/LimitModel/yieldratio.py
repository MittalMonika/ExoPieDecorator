#created by Fasya Khuzaimah on 2020.05.01

## edited by Raman Khurana on 2020.05.11
##     - added commandline changing of rootfile name 
##     - made it compatibale for both Data and Asimov mode 
##     - directing the plots in required directory 
##     - added .png file for html viewing 

import ROOT
from ROOT import TFile, TH1F, TGraph, TGraphAsymmErrors


import PlotTemplates
from PlotTemplates import *

import array as arr

nbins = 4
edges = arr.array('f')


filename = sys.argv[1]
plotsdir = sys.argv[2]
postfix_ = sys.argv[3]

file_obj = TFile(filename)

postfix = ""

if "data" in  filename :
    postfix = "_Data"

if "asimov" in  filename :
    postfix = "_Asimov"

postfix = postfix + postfix_
#------------------------TOPE------------------------------#

Tope = "shapes_fit_b/TOPE/"

#get the histograms inside shapes_fit_b/TOPE
TopeDYjets = file_obj.Get(Tope+"dyjets")
for i in range(nbins):
    low = TopeDYjets.GetXaxis().GetBinLowEdge(i+1)
    edges.append(low)
up = TopeDYjets.GetXaxis().GetBinUpEdge(nbins)
edges.append(up)

Topedata = file_obj.Get(Tope+"data")
dataTope = TH1F("dataTope","",nbins,edges)
nPointsTope = Topedata.GetN()
for i in range(nPointsTope):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Topedata.GetPoint(i, x, y)
    k = dataTope.FindFixBin(x)
    dataTope.SetBinContent(k, y)
    dataTope.SetBinError(i+1, Topedata.GetErrorY(i))

Topediboson = file_obj.Get(Tope+"diboson")
TopeQCD = file_obj.Get(Tope+"qcd")
TopeST = file_obj.Get(Tope+"singlet")
TopeSMH = file_obj.Get(Tope+"smh")
TopeWjets = file_obj.Get(Tope+"wjets")
TopeTT = file_obj.Get(Tope+"tt")

tt_data_in_topE = dataTope - (Topediboson + TopeDYjets + TopeQCD + TopeST + TopeSMH + TopeWjets)


#------------------------TOPMU-----------------------------#

Topmu = "shapes_fit_b/TOPMU/"

#get the histograms inside shapes_fit_b/TOPMU
Topmudata = file_obj.Get(Topmu+"data")
dataTopmu = TH1F("dataTopmu","",nbins,edges)
nPointsTopmu = Topmudata.GetN()
for i in range(nPointsTopmu):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Topmudata.GetPoint(i, x, y)
    k = dataTopmu.FindFixBin(x)
    dataTopmu.SetBinContent(k,y)
    dataTopmu.SetBinError(i+1, Topmudata.GetErrorY(i))
Topmudiboson = file_obj.Get(Topmu+"diboson")
TopmuDYjets = file_obj.Get(Topmu+"dyjets")
TopmuQCD = file_obj.Get(Topmu+"qcd")
TopmuST = file_obj.Get(Topmu+"singlet")
TopmuSMH = file_obj.Get(Topmu+"smh")
TopmuWjets = file_obj.Get(Topmu+"wjets")
TopmuTT = file_obj.Get(Topmu+"tt")

tt_data_in_topMU = dataTopmu - (Topmudiboson + TopmuDYjets + TopmuQCD + TopmuST + TopmuSMH + TopmuWjets)


#------------------------WE------------------------------#

We = "shapes_fit_b/WE/"

#get the histograms inside shapes_fit_b/WE
WeDYjets = file_obj.Get(We+"dyjets")
for i in range(nbins):
    low = WeDYjets.GetXaxis().GetBinLowEdge(i+1)
    edges.append(low)
up = WeDYjets.GetXaxis().GetBinUpEdge(nbins)
edges.append(up)

Wedata = file_obj.Get(We+"data")
dataWe = TH1F("dataWe","",nbins,edges)
nPointsWe = Wedata.GetN()
for i in range(nPointsWe):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Wedata.GetPoint(i, x, y)
    k = dataWe.FindFixBin(x)
    dataWe.SetBinContent(k, y)
    dataWe.SetBinError(i+1, Wedata.GetErrorY(i))

Wediboson = file_obj.Get(We+"diboson")
WeQCD = file_obj.Get(We+"qcd")
WeST = file_obj.Get(We+"singlet")
WeSMH = file_obj.Get(We+"smh")
WeTT = file_obj.Get(We+"tt")
WeWjets = file_obj.Get(We+"wjets")

Wjets_data_in_WE = dataWe - (Wediboson + WeDYjets + WeQCD + WeST + WeSMH + WeTT)

#-----------------------WMU-----------------------------#

Wmu = "shapes_fit_b/WMU/"

#get the histograms inside shapes_fit_b/WMU
Wmudata = file_obj.Get(Wmu+"data")
dataWmu = TH1F("dataWmu","",nbins,edges)
nPointsWmu = Wmudata.GetN()
for i in range(nPointsWmu):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Wmudata.GetPoint(i, x, y)
    k = dataWmu.FindFixBin(x)
    dataWmu.SetBinContent(k,y)
    dataWmu.SetBinError(i+1, Wmudata.GetErrorY(i))
Wmudiboson = file_obj.Get(Wmu+"diboson")
WmuDYjets = file_obj.Get(Wmu+"dyjets")
WmuQCD = file_obj.Get(Wmu+"qcd")
WmuST = file_obj.Get(Wmu+"singlet")
WmuSMH = file_obj.Get(Wmu+"smh")
WmuTT = file_obj.Get(Wmu+"tt")
WmuWjets = file_obj.Get(Wmu+"wjets")


Wjets_data_in_WMU = dataWmu - (Wmudiboson + WmuDYjets + WmuQCD + WmuST + WmuSMH + WmuTT)


#------------------------ZEE------------------------------#

Zee = "shapes_fit_b/ZEE/"

#get the histograms inside shapes_fit_b/ZEE
ZeeDYjets = file_obj.Get(Zee+"dyjets")
for i in range(nbins):
    low = ZeeDYjets.GetXaxis().GetBinLowEdge(i+1)
    edges.append(low)
up = ZeeDYjets.GetXaxis().GetBinUpEdge(nbins)
edges.append(up)

Zeedata = file_obj.Get(Zee+"data")
dataZee = TH1F("dataZee","",nbins,edges)
nPointsZee = Zeedata.GetN()
for i in range(nPointsZee):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Zeedata.GetPoint(i, x, y)
    k = dataZee.FindFixBin(x)
    dataZee.SetBinContent(k, y)
    dataZee.SetBinError(i+1, Zeedata.GetErrorY(i))

Zeediboson = file_obj.Get(Zee+"diboson")
ZeeST = file_obj.Get(Zee+"singlet")
ZeeSMH = file_obj.Get(Zee+"smh")
ZeeTT = file_obj.Get(Zee+"tt")

'''
for i in range(nbins):
    ErrorWjet = WeWjets.GetBinError(i+1)
    print "W+jets error_",i+1, ErrorWjet
'''

DYjets_data_in_ZEE = dataZee - (Zeediboson + ZeeST + ZeeSMH + ZeeTT)

#-----------------------ZMUMU-----------------------------#

Zmumu = "shapes_fit_b/ZMUMU/"

#get the histograms inside shapes_fit_b/ZMUMU
Zmumudata = file_obj.Get(Zmumu+"data")
dataZmumu = TH1F("dataZmumu","",nbins,edges)
nPointsZmumu = Zmumudata.GetN()
for i in range(nPointsZmumu):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    Zmumudata.GetPoint(i, x, y)
    k = dataZmumu.FindFixBin(x)
    dataZmumu.SetBinContent(k,y)
    dataZmumu.SetBinError(i+1, Zmumudata.GetErrorY(i))
Zmumudiboson = file_obj.Get(Zmumu+"diboson")
ZmumuST = file_obj.Get(Zmumu+"singlet")
ZmumuSMH = file_obj.Get(Zmumu+"smh")
ZmumuTT = file_obj.Get(Zmumu+"tt")
ZmumuDYjets = file_obj.Get(Zmumu+"dyjets")


DYjets_data_in_ZMUMU = dataZmumu - (Zmumudiboson + ZmumuST + ZmumuSMH + ZmumuTT)

#----------------------SR-----------------------------------#

SR = "shapes_fit_b/SR/"

#get the histograms inside shapes_fit_b/SR
SRdata = file_obj.Get(SR+"data")
dataSR = TH1F("dataSR","",nbins,edges)
nPointsSR = SRdata.GetN()
for i in range(nPointsSR):
    x = ROOT.Double(0)
    y = ROOT.Double(0)
    SRdata.GetPoint(i, x, y)
    k = dataSR.FindFixBin(x)
    dataSR.SetBinContent(k,y)
    dataSR.SetBinError(i+1, SRdata.GetErrorY(i))
SRdiboson = file_obj.Get(SR+"diboson")
SRqcd = file_obj.Get(SR+"qcd")
SRst = file_obj.Get(SR+"singlet")
SRsmh = file_obj.Get(SR+"smh")
SRwjets = file_obj.Get(SR+"wjets")
SRzjets = file_obj.Get(SR+"zjets")
SRtt = file_obj.Get(SR+"tt")

tt_data_in_SR = dataSR - (SRdiboson + SRqcd + SRst + SRsmh + SRwjets + SRzjets)
Wjets_data_in_SR = dataSR - (SRdiboson + SRqcd + SRst + SRsmh + SRzjets +SRtt)
Zjets_data_in_SR = dataSR - (SRdiboson + SRqcd + SRst + SRsmh + SRwjets + SRtt)

#----------------------yield ratio--------------------------#

#*************TOP DATA****************#

yieldratioTopeData = tt_data_in_topE.Clone("yieldratioTopeData")
yieldratioTopmuData = tt_data_in_topMU.Clone("yieldratioTopmuData")
yieldratioTopeData.Divide(tt_data_in_SR)
yieldratioTopmuData.Divide(tt_data_in_SR)


#*************TOP MC****************#

yieldratioTopeMC = TopeTT.Clone("yieldratioTopeMC")
yieldratioTopmuMC = TopmuTT.Clone("yieldratioTopmuMC")
yieldratioTopeMC.Divide(SRtt)
yieldratioTopmuMC.Divide(SRtt)


#***********WJETS DATA*************#

yieldratioWeData = Wjets_data_in_WE.Clone("yieldratioWeData")
yieldratioWmuData = Wjets_data_in_WMU.Clone("yieldratioWmuData")
yieldratioWeData.Divide(Wjets_data_in_SR)#, 1.0, 1.0, "B")
yieldratioWmuData.Divide(Wjets_data_in_SR)#, 1.0, 1.0, "B")

#************WJETS MC*************#

yieldratioWeMC = WeWjets.Clone("yieldratioWeMC")
yieldratioWmuMC = WmuWjets.Clone("yieldratioWmuMC")
yieldratioWeMC.Divide(SRwjets)
yieldratioWmuMC.Divide(SRwjets)

#**********ZJETS DATA*************#

yieldratioZeeData = DYjets_data_in_ZEE.Clone("yieldratioZeeData")
yieldratioZmumuData = DYjets_data_in_ZMUMU.Clone("yieldratioZmumuData")
yieldratioZeeData.Divide(Zjets_data_in_SR)
yieldratioZmumuData.Divide(Zjets_data_in_SR)

#***********ZJETS MC************#

yieldratioZeeMC = ZeeDYjets.Clone("yieldratioZeeMC")
yieldratioZmumuMC = ZmumuDYjets.Clone("yieldratioZmumuMC")
yieldratioZeeMC.Divide(SRzjets)
yieldratioZmumuMC.Divide(SRzjets)



#-----------------Plot the yield ratio----------------#

yminTop = 0.0
ymaxTop = 10.0
yminW = -6.0
ymaxW = 9.0
yminZ = 0.0
ymaxZ = 18.0

def drawenergy(is2017 = True, text_=" Internal", data = True):
    pt = TPaveText(0.0877181,0.9,0.9580537,0.96,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(52)
    
    cmstextSize = 0.07
    preliminarytextfize = cmstextSize * 0.7
    lumitextsize = cmstextSize *0.7
    pt.SetTextSize(cmstextSize)
    text = pt.AddText(0.01,0.57,"#font[61]{CMS}")
    
    pt1 = TPaveText(0.0877181,0.904,0.9580537,0.96,"brNDC")
    pt1.SetBorderSize(0)
    pt1.SetTextAlign(12)
    pt1.SetFillStyle(0)
    pt1.SetTextFont(52)
    
    pt1.SetTextSize(preliminarytextfize)
    #text1 = pt1.AddText(0.155,0.4,"Preliminary")
    text1 = pt1.AddText(0.125,0.4,text_)
    
    pt2 = TPaveText(0.0877181,0.9,0.7280537,0.96,"brNDC")
    pt2.SetBorderSize(0)
    pt2.SetTextAlign(12)
    pt2.SetFillStyle(0)
    pt2.SetTextFont(52)
    pt2.SetTextFont(42)
    pt2.SetTextSize(lumitextsize)
    
    pavetext = ''
    if is2017 and data: pavetext = "41.1 fb^{-1} (13 TeV)"
    if (not is2017) and data: pavetext = "(13 TeV)"
    
    if is2017 and not data: pavetext = "(13 TeV)"
    if (not is2017) and not data: pavetext = "(13 TeV)"
    
    if data: text3 = pt2.AddText(0.735,0.5,pavetext)
    if not data: text3 = pt2.AddText(0.75,0.5,pavetext)
    
    return [pt,pt1,pt2]

#************* TOPE ****************#

c1 = PlotTemplates.myCanvas()

h_yieldratioTopeData = PlotTemplates.Save1DHisto(yieldratioTopeData, c1, "Recoil", "Yield Ratio (TopE/tt)")
h_yieldratioTopeData.SetMaximum(ymaxTop)
h_yieldratioTopeData.SetMinimum(yminTop)
h_yieldratioTopeData.SetMarkerStyle(20)
h_yieldratioTopeData.SetLineWidth(2)

h_yieldratioTopeMC = PlotTemplates.Save1DHisto(yieldratioTopeMC, c1, "Recoil", "Yield Ratio (TopE/tt)")
h_yieldratioTopeMC.SetMaximum(ymaxTop)
h_yieldratioTopeMC.SetMinimum(yminTop)
#h_yieldratioTopeMC.SetMarkerStyle(21)
#h_yieldratioTopeMC.SetMarkerColor(2)
h_yieldratioTopeMC.SetLineColor(2)
h_yieldratioTopeMC.SetLineWidth(3)

h_yieldratioTopeMC.Draw("e1")
h_yieldratioTopeData.Draw("e1same")

leg1 = PlotTemplates.SetLegend()
leg1.AddEntry(h_yieldratioTopeMC, "MC")
leg1.AddEntry(yieldratioTopeData, "Data")
leg1.Draw()
E1 = drawenergy()
for i in E1:
    i.Draw()

c1.SaveAs(plotsdir+"Tope_YieldRatio"+postfix+".pdf")
c1.SaveAs(plotsdir+"Tope_YieldRatio"+postfix+".png")
c1.SaveAs(plotsdir+"Tope_YieldRatio"+postfix+".root")
c1.SaveAs(plotsdir+"Tope_YieldRatio"+postfix+".C")


#************* TOPMU ****************#

c2 = PlotTemplates.myCanvas()

h_yieldratioTopmuData = PlotTemplates.Save1DHisto(yieldratioTopmuData, c2, "Recoil", "Yield Ratio (TopMu/tt)")
h_yieldratioTopmuData.SetMaximum(ymaxTop)
h_yieldratioTopmuData.SetMinimum(yminTop)
h_yieldratioTopmuData.SetMarkerStyle(20)
h_yieldratioTopmuData.SetLineWidth(2)

h_yieldratioTopmuMC = PlotTemplates.Save1DHisto(yieldratioTopmuMC, c2, "Recoil", "Yield Ratio (TopMu/tt)")
h_yieldratioTopmuMC.SetMaximum(ymaxTop)
h_yieldratioTopmuMC.SetMinimum(yminTop)
#h_yieldratioTopmuMC.SetMarkerStyle(21)
#h_yieldratioTopmuMC.SetMarkerColor(2)
h_yieldratioTopmuMC.SetLineColor(2)
h_yieldratioTopmuMC.SetLineWidth(3)

h_yieldratioTopmuMC.Draw("e1")
h_yieldratioTopmuData.Draw("e1same")

leg2 = PlotTemplates.SetLegend()
leg2.AddEntry(h_yieldratioTopmuMC, "MC")
leg2.AddEntry(yieldratioTopmuData, "Data")
leg2.Draw()
E2 = drawenergy()
for i in E2:
    i.Draw()

c2.SaveAs(plotsdir+"Topmu_YieldRatio"+postfix+".pdf")
c2.SaveAs(plotsdir+"Topmu_YieldRatio"+postfix+".png")
c2.SaveAs(plotsdir+"Topmu_YieldRatio"+postfix+".root")
c2.SaveAs(plotsdir+"Topmu_YieldRatio"+postfix+".C")


#************* WE ****************#

c3 = PlotTemplates.myCanvas()

h_yieldratioWeData = PlotTemplates.Save1DHisto(yieldratioWeData, c3, "Recoil", "Yield Ratio (We/WJets)")
h_yieldratioWeData.SetMaximum(ymaxW)
h_yieldratioWeData.SetMinimum(yminW)
h_yieldratioWeData.SetMarkerStyle(20)
h_yieldratioWeData.SetLineWidth(2)

h_yieldratioWeMC = PlotTemplates.Save1DHisto(yieldratioWeMC, c3, "Recoil", "Yield Ratio (We/WJets)")
h_yieldratioWeMC.SetMaximum(ymaxW)
h_yieldratioWeMC.SetMinimum(yminW)
#h_yieldratioWeMC.SetMarkerStyle(21)
#h_yieldratioWeMC.SetMarkerColor(2)
h_yieldratioWeMC.SetLineColor(2)
h_yieldratioWeMC.SetLineWidth(3)

h_yieldratioWeMC.Draw("e1")
h_yieldratioWeData.Draw("e1same")

leg3 = PlotTemplates.SetLegend()
leg3.AddEntry(h_yieldratioWeMC, "MC")
leg3.AddEntry(yieldratioWeData, "Data")
leg3.Draw()
E3 = drawenergy()
for i in E3:
    i.Draw()

c3.SaveAs(plotsdir+"We_YieldRatio"+postfix+".pdf")
c3.SaveAs(plotsdir+"We_YieldRatio"+postfix+".png")
c3.SaveAs(plotsdir+"We_YieldRatio"+postfix+".C")
c3.SaveAs(plotsdir+"We_YieldRatio"+postfix+".root")


#************* WMU ****************#

c4 = PlotTemplates.myCanvas()

h_yieldratioWmuData = PlotTemplates.Save1DHisto(yieldratioWmuData, c4, "Recoil", "Yield Ratio (Wmu/WJets)")
h_yieldratioWmuData.SetMaximum(ymaxW)
h_yieldratioWmuData.SetMinimum(yminW)
h_yieldratioWmuData.SetMarkerStyle(20)
h_yieldratioWmuData.SetLineWidth(2)

h_yieldratioWmuMC = PlotTemplates.Save1DHisto(yieldratioWmuMC, c4, "Recoil", "Yield Ratio (Wmu/WJets)")
h_yieldratioWmuMC.SetMaximum(ymaxW)
h_yieldratioWmuMC.SetMinimum(yminW)
#h_yieldratioWmuMC.SetMarkerStyle(21)
#h_yieldratioWmuMC.SetMarkerColor(2)
h_yieldratioWmuMC.SetLineColor(2)
h_yieldratioWmuMC.SetLineWidth(3)

h_yieldratioWmuMC.Draw("e1")
h_yieldratioWmuData.Draw("e1same")

leg4 = PlotTemplates.SetLegend()
leg4.AddEntry(h_yieldratioWmuMC, "MC")
leg4.AddEntry(yieldratioWmuData, "Data")
leg4.Draw()
E4 = drawenergy()
for i in E4:
    i.Draw()

c4.SaveAs(plotsdir+"Wmu_YieldRatio"+postfix+".pdf")
c4.SaveAs(plotsdir+"Wmu_YieldRatio"+postfix+".png")
c4.SaveAs(plotsdir+"Wmu_YieldRatio"+postfix+".root")
c4.SaveAs(plotsdir+"Wmu_YieldRatio"+postfix+".C")


#************* ZEE ****************#

c5 = PlotTemplates.myCanvas()

h_yieldratioZeeData = PlotTemplates.Save1DHisto(yieldratioZeeData, c5, "Recoil", "Yield Ratio (Zee/ZJets)")
h_yieldratioZeeData.SetMaximum(ymaxZ)
h_yieldratioZeeData.SetMinimum(yminZ)
h_yieldratioZeeData.SetMarkerStyle(20)
h_yieldratioZeeData.SetLineWidth(2)

h_yieldratioZeeMC = PlotTemplates.Save1DHisto(yieldratioZeeMC, c5, "Recoil", "Yield Ratio (Zee/ZJets)")
h_yieldratioZeeMC.SetMaximum(ymaxZ)
h_yieldratioZeeMC.SetMinimum(yminZ)
#h_yieldratioZeeMC.SetMarkerStyle(21)
#h_yieldratioZeeMC.SetMarkerColor(2)
h_yieldratioZeeMC.SetLineColor(2)
h_yieldratioZeeMC.SetLineWidth(3)

h_yieldratioZeeMC.Draw("e1")
h_yieldratioZeeData.Draw("e1same")

leg5 = PlotTemplates.SetLegend()
leg5.AddEntry(h_yieldratioZeeMC, "MC")
leg5.AddEntry(h_yieldratioZeeData, "Data")
leg5.Draw()
E5 = drawenergy()
for i in E5:
    i.Draw()

c5.SaveAs(plotsdir+"Zee_YieldRatio"+postfix+".pdf")
c5.SaveAs(plotsdir+"Zee_YieldRatio"+postfix+".png")
c5.SaveAs(plotsdir+"Zee_YieldRatio"+postfix+".root")
c5.SaveAs(plotsdir+"Zee_YieldRatio"+postfix+".C")


#************* ZMUMU ****************#

c6 = PlotTemplates.myCanvas()

h_yieldratioZmumuData = PlotTemplates.Save1DHisto(yieldratioZmumuData, c6, "Recoil", "Yield Ratio (Zmumu/ZJets)")
h_yieldratioZmumuData.SetMaximum(ymaxZ)
h_yieldratioZmumuData.SetMinimum(yminZ)
h_yieldratioZmumuData.SetMarkerStyle(20)
h_yieldratioZmumuData.SetLineWidth(2)

h_yieldratioZmumuMC = PlotTemplates.Save1DHisto(yieldratioZmumuMC, c6, "Recoil", "Yield Ratio (Zmumu/ZJets)")
h_yieldratioZmumuMC.SetMaximum(ymaxZ)
h_yieldratioZmumuMC.SetMinimum(yminZ)
#h_yieldratioZmumuMC.SetMarkerStyle(21)
#h_yieldratioZmumuMC.SetMarkerColor(2)
h_yieldratioZmumuMC.SetLineColor(2)
h_yieldratioZmumuMC.SetLineWidth(3)

h_yieldratioZmumuMC.Draw("e1")
h_yieldratioZmumuData.Draw("e1same")

leg6 = PlotTemplates.SetLegend()
leg6.AddEntry(h_yieldratioZmumuMC, "MC")
leg6.AddEntry(h_yieldratioZmumuData, "Data")
leg6.Draw()
E6 = drawenergy()
for i in E6:
    i.Draw()

c6.SaveAs(plotsdir+"Zmumu_YieldRatio"+postfix+".pdf")
c6.SaveAs(plotsdir+"Zmumu_YieldRatio"+postfix+".png")
c6.SaveAs(plotsdir+"Zmumu_YieldRatio"+postfix+".root")
c6.SaveAs(plotsdir+"Zmumu_YieldRatio"+postfix+".C")

