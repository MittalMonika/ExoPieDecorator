#!/bin/bash


samples_2hdma=(2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1000-MH4-150-MH2-1000-MHC-1000 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1000-MH4-250-MH2-1000-MHC-1000 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1000-MH4-350-MH2-1000-MHC-1000 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1000-MH4-400-MH2-1000-MHC-1000 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1000-MH4-500-MH2-1000-MHC-1000 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1100-MH4-250-MH2-1100-MHC-1100 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1100-MH4-350-MH2-1100-MHC-1100 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1100-MH4-500-MH2-1100-MHC-1100 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1200-MH4-150-MH2-1200-MHC-1200 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1200-MH4-250-MH2-1200-MHC-1200 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1200-MH4-350-MH2-1200-MHC-1200 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1200-MH4-500-MH2-1200-MHC-1200 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1300-MH4-150-MH2-1300-MHC-1300 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1300-MH4-250-MH2-1300-MHC-1300 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1300-MH4-350-MH2-1300-MHC-1300 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1300-MH4-500-MH2-1300-MHC-1300 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1400-MH4-150-MH2-1400-MHC-1400 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1400-MH4-250-MH2-1400-MHC-1400 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1400-MH4-350-MH2-1400-MHC-1400 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1400-MH4-450-MH2-1400-MHC-1400 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1500-MH4-150-MH2-1500-MHC-1500 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1500-MH4-250-MH2-1500-MHC-1500 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1500-MH4-400-MH2-1500-MHC-1500 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1600-MH4-150-MH2-1600-MHC-1600 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1600-MH4-250-MH2-1600-MHC-1600 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1600-MH4-350-MH2-1600-MHC-1600 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-200-MH4-100-MH2-200-MHC-200 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-200-MH4-150-MH2-200-MHC-200 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-300-MH4-100-MH2-300-MHC-300 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-300-MH4-150-MH2-300-MHC-300 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-400-MH4-100-MH2-400-MHC-400 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-400-MH4-150-MH2-400-MHC-400 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-400-MH4-250-MH2-400-MHC-400 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-500-MH4-150-MH2-500-MHC-500 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-500-MH4-200-MH2-500-MHC-500 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-500-MH4-250-MH2-500-MHC-500 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-500-MH4-300-MH2-500-MHC-500 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-600-MH4-250-MH2-600-MHC-600 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-600-MH4-300-MH2-600-MHC-600 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-600-MH4-350-MH2-600-MHC-600 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-700-MH4-250-MH2-700-MHC-700 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-700-MH4-300-MH2-700-MHC-700 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-700-MH4-350-MH2-700-MHC-700 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-700-MH4-400-MH2-700-MHC-700 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-800-MH4-250-MH2-800-MHC-800 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-800-MH4-300-MH2-800-MHC-800 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-800-MH4-350-MH2-800-MHC-800 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-800-MH4-400-MH2-800-MHC-800 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-800-MH4-500-MH2-800-MHC-800 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-900-MH4-300-MH2-900-MHC-900 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-900-MH4-350-MH2-900-MHC-900 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-900-MH4-400-MH2-900-MHC-900 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-900-MH4-500-MH2-900-MHC-900)

#samples_2hdma=(2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-600-MH4-200-MH2-600-MHC-600 2HDMa-gg-sinp-0p35-tanb-1-mXd-10-MH3-1000-MH4-250-MH2-1000-MHC-1000)


echo "sinp tanb dm mh3 mh4 mh2 mhc twosigdown onesigdown exp onesigup twosigup observed" > limits_2hdma_mass.txt


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

    cp combined_tmpl.txt thdma/monoHbb_datacard_2016_2hdma_C_allregion_${k}.txt
    sed -i 's/XX-SIGNAL-XX/'${k}'/g' thdma/monoHbb_datacard_2016_2hdma_C_allregion_${k}.txt

    
done
