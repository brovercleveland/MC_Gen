Changing Local Pythia8 Version
------------------------------
(This does not work with crab, local only)

        scram b clean                                                                       
        sed -i "s/153/175/g" ../config/toolbox/slc5_amd64_gcc462/tools/selected/pythia8.xml 
        sed -i "s/462/472/g" ../config/toolbox/slc5_amd64_gcc462/tools/selected/pythia8.xml 
        scram setup pythia8
        cmsenv
        echo $PYTHIA8DATA                                                          
        cvs co -r CMSSW_5_3_8 GeneratorInterface/Pythia8Interface                           
        scram b
