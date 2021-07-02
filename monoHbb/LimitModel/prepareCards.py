import os
import yaml
import numpy as np
from collections import OrderedDict
import pandas as pd
import sys, optparse,argparse

## ----- command line argument
usage = "python -y 2017 -c R -reg ['SR']"
parser = argparse.ArgumentParser(description=usage)
parser.add_argument("-y", "--year", dest="year", default="2017")
parser.add_argument("-m", "--model", dest="model", default="THDMa")
parser.add_argument("-c", "--category",  dest="category",default="B")
# parser.add_argument("-r", "--region", dest="region", default=['SR'])
parser.add_argument("-reg", nargs="+", default=["a", "b"])
args = parser.parse_args()

year     = args.year
category = args.category
regions  = args.reg
modelName = args.model


print (year, category, regions)
if category=='R':
    f = open('datacard_tempalate_Resolved.ymal')
else:
    f = open('datacard_tempalate_boosted.ymal')
doc = yaml.safe_load(f)

signalFile = open('datacard_tempalate_signal.ymal','r')
signalDoc  = yaml.safe_load(signalFile)

os.system('mkdir cards')
top_ = '''
imax *  number of channels
jmax *  number of backgrounds

kmax *  number of nuisance parameters (sources of systematical uncertainties)
'''

def getUpperPart2(reg,cat):
	top_= 'shapes * '+reg+' AllMETHistos.root  monoHbb2017_'+cat+'_'+reg+'_$PROCESS monoHbb2017_'+cat+'_'+reg+'_$PROCESS_$SYSTEMATIC'
	return top_

# def getUpperPart2(reg,cat):
# 	top_= 'shapes * '+reg+' AllMETHistos.root  monoHbb2017_'+cat+'_'+reg+'_bdtscore'+'_$PROCESS monoHbb2017_'+cat+'_'+reg+'_bdtscore'+'_$PROCESS_$SYSTEMATIC'
# 	return top_

def getUpperPart3(reg):
	top_ = 'bin '+reg
	# observation -1
	return top_

def getDic(dics,name):
	values=''
	itm=dics[name]
	# print name ,itm[0].split()
	values = itm[0].split()
	# for key, value in dics:
	# 	if key==name:
	# 		itm=np.array(value[0].split())
	return values

def getSyst(lists):
	syst=OrderedDict()
	# print getDic(lists,'bin')
	reg     = getDic(lists,'bin')[0].split(':')[0]
	length  = int(getDic(lists,'bin')[0].split(':')[1])
	nuis    = getDic(lists,'Nuisances')
	unc     = getDic(lists,'SystUnclnN')
	for n, u in zip(nuis,unc):
		# print 'testing ', n , u
		syst[str(n)]=[u] * length

	return syst




def getProcSyst(lists):
	nuisancesForCard=OrderedDict()
	# print 'testing ', lists
	NuisForProc = lists['NuisForProc']
	uncertainties  = lists['UnclnN']
	procs   = getDic(lists,'Process')

	# print 'NuisForProc',NuisForProc
	for ij, istring in enumerate(uncertainties):
		nuis = istring.split()[0]
		syst = istring.split()[1]
		# print 'nuis, syst',nuis, syst
		values=[]
		if syst=='shape':values.append('shape')
		else:values.append('lnN')
		
		for proc in procs:
			# print nuis,NuisForProc[ij]

			if proc in  (NuisForProc[ij])[nuis]:
				if syst=='shape':
					values.append(1)
				else:
					values.append(syst)
			else:values.append('-')
		nuisancesForCard[nuis]=values

	# print ('nuisancesForCard', nuisancesForCard)
	return nuisancesForCard





def getbinProcRate(lists):
	binProcRate = OrderedDict()
	reg     = getDic(lists,'bin')[0].split(':')[0]
	length  = int(getDic(lists,'bin')[0].split(':')[1])
	procs   = getDic(lists,'Process')
	procs1  = getDic(lists,'process1')

	rates   = [getDic(lists,'rate')[0].split(':')[0]] * length

	binProcRate['bin']      =  [reg] * length
	binProcRate['process']  =  procs
	binProcRate['process1'] =  procs1
	binProcRate['rate']     = rates
	# print 'binProcRate', binProcRate

	# print (lists['rateTest'])

	return binProcRate

