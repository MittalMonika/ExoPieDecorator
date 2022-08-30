import os 
import sys 
from LimitHelper import RunLimits
import  copy as copy 
thdma=True



#########################################################
## This will take the merged datacards for each year and tgen combine them all together. 
## possible values for category=["R","B","C"]
#########################################################

'''
Usage: simply execute using 
python combine_run2.py 

Explanation: This macro uses the datacards listed in .txt files and make combination datacards and then execute the AsymptoticLimits. The outcome is generally one pdf/png plot for the combination. 

What to change: There are few parameters which needs to be changed: 
1.  maList: only those points can enter for which exist for all years. 
2. category: possible values are "R", "B", "C" or depending on how datacards are made 
3. dmsimp: the boolean can be used to switch the model to scan 
4. 

'''

def getmAma(dc):
    mA=dc.split(".txt")[0].split("_")[-3]
    ma=dc.split(".txt")[0].split("_")[-1]
    return (str(ma),str(mA))

category="C"
model="2hdma"

limithelp=RunLimits("","161718","monoHbb",category,"Run2Combo_"+category,model )

datacards_2017 = 'bbDM2017_datacardslist_C_'+model+'.txt'
datacards_2016 = 'datacards_monoHbb_2016/thdma/monoHbb_datacard_2016_2hdma_C_allregion_2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-{}-MH4-{}-MH2-{}-MHC-{}.txt'

if thdma==True:
    dc_list=[]
    for id_ in open(datacards_2017):
        dc_list.append(id_.rstrip())
    
    
    dc_list_2017 = copy.deepcopy(dc_list)
    
    dc_list_2018 = copy.deepcopy(dc_list)
    dc_list_2018 = [w.replace("2017","2018") for w in dc_list_2018]
    
    print (dc_list_2017)
    print (dc_list_2018)

    datacardCounter=0
    
    for i in range(len(dc_list_2017)):
        dc_2017 = dc_list_2017[i]
        dc_2018 = dc_list_2017[i].replace("2017","2018")
        
        masses = getmAma(dc_2017)
        dc_2016 = datacards_2016.format(masses[1], masses[0], masses[1], masses[1])
        
        dc_run2 = dc_list_2017[i].replace("2017","run2")
        
        if os.path.isfile(dc_2017) and os.path.isfile(dc_2018) and os.path.isfile(dc_2016) :
            print ("data card for 2016, 2017 and 2018 exist ")

            
            combodatacard  = "combineCards.py  d2016="+dc_2016+" d2017="+dc_2017+" d2018="+dc_2018+" > "+dc_run2
            print (combodatacard)
            os.system(combodatacard)
            
            log_run2 = dc_run2.replace(".txt",".log")
            '''
            fout=open("tmp.txt","w")
            for iline in open(dc_run2):
                iline=iline.replace("datacards_monoHbb_2017/datacards_monoHbb_2017", "datacards_monoHbb_2017")
                iline=iline.replace("datacards_monoHbb_2018/datacards_monoHbb_2018", "datacards_monoHbb_2018")
                fout.write(iline)
            fout.close()
            os.system("mv tmp.txt "+ dc_run2)
            '''
            
    
            os.system ('combine -M AsymptoticLimits '+dc_run2+' --noFitAsimov -t -1 > '+log_run2)
            
            if datacardCounter ==0: mode = "w"
            if datacardCounter > 0: mode = "a"
            
            datacardCounter=datacardCounter+1
            
            limit_textfilename=limithelp.LogToLimitList(log_run2,category,mode)
            print ("output limit text file name", limit_textfilename)
            limit_rootfilename = limithelp.TextFileToRootGraphs(limit_textfilename)
            #limithelp.SaveLimitPdf1D(limit_rootfilename)

        else: 
            print (dc_2017, dc_2018, "one of these datacard does not exist")
            

    
    

    



