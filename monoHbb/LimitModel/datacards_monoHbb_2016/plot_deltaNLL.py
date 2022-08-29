from __future__ import division

import ROOT
from ROOT import gROOT, TFile, TTree, TChain, gPad, gDirectory, AddressOf, TH1F, TCanvas, gStyle, TLegend, TGaxis
from multiprocessing import Process
from optparse import OptionParser
from operator import add
import math
import sys
import time
from array import array
import numpy
import os
import csv

def main(options,args):
	
	ifile = options.ifile
	tfile = options.tfile
	ofile = options.ofile
	var = options.variable
	tf1 = ROOT.TFile(ifile);
	tt1 = tf1.Get("limit");
	tf2 = ROOT.TFile(tfile);
	tt2 = tf2.Get("limit");

        Apply = True;

	if Apply: GetEffs(tt1,tt2,ofile,var);

######--------------------------------------------------------------------------------------------------------
######--------------------------------------------------------------------------------------------------------
def GetEffs(tt1,tt2,ofile,var):


	c1 = TCanvas('c1','deltaNLL',200,10,800,700)
	gStyle.SetOptStat(0)

	
	#Declaring all the histograms to be filled from tree
	#hfail_20perc_down = TH1F('hfail_20perc_down','hfail_20perc_down',4,array('f',bins))

	#Filling all the histograms from tree
	#tt1.Draw("2*deltaNLL:mettrig >> hdata")
	#tt2.Draw("2*deltaNLL:mettrig >> hasimov")
	tt1.Draw("2*deltaNLL:%s >> hdata" % var)
	tt2.Draw("2*deltaNLL:%s >> hasimov" % var)

	hdata = gDirectory.Get("hdata")
	hdata.SetMarkerSize(17)
	hdata.SetTitle("")
	hdata.GetXaxis().SetTitle("%s" % var)
	hdata.GetYaxis().SetTitle("2*deltaNLL")
	hdata.Draw()

	hasimov = gDirectory.Get("hasimov")
	hasimov.SetMarkerSize(17)
	hasimov.SetMarkerColor(632)
	hasimov.Draw("SAME")
	
	leg = TLegend(.56,.65,.47,.83)
	leg.SetBorderSize(0)
	leg.SetFillColor(0)
	leg.SetFillStyle(0)
	leg.SetTextFont(42)
	leg.SetTextSize(0.032)
	leg.AddEntry(hdata,"Data","p")
	leg.AddEntry(hasimov,"Asimov","p")
	leg.Draw()

	c1.Update()

	c1.SaveAs("%s.pdf" % ofile)
	c1.SaveAs("%s.png" % ofile)


##----##----##----##----##----##----##
if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('-i','--ifile', dest='ifile', default = 'file1.root',help='MC/data file to add the N2DDT branch to', metavar='ifile')
	parser.add_option('-t','--tfile', dest='tfile', default = 'file2.root',help='MC/data file to add the N2DDT branch to', metavar='tfile')
	parser.add_option('-o','--ofile', dest='ofile', default = 'file',help='MC/data file to add the N2DDT branch to', metavar='ofile')
	parser.add_option('-v','--variable', dest='variable', default = 'fj1Pt',help='MC/data file to add the N2DDT branch to', metavar='variable')

	(options, args) = parser.parse_args()
	 
	main(options,args)





