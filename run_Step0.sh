#!/bin/sh


cd ${_CONDOR_SCRATCH_DIR}
 

job=$1
ntrials=$2

sed -i "s/NJOB/$job/g" PYTHIA8_POWHEG_H_Zg_8TeV_cff_py_GEN_SIM.py
sed -i "s/NTRIALS/$ntrials/g" PYTHIA8_POWHEG_H_Zg_8TeV_cff_py_GEN_SIM.py

echo "running cmsRun PYTHIA8_POWHEG_H_Zg_8TeV_cff_py_GEN_SIM.py, job $job ntrials $ntrials" >> /dev/stderr
cmsRun PYTHIA8_POWHEG_H_Zg_8TeV_cff_py_GEN_SIM.py 

rm PYTHIA8_POWHEG_H_Zg_8TeV_cff_py_GEN_SIM.py
echo "DONE" >> /dev/stderr
hostname

