import FWCore.ParameterSet.Config as cms
#!
#! PROCESS
#!
process = cms.Process("JEC")

#!
#! INPUT
#!
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )
process.source = cms.Source(
    'PoolSource',
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_3_5_5/RelValQCD_FlatPt_15_3000/GEN-SIM-RECO/MC_3XY_V25-v1/0007/E0707AC5-0F38-DF11-B1FD-0026189437E8.root')
    )

#!
#! SERVICES
#!
process.MessageLogger = cms.Service(
    "MessageLogger",
    destinations = cms.untracked.vstring('cout'),
    cout         = cms.untracked.PSet(threshold = cms.untracked.string('INFO'))
    )
process.TFileService=cms.Service("TFileService",fileName=cms.string('histos.root'))

#!
#! JET CORRECTION
#!
process.load('JetMETCorrections.Configuration.DemoJEC_cff')

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

process.ak5CaloHistos = cms.EDAnalyzer(
    'CandViewHistoAnalyzer',
    src = cms.InputTag('ak5CaloJets'),
    histograms = cms.VPSet(jetPtHistogram)
    )
process.ak5CaloL1L2L3L4L5L7Histos = cms.EDAnalyzer(
    'CandViewHistoAnalyzer',
    src = cms.InputTag('ak5CaloJetsL1L2L3L4L5L7'),
    histograms = cms.VPSet(jetPtHistogram)
    )

#
# RUN!
#
process.run = cms.Path(process.ak5CaloJetsL1L2L3L4L5L7 * process.ak5CaloHistos * process.ak5CaloL1L2L3L4L5L7Histos)


