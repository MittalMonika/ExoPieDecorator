## makeLimitFiles2HDM_a.sh V1: 15 March 2022 
## Raman Khurana, Monika Mittal
## source makeLimitFiles2HDM_a.sh

## This script take the input as limit file, which has all the points 
## split the file into many small files as per scans, for 2HDM+a we have 7 scans at the moment 
## individual files are sorted as per parameters 
## only unique rows are accpeted, remaining are killed. 


inputScan=bin/Run2Combo_C/limits_monoHbb_2hdma_C_1718.txt

## -k1n is for field 1, -o for output, both syntax for -k are equivalent , -u  is to remove duplicate, i..e take unique entries 

## get ma=150, tanbeta = 1, 
mAScan150=bin/scan_2d_13May2022/limits_monoHbb_2hdmaScan_ma_150_tanbeta_1p0_sinth_0p35.txt
cat ${inputScan} | gawk 'NF>5 && $1==150 && $3==1 {print $1" "$2" "$6" "$7" "$8" "$9" "$10" "$11}'  > ${mAScan150}
sort  -k 2n ${mAScan150} -o ${mAScan150} -u 

## get ma=250, tanbeta = 1,
mAScan250=bin/scan_2d_13May2022/limits_monoHbb_2hdmaScan_ma_250_tanbeta_1p0_sinth_0p35.txt
cat ${inputScan} | gawk 'NF>5 && $1==250 && $3==1 {print $1" "$2" "$6" "$7" "$8" "$9" "$10" "$11}'  > ${mAScan250}
sort  -k 2n ${mAScan250} -o ${mAScan250} -u 


## get ma=350, tanbeta = 1,
mAScan350=bin/scan_2d_13May2022/limits_monoHbb_2hdmaScan_ma_350_tanbeta_1p0_sinth_0p35.txt
cat ${inputScan} | gawk 'NF>5 && $1==350 && $3==1 {print $1" "$2" "$6" "$7" "$8" "$9" "$10" "$11}'  > ${mAScan350}
sort  -k 2n ${mAScan350} -o ${mAScan350} -u


## get ma vs mA scan for tan beta = 1 , sin theta = 0.35 concat of above three files 
mAvsmaScan=bin/scan_2d_13May2022/limits_monoHbb_2hdmaScan_ma_vs_mA_tanbeta_1p0_sinth_0p35.txt
cat ${inputScan} | gawk 'NF>5 && $3==1 && $4==0.35  {print $1" "$2" "$6" "$7" "$8" "$9" "$10" "$11}' > ${mAvsmaScan}
sort  -k1n -k2n  ${mAvsmaScan} -o  ${mAvsmaScan} -u 

## get tan beta scan for ma=150 and mA = 600 GeV 
tanbetaScan150=bin/scan_2d_13May2022/limits_monoHbb_2hdmaScan_tanbetaScan_ma_150_mA_600_sinth_0p35.txt
cat ${inputScan} | gawk 'NF>5 && $1==150 && $2==600  {print $1" "$3" "$6" "$7" "$8" "$9" "$10" "$11}' > ${tanbetaScan150}
sort -k2n ${tanbetaScan150} -o ${tanbetaScan150} -u 

## get tan beta scan for ma=250 and mA = 600 GeV 
tanbetaScan250=bin/scan_2d_13May2022/limits_monoHbb_2hdmaScan_tanbetaScan_ma_250_mA_600_sinth_0p35.txt
cat ${inputScan} | gawk 'NF>5 && $1==250 && $2==600  {print $1" "$3" "$6" "$7" "$8" "$9" "$10" "$11}' > ${tanbetaScan250}
sort -k2n ${tanbetaScan250} -o ${tanbetaScan250} -u


## get sin theta scan for ma=200 and mA = 600 GeV and tanbeta = 1
sinthetaScan200=bin/scan_2d_13May2022/limits_monoHbb_2hdmaScan_sinthetaScan_ma_200_mA_600_tanbeta_1.txt
cat ${inputScan} | gawk 'NF>5 && $1==200 && $2==600  {print $1" "$4" "$6" "$7" "$8" "$9" "$10" "$11}' > ${sinthetaScan200}
sort -k2n ${sinthetaScan200} -o ${sinthetaScan200} -u 

