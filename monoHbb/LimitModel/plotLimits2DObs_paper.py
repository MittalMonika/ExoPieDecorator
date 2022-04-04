from ROOT import TCanvas, TGraph, TGraphAsymmErrors, TLegend, TLatex, TFile, TTree, TH2D, TGraph2D, TGraphSmooth
import ROOT as root
from array import array
from sys import argv,stdout,exit
from tdrStyle import *
import plotConfig
from glob import glob 
from collections import namedtuple

root.gROOT.SetBatch(1)


import sys, optparse

usage = "usage: %prog [options] "
parser = optparse.OptionParser(usage)

parser.add_option("-t", "--thdm", action="store_true", dest="thdm")
parser.add_option("-b", "--zpb", action="store_true", dest="zpb")

(options, args) = parser.parse_args()
dosmooth = 'false'

root.gStyle.SetNumberContours(505);                                                                                                                                            
root.gStyle.SetPalette(57)
#root.TColor.InvertPalette();

setTDRStyle()

XSECUNCERT=0.1
VERBOSE=False

drawLegend=True

iC=0

def get_contours(h2, cold):
  ctmp = TCanvas()
  ctmp.cd()
  h2.Draw("contlist")
  ctmp.Update()

  conts = root.gROOT.GetListOfSpecials().FindObject("contours")
  graphs = []
  for ib in xrange(conts.GetSize()):
    l = conts.At(ib)
    #graph = root.TGraph(l.First())
    graph = l.First()
    if not graph:
      continue
    graph = root.TGraph(graph) # clone
    graph.SetLineColor(h2.GetLineColor())
    graph.SetLineWidth(h2.GetLineWidth())
    graph.SetLineStyle(h2.GetLineStyle())
    graphs.append(graph)

  cold.cd()
  return graphs

L = namedtuple('L', ['mMed','mChi','down2','down1','cent','up1','up2','obs'])

def parseLimitFiles2D(filepath):
  # returns a dict (mMed,mChi) : Limit
  # if xsecs=None, Limit will have absolute xsec
  # if xsecs=dict of xsecs, Limit will have mu values
  limits = {}
  flist = list(open(filepath, 'r').readlines())
  for line in flist[1:]:
    l = L(*map(float, line.strip().split()))
    limits[(l.mMed , l.mChi )] = l
  print 'Successfully parsed %i points'%(len(limits))
  print (limits)
  return limits

def makePlot2D(filepath,foutname,medcfg,chicfg,header='',offshell=False):
  limits = parseLimitFiles2D(filepath)
  gs = {}
  for g in ['exp','expup','expdown','obs','obsup','obsdown','expup2','expdown2']:
    gs[g] = TGraph2D()

  iP=0
  hgrid = TH2D('grid','grid',medcfg[0],medcfg[1],medcfg[2],chicfg[0],chicfg[1],chicfg[2])
  for p in limits:
    mMed = p[0]; mChi = p[1]
    l = limits[p]
    if l.obs==0 or l.cent==0:
      print mMed,mChi
      continue
    hgrid.Fill(mMed,mChi,100)
    gs['exp'].SetPoint(iP,mMed,mChi,l.cent)
    gs['expup'].SetPoint(iP,mMed,mChi,l.up1)
    gs['expdown'].SetPoint(iP,mMed,mChi,l.down1)
    gs['obs'].SetPoint(iP,mMed,mChi,l.obs)
    gs['obsup'].SetPoint(iP,mMed,mChi,l.obs/(1-XSECUNCERT))
    gs['obsdown'].SetPoint(iP,mMed,mChi,l.obs/(1+XSECUNCERT))
    gs['expup2'].SetPoint(iP,mMed,mChi,l.up2)
    gs['expdown2'].SetPoint(iP,mMed,mChi,l.down2)

    iP += 1

  hs = {}
  for h in ['exp','expup','expdown','obs','obsup','obsdown','expup2','expdown2']:
    hs[h] = TH2D(h,h,medcfg[0],medcfg[1],medcfg[2],chicfg[0],chicfg[1],chicfg[2])
    # hs[h].SetStats(0); hs[h].SetTitle('')
    for iX in xrange(0,medcfg[0]):
      for iY in xrange(0,chicfg[0]):
        x = medcfg[1] + (medcfg[2]-medcfg[1])*iX/medcfg[0]
        y = chicfg[1] + (chicfg[2]-chicfg[1])*iY/chicfg[0]
        if not(offshell) and 2*y>x:
          val = 9999
        else:
          val = gs[h].Interpolate(x,y)
        if val == 0:
          val = 9999
          

        if options.thdm:
          if  (125+y) > x:
            val = 9999
            #print "inside offshell", x, y
          else:
            val = gs[h].Interpolate(x,y)
          if val == 0:
            val = 9999
            
          if iX == 115 and iY == 61:
            val = 1.09
          if iX == 121 and iY == 61:
            val = 1.17
          if iX == 161 and iY == 61:
            val = 2.53
          if iX == 181 and iY == 61:
            val = 4.36
          if iX == 182 and iY == 61:
            val = 4.51            
        val = max(0.01,min(100,val))
        hs[h].SetBinContent(iX+1,iY+1,val)

