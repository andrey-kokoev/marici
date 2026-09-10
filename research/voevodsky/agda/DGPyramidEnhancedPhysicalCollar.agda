{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidEnhancedPhysicalCollar where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidStructuralPrediction
open import DGPyramidNormalizationDualityDilation
open import DGPyramidAllDegreeEndpointTangential
open import DGPyramidReflectedConormalButterfly
open import DGPyramidAugmentedResidueCandidateAudit
open import DGPyramidPhysicalEndpointPullback

-- Specification of the smallest target on which the reference quadratic
-- short-Rees experiment is well typed.  No inhabitant is manufactured from
-- the coefficient-only principal-line calculation.
record EnhancedPhysicalCollarSpecification {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Flag Road CollarState : Type ℓ
    flagCountIsEightyFour : Type ℓ
    roadCountIsThree : Type ℓ
    collarStatesPerRoadAreSixteen : Type ℓ
    frontStatesPerRoadAreEight : Type ℓ
    backStatesPerRoadAreEight : Type ℓ
    middleStatesPerRoadAreEight : Type ℓ

    Coefficient PrincipalLine PrincipalDual : Type ℓ
    principalLine : Road → PrincipalLine
    principalDual : Road → PrincipalDual
    evaluatePrincipalPair : PrincipalLine → PrincipalDual → Coefficient
    primitivePrincipalEvaluation : Type ℓ
    allFrontBackAndMiddleCoefficientSquaresCommute : Type ℓ
    ordinaryUnitNormalizedFrontLiftIsImpossible : Type ℓ

    NormalState CechState EndpointState GenericQState : Type ℓ
    EnhancedState : Type ℓ
    includeCollar : CollarState → EnhancedState
    includeNormal : NormalState → EnhancedState
    includeCech : CechState → EnhancedState
    includeEndpoint : EndpointState → EnhancedState
    includeGenericQ : GenericQState → EnhancedState

    differential : EnhancedState → EnhancedState
    differentialSquaresToZero : Type ℓ
    principalLineDifferentialCompatibility : Type ℓ
    cechLocalizationDifferentialCompatibility : Type ℓ
    endpointButterflyConnectorCompatibility : Type ℓ
    genuineQProjectionIsChainMap : Type ℓ

    reflection rotation : EnhancedState → EnhancedState
    reflectionSquaresToIdentity : Type ℓ
    rotationHasOrderThree : Type ℓ
    reflectionExchanges35And04Frames : Type ℓ
    symmetryCommutesWithDifferential : Type ℓ
    transportedOrientationCompatibility : Type ℓ

record ReferenceQuadraticDefectExperiment {ℓ : Level}
  (Collar : EnhancedPhysicalCollarSpecification {ℓ})
  (Defects : ShortReesSupportedDefectCertificate {ℓ})
  (Duality : FullConductorTwoGradeDualityCertificate {ℓ})
  (EndpointClasses : SupportedEndpointClassCertificate {ℓ})
  (Tangential : TangentialDualityScalarPairingCertificate {ℓ})
  (EndpointPullback : PhysicalEndpointPullbackCertificate {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    ReferenceQuadraticSource TargetHomComplex : Type ℓ
    referenceQuadraticSource : ReferenceQuadraticSource
    targetHomComplex : TargetHomComplex
    CandidateMap : Type ℓ
    candidate : CandidateMap

    candidateIsClosed : Type ℓ
    sourceRelationColumnsRetained : Type ℓ
    nonzeroGenuineQComponent : Type ℓ
    bothEndpointBoundariesRetained : Type ℓ
    endpointBoundariesHaveCollarHomotopies : Type ℓ
    localPuncturedDualRetained : Type ℓ
    fullNonsplitRelativeDualizingTargetRetained : Type ℓ
    scalarAndOccurrenceTraceGradesRetained : Type ℓ
    primitiveDualizingConnectingMorphismRetained : Type ℓ
    supportedEndpointNullClassesNotPromotedToPhysicalConnectors : Type ℓ
    primitiveGenericSupportedClassRetained : Type ℓ
    scalarTangentialReadoutDoesNotReplaceTwoGradeTarget : Type ℓ
    sameTargetPrimitiveEndpointPullbackIsNotUsed : Type ℓ
    eulerEvaluatedEndpointComparisonIsNotUsed : Type ℓ
    endpointRelativeOperationKernelIsRetained : Type ℓ
    primaryCoordinateIsUnit : Type ℓ
    reciprocalECoordinateIsUnit : Type ℓ
    reciprocalRCoordinateIsZero : Type ℓ
    reflectionTransportProducesConjugateQuadraticMap : Type ℓ

    -- Negative controls distinguish this experiment from the two known failed
    -- factorizations.
    CandidateFactorsThroughExistingNativeCap : Type ℓ
    doesNotFactorThroughExistingNativeCap :
      CandidateFactorsThroughExistingNativeCap → ⊥
    CandidateUsesOrdinaryUnitNormalizedCollar : Type ℓ
    doesNotUseOrdinaryUnitNormalizedCollar :
      CandidateUsesOrdinaryUnitNormalizedCollar → ⊥

-- Current executable evidence reaches the specification boundary only.
record EnhancedPhysicalCollarConstructionBoundary {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    KnownCoefficientCollar : Type ℓ
    knownCoefficientCollar : KnownCoefficientCollar
    eightyFourFlagAuditPasses : Type ℓ
    principalLineRepairPasses : Type ℓ
    MissingNormalCechEndpointQDifferential : Type ℓ
    missingChainTarget : MissingNormalCechEndpointQDifferential
    reflectedConormalButterflyBoundary :
      ReflectedConormalButterflyConstructionBoundary {ℓ}
    reducedRoadBaseNullCandidate : ReducedRoadBaseNullCandidate {ℓ}
    augmentedResidueSelectionGate :
      AugmentedResidueSelectionGate reducedRoadBaseNullCandidate
    physicalEndpointPullback : PhysicalEndpointPullbackCertificate {ℓ}
    endpointComparisonDeformationFibre :
      EndpointComparisonDeformationFibre physicalEndpointPullback
    noReferenceHomBeforeTargetDifferential : Type ℓ
