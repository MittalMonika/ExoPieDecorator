## makeLimitFiles2HDM_a.sh V1: 15 March 2022 
## Raman Khurana, Monika Mittal
## source makeLimitFiles2HDM_a.sh

## This script take the input as limit file, which has all the points 
## split the file into many small files as per scans, for 2HDM+a we have 7 scans at the moment 
## individual files are sorted as per parameters 
## only unique rows are accpeted, remaining are killed. 


inputScan=bin/scan_2d/limits_monoHbb_zpb_combined_2017.txt

## -k1n is for field 1, -o for output, both syntax for -k are equivalent , -u  is to remove duplicate, i..e take unique entries 

## get mChi=1
ZpScan1=bin/scan_2d/limits_monoHbb_ZpBScan_mChi_1.txt
cat ${inputScan} | gawk 'NF>2 && $1==1'   > ${ZpScan1}
sort  -k 2n ${ZpScan1} -o ${ZpScan1} -u 


## get mChi=100
ZpScan100=bin/scan_2d/limits_monoHbb_ZpBScan_mChi_100.txt
cat ${inputScan} | gawk 'NF>2 && $1==100'   > ${ZpScan100}
sort  -k 2n ${ZpScan100} -o ${ZpScan100} -u 


## get mChi=200
ZpScan200=bin/scan_2d/limits_monoHbb_ZpBScan_mChi_200.txt
cat ${inputScan} | gawk 'NF>2 && $1==200'   > ${ZpScan200}
sort  -k 2n ${ZpScan200} -o ${ZpScan200} -u 


## get mChi=400
ZpScan400=bin/scan_2d/limits_monoHbb_ZpBScan_mChi_400.txt
cat ${inputScan} | gawk 'NF>2 && $1==400'   > ${ZpScan400}
sort  -k 2n ${ZpScan400} -o ${ZpScan400} -u 


## get mZp vs mChi scan 
mZpvsmChiScan=bin/scan_2d/limits_monoHbb_ZpBScan_mZpvsmChi.txt
cat ${inputScan} | gawk 'NF>2' > ${mZpvsmChiScan}
sort  -k1n -k2n  ${mZpvsmChiScan} -o  ${mZpvsmChiScan} -u 