#  hs['obs'].Smooth()
  hs['obsclone'] = hs['obs'].Clone() # clone it so we can draw with different settings
  for h in ['exp','expup','expdown','obsclone','obsup','obsdown','expup2','expdown2']:
    hs[h].SetContour(2)
    hs[h].SetContourLevel(1,1)
    for iX in xrange(1,medcfg[0]+1):
      for iY in xrange(1,chicfg[0]+1):
        if hs[h].GetBinContent(iX,iY)<=0:
          hs[h].SetBinContent(iX,iY,100)

  


  global iC
  canvas = ROOT.TCanvas("canvas%i"%iC, '',  1000, 800)
  canvas.SetLogz()
 # canvas.SetLeftMargin(0.12)
 # canvas.SetRightMargin(0.06)
#  canvas.SetBottomMargin(0.04)
 #OB canvas.SetTopMargin(0.08)  
  iC+=1

  frame = canvas.DrawFrame(medcfg[1],chicfg[1],medcfg[2],chicfg[2],"")

#  frame.GetYaxis().CenterTitle();
  #frame.GetYaxis().SetTitle("m_{A} [TeV]");
  if options.thdm: frame.GetYaxis().SetTitle("m_{A} [GeV]");
  if options.zpb:  frame.GetYaxis().SetTitle("m_{#chi} [GeV]");
  frame.GetXaxis().SetTitle("m_{Z'} [GeV]");
  frame.GetXaxis().SetTitleOffset(1.1);

  frame.GetXaxis().SetTitleFont(42);
  frame.GetXaxis().SetLabelFont(42);
  frame.GetYaxis().SetTitleFont(42);
  frame.GetYaxis().SetLabelFont(42);

  frame.GetXaxis().SetLabelSize(.047);
  frame.GetYaxis().SetLabelSize(.047);
  frame.GetYaxis().SetTitleSize(.047);
  frame.GetXaxis().SetTitleSize(.047);

  frame.GetYaxis().SetTitleOffset(1.25);
