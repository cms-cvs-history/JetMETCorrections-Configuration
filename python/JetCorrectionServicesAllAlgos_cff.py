import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Configuration.JetCorrectionServices_cff import *


#
# SINGLE LEVEL CORRECTION SERVICES
#

# L2 (relative eta-conformity) Correction Services
ak7CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'AK7Calo' )
kt4CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'KT4Calo' )
kt6CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'KT6Calo' )
sc5CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'SC5Calo' )
sc7CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'SC7Calo' )
ic5CaloL2Relative = ak5CaloL2Relative.clone( algorithm = 'IC5Calo' )

ak7PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'AK7PF' )
kt4PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'KT4PF' )
kt6PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'KT6PF' )
sc5PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'SC5PF' )
sc7PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'SC7PF' )
ic5PFL2Relative   = ak5PFL2Relative.clone  ( algorithm = 'IC5PF' )

# L3 (absolute) Correction Services
ak7CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'AK7Calo' )
kt4CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'KT4Calo' )
kt6CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'KT6Calo' )
sc5CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'SC5Calo' )
sc7CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'SC7Calo' )
ic5CaloL3Absolute = ak5CaloL3Absolute.clone( algorithm = 'IC5Calo' )

ak7PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'AK7PF' )
kt4PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'KT4PF' )
kt6PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'KT6PF' )
sc5PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'SC5PF' )
sc7PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'SC7PF' )
ic5PFL3Absolute   = ak5PFL3Absolute.clone  ( algorithm = 'IC5PF' )


# L6 (semileptonically decaying b-jet) Correction Services
ak7CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('ak7CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ak7CaloJetsSoftMuonTagInfos')
    )
kt4CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('kt4CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('kt4CaloJetsSoftMuonTagInfos')
    )
kt6CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('kt6CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('kt6CaloJetsSoftMuonTagInfos')
    )
sc5CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('sc5CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('sc5CaloJetsSoftMuonTagInfos')
    )
sc7CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('sc7CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('sc7CaloJetsSoftMuonTagInfos')
    )
ic5CaloL6SLB = ak5CaloL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('ic5CaloJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ic5CaloJetsSoftMuonTagInfos')
    )

ak7PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('ak7PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ak7PFJetsSoftMuonTagInfos')
    )
kt4PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('kt4PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('kt4PFJetsSoftMuonTagInfos')
    )
kt6PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('kt6PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('kt6PFJetsSoftMuonTagInfos')
    )
sc5PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('sc5PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('sc5PFJetsSoftMuonTagInfos')
    )
sc7PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('sc7PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('sc7PFJetsSoftMuonTagInfos')
    )
ic5PFL6SLB = ak5PFL6SLB.clone(
    srcBTagInfoElectron = cms.InputTag('ic5PFJetsSoftElectronTagInfos'),
    srcBTagInfoMuon     = cms.InputTag('ic5PFJetsSoftMuonTagInfos')
    )


#
# MULTIPLE LEVEL CORRECTION SERVICES
#

# L2L3 CORRECTION SERVICES
ak7CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7CaloL2Relative','ak7CaloL3Absolute')
    )
kt4CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4CaloL2Relative','kt4CaloL3Absolute')
    )
kt6CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6CaloL2Relative','kt6CaloL3Absolute')
    )
sc5CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('sc5CaloL2Relative','sc5CaloL3Absolute')
    )
sc7CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('sc7CaloL2Relative','sc7CaloL3Absolute')
    )
ic5CaloL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5CaloL2Relative','ic5CaloL3Absolute')
    )

ak7PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ak7PFL2Relative','ak7PFL3Absolute')
    )
kt4PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt4PFL2Relative','kt4PFL3Absolute')
    )
kt6PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('kt6PFL2Relative','kt6PFL3Absolute')
    )
sc5PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('sc5PFL2Relative','sc5PFL3Absolute')
    )
sc7PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('sc7PFL2Relative','sc7PFL3Absolute')
    )
ic5PFL2L3 = cms.ESSource(
    'JetCorrectionServiceChain',
    correctors = cms.vstring('ic5PFL2Relative','ic5PFL3Absolute')
    )

# L1L2L3 CORRECTION SERVICES
ak7CaloL1L2L3 = ak7CaloL2L3.clone()
ak7CaloL1L2L3.correctors.insert(0,'L1Fastjet')
kt4CaloL1L2L3 = kt4CaloL2L3.clone()
kt4CaloL1L2L3.correctors.insert(0,'L1Fastjet')
kt6CaloL1L2L3 = kt6CaloL2L3.clone()
kt6CaloL1L2L3.correctors.insert(0,'L1Fastjet')
sc5CaloL1L2L3 = sc5CaloL2L3.clone()
sc5CaloL1L2L3.correctors.insert(0,'L1Fastjet')
sc7CaloL1L2L3 = sc7CaloL2L3.clone()
sc7CaloL1L2L3.correctors.insert(0,'L1Fastjet')
ic5CaloL1L2L3 = ic5CaloL2L3.clone()
ic5CaloL1L2L3.correctors.insert(0,'L1Fastjet')

