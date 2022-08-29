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


'''

zp2hdm = lp.LimitPlotter("zp2hdm")

zp2hdm.TextFileToRootGraphs1D(doc['zp2hdm']['oned']['mZpScanmA300'])
zp2hdm.SaveLimitPdf1D()


zp2hdm.TextFileToRootGraphs1D(doc['zp2hdm']['oned']['mZpScanmA400'])
zp2hdm.SaveLimitPdf1D()

zp2hdm.TextFileToRootGraphs1D(doc['zp2hdm']['oned']['mZpScanmA500'])
zp2hdm.SaveLimitPdf1D()

zp2hdm.TextFileToRootGraphs1D(doc['zp2hdm']['oned']['mZpScanmA600'])
zp2hdm.SaveLimitPdf1D()

zp2hdm.TextFileToRootGraphs1D(doc['zp2hdm']['oned']['mZpScanmA700'])
zp2hdm.SaveLimitPdf1D()

zp2hdm.TextFileToRootGraphs1D(doc['zp2hdm']['oned']['mZpScanmA800'])
zp2hdm.SaveLimitPdf1D()

zp2hdm.TextFileToRootGraphs1D(doc['zp2hdm']['oned']['mZpScanmA900'])
zp2hdm.SaveLimitPdf1D()


zp2hdm.TextFileToRootGraphs1D(doc['zp2hdm']['oned']['mZpScanmA1000'])
zp2hdm.SaveLimitPdf1D()


zpb = lp.LimitPlotter("zpb")

zpb.TextFileToRootGraphs1D(doc['zpb']['oned']['mZpScanmChi1'])
zpb.SaveLimitPdf1D()


zpb.TextFileToRootGraphs1D(doc['zpb']['oned']['mZpScanmChi100'])
zpb.SaveLimitPdf1D()


zpb.TextFileToRootGraphs1D(doc['zpb']['oned']['mZpScanmChi200'])
zpb.SaveLimitPdf1D()

zpb.TextFileToRootGraphs1D(doc['zpb']['oned']['mZpScanmChi400'])
zpb.SaveLimitPdf1D()

'''

os.system("cp plots_limit/scan_2d_13May2022/* /eos/user/m/mmittal/www/MonoHbb/scan_2d_13May2022/")
#a.TextFileToRootGraphs1D(tanb250)
#a.SaveLimitPdf1D()
