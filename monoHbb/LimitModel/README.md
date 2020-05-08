How to create workspace, run limit and then save limit plots and cross-check plots. 
===================================================================================

This setup likley only one input from previous analysis steps, i.e. **AllMETHisto.root**. This must have: 
 * histogram for each background process 
 * histogram for each signal process
 * both of above for each category 
 * up and down histogram for each of the systematic uncertainties 


### Step 1: Create Workspace ### 
The first step is to create the workspace using **AllMETHisto.root**. This create the rooparamhist for each of the background we need to estimate using CRs. You can create the worksapce using 
```root -l -b -q PrepareWS_withnuisance.C```

Once **monoHbb_WS.root** woskspace is created, copy it to datacards_monoHbb_2017 

```cp monoHbb_WS.root datacards_monoHbb_2017```

### Step 2: Create datacards ### 
The datacards can be created by replacing the parameters in the template datacards using **RunLimits.py**. This is the main controlling script to perform all the steps once workspace is created and copied to respective directory. Define the parameters in **params.txt**. After this you can create datacards using: 

```python RunLimits.py -c --model 2hdma --merged --region "SR TOPE TOPMU WE WMU ZEE ZMUMU"``` 

 * -c: create datacards 
 * --model XXXX: tell the model name 
 * --merged/--resolved/--combined: code will create datacards for either one of the caregory, it will change in near future
 * --region " ": keep all the regions you want to combine in a single string seprated by single space
This will read the datacards from the **datacards_tmplate** and save newly created datacards in the **datacards_monoHbb_2017**. This create the datacards for each of the region as well as combining them. The string in the --region is same as in the histograms or used in the model formation

create the workspace from AllMETHisto.root using






create the workspace from AllMETHisto.root using  
## This will need many configurable parameters. 

## To set the environmanet do 
source envsetter.sh ## for Raman only, you can do the setup in new CMSSW that is better. 

## prepare the workspace with model ## right now only for boosted case, a string can be added to make similar model for resolved if the model will be same else it has to be a different file. 
root -l -b -q PrepareWS.C

copy worksoace to  datacards_monoHbb_2017 

cp monoHbb_WS.root datacards_monoHbb_2017 


## The out of above will be monoHbb_WS.root 
This file be used in the datacards to perform the simultaneous fit of SR and CRs. 


## create datacards using (some tweaks needed):
## you can provide the list of the regions you want to merge in the --region optin in double quotes. 
## before running this, set the parameters in params.txt 
python RunLimits.py -c --model 2hdma --merged --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" 


## run all the datacards using:
python RunLimits.py -A -L -v 0 -i monohbb2017_datacardslist_2hdma.txt



######### To do next ###### 

* run all the steps in a single shell script to automate the process for a given date or tag or some other string in order to differentiate the limits, 
* save the Pulls and impact plots [for Asimov, CR only fit, for bkg only fit, for s+b fit]
* save yield ratio comparison plots  [for bkg only fit, for s+b fit]
* save TF plots  [prefit only with systamatics ]
* save prefit postfit comparisomn plot with data [for for bkg only fit, for s+b fit]