#  frame.GetXaxis().SetNdivisions(5)

  frame.Draw()

  htest = hs['exp']

  obs_color = root.kOrange

  hs['obs'].SetMinimum(0.01)
  hs['obs'].SetMaximum(100.)

  hs['obs'].GetZaxis().SetTitle("#sigma_{95% CL}/#sigma_{th}"); # we can now remove the box and use this axis to draw the axis title. 
  hs['obs'].GetZaxis().SetTitleFont(42);
  hs['obs'].GetZaxis().SetLabelFont(42);
  hs['obs'].GetZaxis().SetLabelSize(.047);
  hs['obs'].GetZaxis().SetTitleSize(.049);
  hs['obs'].GetZaxis().SetTitleOffset(0.90);
  hs['obs'].GetZaxis().SetLabelOffset(0.001);
  hs['obs'].Draw("COLZ SAME")


  '''
  hs['obsclone'].SetLineStyle(1)
  hs['obsclone'].SetLineWidth(3)
  hs['obsclone'].SetLineColor(obs_color)
  hs['obsclone'].Draw('CONT3 SAME')
  
  '''
  conts = {}

  if dosmooth: hs['obsclone'].Smooth()  
  conts['obsclone'] = get_contours(hs['obsclone'], canvas)[0]
  if dosmooth:
    graphsSmooth1 = TGraphSmooth("normal")
    graphsSmooth_approx1 = graphsSmooth1.Approx(conts['obsclone'], "linear")
    conts['obsclone'] = graphsSmooth_approx1

  conts['obsclone'].SetLineStyle(1)
  conts['obsclone'].SetLineWidth(2)
  conts['obsclone'].SetLineColor(2)
  conts['obsclone'].Draw("L SAME")

  
  
  ctemp = root.TCanvas()
  hs['obsclone'].Draw('contlist')
  ctemp.Update()
  objs = root.gROOT.GetListOfSpecials().FindObject('contours')
  saveobs = root.TGraph((objs.At(0)).First())

  canvas.cd()

  root.gStyle.SetLineStyleString(11, '40 80')

  
  hs['obsup'].SetLineStyle(3)
  hs['obsup'].SetLineWidth(2)
  hs['obsup'].SetLineColor(obs_color)
  conts['obsup'] = get_contours(hs['obsup'], canvas)[0]
  conts['obsup'].SetLineStyle(3)
  conts['obsup'].SetLineWidth(2)
  conts['obsup'].SetLineColor(2)
  conts['obsup'].Draw('L SAME')
#  hs['obsup'].Draw('CONT3 SAME')

  hs['obsdown'].SetLineStyle(3)
  hs['obsdown'].SetLineWidth(2)
  hs['obsdown'].SetLineColor(obs_color)
  conts['obsdown'] = get_contours(hs['obsdown'], canvas)[0]
  conts['obsdown'].SetLineStyle(3)
  conts['obsdown'].SetLineWidth(2)
  conts['obsdown'].SetLineColor(2)
  conts['obsdown'].Draw('L SAME')
  #hs['obsdown'].Draw('CONT3 SAME')

  hs['exp'].SetLineStyle(1)
  hs['exp'].SetLineWidth(2)
  hs['exp'].SetLineColor(1)
  #####hs['exp'].Draw('CONT3 SAME')
 
  if dosmooth:  hs['exp'].Smooth()
  conts['exp'] = get_contours(hs['exp'], canvas)[0]

  if dosmooth:
    graphsSmooth2 = TGraphSmooth("normal")
    graphsSmooth_approx2 = graphsSmooth2.Approx(conts['exp'], "linear")
    conts['exp'] = graphsSmooth_approx2

  conts['exp'].SetLineStyle(1)
  conts['exp'].SetLineWidth(2)
  conts['exp'].SetLineColor(1)
  conts['exp'].Draw('CONT3 SAME')

  hs['expup'].SetLineStyle(3)
  hs['expup'].SetLineWidth(2)
  hs['expup'].SetLineColor(1)
  conts['expup'] = get_contours(hs['expup'], canvas)[0]
  conts['expup'].SetLineStyle(3)
  conts['expup'].SetLineWidth(2)
  conts['expup'].SetLineColor(1)
  

  conts['expup'].Draw('L SAME')




  hs['expup2'].SetLineStyle(3)
  hs['expup2'].SetLineWidth(2)
  hs['expup2'].SetLineColor(1)
  conts['expup2'] = get_contours(hs['expup2'], canvas)[0]
  conts['expup2'].SetLineStyle(4)
  conts['expup2'].SetLineWidth(2)
  conts['expup2'].SetLineColor(1)
  

 
  #hs['expup'].Draw('CONT3 SAME')

  hs['expdown'].SetLineStyle(3)
  hs['expdown'].SetLineWidth(2)
  hs['expdown'].SetLineColor(1)
  conts['expdown'] = get_contours(hs['expdown'], canvas)[0]
  conts['expdown'].SetLineStyle(3)
  conts['expdown'].SetLineWidth(2)
  conts['expdown'].SetLineColor(1)
  conts['expdown'].Draw('L SAME')

  hs['expdown2'].SetLineStyle(6)
  hs['expdown2'].SetLineWidth(2)
  hs['expdown2'].SetLineColor(1)
  conts['expdown2'] = get_contours(hs['expdown2'], canvas)[0]
  conts['expdown2'].SetLineStyle(4)
  conts['expdown2'].SetLineWidth(2)
  conts['expdown2'].SetLineColor(1)
  #hs['expdown2'].Draw('CONT3 SAME')
