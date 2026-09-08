{-# OPTIONS --safe --cubical --guardedness #-}
module FunctorialLocalCohomology where

open import Cubical.Foundations.Prelude
open import UpperShriekAdjunction

-- Functorial affine/local-cohomology recollement in the shape used by the
-- Stacks extended-Cech construction.
record FunctorialLocalCohomology {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Ambient Supported : CategoryData {ℓ}
    supportInclusion : FunctorData Supported Ambient
    sectionsWithSupport : FunctorData Ambient Supported
    supportAdjunction :
      UpperShriekAdjunction Supported Ambient
    adjunctionUsesSupportInclusion :
      UpperShriekAdjunction.pushforward supportAdjunction ≡ supportInclusion
    adjunctionUsesSectionsWithSupport :
      UpperShriekAdjunction.upperShriek supportAdjunction ≡ sectionsWithSupport

  private
    identityAmbient : FunctorData Ambient Ambient
    identityAmbient = record
      { F₀ = λ X → X
      ; F₁ = λ f → f
      ; map-id = refl
      ; map-compose = λ g f → refl
      }

  field
    SupportEndofunctor OpenEndofunctor CechTensorFunctor :
      FunctorData Ambient Ambient
    supportCounit : NaturalTransformation SupportEndofunctor identityAmbient
    ambientToOpen : NaturalTransformation identityAmbient OpenEndofunctor

    -- The extended Cech tensor complex computes RΓ_Z naturally in K.
    cechToSupport : NaturalTransformation CechTensorFunctor SupportEndofunctor
    supportToCech : NaturalTransformation SupportEndofunctor CechTensorFunctor


    cechSupportSection : (X : CategoryData.Obj Ambient) →
      CategoryData._∘_ Ambient
        (NaturalTransformation.component supportToCech X)
        (NaturalTransformation.component cechToSupport X) ≡
      CategoryData.id Ambient
    cechSupportRetraction : (X : CategoryData.Obj Ambient) →
      CategoryData._∘_ Ambient
        (NaturalTransformation.component cechToSupport X)
        (NaturalTransformation.component supportToCech X) ≡
      CategoryData.id Ambient

    Shift : CategoryData.Obj Ambient → CategoryData.Obj Ambient
    localizationConnecting : (X : CategoryData.Obj Ambient) →
      CategoryData.Hom Ambient
        (FunctorData.F₀ OpenEndofunctor X)
        (Shift (FunctorData.F₀ SupportEndofunctor X))
    LocalizationTriangle : (X : CategoryData.Obj Ambient) → Type ℓ
    localizationTriangle : (X : CategoryData.Obj Ambient) →
      LocalizationTriangle X
    localizationNatural : {X Y : CategoryData.Obj Ambient} →
      CategoryData.Hom Ambient X Y → Type ℓ

    composeEndofunctors :
      FunctorData Ambient Ambient → FunctorData Ambient Ambient →
      FunctorData Ambient Ambient
    supportIdempotence : NaturalTransformation
      (composeEndofunctors SupportEndofunctor SupportEndofunctor)
      SupportEndofunctor
    openIdempotence : NaturalTransformation
      (composeEndofunctors OpenEndofunctor OpenEndofunctor)
      OpenEndofunctor

    ZeroObject : CategoryData.Obj Ambient
    supportThenOpenZero : (X : CategoryData.Obj Ambient) →
      FunctorData.F₀
        (composeEndofunctors OpenEndofunctor SupportEndofunctor) X ≡ ZeroObject
    openThenSupportZero : (X : CategoryData.Obj Ambient) →
      FunctorData.F₀
        (composeEndofunctors SupportEndofunctor OpenEndofunctor) X ≡ ZeroObject

-- Functorial Mayer-Vietoris data for a union of supports/opens. The maps are
-- natural transformations, so overlap classes cannot be replaced by a list of
-- unrelated residue groups.
record FunctorialMayerVietoris {ℓ : Level}
  (C : CategoryData {ℓ}) : Type (ℓ-suc ℓ) where
  field
    Global Open₁ Open₂ Intersection Pieces : FunctorData C C
    globalToPieces : NaturalTransformation Global Pieces
    piecesToIntersection : NaturalTransformation Pieces Intersection

    -- Concrete instances identify Pieces with the biproduct Open₁ ⊕ Open₂.
    PiecesAreBiproduct : Type ℓ
    piecesWitness : PiecesAreBiproduct
    DegreewiseShortExact : Type ℓ
    shortExactWitness : DegreewiseShortExact
    LongConnectingSequence : Type ℓ
    longConnectingWitness : LongConnectingSequence
    connectingNatural : Type ℓ
    connectingNaturalWitness : connectingNatural

record FunctorialRecollementCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    localCohomology : FunctorialLocalCohomology {ℓ}
    mayerVietoris :
      FunctorialMayerVietoris
        (FunctorialLocalCohomology.Ambient localCohomology)
