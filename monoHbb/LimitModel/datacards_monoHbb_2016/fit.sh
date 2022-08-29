combine -M MaxLikelihoodFit ${1} --saveShapes --saveWithUncertainties  | tee log_fit.txt 2>&1
#combine -M MaxLikelihoodFit ${1} --saveShapes --saveWithUncertainties --setPhysicsModelParameters mask_sig=1 --minimizerAlgo Minuit2 | tee log_fit.txt 2>&1

#combine -M MaxLikelihoodFit ${1} --saveShapes -t-1 --saveWithUncertainties  --minimizerAlgo Minuit | tee log_fit.txt
#combine -M MaxLikelihoodFit ${1} --saveShapes -t-1 --saveWithUncertainties  --minimizerAlgo Minuit2 | tee log_fit.txt
