datacard=datacards_monoHbb_2018/monoHbb_datacard_2018_2hdma_R_allregion_ggF_sp_0p35_tb_1p0_mXd_10_mA_800_ma_150.txt
year=2018
catg=C

text2workspace.py $datacard --channel-masks
datacardws=`echo $datacard | sed  's|.txt|.root|g'`

echo $datacardws

combine -M GoodnessOfFit -d $datacardws --algo=saturated -n _result_bonly_CRonly --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0

combine -M GoodnessOfFit -d $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 30 --toysFrequentist -s 12431 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12432 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12433 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12434 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12435 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12436 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12437 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12438 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12439 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 12430 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124311 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124312 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124313 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124314 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124315 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124316 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124317 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124318 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124319 &
combine -M GoodnessOfFit -d  $datacardws --algo=saturated -n _result_bonly_CRonly_toy --setParametersForFit mask_SR=1 --setParametersForEval mask_SR=0 --freezeParameters r --setParameters r=0,mask_SR=1 -t 100 --toysFrequentist -s 124320 &
#hadd higgsCombine_result_bonly_CRonly_toy.GoodnessOfFit.mH120.Merged.root higgsCombine_result_bonly_CRonly_toy.GoodnessOfFit.mH120.1243*.root
