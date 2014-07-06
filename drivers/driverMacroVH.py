#!/usr/bin/env python

import os

step = raw_input('enter step 0, 1, or 2: ')
if int(step) == 0:
  os.system('cmsDriver.py PYTHIA8_VH_H_Zg_8TeV_cff.py \
      --step GEN,SIM \
      --conditions START53_V7N::All \
      --pileup NoPileUp \
      --datamix NODATAMIXER \
      --eventcontent RAWSIM \
      --datatier GEN-SIM \
      --no_exec')
elif int(step) == 1:
  os.system('cmsDriver.py REDIGI_PYTHIA8_VH_H_Zg_8TeV \
      --step DIGI,L1,DIGI2RAW,HLT:7E33v2 \
      --runsScenarioForMC Run2012_AB_C_D_oneRunPerEra \
      --conditions START53_V7N::All \
      --pileup fromDB\
      --pileup_input dbs:/RelValMinBias/CMSSW_5_2_1-START52_V4-v1/GEN-SIM \
      --datamix NODATAMIXER \
      --eventcontent RAWSIM \
      --datatier GEN-SIM-RAW \
      --filein file:PYTHIA8_VH_H_Zg_8TeV_cff_py_GEN_SIM.root \
      --no_exec')
elif int(step) == 2:
  os.system('cmsDriver.py STEP2_PYTHIA8_VH_H_Zg_8TeV \
      --step RAW2DIGI,L1Reco,RECO,VALIDATION:validation_prod,DQM:DQMOfflinePOGMC \
      --conditions START53_V7N::All \
      --pileup fromDB\
      --pileup_input dbs:/RelValMinBias/CMSSW_5_2_1-START52_V4-v1/GEN-SIM \
      --datamix NODATAMIXER \
      --eventcontent AODSIM,DQM \
      --datatier AODSIM,DQM \
      --filein file:REDIGI_PYTHIA8_VH_H_Zg_8TeV_DIGI_L1_DIGI2RAW_HLT_PU.root \
      --no_exec')
else:
  print 'how did you fuck this up?'

