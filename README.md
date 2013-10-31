Changing Local Pythia8 Version
------------------------------
(This does not work with crab, local only)
This should no longer be needed since CMSSW_5_3_13_cand1

        scram b clean                                                                       
        sed -i "s/153/175/g" ../config/toolbox/slc5_amd64_gcc462/tools/selected/pythia8.xml 
        sed -i "s/462/472/g" ../config/toolbox/slc5_amd64_gcc462/tools/selected/pythia8.xml 
        scram setup pythia8
        cmsenv
        echo $PYTHIA8DATA                                                          
        cvs co -r CMSSW_5_3_8 GeneratorInterface/Pythia8Interface                           
        scram b

Settings
--------
Driver macros are all tuned to produce signal for 2012, S10 pileup, 5_3_X conditions.
Currently, the available gen fragments are:
  * LO Pythia8
  * NLO POWHEG + Pythia8 (still working on tuning)
  * LO VBF Pythia8

Newest Instructions
-------------------
Use CMSSW_5_3_13_cand1, this has two version of pythia8 installed (notably 8.175).
Quick setup:
        
        cmsrel CMSSW_5_3_13_cand1
        cd CMSSW_5_3_13_cand1/src
        crabenv
        git cms-addpkg GeneratorInterface/Pythia8Interface
        git cms-addpkg Configuration/Generator
        git clone https://github.com/brovercleveland/MC_Gen
        cp MC_Gen/PYTHIA8_POWHEG_H_Zg_8TeV_cff.py Configuration/Generator/python/.
        scram b -j 9
        cd MC_Gen

In CMSSW_5_3_13_cand1, to invoke p8.175, simply say `Pythia8175HadronizerFilter` in the gen fragment



