#!/usr/bin/env python

import os

for i in range (0,200):
  os.system('ls testOut2/PYTHIA8_175_POWHEG_H_Zg_8TeV_cff_py_GEN_SIM_REDIGI_DIGI_L1_DIGI2RAW_HLT_PU_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU_{0}.root'.format(i))

