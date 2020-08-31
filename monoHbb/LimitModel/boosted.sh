python RunLimits.py -c --model 2hdma_all --region "SR TOPE TOPMU WE WMU ZEE ZMUMU"
python RunLimits.py -A -L -v 0 -i monohbb2017_datacardslist_B_2hdma_all.txt --savepdf --outlog "saving boosted limit plot version to show in the meeting,"
python RunLimits.py --pulls --runmode cronly -i monohbb2017_datacardslist_B_2hdma.txt --outlog "pulls for cr only: for the meeting boosted"
python RunLimits.py --pulls --runmode asimov -i monohbb2017_datacardslist_B_2hdma.txt --outlog " pulls for asimov: version for the meeting"
python RunLimits.py --pulls --runmode data -i monohbb2017_datacardslist_B_2hdma.txt --outlog " pulls for asimov: version for the meeting"
python transferfactor.py ## for now like this, and will be added in the main macro later 
python RunLimits.py --impact --runmode data -i monohbb2017_datacardslist_B_2hdma.txt
