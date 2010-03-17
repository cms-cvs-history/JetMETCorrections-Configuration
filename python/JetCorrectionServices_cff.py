################################################################################
#
# JetCorrectionServices_cff
# -------------------------
#
# Define most relevant jet correction services
# for AntiKt R=0.5 CaloJets and PFJets
#
################################################################################
import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Configuration.JetCorrectionEra_cff import *


#
# SINGLE LEVEL CORRECTION SERVICES
#

# L1 (Offset) Correction Service
L1Offset = cms.ESSource(
    'LXXXCorrectionService',
    era = cms.string(''),
    level = cms.string('L1Offset'),
    algorithm = cms.string('1PU_IC5Calo')
    )

# L1 (Fastjet PU&UE Subtraction) Correction Service
L1Fastjet = cms.ESSource(
    'L1FastjetCorrectionService',
    srcMedianPt = cms.InputTag('kt6PFJets')
    )

# L2 (relative eta-conformity) Correction Services
ak5CaloL2Relative = cms.ESSource(
    'LXXXCorrectionService',
    JetCorrectionEra,
    level     = cms.string('L2Relative'),
    algorithm = cms.string('AK5Calo')
    )
ak5PFL2Relative = ak5CaloL2Relative.clone( algorithm = 'AK5PF' )

# L3 (absolute) Correction Services
ak5CaloL3Absolute = cms.ESSource(
    'LXXXCorrectionService',
    JetCorrectionEra,
    level     = cms.string('L3Absolute'),
    algorithm = cms.string('AK5Calo')
    )
ak5PFL3Absolute   = ak5CaloL3Absolute.clone( algorithm = 'AK5PF' )


# L6 (semileptonically decaying b-jet) Correction Services
ak5CaloL6SLB = cms.ESSource(
    'L6SLBCorrectionService',
    era                 = cms.string(''),
    algorithm           = cms.string(''),
    addMuonToJet        = cms.bool(True),
    srcBTagInfoElectron = cms.InputTag('ak5CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ak5CaloJetsSoftMuonTagInfos')
    )
ak5PFL6SLB = cms.ESSource(
    'L6SLBCorrectionService',
    era                 = cms.string(''),
    algorithm           = cms.string(''),
    addMuonToJet        = cms.bool(False),
    srcBTagInfoElectron = cms.InputTag('ak5PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ak5PFJetsSoftMuonTagInfos')
    )


#
# MULTIPLE LEVEL CORRECTION SERVICES
#

# L2L3 CORRECTION SERVICES
ak5CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak5CaloL2Relative','ak5CaloL3Absolute')
    )
ak5PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak5PFL2Relative','ak5PFL3Absolute')
    )

# L1L2L3 CORRECTION SERVICES
ak5CaloL1L2L3 = ak5CaloL2L3.clone()
ak5CaloL1L2L3.correctors.insert(0,'L1Fastjet')
ak5PFL1L2L3 = ak5PFL2L3.clone()
ak5PFL1L2L3.correctors.insert(0,'L1Fastjet')


# L2L3L6 CORRECTION SERVICES
ak5CaloL2L3L6 = ak5CaloL2L3.clone()
ak5CaloL2L3L6.correctors.append('ak5CaloL6SLB')
ak5PFL2L3L6 = ak5PFL2L3.clone()
ak5PFL2L3L6.correctors.append('ak5PFL6SLB')


# L1L2L3L6 CORRECTION SERVICES
ak5CaloL1L2L3L6 = ak5CaloL1L2L3.clone()
ak5CaloL1L2L3L6.correctors.append('ak5CaloL6SLB')
ak5PFL1L2L3L6 = ak5PFL1L2L3.clone()
ak5PFL1L2L3L6.correctors.append('ak5PFL6SLB')