rootfile=$1
year=$2

root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"1b\", \"RECREATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"
root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"2b\", \"UPDATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"


#
##root -l -b -q PrepareWS_withnuisance_5bin.C"(\"bbDM\", \"1b\", \"RECREATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"
##root -l -b -q PrepareWS_withnuisance_5bin.C"(\"bbDM\", \"2b\", \"UPDATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"
#

python RunLimits.py -c --model 2hdma_all --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" --category=sr1
python RunLimits.py -c --model 2hdma_all --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" --category=sr2
python RunLimits.py -c --model 2hdma_all --region "bbDM${year}_datacardslist_1b_2hdma_all.txt bbDM${year}_datacardslist_2b_2hdma_all.txt" --category=srall


cp bbDM_${year}_WS.root datacards_bbDM_${year}/bbDM_${year}_WS.root


python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_1b_2hdma_all.txt --category=sr1 --savepdf --outlog="running limits for 1b"
python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_2b_2hdma_all.txt --category=sr2 --savepdf --outlog="running limits for 2b"
python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_C_2hdma_all.txt --category=srall --savepdf --outlog="running limits for 1b+2b"

#python RunLimits.py --savepdf --limitTextFile bin/limits_bbDM_1b_${year}.txt --outlog "saving pdf for 1b" --category=sr1
#python RunLimits.py --savepdf --limitTextFile bin/limits_bbDM_2b_${year}.txt --outlog "saving pdf for 2b" --category=sr2
#python RunLimits.py --savepdf --limitTextFile bin/limits_bbDM_combined_${year}.txt --outlog "saving pdf for 1b+2b" --category=srall



## for pull etc 
#root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"1b\", \"RECREATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"
#root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"2b\", \"UPDATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"
#python RunLimits.py -c --model 2hdma --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" --category=sr1
#python RunLimits.py -c --model 2hdma --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" --category=sr2
#python RunLimits.py -c --model 2hdma --region "bbDM${year}_datacardslist_1b_2hdma_all.txt bbDM${year}_datacardslist_2b_2hdma_all.txt" --category=srall
#python RunLimits.py --pulls --runmode asimov -i bbDM2017_datacardslist_C_2hdma.txt  --outlog "testing the pulls for asimov" --category srall
#python PlotPreFitPostFit.py fitDiagnostics_combined_2017_asimov.root plots_limit/postfitOverlay/ _combined_2017_

#python RunLimits.py --pulls --runmode data -i bbDM2016_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall                                                               

#python RunLimits.py --pulls --runmode cronly -i bbDM2016_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall                                                               
#python RunLimits.py --pulls --runmode cronly -i bbDM2017_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall                                                               
#python RunLimits.py --pulls --runmode cronly -i bbDM2018_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall                                                               
#
#python RunLimits.py --pulls --runmode cronly -i bbDM2017_datacardslist_1b_2hdma.txt  --outlog "testing the pulls for data" --category sr1b
#python RunLimits.py --pulls --runmode cronly -i bbDM2017_datacardslist_2b_2hdma.txt  --outlog "testing the pulls for data" --category sr2b
#python RunLimits.py --pulls --runmode cronly -i bbDM2017_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall

#text2workspace.py datacards_bbDM_2017/datacard_bbDM2017_2b_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_150.txt --channel-masks
#combine -M FitDiagnostics  datacards_bbDM_2017/datacard_bbDM2017_2b_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_150.root --saveShapes --saveWithUncertainties --setParameters mask_SR=1
#plotPostNuisance_combine.C("fitDiagnostics_2b_2017_cronly.root","plots_limit/pulls/","_2b_2017_")
