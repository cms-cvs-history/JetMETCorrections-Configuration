import FWCore.ParameterSet.Config as cms

#################### L2 Source definitions ##################################
L2JetCorrectorIC5Calo = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_IC5Calo'),
    label = cms.string('L2RelativeJetCorrectorIC5Calo')
)
L2JetCorrectorIC5PF= cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_IC5PF'),
    label = cms.string('L2RelativeJetCorrectorIC5PF')
)
L2JetCorrectorAK5Calo = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_AK5Calo'),
    label = cms.string('L2RelativeJetCorrectorAK5Calo')
)
L2JetCorrectorAK5PF= cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_AK5PF'),
    label = cms.string('L2RelativeJetCorrectorAK5PF')
)
L2JetCorrectorAK7Calo = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_AK7Calo'),
    label = cms.string('L2RelativeJetCorrectorAK7Calo')
)
L2JetCorrectorAK7PF= cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_AK7PF'),
    label = cms.string('L2RelativeJetCorrectorAK7PF')
)
L2JetCorrectorSC5Calo = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_SC5Calo'),
    label = cms.string('L2RelativeJetCorrectorSC5Calo')
)
L2JetCorrectorSC5PF= cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_SC5PF'),
    label = cms.string('L2RelativeJetCorrectorSC5PF')
)
L2JetCorrectorSC7Calo = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_SC7Calo'),
    label = cms.string('L2RelativeJetCorrectorSC7Calo')
)
L2JetCorrectorSC7PF= cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_SC7PF'),
    label = cms.string('L2RelativeJetCorrectorSC7PF')
)
L2JetCorrectorKT4Calo = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_KT4Calo'),
    label = cms.string('L2RelativeJetCorrectorKT4Calo')
)
L2JetCorrectorKT4PF = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_KT4PF'),
    label = cms.string('L2RelativeJetCorrectorKT4PF')
)
L2JetCorrectorKT6Calo = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_KT6Calo'),
    label = cms.string('L2RelativeJetCorrectorKT6Calo')
)
L2JetCorrectorKT6PF = cms.ESSource("L2RelativeCorrectionService", 
    tagName = cms.string('900GeV_L2Relative_KT6PF'),
    label = cms.string('L2RelativeJetCorrectorKT6PF')
)
#################### L3 Source definitions ##################################
L3JetCorrectorIC5Calo = cms.ESSource("L3AbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_IC5Calo'),
    label = cms.string('L3AbsoluteJetCorrectorIC5Calo')
)
L3JetCorrectorIC5PF = cms.ESSource("L3PFAbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_IC5PF'),
    label = cms.string('L3AbsoluteJetCorrectorIC5PF')
)
L3JetCorrectorAK5Calo = cms.ESSource("L3AbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_AK5Calo'),
    label = cms.string('L3AbsoluteJetCorrectorAK5Calo')
)
L3JetCorrectorAK5PF = cms.ESSource("L3PFAbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_AK5PF'),
    label = cms.string('L3AbsoluteJetCorrectorAK5PF')
)
L3JetCorrectorAK7Calo = cms.ESSource("L3AbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_AK7Calo'),
    label = cms.string('L3AbsoluteJetCorrectorAK7Calo')
)
L3JetCorrectorAK7PF = cms.ESSource("L3PFAbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_AK7PF'),
    label = cms.string('L3AbsoluteJetCorrectorAK7PF')
)
L3JetCorrectorSC5Calo = cms.ESSource("L3AbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_SC5Calo'),
    label = cms.string('L3AbsoluteJetCorrectorSC5Calo')
)
L3JetCorrectorSC5PF = cms.ESSource("L3PFAbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_SC5PF'),
    label = cms.string('L3AbsoluteJetCorrectorSC5PF')
)
L3JetCorrectorSC7Calo = cms.ESSource("L3AbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_SC7Calo'),
    label = cms.string('L3AbsoluteJetCorrectorSC7Calo')
)
L3JetCorrectorSC7PF = cms.ESSource("L3PFAbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_SC7PF'),
    label = cms.string('L3AbsoluteJetCorrectorSC7PF')
)
L3JetCorrectorKT4Calo = cms.ESSource("L3AbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_KT4Calo'),
    label = cms.string('L3AbsoluteJetCorrectorKT4Calo')
)
L3JetCorrectorKT4PF = cms.ESSource("L3PFAbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_KT4PF'),
    label = cms.string('L3AbsoluteJetCorrectorKT4PF')
)
L3JetCorrectorKT6Calo = cms.ESSource("L3AbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_KT6Calo'),
    label = cms.string('L3AbsoluteJetCorrectorKT6Calo')
)
L3JetCorrectorKT6PF = cms.ESSource("L3PFAbsoluteCorrectionService", 
    tagName = cms.string('900GeV_L3Absolute_KT6PF'),
    label = cms.string('L3AbsoluteJetCorrectorKT6PF')
)
#################### L2L3 Source definitions ##################################
L2L3JetCorrectorIC5Calo = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorIC5Calo','L3AbsoluteJetCorrectorIC5Calo'),
    label = cms.string('L2L3JetCorrectorIC5Calo') 
)
L2L3JetCorrectorIC5PF = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorIC5PF','L3AbsoluteJetCorrectorIC5PF'),
    label = cms.string('L2L3JetCorrectorIC5PF') 
)
L2L3JetCorrectorAK5Calo = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorAK5Calo','L3AbsoluteJetCorrectorAK5Calo'),
    label = cms.string('L2L3JetCorrectorAK5Calo') 
)
L2L3JetCorrectorAK5PF = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorAK5PF','L3AbsoluteJetCorrectorAK5PF'),
    label = cms.string('L2L3JetCorrectorAK5PF') 
)
L2L3JetCorrectorAK7Calo = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorAK7Calo','L3AbsoluteJetCorrectorAK7Calo'),
    label = cms.string('L2L3JetCorrectorAK7Calo') 
)
L2L3JetCorrectorAK7PF = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorAK7PF','L3AbsoluteJetCorrectorAK7PF'),
    label = cms.string('L2L3JetCorrectorAK7PF') 
)
L2L3JetCorrectorSC5Calo = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorSC5Calo','L3AbsoluteJetCorrectorSC5Calo'),
    label = cms.string('L2L3JetCorrectorSC5Calo') 
)
L2L3JetCorrectorSC5PF = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorSC5PF','L3AbsoluteJetCorrectorSC5PF'),
    label = cms.string('L2L3JetCorrectorSC5PF') 
)
L2L3JetCorrectorSC7Calo = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorSC7Calo','L3AbsoluteJetCorrectorSC7Calo'),
    label = cms.string('L2L3JetCorrectorSC7Calo') 
) 
L2L3JetCorrectorSC7PF = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorSC7PF','L3AbsoluteJetCorrectorSC7PF'),
    label = cms.string('L2L3JetCorrectorSC7PF') 
)
L2L3JetCorrectorKT4Calo = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorKT4Calo','L3AbsoluteJetCorrectorKT4Calo'),
    label = cms.string('L2L3JetCorrectorKT4Calo') 
)
L2L3JetCorrectorKT4PF = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorKT4PF','L3AbsoluteJetCorrectorKT4PF'),
    label = cms.string('L2L3JetCorrectorKT4PF') 
)
L2L3JetCorrectorKT6Calo = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorKT6Calo','L3AbsoluteJetCorrectorKT6Calo'),
    label = cms.string('L2L3JetCorrectorKT6Calo') 
)
L2L3JetCorrectorKT6PF = cms.ESSource("JetCorrectionServiceChain",  
    correctors = cms.vstring('L2RelativeJetCorrectorKT6PF','L3AbsoluteJetCorrectorKT6PF'),
    label = cms.string('L2L3JetCorrectorKT6PF') 
)
#################### L2L3 Module definitions ##################################
L2L3CorJetIC5Calo = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5CaloJets"),
    correctors = cms.vstring('L2L3JetCorrectorIC5Calo')
)
L2L3CorJetIC5PF = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("iterativeCone5PFJets"),
    correctors = cms.vstring('L2L3JetCorrectorIC5PF')
)
L2L3CorJetAK5Calo = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak5CaloJets"),
    correctors = cms.vstring('L2L3JetCorrectorAK5Calo')
)
L2L3CorJetAK5PF = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak5PFJets"),
    correctors = cms.vstring('L2L3JetCorrectorAK5PF')
)
L2L3CorJetAK7Calo = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("ak7CaloJets"),
    correctors = cms.vstring('L2L3JetCorrectorAK7Calo')
)
L2L3CorJetAK7PF = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("ak7PFJets"),
    correctors = cms.vstring('L2L3JetCorrectorAK7PF')
)
L2L3CorJetSC5Calo = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("sisCone5CaloJets"),
    correctors = cms.vstring('L2L3JetCorrectorSC5Calo')
)
L2L3CorJetSC5PF = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("sisCone5PFJets"),
    correctors = cms.vstring('L2L3JetCorrectorSC5PF')
)
L2L3CorJetSC7Calo = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("sisCone7CaloJets"),
    correctors = cms.vstring('L2L3JetCorrectorSC7Calo')
)
L2L3CorJetSC7PF = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("sisCone7PFJets"),
    correctors = cms.vstring('L2L3JetCorrectorSC7PF')
)
L2L3CorJetKT4Calo = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt4CaloJets"),
    correctors = cms.vstring('L2L3JetCorrectorKT4Calo')
)
L2L3CorJetKT4PF = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt4PFJets"),
    correctors = cms.vstring('L2L3JetCorrectorKT4PF')
)
L2L3CorJetKT6Calo = cms.EDProducer("CaloJetCorrectionProducer",
    src = cms.InputTag("kt6CaloJets"),
    correctors = cms.vstring('L2L3JetCorrectorKT6Calo')
)
L2L3CorJetKT6PF = cms.EDProducer("PFJetCorrectionProducer",
    src = cms.InputTag("kt6PFJets"),
    correctors = cms.vstring('L2L3JetCorrectorKT6PF')
)