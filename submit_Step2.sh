#!/bin/sh
#===================================================================================================
# Submit a set of jobs to run over a given dataset, splitting the jobs according to the filesets.
#
# Version 1.0                                                                      November 14, 2008
#===================================================================================================

# Read the arguments
jobId=`date +%j%m%d%k%M%S`
ntrials=500
njobs=200
#ntrials=1
#njobs=2

# Prepare environment
echo " "
workDir=/uscms_data/d2/bpollack/genProd/CMSSW_5_3_11_patch6/src/test/
cd $workDir
script=/uscms_data/d2/bpollack/genProd/CMSSW_5_3_11_patch6/src/test/run_Step2.sh

genDir=/uscms_data/d2/bpollack/genProd/CMSSW_5_3_11_patch6/src/GeneratorInterface




# Looping through each single file and submitting the condor jobs
echo " "
echo "Submitting jobs to condor"
echo " "

i=0;
cd $workDir/testOut2
while(( $i < $njobs )); do 
  inputFile=/uscms_data/d2/bpollack/genProd/CMSSW_5_3_11_patch6/src/test/testOut1/PYTHIA8_175_H_Zg_8TeV_cff_py_GEN_SIM_REDIGI_DIGI_L1_DIGI2RAW_HLT_PU_${i}.root

cat > submit.cmd <<EOF
            Universe                = vanilla
            Notify_user             = brian.pollack@cern.ch
            Notification            = Error
            Executable              = $script
            Arguments               = $i $ntrials 
            Rank                    = Mips
            Requirements            = (OpSys == "LINUX") && (Disk >= DiskUsage) && ((Memory * 1024) >= ImageSize) && (HasFileTransfer) 
            +LENGTH                 = "LONG"  
            GetEnv                  = True
            Input                   = /dev/null
            Output                  = ../res2/job_${i}.out
            Error                   = ../res2/job_${i}.err
            should_transfer_files   = YES
            when_to_transfer_output = ON_EXIT
            transfer_input_files    = $workDir/STEP2_RAW2DIGI_L1Reco_RECO_VALIDATION_DQM_PU.py, $genDir, $inputFile 
            Queue
EOF

  condor_submit submit.cmd # >& /dev/null;
  echo ""
  rm submit.cmd

  (( i++ ));

done

exit 0

