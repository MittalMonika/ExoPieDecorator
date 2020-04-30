# Workflow for Limit Calculation
## Installation
Use the Higgs [Combine](http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/) page to install combine tool and for documentation

## Usage
- Make the AllMETHistos.root file using bbDM_combinedroot.py file
- Make the bbDM_WS.root file using PrepareWS_withSyst.C file
```root -l -b -q PrepareWS_withSyst.C```
- Run the dataCard_makeNrun.py file with create command for making the datacards
```python dataCard_makeNrun.py create```
- Run the dataCard_makeNrun.py file with run command for calculating the limit
```python dataCard_makeNrun.py run```
- Run limit_scanner.py file for getting the limit in text file
```python limit_scanner.py```
- Run limit_textTOgraph.py file to get the limit in root file
```python limit_textTOgraph.py```
- Run limit_plotter.py to get the plots:
```python limit_plotter.py```
