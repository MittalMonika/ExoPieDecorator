import os 
import sys 
from ROOT import TFile, TH1F 

f = TFile("AllMETHistos/AllMETHistos_2018_monohbb_v12_08_21_addedMorePointsForZp2HDM.root")

mA= [300,400,500,600,700,800,900,1000,1200]
mzp=  [450,550,600,800,1000,1200,1400,1700,2000,2500,3000,3500,4000,4500,5000]


h_tmp = "monoHbb2018_B_SR_MZpXXX_MA0YYY"

for imzp in mzp:
    for ima in mA:
        if (int(imzp)) >= (int(ima) + 125.  ): 
            h_tmp1 = h_tmp.replace("XXX",str(imzp))
            h_2hdm = h_tmp1.replace("YYY",str(ima))
            
            h = f.Get(h_2hdm)
            if (h):
                print ("histogram exist")
            else:
                print (h_2hdm,"histograms does not exist--------")




fzpb = TFile("AllMETHistos/AllMETHistos_2018_monohbb_v12_08_21_addedMorePointsForZp2HDM.root")
mchi= [1,50,100,150,200,400,600,800]
mzp= [100,200,300,350,500,650,800,1000,1500,2000,2500,3000,3500]


h_tmp = "monoHbb2018_B_SR_MZp_XXX_Mchi_YYY"
for imzp in mzp:
    for imchi in mchi:
        if  (int(imzp)==100 and (int(imchi)==1 or int(imchi)==50)):isfill=True
        if  (int(imzp)==200 and (int(imchi)==1 or int(imchi)==50 or int(imchi)==100 or int(imchi)==150)):isfill=True
        if  (int(imzp)==300 and int(imchi)==150):isfill=True
        if  (int(imzp)==350 and int(imchi)==50):isfill=True
        if  (int(imzp)==500 and (int(imchi)==1 or int(imchi)==100 or int(imchi)==200 or int(imchi)==400)):isfill=True
        if  (int(imzp)==650 and int(imchi)==50):isfill=True
        if  (int(imzp)==800 and int(imchi)==50):isfill=True
        if  (int(imzp)==1000 and (int(imchi)==1 or int(imchi)==100 or int(imchi)==200 or int(imchi)==400 or int(imchi)==600 or int(imchi)==800)):isfill=True
        if  (int(imzp)==1500 and (int(imchi)==1 or int(imchi)==100 or int(imchi)==200 or int(imchi)==400 or int(imchi)==600 or int(imchi)==800)):isfill=True
        if  (int(imzp)==2000 and (int(imchi)==1 or int(imchi)==100 or int(imchi)==200 or int(imchi)==400 or int(imchi)==600 or int(imchi)==800)):isfill=True
        if  (int(imzp)==2500 and (int(imchi)==1 or int(imchi)==100 or int(imchi)==200 or int(imchi)==400 or int(imchi)==600 or int(imchi)==800)):isfill=True
        if  (int(imzp)==3000 and (int(imchi)==1 or int(imchi)==100 or int(imchi)==200 )):isfill=True
        if  (int(imzp)==3500 and (int(imchi)==1 or int(imchi)==100)):isfill=True
        if (isfill) and (imzp>imchi):
            h_tmp1 = h_tmp.replace("XXX",str(imzp))
            h_zpb = h_tmp1.replace("YYY",str(imchi))
            h = fzpb.Get(h_zpb)
            if (h):
                print ("histogram exist")
            else:
                print (h_zpb,"histograms does not exist--------")

