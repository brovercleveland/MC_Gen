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

sed -i "s/NJOB/$job/g" STEP2_PYTHIA8_POWHEG_H_Zg_8TeV_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU.py
sed -i "s/NTRIALS/$ntrials/g" STEP2_PYTHIA8_POWHEG_H_Zg_8TeV_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU.py

echo "running cmsRun STEP2_PYTHIA8_POWHEG_H_Zg_8TeV_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU.py, job $job ntrials $ntrials" >> /dev/stderr
cmsRun STEP2_PYTHIA8_POWHEG_H_Zg_8TeV_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU.py 

rm STEP2_PYTHIA8_POWHEG_H_Zg_8TeV_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU.py 
echo "DONE" >> /dev/stderr
hostname

