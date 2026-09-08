{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidSupportedTraceDuality where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidTCellPyramid

record SupportedOccurrenceTraceCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Ring LocalCohomology SupportedCovector Residue : Type ℓ
    primitiveResidue : Residue
    residueInLocalCohomology : Residue → LocalCohomology
    annihilatorIsResidualIdeal : Type ℓ
    SupportedReverseQuotient : Type ℓ
    supportedReverse : SupportedReverseQuotient → LocalCohomology
    reverseInverse : LocalCohomology → SupportedReverseQuotient
    reverseSection : (h : LocalCohomology) → supportedReverse (reverseInverse h) ≡ h
    reverseRetraction : (q : SupportedReverseQuotient) → reverseInverse (supportedReverse q) ≡ q

    firstLift secondLift comparisonHomotopy : SupportedCovector
    firstLiftValue secondLiftValue : Type ℓ
    liftsCompared : Type ℓ
    FixedOccurrenceFrame : Type ℓ
    framedTraceFibreContractible : Type ℓ

record WholeKoszulGysinCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    OccurrenceKoszul OccurrenceCech GenericLine Conductor : Type ℓ
    genericResidueMap : GenericLine → OccurrenceCech
    specializeGeneric : OccurrenceCech → Conductor
    zeroConductor : Conductor
    genericSpecializesToZero : (g : GenericLine) →
      specializeGeneric (genericResidueMap g) ≡ zeroConductor

    wholeKoszulGysin : OccurrenceKoszul → OccurrenceCech
    FourLiteralRows : Type ℓ
    fourRowsWitness : FourLiteralRows
    bottomCoefficientOne : Type ℓ
    conductorBottomSurvives : Type ℓ
    CodimensionTwoShift : Type ℓ
    DualConormalDeterminant : Type ℓ
    shiftWitness : CodimensionTwoShift
    determinantWitness : DualConormalDeterminant
    residueAndGysinDistinct : Type ℓ

record NormalizationSupportContinuationCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Node PlusSheet MinusSheet Conductor SupportedObject : Type ℓ
    nodeToPlusSheet : Node → PlusSheet
    nodeToMinusSheet : Node → MinusSheet
    plusAugmentation : PlusSheet → Conductor
    minusAugmentation : MinusSheet → Conductor
    supportNode : Node → SupportedObject
    DegreeZeroChannel DegreeTwoChannel : Type ℓ
    conductorIdealChannel : DegreeZeroChannel
    residueChannel : DegreeTwoChannel
    normalizationSquareCommutes : Type ℓ
    noIdenticalUnshiftedSheetModel : Type ℓ

record DescentDualityCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Base BoundaryModule CyclicObstruction ScalarTarget : Type ℓ
    obstruction : CyclicObstruction
    scalarPushout : BoundaryModule → ScalarTarget
    ThreeMixedPoleClasses : Type ℓ
    threeMixedPoleWitness : ThreeMixedPoleClasses
    ScalarBlindKernel : Type ℓ
    scalarBlindKernelWitness : ScalarBlindKernel
    nonzeroScalarBlindClass : CyclicObstruction
    scalarBlindNonzero : Type ℓ
    allBaseScalarTestsVanish : Type ℓ

    RelativeDualizing BranchTerm ConductorTerm : Type ℓ
    relativeDualizing : RelativeDualizing
    branchTerm : BranchTerm
    conductorTerm : ConductorTerm
    conductorOddUnderSheetExchange : Type ℓ
    NonSplitAttachment : Type ℓ
    nonSplitAttachmentWitness : NonSplitAttachment

    ConductorConormal SupportedDual : Type ℓ
    supportedDual : CyclicObstruction → ConductorConormal → SupportedDual
    supportedDualRetainsObstruction : Type ℓ
    ReverseComparisonTriangle : Type ℓ
    reverseTriangleWitness : ReverseComparisonTriangle

record EndpointCompleteTCellPyramidCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    interior : TCellPyramidCertificate {ℓ}
    EndpointCap : Type ℓ
    positiveCap negativeCap : EndpointCap
    FourteenBoundaryComponents : Type ℓ
    fourteenComponentsWitness : FourteenBoundaryComponents
    endpointProjectionPositive endpointProjectionNegative :
      FourteenBoundaryComponents → EndpointCap
    JointEndpointDetectionOnCyclicClass : Type ℓ
    jointEndpointDetectionWitness : JointEndpointDetectionOnCyclicClass
    EndpointCompleteCocycle : Type ℓ
    endpointCompleteCocycle : EndpointCompleteCocycle
    interiorRestriction : EndpointCompleteCocycle → Type ℓ
    NonSplitConductorAttachment : Type ℓ
    conductorAttachmentWitness : NonSplitConductorAttachment
    PhysicalEndpointCompleteCorrespondence : Type ℓ