#2sigma
  if options.thdm:
    conts['expup2'].Draw('L SAME')
    conts['expdown2'].Draw('L SAME')
 


  graphroot = TFile("limitGraphs2HDMComboTanBeta.root","RECREATE")
  graphroot.cd()
  h_exp = conts['exp']
  h_exp.SetName("expected_curve")
  h_exp.Write()  
  #conts['exp'].Write()
  
  conts['expup'].Write()
  conts['expdown'].Write()
  conts['expup2'].Write()
  conts['expdown2'].Write()
  #conts['obsclone'].Write()
  
  h_obs = conts['obsclone']
  h_obs.SetName("observed_curve")
  h_obs.Write()

  conts['obsup'].Write()
  conts['obsdown'].Write()

  



  if drawLegend:
#2sigma
    leg = root.TLegend(0.53,0.67,0.84,0.86);#,NULL,"brNDC");
#    leg = root.TLegend(0.60,0.72,0.84,0.91);#,NULL,"brNDC");
#    leg.SetHeader(" DM + h(b#bar{b} + #gamma#gamma + #tau#tau + WW + ZZ)","C")
    leg.AddEntry(conts['obsclone'],"Observed 95% CL","L");

    leg.AddEntry(conts['obsup']," #pm 1 s.d._{theory}","L");
    leg.AddEntry(conts['exp'],"Expected 95% CL","L");

#2sigma  
    leg.AddEntry(conts['expup']," #pm 1 s.d.","L");
    leg.AddEntry(conts['expup2']," #pm 2 s.d.","L");

    leg.SetTextFont(42);
    leg.SetTextSize(0.0385);
    leg.SetFillColor(0); leg.SetBorderSize(0)
    leg.Draw("SAME");

  tex = root.TLatex();
  tex.SetNDC();
  tex.SetTextFont(42);
  tex.SetTextAlign(11);
  tex.SetTextSize(0.045);
  tex.SetTextAlign(31);
  tex.Draw();
  tex.DrawLatex(0.85,0.93,"35.9 fb^{-1} (13 TeV)");

  coupling = root.TLatex();
  coupling.SetNDC();
  coupling.SetTextFont(42);
  coupling.SetTextAlign(11);
  coupling.SetTextSize(0.0385);
  coupling.SetTextAlign(31);
  #coupling.SetLineWidth(2);
  #coupling.SetTextSize(0.025);
  coupling.SetTextColor(1);
  coupling.Draw();
  if options.thdm: 
    coupling.DrawLatex(0.387, 0.87, "Z'-2HDM, Dirac DM");
    coupling.DrawLatex(0.328, 0.84,"g_{Z'} = 0.8, g_{#chi} = 1");
    coupling.DrawLatex(0.316, 0.795,"m_{#chi} = 100 GeV");
    coupling.DrawLatex(0.238, 0.76, "tan#beta = 1");
    coupling.DrawLatex(0.320, 0.728,"m_{A} = m_{H^{#pm}} = m_{H}");
    coupling.DrawLatex(0.84, 0.87," DM + h(b#bar{b} + #gamma#gamma + #tau#tau + WW + ZZ)")

#    coupling.DrawLatex(0.337, 0.83, "Z'-2HDM, Dirac DM");
#    coupling.DrawLatex(0.288, 0.80,"g_{Z'} = 0.8, g_{#chi} = 1");
#    coupling.DrawLatex(0.286, 0.76,"m_{#chi} = 100 GeV");
#    coupling.DrawLatex(0.22, 0.725, "tan#beta = 1");
#    coupling.DrawLatex(0.285, 0.695,"m_{A} = m_{H^{#pm}} = m_{H}");
  if options.zpb: 
    coupling.DrawLatex(0.25, 0.83, "Baryonic Z'");
