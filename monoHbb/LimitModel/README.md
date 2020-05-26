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

```python RunLimits.py -c --model 2hdma --region "SR TOPE TOPMU WE WMU ZEE ZMUMU"``` 

 * -c: create datacards 
 * --model XXXX: tell the model name. It can take two values for now, 2HDMa and 2HDMa_all . Former used for one point and other used for all points
 * --merged/--resolved/--combined: depriciated, now declared in the describepy, code will create datacards for either one of the caregory, it will change in near future
 * --region " ": keep all the regions you want to combine in a single string seprated by single space

This will read the datacards from the **datacards_tmplate** and save newly created datacards in the **datacards_monoHbb_2017**. 
This create the datacards for each of the region as well as combining them. The string in the --region is same as in the histograms or used in the model formation. 


This will also create a .txt file **monohbb2017_datacardslist_2hdma.txt** which will have path to the newly created combined data card only [created by combining all the regions you just listed]

### Step 2.2 Combine category datacards ###
In order to combine the datacards for resolved and boosted categories, you can use the same command as to create but change the regions as below: 

```python RunLimits.py -c --model 2hdma_all --region "monohbb2017_datacardslist_B_2hdma_all.txt monohbb2017_datacardslist_R_2hdma_all.txt"```

Note that the order of Booseted and Resolved here should same as in the describe.py. 

 * For reference we use boosted as high priority w.r.t resolved 
 * One must provide additional list in describe.py **categories_input** to sync all the names etc. 

## run all the datacards listed in the **monohbb2017_datacardslist_2hdma.txt**:

```python RunLimits.py -A -L -v 0 -i monohbb2017_datacardslist_2hdma.txt --merged --savepdf```

 * -A: use the asymptotic limit method 
 * --merged or --resolved or --combined : this is category of analysis and will be used in order to name the limit.txt file and rootfile with grapsh 
 * --makegraph: save the limit graphs in .roor file 
 * --savepdf: save the pdf of the graphs, if this is given --makegraph will be called automatically 
 * -L: run the limits using above method i.e. asymptotic [others will not work at the moment]
 * -v: verbose, [possible values 0,1,2,3]
 * -i: This is the input file which is created in previous step, **monohbb2017_datacardslist_2hdma.txt**. This can be automated using decaribe.py in future 

## prepare results using limit.txt 

Prepare graphs using the limit.txt without runing the limits code again, just convert the .txt file into .root of .pdf. For this you need to provide the limit.txt and can be done using 

```python RunLimits.py --savepdf --limitTextFile path_to_limits_text_file```
 * --savepdf: save the graphs and pdf file for the limits 
 * --limitTextFile: use the input from .txt file which will be provided from command line 

## Pulls and FitDiagnostics ## 

In order to perform the fit checks, plot pulls, yieldratios, postfit and prefit comparison one just need to run the command in correct manner: 

```python RunLimits.py --pulls --runmode data -i monohbb2017_datacardslist_2hdma.txt``` 



 * --pulls: run the code to estimate the Pulls 
 * --runmode: data OR asimov OR cronly : there is no way that these 3 modes can be run in one go. so the plots will be saved in different directory as they will result from 3 different run. 
 * -i: input text file with datacard lists, Now monohbb2017_datacardslist_2hdma.txt should contain path to ONLY one data card which will be used to perform the fit and do checks.
        If it will have more than one datacard then it will run on all fo them and save results only for the last one in the list. This is little time consuming. 
 * the directory structure is hardcoded and chnaged for each time code is run so that plots are not overwritten. 
 * outlog: provide quick text to be written into the output.log file. Without this code will not work. 

## Impact plots ## 

```python RunLimits.py --impact --runmode data -i monohbb2017_datacardslist_2hdma.txt```	

 * --impact: to ensure that code runs to prepare the inpact plot 
 * --runmode: possible values: data, asimov, cronly; there is no way that these 3 modes can be run in one go. so the plots will be saved in different directory as they will result from 3 different run
 * -i: text file with path to datacard inside, Only one datacard should be there 



## To do next ##
 * save limit plot 
 * add a command line option to show comparison of limit graph 
 * save impact plot 
 * save TF plots  [prefit only with systamatics ]
 * add Top TF from Wjets CR 
 * check what is wrong with the ele and mu sclae, why they are so pulled, 
 * checck the prefit and postfit plots to debug 
 * check the total background and its uncertainity with and without masking data in the SR. the plot is in "shapes_fit_b/signal/total_background" 
 * debug following: 
  * [WARNING] Found [rrvbc_SR_wjets2] at boundary. 
  * [WARNING] Found [rrvbc_SR_wjets3] at boundary. 
  * [WARNING] Found [rrvbc_SR_wjets4] at boundary. 
  * [WARNING] Found [eletrigeffCMS2016_scale_] at boundary. 
 


$$ For merged: 
root -l -b -q PrepareWS_withnuisance.C"(\"monoHbb\", \"merged\", \"RECREATE\")"

$$ For resolved: 
root -l -b -q PrepareWS_withnuisance.C"(\"monoHbb\", \"resolved\", \"UPDATE\")"





