{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidEndpointTransformationSupport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record GlobalEndpointTransformationCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    EndpointExtension GlobalTransformation SupportedVariation : Type ℓ
    endpointExtension : EndpointExtension
    globalTransformation : GlobalTransformation
    transformationFixesOldQuotient : Type ℓ
    transformationFixesGenericArrow : Type ℓ
    transformationPreservesConductorAttachment : Type ℓ

    SevenCornerIdeal FullEightCornerIdeal EndpointCorner : Type ℓ
    sevenCornerIdeal : SevenCornerIdeal
    fullEightCornerIdeal : FullEightCornerIdeal
    endpointCorner : EndpointCorner
    sevenIntoEight : SevenCornerIdeal → FullEightCornerIdeal
    quotientIsEndpointCorner : Type ℓ

    SevenGenerators NineRelations ThreeSquareRelations : Type ℓ
    sevenGeneratorWitness : SevenGenerators
    nineRelationWitness : NineRelations
    threeSquareWitness : ThreeSquareRelations
    sevenNineThreeResolutionExact : Type ℓ

    FiniteNormalJet JetObstruction : Type ℓ
    restrictTransformation : GlobalTransformation → FiniteNormalJet
    obstruction : FiniteNormalJet → JetObstruction
    zeroJetObstruction : JetObstruction
    extendsGloballyExactlyWhenObstructionZero : Type ℓ
    constantDoubleSubsetCorrectionsDoNotExtend : Type ℓ

    DerivedNormalFibre FirstTor SecondTor : Type ℓ
    derivedNormalFibre : DerivedNormalFibre
    threeFirstTorLines : FirstTor
    oneSecondTorLine : SecondTor
    noHigherNormalTor : Type ℓ
    exactWeightRigidityRetained : Type ℓ

record FullConductorSquareSupportCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    CoherentExtension FullConductorSquareCompletion : Type ℓ
    completeSquare : CoherentExtension → FullConductorSquareCompletion
    Rank9Completions Rank3EquivariantCompletions : Type ℓ
    rank9Witness : Rank9Completions
    rank3Witness : Rank3EquivariantCompletions
    lowerConductorAddsNoEquation : Type ℓ
    resolvedDiagonalRequiresHomotopyCorrection : Type ℓ

    CompleteTarget Facet35 LongFacet03 MarkedD03Gallery Facet03Union35 : Type ℓ
    SupportedOn : CoherentExtension → Type ℓ → Type ℓ
    noMarkedD03SupportedExtension : (e : CoherentExtension) →
      SupportedOn e MarkedD03Gallery → ⊥
    noLongFacet03SupportedExtension : (e : CoherentExtension) →
      SupportedOn e LongFacet03 → ⊥

    Facet35Direction : Type ℓ
    firstFacet35Direction secondFacet35Direction : Facet35Direction
    Rank2Facet35 : Type ℓ
    rank2Facet35Witness : Rank2Facet35
    UnavoidableD25Support : Facet35Direction → Type ℓ
    firstUnavoidableD25 : UnavoidableD25Support firstFacet35Direction
    secondUnavoidableD25 : UnavoidableD25Support secondFacet35Direction
    ReflectionOdd : Facet35Direction → Type ℓ
    firstReflectionOdd : ReflectionOdd firstFacet35Direction
    secondReflectionOdd : ReflectionOdd secondFacet35Direction
    noInvariantFacet35Direction : Type ℓ

    PhysicalSupportChangingD03Comparison : Type ℓ
