import os 
import yaml 
import LimitPlotter as lp 



f = open("Scans2HDMa.yaml")
doc = yaml.safe_load(f)



a = lp.LimitPlotter("2hdma")

a.TextFileToRootGraphs1D(doc['2hdma']['oned']['tanbetaScan150'])
a.SaveLimitPdf1D()


a.TextFileToRootGraphs1D(doc['2hdma']['oned']['tanbetaScan250'])
a.SaveLimitPdf1D()


a.TextFileToRootGraphs1D(doc['2hdma']['oned']['sinthetaScanma200'])
a.SaveLimitPdf1D()

a.TextFileToRootGraphs1D(doc['2hdma']['oned']['mAScanma150'])
a.SaveLimitPdf1D()

a.TextFileToRootGraphs1D(doc['2hdma']['oned']['mAScanma250'])
a.SaveLimitPdf1D()

a.TextFileToRootGraphs1D(doc['2hdma']['oned']['mAScanma350'])
a.SaveLimitPdf1D()



os.system("cp plots_limit/scan_2d/* /eos/user/m/mmittal/www/MonoHbb/scan_2d/")
#a.TextFileToRootGraphs1D(tanb250)
#a.SaveLimitPdf1D()
