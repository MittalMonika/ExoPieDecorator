## Only for Raman 
I don't have setup of correct version of combine, so i source this script in my area, you might want to install the combine correctly. 
source envsetter.sh

## 
root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"1b\", \"RECREATE\", \"AllMETHistos\")"

##
python RunLimits.py -c --model 2hdma --region "SR"

##  combine 1b and 2b category 
python RunLimits.py -c --model 2hdma_all --region "bbDM2016_datacardslist_1b_2hdma_all.txt bbDM2016_datacardslist_2b_2hdma_all.txt"


##
combine -M AsymptoticLimits datacards_bbDM_2016/datacard_bbDM2016_1b_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_150.txt

## To do 

#### move datacardtemplatename_ to describe.py 
#### move fparam to describe.py 


# Workflow for Limit Calculation
## Installation
Use the Higgs [Combine](http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/) page to install combine tool and for documentation

## Usage
* Make the ```AllMETHistos.root``` file using bbDM_combinedroot.py file
* Make the ```bbDM_WS.root``` file using PrepareWS_withSyst.C file
```
root -l -b -q PrepareWS_withSyst.C
```
* Run the dataCard_makeNrun.py file with create command for making the datacards
```
python dataCard_makeNrun.py create
```
* Run the dataCard_makeNrun.py file with run command for calculating the limit
```
python dataCard_makeNrun.py run
```
* Run limit_scanner.py file for getting the limit in text file
```
python limit_scanner.py
```
* Run limit_textTOgraph.py file to get the limit in root file
```
python limit_textTOgraph.py
```
* Run limit_plotter.py to get the plots:
```
python limit_plotter.py
```

### For getting prefit and postfit plots
```
combine -M FitDiagnostics --saveShapes --abs --all --plots datacard.txt
```
