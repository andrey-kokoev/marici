{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidOrbitSupportAssembly where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record OrbitSupportAssemblyCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    PairSupport IntersectionSupport UnionSupport : Type ℓ
    pair₁ pair₂ pair₃ : PairSupport
    intersection : IntersectionSupport
    union : UnionSupport

    IntersectionDual UnionDual : Type ℓ
    intersectionDual : IntersectionDual
    unionDual : UnionDual
    DegreeTwo DegreeThree DegreeFour DegreeSix : Type ℓ
    pairResidues : DegreeTwo
    pairwiseOverlaps : DegreeThree
    tripleCompatibility : DegreeFour
    intersectionPlacement : DegreeSix

    UnionResolution : Type ℓ
    unionResolution : UnionResolution
    TwentyEightGeneratorResolution : Type ℓ
    unionResolutionRanks181261 : TwentyEightGeneratorResolution
    unionDualDifferentialRetained : Type ℓ
    unionDualDifferentialWitness : unionDualDifferentialRetained

    LocalizedUnion LocalizedIntersection : Type ℓ
    localizedUnion : LocalizedUnion
    localizedIntersection : LocalizedIntersection
    zeroLocalizedIntersection : LocalizedIntersection
    localizedIntersectionVanishes :
      localizedIntersection ≡ zeroLocalizedIntersection
    localizedUnionClass : LocalizedUnion
    zeroLocalizedUnion : LocalizedUnion
    localizedUnionSurvives : localizedUnionClass ≡ zeroLocalizedUnion → ⊥

    ProposedSupportIdentification : Type ℓ
    identificationForcesUnionZero : ProposedSupportIdentification →
      localizedUnionClass ≡ zeroLocalizedUnion

    GenericOpen IntersectionGeneric : Type ℓ
    intersectionGeneric : IntersectionGeneric
    zeroIntersectionGeneric : IntersectionGeneric
    intersectionContractsGenerically :
      intersectionGeneric ≡ zeroIntersectionGeneric

    PCTarget GenericQ : Type ℓ
    unionProjection : PCTarget → GenericQ
    DerivedSection : Type ℓ
    unionHasNoDerivedSection : DerivedSection → ⊥

    CounitCone : Type ℓ
    unionCounitCone : CounitCone
    GenericData : Type ℓ
    retainedGenericData : GenericData
    coneRetainsGenericData : Type ℓ
    coneGenericWitness : coneRetainsGenericData

    NativeSource : Type ℓ
    SourceAssembly : NativeSource → Type ℓ
    NativeAssemblyComparison : NativeSource → CounitCone → Type ℓ

unionAssemblyIsNotIntersectionTensor : {ℓ : Level}
  (C : OrbitSupportAssemblyCertificate {ℓ}) →
  OrbitSupportAssemblyCertificate.ProposedSupportIdentification C → ⊥
unionAssemblyIsNotIntersectionTensor C identification =
  OrbitSupportAssemblyCertificate.localizedUnionSurvives C
    (OrbitSupportAssemblyCertificate.identificationForcesUnionZero C identification)
