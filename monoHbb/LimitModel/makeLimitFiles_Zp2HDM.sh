## makeLimitFiles2HDM_a.sh V1: 15 March 2022 
## Raman Khurana, Monika Mittal
## source makeLimitFiles2HDM_a.sh

## This script take the input as limit file, which has all the points 
## split the file into many small files as per scans, for 2HDM+a we have 7 scans at the moment 
## individual files are sorted as per parameters 
## only unique rows are accpeted, remaining are killed. 


inputScan=bin/scan_2d/limits_monoHbb_zp2hdm_combined_2017.txt

## -k1n is for field 1, -o for output, both syntax for -k are equivalent , -u  is to remove duplicate, i..e take unique entries 

## get mA=300,
ZpScan300=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mA_300.txt
cat ${inputScan} | gawk 'NF>2 && $1==300'   > ${ZpScan300}
sort  -k 2n ${ZpScan300} -o ${ZpScan300} -u 


## get mA=400,
ZpScan400=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mA_400.txt
cat ${inputScan} | gawk 'NF>2 && $1==400'   > ${ZpScan400}
sort  -k 2n ${ZpScan400} -o ${ZpScan400} -u 


## get mA=500,
ZpScan500=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mA_500.txt
cat ${inputScan} | gawk 'NF>2 && $1==500'   > ${ZpScan500}
sort  -k 2n ${ZpScan500} -o ${ZpScan500} -u 


## get mA=600,
ZpScan600=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mA_600.txt
cat ${inputScan} | gawk 'NF>2 && $1==600'   > ${ZpScan600}
sort  -k 2n ${ZpScan600} -o ${ZpScan600} -u 


## get mA=700,
ZpScan700=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mA_700.txt
cat ${inputScan} | gawk 'NF>2 && $1==700'   > ${ZpScan700}
sort  -k 2n ${ZpScan700} -o ${ZpScan700} -u 


## get mA=800,
ZpScan800=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mA_800.txt
cat ${inputScan} | gawk 'NF>2 && $1==800'   > ${ZpScan800}
sort  -k 2n ${ZpScan800} -o ${ZpScan800} -u 


## get mA=900,
ZpScan900=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mA_900.txt
cat ${inputScan} | gawk 'NF>2 && $1==900'   > ${ZpScan900}
sort  -k 2n ${ZpScan900} -o ${ZpScan900} -u 


## get mA=1000,
ZpScan1000=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mA_1000.txt
cat ${inputScan} | gawk 'NF>2 && $1==1000'   > ${ZpScan1000}
sort  -k 2n ${ZpScan1000} -o ${ZpScan1000} -u 


## get ma vs mA scan for tan beta = 1 , sin theta = 0.35 concat of above three files 
mZpvsmAScan=bin/scan_2d/limits_monoHbb_Zp2hdmScan_mZpvsmA.txt
cat ${inputScan} | gawk 'NF>2' > ${mZpvsmAScan}
sort  -k1n -k2n  ${mZpvsmAScan} -o  ${mZpvsmAScan} -u 
