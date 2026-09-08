{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidMixedVarianceMate where

open import Cubical.Foundations.Prelude hiding (J)
open import DGPyramidBoundary
open import DGPyramidFiller
open import DGPyramidPartialMariciAdapter
open import DGPyramidEnhancedPhysicalCollar

-- Exact acceptance contract for the still-missing physical mate. Predicates
-- are declared before a candidate is selected, so a packet cannot define
-- compatibility retrospectively to accept its chosen map.
record PhysicalMixedVarianceMateSpecification {ℓ : Level}
  {P : DGPyramidBoundary {ℓ}} (Partial : PartialMariciPacket P)
  : Type (ℓ-suc ℓ) where
  field
    Mate : Type ℓ

    -- 1. The mate is based on the computed ordinary source equivalence.
    SourceEquivalenceCompatibility : Mate → Type ℓ

    -- 2–3. Both carrier collars are identified with physical endpoint cells.
    PositiveEndpointCompatibility : Mate → Type ℓ
    NegativeEndpointCompatibility : Mate → Type ℓ

    -- 4. It respects the genuine full Q quotient and selected contraction.
    FullQCompatibility : Mate → Type ℓ

    -- 5. It carries the corrected Morse disk with its fixed boundary.
    MorseDiskCompatibility : Mate → Type ℓ

    -- 6. It places the marked-normal top class omega in the correct fine
    -- sector, without coercing it to the unit-degree roof.
    MarkedNormalCompatibility : Mate → Type ℓ

    -- Continuation through the short-normal cube is source-defined. In
    -- particular, neither terminal contractibility nor a chosen branch may be
    -- substituted for this data.
    NormalCubeCompatibility : Mate → Type ℓ
    ExternalTorPlacement : Mate → Type ℓ
    EndpointNormalizationCompatibility : Mate → Type ℓ
    BranchReflectionTransport : Mate → Type ℓ

    -- Rees-weighted filling variation and both annihilating homotopies are
    -- transported pointwise, including the secondary theta03 obstruction and
    -- the nonzero endpoint terms above the bottom cycle.
    ReesResonanceCompatibility : Mate → Type ℓ
    PointwiseLowerCorrectionCompatibility : Mate → Type ℓ
    Omega03Admissibility : Mate → Type ℓ
    AnnihilatorHomotopyCompatibility : Mate → Type ℓ
    Theta03Compatibility : Mate → Type ℓ

    -- 7. It carries omega's nonzero lower-support transgression b.
    SupportAttachmentCompatibility : Mate → Type ℓ

    -- 8. Variance reversal agrees with the Cartier/Rees/Koszul comparison.
    CartierReesDualityCompatibility : Mate → Type ℓ

    -- The word "mate" is justified by derived tensor-Hom/support-duality
    -- adjunctions, including the opposite-algebra and Koszul symmetry signs.
    TensorHomAdjunctionCompatibility : Mate → Type ℓ
    SupportedDualMateCompatibility : Mate → Type ℓ
    OppositeDGAlgebraCompatibility : Mate → Type ℓ
    KoszulSymmetrySignCompatibility : Mate → Type ℓ
    PrincipalLineFactorizationCompatibility : Mate → Type ℓ
    OrderedRegularPurityCompatibility : Mate → Type ℓ
    CommonReesFrameCompatibility : Mate → Type ℓ
    PrimitiveExcessPreservation : Mate → Type ℓ
    DualTransgressionRealization : Mate → Type ℓ
    FixedPhysicalTripleCompatibility : Mate → Type ℓ
    FirstNormalSymbolCompatibility : Mate → Type ℓ
    NativeOccurrence35Separation : Mate → Type ℓ
    PointwiseEndpointCompatibility : Mate → Type ℓ
    UpperAnnihilatorGradePreservation : Mate → Type ℓ
    UpperShriekAdjunctionCompatibility : Mate → Type ℓ
    IteratedPurityDeterminantCompatibility : Mate → Type ℓ
    SignedTensorHomCurryingCompatibility : Mate → Type ℓ
    SupportTriangleDualReversalCompatibility : Mate → Type ℓ
    KFlatBaseChangeCompatibility : Mate → Type ℓ
    FirstSymbolFunctorialityCompatibility : Mate → Type ℓ
    StrictSummandPreservation : Mate → Type ℓ
    SupportedReesResidueCompatibility : Mate → Type ℓ
    GysinValuedReversePairingCompatibility : Mate → Type ℓ
    OrbitSupportedQCompatibility : Mate → Type ℓ
    NativeOrbitAuthorizationCompatibility : Mate → Type ℓ
    BetaFamilyCompatibility : Mate → Type ℓ
    BetaZeroEndpointCompatibility : Mate → Type ℓ
    FirstInfinitesimalCompatibility : Mate → Type ℓ
    NonfactorizingGenericRealization : Mate → Type ℓ
    ComplementarySupportCompatibility : Mate → Type ℓ
    GenuineRelativeQuotientCompatibility : Mate → Type ℓ
    SupportedCohomologicalRealization : Mate → Type ℓ
    LocalizationConnectingCompatibility : Mate → Type ℓ
    NestedSupportTransitivityCompatibility : Mate → Type ℓ
    RegulatorVertexFramingCompatibility : Mate → Type ℓ
    SourceAssemblyLocalityCompatibility : Mate → Type ℓ
    UnionCounitConeCompatibility : Mate → Type ℓ
    OrdinaryEndpointCompatibility : Mate → Type ℓ
    StrictEndpointCompatibility : Mate → Type ℓ
    HomotopyCoherentEndpointCompatibility : Mate → Type ℓ
    LowerCochainPreservation : Mate → Type ℓ
    NormalizationSheetToCubicalKernel : Mate → Type ℓ
    CrossFrameEndpointCompatibility : Mate → Type ℓ
    RingedVerdierIdentification : Mate → Type ℓ
    PhysicalReflectionParity : Mate → Type ℓ
    GenuineUnionRecollementCompatibility : Mate → Type ℓ
    SourceConductorDegreeSelection : Mate → Type ℓ
    FramedPrimarySelection : Mate → Type ℓ
    CoherentEndpointQFrameCompatibility : Mate → Type ℓ
    FunctorialRecollementCompatibility : Mate → Type ℓ
    MayerVietorisAssemblyCompatibility : Mate → Type ℓ
    ResidualOccurrenceSupportCompatibility : Mate → Type ℓ
    OccurrenceGysinCompatibility : Mate → Type ℓ
    CoefficientSystemCapCompatibility : Mate → Type ℓ
    DescentTorsorCompatibility : Mate → Type ℓ
    TwelveResidueCoordinateCompatibility : Mate → Type ℓ
    FirstConductorPrimaryHomotopySelection : Mate → Type ℓ
    PhysicalTCellCorrespondence : Mate → Type ℓ
    EndpointCompleteSupportedDualCorrespondence : Mate → Type ℓ
    CompleteChainValuedConductorSymbol : Mate → Type ℓ
    QuadraticConductorCompatibility : Mate → Type ℓ
    ConductorDihedralTransportCompatibility : Mate → Type ℓ
    IntegralInvariantConductorChoice : Mate → Type ℓ
    PhysicalRowwiseConductorRestriction : Mate → Type ℓ
    FourChannelConductorReconstruction : Mate → Type ℓ
    FaceRankHomotopyDegreeIdentification : Mate → Type ℓ
    EndpointReverseConeCompatibility : Mate → Type ℓ
    SourceRelationMapCompatibility : Mate → Type ℓ
    JointSheetHomotopyCompatibility : Mate → Type ℓ
    SixOccurrenceDeterminantCompatibility : Mate → Type ℓ
    PrimitiveSixfoldResiduePairing : Mate → Type ℓ
    NoFivefoldNodeEndpointPromotion : Mate → Type ℓ
    NativeTripleGysinCompatibility : Mate → Type ℓ
    NativeAttachmentNonSplitCompatibility : Mate → Type ℓ
    NoPrimitiveConductorSection : Mate → Type ℓ
    WeightedCollarCoefficientCompatibility : Mate → Type ℓ
    RawCollarConductorVanishing : Mate → Type ℓ
    ResolvedIdealSourceDescent : Mate → Type ℓ
    RelationOnlyComparisonCompatibility : Mate → Type ℓ
    GlobalDerivedEndpointAttachmentCompatibility : Mate → Type ℓ
    SupportedEndpointGysinCompatibility : Mate → Type ℓ
    SupportedLiftTorsorSelection : Mate → Type ℓ
    LocalPrimitiveDescentCompatibility : Mate → Type ℓ
    PhysicalSideEdgeComposition : Mate → Type ℓ
    TStemBoundaryMultiplierCoherence : Mate → Type ℓ
    MixedAndSameSheetStemDistinction : Mate → Type ℓ
    IntrinsicConductorTowerCompatibility : Mate → Type ℓ
    AmbientIntrinsicFibreDistinction : Mate → Type ℓ
    IntrinsicFibreGlobalAttachmentLimitation : Mate → Type ℓ
    FaceRankIsNotCompleteHomotopyDegree : Mate → Type ℓ
    NativeShortFaceComparison : Mate → Type ℓ
    JointComplementaryFaceCapCompatibility : Mate → Type ℓ
    JointGenericEndpointDiagonalCompatibility : Mate → Type ℓ
    ConstantSpatialCochainCompatibility : Mate → Type ℓ
    NormalizationSheetExtensionObstructionCompatibility : Mate → Type ℓ
    NativeSpatialThreeExtensionCompatibility : Mate → Type ℓ
    FourteenTriangleCycleCompatibility : Mate → Type ℓ
    EndpointTriangleEssentiality : Mate → Type ℓ
    CoherentNormalizationSheetExtensionSelection : Mate → Type ℓ
    FaceRingNormalLocalizedComparison : Mate → Type ℓ
    IncidentLongStarSelection : Mate → Type ℓ
    TCellLongStarAnticommutation : Mate → Type ℓ
    MixedEdgeAttachmentTransport : Mate → Type ℓ
    LongStarsAsBridgeDifferences : Mate → Type ℓ
    NoCellwiseTCellLongStarBijection : Mate → Type ℓ
    ConductorCostalkCounitCompatibility : Mate → Type ℓ
    CostalkPrimarySelection : Mate → Type ℓ
    GlobalEndpointTransformationCompatibility : Mate → Type ℓ
    EndpointJetObstructionCompatibility : Mate → Type ℓ
    FullConductorSquareCompletionCompatibility : Mate → Type ℓ
    MarkedD03SupportChangingComparison : Mate → Type ℓ
    UnavoidableD25SupportCompatibility : Mate → Type ℓ
    CompletedNormalDualCompatibility : Mate → Type ℓ
    ExactTraceImageIdealCompatibility : Mate → Type ℓ
    QuadraticCubicReesFiltrationCompatibility : Mate → Type ℓ
    ReesFaceVanishingCompatibility : Mate → Type ℓ
    PhysicalSupportedReesGysinLift : Mate → Type ℓ
    MarkedGalleryNormalGraphCompatibility : Mate → Type ℓ
    CompletedToricProperDescentCompatibility : Mate → Type ℓ
    ConductorOperationNaturality : Mate → Type ℓ
    FormalPuncturedTargetCompatibility : Mate → Type ℓ
    PhysicalCollarAndReflectionIdentification : Mate → Type ℓ
    NativeOccurrenceExcessCompatibility : Mate → Type ℓ
    SourceRelationExcessCompatibility : Mate → Type ℓ
    NativeNormalizationExcessCompatibility : Mate → Type ℓ
    HigherWedgeReesDefectCompatibility : Mate → Type ℓ
    PuncturedLocalDualCompatibility : Mate → Type ℓ
    ReciprocalExcessTraceCompatibility : Mate → Type ℓ
    PredictedEnrichedSupportSquareCompatibility : Mate → Type ℓ
    StructuralFalsifierCompatibility : Mate → Type ℓ
    MinimalPredictiveEnvelopeCompatibility : Mate → Type ℓ
    PredictedThreeCoordinateFingerprintCompatibility : Mate → Type ℓ
    NativeUniversalPuncturedOverlapCompatibility : Mate → Type ℓ
    NonsplitOccurrenceExtensionCompatibility : Mate → Type ℓ
    DistinctCoefficientActionCompatibility : Mate → Type ℓ
    CechSupportedReciprocalTraceCompatibility : Mate → Type ℓ
    TwoChartRelationHomotopyCompatibility : Mate → Type ℓ
    OddConductorClassCompatibility : Mate → Type ℓ
    OccurrencePreservingAuxiliaryBridgeCompatibility : Mate → Type ℓ
    QuadraticAuxiliaryNativeDefectCompatibility : Mate → Type ℓ
    ShortReesDivisorIncidenceCompatibility : Mate → Type ℓ
    DirectPhysicalDefectCorrespondence : Mate → Type ℓ
    EnhancedPhysicalCollarTargetCompatibility : Mate → Type ℓ
    ReferenceQuadraticDefectExperimentCompatibility : Mate → Type ℓ
    TotalNormalizationKernelCompatibility : Mate → Type ℓ
    FilteredNormalizationDefectCompatibility : Mate → Type ℓ
    FullConductorTwoGradeDualityCompatibility : Mate → Type ℓ
    SeparatedDilationBoundaryCompatibility : Mate → Type ℓ
    AllDegreeConductorOperationCompatibility : Mate → Type ℓ
    SupportedEndpointClassCompatibility : Mate → Type ℓ
    ScalarTangentialBlindnessCompatibility : Mate → Type ℓ

    -- 9. Rotation, reflection, endpoint swap, and orientation signs cohere.
    DihedralOrientationCompatibility : Mate → Type ℓ
    FineZeroDihedralAttachmentCompatibility : Mate → Type ℓ

    -- 10. The mate identifies the physical q,e,h_M,H_C faces and places the
    -- resulting closed discrepancy in the stated physical frame. This is not
    -- an assertion that the discrepancy has a filler.
    BoundaryCellCompatibility : Mate → Type ℓ
    DiscrepancyFrameCompatibility : Mate → Type ℓ

open PhysicalMixedVarianceMateSpecification public

record PhysicalMixedVarianceMate {ℓ : Level}
  {P : DGPyramidBoundary {ℓ}} {Partial : PartialMariciPacket P}
  (Spec : PhysicalMixedVarianceMateSpecification Partial)
  : Type (ℓ-suc ℓ) where
  field
    mate : Mate Spec
    sourceEquivalenceWitness : SourceEquivalenceCompatibility Spec mate
    positiveEndpointWitness : PositiveEndpointCompatibility Spec mate
    negativeEndpointWitness : NegativeEndpointCompatibility Spec mate
    fullQWitness : FullQCompatibility Spec mate
    morseDiskWitness : MorseDiskCompatibility Spec mate
    markedNormalWitness : MarkedNormalCompatibility Spec mate
    normalCubeWitness : NormalCubeCompatibility Spec mate
    externalTorPlacementWitness : ExternalTorPlacement Spec mate
    endpointNormalizationWitness : EndpointNormalizationCompatibility Spec mate
    branchReflectionWitness : BranchReflectionTransport Spec mate
    reesResonanceWitness : ReesResonanceCompatibility Spec mate
    pointwiseLowerCorrectionWitness :
      PointwiseLowerCorrectionCompatibility Spec mate
    omega03Witness : Omega03Admissibility Spec mate
    annihilatorHomotopyWitness : AnnihilatorHomotopyCompatibility Spec mate
    theta03Witness : Theta03Compatibility Spec mate
    supportAttachmentWitness : SupportAttachmentCompatibility Spec mate
    cartierReesDualityWitness : CartierReesDualityCompatibility Spec mate
    tensorHomAdjunctionWitness : TensorHomAdjunctionCompatibility Spec mate
    supportedDualMateWitness : SupportedDualMateCompatibility Spec mate
    oppositeDGAlgebraWitness : OppositeDGAlgebraCompatibility Spec mate
    koszulSymmetrySignWitness : KoszulSymmetrySignCompatibility Spec mate
    principalLineFactorizationWitness :
      PrincipalLineFactorizationCompatibility Spec mate
    orderedRegularPurityWitness : OrderedRegularPurityCompatibility Spec mate
    commonReesFrameWitness : CommonReesFrameCompatibility Spec mate
    primitiveExcessWitness : PrimitiveExcessPreservation Spec mate
    dualTransgressionWitness : DualTransgressionRealization Spec mate
    fixedPhysicalTripleWitness : FixedPhysicalTripleCompatibility Spec mate
    firstNormalSymbolWitness : FirstNormalSymbolCompatibility Spec mate
    nativeOccurrence35Witness : NativeOccurrence35Separation Spec mate
    pointwiseEndpointWitness : PointwiseEndpointCompatibility Spec mate
    upperAnnihilatorGradeWitness : UpperAnnihilatorGradePreservation Spec mate
    upperShriekAdjunctionWitness : UpperShriekAdjunctionCompatibility Spec mate
    iteratedPurityDeterminantWitness :
      IteratedPurityDeterminantCompatibility Spec mate
    signedTensorHomCurryingWitness :
      SignedTensorHomCurryingCompatibility Spec mate
    supportTriangleDualReversalWitness :
      SupportTriangleDualReversalCompatibility Spec mate
    kFlatBaseChangeWitness : KFlatBaseChangeCompatibility Spec mate
    firstSymbolFunctorialityWitness :
      FirstSymbolFunctorialityCompatibility Spec mate
    strictSummandWitness : StrictSummandPreservation Spec mate
    supportedReesResidueWitness : SupportedReesResidueCompatibility Spec mate
    gysinValuedReversePairingWitness :
      GysinValuedReversePairingCompatibility Spec mate
    orbitSupportedQWitness : OrbitSupportedQCompatibility Spec mate
    nativeOrbitAuthorizationWitness :
      NativeOrbitAuthorizationCompatibility Spec mate
    betaFamilyWitness : BetaFamilyCompatibility Spec mate
    betaZeroEndpointWitness : BetaZeroEndpointCompatibility Spec mate
    firstInfinitesimalWitness : FirstInfinitesimalCompatibility Spec mate
    nonfactorizingGenericWitness : NonfactorizingGenericRealization Spec mate
    complementarySupportWitness : ComplementarySupportCompatibility Spec mate
    genuineRelativeQuotientWitness :
      GenuineRelativeQuotientCompatibility Spec mate
    supportedCohomologicalWitness :
      SupportedCohomologicalRealization Spec mate
    localizationConnectingWitness :
      LocalizationConnectingCompatibility Spec mate
    nestedSupportTransitivityWitness :
      NestedSupportTransitivityCompatibility Spec mate
    regulatorVertexFramingWitness :
      RegulatorVertexFramingCompatibility Spec mate
    sourceAssemblyLocalityWitness :
      SourceAssemblyLocalityCompatibility Spec mate
    unionCounitConeWitness : UnionCounitConeCompatibility Spec mate
    ordinaryEndpointWitness : OrdinaryEndpointCompatibility Spec mate
    strictEndpointWitness : StrictEndpointCompatibility Spec mate
    homotopyCoherentEndpointWitness :
      HomotopyCoherentEndpointCompatibility Spec mate
    lowerCochainWitness : LowerCochainPreservation Spec mate
    normalizationSheetToCubicalKernelWitness :
      NormalizationSheetToCubicalKernel Spec mate
    crossFrameEndpointWitness : CrossFrameEndpointCompatibility Spec mate
    ringedVerdierWitness : RingedVerdierIdentification Spec mate
    physicalReflectionParityWitness : PhysicalReflectionParity Spec mate
    genuineUnionRecollementWitness :
      GenuineUnionRecollementCompatibility Spec mate
    sourceConductorDegreeWitness : SourceConductorDegreeSelection Spec mate
    framedPrimarySelectionWitness : FramedPrimarySelection Spec mate
    coherentEndpointQFrameWitness :
      CoherentEndpointQFrameCompatibility Spec mate
    functorialRecollementWitness :
      FunctorialRecollementCompatibility Spec mate
    mayerVietorisAssemblyWitness :
      MayerVietorisAssemblyCompatibility Spec mate
    residualOccurrenceSupportWitness :
      ResidualOccurrenceSupportCompatibility Spec mate
    occurrenceGysinWitness : OccurrenceGysinCompatibility Spec mate
    coefficientSystemCapWitness : CoefficientSystemCapCompatibility Spec mate
    descentTorsorWitness : DescentTorsorCompatibility Spec mate
    twelveResidueCoordinateWitness :
      TwelveResidueCoordinateCompatibility Spec mate
    firstConductorPrimaryHomotopyWitness :
      FirstConductorPrimaryHomotopySelection Spec mate
    physicalTCellCorrespondenceWitness : PhysicalTCellCorrespondence Spec mate
    endpointCompleteSupportedDualWitness :
      EndpointCompleteSupportedDualCorrespondence Spec mate
    completeChainValuedConductorSymbolWitness :
      CompleteChainValuedConductorSymbol Spec mate
    quadraticConductorWitness : QuadraticConductorCompatibility Spec mate
    conductorDihedralTransportWitness :
      ConductorDihedralTransportCompatibility Spec mate
    integralInvariantConductorChoiceWitness :
      IntegralInvariantConductorChoice Spec mate
    physicalRowwiseConductorRestrictionWitness :
      PhysicalRowwiseConductorRestriction Spec mate
    fourChannelConductorReconstructionWitness :
      FourChannelConductorReconstruction Spec mate
    faceRankHomotopyDegreeWitness :
      FaceRankHomotopyDegreeIdentification Spec mate
    endpointReverseConeWitness : EndpointReverseConeCompatibility Spec mate
    sourceRelationMapWitness : SourceRelationMapCompatibility Spec mate
    jointSheetHomotopyWitness : JointSheetHomotopyCompatibility Spec mate
    sixOccurrenceDeterminantWitness :
      SixOccurrenceDeterminantCompatibility Spec mate
    primitiveSixfoldResidueWitness : PrimitiveSixfoldResiduePairing Spec mate
    noFivefoldNodeEndpointPromotionWitness :
      NoFivefoldNodeEndpointPromotion Spec mate
    nativeTripleGysinWitness : NativeTripleGysinCompatibility Spec mate
    nativeAttachmentNonSplitWitness :
      NativeAttachmentNonSplitCompatibility Spec mate
    noPrimitiveConductorSectionWitness : NoPrimitiveConductorSection Spec mate
    weightedCollarCoefficientWitness :
      WeightedCollarCoefficientCompatibility Spec mate
    rawCollarConductorVanishingWitness : RawCollarConductorVanishing Spec mate
    resolvedIdealSourceDescentWitness : ResolvedIdealSourceDescent Spec mate
    relationOnlyComparisonWitness :
      RelationOnlyComparisonCompatibility Spec mate
    globalDerivedEndpointAttachmentWitness :
      GlobalDerivedEndpointAttachmentCompatibility Spec mate
    supportedEndpointGysinWitness : SupportedEndpointGysinCompatibility Spec mate
    supportedLiftTorsorSelectionWitness : SupportedLiftTorsorSelection Spec mate
    localPrimitiveDescentWitness : LocalPrimitiveDescentCompatibility Spec mate
    physicalSideEdgeCompositionWitness : PhysicalSideEdgeComposition Spec mate
    tStemBoundaryMultiplierWitness : TStemBoundaryMultiplierCoherence Spec mate
    mixedAndSameSheetStemWitness : MixedAndSameSheetStemDistinction Spec mate
    intrinsicConductorTowerWitness : IntrinsicConductorTowerCompatibility Spec mate
    ambientIntrinsicFibreWitness : AmbientIntrinsicFibreDistinction Spec mate
    intrinsicFibreGlobalAttachmentWitness :
      IntrinsicFibreGlobalAttachmentLimitation Spec mate
    faceRankNotCompleteHomotopyDegreeWitness :
      FaceRankIsNotCompleteHomotopyDegree Spec mate
    nativeShortFaceWitness : NativeShortFaceComparison Spec mate
    jointComplementaryFaceCapWitness :
      JointComplementaryFaceCapCompatibility Spec mate
    jointGenericEndpointDiagonalWitness :
      JointGenericEndpointDiagonalCompatibility Spec mate
    constantSpatialCochainWitness : ConstantSpatialCochainCompatibility Spec mate
    normalizationSheetExtensionObstructionWitness :
      NormalizationSheetExtensionObstructionCompatibility Spec mate
    nativeSpatialThreeExtensionWitness :
      NativeSpatialThreeExtensionCompatibility Spec mate
    fourteenTriangleCycleWitness : FourteenTriangleCycleCompatibility Spec mate
    endpointTriangleEssentialityWitness : EndpointTriangleEssentiality Spec mate
    coherentNormalizationSheetExtensionWitness :
      CoherentNormalizationSheetExtensionSelection Spec mate
    faceRingNormalLocalizedWitness : FaceRingNormalLocalizedComparison Spec mate
    incidentLongStarSelectionWitness : IncidentLongStarSelection Spec mate
    tCellLongStarAnticommutationWitness : TCellLongStarAnticommutation Spec mate
    mixedEdgeAttachmentTransportWitness : MixedEdgeAttachmentTransport Spec mate
    longStarsAsBridgeDifferencesWitness : LongStarsAsBridgeDifferences Spec mate
    noCellwiseTCellLongStarBijectionWitness :
      NoCellwiseTCellLongStarBijection Spec mate
    conductorCostalkCounitWitness : ConductorCostalkCounitCompatibility Spec mate
    costalkPrimarySelectionWitness : CostalkPrimarySelection Spec mate
    globalEndpointTransformationWitness :
      GlobalEndpointTransformationCompatibility Spec mate
    endpointJetObstructionWitness : EndpointJetObstructionCompatibility Spec mate
    fullConductorSquareCompletionWitness :
      FullConductorSquareCompletionCompatibility Spec mate
    markedD03SupportChangingWitness : MarkedD03SupportChangingComparison Spec mate
    unavoidableD25SupportWitness : UnavoidableD25SupportCompatibility Spec mate
    completedNormalDualWitness : CompletedNormalDualCompatibility Spec mate
    exactTraceImageIdealWitness : ExactTraceImageIdealCompatibility Spec mate
    quadraticCubicReesFiltrationWitness :
      QuadraticCubicReesFiltrationCompatibility Spec mate
    reesFaceVanishingWitness : ReesFaceVanishingCompatibility Spec mate
    physicalSupportedReesGysinLiftWitness : PhysicalSupportedReesGysinLift Spec mate
    markedGalleryNormalGraphWitness : MarkedGalleryNormalGraphCompatibility Spec mate
    completedToricProperDescentWitness :
      CompletedToricProperDescentCompatibility Spec mate
    conductorOperationNaturalityWitness : ConductorOperationNaturality Spec mate
    formalPuncturedTargetWitness : FormalPuncturedTargetCompatibility Spec mate
    physicalCollarAndReflectionWitness :
      PhysicalCollarAndReflectionIdentification Spec mate
    nativeOccurrenceExcessWitness : NativeOccurrenceExcessCompatibility Spec mate
    sourceRelationExcessWitness : SourceRelationExcessCompatibility Spec mate
    nativeNormalizationExcessWitness :
      NativeNormalizationExcessCompatibility Spec mate
    higherWedgeReesDefectWitness : HigherWedgeReesDefectCompatibility Spec mate
    puncturedLocalDualWitness : PuncturedLocalDualCompatibility Spec mate
    reciprocalExcessTraceWitness : ReciprocalExcessTraceCompatibility Spec mate
    predictedEnrichedSupportSquareWitness :
      PredictedEnrichedSupportSquareCompatibility Spec mate
    structuralFalsifierWitness : StructuralFalsifierCompatibility Spec mate
    minimalPredictiveEnvelopeWitness :
      MinimalPredictiveEnvelopeCompatibility Spec mate
    predictedThreeCoordinateFingerprintWitness :
      PredictedThreeCoordinateFingerprintCompatibility Spec mate
    nativeUniversalPuncturedOverlapWitness :
      NativeUniversalPuncturedOverlapCompatibility Spec mate
    nonsplitOccurrenceExtensionWitness :
      NonsplitOccurrenceExtensionCompatibility Spec mate
    distinctCoefficientActionWitness : DistinctCoefficientActionCompatibility Spec mate
    cechSupportedReciprocalTraceWitness :
      CechSupportedReciprocalTraceCompatibility Spec mate
    twoChartRelationHomotopyWitness :
      TwoChartRelationHomotopyCompatibility Spec mate
    oddConductorClassWitness : OddConductorClassCompatibility Spec mate
    occurrencePreservingAuxiliaryBridgeWitness :
      OccurrencePreservingAuxiliaryBridgeCompatibility Spec mate
    quadraticAuxiliaryNativeDefectWitness :
      QuadraticAuxiliaryNativeDefectCompatibility Spec mate
    shortReesDivisorIncidenceWitness :
      ShortReesDivisorIncidenceCompatibility Spec mate
    directPhysicalDefectWitness : DirectPhysicalDefectCorrespondence Spec mate
    enhancedPhysicalCollarTargetWitness :
      EnhancedPhysicalCollarTargetCompatibility Spec mate
    referenceQuadraticDefectExperimentWitness :
      ReferenceQuadraticDefectExperimentCompatibility Spec mate
    totalNormalizationKernelWitness : TotalNormalizationKernelCompatibility Spec mate
    filteredNormalizationDefectWitness :
      FilteredNormalizationDefectCompatibility Spec mate
    fullConductorTwoGradeDualityWitness :
      FullConductorTwoGradeDualityCompatibility Spec mate
    separatedDilationBoundaryWitness :
      SeparatedDilationBoundaryCompatibility Spec mate
    allDegreeConductorOperationWitness :
      AllDegreeConductorOperationCompatibility Spec mate
    supportedEndpointClassWitness : SupportedEndpointClassCompatibility Spec mate
    scalarTangentialBlindnessWitness :
      ScalarTangentialBlindnessCompatibility Spec mate
    dihedralOrientationWitness : DihedralOrientationCompatibility Spec mate
    fineZeroDihedralAttachmentWitness :
      FineZeroDihedralAttachmentCompatibility Spec mate
    boundaryCellWitness : BoundaryCellCompatibility Spec mate
    discrepancyFrameWitness : DiscrepancyFrameCompatibility Spec mate

open PhysicalMixedVarianceMate public

-- The conjunction is available for downstream auditing without hiding which
-- coherence failed.
PreservesAllMateCoherences : {ℓ : Level}
  {P : DGPyramidBoundary {ℓ}} {Partial : PartialMariciPacket P}
  (Spec : PhysicalMixedVarianceMateSpecification Partial) → Mate Spec → Type ℓ
PreservesAllMateCoherences Spec m =
  Σ (SourceEquivalenceCompatibility Spec m) λ _ →
  Σ (PositiveEndpointCompatibility Spec m) λ _ →
  Σ (NegativeEndpointCompatibility Spec m) λ _ →
  Σ (FullQCompatibility Spec m) λ _ →
  Σ (MorseDiskCompatibility Spec m) λ _ →
  Σ (MarkedNormalCompatibility Spec m) λ _ →
  Σ (NormalCubeCompatibility Spec m) λ _ →
  Σ (ExternalTorPlacement Spec m) λ _ →
  Σ (EndpointNormalizationCompatibility Spec m) λ _ →
  Σ (BranchReflectionTransport Spec m) λ _ →
  Σ (ReesResonanceCompatibility Spec m) λ _ →
  Σ (PointwiseLowerCorrectionCompatibility Spec m) λ _ →
  Σ (Omega03Admissibility Spec m) λ _ →
  Σ (AnnihilatorHomotopyCompatibility Spec m) λ _ →
  Σ (Theta03Compatibility Spec m) λ _ →
  Σ (SupportAttachmentCompatibility Spec m) λ _ →
  Σ (CartierReesDualityCompatibility Spec m) λ _ →
  Σ (TensorHomAdjunctionCompatibility Spec m) λ _ →
  Σ (SupportedDualMateCompatibility Spec m) λ _ →
  Σ (OppositeDGAlgebraCompatibility Spec m) λ _ →
  Σ (KoszulSymmetrySignCompatibility Spec m) λ _ →
  Σ (PrincipalLineFactorizationCompatibility Spec m) λ _ →
  Σ (OrderedRegularPurityCompatibility Spec m) λ _ →
  Σ (CommonReesFrameCompatibility Spec m) λ _ →
  Σ (PrimitiveExcessPreservation Spec m) λ _ →
  Σ (DualTransgressionRealization Spec m) λ _ →
  Σ (FixedPhysicalTripleCompatibility Spec m) λ _ →
  Σ (FirstNormalSymbolCompatibility Spec m) λ _ →
  Σ (NativeOccurrence35Separation Spec m) λ _ →
  Σ (PointwiseEndpointCompatibility Spec m) λ _ →
  Σ (UpperAnnihilatorGradePreservation Spec m) λ _ →
  Σ (UpperShriekAdjunctionCompatibility Spec m) λ _ →
  Σ (IteratedPurityDeterminantCompatibility Spec m) λ _ →
  Σ (SignedTensorHomCurryingCompatibility Spec m) λ _ →
  Σ (SupportTriangleDualReversalCompatibility Spec m) λ _ →
  Σ (KFlatBaseChangeCompatibility Spec m) λ _ →
  Σ (FirstSymbolFunctorialityCompatibility Spec m) λ _ →
  Σ (StrictSummandPreservation Spec m) λ _ →
  Σ (SupportedReesResidueCompatibility Spec m) λ _ →
  Σ (GysinValuedReversePairingCompatibility Spec m) λ _ →
  Σ (OrbitSupportedQCompatibility Spec m) λ _ →
  Σ (NativeOrbitAuthorizationCompatibility Spec m) λ _ →
  Σ (BetaFamilyCompatibility Spec m) λ _ →
  Σ (BetaZeroEndpointCompatibility Spec m) λ _ →
  Σ (FirstInfinitesimalCompatibility Spec m) λ _ →
  Σ (NonfactorizingGenericRealization Spec m) λ _ →
  Σ (ComplementarySupportCompatibility Spec m) λ _ →
  Σ (GenuineRelativeQuotientCompatibility Spec m) λ _ →
  Σ (SupportedCohomologicalRealization Spec m) λ _ →
  Σ (LocalizationConnectingCompatibility Spec m) λ _ →
  Σ (NestedSupportTransitivityCompatibility Spec m) λ _ →
  Σ (RegulatorVertexFramingCompatibility Spec m) λ _ →
  Σ (SourceAssemblyLocalityCompatibility Spec m) λ _ →
  Σ (UnionCounitConeCompatibility Spec m) λ _ →
  Σ (OrdinaryEndpointCompatibility Spec m) λ _ →
  Σ (StrictEndpointCompatibility Spec m) λ _ →
  Σ (HomotopyCoherentEndpointCompatibility Spec m) λ _ →
  Σ (LowerCochainPreservation Spec m) λ _ →
  Σ (NormalizationSheetToCubicalKernel Spec m) λ _ →
  Σ (CrossFrameEndpointCompatibility Spec m) λ _ →
  Σ (RingedVerdierIdentification Spec m) λ _ →
  Σ (PhysicalReflectionParity Spec m) λ _ →
  Σ (GenuineUnionRecollementCompatibility Spec m) λ _ →
  Σ (SourceConductorDegreeSelection Spec m) λ _ →
  Σ (FramedPrimarySelection Spec m) λ _ →
  Σ (CoherentEndpointQFrameCompatibility Spec m) λ _ →
  Σ (FunctorialRecollementCompatibility Spec m) λ _ →
  Σ (MayerVietorisAssemblyCompatibility Spec m) λ _ →
  Σ (ResidualOccurrenceSupportCompatibility Spec m) λ _ →
  Σ (OccurrenceGysinCompatibility Spec m) λ _ →
  Σ (CoefficientSystemCapCompatibility Spec m) λ _ →
  Σ (DescentTorsorCompatibility Spec m) λ _ →
  Σ (TwelveResidueCoordinateCompatibility Spec m) λ _ →
  Σ (FirstConductorPrimaryHomotopySelection Spec m) λ _ →
  Σ (PhysicalTCellCorrespondence Spec m) λ _ →
  Σ (EndpointCompleteSupportedDualCorrespondence Spec m) λ _ →
  Σ (CompleteChainValuedConductorSymbol Spec m) λ _ →
  Σ (QuadraticConductorCompatibility Spec m) λ _ →
  Σ (ConductorDihedralTransportCompatibility Spec m) λ _ →
  Σ (IntegralInvariantConductorChoice Spec m) λ _ →
  Σ (PhysicalRowwiseConductorRestriction Spec m) λ _ →
  Σ (FourChannelConductorReconstruction Spec m) λ _ →
  Σ (FaceRankHomotopyDegreeIdentification Spec m) λ _ →
  Σ (EndpointReverseConeCompatibility Spec m) λ _ →
  Σ (SourceRelationMapCompatibility Spec m) λ _ →
  Σ (JointSheetHomotopyCompatibility Spec m) λ _ →
  Σ (SixOccurrenceDeterminantCompatibility Spec m) λ _ →
  Σ (PrimitiveSixfoldResiduePairing Spec m) λ _ →
  Σ (NoFivefoldNodeEndpointPromotion Spec m) λ _ →
  Σ (NativeTripleGysinCompatibility Spec m) λ _ →
  Σ (NativeAttachmentNonSplitCompatibility Spec m) λ _ →
  Σ (NoPrimitiveConductorSection Spec m) λ _ →
  Σ (WeightedCollarCoefficientCompatibility Spec m) λ _ →
  Σ (RawCollarConductorVanishing Spec m) λ _ →
  Σ (ResolvedIdealSourceDescent Spec m) λ _ →
  Σ (RelationOnlyComparisonCompatibility Spec m) λ _ →
  Σ (GlobalDerivedEndpointAttachmentCompatibility Spec m) λ _ →
  Σ (SupportedEndpointGysinCompatibility Spec m) λ _ →
  Σ (SupportedLiftTorsorSelection Spec m) λ _ →
  Σ (LocalPrimitiveDescentCompatibility Spec m) λ _ →
  Σ (PhysicalSideEdgeComposition Spec m) λ _ →
  Σ (TStemBoundaryMultiplierCoherence Spec m) λ _ →
  Σ (MixedAndSameSheetStemDistinction Spec m) λ _ →
  Σ (IntrinsicConductorTowerCompatibility Spec m) λ _ →
  Σ (AmbientIntrinsicFibreDistinction Spec m) λ _ →
  Σ (IntrinsicFibreGlobalAttachmentLimitation Spec m) λ _ →
  Σ (FaceRankIsNotCompleteHomotopyDegree Spec m) λ _ →
  Σ (NativeShortFaceComparison Spec m) λ _ →
  Σ (JointComplementaryFaceCapCompatibility Spec m) λ _ →
  Σ (JointGenericEndpointDiagonalCompatibility Spec m) λ _ →
  Σ (ConstantSpatialCochainCompatibility Spec m) λ _ →
  Σ (NormalizationSheetExtensionObstructionCompatibility Spec m) λ _ →
  Σ (NativeSpatialThreeExtensionCompatibility Spec m) λ _ →
  Σ (FourteenTriangleCycleCompatibility Spec m) λ _ →
  Σ (EndpointTriangleEssentiality Spec m) λ _ →
  Σ (CoherentNormalizationSheetExtensionSelection Spec m) λ _ →
  Σ (FaceRingNormalLocalizedComparison Spec m) λ _ →
  Σ (IncidentLongStarSelection Spec m) λ _ →
  Σ (TCellLongStarAnticommutation Spec m) λ _ →
  Σ (MixedEdgeAttachmentTransport Spec m) λ _ →
  Σ (LongStarsAsBridgeDifferences Spec m) λ _ →
  Σ (NoCellwiseTCellLongStarBijection Spec m) λ _ →
  Σ (ConductorCostalkCounitCompatibility Spec m) λ _ →
  Σ (CostalkPrimarySelection Spec m) λ _ →
  Σ (GlobalEndpointTransformationCompatibility Spec m) λ _ →
  Σ (EndpointJetObstructionCompatibility Spec m) λ _ →
  Σ (FullConductorSquareCompletionCompatibility Spec m) λ _ →
  Σ (MarkedD03SupportChangingComparison Spec m) λ _ →
  Σ (UnavoidableD25SupportCompatibility Spec m) λ _ →
  Σ (CompletedNormalDualCompatibility Spec m) λ _ →
  Σ (ExactTraceImageIdealCompatibility Spec m) λ _ →
  Σ (QuadraticCubicReesFiltrationCompatibility Spec m) λ _ →
  Σ (ReesFaceVanishingCompatibility Spec m) λ _ →
  Σ (PhysicalSupportedReesGysinLift Spec m) λ _ →
  Σ (MarkedGalleryNormalGraphCompatibility Spec m) λ _ →
  Σ (CompletedToricProperDescentCompatibility Spec m) λ _ →
  Σ (ConductorOperationNaturality Spec m) λ _ →
  Σ (FormalPuncturedTargetCompatibility Spec m) λ _ →
  Σ (PhysicalCollarAndReflectionIdentification Spec m) λ _ →
  Σ (NativeOccurrenceExcessCompatibility Spec m) λ _ →
  Σ (SourceRelationExcessCompatibility Spec m) λ _ →
  Σ (NativeNormalizationExcessCompatibility Spec m) λ _ →
  Σ (HigherWedgeReesDefectCompatibility Spec m) λ _ →
  Σ (PuncturedLocalDualCompatibility Spec m) λ _ →
  Σ (ReciprocalExcessTraceCompatibility Spec m) λ _ →
  Σ (PredictedEnrichedSupportSquareCompatibility Spec m) λ _ →
  Σ (StructuralFalsifierCompatibility Spec m) λ _ →
  Σ (MinimalPredictiveEnvelopeCompatibility Spec m) λ _ →
  Σ (PredictedThreeCoordinateFingerprintCompatibility Spec m) λ _ →
  Σ (NativeUniversalPuncturedOverlapCompatibility Spec m) λ _ →
  Σ (NonsplitOccurrenceExtensionCompatibility Spec m) λ _ →
  Σ (DistinctCoefficientActionCompatibility Spec m) λ _ →
  Σ (CechSupportedReciprocalTraceCompatibility Spec m) λ _ →
  Σ (TwoChartRelationHomotopyCompatibility Spec m) λ _ →
  Σ (OddConductorClassCompatibility Spec m) λ _ →
  Σ (OccurrencePreservingAuxiliaryBridgeCompatibility Spec m) λ _ →
  Σ (QuadraticAuxiliaryNativeDefectCompatibility Spec m) λ _ →
  Σ (ShortReesDivisorIncidenceCompatibility Spec m) λ _ →
  Σ (DirectPhysicalDefectCorrespondence Spec m) λ _ →
  Σ (EnhancedPhysicalCollarTargetCompatibility Spec m) λ _ →
  Σ (ReferenceQuadraticDefectExperimentCompatibility Spec m) λ _ →
  Σ (TotalNormalizationKernelCompatibility Spec m) λ _ →
  Σ (FilteredNormalizationDefectCompatibility Spec m) λ _ →
  Σ (FullConductorTwoGradeDualityCompatibility Spec m) λ _ →
  Σ (SeparatedDilationBoundaryCompatibility Spec m) λ _ →
  Σ (AllDegreeConductorOperationCompatibility Spec m) λ _ →
  Σ (SupportedEndpointClassCompatibility Spec m) λ _ →
  Σ (ScalarTangentialBlindnessCompatibility Spec m) λ _ →
  Σ (DihedralOrientationCompatibility Spec m) λ _ →
  Σ (FineZeroDihedralAttachmentCompatibility Spec m) λ _ →
  Σ (BoundaryCellCompatibility Spec m) λ _ →
      DiscrepancyFrameCompatibility Spec m

mateCoherences : {ℓ : Level}
  {P : DGPyramidBoundary {ℓ}} {Partial : PartialMariciPacket P}
  {Spec : PhysicalMixedVarianceMateSpecification Partial} →
  (candidate : PhysicalMixedVarianceMate Spec) →
  PreservesAllMateCoherences Spec (mate candidate)
mateCoherences candidate =
  sourceEquivalenceWitness candidate ,
  positiveEndpointWitness candidate ,
  negativeEndpointWitness candidate ,
  fullQWitness candidate ,
  morseDiskWitness candidate ,
  markedNormalWitness candidate ,
  normalCubeWitness candidate ,
  externalTorPlacementWitness candidate ,
  endpointNormalizationWitness candidate ,
  branchReflectionWitness candidate ,
  reesResonanceWitness candidate ,
  pointwiseLowerCorrectionWitness candidate ,
  omega03Witness candidate ,
  annihilatorHomotopyWitness candidate ,
  theta03Witness candidate ,
  supportAttachmentWitness candidate ,
  cartierReesDualityWitness candidate ,
  tensorHomAdjunctionWitness candidate ,
  supportedDualMateWitness candidate ,
  oppositeDGAlgebraWitness candidate ,
  koszulSymmetrySignWitness candidate ,
  principalLineFactorizationWitness candidate ,
  orderedRegularPurityWitness candidate ,
  commonReesFrameWitness candidate ,
  primitiveExcessWitness candidate ,
  dualTransgressionWitness candidate ,
  fixedPhysicalTripleWitness candidate ,
  firstNormalSymbolWitness candidate ,
  nativeOccurrence35Witness candidate ,
  pointwiseEndpointWitness candidate ,
  upperAnnihilatorGradeWitness candidate ,
  upperShriekAdjunctionWitness candidate ,
  iteratedPurityDeterminantWitness candidate ,
  signedTensorHomCurryingWitness candidate ,
  supportTriangleDualReversalWitness candidate ,
  kFlatBaseChangeWitness candidate ,
  firstSymbolFunctorialityWitness candidate ,
  strictSummandWitness candidate ,
  supportedReesResidueWitness candidate ,
  gysinValuedReversePairingWitness candidate ,
  orbitSupportedQWitness candidate ,
  nativeOrbitAuthorizationWitness candidate ,
  betaFamilyWitness candidate ,
  betaZeroEndpointWitness candidate ,
  firstInfinitesimalWitness candidate ,
  nonfactorizingGenericWitness candidate ,
  complementarySupportWitness candidate ,
  genuineRelativeQuotientWitness candidate ,
  supportedCohomologicalWitness candidate ,
  localizationConnectingWitness candidate ,
  nestedSupportTransitivityWitness candidate ,
  regulatorVertexFramingWitness candidate ,
  sourceAssemblyLocalityWitness candidate ,
  unionCounitConeWitness candidate ,
  ordinaryEndpointWitness candidate ,
  strictEndpointWitness candidate ,
  homotopyCoherentEndpointWitness candidate ,
  lowerCochainWitness candidate ,
  normalizationSheetToCubicalKernelWitness candidate ,
  crossFrameEndpointWitness candidate ,
  ringedVerdierWitness candidate ,
  physicalReflectionParityWitness candidate ,
  genuineUnionRecollementWitness candidate ,
  sourceConductorDegreeWitness candidate ,
  framedPrimarySelectionWitness candidate ,
  coherentEndpointQFrameWitness candidate ,
  functorialRecollementWitness candidate ,
  mayerVietorisAssemblyWitness candidate ,
  residualOccurrenceSupportWitness candidate ,
  occurrenceGysinWitness candidate ,
  coefficientSystemCapWitness candidate ,
  descentTorsorWitness candidate ,
  twelveResidueCoordinateWitness candidate ,
  firstConductorPrimaryHomotopyWitness candidate ,
  physicalTCellCorrespondenceWitness candidate ,
  endpointCompleteSupportedDualWitness candidate ,
  completeChainValuedConductorSymbolWitness candidate ,
  quadraticConductorWitness candidate ,
  conductorDihedralTransportWitness candidate ,
  integralInvariantConductorChoiceWitness candidate ,
  physicalRowwiseConductorRestrictionWitness candidate ,
  fourChannelConductorReconstructionWitness candidate ,
  faceRankHomotopyDegreeWitness candidate ,
  endpointReverseConeWitness candidate ,
  sourceRelationMapWitness candidate ,
  jointSheetHomotopyWitness candidate ,
  sixOccurrenceDeterminantWitness candidate ,
  primitiveSixfoldResidueWitness candidate ,
  noFivefoldNodeEndpointPromotionWitness candidate ,
  nativeTripleGysinWitness candidate ,
  nativeAttachmentNonSplitWitness candidate ,
  noPrimitiveConductorSectionWitness candidate ,
  weightedCollarCoefficientWitness candidate ,
  rawCollarConductorVanishingWitness candidate ,
  resolvedIdealSourceDescentWitness candidate ,
  relationOnlyComparisonWitness candidate ,
  globalDerivedEndpointAttachmentWitness candidate ,
  supportedEndpointGysinWitness candidate ,
  supportedLiftTorsorSelectionWitness candidate ,
  localPrimitiveDescentWitness candidate ,
  physicalSideEdgeCompositionWitness candidate ,
  tStemBoundaryMultiplierWitness candidate ,
  mixedAndSameSheetStemWitness candidate ,
  intrinsicConductorTowerWitness candidate ,
  ambientIntrinsicFibreWitness candidate ,
  intrinsicFibreGlobalAttachmentWitness candidate ,
  faceRankNotCompleteHomotopyDegreeWitness candidate ,
  nativeShortFaceWitness candidate ,
  jointComplementaryFaceCapWitness candidate ,
  jointGenericEndpointDiagonalWitness candidate ,
  constantSpatialCochainWitness candidate ,
  normalizationSheetExtensionObstructionWitness candidate ,
  nativeSpatialThreeExtensionWitness candidate ,
  fourteenTriangleCycleWitness candidate ,
  endpointTriangleEssentialityWitness candidate ,
  coherentNormalizationSheetExtensionWitness candidate ,
  faceRingNormalLocalizedWitness candidate ,
  incidentLongStarSelectionWitness candidate ,
  tCellLongStarAnticommutationWitness candidate ,
  mixedEdgeAttachmentTransportWitness candidate ,
  longStarsAsBridgeDifferencesWitness candidate ,
  noCellwiseTCellLongStarBijectionWitness candidate ,
  conductorCostalkCounitWitness candidate ,
  costalkPrimarySelectionWitness candidate ,
  globalEndpointTransformationWitness candidate ,
  endpointJetObstructionWitness candidate ,
  fullConductorSquareCompletionWitness candidate ,
  markedD03SupportChangingWitness candidate ,
  unavoidableD25SupportWitness candidate ,
  completedNormalDualWitness candidate ,
  exactTraceImageIdealWitness candidate ,
  quadraticCubicReesFiltrationWitness candidate ,
  reesFaceVanishingWitness candidate ,
  physicalSupportedReesGysinLiftWitness candidate ,
  markedGalleryNormalGraphWitness candidate ,
  completedToricProperDescentWitness candidate ,
  conductorOperationNaturalityWitness candidate ,
  formalPuncturedTargetWitness candidate ,
  physicalCollarAndReflectionWitness candidate ,
  nativeOccurrenceExcessWitness candidate ,
  sourceRelationExcessWitness candidate ,
  nativeNormalizationExcessWitness candidate ,
  higherWedgeReesDefectWitness candidate ,
  puncturedLocalDualWitness candidate ,
  reciprocalExcessTraceWitness candidate ,
  predictedEnrichedSupportSquareWitness candidate ,
  structuralFalsifierWitness candidate ,
  minimalPredictiveEnvelopeWitness candidate ,
  predictedThreeCoordinateFingerprintWitness candidate ,
  nativeUniversalPuncturedOverlapWitness candidate ,
  nonsplitOccurrenceExtensionWitness candidate ,
  distinctCoefficientActionWitness candidate ,
  cechSupportedReciprocalTraceWitness candidate ,
  twoChartRelationHomotopyWitness candidate ,
  oddConductorClassWitness candidate ,
  occurrencePreservingAuxiliaryBridgeWitness candidate ,
  quadraticAuxiliaryNativeDefectWitness candidate ,
  shortReesDivisorIncidenceWitness candidate ,
  directPhysicalDefectWitness candidate ,
  enhancedPhysicalCollarTargetWitness candidate ,
  referenceQuadraticDefectExperimentWitness candidate ,
  totalNormalizationKernelWitness candidate ,
  filteredNormalizationDefectWitness candidate ,
  fullConductorTwoGradeDualityWitness candidate ,
  separatedDilationBoundaryWitness candidate ,
  allDegreeConductorOperationWitness candidate ,
  supportedEndpointClassWitness candidate ,
  scalarTangentialBlindnessWitness candidate ,
  dihedralOrientationWitness candidate ,
  fineZeroDihedralAttachmentWitness candidate ,
  boundaryCellWitness candidate ,
  discrepancyFrameWitness candidate

-- A coherent mate still does not contain K or delta(K)=Delta. Promotion to an
-- admissible filler requires the existing independent fibre unchanged.
record MateWithAdmissibleFiller {ℓ : Level}
  {P : DGPyramidBoundary {ℓ}} {Partial : PartialMariciPacket P}
  (MateSpec : PhysicalMixedVarianceMateSpecification Partial)
  (Frame : PyramidFrame P) : Type (ℓ-suc ℓ) where
  field
    coherentMate : PhysicalMixedVarianceMate MateSpec
    admissibleFiller : AdmissibleFiller P Frame

-- No PhysicalMixedVarianceMate or MateWithAdmissibleFiller inhabitant is
-- constructed from current coefficient, carrier, or target-sector packets.
