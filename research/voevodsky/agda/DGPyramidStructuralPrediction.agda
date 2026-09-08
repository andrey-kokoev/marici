{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidStructuralPrediction where

open import Cubical.Foundations.Prelude
open import DGPyramidMarkedGalleryToricDescent
open import DGPyramidConductorFormalTower

-- A small diagnostic table: these interfaces expose only structure already
-- forced by the chain calculations.  They do not postulate a six-functor
-- formalism or an unspecified infinity-category.
data Capability : Type₀ where
  dgHom supportGluing equivariantTarget framedDetection excessLayers
    continuousCompletion : Capability

data CapabilityStatus : Type₀ where
  witnessed predicted unresolved : CapabilityStatus

data DetectorValue : Type₀ where
  zeroValue unitValue : DetectorValue

data SupportValue : Type₀ where
  absent retained : SupportValue

record PhysicalPredictionFingerprint : Type₀ where
  field
    primaryCoordinate reciprocalECoordinate reciprocalRCoordinate : DetectorValue
    localPuncturedDual endpointCartierCell relationCoordinate : SupportValue
    occurrenceTwoExtension nativeTripleResidues : SupportValue
    cechSupportedReciprocalTrace oddConductorClass : SupportValue
    shortReesDefectComplexes defectGenericQImage : SupportValue
    primaryIsUnit : primaryCoordinate ≡ unitValue
    reciprocalEIsUnit : reciprocalECoordinate ≡ unitValue
    reciprocalRIsZero : reciprocalRCoordinate ≡ zeroValue
    puncturedDualIsRetained : localPuncturedDual ≡ retained
    endpointCellIsRetained : endpointCartierCell ≡ retained
    relationCoordinateIsRetained : relationCoordinate ≡ retained
    occurrenceTwoExtensionIsRetained : occurrenceTwoExtension ≡ retained
    nativeTripleResiduesAreRetained : nativeTripleResidues ≡ retained
    cechSupportedReciprocalTraceIsRetained : cechSupportedReciprocalTrace ≡ retained
    oddConductorClassIsRetained : oddConductorClass ≡ retained
    shortReesDefectComplexesAreRetained : shortReesDefectComplexes ≡ retained
    defectGenericQImageIsAbsent : defectGenericQImage ≡ absent

record PhysicalPredictionObservation : Type₀ where
  field
    observedPrimary observedReciprocalE observedReciprocalR : DetectorValue
    observedPuncturedDual observedEndpointCell observedRelation : SupportValue
    observedOccurrenceTwoExtension observedNativeTripleResidues : SupportValue
    observedCechSupportedReciprocalTrace observedOddConductorClass : SupportValue
    observedShortReesDefectComplexes observedDefectGenericQImage : SupportValue

record MatchesPhysicalPrediction
  (expected : PhysicalPredictionFingerprint)
  (observed : PhysicalPredictionObservation) : Type₀ where
  field
    primaryMatches :
      PhysicalPredictionObservation.observedPrimary observed ≡
      PhysicalPredictionFingerprint.primaryCoordinate expected
    reciprocalEMatches :
      PhysicalPredictionObservation.observedReciprocalE observed ≡
      PhysicalPredictionFingerprint.reciprocalECoordinate expected
    reciprocalRMatches :
      PhysicalPredictionObservation.observedReciprocalR observed ≡
      PhysicalPredictionFingerprint.reciprocalRCoordinate expected
    puncturedDualMatches :
      PhysicalPredictionObservation.observedPuncturedDual observed ≡
      PhysicalPredictionFingerprint.localPuncturedDual expected
    endpointCellMatches :
      PhysicalPredictionObservation.observedEndpointCell observed ≡
      PhysicalPredictionFingerprint.endpointCartierCell expected
    relationMatches :
      PhysicalPredictionObservation.observedRelation observed ≡
      PhysicalPredictionFingerprint.relationCoordinate expected
    occurrenceTwoExtensionMatches :
      PhysicalPredictionObservation.observedOccurrenceTwoExtension observed ≡
      PhysicalPredictionFingerprint.occurrenceTwoExtension expected
    nativeTripleResiduesMatch :
      PhysicalPredictionObservation.observedNativeTripleResidues observed ≡
      PhysicalPredictionFingerprint.nativeTripleResidues expected
    cechSupportedReciprocalTraceMatches :
      PhysicalPredictionObservation.observedCechSupportedReciprocalTrace observed ≡
      PhysicalPredictionFingerprint.cechSupportedReciprocalTrace expected
    oddConductorClassMatches :
      PhysicalPredictionObservation.observedOddConductorClass observed ≡
      PhysicalPredictionFingerprint.oddConductorClass expected
    shortReesDefectComplexesMatch :
      PhysicalPredictionObservation.observedShortReesDefectComplexes observed ≡
      PhysicalPredictionFingerprint.shortReesDefectComplexes expected
    defectGenericQImageMatches :
      PhysicalPredictionObservation.observedDefectGenericQImage observed ≡
      PhysicalPredictionFingerprint.defectGenericQImage expected

-- Directed edges are obligations, not logical implications derivable from a
-- capability name alone.
data CapabilityEdge : Capability → Capability → Type₀ where
  dgToFramedDetection : CapabilityEdge dgHom framedDetection
  supportToContinuous : CapabilityEdge supportGluing continuousCompletion
  supportToEquivariance : CapabilityEdge supportGluing equivariantTarget
  excessToFramedDetection : CapabilityEdge excessLayers framedDetection

record CapabilityRow {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    capability : Capability
    status : CapabilityStatus
    ExistingWitness RequiredOperation Falsifier : Type ℓ
    existingWitness : ExistingWitness
    -- A falsifier is data that must be rejected, not evidence obtained by
    -- assuming the desired operation.
    rejects : Falsifier → Type ℓ

record DGEnrichedComparison {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Object HomComplex : Type ℓ
    source target : Object
    hom : Object → Object → HomComplex
    identity : Object → HomComplex
    compose : HomComplex → HomComplex → HomComplex
    differentialCompatibleComposition : Type ℓ
    sourceRelationCellsRetained : Type ℓ

record SupportedRecollementComparison {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Whole Formal Punctured Overlap : Type ℓ
    restrictFormal : Whole → Formal
    restrictPunctured : Whole → Punctured
    formalToOverlap : Formal → Overlap
    puncturedToOverlap : Punctured → Overlap
    reconstruction : Type ℓ
    puncturedPartNotDeterminedByAffineCompletedDual : Type ℓ

record EquivariantTargetTransport {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Target Transport : Type ℓ
    target35 target04 : Target
    physicalReflection : Transport
    reflectionCarries35To04 : Type ℓ
    reflectionSquaredCoherence : Type ℓ
    transportedOrientationLine : Type ℓ

record FramedDualityDetector {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Comparison Primary Reciprocal Relation : Type ℓ
    primary : Comparison → Primary
    reciprocal : Comparison → Reciprocal
    relation : Comparison → Relation
    threeCoordinatesAreJointlyDetecting : Type ℓ
    primaryAloneIsNotDetecting : Type ℓ

record ExcessFiltration {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Comparison PrimaryPart NativeOccurrencePart RelationPart : Type ℓ
    primaryLayer : Comparison → PrimaryPart
    nativeOccurrenceLayer : Comparison → NativeOccurrencePart
    relationLayer : Comparison → RelationPart
    decompositionRetainedByCartier : Type ℓ
    longReesExcessRemainsDistinct : Type ℓ

record NativeUniversalOverlapComparison {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    NativeNode AuxiliaryNode OccurrenceBase ComparisonCone : Type ℓ
    nativeNode : NativeNode
    auxiliaryNode : AuxiliaryNode
    commonOccurrenceBase : OccurrenceBase
    occurrencePreservingAugmentation : AuxiliaryNode → NativeNode
    allSixNativeOccurrenceDirectionsPreserved : Type ℓ
    exactlyTwoAuxiliaryDirectionsKilledAtFirstOrder : Type ℓ
    comparisonIsQuotientNotEquivalence : Type ℓ
    exactKernelContainsAuxiliaryTailsAndMixedProducts : Type ℓ
    comparisonCone : ComparisonCone
    NineQuadraticTorCokernel : Type ℓ
    nineQuadraticTorCokernel : NineQuadraticTorCokernel
    TripleOccurrenceResidue : Type ℓ
    positiveTripleResidue negativeTripleResidue : TripleOccurrenceResidue
    bothTripleOccurrenceResiduesPreservedWithCoefficientOne : Type ℓ
    restrictedScalarTangentFactorizationWouldLoseDirections : Type ℓ
    restrictedScalarTangentArgumentIsNotAnObstructionToThisBridge : Type ℓ
    nativeDualizingConductorAttachmentIsNontrivial : Type ℓ
    auxiliaryNormalizationPullbackHasUnboundedTor : Type ℓ

record W03CechSupportedTraceDescent {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    NegativeLocalization PositiveLocalization SupportedTraceComplex : Type ℓ
    negativeLocalization : NegativeLocalization
    positiveLocalization : PositiveLocalization
    separateBranchLocalizationsAreNonzero : Type ℓ
    simultaneousMixedLaurentLocalizationIsZero : Type ℓ
    supportedTraceComplex : SupportedTraceComplex

    SupportedReciprocalTrace Counit : Type ℓ
    supportedNuE supportedNuR : SupportedReciprocalTrace
    supportedTraceRankTwo : Type ℓ
    counit : Counit
    supportedCounitIsIdentityOnTraceClasses : Type ℓ
    zeroUnitRepresentativesExist : Type ℓ
    supportAddsNoClassAmbiguityOverFixedTrace : Type ℓ

    RelationOnlySupportedClass : Type ℓ
    relationOnlySupportedClass : RelationOnlySupportedClass
    relationClassUsesBothLocalizedCharts : Type ℓ
    relationClassHasCoordinatesOneMinusOne : Type ℓ
    forgettingEitherLocalizedComparisonLosesRelation : Type ℓ

    CechCartierInterchange CanonicalOddConductorClass : Type ℓ
    cechCartierInterchange : CechCartierInterchange
    interchangeSquaresToIdentity : Type ℓ
    interchangeSignOnDoublyShiftedComponents : Type ℓ
    bothSupportedTracesSurviveCartier : Type ℓ
    canonicalOddConductorClass : CanonicalOddConductorClass
    conductorClassHasExactOccurrenceIdealAnnihilator : Type ℓ
    conductorClassIsPolarityOddWithoutDividingByTwo : Type ℓ
    nodalTorShiftsMixedResidueFromCechTwoToOne : Type ℓ

record ShortReesSupportedDefectCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SelectionCone SupportedLocalizationCone DefectInput : Type ℓ
    selectionCone : SelectionCone
    supportedLocalizationCone : SupportedLocalizationCone
    comparisonOfSelectionAndLocalizationTriangles : Type ℓ
    eightCompleteProductCartierInputs : DefectInput
    sixFirstConormalDefectsAreNull : Type ℓ
    eightHigherWedgeDefectsAreNonzero : Type ℓ

    QuadraticDivisorDiagram CubicDivisorIncidence : Type ℓ
    quadraticTwoDivisorDiagram : QuadraticDivisorDiagram
    cubicNonsplitDivisorIncidence : CubicDivisorIncidence
    cubicTripleIntersectionClassRetained : Type ℓ
    lowerPartialPoleTermsAreRequired : Type ℓ
    highestPoleProjectionKillsAllEightDefects : Type ℓ
    eightPrimitiveCentralNativeExtensions : Type ℓ
    supportedMapsAreNotOrdinaryRawSelectionLifts : Type ℓ

    NativeCap EndpointComposite GenericQ : Type ℓ
    nativeCap : NativeCap
    endpointComposite : EndpointComposite
    sixQuadraticCapImagesAreIdenticallyZero : Type ℓ
    twoCubicImagesGivePrimitiveLowerSupportClasses : Type ℓ
    cubicOppositeEndpointBoundaryHasMarkedNormalNullhomotopy : Type ℓ
    everyDefectGenericQImageIsZero : Type ℓ
    existingCapThenResidueCannotProduceRequiredGenericMap : Type ℓ
    RequiredDirectPhysicalDefectCorrespondence : Type ℓ

record RelativeOccurrenceExtension {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    RelativeOccurrenceComplex ScalarHomology UpperAnnihilator : Type ℓ
    relativeOccurrenceComplex : RelativeOccurrenceComplex
    scalarHomology : ScalarHomology
    upperAnnihilator : UpperAnnihilator
    relativeProjectionIsMinusBetaIdentityOnTwoClasses : Type ℓ
    scalarProjectionIdentifiesTwoExcessClasses : Type ℓ
    PrimitiveTwoExtension : Type ℓ
    primitiveTwoExtension : PrimitiveTwoExtension
    occurrenceComplexDoesNotSplitAsHomologySum : Type ℓ
    twoEndpointLiftingObstructions : Type ℓ
    scalarProjectionLosesPrimitiveRelationCoordinate : Type ℓ
    mixedSheetLaurentBaseChangeIsZeroRing : Type ℓ

record MinimalPredictiveEnvelope {ℓ : Level}
  (DG : DGEnrichedComparison {ℓ})
  (Support : SupportedRecollementComparison {ℓ})
  (Equivariance : EquivariantTargetTransport {ℓ})
  (Duality : FramedDualityDetector {ℓ})
  (Excess : ExcessFiltration {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    dgCompositionActsOnThreeDetectors : Type ℓ
    supportGluingRetainsPuncturedReciprocalData : Type ℓ
    reflectionTransportsRatherThanFixesTarget : Type ℓ
    excessAssociatedGradedFeedsFramedDetection : Type ℓ
    completionIsContinuousAcrossFormalPuncturedOverlap : Type ℓ
    endpointCartierCellIsPartOfTheGluedMorphism : Type ℓ

    -- These separation laws prevent the envelope from manufacturing the
    -- missing physical identifications by definition.
    localDualNotCollapsedToAffineCompletedDual : Type ℓ
    nativeOccurrenceExcessNotCollapsedToLongExcess : Type ℓ
    endpointAttachmentNotCollapsedToFormalJet : Type ℓ

record MariciStructuralPrediction {ℓ : Level}
  (Gallery : MarkedGalleryToricDescentCertificate {ℓ})
  (FormalTower : ConductorFormalTowerCertificate {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    dgEnrichment : DGEnrichedComparison {ℓ}
    recollement : SupportedRecollementComparison {ℓ}
    equivariantTransport : EquivariantTargetTransport {ℓ}
    framedDuality : FramedDualityDetector {ℓ}
    excessFiltration : ExcessFiltration {ℓ}
    nativeUniversalOverlap : NativeUniversalOverlapComparison {ℓ}
    shortReesSupportedDefects : ShortReesSupportedDefectCertificate {ℓ}
    relativeOccurrenceExtension : RelativeOccurrenceExtension {ℓ}
    cechSupportedTraceDescent : W03CechSupportedTraceDescent {ℓ}
    minimalEnvelope :
      MinimalPredictiveEnvelope
        dgEnrichment recollement equivariantTransport framedDuality excessFiltration

    dgRow supportRow equivarianceRow dualityRow excessRow continuityRow :
      CapabilityRow {ℓ}
    dgRowClassifiesDG : CapabilityRow.capability dgRow ≡ dgHom
    supportRowClassifiesGluing : CapabilityRow.capability supportRow ≡ supportGluing
    equivarianceRowClassifiesTransport :
      CapabilityRow.capability equivarianceRow ≡ equivariantTarget
    dualityRowClassifiesDetection :
      CapabilityRow.capability dualityRow ≡ framedDetection
    excessRowClassifiesLayers : CapabilityRow.capability excessRow ≡ excessLayers
    continuityRowClassifiesCompletion :
      CapabilityRow.capability continuityRow ≡ continuousCompletion

    -- The known counterexamples populate the falsifier column.
    rejectsPrimaryOnlyComparison : Type ℓ
    rejectsAffineCompletedDualAsWholeTargetDual : Type ℓ
    rejectsFixedTargetPhysicalReflection : Type ℓ
    rejectsSingleUnnamedExcessLine : Type ℓ
    rejectsFiniteJetEndpointCriterion : Type ℓ
    rejectsForcingOccurrencesThroughAuxiliaryScalarTangent : Type ℓ
    rejectsSplitOccurrenceHomologyReplacement : Type ℓ
    rejectsMixedSheetLaurentBaseChange : Type ℓ
    rejectsSingleChartReciprocalTraceDescent : Type ℓ
    rejectsScalarizationOfOddConductorClass : Type ℓ

    -- Certified implication edges say which neighboring cells constrain one
    -- another.  They deliberately stop short of a full six-functor claim.
    dgDetectionEdge : CapabilityEdge dgHom framedDetection
    supportContinuityEdge : CapabilityEdge supportGluing continuousCompletion
    supportEquivarianceEdge : CapabilityEdge supportGluing equivariantTarget
    excessDetectionEdge : CapabilityEdge excessLayers framedDetection
    noAutomaticSixFunctorPromotion : Type ℓ
    noAutomaticInfinityCategoricalPromotion : Type ℓ

    -- Forgetting the diagnostic structures recovers the existing concrete
    -- certificates; it is not allowed to replace them.
    forgetDGToResolvedSourceRelations :
      DGEnrichedComparison {ℓ} → MarkedGalleryToricDescentCertificate {ℓ}
    forgetDGWitness : forgetDGToResolvedSourceRelations dgEnrichment ≡ Gallery

    forgetRecollementToFormalPunctured :
      SupportedRecollementComparison {ℓ} → ConductorFormalTowerCertificate {ℓ}
    forgetRecollementWitness :
      forgetRecollementToFormalPunctured recollement ≡ FormalTower

    -- Concrete prediction: the support-changing transfer, local punctured
    -- dual, reciprocal excess detector, and endpoint Cartier continuation
    -- must be one compatible square.  A ranks-only or primary-only candidate
    -- cannot inhabit this type.
    MarkedPuncturedReciprocalEndpointSquare :
      MarkedGalleryToricDescentCertificate {ℓ} →
      ConductorFormalTowerCertificate {ℓ} →
      DGEnrichedComparison {ℓ} →
      SupportedRecollementComparison {ℓ} →
      FramedDualityDetector {ℓ} → Type ℓ
    predictedSquare :
      MarkedPuncturedReciprocalEndpointSquare
        Gallery FormalTower dgEnrichment recollement framedDuality

    predictedSquareRetainsSourceRelationCoordinate : Type ℓ
    predictedSquareRetainsLocalPuncturedDual : Type ℓ
    predictedSquareTransportsEndpointCartierCell : Type ℓ
    predictedSquareRespects35To04Reflection : Type ℓ
    predictedSquareUsesOccurrencePreservingAuxiliaryQuotient : Type ℓ
    predictedSquarePreservesAllSixNativeConormalDirections : Type ℓ
    predictedSquarePreservesBothTripleOccurrenceResidues : Type ℓ
    predictedSquareRetainsPrimitiveOccurrenceTwoExtension : Type ℓ
    predictedSquareUsesDistinctSourceAndTargetCoefficientActions : Type ℓ
    predictedSquareFactorsReciprocalTraceThroughCechSupport : Type ℓ
    predictedSquarePreservesRankTwoSupportedCounit : Type ℓ
    predictedSquareRetainsTwoChartRelationHomotopies : Type ℓ
    predictedSquareCommutesWithCechCartierInterchange : Type ℓ
    predictedSquareDoesNotFactorEightDefectsThroughExistingCap : Type ℓ
    predictedSquareActsOnWholeDivisorIncidenceComplexes : Type ℓ

    -- Falsifiable output of the table.  The expected reciprocal coordinates
    -- are those of the source-specified map, not an arbitrary normalization.
    expectedPhysicalFingerprint : PhysicalPredictionFingerprint
    predictedCandidate : FramedDualityDetector.Comparison framedDuality
    observeCandidate :
      FramedDualityDetector.Comparison framedDuality →
      PhysicalPredictionObservation
    candidateFingerprintMatches :
      MatchesPhysicalPrediction
        expectedPhysicalFingerprint (observeCandidate predictedCandidate)
    fingerprintStableUnderEndpointCartierContinuation : Type ℓ
    fingerprintStableUnderPhysicalReflectionTransport : Type ℓ
