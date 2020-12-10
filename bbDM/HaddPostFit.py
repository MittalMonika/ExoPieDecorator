from ROOT import TFile, TH1F, TGraphAsymmErrors
import ROOT
import os,traceback
import sys, optparse,argparse
import glob
import array as arr



baseDirs=["shapes_fit_b","shapes_prefit"]

regionlist = ["SR", "TOPE", "TOPMU", "WE", "WMU", "ZEE", "ZMUMU"]
regionlist_1b=["cat_1b_"+ir for ir in regionlist]
regionlist_2b=["cat_2b_"+ir for ir in regionlist]
regionlist = regionlist_1b + regionlist_2b                                                                                                                                                                

prefitbkglist = ["diboson", "qcd", "singlet", "smh", "tt", "wjets", "zjets","dyjets","signal","total","total_signal","total_background","data"]

files=["run2_postfit/fitDiagnostics_combined_2016_data.root","run2_postfit/fitDiagnostics_combined_2017_data.root","run2_postfit/fitDiagnostics_combined_2018_data.root"]
outfile= "run2_postfit/run2_fitDiagnostics_combined_140fbinv.root"


f1 = TFile(files[0])
f2 = TFile(files[1])
f3 = TFile(files[2])
fout = TFile(outfile,"RECREATE")

nbins = 4
edges = arr.array('f')


edges = arr.array('f')
for i in range(nbins):
    bkg = f1.Get("shapes_prefit/cat_2b_ZEE/singlet")
    low = bkg.GetXaxis().GetBinLowEdge(i+1)
    edges.append(low)
up = bkg.GetXaxis().GetBinUpEdge(nbins)
edges.append(up)

print edges    
def graphToTH1F(data):
    data_ = TH1F("data_","",nbins,edges)
    nPoints = data.GetN()
    for i in range(nPoints):
        x = ROOT.Double(0)
        y = ROOT.Double(0)
        data.GetPoint(i, x, y)
        k = data_.FindFixBin(x)
        data_.SetBinContent(k, y)
        data_.SetBinError(i+1, data.GetErrorY(i))
        #data_.SetName("data")
    return data_


for iDirs in baseDirs:
    fout.mkdir(iDirs)
    for iregion in regionlist:
        fout.mkdir(iDirs+"/"+iregion)
        for iprocess in prefitbkglist:
            outdir = iDirs+"/"+iregion
            histname = iDirs+"/"+iregion+"/"+iprocess
            print (iDirs+"/"+iregion+"/"+iprocess)
            h1= f1.Get(histname)
            h2= f2.Get(histname)
            h3= f3.Get(histname)
            if h1:
                print h1.Integral()
                print h2.Integral()
                print h3.Integral()
                print (h1.GetName())
                print type(h1)
                if type(h1) is  TH1F:
                    hout = h1.Clone()
                    print ("merging TH1F")
                    hout.Add(h2)
                    hout.Add(h3)
                    fout.cd(outdir)
                    hout.Write()
                if type(h1) is TGraphAsymmErrors:
                    print ("merging TGraphAsymmErrors")
                    h1_d = graphToTH1F(h1)
                    h2_d = graphToTH1F(h2)
                    h3_d = graphToTH1F(h3)
                    hout = h1_d.Clone()
                    hout.Add(h2_d)
                    hout.Add(h3_d)
                    hout.SetName("data")
                    hout.SetTitle("data")
                    fout.cd(outdir)
                    hout.Write()

            

