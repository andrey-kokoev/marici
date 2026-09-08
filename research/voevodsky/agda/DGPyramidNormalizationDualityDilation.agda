{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidNormalizationDualityDilation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record DerivedNormalizationKernelCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    AuxiliaryKernel NativeKernel DerivedBaseChangedKernel : Type ℓ
    derivedBaseChangedKernel : DerivedBaseChangedKernel
    compareTotalKernel : DerivedBaseChangedKernel → NativeKernel
    totalKernelComparisonIsEquivalence : Type ℓ
    totalKernelComparisonKernelIsContractible : Type ℓ
    contractionIsIntegralAndEquivariant : Type ℓ

    RowFilteredKernel FiltrationReesDefect : Type ℓ
    rowFilteredKernel : RowFilteredKernel
    contractionDoesNotPreserveRowFiltration : Type ℓ
    filteredKernelComparisonIsNotEquivalence : Type ℓ
    filtrationReesDefect : FiltrationReesDefect
    reesDefectIsKilledExactlyByBookkeepingParameter : Type ℓ
    bookkeepingParameterIsNotPhysicalReesTime : Type ℓ

    RelativeNormalizationQuotient EndpointRoadObject UnboundedRelativeFibre : Type ℓ
    relativeNormalizationQuotient : RelativeNormalizationQuotient
    endpointRoadObject : EndpointRoadObject
    unboundedRelativeFibre : UnboundedRelativeFibre
    relativeQuotientRetainsUnboundedFibre : Type ℓ
    endpointRoadObjectRetainsShiftedUnboundedFibre : Type ℓ
    scalarUnitPassesButCoefficientLinearSectionDoesNotExist : Type ℓ

record FullConductorTwoGradeDualityCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    ScalarGrade OccurrenceConormalGrade ReciprocalTrace : Type ℓ
    nuE nuR : ReciprocalTrace
    scalarGrade : ScalarGrade
    occurrenceConormalGrade : OccurrenceConormalGrade
    twoGradeTraceMatrixIsMinusBetaUpperTriangularUnit : Type ℓ
    traceIsUnimodularAfterFixedNonzeroBetaNormalization : Type ℓ
    noBetaDivisionAtRegulatorZero : Type ℓ
    scalarProjectionIdentifiesNuEAndNuR : Type ℓ
    occurrenceGradeDistinguishesNuEAndNuR : Type ℓ
    relationOnlyClassDescendsToFirstNormalColumn : Type ℓ

    RelativeDualizingComplex FullConductorSupportedDual Residue : Type ℓ
    relativeDualizingComplex : RelativeDualizingComplex
    twoSheetCanonicalModulesInDegreeMinusThree : Type ℓ
    conductorModuleInDegreeMinusOne : Type ℓ
    primitiveNonsplitConnectingMorphism : Type ℓ
    notSingleOrientationLine : Type ℓ
    notDirectSumOfCohomologyModules : Type ℓ
    fullConductorSupportedDual : FullConductorSupportedDual
    residue : Residue
    residueUsesAmbientLocalCohomologyNotMixedFractions : Type ℓ
    bothFullSupportedTraceClassesRemainIndependent : Type ℓ
    fiveResolvedReadingsDetectBothTracesAndRelation : Type ℓ
    dualizedTraceChangesSourceToRelativeDual : Type ℓ

record SeparatedCoefficientDilationCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    SourceRing IndependentTargetRing DerivedIncidence : Type ℓ
    sourceRing : SourceRing
    independentTargetRing : IndependentTargetRing
    derivedIncidence : DerivedIncidence
    noOrdinaryRingMapWithIndependentDilationFormulas : Type ℓ
    derivedBaseChangeUsesAmbientPolynomialRing : Type ℓ
    incidenceSupportedOnTwoAxesAndIntersection : Type ℓ
    twoTraceClassesFormIntersectionSupportedRankTwoModule : Type ℓ
    endpointConnectingEquationsRetained : Type ℓ

    DiagonalIncidence DiagonalExcess : Type ℓ
    diagonalIncidence : DiagonalIncidence
    diagonalDilationIsNonflat : Type ℓ
    diagonalCreatesClosedExcessGenerator : DiagonalExcess
    diagonalDerivedTermsMustBeRetained : Type ℓ
    genericMixedDilationChartIsEmptyAfterSaturation : Type ℓ
    dilationDoesNotConstructPhysicalGenericTrace : Type ℓ
