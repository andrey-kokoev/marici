{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidMarkedGalleryToricDescent where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record MarkedGalleryToricDescentCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    Facet35 MarkedD03Gallery LocalizedSlopeTransfer : Type ℓ
    supportTransfer : Facet35 → MarkedD03Gallery
    requiresTwoNativeSlopeInverses : Type ℓ
    polynomialDoubleSlopeRegularization : Type ℓ
    primitiveFourStateMiddleVertexSymbol : Type ℓ

    EndpointPacket EndpointCompleteTransfer : Type ℓ
    endpointCompleteTransfer : EndpointCompleteTransfer
    identityOnThirtyTwoEndpointStates : Type ℓ
    nonzeroOffDiagonalEndpointComparison : Type ℓ
    invariantComparisonImageHasRankOne : Type ℓ
    nonzeroImageChangesEndpointFraming : Type ℓ

    GalleryCostalk OppositeEdgeCostalk : Type ℓ
    markedGalleryCostalkRankThree : Type ℓ
    markedGalleryPrimaryIsZero : Type ℓ
    oppositeEdgePrimaryRankOnePrimitive : Type ℓ
    deletingD25CreatesChainDefect : Type ℓ
    physicalReflectionExchanges35And04Targets : Type ℓ

    NativeOccurrenceExcess PrimaryCarryingMap ZeroPrimaryExcessMap : Type ℓ
    RelationOnlyExcessMap : Type ℓ
    nativeOccurrenceExcess : NativeOccurrenceExcess
    primaryCarryingMap : PrimaryCarryingMap
    zeroPrimaryExcessMap : ZeroPrimaryExcessMap
    relationOnlyExcessMap : RelationOnlyExcessMap
    literalBetaPrimaryPlusExcessDecomposition : Type ℓ
    localCostalkIsThreeFreeRegulatorLines : Type ℓ
    originalMapHasPrimaryExcessCoordinatesOneOneZero : Type ℓ
    primitiveExcessNonvanishing : Type ℓ
    primaryProjectionDeletesNonzeroExcess : Type ℓ
    relationOnlyExcessRequiresSourceRelationColumns : Type ℓ
    cartierPreservesNativeOccurrenceExcessDecomposition : Type ℓ
    saturatedRankThreeCartierImage : Type ℓ
    oppositeEndpointConnectingEquationRetained : Type ℓ
    physicalReflectionPreservesExcessDecomposition : Type ℓ

    NativeNormalizationExcessPullback AsymmetricSheetExcessPackets : Type ℓ
    nativeNormalizationExcessPullback : NativeNormalizationExcessPullback
    asymmetricSheetExcessPackets : AsymmetricSheetExcessPackets
    fourteenPrimitiveConductorAttachments : Type ℓ
    sixPrimitiveFirstConormalChannels : Type ℓ
    eightHigherWedgeShortReesDefects : Type ℓ
    selectedExcessGeneratorHasCoefficientOne : Type ℓ
    centralShortReesImageHasExactlySixChannels : Type ℓ
    noOrdinaryDegreeZeroNativeToSelectedSourceMap : Type ℓ

    ReciprocalNativePairing ClosedBasepointTrace : Type ℓ
    reciprocalNativePairing : ReciprocalNativePairing
    reciprocalCurryingIsChainIsomorphism : Type ℓ
    closedBasepointTrace : ClosedBasepointTrace
    traceDetectsZeroPrimaryExcessAndRelationClasses : Type ℓ
    primaryAndTraceDetectAllThreeLocalCoordinates : Type ℓ
    originalMapHasTraceCoordinatesOneZero : Type ℓ
    collapsedMapHasZeroReciprocalTrace : Type ℓ
    primitiveMixedRelationTraceClass : Type ℓ
    reciprocalTraceSurvivesCartierAsSaturatedRankTwo : Type ℓ

    ReesModification RelativeJacobian ResidualCartierLine : Type ℓ
    sixChartBlowupModification : ReesModification
    pairProductIdealIsRelativeJacobian : Type ℓ
    relativeJacobianIsInvertible : Type ℓ
    residualCartierLine : ResidualCartierLine

    CartierComparison GenericCap EndpointDifference : Type ℓ
    cartierComparison : CartierComparison
    lowerGenericCap : GenericCap
    upperSixTermEndpointDifference : EndpointDifference
    primitiveCorrectedGenericClassOnAllCharts : Type ℓ
    centralLowerMapIsZero : Type ℓ
    centralUpperEndpointMapSurvives : Type ℓ
    fullShortReesAttachmentTriangleSurvives : Type ℓ
    endpointQuotientReesModuleHasRankSixteen : Type ℓ
    endpointProductDivisorCechModels : Type ℓ
    sevenTermEndpointBoundaryWitness : Type ℓ
    primitiveCentralFullyMarkedEndpointContinuation : Type ℓ
    threePresentationsThreePairHomotopiesTripleCoherence : Type ℓ

    LongExcessBundle ShortExcess : Type ℓ
    nontrivialRankTwoLongExcess : LongExcessBundle
    primitiveTopExcessProperTrace : Type ℓ
    deletingLongExcessMakesTraceZero : Type ℓ
    independentShortExcess : ShortExcess
    longExcessNotIdentifiedWithShortExcess : Type ℓ

    CompletedNormalDual ModifiedCompletedDual : Type ℓ
    completedNormalDual : CompletedNormalDual
    modifiedCompletedDual : ModifiedCompletedDual
    quasiCoherentDerivedLimitRequired : Type ℓ
    properTraceIsEquivalence : Type ℓ
    completedDescentPreservesAllSupportTriangles : Type ℓ
    completedDescentPreservesBothEndpoints : Type ℓ
    completedDescentPreservesQuadraticCubicCoupling : Type ℓ
    fourCentralGenericDualLines : Type ℓ
    noCentralFirstDerivedLimitTerm : Type ℓ
    completedNormalizedReverseTraceStillZeroCentrally : Type ℓ
    naiveChartwisePowerSeriesPullbackIsFalse : Type ℓ

    PhysicalSupportedVerdierIdentification : Type ℓ
    PhysicalCollarFrameIdentification : Type ℓ
    PhysicalReflectionParity : Type ℓ
