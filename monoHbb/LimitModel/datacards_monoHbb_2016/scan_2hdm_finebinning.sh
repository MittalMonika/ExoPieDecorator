#!/bin/bash


samples_2hdm=(ZpA0-600-300 ZpA0-600-400 ZpA0-800-300 ZpA0-800-400 ZpA0-800-500 ZpA0-800-600 ZpA0-1000-300 ZpA0-1000-400 ZpA0-1000-500 ZpA0-1000-600 ZpA0-1000-700 ZpA0-1000-800 ZpA0-1200-300 ZpA0-1200-400 ZpA0-1200-500 ZpA0-1200-600 ZpA0-1200-700 ZpA0-1200-800 ZpA0-1400-300 ZpA0-1400-400 ZpA0-1400-500 ZpA0-1400-600 ZpA0-1400-700 ZpA0-1400-800 ZpA0-1700-300 ZpA0-1700-400 ZpA0-1700-500 ZpA0-1700-600 ZpA0-1700-700 ZpA0-1700-800 ZpA0-2000-300 ZpA0-2000-400 ZpA0-2000-400 ZpA0-2000-500 ZpA0-2000-600 ZpA0-2000-700 ZpA0-2000-800 ZpA0-2500-300 ZpA0-2500-400 ZpA0-2500-500 ZpA0-2500-600 ZpA0-2500-700 ZpA0-2500-800 ZpA0-2750-300 ZpA0-2750-500 ZpA0-2750-800 ZpA0-3000-300 ZpA0-3000-500 ZpA0-3000-800 ZpA0-3500-300 ZpA0-3500-500 ZpA0-3500-800 ZpA0-4000-300 ZpA0-4000-500 ZpA0-4000-800 )
#samples_2hdm=(ZpA0-3000-300)

echo "med dm twosigdown onesigdown exp onesigup twosigup observed" > limits_2hdm_finebinning.txt


for k in "${samples_2hdm[@]}"; do
    mediator=${k#'ZpA0-'}
    dmmass=${mediator#*-}
    mediator=${mediator%-*}
    branchingratio='1.00'
    
    cp combined_tmpl_finebinning.txt combined.txt
    sed -i 's/XX-SIGNAL-XX/'${k}'/g' combined.txt
    
    #Computing limits
    combine -M Asymptotic combined.txt  --rAbsAcc 0 --rMax 10 | tee limits_tmp.txt
    #Parsing results into textfile
    observed=`cat limits_tmp.txt | grep 'Observed Limit: r < ' | awk '{print $5}'`
    twosigdown=`cat limits_tmp.txt | grep 'Expected  2.5%: r <' | awk '{print $5}'`
    onesigdown=`cat limits_tmp.txt | grep 'Expected 16.0%: r <' | awk '{print $5}'`
    exp=`cat limits_tmp.txt | grep 'Expected 50.0%: r <' | awk '{print $5}'`
    onesigup=`cat limits_tmp.txt | grep 'Expected 84.0%: r <' | awk '{print $5}'`
    twosigup=`cat limits_tmp.txt | grep 'Expected 97.5%: r <' | awk '{print $5}'`

    #Applying branching ratio
    observed=`echo "scale=7 ; $observed / $branchingratio" | bc`
    twosigdown=`echo "scale=7 ; $twosigdown / $branchingratio" | bc`
    onesigdown=`echo "scale=7 ; $onesigdown / $branchingratio" | bc`
    exp=`echo "scale=7 ; $exp / $branchingratio" | bc`
    onesigup=`echo "scale=7 ; $onesigup / $branchingratio" | bc`
    twosigup=`echo "scale=7 ; $twosigup / $branchingratio" | bc`

    echo "${mediator} ${dmmass} ${twosigdown} ${onesigdown} ${exp} ${onesigup} ${twosigup} ${observed}" >> limits_2hdm_finebinning.txt
done
