import os 
import sys
import csv

versionChangeLog="running the merged and resolved analysis for 29 May meeting"

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
/afs/cern.ch/work/p/ptiwari/public/bbDM/WCr_Split/AllMETHistos.root     

## The analysis details which has to be changed for each analsis                                                                                                             '''
anadetails={
    "histFileName":    "AllMETHistos.root",     ## root file with histograms 
    "analysisName":    "monoHbb",               ## For which analysis this is being done 
    "yearStr":         "2018",                  ## For which year data this model is being run, by default it is set to 2016, but can be changed here. 
    
    
    ## for combined additional information is needed in order to sync all the names etc, e.g. for each type is below, commented for now  '''
    ## categories is made list, but at the moment accept only one value, multiple value compatibility is still not available 
    "sr1":{
        "categories":      ["B"],
        "categories_short": ["_B"],
        "categories_input":["B"]
    },
    
    
    "sr2":{
        "categories":      ["R"],
        "categories_short": ["_R"],
        "categories_input":["R"]
    },

    "sr3":{
        "categories":      ["F"],
        "categories_short": ["_F"],
        "categories_input":["F"]
    },

    
    "srall":{
        "categories":      ["combined"],
        "categories_short": ["_C"],
        "categories_input":["B", "R", "F"]   ## use this order in the command line also 
        #"categories_input":["B", "R"]   ## use this order in the command line also , when far category is not needed
    },
    
    ## these are dir for limit and other type of plots 
    "plotsDir":   {"limit":"plots_limit/",
                   "limitcomp":"plots_limit/limitcomp/",
                   "pulls":"plots_limit/pulls/",
                   "impact":"plots_limit/impact/",
                   "tf":"plots_limit/TF/",
                   "stack":"plots_limit/Stack/",
                   "yr":"plots_limit/YieldRatio/",
                   "pfitOverlay":"plots_limit/postfitOverlay/"
               },
    "version" :         {"V2":versionChangeLog},            ## #any other information needed to explain the details by rootfile name, by default it is version track
}


## High level details constructed using the analysis details dictionary 
#HLdetails={
#    "WSRootFile":   myjoin([anadetails["analysisName"], anadetails["yearStr"], "WS"])+ ".root", # output file with the workspace including all information about the model including inputs
#    "wsname"    :   [myjoin(["ws", anadetails["analysisName"], category, anadetails["yearStr"] ] ) for category in anadetails["categories"] ], # name of the workspace
#    "datacardDir":  myjoin(["datacards", anadetails["analysisName"], anadetails["yearStr"]]),
#    "TFdir"      :  [myjoin(["transferfactor", anadetails["analysisName"], anadetails["yearStr"], catShort]) for catShort in anadetails["categories_short"]]
#}

