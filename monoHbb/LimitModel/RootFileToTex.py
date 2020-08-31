import os
from ROOT import TH1F, TFile 

f = TFile("fitDiagnostics_merged_2017_data.root","READ")



def getyield(region, proc_):
    h = f.Get(region+proc_[0])
    yield_     = h.Integral()
    yield_err_ = 
    
    #f.cd(region)
    
    #print "yield "

regions=["SR","TOPE","TOPMU","WE", "WMU", "ZEE", "ZMUMU"]
regions_dir= ["shapes_prefit/"+ir+"/" for ir in regions]
proc_sr=["zjets","wjets","tt","singlet","qcd","smh"]

print getyield(regions_dir[0], proc_sr)
print regions_dir
