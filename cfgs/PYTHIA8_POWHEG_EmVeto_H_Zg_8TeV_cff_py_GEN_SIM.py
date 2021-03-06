# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: PYTHIA8_POWHEG_EmVeto_H_Zg_8TeV_cff.py --step GEN,SIM --conditions START53_V27::All --pileup NoPileUp --datamix NODATAMIXER --eventcontent RAWSIM --datatier GEN-SIM --filein=file:/eos/uscms/store/user/bpollack/lhe/h_ggH_WW_ZGamma_125_15.lhe --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring('file:/eos/uscms/store/user/bpollack/lhe/h_ggH_WW_ZGamma_125_15.lhe')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('PYTHIA8_POWHEG_EmVeto_H_Zg_8TeV_cff.py nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('PYTHIA8_POWHEG_EmVeto_H_Zg_8TeV_cff_py_GEN_SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V27::All', '')

process.generator = cms.EDFilter("Pythia8175HadronizerFilter",
    emissionVeto1 = cms.untracked.PSet(

    ),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    EV1_nFinal = cms.int32(2),
    EV1_MPIvetoOn = cms.bool(False),
    EV1_pTempMode = cms.int32(0),
    EV1_pThardMode = cms.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    EV1_vetoOn = cms.bool(True),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    EV1_pTdefMode = cms.int32(1),
    comEnergy = cms.double(8000),
    EV1_emittedMode = cms.int32(0),
    maxEventsToPrint = cms.untracked.int32(1),
    EV1_maxVetoCount = cms.int32(10000),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring('Tune:pp = 5', 
            'PDF:pSet = 7', 
            'HiggsSM:gg2H = on', 
            '25:m0 = 125.0', 
            '25:onMode = off', 
            '25:onIfMatch = 23 22', 
            '23:mMin = 50.0', 
            '23:onMode = off', 
            '23:onIfAny = 11 13 15', 
            'SpaceShower:pTmaxMatch = 2', 
            'TimeShower:pTmaxMatch  = 2'),
        parameterSets = cms.vstring('processParameters')
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

