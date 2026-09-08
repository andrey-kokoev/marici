{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidIntrinsicConductorResolution where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTCellPyramid
open import DGPyramidConductorChannels

record IntrinsicConductorResolutionCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    SingularRing Conductor AlternatingWord ResolutionDegree : Type ℓ
    resolutionWord : ResolutionDegree → AlternatingWord
    differential : AlternatingWord → AlternatingWord
    zeroWord : AlternatingWord
    differentialSquareZero : (w : AlternatingWord) →
      differential (differential w) ≡ zeroWord
    IntegralAugmentationContraction : Type ℓ
    integralContractionWitness : IntegralAugmentationContraction
    resolutionAllDegrees : Type ℓ

    ConductorTorRank PoincareSeries : Type ℓ
    conductorTorRank : ResolutionDegree → ConductorTorRank
    poincareSeries : PoincareSeries
    FirstConductorTorRanks : Type ℓ
    firstRankWitness : FirstConductorTorRanks
    nonzeroSyzygiesInEveryDegree : (n : ResolutionDegree) → Type ℓ

    ChannelIntrinsicTower : TRow → TColumn → Type ℓ
    channelIntrinsicTower : (r : TRow) (c : TColumn) →
      ChannelIntrinsicTower r c
    EndpointIntrinsicTower : Type ℓ
    positiveEndpointTower negativeEndpointTower : EndpointIntrinsicTower
    FourteenChannelIntrinsicFibre : Type ℓ
    fourteenChannelFibre : FourteenChannelIntrinsicFibre
    FirstFourteenChannelRanks : Type ℓ
    fourteenRankWitness : FirstFourteenChannelRanks

    MarkedInfinityGroupoid HomotopyRank : Type ℓ
    markedInfinityGroupoid : MarkedInfinityGroupoid
    homotopyRank : ResolutionDegree → HomotopyRank
    markedGroupoidUnbounded : (n : ResolutionDegree) → Type ℓ

    AmbientFibre IntrinsicFibre : Type ℓ
    ambientFibre : AmbientFibre
    intrinsicFibre : IntrinsicFibre
    AmbientIntrinsicDistinction : Type ℓ
    ambientIntrinsicWitness : AmbientIntrinsicDistinction

    GlobalEndpointAttachment : Type ℓ
    intrinsicFibreWithAttachment : GlobalEndpointAttachment → IntrinsicFibre
    intrinsicFibreWithoutAttachment : IntrinsicFibre
    intrinsicFibreForgetsGlobalAttachment : (a : GlobalEndpointAttachment) →
      intrinsicFibreWithAttachment a ≡ intrinsicFibreWithoutAttachment

    PerfectSourceCandidate : Type ℓ
    EquivalentToFourteenChannelSource : PerfectSourceCandidate → Type ℓ
    noPerfectSourceEquivalence : (p : PerfectSourceCandidate) →
      EquivalentToFourteenChannelSource p → ⊥

    FaceRankIsResidueIncidence : Type ℓ
    faceRankIncidenceWitness : FaceRankIsResidueIncidence
    FaceRankIsCompleteHomotopyDegree : Type ℓ
    noFaceRankAsCompleteHomotopyDegree :
      FaceRankIsCompleteHomotopyDegree → ⊥

    PhysicalIntrinsicConductorTowerCompatibility : Type ℓ
