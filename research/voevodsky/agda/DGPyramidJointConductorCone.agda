{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidJointConductorCone where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTCellPyramid
open import DGPyramidConductorChannels

record EndpointCompleteReverseConeCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    BranchVolumeLine ConductorLine ReverseCone Attachment : Type ℓ
    SixteenBranchLines FifteenConductorLines : Type ℓ
    sixteenBranchWitness : SixteenBranchLines
    fifteenConductorWitness : FifteenConductorLines
    attachment : Attachment
    reverseCone : ReverseCone
    FifteenBySixteenAttachment : Type ℓ
    attachmentSizeWitness : FifteenBySixteenAttachment

    PositiveEndpointBlock NegativeEndpointBlock : Type ℓ
    positiveEndpointBlock : PositiveEndpointBlock
    negativeEndpointBlock : NegativeEndpointBlock
    endpointBlocksNonzero : Type ℓ
    endpointAnnihilatorUnchanged : Type ℓ

    SplitCohomologyReplacement : Type ℓ
    splitReplacement : SplitCohomologyReplacement
    SpuriousDegreeMinusSevenClasses : Type ℓ
    splitReplacementIsWrong : SpuriousDegreeMinusSevenClasses
    SquareZeroWithoutEndpoints : Type ℓ
    squareZeroDoesNotDetectEndpointExtension : SquareZeroWithoutEndpoints

    GenericReverseSquare EndpointReverseSquare : Type ℓ
    genericReverseSquare : GenericReverseSquare
    endpointReverseSquare : EndpointReverseSquare
    chartHomotopyCoherence : Type ℓ

record ConductorIdealResolvedMapCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    ConductorIdeal StrictMap ResolvedMap GeneratorValue RelationValue : Type ℓ
    Rank16Strict Rank40Resolved Rank34GeneratorImage Rank6RelationKernel : Type ℓ
    rank16Witness : Rank16Strict
    rank40Witness : Rank40Resolved
    rank34Witness : Rank34GeneratorImage
    rank6Witness : Rank6RelationKernel
    evaluateGenerators : ResolvedMap → GeneratorValue
    relationValue : ResolvedMap → RelationValue
    generatorKernelIsRelationData : Type ℓ
    strictMapsEmbedSaturated : Type ℓ

    EquivariantResolvedMap AlternatingScalarValue : Type ℓ
    Rank13Equivariant Rank11ScalarVisible Rank2RelationOnly : Type ℓ
    rank13Witness : Rank13Equivariant
    rank11Witness : Rank11ScalarVisible
    rank2Witness : Rank2RelationOnly
    evaluateAlternatingScalar : EquivariantResolvedMap → AlternatingScalarValue
    invariantEvaluationSaturated : Type ℓ
    noIndexTwoDefectInThisProblem : Type ℓ
    PhysicalResolvedConductorMapSelection : Type ℓ

record JointNormalizationDualCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    NodeResolution PlusSheetMap MinusSheetMap SheetHomotopy : Type ℓ
    nodeResolution : NodeResolution
    plusSheetMap : PlusSheetMap
    minusSheetMap : MinusSheetMap
    sheetHomotopy : SheetHomotopy
    jointSheetHomotopyEquation : Type ℓ
    normalizationFibreEquivalence : Type ℓ

    PlusBranchDual MinusBranchDual ConductorDual : Type ℓ
    plusBranchDual : PlusBranchDual
    minusBranchDual : MinusBranchDual
    conductorDual : ConductorDual
    DegreeThreeBranches DegreeFiveConductor SixOccurrenceDeterminant : Type ℓ
    branchDegreeWitness : DegreeThreeBranches
    conductorDegreeWitness : DegreeFiveConductor
    sixDeterminantWitness : SixOccurrenceDeterminant
    conductorIsSixfoldTransgression : Type ℓ

    SourceGluingCocycle PrimitiveSixfoldResidue : Type ℓ
    sourceGluingCocycle : SourceGluingCocycle
    primitiveSixfoldResidue : PrimitiveSixfoldResidue
    conductorPairing : ConductorDual → SourceGluingCocycle → PrimitiveSixfoldResidue
    primitivePairingEquation : Type ℓ
    conductorUnitReflectionHomotopy : Type ℓ

    FivefoldAxisGysin NodePullback : Type ℓ
    fivefoldAxisGysin : FivefoldAxisGysin
    pullbackToNode : FivefoldAxisGysin → NodePullback
    SupportCounit : NodePullback → Type ℓ
    DerivedConductorSpecialization : NodePullback → Type ℓ
    ZeroCounit : Type ℓ
    ZeroSpecialization : Type ℓ
    fivefoldNodeCounitZero :
      SupportCounit (pullbackToNode fivefoldAxisGysin) → ZeroCounit
    fivefoldNodeSpecializationZero :
      DerivedConductorSpecialization (pullbackToNode fivefoldAxisGysin) →
      ZeroSpecialization
    noFivefoldNodeEndpointPromotion : Type ℓ

    SignedBranchSector : Type ℓ
    rowChannelToSignedBranch : TRow → SignedBranchSector
    signedBranchToJointConductor : SignedBranchSector → ConductorDual
    FourToTwoToOneReconstruction : Type ℓ
    fourToTwoToOneWitness : FourToTwoToOneReconstruction

    PhysicalJointNormalizationDualComparison : Type ℓ
