{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidPartialMariciAdapter where

open import Cubical.Foundations.Prelude hiding (J)
open import DGPyramidBoundary
open import DGPyramidAdapter
open import DGPyramidQSupport
open import DGPyramidCarrierEndpoint
open import DGPyramidMarkedNormalQ
open import DGPyramidSupportEquivalence
open import DGPyramidQFillingAttachment
open import DGPyramidEndpointNormalCube
open import DGPyramidReesResonance
open import DGPyramidDihedralAttachment
open import DGPyramidDerivedHom
open import DGPyramidNonflatBaseChange
open import DGPyramidPurityDualTransgression
open import UpperShriekAdjunction
open import CartierSupportedHomCone
open import IteratedRegularImmersionPurity
open import TensorHomCurrying
open import SupportTriangleDualReversal
open import KFlatBaseChange
open import FirstNormalSymbol
open import StrictTwoTermSummand
open import DGPyramidPhysicalReesGysin
open import DGPyramidSupportedReesResidue
open import DGPyramidOrbitSupportedQ
open import DGPyramidBetaZeroExcessEndpoint
open import DGPyramidCommonSpatialGate
open import DGPyramidCubicalSupportedDualKernel
open import SupportedCohomologicalCorrespondence
open import DGPyramidRegulatorVertexDecomposition
open import DGPyramidBetaEndpointQTransgression
open import DGPyramidOrbitSupportAssembly
open import DGPyramidUnionRecollement
open import FunctorialLocalCohomology
open import DGPyramidFramedDeformations
open import DGPyramidNativeKernelRealization
open import DGPyramidOccurrenceDescent
open import DGPyramidTCellPyramid
open import DGPyramidTStemSideProduct
open import DGPyramidTCellLongStarComparison
open import DGPyramidMixedEdgeCostalk
open import DGPyramidShortFaceSpatialCap
open import DGPyramidNativeSpatialThreeExtension
open import DGPyramidEndpointTransformationSupport
open import DGPyramidCompletedNormalDual
open import DGPyramidMarkedGalleryToricDescent
open import DGPyramidConductorFormalTower
open import DGPyramidStructuralPrediction
open import DGPyramidNormalizationDualityDilation
open import DGPyramidAllDegreeEndpointTangential
open import DGPyramidPhysicalEndpointPullback
open import DGPyramidSupportedTraceDuality
open import DGPyramidConductorChannels
open import DGPyramidJointConductorCone
open import DGPyramidNativeConductorAttachment
open import DGPyramidReverseEndpointGysin
open import DGPyramidIntrinsicConductorResolution
open import DGPyramidFirstConductorCoherent
open import DGPyramidConductorSymbolLifting

-- Everything presently available, bundled around a TYPED candidate boundary.
-- Supplying P checks degrees and signs; it does not certify that P's e and H_C
-- are the physical spatial comparison and conductor cell.
record PartialMariciPacket {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    qSupport : QSupportCertificate {ℓ}
    carrierEndpoint : CarrierEndpointCertificate {ℓ}
    markedNormalQ : MarkedNormalQCertificate {ℓ}
    supportEquivalence : SupportPreservingEquivalenceCertificate {ℓ}
    qFillingAttachment : QFillingAttachmentCertificate {ℓ}
    endpointNormalCube : EndpointNormalCubeCertificate {ℓ}
    reesResonance : ReesResonanceCertificate {ℓ}
    dihedralAttachment : DihedralAttachmentCertificate {ℓ}
    derivedHomJustification : DerivedHomComputationCertificate {ℓ}
    nonflatBaseChange : RHomBaseChangeCertificate {ℓ}
    principalLineDuality : PrincipalLineDualityCertificate {ℓ}
    regularImmersionPurity : RegularImmersionPurityCertificate {ℓ}
    dualTransgression : DualTransgressionCertificate {ℓ}
    reesSelectorExcess : ReesSelectorExcessCertificate {ℓ}
    physicalReesGysinTriple : PhysicalReesGysinTripleCertificate {ℓ}
    occurrence35Summand : Occurrence35SummandCertificate {ℓ}
    cartierSupportedHomCone : CartierSupportedHomConeCertificate {ℓ}
    cartierUpperShriek : CartierUpperShriekCertificate {ℓ}
    iteratedRegularPurity : IteratedRegularPurityCertificate {ℓ}
    signedTensorHomCurrying : SignedTensorHomCurrying {ℓ}
    supportTriangleDuality : SupportTriangleDualityCertificate {ℓ}
    boundedFreeBaseChange : BoundedFreeBaseChangeCertificate {ℓ}
    firstNormalSymbol : FirstNormalSymbolCertificate {ℓ}
    strictSummandTruncation : StrictSummandTruncationCertificate {ℓ}
    supportedReesResidue : SupportedReesResidueTraceCertificate {ℓ}
    orbitSupportedQ : OrbitSupportedQCertificate {ℓ}
    betaZeroExcessEndpoint : BetaZeroExcessEndpointCertificate {ℓ}
    commonSpatialGate : CommonSpatialCorrespondenceGateCertificate {ℓ}
    cubicalSupportedDualKernel : CubicalSupportedDualKernelCertificate {ℓ}
    supportedCorrespondence : SupportedCorrespondenceCertificate {ℓ}
    regulatorVertexDecomposition : RegulatorVertexDecompositionCertificate {ℓ}
    betaEndpointQTransgression : BetaEndpointQTransgressionCertificate {ℓ}
    orbitSupportAssembly : OrbitSupportAssemblyCertificate {ℓ}
    unionRecollement : UnionRecollementCertificate {ℓ}
    functorialRecollement : FunctorialRecollementCertificate {ℓ}
    firstConductorDeformations : FirstConductorFramedDeformationCertificate {ℓ}
    coherentEndpointQFrame : CoherentEndpointQFrameCertificate {ℓ}
    occurrenceLinearPairing : OccurrenceLinearReversePairingCertificate {ℓ}
    obstructionComplementDescent : ObstructionComplementDescentCertificate {ℓ}
    tCellPyramid : TCellPyramidCertificate {ℓ}
    tStemSideProducts : TStemSideProductCertificate {ℓ}
    tCellLongStarComparison : TCellLongStarComparisonCertificate {ℓ}
    mixedShortEdgeAttachment : MixedShortEdgeAttachmentCertificate {ℓ}
    milnorConductorCostalk : MilnorConductorCostalkCertificate {ℓ}
    nativeShortFaceComparison : NativeShortFaceComparisonCertificate {ℓ}
    jointConductorSpatialCap : JointConductorSpatialCapCertificate {ℓ}
    normalizationSheetObstruction :
      NormalizationSheetExtensionObstructionCertificate {ℓ}
    nativeSpatialThreeExtension : NativeSpatialThreeExtensionCertificate {ℓ}
    normalizationSheetCoherentExtension :
      NormalizationSheetCoherentExtensionCertificate {ℓ}
    globalEndpointTransformations : GlobalEndpointTransformationCertificate {ℓ}
    fullConductorSquareSupport : FullConductorSquareSupportCertificate {ℓ}
    completedNormalDual : CompletedNormalDualComparisonCertificate {ℓ}
    markedGalleryToricDescent : MarkedGalleryToricDescentCertificate {ℓ}
    conductorFormalTower : ConductorFormalTowerCertificate {ℓ}
    structuralPrediction :
      MariciStructuralPrediction markedGalleryToricDescent conductorFormalTower
    derivedNormalizationKernel : DerivedNormalizationKernelCertificate {ℓ}
    fullConductorTwoGradeDuality : FullConductorTwoGradeDualityCertificate {ℓ}
    separatedCoefficientDilation : SeparatedCoefficientDilationCertificate {ℓ}
    allDegreeConductorComparison : AllDegreeConductorComparisonCertificate {ℓ}
    supportedEndpointClasses : SupportedEndpointClassCertificate {ℓ}
    tangentialDualityScalarPairing : TangentialDualityScalarPairingCertificate {ℓ}
    physicalEndpointPullback : PhysicalEndpointPullbackCertificate {ℓ}
    endpointCompleteTCellPyramid : EndpointCompleteTCellPyramidCertificate {ℓ}
    supportedOccurrenceTrace : SupportedOccurrenceTraceCertificate {ℓ}
    wholeKoszulGysin : WholeKoszulGysinCertificate {ℓ}
    normalizationSupportContinuation : NormalizationSupportContinuationCertificate {ℓ}
    descentDuality : DescentDualityCertificate {ℓ}
    fourConductorChannels : FourConductorChannelCertificate {ℓ}
    endpointCompleteReverseCone : EndpointCompleteReverseConeCertificate {ℓ}
    conductorIdealResolvedMaps : ConductorIdealResolvedMapCertificate {ℓ}
    jointNormalizationDual : JointNormalizationDualCertificate {ℓ}
    nativeConductorAttachment : NativeConductorDualAttachmentCertificate {ℓ}
    normalizationIdealDescent : NormalizationIdealDescentCertificate {ℓ}
    reverseEndpointGysin : ReverseEndpointGysinCertificate {ℓ}
    intrinsicConductorResolution : IntrinsicConductorResolutionCertificate {ℓ}
    firstConductorCoherent : FirstConductorCoherentPrimaryCertificate {ℓ}
    conductorSymbolLifting : ConductorSymbolLiftingCertificate {ℓ}

    morseDegreeShift : MorseDegreeAdapter P

    -- The Q certificate is installed only through the existing generic-Q
    -- adapter gate, never by its unit coordinate alone.
    adapterSpecification : AdapterSpecification P
    qSupportBridge :
      QSupportAdapterBridge adapterSpecification qSupport

    -- Cross-certificate compatibility is explicit. Concrete packets choose
    -- rich equality/commuting-diagram records for these types.
    CarrierQCompatibility :
      CarrierEndpointCertificate {ℓ} → QSupportCertificate {ℓ} → Type ℓ
    carrierQWitness : CarrierQCompatibility carrierEndpoint qSupport

    MarkedQCompatibility :
      MarkedNormalQCertificate {ℓ} → QSupportCertificate {ℓ} → Type ℓ
    markedQWitness : MarkedQCompatibility markedNormalQ qSupport

    EquivalenceQCompatibility :
      SupportPreservingEquivalenceCertificate {ℓ} →
      QSupportCertificate {ℓ} → Type ℓ
    equivalenceQWitness :
      EquivalenceQCompatibility supportEquivalence qSupport

    FillingQCompatibility :
      QFillingAttachmentCertificate {ℓ} →
      QSupportCertificate {ℓ} → Type ℓ
    fillingQWitness :
      FillingQCompatibility qFillingAttachment qSupport

    NormalCubeCompatibility :
      EndpointNormalCubeCertificate {ℓ} →
      MarkedNormalQCertificate {ℓ} → Type ℓ
    normalCubeWitness :
      NormalCubeCompatibility endpointNormalCube markedNormalQ

    ResonanceFillingCompatibility :
      ReesResonanceCertificate {ℓ} →
      QFillingAttachmentCertificate {ℓ} → Type ℓ
    resonanceFillingWitness :
      ResonanceFillingCompatibility reesResonance qFillingAttachment

    DihedralFillingCompatibility :
      DihedralAttachmentCertificate {ℓ} →
      QFillingAttachmentCertificate {ℓ} → Type ℓ
    dihedralFillingWitness :
      DihedralFillingCompatibility dihedralAttachment qFillingAttachment

    DerivedHomSourceCompatibility :
      DerivedHomComputationCertificate {ℓ} →
      SupportPreservingEquivalenceCertificate {ℓ} → Type ℓ
    derivedHomSourceWitness :
      DerivedHomSourceCompatibility derivedHomJustification supportEquivalence

    BaseChangeQCompatibility :
      RHomBaseChangeCertificate {ℓ} →
      QSupportCertificate {ℓ} → Type ℓ
    baseChangeQWitness :
      BaseChangeQCompatibility nonflatBaseChange qSupport

    PurityBranchCompatibility :
      PrincipalLineDualityCertificate {ℓ} →
      RegularImmersionPurityCertificate {ℓ} → Type ℓ
    purityBranchWitness :
      PurityBranchCompatibility principalLineDuality regularImmersionPurity

    DualSupportCompatibility :
      DualTransgressionCertificate {ℓ} →
      QSupportCertificate {ℓ} → Type ℓ
    dualSupportWitness :
      DualSupportCompatibility dualTransgression qSupport

    ReesExcessCompatibility :
      ReesSelectorExcessCertificate {ℓ} →
      ReesResonanceCertificate {ℓ} → Type ℓ
    reesExcessWitness :
      ReesExcessCompatibility reesSelectorExcess reesResonance

    PhysicalSpecializationCompatibility :
      PhysicalReesGysinTripleCertificate {ℓ} →
      ReesResonanceCertificate {ℓ} → Type ℓ
    physicalSpecializationWitness :
      PhysicalSpecializationCompatibility physicalReesGysinTriple reesResonance

    OccurrenceFactorCompatibility :
      Occurrence35SummandCertificate {ℓ} →
      EndpointNormalCubeCertificate {ℓ} → Type ℓ
    occurrenceFactorWitness :
      OccurrenceFactorCompatibility occurrence35Summand endpointNormalCube

    CartierConeTripleCompatibility :
      CartierSupportedHomConeCertificate {ℓ} →
      PhysicalReesGysinTripleCertificate {ℓ} → Type ℓ
    cartierConeTripleWitness :
      CartierConeTripleCompatibility cartierSupportedHomCone physicalReesGysinTriple

    ShriekPurityCompatibility :
      CartierUpperShriekCertificate {ℓ} →
      RegularImmersionPurityCertificate {ℓ} → Type ℓ
    shriekPurityWitness :
      ShriekPurityCompatibility cartierUpperShriek regularImmersionPurity

    IteratedPurityCompatibility :
      IteratedRegularPurityCertificate {ℓ} →
      RegularImmersionPurityCertificate {ℓ} → Type ℓ
    iteratedPurityWitness :
      IteratedPurityCompatibility iteratedRegularPurity regularImmersionPurity

    CurryingDerivedHomCompatibility :
      SignedTensorHomCurrying {ℓ} →
      DerivedHomComputationCertificate {ℓ} → Type ℓ
    curryingDerivedHomWitness :
      CurryingDerivedHomCompatibility signedTensorHomCurrying derivedHomJustification

    SupportDualTransgressionCompatibility :
      SupportTriangleDualityCertificate {ℓ} →
      DualTransgressionCertificate {ℓ} → Type ℓ
    supportDualTransgressionWitness :
      SupportDualTransgressionCompatibility supportTriangleDuality dualTransgression

    KFlatNonflatCompatibility :
      BoundedFreeBaseChangeCertificate {ℓ} →
      RHomBaseChangeCertificate {ℓ} → Type ℓ
    kFlatNonflatWitness :
      KFlatNonflatCompatibility boundedFreeBaseChange nonflatBaseChange

    FirstSymbolPhysicalCompatibility :
      FirstNormalSymbolCertificate {ℓ} →
      PhysicalReesGysinTripleCertificate {ℓ} → Type ℓ
    firstSymbolPhysicalWitness :
      FirstSymbolPhysicalCompatibility firstNormalSymbol physicalReesGysinTriple

    StrictOccurrenceSummandCompatibility :
      StrictSummandTruncationCertificate {ℓ} →
      Occurrence35SummandCertificate {ℓ} → Type ℓ
    strictOccurrenceSummandWitness :
      StrictOccurrenceSummandCompatibility
        strictSummandTruncation occurrence35Summand

    SupportedResidueDualityCompatibility :
      SupportedReesResidueTraceCertificate {ℓ} →
      SupportTriangleDualityCertificate {ℓ} → Type ℓ
    supportedResidueDualityWitness :
      SupportedResidueDualityCompatibility
        supportedReesResidue supportTriangleDuality

    SupportedResidueExcessCompatibility :
      SupportedReesResidueTraceCertificate {ℓ} →
      ReesSelectorExcessCertificate {ℓ} → Type ℓ
    supportedResidueExcessWitness :
      SupportedResidueExcessCompatibility
        supportedReesResidue reesSelectorExcess

    OrbitQSupportCompatibility :
      OrbitSupportedQCertificate {ℓ} →
      QSupportCertificate {ℓ} → Type ℓ
    orbitQSupportWitness :
      OrbitQSupportCompatibility orbitSupportedQ qSupport

    OrbitPurityCompatibility :
      OrbitSupportedQCertificate {ℓ} →
      IteratedRegularPurityCertificate {ℓ} → Type ℓ
    orbitPurityWitness :
      OrbitPurityCompatibility orbitSupportedQ iteratedRegularPurity

    BetaFamilyPhysicalCompatibility :
      BetaZeroExcessEndpointCertificate {ℓ} →
      PhysicalReesGysinTripleCertificate {ℓ} → Type ℓ
    betaFamilyPhysicalWitness :
      BetaFamilyPhysicalCompatibility
        betaZeroExcessEndpoint physicalReesGysinTriple

    BetaEndpointCompatibility :
      BetaZeroExcessEndpointCertificate {ℓ} →
      EndpointNormalCubeCertificate {ℓ} → Type ℓ
    betaEndpointWitness :
      BetaEndpointCompatibility betaZeroExcessEndpoint endpointNormalCube

    CommonSpatialEndpointCompatibility :
      CommonSpatialCorrespondenceGateCertificate {ℓ} →
      EndpointNormalCubeCertificate {ℓ} → Type ℓ
    commonSpatialEndpointWitness :
      CommonSpatialEndpointCompatibility commonSpatialGate endpointNormalCube

    CommonSpatialResidueCompatibility :
      CommonSpatialCorrespondenceGateCertificate {ℓ} →
      SupportedReesResidueTraceCertificate {ℓ} → Type ℓ
    commonSpatialResidueWitness :
      CommonSpatialResidueCompatibility commonSpatialGate supportedReesResidue

    CubicalKernelDualityCompatibility :
      CubicalSupportedDualKernelCertificate {ℓ} →
      SupportTriangleDualityCertificate {ℓ} → Type ℓ
    cubicalKernelDualityWitness :
      CubicalKernelDualityCompatibility
        cubicalSupportedDualKernel supportTriangleDuality

    CubicalKernelResidueCompatibility :
      CubicalSupportedDualKernelCertificate {ℓ} →
      SupportedReesResidueTraceCertificate {ℓ} → Type ℓ
    cubicalKernelResidueWitness :
      CubicalKernelResidueCompatibility
        cubicalSupportedDualKernel supportedReesResidue

    CubicalKernelSpatialGateCompatibility :
      CubicalSupportedDualKernelCertificate {ℓ} →
      CommonSpatialCorrespondenceGateCertificate {ℓ} → Type ℓ
    cubicalKernelSpatialGateWitness :
      CubicalKernelSpatialGateCompatibility
        cubicalSupportedDualKernel commonSpatialGate

    ExtraordinaryCorrespondenceCompatibility :
      SupportedCorrespondenceCertificate {ℓ} →
      CommonSpatialCorrespondenceGateCertificate {ℓ} →
      SupportedReesResidueTraceCertificate {ℓ} → Type ℓ
    extraordinaryCorrespondenceWitness :
      ExtraordinaryCorrespondenceCompatibility
        supportedCorrespondence commonSpatialGate supportedReesResidue

    FilteredExcessCorrespondenceCompatibility :
      SupportedCorrespondenceCertificate {ℓ} →
      FirstNormalSymbolCertificate {ℓ} →
      BetaZeroExcessEndpointCertificate {ℓ} → Type ℓ
    filteredExcessCorrespondenceWitness :
      FilteredExcessCorrespondenceCompatibility
        supportedCorrespondence firstNormalSymbol betaZeroExcessEndpoint

    RegulatorVertexCompatibility :
      RegulatorVertexDecompositionCertificate {ℓ} →
      BetaZeroExcessEndpointCertificate {ℓ} → Type ℓ
    regulatorVertexWitness :
      RegulatorVertexCompatibility
        regulatorVertexDecomposition betaZeroExcessEndpoint

    BetaTransgressionCompatibility :
      BetaEndpointQTransgressionCertificate {ℓ} →
      RegulatorVertexDecompositionCertificate {ℓ} →
      QSupportCertificate {ℓ} → Type ℓ
    betaTransgressionWitness :
      BetaTransgressionCompatibility
        betaEndpointQTransgression regulatorVertexDecomposition qSupport

    OrbitAssemblyCompatibility :
      OrbitSupportAssemblyCertificate {ℓ} →
      OrbitSupportedQCertificate {ℓ} → Type ℓ
    orbitAssemblyWitness :
      OrbitAssemblyCompatibility orbitSupportAssembly orbitSupportedQ

    AssemblyCorrespondenceCompatibility :
      OrbitSupportAssemblyCertificate {ℓ} →
      SupportedCorrespondenceCertificate {ℓ} → Type ℓ
    assemblyCorrespondenceWitness :
      AssemblyCorrespondenceCompatibility
        orbitSupportAssembly supportedCorrespondence

    RecollementAssemblyCompatibility :
      UnionRecollementCertificate {ℓ} →
      OrbitSupportAssemblyCertificate {ℓ} → Type ℓ
    recollementAssemblyWitness :
      RecollementAssemblyCompatibility unionRecollement orbitSupportAssembly

    FunctorialRecollementCompatibility :
      FunctorialRecollementCertificate {ℓ} →
      UnionRecollementCertificate {ℓ} →
      CartierUpperShriekCertificate {ℓ} → Type ℓ
    functorialRecollementWitness :
      FunctorialRecollementCompatibility
        functorialRecollement unionRecollement cartierUpperShriek

    ConductorFrameCompatibility :
      FirstConductorFramedDeformationCertificate {ℓ} →
      FirstNormalSymbolCertificate {ℓ} → Type ℓ
    conductorFrameWitness :
      ConductorFrameCompatibility firstConductorDeformations firstNormalSymbol

    CoherentFrameTransgressionCompatibility :
      CoherentEndpointQFrameCertificate {ℓ} →
      BetaEndpointQTransgressionCertificate {ℓ} → Type ℓ
    coherentFrameTransgressionWitness :
      CoherentFrameTransgressionCompatibility
        coherentEndpointQFrame betaEndpointQTransgression

    OccurrenceKernelCompatibility :
      OccurrenceLinearReversePairingCertificate {ℓ} →
      CubicalSupportedDualKernelCertificate {ℓ} → Type ℓ
    occurrenceKernelWitness :
      OccurrenceKernelCompatibility occurrenceLinearPairing cubicalSupportedDualKernel

    DescentRecollementCompatibility :
      ObstructionComplementDescentCertificate {ℓ} →
      UnionRecollementCertificate {ℓ} → Type ℓ
    descentRecollementWitness :
      DescentRecollementCompatibility obstructionComplementDescent unionRecollement

    TCellDescentCompatibility :
      TCellPyramidCertificate {ℓ} →
      ObstructionComplementDescentCertificate {ℓ} → Type ℓ
    tCellDescentWitness :
      TCellDescentCompatibility tCellPyramid obstructionComplementDescent

    TStemProductCompatibility :
      TStemSideProductCertificate {ℓ} →
      TCellPyramidCertificate {ℓ} → Type ℓ
    tStemProductWitness :
      TStemProductCompatibility tStemSideProducts tCellPyramid

    TCellLongStarCompatibility :
      TCellLongStarComparisonCertificate {ℓ} →
      TStemSideProductCertificate {ℓ} →
      NativeSpatialThreeExtensionCertificate {ℓ} → Type ℓ
    tCellLongStarWitness :
      TCellLongStarCompatibility
        tCellLongStarComparison tStemSideProducts nativeSpatialThreeExtension

    MixedEdgeCostalkCompatibility :
      MixedShortEdgeAttachmentCertificate {ℓ} →
      MilnorConductorCostalkCertificate {ℓ} →
      NativeSpatialThreeExtensionCertificate {ℓ} → Type ℓ
    mixedEdgeCostalkWitness :
      MixedEdgeCostalkCompatibility
        mixedShortEdgeAttachment milnorConductorCostalk nativeSpatialThreeExtension

    ShortFaceSpatialCapCompatibility :
      NativeShortFaceComparisonCertificate {ℓ} →
      JointConductorSpatialCapCertificate {ℓ} →
      TStemSideProductCertificate {ℓ} → Type ℓ
    shortFaceSpatialCapWitness :
      ShortFaceSpatialCapCompatibility
        nativeShortFaceComparison jointConductorSpatialCap tStemSideProducts

    SheetExtensionCompatibility :
      NormalizationSheetExtensionObstructionCertificate {ℓ} →
      NormalizationIdealDescentCertificate {ℓ} → Type ℓ
    sheetExtensionWitness :
      SheetExtensionCompatibility
        normalizationSheetObstruction normalizationIdealDescent

    NativeSpatialExtensionCompatibility :
      NativeSpatialThreeExtensionCertificate {ℓ} →
      NativeShortFaceComparisonCertificate {ℓ} →
      JointConductorSpatialCapCertificate {ℓ} → Type ℓ
    nativeSpatialExtensionWitness :
      NativeSpatialExtensionCompatibility
        nativeSpatialThreeExtension nativeShortFaceComparison
        jointConductorSpatialCap

    CoherentSheetExtensionCompatibility :
      NormalizationSheetCoherentExtensionCertificate {ℓ} →
      NormalizationSheetExtensionObstructionCertificate {ℓ} → Type ℓ
    coherentSheetExtensionWitness :
      CoherentSheetExtensionCompatibility
        normalizationSheetCoherentExtension normalizationSheetObstruction

    EndpointTransformationSupportCompatibility :
      GlobalEndpointTransformationCertificate {ℓ} →
      FullConductorSquareSupportCertificate {ℓ} →
      ReverseEndpointGysinCertificate {ℓ} → Type ℓ
    endpointTransformationSupportWitness :
      EndpointTransformationSupportCompatibility
        globalEndpointTransformations fullConductorSquareSupport
        reverseEndpointGysin

    CompletedNormalDualCompatibility :
      CompletedNormalDualComparisonCertificate {ℓ} →
      NativeSpatialThreeExtensionCertificate {ℓ} →
      JointConductorSpatialCapCertificate {ℓ} → Type ℓ
    completedNormalDualWitness :
      CompletedNormalDualCompatibility
        completedNormalDual nativeSpatialThreeExtension jointConductorSpatialCap

    CompletedPhysicalDescentCompatibility :
      MarkedGalleryToricDescentCertificate {ℓ} →
      ConductorFormalTowerCertificate {ℓ} →
      CompletedNormalDualComparisonCertificate {ℓ} → Type ℓ
    completedPhysicalDescentWitness :
      CompletedPhysicalDescentCompatibility
        markedGalleryToricDescent conductorFormalTower completedNormalDual

    StructuralPredictionCompatibility :
      MariciStructuralPrediction markedGalleryToricDescent conductorFormalTower →
      ReverseEndpointGysinCertificate {ℓ} → Type ℓ
    structuralPredictionWitness :
      StructuralPredictionCompatibility structuralPrediction reverseEndpointGysin

    NormalizationDualityDilationCompatibility :
      DerivedNormalizationKernelCertificate {ℓ} →
      FullConductorTwoGradeDualityCertificate {ℓ} →
      SeparatedCoefficientDilationCertificate {ℓ} → Type ℓ
    normalizationDualityDilationWitness :
      NormalizationDualityDilationCompatibility
        derivedNormalizationKernel fullConductorTwoGradeDuality
        separatedCoefficientDilation

    EndpointScalarComparisonCompatibility :
      AllDegreeConductorComparisonCertificate {ℓ} →
      SupportedEndpointClassCertificate {ℓ} →
      TangentialDualityScalarPairingCertificate {ℓ} → Type ℓ
    endpointScalarComparisonWitness :
      EndpointScalarComparisonCompatibility allDegreeConductorComparison
        supportedEndpointClasses tangentialDualityScalarPairing

    PhysicalEndpointPullbackCompatibility :
      PhysicalEndpointPullbackCertificate {ℓ} → Type ℓ
    physicalEndpointPullbackWitness :
      PhysicalEndpointPullbackCompatibility physicalEndpointPullback

    EndpointCompleteDescentCompatibility :
      EndpointCompleteTCellPyramidCertificate {ℓ} →
      ObstructionComplementDescentCertificate {ℓ} →
      DescentDualityCertificate {ℓ} → Type ℓ
    endpointCompleteDescentWitness :
      EndpointCompleteDescentCompatibility
        endpointCompleteTCellPyramid obstructionComplementDescent descentDuality

    SupportedTraceGysinCompatibility :
      SupportedOccurrenceTraceCertificate {ℓ} →
      WholeKoszulGysinCertificate {ℓ} →
      OccurrenceLinearReversePairingCertificate {ℓ} → Type ℓ
    supportedTraceGysinWitness :
      SupportedTraceGysinCompatibility
        supportedOccurrenceTrace wholeKoszulGysin occurrenceLinearPairing

    NormalizationSupportedGysinCompatibility :
      NormalizationSupportContinuationCertificate {ℓ} →
      WholeKoszulGysinCertificate {ℓ} → Type ℓ
    normalizationSupportedGysinWitness :
      NormalizationSupportedGysinCompatibility
        normalizationSupportContinuation wholeKoszulGysin

    ConductorChannelCompatibility :
      FourConductorChannelCertificate {ℓ} →
      EndpointCompleteTCellPyramidCertificate {ℓ} →
      DescentDualityCertificate {ℓ} → Type ℓ
    conductorChannelWitness :
      ConductorChannelCompatibility
        fourConductorChannels endpointCompleteTCellPyramid descentDuality

    JointConductorConeCompatibility :
      EndpointCompleteReverseConeCertificate {ℓ} →
      ConductorIdealResolvedMapCertificate {ℓ} →
      JointNormalizationDualCertificate {ℓ} →
      FourConductorChannelCertificate {ℓ} → Type ℓ
    jointConductorConeWitness :
      JointConductorConeCompatibility
        endpointCompleteReverseCone conductorIdealResolvedMaps
        jointNormalizationDual fourConductorChannels

    NativeConductorDescentCompatibility :
      NativeConductorDualAttachmentCertificate {ℓ} →
      NormalizationIdealDescentCertificate {ℓ} →
      JointNormalizationDualCertificate {ℓ} → Type ℓ
    nativeConductorDescentWitness :
      NativeConductorDescentCompatibility
        nativeConductorAttachment normalizationIdealDescent jointNormalizationDual

    ReverseEndpointGysinCompatibility :
      ReverseEndpointGysinCertificate {ℓ} →
      EndpointCompleteReverseConeCertificate {ℓ} →
      NativeConductorDualAttachmentCertificate {ℓ} → Type ℓ
    reverseEndpointGysinWitness :
      ReverseEndpointGysinCompatibility
        reverseEndpointGysin endpointCompleteReverseCone nativeConductorAttachment

    IntrinsicConductorCompatibility :
      IntrinsicConductorResolutionCertificate {ℓ} →
      ReverseEndpointGysinCertificate {ℓ} →
      EndpointCompleteTCellPyramidCertificate {ℓ} → Type ℓ
    intrinsicConductorWitness :
      IntrinsicConductorCompatibility
        intrinsicConductorResolution reverseEndpointGysin
        endpointCompleteTCellPyramid

    FirstConductorCoherentCompatibility :
      FirstConductorCoherentPrimaryCertificate {ℓ} →
      FirstConductorFramedDeformationCertificate {ℓ} →
      CoherentEndpointQFrameCertificate {ℓ} → Type ℓ
    firstConductorCoherentWitness :
      FirstConductorCoherentCompatibility
        firstConductorCoherent firstConductorDeformations coherentEndpointQFrame

    ConductorSymbolCoherentCompatibility :
      ConductorSymbolLiftingCertificate {ℓ} →
      FirstConductorCoherentPrimaryCertificate {ℓ} → Type ℓ
    conductorSymbolCoherentWitness :
      ConductorSymbolCoherentCompatibility
        conductorSymbolLifting firstConductorCoherent

open PartialMariciPacket public

-- Exact residual obligations. Their predicates are specified independently of
-- their witnesses, preventing a completion record from defining "valid" to be
-- whatever value it happened to choose.
record PhysicalCompletionSpecification {ℓ : Level}
  {P : DGPyramidBoundary {ℓ}} (Partial : PartialMariciPacket P)
  : Type (ℓ-suc ℓ) where
  field
    MixedVarianceMate : Type ℓ
    PhysicalPlusConnector PhysicalMinusConnector : Type ℓ
    PhysicalEComparison PhysicalHCComparison : Type ℓ
    CartierReesComparison : Type ℓ
    nativeKernelSpecification : NativeKernelRealizationSpecification {ℓ}

    mateValid : MixedVarianceMate → Type ℓ
    plusConnectorValid : PhysicalPlusConnector → Type ℓ
    minusConnectorValid : PhysicalMinusConnector → Type ℓ
    eComparisonValid : PhysicalEComparison → Type ℓ
    hCComparisonValid : PhysicalHCComparison → Type ℓ
    cartierReesValid : CartierReesComparison → Type ℓ

    -- This is the consolidated source-to-cubical-kernel obligation. It is not
    -- inferred from the separate scalar or target-side compatibility gates.
    nativeKernelValid :
      NativeKernelRealization nativeKernelSpecification → Type ℓ

    -- Carrier-to-physical endpoint identification is part of the missing
    -- mixed-variance assembly, not inferred from endpoint coefficients.
    identifiesCarrierPlus :
      MixedVarianceMate → PhysicalPlusConnector → Type ℓ
    identifiesCarrierMinus :
      MixedVarianceMate → PhysicalMinusConnector → Type ℓ

    -- These predicates must identify the already typed cells of P with the
    -- physical constructions, not merely compare scalar readouts.
    identifiesBoundaryE : PhysicalEComparison → QFtwo P → Type ℓ
    identifiesBoundaryHC : PhysicalHCComparison → JFone P → Type ℓ

open PhysicalCompletionSpecification public

record PhysicalCompletionGates {ℓ : Level}
  {P : DGPyramidBoundary {ℓ}} {Partial : PartialMariciPacket P}
  (Spec : PhysicalCompletionSpecification Partial) : Type (ℓ-suc ℓ) where
  field
    mixedVarianceMate : MixedVarianceMate Spec
    mateWitness : mateValid Spec mixedVarianceMate

    physicalPlusConnector : PhysicalPlusConnector Spec
    physicalMinusConnector : PhysicalMinusConnector Spec
    plusWitness : plusConnectorValid Spec physicalPlusConnector
    minusWitness : minusConnectorValid Spec physicalMinusConnector
    carrierPlusWitness :
      identifiesCarrierPlus Spec mixedVarianceMate physicalPlusConnector
    carrierMinusWitness :
      identifiesCarrierMinus Spec mixedVarianceMate physicalMinusConnector

    physicalEComparison : PhysicalEComparison Spec
    physicalHCComparison : PhysicalHCComparison Spec
    eWitness : eComparisonValid Spec physicalEComparison
    hCWitness : hCComparisonValid Spec physicalHCComparison
    identifiesE : identifiesBoundaryE Spec physicalEComparison (e P)
    identifiesHC : identifiesBoundaryHC Spec physicalHCComparison (H_C P)

    cartierReesComparison : CartierReesComparison Spec
    cartierReesWitness : cartierReesValid Spec cartierReesComparison

    nativeKernelRealization :
      NativeKernelRealization (nativeKernelSpecification Spec)
    nativeKernelWitness : nativeKernelValid Spec nativeKernelRealization

open PhysicalCompletionGates public

-- Even completion of these comparison gates does not silently manufacture the
-- degree-zero K or its four framed witnesses. The final filler remains exactly
-- the separate AdmissibleFiller type from DGPyramidFiller.
