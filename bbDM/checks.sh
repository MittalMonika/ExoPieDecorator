##https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/HiggsPAGPreapprovalChecks

datacard=datacards_bbDM_2017/datacard_bbDM2017_2b_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_100.txt
year=2017
catg=2b
mode=asimov


combine -M AsymptoticLimits $datacard  --noFitAsimov  -v 0 --rMin 1e-07 --rMax 30

rm fitDiagnostics.root
combine -M FitDiagnostics --saveShapes $datacard --saveWithUncertainties --saveNormalizations --X-rtd MINIMIZER_analytic  --rMin -100 -t -1 --expectSignal 0

rm fitDiagnostics_$catg_$year_$mode.root
mv fitDiagnostics.root fitDiagnostics_$catg_$year_$mode.root

rm pulls_$catg_$year_$mode.root
python diffNuisances.py fitDiagnostics_$catg_$year_$mode.root --abs --all -g pulls_$catg_$year_$mode.root

root -l -b -q PlotPulls.C\(\"pulls_$catg_$year_$mode.root\",\"plots_limit/pulls/\",\"_$catg_$year_\"\)

python yieldratio.py fitDiagnostics_$catg_$year_$mode.root plots_limit/YieldRatio/ _$catg_$year_

python stackhist.py  fitDiagnostics_$catg_$year_$mode.root $catg $mode $year


## move everything to a web page and spit the link to page 

mode=cronly

rm fitDiagnostics.root

## convert to workspace 
text2workspace.py $datacard --channel-masks
datacardws=`echo $datacard | sed  's|.txt|.root|g'`
echo $datacardws

## perform fit 
combine -M FitDiagnostics  $datacardws --saveShapes --saveWithUncertainties --setParameters mask_SR=1,mask_cat_1b_SR=1,mask_cat_2b_SR=1 --X-rtd MINIMIZER_analytic --cminFallbackAlgo Minuit2,0:1.0

## clean area 
rm fitDiagnostics_${catg}_${year}_${mode}.root
mv fitDiagnostics.root fitDiagnostics_${catg}_${year}_${mode}.root

rm pulls_${catg}_${year}_${mode}.root

## create pulls 
python diffNuisances.py fitDiagnostics_${catg}_${year}_${mode}.root --abs --all -g pulls_${catg}_${year}_${mode}.root


## save pulls 
root -l -b -q PlotPulls.C\(\"pulls_${catg}_${year}_${mode}.root\",\"plots_limit/pulls/\",\"_${catg}_${year}_\"\)

## save yield ratio 
python yieldratio.py fitDiagnostics_${catg}_${year}_${mode}.root plots_limit/YieldRatio/ _${catg}_${year}_

## save stack plots 
python stackhist.py  fitDiagnostics_${catg}_${year}_${mode}.root ${catg} ${mode} ${year}




## run impact b-only
combineTool.py -M Impacts -d $datacardws --doInitialFit --robustFit 1 -m 125 -t -1 --expectSignal 0 --rMin -10
combineTool.py -M Impacts -d $datacardws --doFits  --robustFit 1 -m 125 --parallel 32 -t -1 --expectSignal 0 --rMin -10
combineTool.py -M Impacts -d  $datacardws -m 125 -o impacts_t0.json
plotImpacts.py -i  impacts_t0.json -o  impacts_t0



## run impact signal injected 
combineTool.py -M Impacts -d $datacardws --doInitialFit --robustFit 1 -m 125 -t -1 --expectSignal 1 --rMin -10
combineTool.py -M Impacts -d $datacardws --doFits  --robustFit 1 -m 125 --parallel 32 -t -1 --expectSignal 1 --rMin -10
combineTool.py -M Impacts -d  $datacardws -m 125 -o impacts_t1.json
plotImpacts.py -i  impacts_t1.json -o  impacts_t1




## limit 
combine -M AsymptoticLimits $datacardws --noFitAsimov  -v 0 --rMin 1e-07 --rMax 3 


## Pulls b only 
combine -M FitDiagnostics  $datacardws --saveShapes --saveWithUncertainties -t -1 --expectSignal 0
python diffNuisances.py fitDiagnostics.root -a  --abs -g plots_t0.root

## Pulls signal injected 
combine -M FitDiagnostics  $datacardws --saveShapes --saveWithUncertainties -t -1 --expectSignal 1
python diffNuisances.py fitDiagnostics.root -a  --abs -g plots_t1.root



## Good ness of fit test 

## Use saturated method 

## run on real data 
combine -M GoodnessOfFit $datacard --algo=saturated 

combine -M GoodnessOfFit $datacard --algo=saturated -t 500 -s 123 --toysFreq ## It is recomended to use the frequentist toys (--toysFreq) when running the saturated model


## For masked channels 

text2workspace.py $datacard --channel-masks
datacardws=`echo $datacard | sed  's|.txt|.root|g'`
echo $datacardws

## s+b fit , signal and control regions are included in both the fit and in the evaluation of the test-static, and the signal strength is freely floating. This measures the compatibility between the signal+background fit and the observed data
combine -M GoodnessOfFit -d $datacardws --algo=saturated -n _result_sb 


## CR only fit 
### for data
combine -M GoodnessOfFit -d $datacardws --algo=saturated -n _result_bonly_CRonly --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0
### for toys
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 50 --toysFrequentist -s 123

combineTool.py -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 10 --toysFrequentist -s 123 --job-mode condor --sub-opt`+JobFlavour = "workday"`


## fit diagonistics for postfit shapes
combine -M FitDiagnostics -d $datacardws -n _fit_CRonly_result --saveShapes --saveWithUncertainties --setParameters mask_SR=1 --X-rtd MINIMIZER_analytic --cminFallbackAlgo Minuit2,0:1.0
python diffNuisances.py fitDiagnostics_fit_CRonly_result.root -a  --abs -g pulls_CRonly.root