def getProcRate(lists):
	binProcRate = OrderedDict()
	reg     = getDic(lists,'bin')[0].split(':')[0]
	length  = int(getDic(lists,'bin')[0].split(':')[1])
	procs   = getDic(lists,'Process')
	procs1  = getDic(lists,'process1')

	rates   = [getDic(lists,'rate')[0].split(':')[0]] * length

	# binProcRate['bin']      =  [reg] * length
	# binProcRate['process']  =  procs
	binProcRate['process'] =  procs1
	binProcRate['rate']     = rates
	# print 'binProcRate', binProcRate

	# print (lists['rateTest'])

	return binProcRate


def getSignalHists(doc,model):
	parameters = doc[model]
	print ("parameters   :  %s"%parameters)
	samples  = []
	if model=="THDMa":
		tb_list  = parameters[0]['tb']
		st_list  = parameters[1]['st']
		ma_list  = parameters[2]['ma']
		mA_list  = parameters[3]['mA']

		# for tb in tb_list:
		# 	for st in st_list:
		# 		for ma in ma_list:
		# 			for mA in mA_list:
		# 				# print ('tb',tb,'st',st,'ma',ma,'mA',mA)
		# 				samp = 'ggF_sp_'+st+'_tb_'+tb+'_mXd_10_mA_'+str(mA)+'_ma_'+str(ma)
		# 				samples.append(samp)

		for ma in ma_list:
			for tb in tb_list:
				if int(ma)==350 or int(ma)==200:continue
				mA='600'
				st='0p35'
				samp = 'ggF_sp_'+st+'_tb_'+tb+'_mXd_10_mA_'+str(mA)+'_ma_'+str(ma)
				samples.append(samp)
			for st in st_list:
				if int(ma)!=200:continue
				mA='600'
				tb='1p0'
				samp = 'ggF_sp_'+st+'_tb_'+tb+'_mXd_10_mA_'+str(mA)+'_ma_'+str(ma)
				samples.append(samp)
			for mA in mA_list:
				if int(ma)==200:continue
				st='0p35'
				tb='1p0'
				samp = 'ggF_sp_'+st+'_tb_'+tb+'_mXd_10_mA_'+str(mA)+'_ma_'+str(ma)
				samples.append(samp)





	elif model=="ZpB":
		mchi_list = parameters[0]['mchi']
		mzp_list  = parameters[1]['mzp']
		for mzp in mzp_list:
			for mchi in mchi_list:
				isfill = False
				if  (int(mzp)==100 and (int(mchi)==1 or int(mchi)==50)):isfill=True
				if  (int(mzp)==200 and (int(mchi)==1 or int(mchi)==50 or int(mchi)==100 or int(mchi)==150)):isfill=True
				if  (int(mzp)==300 and int(mchi)==150):isfill=True
				if  (int(mzp)==350 and int(mchi)==50):isfill=True
				if  (int(mzp)==500 and (int(mchi)==1 or int(mchi)==100 or int(mchi)==200 or int(mchi)==400)):isfill=True
				if  (int(mzp)==650 and int(mchi)==50):isfill=True
				if  (int(mzp)==800 and int(mchi)==50):isfill=True
				if  (int(mzp)==1000 and (int(mchi)==1 or int(mchi)==100 or int(mchi)==200 or int(mchi)==400 or int(mchi)==600 or int(mchi)==800)):isfill=True
				if  (int(mzp)==1500 and (int(mchi)==1 or int(mchi)==100 or int(mchi)==200 or int(mchi)==400 or int(mchi)==600 or int(mchi)==800)):isfill=True
				if  (int(mzp)==2000 and (int(mchi)==1 or int(mchi)==100 or int(mchi)==200 or int(mchi)==400 or int(mchi)==600 or int(mchi)==800)):isfill=True
				if  (int(mzp)==2500 and (int(mchi)==1 or int(mchi)==100 or int(mchi)==200 or int(mchi)==400 or int(mchi)==600 or int(mchi)==800)):isfill=True
				if  (int(mzp)==3000 and (int(mchi)==1 or int(mchi)==100 or int(mchi)==200 )):isfill=True
				if  (int(mzp)==3500 and (int(mchi)==1 or int(mchi)==100)):isfill=True

				if isfill:
					samp = 'MZp_'+str(mzp)+'_Mchi_'+str(mchi)
					samples.append(samp)

	elif model=="ZpTHDM":
		mA_list = parameters[0]['mA']
		mzp_list  = parameters[1]['mzp']
		for mzp in mzp_list:
			for mA in mA_list:
				# print (mA,mzp)
				isfill=False
				if  (int(mzp)==1000 and (int(mA)==300 or int(mA)==800)):isfill=True
				if (int(mzp)==1200 and (int(mA)==300 or int(mA)==500 or int(mA)==900 or int(mA)==1000)):isfill=True
				if (int(mzp)==1400 and (int(mA)==300 or int(mA)==400 or int(mA)==500 or int(mA)==600 or int(mA)==800 or int(mA)==900 or int(mA)==1000 or int(mA)==1200)) :isfill=True
				if (int(mzp)==1700 and (int(mA)==300 or int(mA)==400 or int(mA)==500 or int(mA)==600 or int(mA)==700 or int(mA)==800 or int(mA)==900 or int(mA)==1000 or int(mA)==1200 or int(mA)==1400)) :isfill=True
				if (int(mzp)==2000 and (int(mA)==300 or int(mA)==700 or int(mA)==1000 or int(mA)==1200 or int(mA)==1400 or int(mA)==1600)):isfill=True
				if (int(mzp)==2500 and (int(mA)==300 or int(mA)==400 or int(mA)==500 or int(mA)==600 or int(mA)==700 or int(mA)==1000 or int(mA)==1200 or int(mA)==1600)):isfill=True
				if isfill:
					samp = 'MZp'+str(mzp)+'_MA0'+str(mA)
					samples.append(samp)
	print ("samples  ",samples)
	print ("total samples   ",len(samples))


	return samples




