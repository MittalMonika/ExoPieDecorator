#!/bin/bash


samples_2hdma=( 2HDMa-sinp-0p35-tanb-0p5-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p5-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p5-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p5-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p5-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p5-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p5-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p5-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p8-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p8-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p8-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p8-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p8-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p8-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p8-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-0p8-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-10p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-10p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-10p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-10p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-10p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-10p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-10p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-10p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p5-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p5-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p5-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p5-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p5-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p5-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p5-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-1p5-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-20p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-20p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-20p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-20p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-20p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-20p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-20p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-20p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-2p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-2p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-2p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-2p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-2p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-2p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-2p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-2p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-30p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-30p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-30p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-30p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-30p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-30p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-30p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-30p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-40p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-40p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-40p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-40p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-40p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-40p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-40p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-40p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-4p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-4p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-4p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-4p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-4p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-4p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-4p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-4p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-50p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-50p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-50p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-50p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-50p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-50p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-50p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-50p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-6p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-6p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-6p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-6p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-6p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-6p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-6p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-6p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-8p0-mXd-10-MH3-600-MH4-100-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-8p0-mXd-10-MH3-600-MH4-150-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-8p0-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-8p0-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-8p0-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-8p0-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-8p0-mXd-10-MH3-600-MH4-400-MH2-600-MHC-600 2HDMa-sinp-0p35-tanb-8p0-mXd-10-MH3-600-MH4-500-MH2-600-MHC-600 )

echo "sinp tanb dm mh3 mh4 mh2 mhc twosigdown onesigdown exp onesigup twosigup observed" > limits_2hdma_tanb.txt


for k in "${samples_2hdma[@]}"; do
    echo $k > tmp.txt
    mass_dm=`sed '/mXd-/!d;s//&\n/;s/.*\n//;:a;/-MH3/bb;$!{n;ba};:b;s//\n&/;P;D' tmp.txt`
    mass_h3=`sed '/MH3-/!d;s//&\n/;s/.*\n//;:a;/-MH4/bb;$!{n;ba};:b;s//\n&/;P;D' tmp.txt`
    mass_h4=`sed '/MH4-/!d;s//&\n/;s/.*\n//;:a;/-MH2/bb;$!{n;ba};:b;s//\n&/;P;D' tmp.txt`
    sinp_tmp=`sed '/sinp-/!d;s//&\n/;s/.*\n//;:a;/-tanb/bb;$!{n;ba};:b;s//\n&/;P;D' tmp.txt`
    tanb_tmp=`sed '/tanb-/!d;s//&\n/;s/.*\n//;:a;/-mXd/bb;$!{n;ba};:b;s//\n&/;P;D' tmp.txt`
    dot="."
    sinp=${sinp_tmp/p/$dot}
    tanb=${tanb_tmp/p/$dot}
    rm -f tmp.txt
    branchingratio='1.0'
    echo $mass_dm
    echo $mass_h3
    echo $mass_h4
    echo $sinp
    echo $tanb

    cp combined_tmpl.txt combined.txt
    sed -i 's/XX-SIGNAL-XX/'${k}'/g' combined.txt

    #Computing limits                                                                                                                                                                 
    combine -M Asymptotic combined.txt  --rAbsAcc 0 --rMax 30 --verbose 3 | tee limits_tmp.txt
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

    echo "${sinp} ${tanb} ${mass_dm} ${mass_h3} ${mass_h4} ${mass_h3} ${mass_h3} ${twosigdown} ${onesigdown} ${exp} ${onesigup} ${twosigup} ${observed}" >> limits_2hdma_tanb.txt        
done
