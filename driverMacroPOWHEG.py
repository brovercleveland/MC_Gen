#!/usr/bin/env python

import os


#os.system('cmsDriver.py POWHEG_PYTHIA8_H_Zg_8TeV_cff.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO --beamspot Realistic8TeVCollision --conditions auto:startup --pileup 2012_Startup_50ns_PoissonOOTPU --datatier GEN-SIM-RECO --eventcontent RECOSIM -n 10 --no_exec')
#os.system('cmsDriver.py POWHEG_PYTHIA8_H_Zg_8TeV_cff.py -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT,RAW2DIGI,RECO --beamspot Realistic8TeVCollision --conditions START53_V15::All --pileup 2012_Startup_50ns_PoissonOOTPU --pileup_input dbs:/RelValMinBias/CMSSW_5_2_1-START52_V4-v1/GEN-SIM --datatier GEN-SIM-RECO --eventcontent RECOSIM -n 50 --no_exec')

#os.system('cmsDriver.py MCDBtoEDM \
    #    --conditions START53_V7A::All \
    #-s NONE \
    #--eventcontent RAWSIM \
    #--datatier GEN \
    #--filein mcdb:5727')

#fuck, should be using 2012_Summer_50ns_PoissonOOTPU, 7E33v2
#--filein=file:/eos/uscms/store/user/bpollack/lhe/h_ggH_WW_ZGamma_125_15.lhe \
#START53_V19D::All works with 538
#--pileup_input dbs:/RelValMinBias/CMSSW_5_2_1-START52_V4-v1/GEN-SIM \
# --beamspot Realistic8TeVCollision
#--runsScenarioForMC Run2012_AB_C_D_oneRunPerEra

  #os.system('cmsDriver.py PYTHIA8_ee_H_Zg_160GeV_cff.py \
      #    --step GEN,SIM \
      #--conditions START53_V27::All \
      #--pileup NoPileUp \
      #--datamix NODATAMIXER \
      #--eventcontent RAWSIM \
      #--datatier GEN-SIM \
      #--no_exec')

step = raw_input('enter step 0, 1, or 2: ')
if int(step) == 0:
  os.system('cmsDriver.py PYTHIA8_POWHEG_H_Zg_8TeV_cff.py \
      --step GEN,SIM \
      --conditions START53_V27::All \
      --pileup NoPileUp \
      --datamix NODATAMIXER \
      --eventcontent RAWSIM \
      --datatier GEN-SIM \
      --filein=file:/eos/uscms/store/user/bpollack/lhe/h_ggH_WW_ZGamma_125_15.lhe \
      --no_exec')
elif int(step) == 1:
  os.system('cmsDriver.py REDIGI_PYTHIA8_POWHEG_H_Zg_8TeV \
      --step DIGI,L1,DIGI2RAW,HLT:7E33v2 \
      --conditions START53_V27::All \
      --pileup 2012_Summer_50ns_PoissonOOTPU \
      --pileup_input dbs:/RelValMinBias/CMSSW_5_2_1-START52_V4-v1/GEN-SIM \
      --datamix NODATAMIXER \
      --eventcontent RAWSIM \
      --datatier GEN-SIM-RAW \
      --filein file:PYTHIA8_POWHEG_H_Zg_8TeV_cff_py_GEN_SIM.root \
      --no_exec')
elif int(step) == 2:
  os.system('cmsDriver.py STEP2_PYTHIA8_POWHEG_H_Zg_8TeV \
      --step RAW2DIGI,L1Reco,RECO,VALIDATION:validation_prod,DQM:DQMOfflinePOGMC \
      --conditions START53_V27::All \
      --pileup 2012_Summer_50ns_PoissonOOTPU \
      --pileup_input dbs:/RelValMinBias/CMSSW_5_2_1-START52_V4-v1/GEN-SIM \
      --datamix NODATAMIXER \
      --eventcontent AODSIM,DQM \
      --datatier AODSIM,DQM \
      --filein file:REDIGI_PYTHIA8_POWHEG_H_Zg_8TeV_DIGI_L1_DIGI2RAW_HLT_PU.root \
      --no_exec')
else:
  print 'how did you fuck this up?'

