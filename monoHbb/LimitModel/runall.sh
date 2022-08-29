rootfile=$1
year=$2
postfix=$3
nbins=$4
model=$5
#cat=$6
limitmodel=$6

echo $nbins



#catRB=" "
#if [[ $cat == "R" ]]
#then
#    catRB="sr2"
#fi
#
#if [[ $cat == "B" ]]
#then
#    catRB="sr1"
#fi
#
#if [[ $cat == "combo" ]]
#then
#    catRB="srall"
#fi


echo $cat, $limitmodel, $catRB


    
    #####################    #####################    #####################    #####################    #####################
    ###For RateParam
    if [ $limitmodel == "RP" ]
    then 
	#python prepareCards_RP.py -c B  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d AllMETHistos_monohbb_v12_07_16_unrolled_45BinsHist_BoostedCROnly.root
	#python prepareCards_RP.py -c R  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d AllMETHistos_monohbb_v12_07_16_unrolled_43RVs61BRebinBinsHist.root  
	#python prepareCards_RP.py -c F  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d AllMETHistos_monohbb_v12_07_16_lowMETCat_25bins_UpdatedMetTrig_v2.root

	#farrootfile="AllMETHistos_monohbb_v12_08_20_FarCat_25bins.root"
	#farrootfile="AllMETHistos_2018_monohbb_v12_08_20_FarCat_25bins.root"
	#echo ${farrootfile}
	#boosted
	echo "prepareCards_RP.py -c B  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d ${rootfile}"
	python prepareCards_RP.py -c B  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d ${rootfile}
	#python prepareCards_RP_fullscans.py -c B  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d ${rootfile}
	#resolved
	python prepareCards_RP.py -c R  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d ${rootfile}
	#python prepareCards_RP.py -c F  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d ${farrootfile}
	#python prepareCards_RP.py -c F  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year} -d ${rootfile}


	cp AllMETHistos/${rootfile} datacards_monoHbb_${year}/
	#cp AllMETHistos/${farrootfile} datacards_monoHbb_${year}/
	
	python RunLimits.py -A -L -v 0 -i  monohbb${year}_datacardslist_B_allregion_${model}_all.txt --category=sr1 --postfix $postfix --savepdf --outlog="running limits for Boosted"  --year ${year} --model ${model} --oned
	python RunLimits.py -A -L -v 0 -i  monohbb${year}_datacardslist_R_allregion_${model}_all.txt --category=sr2 --postfix $postfix --savepdf --outlog="running limits for Resolved"  --year ${year} --model ${model} --oned	


	#python RunLimits.py -A -L -v 0 -i  monohbb${year}_datacardslist_F_allregion_${model}_all.txt --category=sr3 --postfix $postfix --savepdf --outlog="running limits for lowmet"  --year ${year} --model ${model}
	#python RunLimits.py -c  --region "monohbb${year}_datacardslist_B_allregion_${model}_all.txt monohbb${year}_datacardslist_R_allregion_${model}_all.txt monohbb${year}_datacardslist_F_allregion_${model}_all.txt" --category=srall --year ${year} --model ${model}

	python RunLimits.py -c  --region "monohbb${year}_datacardslist_B_allregion_${model}_all.txt monohbb${year}_datacardslist_R_allregion_${model}_all.txt" --category=srall --year ${year} --model ${model}
	python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_C_${model}.txt --category=srall --postfix $postfix --savepdf --outlog="running limits for R and B"  --year ${year} --model ${model} --oned

    fi


    #for TF R or B doesn't make diffeernce it will run for both
    if [[ $limitmodel == "TF" ]] 
    then 
	echo $limitmodel , "in TF 1 "
	python prepareCards.py -c B  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year}
	python prepareCards.py -c R  -m ${model} -reg SR TOPE TOPMU ZEE ZMUMU -y ${year}
	## create workspace 
	


        root -l -b -q PrepareWS_withnuisanceInvertTF_noW_nBins.C"(\"monoHbb\", \"B\", \"RECREATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\", $nbins)"
        root -l -b -q PrepareWS_withnuisanceInvertTF_noW_nBins.C"(\"monoHbb\", \"R\", \"UPDATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\", $nbins)"
	## copy the workspace 
	cp monoHbb_${year}_WS.root datacards_monoHbb_${year}/monoHbb_${year}_WS.root
        ## run limits 
	python RunLimits.py -A -L -v 0 -i  monohbb${year}_datacardslist_B_allregion_${model}_all.txt --category=sr1 --postfix $postfix --savepdf --outlog="running limits for Boosted"  --year ${year} --model ${model}
	python RunLimits.py -A -L -v 0 -i  monohbb${year}_datacardslist_R_allregion_${model}_all.txt --category=sr2 --postfix $postfix --savepdf --outlog="running limits for Resolved"  --year ${year} --model ${model}
	python RunLimits.py -c  --region "monohbb${year}_datacardslist_B_allregion_${model}_all.txt monohbb${year}_datacardslist_R_allregion_${model}_all.txt" --category=srall --year ${year} --model ${model}
	python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_C_${model}.txt --category=srall --postfix $postfix --savepdf --outlog="running limits for R and B"  --year ${year} --model ${model}
	
    fi

    
    ## create combination cards resolved + boosted we run run it for now
