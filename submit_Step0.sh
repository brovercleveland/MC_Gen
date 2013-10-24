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
#ntrials=2
#njobs=2

# Prepare environment
echo " "
workDir=/uscms_data/d2/bpollack/genProd/CMSSW_5_3_11_patch6/src/test/
cd $workDir
script=/uscms_data/d2/bpollack/genProd/CMSSW_5_3_11_patch6/src/test/run_Step0.sh

genDir=/uscms_data/d2/bpollack/genProd/CMSSW_5_3_11_patch6/src/GeneratorInterface


# Looping through each single file and submitting the condor jobs
echo " "
echo "Submitting jobs to condor"
echo " "

i=0;
cd $workDir/testOut0_pdf7
while(( $i < $njobs )); do 

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
            Output                  = ../res0_pdf7/job_${i}.out
            Error                   = ../res0_pdf7/job_${i}.err
            Log                     = ../res0_pdf7/job_${i}.log 
            should_transfer_files   = YES
            when_to_transfer_output = ON_EXIT
            transfer_input_files    = $workDir/PYTHIA8_POWHEG_H_Zg_8TeV_cff_py_GEN_SIM.py, $genDir 
            Queue
EOF

  condor_submit submit.cmd # >& /dev/null;
  echo ""
  rm submit.cmd

  (( i++ ));

done

exit 0

