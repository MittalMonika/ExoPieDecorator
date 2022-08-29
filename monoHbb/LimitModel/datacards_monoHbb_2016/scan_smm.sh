#!/bin/bash


#samples_smm=(SMM-10-1 SMM-10-4 SMM-10-25 SMM-10-50 SMM-10-100 SMM-10-500 SMM-100-25 SMM-100-1 SMM-1000-1 SMM-1000-25 SMM-1000-1000 SMM-1000-50 SMM-1000-5 SMM-15-1 SMM-15-100 SMM-15-25 SMM-15-5 SMM-20-1 SMM-20-100 SMM-20-25 SMM-20-500 SMM-200-25 SMM-200-5 SMM-200-50 SMM-300-1 SMM-300-100 SMM-300-1000 SMM-300-25 SMM-300-5 SMM-50-1 SMM-50-100 SMM-50-24 SMM-50-5 SMM-50-500 SMM-500-1 SMM-500-1000 SMM-500-25 SMM-500-5 SMM-700-1 SMM-700-1000)
samples_smm=(SMM-10-1 SMM-100-1 SMM-1000-1 SMM-15-1 SMM-20-1 SMM-300-1 SMM-50-1 SMM-500-1 SMM-700-1)

echo "med dm twosigdown onesigdown exp onesigup twosigup observed" > limits_smm.txt


for k in "${samples_smm[@]}"; do
    mediator=${k#'SMM-'}
    dmmass=${mediator#*-}
    mediator=${mediator%-*}
    branchingratio='1.0'
    
    cp combined_tmpl.txt combined.txt
    sed -i 's/XX-SIGNAL-XX/'${k}'/g' combined.txt
    
    #Computing limits
    combine -M Asymptotic combined.txt  --rAbsAcc 0 --rMax 15  | tee limits_tmp.txt
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

    echo "${mediator} ${dmmass} ${twosigdown} ${onesigdown} ${exp} ${onesigup} ${twosigup} ${observed}" >> limits_smm.txt
done
