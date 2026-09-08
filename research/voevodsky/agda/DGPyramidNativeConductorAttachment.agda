{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidNativeConductorAttachment where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record NativeConductorDualAttachmentCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    NativeDual PlusBranchDual MinusBranchDual ConductorDual : Type ℓ
    nativeDual : NativeDual
    plusBranchDual : PlusBranchDual
    minusBranchDual : MinusBranchDual
    conductorDual : ConductorDual

    PlusTripleGysin MinusTripleGysin ResidualPairGysin MissingX0Gysin : Type ℓ
    plusTripleGysin : PlusTripleGysin
    minusTripleGysin : MinusTripleGysin
    residualPairGysin : ResidualPairGysin
    missingX0Gysin : MissingX0Gysin
    minusFactorization : Type ℓ
    plusCoordinatesX1X3X5 : Type ℓ
    minusCoordinatesX0X2X4 : Type ℓ

    DegreeThreeBranches DegreeFiveConductor SixDeterminant : Type ℓ
    degreeThreeWitness : DegreeThreeBranches
    degreeFiveWitness : DegreeFiveConductor
    sixDeterminantWitness : SixDeterminant
    NativeAttachment : Type ℓ
    nativeAttachment : NativeAttachment
    nativeAttachmentNonzero : Type ℓ
    nativeAttachmentNonSplit : Type ℓ

    PrimitiveConductorSection : Type ℓ
    noPrimitiveConductorSection : PrimitiveConductorSection → ⊥
    FivefoldComparison : Type ℓ
    noFivefoldComparison : FivefoldComparison → ⊥
    TwentyEightUnitPivots FortyNineUnitPivots : Type ℓ
    twentyEightPivotWitness : TwentyEightUnitPivots
    fortyNinePivotWitness : FortyNineUnitPivots

    PlusCollar MinusCollar : Type ℓ
    plusCollar : PlusCollar
    minusCollar : MinusCollar
    weightedCollarCoefficientCompatibility : Type ℓ
    rawCollarConductorVanishing : Type ℓ
    collarDoesNotYetIdentifyGysin : Type ℓ

    SourceSupportedCocycle ReflectionHomotopy PrimitiveSixfoldResidue : Type ℓ
    sourceSupportedCocycle : SourceSupportedCocycle
    reflectionHomotopy : ReflectionHomotopy
    primitiveSixfoldResidue : PrimitiveSixfoldResidue
    nativePairingEquation : Type ℓ

record NormalizationIdealDescentCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    ConductorIdeal IdealResolution FramedTarget : Type ℓ
    conductorIdeal : ConductorIdeal
    idealResolution : IdealResolution
    framedTarget : FramedTarget

    IndependentTargetCycles AdmissibleGeneratorAssignments ResolvedMaps : Type ℓ
    StrictMaps RelationOnlyMaps : Type ℓ
    Rank60Independent Rank34Admissible Rank40Resolved : Type ℓ
    Rank16Strict Rank6RelationOnly Rank26DescentConditions : Type ℓ
    rank60Witness : Rank60Independent
    rank34Witness : Rank34Admissible
    rank40Witness : Rank40Resolved
    rank16Witness : Rank16Strict
    rank6Witness : Rank6RelationOnly
    rank26Witness : Rank26DescentConditions

    evaluateGenerators : ResolvedMaps → AdmissibleGeneratorAssignments
    relationOnlyKernel : RelationOnlyMaps
    generatorEvaluationExactSaturated : Type ℓ
    relationHomotopiesRequired : Type ℓ
    noMapHomotopyQuotientInFrame : Type ℓ

    EquivariantResolved ScalarConductorValue : Type ℓ
    Rank13Equivariant Rank11ScalarVisible Rank2ScalarInvisible : Type ℓ
    rank13Witness : Rank13Equivariant
    rank11Witness : Rank11ScalarVisible
    rank2Witness : Rank2ScalarInvisible
    evaluateScalarConductor : EquivariantResolved → ScalarConductorValue
    equivariantEvaluationExactSaturated : Type ℓ
    noIndexTwoDefectForIdealDescent : Type ℓ

    PhysicalResolvedIdealComparisonSelection : Type ℓ
    PhysicalRelationOnlyCompatibility : Type ℓ
