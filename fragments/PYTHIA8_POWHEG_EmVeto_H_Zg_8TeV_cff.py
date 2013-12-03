import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8175HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000),

    emissionVeto1 = cms.untracked.PSet(),
    EV1_nFinal = cms.int32(2),
    EV1_vetoOn = cms.bool(True),
    EV1_maxVetoCount = cms.int32(10000),
    EV1_pThardMode = cms.int32(1),
    EV1_pTempMode = cms.int32(0),
    EV1_emittedMode = cms.int32(0),
    EV1_pTdefMode = cms.int32(1),
    EV1_MPIvetoOn = cms.bool(False),

    PythiaParameters = cms.PSet(
      processParameters = cms.vstring(
        'Tune:pp = 5',
        'PDF:pSet = 7',
        'HiggsSM:gg2H = on',
        '25:m0 = 125.0',
        '25:onMode = off',
        '25:onIfMatch = 23 22',
        '23:mMin = 50.0',
        '23:onMode = off',
        '23:onIfAny = 11 13 15',
        'SpaceShower:pTmaxMatch = 2',
        'TimeShower:pTmaxMatch  = 2'
        ),
      parameterSets = cms.vstring('processParameters')
      )
    )