'''
=======================
START WRITING DATACARDS
=======================
'''


for reg in regions:

	# print getSyst(doc.items())
	# print (doc[reg])
	if reg=='SR':
		
		for sigHist in getSignalHists(signalDoc,modelName):

			outputfile = 'monoHbb_datacard_'+year+'_'+reg+'_'+category+'_'+sigHist+'.txt'
			outdir     = 'cards'
			df0 = pd.DataFrame(getbinProcRate(doc[reg]))
			# df1 = pd.DataFrame(getProcRate(doc[reg]))
			df0['process'] = df0['process'].replace(['signal'],sigHist)



			# df =  pd.DataFrame(getSyst(doc))
			df =  pd.DataFrame(getProcSyst(doc[reg]))
			# df = pd.merge(df0,df1)

			fout = open(outdir+'/'+outputfile,'w')
			p0 = df0.T.to_string(justify='right',index=True, header=False)
			# p1 = df1.T.to_string(justify='right',index=True, header=False)
			p = df.T.to_string(justify='right',index=True,header=False)

			part1 = top_
			part2 = getUpperPart2(reg,category)
			part3 = getUpperPart3(reg)

			fout.write(part1+'\n')
			fout.write('------------'+'\n')
			fout.write(part2+'\n')
			fout.write('------------'+'\n')
			fout.write(part3+'\n')
			fout.write('observation -1'+'\n')
			fout.write('------------'+'\n')
			fout.write(p0+'\n')
			# fout.write(p1+'\n')
			fout.write('------------'+'\n')
			fout.write(p+'\n')
			fout.close()

	else:
		outputfile = 'monoHbb_datacard_'+year+'_'+reg+'_'+category+'.txt'
		outdir     = 'cards'
		df0 = pd.DataFrame(getbinProcRate(doc[reg]))
		# df1 = pd.DataFrame(getProcRate(doc[reg]))
		df0['process'] = df0['process'].replace(['signal'],sigHist)



		# df =  pd.DataFrame(getSyst(doc))
		df =  pd.DataFrame(getProcSyst(doc[reg]))
		# df = pd.merge(df0,df1)

		fout = open(outdir+'/'+outputfile,'w')
		p0 = df0.T.to_string(justify='right',index=True, header=False)
		# p1 = df1.T.to_string(justify='right',index=True, header=False)
		p = df.T.to_string(justify='right',index=True,header=False)

		part1 = top_
		part2 = getUpperPart2(reg,category)
		part3 = getUpperPart3(reg)

		fout.write(part1+'\n')
		fout.write('------------'+'\n')
		fout.write(part2+'\n')
		fout.write('------------'+'\n')
		fout.write(part3+'\n')
		fout.write('observation -1'+'\n')
		fout.write('------------'+'\n')
		fout.write(p0+'\n')
		# fout.write(p1+'\n')
		fout.write('------------'+'\n')
		fout.write(p+'\n')
		fout.close()

'''
============================
replace process1 with process
============================
'''
os.system("sed -i'.bak' 's/process1/process /g' cards/*")
os.system("sed -i'.bak' 's/YEAR/"+year+"/g' cards/*")
os.system("rm -rf cards/*bak")

		 

