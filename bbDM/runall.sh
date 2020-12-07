rootfile=$1
year=$2

root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"1b\", \"RECREATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"
root -l -b -q PrepareWS_withnuisance.C"(\"bbDM\", \"2b\", \"UPDATE\", \"AllMETHistos\", \"$rootfile\", \"${year}\")"

python RunLimits.py -c --model 2hdma_all --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" --category=sr1
python RunLimits.py -c --model 2hdma_all --region "SR TOPE TOPMU WE WMU ZEE ZMUMU" --category=sr2
python RunLimits.py -c --model 2hdma_all --region "bbDM${year}_datacardslist_1b_2hdma_all.txt bbDM${year}_datacardslist_2b_2hdma_all.txt" --category=srall

cp bbDM_${year}_WS.root datacards_bbDM_${year}/bbDM_${year}_WS.root


python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_1b_2hdma_all.txt --category=sr1 --savepdf --outlog="running limits for 1b"
python RunLimits.py --savepdf --limitTextFile bin/limits_bbDM_1b_${year}.txt --outlog "saving pdf for 1b" --category=sr1


python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_2b_2hdma_all.txt --category=sr2 --savepdf --outlog="running limits for 2b"
python RunLimits.py --savepdf --limitTextFile bin/limits_bbDM_2b_${year}.txt --outlog "saving pdf for 2b" --category=sr2

python RunLimits.py -A -L -v 0 -i bbDM${year}_datacardslist_C_2hdma_all.txt --category=srall --savepdf --outlog="running limits for 1b+2b"
python RunLimits.py --savepdf --limitTextFile bin/limits_bbDM_combined_${year}.txt --outlog "saving pdf for 1b+2b" --category=srall
