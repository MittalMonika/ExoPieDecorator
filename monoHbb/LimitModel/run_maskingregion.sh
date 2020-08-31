datacard=datacards_monoHbb_2017/datacard_monoHbb2017_B_Merged_sp_0p35_tb_1p0_mXd_10_mA_1000_ma_150.txt
wsname=datacards_monoHbb_2017/datacard_monoHbb2017_B_Merged_sp_0p35_tb_1p0_mXd_10_mA_1000_ma_150.root
text2workspace.py ${datacard} --channel-masks
combine -M FitDiagnostics  ${wsname} --saveShapes --saveWithUncertainties --setParameters mask_WE=1,mask_WMU=1
mv fitDiagnostics.root fitDiagnostics_maskWE_maskWMU.root
python diffNuisances.py fitDiagnostics_maskWE_maskMU.root --abs --all -g pulls_maskWE_maskWMU.root
root -l -b -q PlotPulls.C\(\"pulls_maskWE_maskWMU.root\",\"mask_checks/\",\"merged\"\)
#combine -M FitDiagnostics  ${wsname} --saveShapes --saveWithUncertainties --setParameters mask_WMU=1
#mv fitDiagnostics.root fitDiagnostics_maskWMU.root

