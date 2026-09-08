{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidShortFaceSpatialCap where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTCellPyramid
open import DGPyramidTStemSideProduct

record NativeShortFaceComparisonCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    NativeFaceRing ShortFaceRing NativeDual ShortFaceDual : Type ℓ
    shortToNativeQuotient : ShortFaceRing → NativeFaceRing
    nativeDualToShortDual : NativeDual → ShortFaceDual
    completeDerivedComparison : Type ℓ

    MixedShortEdge SameSheetEdge ConductorClass : Type ℓ
    mixed03 mixed25 mixed41 : MixedShortEdge
    sixSameSheetEdges : SameSheetEdge
    conductorClass : ConductorClass
    mixedEdgeBoundary : MixedShortEdge → ConductorClass
    threeMixedEdgesAttachConductor : Type ℓ

    MixedBridgeModule : Type ℓ
    threeBridgeKernel : MixedBridgeModule
    ConnectingRow111 : Type ℓ
    connectingRowWitness : ConnectingRow111
    TwoRouteDifferenceKernel : Type ℓ
    twoRouteDifferenceWitness : TwoRouteDifferenceKernel
    StrictRotationInvariantUnitLift : Type ℓ
    noStrictRotationInvariantUnitLift : StrictRotationInvariantUnitLift → ⊥

    NativeCubicalSubspace ShortFaceCubicalSubspace : Type ℓ
    nativeCubicalSubspace : NativeCubicalSubspace
    shortFaceCubicalSubspace : ShortFaceCubicalSubspace
    literalContainmentInExistingKernel : Type ℓ
    singletonStemsAreMixedEdges : Type ℓ
    pairStemsAreSameSheetEdges : Type ℓ

record JointConductorSpatialCapCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    NodeResolution EndpointRelativeTarget ComplementaryFaceCap : Type ℓ
    nodeResolution : NodeResolution
    complementaryFaceCap : ComplementaryFaceCap
    JointComparison EndpointComparison GenericComparison : Type ℓ
    jointComparison : JointComparison
    endpointComparison : EndpointComparison
    genericComparison : GenericComparison
    FortyThreeTerms SixteenSourceColumns : Type ℓ
    fortyThreeTermsWitness : FortyThreeTerms
    sixteenColumnsWitness : SixteenSourceColumns
    jointBoundaryEquation : Type ℓ

    GenericValue PlusEndpointValue MinusEndpointValue : Type ℓ
    genericValue : GenericValue
    plusEndpointValue : PlusEndpointValue
    minusEndpointValue : MinusEndpointValue
    JointDiagonal111 : Type ℓ
    jointDiagonalWitness : JointDiagonal111

    SpatialCochainDiagram ConstantCochain : Type ℓ
    spatialCochainDiagram : SpatialCochainDiagram
    constantCochain : ConstantCochain
    completeHomDiagramIsSpatialCochains : Type ℓ
    comparisonIsConstantOnFortyThreeVertices : Type ℓ
    ContractibleNormalizedComparison : Type ℓ
    contractibleComparisonWitness : ContractibleNormalizedComparison

    NodeConductorClass SixfoldResidue : Type ℓ
    reverseGenericLandsInNodeConductor : NodeConductorClass
    orientedSixfoldPairing : SixfoldResidue
    notFivefoldSingleSheetFactorization : Type ℓ

    PhysicalExcessReesComparison : Type ℓ
    PhysicalCollarFrameComparison : Type ℓ

record NormalizationSheetExtensionObstructionCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    IdealMap SheetMap ConductorValuedHomotopy ZerothOrderHomotopy : Type ℓ
    Rank40IdealMaps Rank9Killed Rank31Obstructions : Type ℓ
    rank40Witness : Rank40IdealMaps
    rank9Witness : Rank9Killed
    rank31Witness : Rank31Obstructions
    noNonzeroSameDegreeSheetMap : SheetMap → ⊥
    noNonzeroExtensionWithConductorValuedHomotopy : Type ℓ
    zerothOrderHomotopyKillsNine : Type ℓ
    extensionObstructionSequenceSaturated : Type ℓ

    DoubledConductorConnectingMap : Type ℓ
    doubledConductorObstruction : IdealMap → DoubledConductorConnectingMap
    connectingObstructionNonzeroOnQuotient : Type ℓ
    strictMapsSurvive relationOnlyMapsSurvive : Type ℓ

    Rank13Equivariant Rank3EquivariantlyKilled Rank10EquivariantObstructions : Type ℓ
    rank13Witness : Rank13Equivariant
    rank3Witness : Rank3EquivariantlyKilled
    rank10Witness : Rank10EquivariantObstructions
    equivariantObstructionSequenceSaturated : Type ℓ
    PhysicalNormalizationSheetExtension : Type ℓ
