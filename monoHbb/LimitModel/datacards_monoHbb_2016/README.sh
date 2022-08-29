#CREATING WORKSPACE

text2workspace.py test.txt

#PERFORM S+B FIT TO DATA AND SAVE WORKSPACE+SNAPSHOT 
combine test.root -M MultiDimFit --saveWorkspace  -n PostFit 

#CALCULATE LIMIT FOR ALL NUISANCES FIXED TO THEIR VALUES FROM THE PREVIOUS S+B FIT TO DATA (Result: 0.816406)
combine higgsCombinePostFit.MultiDimFit.mH120.root --snapshotName MultiDimFit -M Asymptotic  -n randomtest --bypassFrequentistFit   --redefineSignalPOIs r --freezeNuisanceGroups all | tee postfit_all_frozen.dat
#CALCULATE FULL ASYMPTOTIC LIMIT AFTER THE PREVIOUS S+B FIT TO DATA (Result: 0.863281)
combine higgsCombinePostFit.MultiDimFit.mH120.root --snapshotName MultiDimFit -M Asymptotic  -n randomtest --bypassFrequentistFit  --redefineSignalPOIs r  | tee postfit_nothing_frozen.dat

#PERFORM S+B FIT TO TOY AND SAVE WORKSPACE+SNAPSHOT 
combine test.root -M MultiDimFit -t -1 --saveWorkspace  -n PreFit 

#CALCULATE LIMIT FOR ALL NUISANCES FIXED TO THEIR VALUES FROM THE PREVIOUS S+B FIT TO TOY (Result: 0.736328)
combine higgsCombinePreFit.MultiDimFit.mH120.root --snapshotName MultiDimFit -M Asymptotic  -n randomtest  --bypassFrequentistFit --redefineSignalPOIs r --freezeNuisanceGroups all | tee prefit_all_frozen.dat

#CALCULATE FULL ASYMPTOTIC LIMIT AFTER THE PREVIOUS S+B FIT TO TOY (Result: 0.771484)
combine higgsCombinePreFit.MultiDimFit.mH120.root --snapshotName MultiDimFit -M Asymptotic  -n randomtest  --bypassFrequentistFit --redefineSignalPOIs r  | tee prefit_nothing_frozen.dat
