{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidPhysicalEndpointPullback where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import DGPyramidHigherCoherenceHom

record PhysicalEndpointPullbackCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    BareQSource FullTarget EndpointTarget BareQ : Type ℓ
    fixedPrimitiveBareQClass : Type ℓ
    coefficientLiftSpaceAtFixedWholeGenericClassIsContractible : Type ℓ
    coefficientEndpointCompositesAreExact : Type ℓ

    UnframedThreeNormalSource FramedEndpointGysinSource : Type ℓ
    unframedSourceHasNoEndpointClassInPrescribedFrame : Type ℓ
    unframedSourceRetainsGenericDegreeFourLine : Type ℓ
    framedSourceHasPrimitiveEndpointLine : Type ℓ
    framedSourceHasNoGenericDegreeFourClass : Type ℓ
    productCartierGeneratorIsRetained : Type ℓ
    endpointConormalDeterminantIsRetained : Type ℓ

    LineRetainingCounit EulerEvaluatedComparison : Type ℓ
    lineRetainingCounit : LineRetainingCounit
    eulerEvaluatedComparison : EulerEvaluatedComparison
    eulerEvaluatedComparisonIsNullhomotopic : Type ℓ
    genuineGysinTransitionCannotUseEulerEvaluatedOrdinaryMap : Type ℓ

    PrimitivePlusEndpointClass PrimitiveMinusEndpointClass : Type ℓ
    primitivePlusEndpointClass : PrimitivePlusEndpointClass
    primitiveMinusEndpointClass : PrimitiveMinusEndpointClass
    SameTargetCandidatePullback : Type ℓ
    sameTargetCandidatePullbackIsEmpty : SameTargetCandidatePullback → ⊥
    sameTargetObstructionIsIntegralPairOneOne : Type ℓ

    NativePlusEndpointModule NativeMinusEndpointModule : Type ℓ
    nineQuadraticActionsNonzeroOnEachEndpoint : Type ℓ
    augmentationUnitCannotMapEquivariantlyToEndpointUnit : Type ℓ
    endpointModuleCanProjectEquivariantlyToGenericAugmentation : Type ℓ
    relativeOperationKernelAndItsOrbitsMustBeRetained : Type ℓ
    decomposableDihedralCorrectionsMustBeRetained : Type ℓ

    NativeSupportedBarSource PhysicalBivariantComparison : Type ℓ
    nativeSupportedBarSource : NativeSupportedBarSource
    physicalBivariantComparisonRemainsUnconstructed : Type ℓ
    noPhysicalReflectionParityAssigned : Type ℓ

-- The actual fixed-structure deformation problem is a fibre of totalized
-- Hom complexes, including endpoint, Cech, normal, group, and operation-bar
-- directions.  It is not just the Hom complex of one source and one target.
record EndpointComparisonDeformationFibre {ℓ : Level}
  (Endpoint : PhysicalEndpointPullbackCertificate {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    CoefficientDeformations PhysicalDeformations ComparisonDeformations :
      HigherCoherenceHomComplex {ℓ}
    FibreComplex : HigherCoherenceHomComplex {ℓ}

    CoefficientToComparison PhysicalToComparison : Type ℓ
    coefficientToComparison : CoefficientToComparison
    physicalToComparison : PhysicalToComparison
    fibreModelsDifferenceMap : Type ℓ
    comparisonIncludesBothEndpoints : Type ℓ
    comparisonIncludesCechTotalization : Type ℓ
    comparisonIncludesNormalSpecializationCube : Type ℓ
    comparisonIncludesDihedralGroupCochains : Type ℓ
    comparisonIncludesRelativeOperationBarComplex : Type ℓ

    AffineDiscrepancy ObstructionH1 ComponentTorsorH0 : Type ℓ
    affineDiscrepancy : AffineDiscrepancy
    obstructionH1 : ObstructionH1
    componentTorsorH0 : ComponentTorsorH0
    existenceIffConnectingObstructionVanishes : Type ℓ
    inhabitedComponentsFormH0Torsor : Type ℓ
    higherAutomorphismsAreNegativeFibreCohomology : Type ℓ
    classificationAssumesFixedModuleAndActionStructures : Type ℓ

record PhysicalEndpointComparisonGate {ℓ : Level}
  (Endpoint : PhysicalEndpointPullbackCertificate {ℓ})
  (Fibre : EndpointComparisonDeformationFibre Endpoint)
  : Type (ℓ-suc ℓ) where
  field
    ComparisonPathDiagram : Type ℓ
    OperationCompatibleBivariantMap : Type ℓ
    comparisonPathDiagram : ComparisonPathDiagram
    operationCompatibleBivariantMap : OperationCompatibleBivariantMap
    primitiveEndpointClassesLiftFromRelativeKernel : Type ℓ
    eighteenQuadraticEndpointClassesAccountedFor : Type ℓ
    bareQClassRemainsSeparateComponent : Type ℓ
    endpointAndGenericSourcesAreNotIdentified : Type ℓ
    allBarCechNormalGroupCoherencesClose : Type ℓ