#
#    if [ $cat == "combo"  ]
#    then
#	echo " I am in combo for ", $model
#	python RunLimits.py -c  --region "monohbb${year}_datacardslist_B_allregion_${model}_all.txt monohbb${year}_datacardslist_R_allregion_${model}_all.txt" --category=$catRB --year ${year} --model ${model}
#	python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_C_${model}_all.txt --category=$catRB --postfix $postfix --savepdf --outlog="running limits for R and B"  --year ${year} --model ${model}
#    fi
    

#fi 





## for pull etc 
#root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"1b\", \"RECREATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"
#root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"2b\", \"UPDATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"
#python RunLimits.py -c --model 2hdma --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" --category=sr1  --year ${year}
#python RunLimits.py -c --model 2hdma --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" --category=sr2 --year ${year}
#python RunLimits.py -c --model 2hdma --region "bbDM${year}_datacardslist_1b_2hdma_all.txt bbDM${year}_datacardslist_2b_2hdma_all.txt" --category=srall  --year ${year}
#python RunLimits.py --pulls --runmode asimov -i bbDM2017_datacardslist_C_2hdma.txt  --outlog "testing the pulls for asimov" --category srall --year ${year}
#python PlotPreFitPostFit.py fitDiagnostics_combined_2017_asimov.root plots_limit/postfitOverlay/ _combined_2017_

#python RunLimits.py --pulls --runmode data -i bbDM2016_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall                                                               

#python RunLimits.py --pulls --runmode cronly -i bbDM2016_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall --year ${year}                                                              
#python RunLimits.py --pulls --runmode cronly -i bbDM2017_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall --year ${year}                                                              
#python RunLimits.py --pulls --runmode cronly -i bbDM2018_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall --year ${year}                                                              
#																	    
#python RunLimits.py --pulls --runmode cronly -i bbDM2017_datacardslist_1b_2hdma.txt  --outlog "testing the pulls for data" --category sr1b --year ${year}
#python RunLimits.py --pulls --runmode cronly -i bbDM2017_datacardslist_2b_2hdma.txt  --outlog "testing the pulls for data" --category sr2b --year ${year}
#python RunLimits.py --pulls --runmode cronly -i bbDM2017_datacardslist_C_2hdma.txt  --outlog "testing the pulls for data" --category srall --year ${year}

#text2workspace.py datacards_bbDM_2017/datacard_bbDM2017_2b_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_100.txt --channel-masks
#combine -M FitDiagnostics  datacards_bbDM_2017/datacard_bbDM2017_2b_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_100.root --saveShapes --saveWithUncertainties --setParameters mask_SR=1
#combine -M FitDiagnostics datacards_bbDM_2017/datacard_bbDM2017_C_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_100.root  --saveShapes --saveWithUncertainties --setParameters mask_cat_1b_SR=1,mask_cat_2b_SR=1
#root -l -b -q plotPostNuisance_combine.C\(\"fitDiagnostics.root\",\"plots_limit/pulls/\",\"_2b_2017_\"\)

#plotPostNuisance_combine.C("fitDiagnostics_2b_2017_cronly.root","plots_limit/pulls/","_2b_2017_")

#python  stackhist.py


## combine -M AsymptoticLimits datacards_bbDM_2017/datacard_bbDM2017_C_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_10.txt  --noFitAsimov  -v 0 --rMin 1e-07 --rMax 30


## impact: asimov 
#combineTool.py -M Impacts -d  datacards_bbDM_2017/datacard_bbDM2017_C_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_100.root -m 200 --rMin -1 --rMax 2 --robustFit 1 --doInitialFit  -t -1 --expectSignal 0
#combineTool.py -M Impacts -d datacards_bbDM_2017/datacard_bbDM2017_C_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_100.root -m 200 --rMin -1 --rMax 2 --robustFit 1 --doFits  -t -1 --expectSignal 0
#combineTool.py -M Impacts -d datacards_bbDM_2017/datacard_bbDM2017_C_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_100.root -m 200 --rMin -1 --rMax 2 --robustFit 1 --output impacts.json
# plotImpacts.py -i impacts.json -o impacts
#[khurana@lxplus774 bbDM]$ combine -M FitDiagnostics  datacards_bbDM_2017/datacard_bbDM2017_2b_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_100.root --saveShapes --saveWithUncertainties --setParameters mask_SR=1,mask_cat_1b_SR=1,mask_cat_2b_SR=1   -v 3 --cminDefaultMinimizerType Minuit2 --cminDefaultMinimizerStrategy 1 --cminFallbackAlgo Minuit2,0:1.0



#combine -M AsymptoticLimits datacards_bbDM_2017/datacard_bbDM2017_C_Merged_sp_0p7_tb_35_mXd_1_mA_600_ma_250.txt  --noFitAsimov  -v 0 --rMin 1e-07 --rMax 30 


# datacards_bbDM_2017_b/datacard_bbDM2017_1b_SR_sp_0p7_tb_35_mXd_1_mA_600_ma_200.txt : 1.9375
# datacards_bbDM_2017_b/datacard_bbDM2017_2b_SR_sp_0p7_tb_35_mXd_1_mA_600_ma_200.txt : 0.6621
