{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidAllDegreeEndpointTangential where

open import Cubical.Foundations.Prelude

record AllDegreeConductorComparisonCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    SpectatorRing AuxiliaryConductor NativeConductor : Type ℓ
    DerivedSelfIntersectionComparison : Type ℓ
    comparison : DerivedSelfIntersectionComparison
    comparisonFactorsThroughSixOccurrencePolynomialAlgebra : Type ℓ
    comparisonIsNotTotalNormalizationKernelComparison : Type ℓ
    auxiliaryAndNativeResolutionsAreUnbounded : Type ℓ
    imageIsSixOccurrenceExteriorCoalgebra : Type ℓ
    imageVanishesAboveDegreeSix : Type ℓ
    imageInclusionHasIntegralUnitPivots : Type ℓ

    NativeYoneda AuxiliaryYoneda RestrictionKernel : Type ℓ
    nativeYoneda : NativeYoneda
    auxiliaryYoneda : AuxiliaryYoneda
    restrictionKernel : RestrictionKernel
    restrictionKernelIsTwoSidedIdealOfNineMixedAnticommutators : Type ℓ
    allHigherOperationFailuresAreGeneratedInDegreeTwo : Type ℓ
    mixedAnticommutatorDefectsAreNotNilpotent : Type ℓ
    comparisonConeIsCoefficientSpaceNotPhysicalStateSpace : Type ℓ

    EndpointComparisonFibre : Type ℓ
    endpointComparisonFibre : EndpointComparisonFibre
    endpointFibreContainsFreeCoefficientRetract : Type ℓ
    uniformNonzeroTensorCannotRepairFixedEndpointComparison : Type ℓ
    uniformNonzeroCoefficientDualCannotRepairFixedEndpointComparison : Type ℓ
    rowDependentOrGradedDiagramChangeRemainsOpen : Type ℓ

record SupportedEndpointClassCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    SupportedInput FullTarget EndpointSupport ShortBoundary GenericQuotient : Type ℓ
    EightSupportedMaps : Type ℓ
    eightSupportedMaps : EightSupportedMaps
    endpointCompositesAreNullhomotopic : Type ℓ
    endpointNullhomotopiesHavePairAndTripleCoherences : Type ℓ
    endpointAndShortBoundaryMappingComplexesAreAcyclic : Type ℓ
    restrictionToEndpointAndGenericQuotientsIsQuasiIsomorphism : Type ℓ
    fixedEntireGenericClassHasContractibleCompatibleLiftSpace : Type ℓ
    closedCapsPreserveGenericProjection : Type ℓ
    genericClassesArePrimitiveAndNonzero : Type ℓ
    genericClassesRequireCompleteSevenEquationKoszulInput : Type ℓ
    genericClassesDoNotGiveOrdinaryRawSourceLifts : Type ℓ
    endpointCoefficientEntriesDoNotDefineNonzeroEndpointClasses : Type ℓ
    extraClassIsExteriorChoiceNotParityOrArithmeticUnit : Type ℓ
    noPhysicalCollarIdentificationOrReflectionParity : Type ℓ

record TangentialDualityScalarPairingCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    IntervalTraceTarget RelativeIntervalQuotient RelativeDualizingComplex : Type ℓ
    TangentialComparison : Type ℓ
    tangentialComparison : TangentialComparison
    comparisonFactorsThroughRelativeIntervalQuotient : Type ℓ
    comparisonTargetsCompleteNonsplitRelativeDualizingComplex : Type ℓ
    chainRepresentativeRequiresTwoEssentialDualizingEntries : Type ℓ
    deletingConormalCorrectionBreaksChainEquation : Type ℓ
    comparisonIsPolynomialWithoutBetaInverse : Type ℓ
    unitNormalizationRequiresNonzeroBeta : Type ℓ
    relativeComparisonVanishesOnBothEndpointPackets : Type ℓ

    ReciprocalTrace : Type ℓ
    nuE nuR : ReciprocalTrace
    bothScalarPairingsEqualMinusBeta : Type ℓ
    allOrdinaryCoefficientLinearTangentialMapsKillTraceDifference : Type ℓ
    traceDifferenceRemainsNonzeroInTwoGradeTraceGroup : Type ℓ
    scalarBlindnessDoesNotContradictBiduality : Type ℓ
    nonrelativeTangentialGeneratorsHaveEndpointRestrictions : Type ℓ
    coefficientComparisonIsNotPhysicalTangentialOperation : Type ℓ
    physicalComparisonMustRetainTwoGradesOrDualizedRelationMap : Type ℓ
