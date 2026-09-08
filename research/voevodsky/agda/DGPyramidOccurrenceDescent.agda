{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidOccurrenceDescent where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record OccurrenceLinearReversePairingCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Ring Core SupportedDual GenericDual Ideal Quotient : Type ℓ
    x₂ x₄ : Ring
    polynomialCore : Core
    coreDifferential : Core → Core
    residualIdeal : Ideal
    idealInclusion : Ideal → Ring
    reverseConnecting : SupportedDual → GenericDual
    imageOfReverse : Ideal
    reverseImageEquation : imageOfReverse ≡ residualIdeal
    reverseCokernel : Quotient
    unitObstruction : Quotient
    zeroQuotient : Quotient
    unitObstructionNonzero : unitObstruction ≡ zeroQuotient → ⊥

    HomogeneousCoefficient Functional : Type ℓ
    homogeneousUnit : HomogeneousCoefficient
    coefficientExtraction : HomogeneousCoefficient → Functional
    CoefficientLinear : Functional → Type ℓ
    extractionNotCoefficientLinear :
      CoefficientLinear (coefficientExtraction homogeneousUnit) → ⊥

    OccurrenceGysinClass : Type ℓ
    occurrenceGysin : OccurrenceGysinClass
    zeroOccurrenceGysin : OccurrenceGysinClass
    occurrenceGysinNonzero : occurrenceGysin ≡ zeroOccurrenceGysin → ⊥
    DualOccurrenceDeterminant : Type ℓ
    residualDualDeterminant : DualOccurrenceDeterminant

    TransportedResidualIdeal : Type ℓ
    sixTransportedIdeals : TransportedResidualIdeal
    transportCompatibility : Type ℓ
    transportWitness : transportCompatibility

    IntegralDiagonal RingLinearDiagonal : Type ℓ
    integralDiagonal : IntegralDiagonal
    RingLinearPromotion : IntegralDiagonal → RingLinearDiagonal → Type ℓ
    noNaiveRingLinearPromotion : (d : RingLinearDiagonal) →
      RingLinearPromotion integralDiagonal d → ⊥
    CoefficientSystemCap : Type ℓ

record ObstructionComplementDescentCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Open CoverIndex LocalLift OverlapCycle ResidueCoordinate : Type ℓ
    obstructionComplement : Open
    SevenOpenCover : Type ℓ
    sevenOpenWitness : SevenOpenCover
    localLift : CoverIndex → LocalLift
    localLiftClosed : (i : CoverIndex) → Type ℓ
    localLiftProjectsToUnit : (i : CoverIndex) → Type ℓ
    overlapDifference : CoverIndex → CoverIndex → OverlapCycle
    cechCocycleEquation : (i j k : CoverIndex) → Type ℓ

    DescentClass : Type ℓ
    descentClass : DescentClass
    zeroDescent : DescentClass
    descentNonzero : descentClass ≡ zeroDescent → ⊥
    twelveResidues : CoverIndex → CoverIndex → ResidueCoordinate
    TwelveResidueCoordinates : Type ℓ
    twelveResidueWitness : TwelveResidueCoordinates
    descentAnnihilatorSixFactor : Type ℓ
    descentAnnihilatorWitness : descentAnnihilatorSixFactor

    GlobalCoefficient LiftableCoefficient GlobalCycle : Type ℓ
    globallyLiftable : GlobalCoefficient → LiftableCoefficient
    branchTailLift : LiftableCoefficient → GlobalCycle
    branchTailLiftClosed : (k : LiftableCoefficient) → Type ℓ
    commonUnit : GlobalCoefficient
    GlobalUnitLift : Type ℓ
    noGlobalUnitLift : GlobalUnitLift → ⊥