#    coupling.DrawLatex(0.405, 0.79, "Z'#rightarrow DM+h(bb+#gamma#gamma+#tau#tau+WW+ZZ)");
    coupling.DrawLatex(0.395, 0.79, "Dirac DM, g_{q} = 0.25, g_{#chi} = 1");




  tex2 = root.TLatex();
  tex2.SetNDC();
  tex2.SetTextFont(42);
  tex2.SetLineWidth(2);
  tex2.SetTextSize(0.04);
  tex2.SetTextAngle(90);
  tex2.SetTextAlign(33)
#  tex2.DrawLatex(.96,0.93," #sigma_{95% CL}/#sigma_{theory}");
#  tex2.DrawLatex(.96,0.93," #sigma_{95% CL}/#sigma_{th}");


  latex =  TLatex();
  latex.SetNDC();
  latex.SetTextSize(0.066);
  latex.SetTextAlign(31);
  latex.SetTextAlign(11);
  latex.DrawLatex(0.14, 0.93, "CMS");
  latexP =  TLatex();
  latexP.SetNDC();
  latexP.SetTextSize(0.05);
  latexP.SetTextAlign(31);
  latexP.SetTextAlign(11);
  latexP.SetTextFont(52);
#  latexP.DrawLatex(0.225, 0.87, "Preliminary");
         
  root.gPad.SetRightMargin(0.15);
  root.gPad.SetTopMargin(0.08);
  root.gPad.SetBottomMargin(0.12);
  root.gPad.RedrawAxis();
  root.gPad.Modified(); 
  root.gPad.Update();

  canvas.SaveAs(foutname+'.png')
  canvas.SaveAs(foutname+'.pdf')
  
  texPrelim = root.TLatex(0.2,0.94,"");
  texPrelim.SetNDC();
  texPrelim.SetTextFont(42);
  texPrelim.SetLineWidth(2);
  texPrelim.SetTextSize(0.05); texPrelim.Draw();

  canvas.SaveAs(foutname+'_prelim.png')
  canvas.SaveAs(foutname+'_prelim.pdf')
  
  canvas.SetGrid()
#  canvas.SetGridY()
#  canvas.SetGridX()
  hgrid.GetXaxis().SetNdivisions(32);
  hgrid.GetYaxis().SetNdivisions(32);
  hgrid.GetXaxis().SetLabelSize(0.014);
  hgrid.GetYaxis().SetLabelSize(0.02);
  hgrid.Draw('BOX')
  hs['obsup'].Draw('CONT3 SAME')

  hs['obsdown'].Draw('CONT3 SAME')

  hs['exp'].Draw('CONT3 SAME')

  hs['expup'].Draw('CONT3 SAME')

  hs['expdown'].Draw('CONT3 SAME')

  canvas.SaveAs(foutname+'_grid.png')
  canvas.SaveAs(foutname+'_grid.pdf')

  fsave = root.TFile(foutname+'.root','RECREATE')
  fsave.WriteTObject(hs['obs'],'hobserved')
  fsave.WriteTObject(gs['obs'],'gobserved')
  fsave.WriteTObject(hs['exp'],'hexp')
  fsave.WriteTObject(gs['exp'],'gexp')
  fsave.WriteTObject(saveobs,'observed')
  fsave.Close()
#  canvas.SaveAs(foutname+'.C')

plotsdir = plotConfig.plotDir

#makePlot2D('refined_limits.txt',plotsdir+'/test',(100,0.011,2.0),(100,0.0011,0.7),'Test',True)

#''' for monoh bb '''
#makePlot2D('limits_barzp_cleaned_NoDuplicate.txt',plotsdir+'/test',(100,0.011,2.0),(100,0.0011,0.7),"Z'-Baryonic",True)

''' for mono-h combination '''
if options.thdm:

#use for final reading
#  makePlot2D('limits_2hdm_combo_scaled_cleaned_NoDuplicate_v2.txt',plotsdir+'/limit2d_2hdm_combo_',(200,450,4000),(100,301,1002),'Z`-2HDM',True)
  makePlot2D('bin/scan_2d/limits_monoHbb_2hdmaScan_ma_vs_mA_tanbeta_1p0_sinth_0p35.txt','limit2d_2hdm_combo_',(200,200,1600),(10,100,400),'2HDM+a',True)
