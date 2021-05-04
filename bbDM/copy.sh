cp index.php plots_limit
cp index.php plots_limit/postfitOverlay
cp index.php plots_limit/pulls
cp index.php plots_limit/limitcomp
cp index.php plots_limit/Stack

rm -rf /afs/cern.ch/work/k/khurana/public/AnalysisStuff/bbDM/LimitStuff/plots_limit/Stack
cp -r plots_limit/Stack /afs/cern.ch/work/k/khurana/public/AnalysisStuff/bbDM/LimitStuff/plots_limit/Stack

rm -rf /afs/cern.ch/work/k/khurana/public/AnalysisStuff/bbDM/LimitStuff/plots_limit/pulls 
cp -r plots_limit/pulls /afs/cern.ch/work/k/khurana/public/AnalysisStuff/bbDM/LimitStuff/plots_limit/pulls

