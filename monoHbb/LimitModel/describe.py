import os 
import sys

def myjoin(tojoin):
    joined=""
    it=0
    for ij in tojoin: 
        if it < (len(tojoin)-1):
            joined = joined+ij+"_"
        if it == (len(tojoin)-1):
            joined = joined+ij
        it = it +1
    return joined

''' input file taken from Praveen at the moment from location
/afs/cern.ch/work/p/ptiwari/public/bbDM/WCr_Split/AllMETHistos.root                                                                                                                 '''
inputfile = "AllMETHistos.root"

''' For which analysis this is being done '''
analysisName = "monoH"

''' For which year data this model is being run, by default it is set to 2016, but can be changed here. '''
yearStr        = "2017"

''' any other information needed to explain the details by rootfile name, by default it is version track, '''
postfix     = "V0";

''' output file with the workspace including all information about the model including inputs'''
outputfile  = myjoin(["combine_ws", analysisName, yearStr, postfix])+ ".root"

print "output file name = ", outputfile
''' name of the workspace ''' 
wsname = "ws" + analysisName

''' fitting range '''
met_low = 200
met_hi = 2000

datacardDir="datacards_monoHbb_2017" 