ak7PFL1L2L3 = ak7PFL2L3.clone()
ak7PFL1L2L3.correctors.insert(0,'L1Fastjet')
kt4PFL1L2L3 = kt4PFL2L3.clone()
kt4PFL1L2L3.correctors.insert(0,'L1Fastjet')
kt6PFL1L2L3 = kt6PFL2L3.clone()
kt6PFL1L2L3.correctors.insert(0,'L1Fastjet')
sc5PFL1L2L3 = sc5PFL2L3.clone()
sc5PFL1L2L3.correctors.insert(0,'L1Fastjet')
sc7PFL1L2L3 = sc7PFL2L3.clone()
sc7PFL1L2L3.correctors.insert(0,'L1Fastjet')
ic5PFL1L2L3 = ic5PFL2L3.clone()
ic5PFL1L2L3.correctors.insert(0,'L1Fastjet')


# L2L3L6 CORRECTION SERVICES
ak7CaloL2L3L6 = ak7CaloL2L3.clone()
ak7CaloL2L3L6.correctors.append('ak7CaloL6SLB')
ak4CaloL2L3L6 = kt4CaloL2L3.clone()
ak4CaloL2L3L6.correctors.append('kt4CaloL6SLB')
ak6CaloL2L3L6 = kt6CaloL2L3.clone()
ak6CaloL2L3L6.correctors.append('kt6CaloL6SLB')
sc5CaloL2L3L6 = sc5CaloL2L3.clone()
sc5CaloL2L3L6.correctors.append('sc5CaloL6SLB')
sc7CaloL2L3L6 = sc7CaloL2L3.clone()
sc7CaloL2L3L6.correctors.append('sc7CaloL6SLB')
ic5CaloL2L3L6 = ic5CaloL2L3.clone()
ic5CaloL2L3L6.correctors.append('ic5CaloL6SLB')

ak7PFL2L3L6 = ak7PFL2L3.clone()
ak7PFL2L3L6.correctors.append('ak7PFL6SLB')
ak4PFL2L3L6 = kt4PFL2L3.clone()
ak4PFL2L3L6.correctors.append('kt4PFL6SLB')
ak6PFL2L3L6 = kt6PFL2L3.clone()
ak6PFL2L3L6.correctors.append('kt6PFL6SLB')
sc5PFL2L3L6 = sc5PFL2L3.clone()
sc5PFL2L3L6.correctors.append('sc5PFL6SLB')
sc7PFL2L3L6 = sc7PFL2L3.clone()
sc7PFL2L3L6.correctors.append('sc7PFL6SLB')
ic5PFL2L3L6 = ic5PFL2L3.clone()
ic5PFL2L3L6.correctors.append('ic5PFL6SLB')


# L1L2L3L6 CORRECTION SERVICES
ak7CaloL1L2L3L6 = ak7CaloL1L2L3.clone()
ak7CaloL1L2L3L6.correctors.append('ak7CaloL6SLB')
ak4CaloL1L2L3L6 = kt4CaloL1L2L3.clone()
ak4CaloL1L2L3L6.correctors.append('kt4CaloL6SLB')
ak6CaloL1L2L3L6 = kt6CaloL1L2L3.clone()
ak6CaloL1L2L3L6.correctors.append('kt6CaloL6SLB')
sc5CaloL1L2L3L6 = sc5CaloL1L2L3.clone()
sc5CaloL1L2L3L6.correctors.append('sc5CaloL6SLB')
sc7CaloL1L2L3L6 = sc7CaloL1L2L3.clone()
sc7CaloL1L2L3L6.correctors.append('sc7CaloL6SLB')
ic5CaloL1L2L3L6 = ic5CaloL1L2L3.clone()
ic5CaloL1L2L3L6.correctors.append('ic5CaloL6SLB')

ak7PFL1L2L3L6 = ak7PFL1L2L3.clone()
ak7PFL1L2L3L6.correctors.append('ak7PFL6SLB')
ak4PFL1L2L3L6 = kt4PFL1L2L3.clone()
ak4PFL1L2L3L6.correctors.append('kt4PFL6SLB')
ak6PFL1L2L3L6 = kt6PFL1L2L3.clone()
ak6PFL1L2L3L6.correctors.append('kt6PFL6SLB')
sc5PFL1L2L3L6 = sc5PFL1L2L3.clone()
sc5PFL1L2L3L6.correctors.append('sc5PFL6SLB')
sc7PFL1L2L3L6 = sc7PFL1L2L3.clone()
sc7PFL1L2L3L6.correctors.append('sc7PFL6SLB')
ic5PFL1L2L3L6 = ic5PFL1L2L3.clone()
ic5PFL1L2L3L6.correctors.append('ic5PFL6SLB')