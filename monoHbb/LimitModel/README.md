How to create workspace, run limit and then save limit plots and cross-check plots. 
===================================================================================

This setup likley only one input from previous analysis steps, i.e. **AllMETHisto.root**. This must have: 
 * histogram for each background process 
 * histogram for each signal process
 * both of above for each category 
 * up and down histogram for each of the systematic uncertainties 


#### Extra ####
For myself, I don't have proper version of CMSSW where I write the mode so I need to set it from another area, 

```source envsetter.sh ```

### Step 1: Create Workspace ### 
The first step is to create the workspace using **AllMETHisto.root**. This create the rooparamhist for each of the background we need to estimate using CRs. You can create the worksapce using
 
```root -l -b -q PrepareWS_withnuisance.C```

The out of above will be **monoHbb_WS.root**. Once **monoHbb_WS.root** woskspace is created, copy it to **datacards_monoHbb_2017**. This file is used in the datacards to perform the simultaneous fit of SR and CRs.


```cp monoHbb_WS.root datacards_monoHbb_2017```

### Step 2: Create datacards ### 
The datacards can be created by replacing the parameters in the template datacards using **RunLimits.py**. This is the main controlling script to perform all the steps once workspace is created and copied to respective directory. Define the parameters in **params.txt**. After this you can create datacards using: 

```python RunLimits.py -c --model 2hdma --merged --region "SR TOPE TOPMU WE WMU ZEE ZMUMU"``` 

 * -c: create datacards 
 * --model XXXX: tell the model name 
 * --merged/--resolved/--combined: code will create datacards for either one of the caregory, it will change in near future
 * --region " ": keep all the regions you want to combine in a single string seprated by single space

This will read the datacards from the **datacards_tmplate** and save newly created datacards in the **datacards_monoHbb_2017**. 
This create the datacards for each of the region as well as combining them. The string in the --region is same as in the histograms or used in the model formation. 


This will also create a .txt file **monohbb2017_datacardslist_2hdma.txt** which will have path to the newly created combined data card only [created by combining all the regions you just listed]

## run all the datacards listed in the **monohbb2017_datacardslist_2hdma.txt**:

```python RunLimits.py -A -L -v 0 -i monohbb2017_datacardslist_2hdma.txt```

 * -A: use the asymptotic limit method 
 * -L: run the limits using above method i.e. asymptotic [others will mot work at the moment]
 * -v: verbose, [possible values 0,1,2,3]
 * -i: This is the input file which is created in previous step, **monohbb2017_datacardslist_2hdma.txt**. This can be automated using decaribe.py in future 



######### To do next ###### 

* run all the steps in a single shell script to automate the process for a given date or tag or some other string in order to differentiate the limits, 
* save the Pulls and impact plots [for Asimov, CR only fit, for bkg only fit, for s+b fit]
* save yield ratio comparison plots  [for bkg only fit, for s+b fit]
* save TF plots  [prefit only with systamatics ]
* save prefit postfit comparisomn plot with data [for for bkg only fit, for s+b fit]


from benedikt
combine datacard.root -M FitDiagnostics --saveShapes --saveWithUncertainties --setParameters mask_signal=1

if your signal region is called "signal"

mask_X 

