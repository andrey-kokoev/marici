{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidNativeSpatialThreeExtension where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record NativeSpatialThreeExtensionCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    EndpointIdeals ShortFaceRing LongFacetLinks MixedBridgeModules Conductor : Type ℓ
    endpointIdeals : EndpointIdeals
    shortFaceRing : ShortFaceRing
    longFacetLinks : LongFacetLinks
    mixedBridgeModules : MixedBridgeModules
    conductor : Conductor

    endpointIntoShort : EndpointIdeals → ShortFaceRing
    restrictToLongLinks : ShortFaceRing → LongFacetLinks
    compareOnBridges : LongFacetLinks → MixedBridgeModules
    augmentConductor : MixedBridgeModules → Conductor
    ExactPolynomialThreeExtension : Type ℓ
    exactThreeExtensionWitness : ExactPolynomialThreeExtension
    NativeDual : Type ℓ
    nativeDual : NativeDual
    spatialRealizesEntireNativeDual : Type ℓ
    nativeNonSplitAttachmentTransported : Type ℓ

    LongStarTriangle EndpointTriangle SpatialCycle : Type ℓ
    twelveLongStarTriangles : LongStarTriangle
    positiveEndpointTriangle negativeEndpointTriangle : EndpointTriangle
    fourteenTriangleCycle : SpatialCycle
    cycleClosed : Type ℓ
    EndpointTrianglesEssential : Type ℓ
    endpointTrianglesEssentialWitness : EndpointTrianglesEssential

    ThreeLongFacetLinks ThreeMixedBridges : Type ℓ
    threeLongFacetLinksWitness : ThreeLongFacetLinks
    threeMixedBridgesWitness : ThreeMixedBridges
    NormRow RoadRelation AugmentationRow : Type ℓ
    normRow111 : NormRow
    roadRelationOneMinusRotationSquared : RoadRelation
    augmentationRow111 : AugmentationRow
    constantOccurrenceWindowExact : Type ℓ

    PolynomialNaturality CoherentEquivariance : Type ℓ
    polynomialNaturalityWitness : PolynomialNaturality
    coherentEquivarianceWitness : CoherentEquivariance
    FaceRingToNormalLocalizedPCComparison : Type ℓ

record NormalizationSheetCoherentExtensionCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    IdealMap CoherentExtension ExtensionObstruction RestrictionHomotopy : Type ℓ
    Rank40IdealMaps Rank9Coherent Rank31Obstructed : Type ℓ
    rank40Witness : Rank40IdealMaps
    rank9Witness : Rank9Coherent
    rank31Witness : Rank31Obstructed
    coherentExtension : IdealMap → RestrictionHomotopy → CoherentExtension
    obstruction : IdealMap → ExtensionObstruction
    zeroObstruction : ExtensionObstruction
    coherentDirectionsHaveZeroObstruction : CoherentExtension → Type ℓ
    saturatedExtensionSequence : Type ℓ

    StrictNonzeroExtension : Type ℓ
    noStrictNonzeroExtension : StrictNonzeroExtension → ⊥
    normalizationSheetMapIsZeroForCoherentDirections : Type ℓ
    uniqueRestrictionHomotopyInFrame : Type ℓ
    coherentComponentsContractible : Type ℓ

    RelationOnlyMap : Type ℓ
    relationOnlyObstructed : RelationOnlyMap → Type ℓ
    scalarConductorDetectsEveryCoherentDirection : Type ℓ

    EquivariantIdealMap EquivariantCoherent EquivariantObstruction : Type ℓ
    Rank13EquivariantIdeal Rank3EquivariantCoherent Rank10EquivariantObstructed : Type ℓ
    rank13Witness : Rank13EquivariantIdeal
    rank3Witness : Rank3EquivariantCoherent
    rank10Witness : Rank10EquivariantObstructed
    equivariantSequenceSaturated : Type ℓ
    PhysicalCoherentExtensionSelection : Type ℓ
