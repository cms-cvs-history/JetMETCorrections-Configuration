import FWCore.ParameterSet.Config as cms
#!
#! PROCESS
#!
process = cms.Process("JEC")

#!
#! INPUT
#!
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source(
    'PoolSource',
    fileNames = cms.untracked.vstring(
'/store/relval/CMSSW_3_5_5/RelValQCD_FlatPt_15_3000/GEN-SIM-RECO/MC_3XY_V25-v1/0007/E0707AC5-0F38-DF11-B1FD-0026189437E8.root'
    )
)

#!
#! SERVICES
#!
process.TFileService=cms.Service("TFileService",fileName=cms.string('histos.root'))

#!
#! JET CORRECTION
#!
process.load('JetMETCorrections.Configuration.DefaultJEC_cff')

#!
#! MAKE SOME HISTOGRAMS
#!
jetPtHistogram = cms.PSet(min          = cms.untracked.double(     50),
                          max          = cms.untracked.double(    500),
                          nbins        = cms.untracked.int32 (     50),
                          name         = cms.untracked.string('JetPt'),
                          description  = cms.untracked.string(     ''),
                          plotquantity = cms.untracked.string(   'pt')
                          )

process.ak5CaloJetsL2L3Histos = cms.EDAnalyzer(
    'CandViewHistoAnalyzer',
    src = cms.InputTag('ak5CaloJetsL2L3'),
    histograms = cms.VPSet(jetPtHistogram)
    )
process.ak5PFJetsL2L3Histos = cms.EDAnalyzer(
    'CandViewHistoAnalyzer',
    src = cms.InputTag('ak5PFJetsL2L3'),
    histograms = cms.VPSet(jetPtHistogram)
    )
process.ak5JPTJetsL2L3Histos = cms.EDAnalyzer(
    'CandViewHistoAnalyzer',
    src = cms.InputTag('ak5JPTJetsL2L3'),
    histograms = cms.VPSet(jetPtHistogram)
    )

#############   Format MessageLogger #################
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10

#
# RUN!
#
process.run = cms.Path(
# create the corrected calojet collection and run the histogram module
process.ak5CaloJetsL2L3 * process.ak5CaloJetsL2L3Histos *
# create the corrected pfjet collection and run the histogram module
process.ak5PFJetsL2L3 * process.ak5PFJetsL2L3Histos *
# create the jptjet collection
process.ZSPJetCorrectionsAntiKt5 * process.ak5JPTJets *
# create the corrected jptjet collection and run the histogram module
process.ak5JPTJetsL2L3 * process.ak5JPTJetsL2L3Histos
)
















