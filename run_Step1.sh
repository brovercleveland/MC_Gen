#!/bin/sh
#source /uscmst1/prod/sw/cms/bashrc prod
#scram pro CMSSW CMSSW_5_3_8
#cd CMSSW_5_3_8/src                     
#eval `scramv1 runtime -sh`
#mv ${_CONDOR_SCRATCH_DIR}/GeneratorInterface .
#scram b clean
#sed -i "s/153/175/g" ../config/toolbox/slc5_amd64_gcc462/tools/selected/pythia8.xml
#sed -i "s/462/472/g" ../config/toolbox/slc5_amd64_gcc462/tools/selected/pythia8.xml
#scram setup pythia8
#cvs co -r CMSSW_5_3_8 GeneratorInterface/Pythia8Interface
#scram b


cd ${_CONDOR_SCRATCH_DIR}
 

job=$1
ntrials=$2

sed -i "s/NJOB/$job/g" REDIGI_DIGI_L1_DIGI2RAW_HLT_PU.py
sed -i "s/NTRIALS/$ntrials/g" REDIGI_DIGI_L1_DIGI2RAW_HLT_PU.py

echo "running cmsRun REDIGI_DIGI_L1_DIGI2RAW_HLT_PU.py, job $job ntrials $ntrials" >> /dev/stderr
cmsRun REDIGI_DIGI_L1_DIGI2RAW_HLT_PU.py 

rm histProbFunction.root
rm REDIGI_DIGI_L1_DIGI2RAW_HLT_PU.py
echo "DONE" >> /dev/stderr
hostname

