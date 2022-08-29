from ROOT import *
from collections import defaultdict
from os import getenv
from array import array
from sys import argv

f_mlfit = TFile(argv[1],'READ')
  
h_postfit_sig = f_mlfit.Get("shapes_fit_s/sig/signal")
print h_postfit_sig.Integral()
