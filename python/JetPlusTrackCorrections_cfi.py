import FWCore.ParameterSet.Config as cms

# "Generic" configurables used by ESSources/EDProducers in both the JetMET and PAT code 

from TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAlong_cfi import * 

JPTZSPCorrectorICone5 = cms.PSet(
    # Look-up tables
    NonEfficiencyFile     = cms.string('CMSSW_167_TrackNonEff'),
    NonEfficiencyFileResp = cms.string('CMSSW_167_TrackLeakage'),
    ResponseFile          = cms.string('CMSSW_167_response'),
    # Access to tracks and muons
    muonSrc      = cms.InputTag("muons"),
    trackSrc     = cms.InputTag("generalTracks"),
    UseQuality   = cms.bool(True),
    TrackQuality = cms.string('highPurity'),
    # Jet-tracks association (null values mean use "on-the-fly" mode)
    JetTrackCollectionAtVertex = cms.InputTag("ZSPiterativeCone5JetTracksAssociatorAtVertex"), 
    JetTrackCollectionAtCalo   = cms.InputTag("ZSPiterativeCone5JetTracksAssociatorAtCaloFace"),
    Propagator = cms.string('SteppingHelixPropagatorAlong'),
    coneSize   = cms.double(0.5),
    # Misc configurables
    respalgo           = cms.int32(5),
    AddOutOfConeTracks = cms.bool(True),
    # Electrons
    recoGsfelectrons = cms.InputTag("gsfElectrons"),
    eIDValueMap      = cms.InputTag("JPTeidTight"),  
    # Split/merge schema: 0-IC, 1-SisCone, 2-anti-Kt
    SplitMergeP = cms.int32(0)
    )
