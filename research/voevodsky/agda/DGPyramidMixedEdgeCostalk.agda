{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidMixedEdgeCostalk where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record MixedShortEdgeAttachmentCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    MixedEdgeClass NativeGenericClass LongStarDifference : Type ℓ
    edge03 edge25 edge41 : MixedEdgeClass
    nativeGenericClass : NativeGenericClass
    connectEdge : MixedEdgeClass → NativeGenericClass
    threeEdgesHaveCommonConnectingImage : Type ℓ
    ConnectingRow111 : Type ℓ
    connectingRowWitness : ConnectingRow111

    DifferenceKernel : Type ℓ
    differenceKernel : DifferenceKernel
    RankTwoDifferenceKernel : Type ℓ
    rankTwoWitness : RankTwoDifferenceKernel
    longStar03 longStar25 longStar14 : LongStarDifference
    longStarsRepresentBridgeDifferences : Type ℓ
    longStarIncidenceOneMinusRotationSquared : Type ℓ
    longStarDifferencesSumToZero : Type ℓ

    IndividualEdgeEndpointLift : MixedEdgeClass → Type ℓ
    noIndividualEdgeEndpointLift : (e : MixedEdgeClass) →
      IndividualEdgeEndpointLift e → ⊥
    PrimitiveEighteenTermTransgression : Type ℓ
    primitiveTransgressionWitness : PrimitiveEighteenTermTransgression

    CoupledNativeCap ThreeShortSourcePresentations : Type ℓ
    coupledNativeCap : CoupledNativeCap
    threePresentations : ThreeShortSourcePresentations
    endpointMapsAgree : Type ℓ
    comparisonHomotopiesHaveZeroEndpointPart : Type ℓ

    CellwiseTCellLongStarBijection : Type ℓ
    noCellwiseTCellLongStarBijection : CellwiseTCellLongStarBijection → ⊥
    PhysicalMixedEdgeAttachmentTransport : Type ℓ

record MilnorConductorCostalkCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    ConductorCostalk Counit CostalkKernel SupportedPrimary : Type ℓ
    conductorCostalk : ConductorCostalk
    counit : ConductorCostalk → Counit
    Rank34Costalk Rank3CounitImage Rank31CounitKernel : Type ℓ
    rank34Witness : Rank34Costalk
    rank3Witness : Rank3CounitImage
    rank31Witness : Rank31CounitKernel
    costalkKernel : CostalkKernel
    counitSequenceExactSaturated : Type ℓ
    normalizationObstructionsExhaustCounitKernel : Type ℓ

    InvariantCostalk InvariantPrimary InvariantResidual : Type ℓ
    Rank11InvariantCostalk Rank1InvariantPrimary Rank10InvariantResidual : Type ℓ
    rank11Witness : Rank11InvariantCostalk
    rank1Witness : Rank1InvariantPrimary
    rank10Witness : Rank10InvariantResidual
    invariantSequenceExactSaturated : Type ℓ

    MilnorTotalization : Type ℓ
    milnorTotalization : MilnorTotalization
    totalizationEquivalentToStructureModule : Type ℓ
    SameDegreeExtensionMechanism : Type ℓ
    noSameDegreeExtensionFromTotalization : SameDegreeExtensionMechanism → ⊥
    earlierTransgressionOutsideCounitImage : Type ℓ
    PhysicalCostalkPrimarySelection : Type ℓ
