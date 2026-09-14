{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidReflectedConormalButterfly where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidHigherCoherenceHom

-- A four-edge loop on one moduli surface.  The type deliberately does not
-- assert that the loop bounds a square.
record ButterflyLoop {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Surface : Type ℓ
    base plus generic minus : Surface
    enterPlus : base ≡ plus
    plusToGeneric : plus ≡ generic
    genericToMinus : generic ≡ minus
    reflectedReturn : minus ≡ base

  butterflyBoundary : base ≡ base
  butterflyBoundary =
    enterPlus ∙ plusToGeneric ∙ genericToMinus ∙ reflectedReturn

open ButterflyLoop public

record ButterflyHolonomy {ℓ : Level} (Loop : ButterflyLoop {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    ScalarValue FirstConormalValue SecondaryValue : Type ℓ
    zeroScalar : ScalarValue
    betaEta35 : FirstConormalValue
    betaSquaredEta04Eta35 : SecondaryValue
    scalarReadout : base Loop ≡ base Loop → ScalarValue
    firstConormalReadout : base Loop ≡ base Loop → FirstConormalValue
    secondaryBoundaryReadout : base Loop ≡ base Loop → SecondaryValue
    scalarBoundaryIsNull : scalarReadout (butterflyBoundary Loop) ≡ zeroScalar
    firstBoundaryIsBetaEta35 :
      firstConormalReadout (butterflyBoundary Loop) ≡ betaEta35
    secondaryBoundaryIsMixedObstruction :
      secondaryBoundaryReadout (butterflyBoundary Loop) ≡ betaSquaredEta04Eta35
    secondaryReadoutOfConstantLoopIsZero :
      secondaryBoundaryReadout refl ≡ betaSquaredEta04Eta35 → ⊥

open ButterflyHolonomy public

NaiveButterflyFiller : {ℓ : Level} → ButterflyLoop {ℓ} → Type ℓ
NaiveButterflyFiller Loop = butterflyBoundary Loop ≡ refl

-- The computed mixed holonomy rules out filling the boundary by an ordinary
-- square on the same surface.  A valid continuation must enlarge the target
-- or provide operation-coherent higher data.
noNaiveButterflyFiller : {ℓ : Level} (Loop : ButterflyLoop {ℓ})
  (Holonomy : ButterflyHolonomy Loop) → NaiveButterflyFiller Loop → ⊥
noNaiveButterflyFiller Loop Holonomy filler =
  secondaryReadoutOfConstantLoopIsZero Holonomy
    (cong (secondaryBoundaryReadout Holonomy) (sym filler) ∙
     secondaryBoundaryIsMixedObstruction Holonomy)

-- Filling is kept as separate data: known holonomy does not manufacture it.
record ChainTarget {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Carrier : Type ℓ
    zeroCarrier : Carrier
    differential : Carrier → Carrier
    differentialSquaresToZero : (x : Carrier) →
      differential (differential x) ≡ zeroCarrier

-- This is the exact interface for adjoining one mixed higher cell.
record MinimalMixedCellExtension {ℓ : Level} (Old : ChainTarget {ℓ})
  : Type (ℓ-suc ℓ) where
  open ChainTarget Old renaming (Carrier to OldCarrier; differential to oldD)
  field
    ExtendedCarrier GenericQ : Type ℓ
    zeroExtended : ExtendedCarrier
    extendedD : ExtendedCarrier → ExtendedCarrier
    includeOld : OldCarrier → ExtendedCarrier
    mixedObstruction : OldCarrier
    q04-35 : ExtendedCarrier
    extendedDifferentialSquaresToZero : (x : ExtendedCarrier) →
      extendedD (extendedD x) ≡ zeroExtended
    inclusionIsChainMap : (x : OldCarrier) →
      extendedD (includeOld x) ≡ includeOld (oldD x)
    newCellKillsMixedObstruction :
      extendedD q04-35 ≡ includeOld mixedObstruction

    projectGenericQ : ExtendedCarrier → GenericQ
    zeroGenericQ : GenericQ
    genericQDifferential : GenericQ → GenericQ
    genericQProjectionIsChainMap : (x : ExtendedCarrier) →
      projectGenericQ (extendedD x) ≡
      genericQDifferential (projectGenericQ x)
    newCellHasZeroGenericQProjection :
      projectGenericQ q04-35 ≡ zeroGenericQ

    reflection : ExtendedCarrier → ExtendedCarrier
    reflectionSquaresToIdentity : (x : ExtendedCarrier) →
      reflection (reflection x) ≡ x
    reflectionCommutesWithDifferential : (x : ExtendedCarrier) →
      reflection (extendedD x) ≡ extendedD (reflection x)
    degreeAndSupportArePhysicallyAdmissible : Type ℓ

mixedObstructionIsClosedInExtension : {ℓ : Level}
  (Old : ChainTarget {ℓ}) (Extension : MinimalMixedCellExtension Old) →
  MinimalMixedCellExtension.includeOld Extension
    (ChainTarget.differential Old
      (MinimalMixedCellExtension.mixedObstruction Extension)) ≡
  MinimalMixedCellExtension.zeroExtended Extension
mixedObstructionIsClosedInExtension Old Extension =
  sym (MinimalMixedCellExtension.inclusionIsChainMap Extension
    (MinimalMixedCellExtension.mixedObstruction Extension)) ∙
  cong (MinimalMixedCellExtension.extendedD Extension)
    (sym (MinimalMixedCellExtension.newCellKillsMixedObstruction Extension)) ∙
  MinimalMixedCellExtension.extendedDifferentialSquaresToZero Extension
    (MinimalMixedCellExtension.q04-35 Extension)

-- Candidate interpretation: the new cell belongs to an augmented totalization,
-- is invisible on every visible boundary quotient, and is consumed by the
-- connecting map of the next evaluation cycle.
record AugmentedTotalPyramidResidue {ℓ : Level}
  (Old : ChainTarget {ℓ}) (Extension : MinimalMixedCellExtension Old)
  : Type (ℓ-suc ℓ) where
  open MinimalMixedCellExtension Extension
  field
    TotalPyramid BaseNullState PlusRestriction MinusRestriction : Type ℓ
    NextCycleTarget : Type ℓ
    zeroPlus : PlusRestriction
    zeroMinus : MinusRestriction

    totalizePyramid : TotalPyramid → ExtendedCarrier
    baseNullInclusion : BaseNullState → ExtendedCarrier
    entirePyramidResidue : BaseNullState
    residueIsMixedHigherCell :
      baseNullInclusion entirePyramidResidue ≡ q04-35

    restrictBaseNullPlus : BaseNullState → PlusRestriction
    restrictBaseNullMinus : BaseNullState → MinusRestriction
    residueHasZeroPlusRestriction :
      restrictBaseNullPlus entirePyramidResidue ≡ zeroPlus
    residueHasZeroMinusRestriction :
      restrictBaseNullMinus entirePyramidResidue ≡ zeroMinus
    residueHasZeroGenericRestriction :
      projectGenericQ (baseNullInclusion entirePyramidResidue) ≡ zeroGenericQ

    nextCycleConnectingMap : BaseNullState → NextCycleTarget
    nextCycleEvaluation : NextCycleTarget
    residueFeedsNextCycle :
      nextCycleConnectingMap entirePyramidResidue ≡ nextCycleEvaluation
    connectingMapIsNotTemporalIteration : Type ℓ
    residueRequiresWholePyramidTotalization : Type ℓ
    baseNullStateIsNotExistingVisibleVertex : Type ℓ

baseNullResidueHasMixedBoundary : {ℓ : Level}
  (Old : ChainTarget {ℓ}) (Extension : MinimalMixedCellExtension Old)
  (Residue : AugmentedTotalPyramidResidue Old Extension) →
  MinimalMixedCellExtension.extendedD Extension
    (AugmentedTotalPyramidResidue.baseNullInclusion Residue
      (AugmentedTotalPyramidResidue.entirePyramidResidue Residue)) ≡
  MinimalMixedCellExtension.includeOld Extension
    (MinimalMixedCellExtension.mixedObstruction Extension)
baseNullResidueHasMixedBoundary Old Extension Residue =
  cong (MinimalMixedCellExtension.extendedD Extension)
    (AugmentedTotalPyramidResidue.residueIsMixedHigherCell Residue) ∙
  MinimalMixedCellExtension.newCellKillsMixedObstruction Extension

baseNullResidueIsInvisibleInGenericQ : {ℓ : Level}
  (Old : ChainTarget {ℓ}) (Extension : MinimalMixedCellExtension Old)
  (Residue : AugmentedTotalPyramidResidue Old Extension) →
  MinimalMixedCellExtension.projectGenericQ Extension
    (MinimalMixedCellExtension.q04-35 Extension) ≡
  MinimalMixedCellExtension.zeroGenericQ Extension
baseNullResidueIsInvisibleInGenericQ Old Extension Residue =
  MinimalMixedCellExtension.newCellHasZeroGenericQProjection Extension

record CurrentTargetMixedCellAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    ExistingTarget OrdinaryCurrentTargetFiller : Type ℓ
    ordinaryCurrentTargetFillerWouldLiftPrimitiveCenter :
      OrdinaryCurrentTargetFiller → Type ℓ
    noOrdinaryCurrentTargetFiller : OrdinaryCurrentTargetFiller → ⊥
    exceptionalMixedCoherenceIsNonboundary : Type ℓ
    adjoiningOneCellRemainsAProposedTargetExtension : Type ℓ
    noPhysicalAuthorizationForNewCellYet : Type ℓ

record ButterflyFillingProblem {ℓ : Level}
  (Loop : ButterflyLoop {ℓ}) (Holonomy : ButterflyHolonomy Loop)
  : Type (ℓ-suc ℓ) where
  field
    HigherTarget : Type ℓ
    higherHomComplex : HigherCoherenceHomComplex {ℓ}
    maurerCartanBoundary :
      ButterflyMaurerCartanBoundary higherHomComplex
    higherCoherenceLiftProblem :
      HigherCoherenceLiftProblem higherHomComplex maurerCartanBoundary
    augmentedHigherHom :
      AugmentedHigherCoherenceHom higherHomComplex maurerCartanBoundary
    augmentationHasNoRetractionToCurrentRHom :
      CurrentRHomRetraction higherHomComplex maurerCartanBoundary
        augmentedHigherHom → ⊥
    CandidateFiller : Type ℓ
    boundaryOf : CandidateFiller → SecondaryValue Holonomy
    fillsMixedBoundary : CandidateFiller → Type ℓ
    MinimalExtensionTarget : ChainTarget {ℓ}
    minimalMixedCellExtension :
      MinimalMixedCellExtension MinimalExtensionTarget
    augmentedTotalPyramidResidue :
      AugmentedTotalPyramidResidue MinimalExtensionTarget
        minimalMixedCellExtension
    currentTargetAudit : CurrentTargetMixedCellAudit {ℓ}
    fillingRequiresPhysicalEndpointAndOperationData : Type ℓ
    candidateIsNotNaiveSameSurfaceSquare :
      CandidateFiller → NaiveButterflyFiller Loop → ⊥

-- Certificates for the three newly computed faces of the proposed loop.
record RelativeOperationFibreCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    NativeYoneda ExteriorOccurrence RelativeHopfAlgebra : Type ℓ
    relativeHopfAlgebra : RelativeHopfAlgebra
    relativeHopfAlgebraIsFreeOnFortyNinePrimitives : Type ℓ
    primitiveCountsAreNineEighteenFifteenSixOne : Type ℓ
    quadraticPartIsNineMixedAnticommutators : Type ℓ
    bothEndpointModulesDetectQuadraticPart : Type ℓ
    genericCoefficientLineDetectsOnlyAugmentation : Type ℓ
    reflectionTransportHasDecomposableCorrections : Type ℓ
    nonlinearRealizationHasUnseenWhiteheadClasses : Type ℓ
    nonlinearRealizationIsNotPhysicalStateSpace : Type ℓ

record SourceRelativeBareQTraceCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    SevenEquationKoszulSource FullTarget EndpointSupport BareQ : Type ℓ
    SourceRelativeTrace PrimitiveBareQClass : Type ℓ
    sourceRelativeTrace : SourceRelativeTrace
    primitiveBareQClass : PrimitiveBareQClass
    traceIsDefinedOnWholeHomComplex : Type ℓ
    quadraticTraceRequiresOccurrenceKoszulCorrection : Type ℓ
    auxiliaryNormalAndExcessFactorIsRemoved : Type ℓ
    productCartierGeneratorAndDeterminantAreRetained : Type ℓ
    allEightChannelsGiveSameBareQMatrixInDifferentFrames : Type ℓ
    bareQClassHasDegreeFourAndIsPrimitive : Type ℓ
    coefficientLiftSpaceAtFixedGenericClassIsContractible : Type ℓ
    bothEndpointCompositesRemainExact : Type ℓ
    noPhysicalEndpointConnectorIsConstructed : Type ℓ

record ConormalTraceExtensionCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    NormalizedTraceDiagram ScalarGrade FirstConormalGrade : Type ℓ
    ConormalExtension MixedQuadraticObstruction : Type ℓ
    conormalExtension : ConormalExtension
    firstConormalDifferenceIsBetaEta35 : Type ℓ
    conormalExtensionIsNonsplitOverPolynomialBetaFamily : Type ℓ
    conormalExtensionSplitsAtBetaZero : Type ℓ
    same35DirectionContinuationExists : Type ℓ
    rightMultiplicationByEta35HasRankFive : Type ℓ
    rightMultiplicationKernelIsEta35Line : Type ℓ
    reflected04ContinuationIsObstructed : Type ℓ
    mixedQuadraticObstruction : MixedQuadraticObstruction
    obstructionIsBetaSquaredEta04Eta35 : Type ℓ
    obstructionDoesNotMeanReflectionFails : Type ℓ

-- A typed boundary for the proposed same-surface loop.  This records which
-- edges are known and isolates the genuinely physical edges and fillers.
record ReflectedConormalButterflySpecification {ℓ : Level}
  (Operations : RelativeOperationFibreCertificate {ℓ})
  (Generic : SourceRelativeBareQTraceCertificate {ℓ})
  (Conormal : ConormalTraceExtensionCertificate {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    loop : ButterflyLoop {ℓ}
    holonomy : ButterflyHolonomy loop
    fillingProblem : ButterflyFillingProblem loop holonomy

    PhysicalSource PlusEndpointSource MinusEndpointSource : Type ℓ
    FullTarget BareQ PlusEndpoint MinusEndpoint : Type ℓ

    genericMap : PhysicalSource → BareQ
    coefficientLift : PhysicalSource → FullTarget
    restrictPlus : FullTarget → PlusEndpoint
    restrictMinus : FullTarget → MinusEndpoint

    PlusCoefficientNullhomotopy MinusCoefficientNullhomotopy : Type ℓ
    plusCoefficientNullhomotopy : PlusCoefficientNullhomotopy
    minusCoefficientNullhomotopy : MinusCoefficientNullhomotopy
    coefficientNullhomotopiesHaveHigherCoherence : Type ℓ

    plusSourceComparison : PlusEndpointSource → PhysicalSource
    minusSourceComparison : MinusEndpointSource → PhysicalSource
    plusPhysicalGysin : PlusEndpointSource → PlusEndpoint
    minusPhysicalGysin : MinusEndpointSource → MinusEndpoint

    PlusPhysicalComparison MinusPhysicalComparison : Type ℓ
    plusPhysicalComparison : PlusPhysicalComparison
    minusPhysicalComparison : MinusPhysicalComparison
    comparisonsAreNotIdentificationsWithCoefficientNullClasses : Type ℓ

    reflectedEndpointTransport : MinusEndpoint → PlusEndpoint
    reflectedSourceTransport : PlusEndpointSource → MinusEndpointSource
    reflectionExchanges35And04NormalLines : Type ℓ

    ScalarHolonomy FirstConormalHolonomy SecondaryBoundary : Type ℓ
    scalarHolonomyIsNull : ScalarHolonomy
    firstConormalHolonomyIsBetaEta35 : FirstConormalHolonomy
    secondaryBoundaryIsBetaSquaredEta04Eta35 : SecondaryBoundary
    abstractLoopReadoutsAgreeWithCoefficientCertificates : Type ℓ
    secondaryBoundaryIsRetainedNotDeclaredZero : Type ℓ

    RelativeOperationCompatibility : Type ℓ
    relativeOperationCompatibility : RelativeOperationCompatibility
    endpointActionsAreNontrivial : Type ℓ
    genericActionIsCurrentlyOnlyAugmentation : Type ℓ
    decomposableReflectionCorrectionIsRetained : Type ℓ

    CandidateHigherFiller : Type ℓ
    candidateHigherFillerWouldKillSecondaryBoundary :
      CandidateHigherFiller → Type ℓ
    physicalHigherFillerIsAdditionalData : Type ℓ

record ReflectedConormalButterflyConstructionBoundary {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    KnownGenericCoefficientLoop : Type ℓ
    knownGenericCoefficientLoop : KnownGenericCoefficientLoop
    KnownFirstConormalHolonomy : Type ℓ
    knownFirstConormalHolonomy : KnownFirstConormalHolonomy
    KnownMixedSecondaryBoundary : Type ℓ
    knownMixedSecondaryBoundary : KnownMixedSecondaryBoundary
    MissingPhysicalEndpointGysinComparisons : Type ℓ
    missingPhysicalEndpointGysinComparisons :
      MissingPhysicalEndpointGysinComparisons
    MissingOperationCoherentHigherFiller : Type ℓ
    missingOperationCoherentHigherFiller :
      MissingOperationCoherentHigherFiller
