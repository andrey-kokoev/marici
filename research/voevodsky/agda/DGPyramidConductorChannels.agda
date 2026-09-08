{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidConductorChannels where

open import Cubical.Foundations.Prelude
open import DGPyramidTCellPyramid
open import DGPyramidSupportedTraceDuality

data ChannelSign : Type where
  positive negative : ChannelSign

data FaceRank : Type where
  rank1 rank2 : FaceRank

record SignedHomRank : Type where
  constructor signed-rank
  field
    sign : ChannelSign
    faceRank : FaceRank

rowSignedRank : TRow → SignedHomRank
rowSignedRank +singleton = signed-rank positive rank1
rowSignedRank +pair      = signed-rank positive rank2
rowSignedRank -singleton = signed-rank negative rank1
rowSignedRank -pair      = signed-rank negative rank2

signedRankRow : SignedHomRank → TRow
signedRankRow (signed-rank positive rank1) = +singleton
signedRankRow (signed-rank positive rank2) = +pair
signedRankRow (signed-rank negative rank1) = -singleton
signedRankRow (signed-rank negative rank2) = -pair

signedRankRowSection : (r : TRow) → signedRankRow (rowSignedRank r) ≡ r
signedRankRowSection +singleton = refl
signedRankRowSection +pair = refl
signedRankRowSection -singleton = refl
signedRankRowSection -pair = refl

rowSignedRankSection : (r : SignedHomRank) → rowSignedRank (signedRankRow r) ≡ r
rowSignedRankSection (signed-rank positive rank1) = refl
rowSignedRankSection (signed-rank positive rank2) = refl
rowSignedRankSection (signed-rank negative rank1) = refl
rowSignedRankSection (signed-rank negative rank2) = refl

record FourConductorChannelCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    GlobalConductor Channel : Type ℓ
    channel : TRow → Channel

    RowBoundary : TRow → Type ℓ
    rowBoundary : (r : TRow) → RowBoundary r
    restrictRowToChannel : (r : TRow) → RowBoundary r → Channel
    channelToGlobalConductor : (r : TRow) → Channel → GlobalConductor

    GlobalAttachment : Type ℓ
    globalAttachment : GlobalAttachment
    assembleChannels : ((r : TRow) → Channel) → GlobalAttachment
    fourChannelReconstruction :
      assembleChannels channel ≡ globalAttachment

    -- The channels refine one seam; they are not asserted to be four loci.
    CommonConductorLocus : Type ℓ
    commonConductorLocus : CommonConductorLocus
    channelHasCommonLocus : (r : TRow) → Type ℓ

    PositiveSheetChannel NegativeSheetChannel : Channel → Type ℓ
    positiveSingletonChannel : PositiveSheetChannel (channel +singleton)
    positivePairChannel : PositiveSheetChannel (channel +pair)
    negativeSingletonChannel : NegativeSheetChannel (channel -singleton)
    negativePairChannel : NegativeSheetChannel (channel -pair)

    SingletonFrame PairFrame : Channel → Type ℓ
    positiveSingletonFrame : SingletonFrame (channel +singleton)
    negativeSingletonFrame : SingletonFrame (channel -singleton)
    positivePairFrame : PairFrame (channel +pair)
    negativePairFrame : PairFrame (channel -pair)

    EndpointCompleteCompatibility :
      EndpointCompleteTCellPyramidCertificate {ℓ} → Type ℓ
    DescentDualityCompatibility : DescentDualityCertificate {ℓ} → Type ℓ

    -- A source realization must provide these maps rather than infer them
    -- from the cardinality four alone.
    PhysicalRowwiseConductorRestriction : Type ℓ

    HomotopyDegree : Type ℓ
    faceRankToHomotopyDegree : FaceRank → HomotopyDegree
    PhysicalFaceRankDegreeIdentification : Type ℓ
