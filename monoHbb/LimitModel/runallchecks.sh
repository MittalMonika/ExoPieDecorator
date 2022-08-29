dirname=$1 #LimitModelTest_Run2017_10_12_2021
year=$2 #2017
datacard=$3 #datacards_monoHbb_2017/monoHbb_datacard_2017_2hdma_F_allregion_ggF_sp_0p35_tb_1p0_mXd_10_mA_400_ma_150.txt
catg=$4 #F

mode=asimov_t_0

## create workspace 
text2workspace.py $datacard --channel-masks
datacardws=`echo $datacard | sed  's|.txt|.root|g'`
echo $datacardws


mkdir -p ${dirname}

## run limits 
#combine -M AsymptoticLimits $datacard    -v 0 --rMin 1e-07 --rMax 30 > ${dirname}/limit.txt
#combine -M AsymptoticLimits $datacard  -t -1  -v 0 --rMin 1e-07 --rMax 30 > ${dirname}/limit_blind.txt


## run pulls and impact asimov b-only 
#### pulls 
combine -M FitDiagnostics  $datacardws --saveShapes --saveWithUncertainties -t -1 --expectSignal 0 -n _${catg}_${year}_${mode}_${dirname}
python diffNuisances.py fitDiagnostics_${catg}_${year}_${mode}_${dirname}.root --abs --all -g pulls_${catg}_${year}_${mode}_${dirname}.root
root -l -b -q PlotPulls.C\(\"pulls_${catg}_${year}_${mode}_${dirname}.root\",\"${dirname}/\",\"_${catg}_${year}_${mode}_${dirname}\"\)



#### impacts
#--freezeParameters ratett --setParameters ratett=1.2
text2workspace.py $datacard --channel-masks
combineTool.py -M Impacts -d $datacardws --doInitialFit --robustFit 1 -m 125 -t -1 --expectSignal 0 --rMin -10
combineTool.py -M Impacts -d $datacardws --doFits  --robustFit 1 -m 125 --parallel 32 -t -1 --expectSignal 0 --rMin -10
combineTool.py -M Impacts -d  $datacardws -m 125 -o impacts_t0.json
plotImpacts.py -i  impacts_t0.json -o   ${dirname}/impacts_t0_${catg}_${year}_${mode}_${dirname}

## run pulls and impact asimov signal injected 
### pulls 

#mode=asimov_t_m1

#combine -M FitDiagnostics  $datacardws --saveShapes --saveWithUncertainties -t -1 --expectSignal 1 -n _${catg}_${year}_${mode}_${dirname}
#python diffNuisances.py fitDiagnostics_${catg}_${year}_${mode}_${dirname}.root --abs --all -g pulls_${catg}_${year}_${mode}_${dirname}.root
#root -l -b -q PlotPulls.C\(\"pulls_${catg}_${year}_${mode}_${dirname}.root\",\"${dirname}/\",\"_${catg}_${year}_${mode}_${dirname}\"\)


#### impacts
#combineTool.py -M Impacts -d $datacardws --doInitialFit --robustFit 1 -m 125 -t -1 --expectSignal 1 --rMin -10
#combineTool.py -M Impacts -d $datacardws --doFits  --robustFit 1 -m 125 --parallel 32 -t -1 --expectSignal 1 --rMin -10
#combineTool.py -M Impacts -d  $datacardws -m 125 -o impacts_t1.json
#plotImpacts.py -i  impacts_t1.json -o  ${dirname}/impacts_t1_${dirname}



mode=fit_CRonly_result

## CR only fit pulls 
combine -M FitDiagnostics -d $datacardws -n _${catg}_${year}_${mode}_${dirname}  --saveShapes --saveWithUncertainties --setParameters mask_sr=1,mask_cat_B_sr=1,mask_cat_R_sr=1,mask_cat_F_sr=1,mask_d2017_cat_B_sr=1,mask_d2017_cat_R_sr=1,mask_d2018_cat_B_sr=1,mask_d2018_cat_R_sr=1 --X-rtd MINIMIZER_analytic --cminFallbackAlgo Minuit2,0:1.0
root -l -b -q plotPostNuisances_multiCanvas.C\(\"fitDiagnostics_${catg}_${year}_${mode}_${dirname}.root\",\"${dirname}/\",\"${catg}_${year}_${mode}_${dirname}\"\)
##root -l -b -q plotPostNuisance_combine.C\(\"fitDiagnostics_${catg}_${year}_${mode}_${dirname}.root\",\"${dirname}/\",\"${catg}_${year}_${mode}_${dirname}\"\)


## CR only postfit summary plot  ## need to work on this one. 
#fitDiagnostics_R_2017_fit_CRonly_result_Testing_mA_800_ma_150_9July2021_nob.root

#echo "monika i am stuck here before stackhist.py", $catg, $mode, $year

#python stackhist.py  fitDiagnostics_${catg}_${year}_${mode}_${dirname}.root ${catg} ${mode} ${year}

#echo "monika i am stuck here after stackhist.py", $catg, $mode, $year
#python crSummary_postfit.py -i fitDiagnostics_${catg}_${year}_${mode}_${dirname}.root -d b -c 2b -t ${catg}_${year}_${mode}_${dirname} -y 2017



#combine -M FitDiagnostics -d $datacardws -n _${catg}_${year}_${mode}_${dirname}  --saveShapes --saveWithUncertainties --freezeParameters ratett --setParameters mask_SR=1,ratett=1.2 --X-rtd MINIMIZER_analytic --cminFallbackAlgo Minuit2,0:1.0

