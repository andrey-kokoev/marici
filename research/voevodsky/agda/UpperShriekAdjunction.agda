{-# OPTIONS --safe --cubical --guardedness #-}
module UpperShriekAdjunction where

open import Cubical.Foundations.Prelude

-- A small, universe-uniform category interface sufficient for recording the
-- closed-immersion adjunction without importing a particular derived category.
record CategoryData {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Obj : Type ℓ
    Hom : Obj → Obj → Type ℓ
    id : {X : Obj} → Hom X X
    _∘_ : {X Y Z : Obj} → Hom Y Z → Hom X Y → Hom X Z
    id-left : {X Y : Obj} (f : Hom X Y) → id ∘ f ≡ f
    id-right : {X Y : Obj} (f : Hom X Y) → f ∘ id ≡ f
    assoc : {W X Y Z : Obj}
      (h : Hom Y Z) (g : Hom X Y) (f : Hom W X) →
      (h ∘ g) ∘ f ≡ h ∘ (g ∘ f)

record FunctorData {ℓ : Level} (C D : CategoryData {ℓ}) : Type (ℓ-suc ℓ) where
  private
    module C = CategoryData C
    module D = CategoryData D
  field
    F₀ : C.Obj → D.Obj
    F₁ : {X Y : C.Obj} → C.Hom X Y → D.Hom (F₀ X) (F₀ Y)
    map-id : {X : C.Obj} → F₁ (C.id {X}) ≡ D.id
    map-compose : {X Y Z : C.Obj} (g : C.Hom Y Z) (f : C.Hom X Y) →
      F₁ (C._∘_ g f) ≡ D._∘_ (F₁ g) (F₁ f)

record NaturalTransformation {ℓ : Level}
  {C D : CategoryData {ℓ}} (F G : FunctorData C D) : Type (ℓ-suc ℓ) where
  private
    module C = CategoryData C
    module D = CategoryData D
    module F = FunctorData F
    module G = FunctorData G
  field
    component : (X : C.Obj) → D.Hom (F.F₀ X) (G.F₀ X)
    natural : {X Y : C.Obj} (f : C.Hom X Y) →
      D._∘_ (G.F₁ f) (component X) ≡
      D._∘_ (component Y) (F.F₁ f)

-- i_* : Closed -> Ambient is left adjoint to i! : Ambient -> Closed.
-- The transpose maps make the mixed variance explicit rather than encoding
-- upper shriek as an unstructured object operation.
record UpperShriekAdjunction {ℓ : Level}
  (Closed Ambient : CategoryData {ℓ}) : Type (ℓ-suc ℓ) where
  private
    module Z = CategoryData Closed
    module X = CategoryData Ambient
  field
    pushforward : FunctorData Closed Ambient
    upperShriek : FunctorData Ambient Closed

  private
    module i* = FunctorData pushforward
    module i! = FunctorData upperShriek

  field
    transpose : {A : Z.Obj} {B : X.Obj} →
      X.Hom (i*.F₀ A) B → Z.Hom A (i!.F₀ B)
    untranspose : {A : Z.Obj} {B : X.Obj} →
      Z.Hom A (i!.F₀ B) → X.Hom (i*.F₀ A) B
    transposeSection : {A : Z.Obj} {B : X.Obj}
      (f : X.Hom (i*.F₀ A) B) → untranspose (transpose f) ≡ f
    transposeRetraction : {A : Z.Obj} {B : X.Obj}
      (g : Z.Hom A (i!.F₀ B)) → transpose (untranspose g) ≡ g

    unit : (A : Z.Obj) → Z.Hom A (i!.F₀ (i*.F₀ A))
    counit : (B : X.Obj) → X.Hom (i*.F₀ (i!.F₀ B)) B
    unitIsTransposeIdentity : (A : Z.Obj) → unit A ≡ transpose X.id
    counitIsUntransposeIdentity : (B : X.Obj) → counit B ≡ untranspose Z.id

    unitNatural : {A A' : Z.Obj} (f : Z.Hom A A') →
      Z._∘_ (i!.F₁ (i*.F₁ f)) (unit A) ≡ Z._∘_ (unit A') f
    counitNatural : {B B' : X.Obj} (f : X.Hom B B') →
      X._∘_ f (counit B) ≡ X._∘_ (counit B') (i*.F₁ (i!.F₁ f))

    leftTriangle : (A : Z.Obj) →
      X._∘_ (counit (i*.F₀ A)) (i*.F₁ (unit A)) ≡ X.id
    rightTriangle : (B : X.Obj) →
      Z._∘_ (i!.F₁ (counit B)) (unit (i!.F₀ B)) ≡ Z.id

-- Cartier purity identifies upper shriek with derived restriction tensored by
-- the dual normal line and shifted by one.  Both directions and naturality are
-- retained; no equality of differently framed normal lines is assumed.
record CartierUpperShriekIdentification {ℓ : Level}
  (Closed Ambient : CategoryData {ℓ})
  (Adj : UpperShriekAdjunction Closed Ambient) : Type (ℓ-suc ℓ) where
  private
    module Z = CategoryData Closed
    module X = CategoryData Ambient
    module Adj = UpperShriekAdjunction Adj
    module i! = FunctorData Adj.upperShriek
  field
    derivedRestriction : FunctorData Ambient Closed
    DualNormalLine Shift : Type ℓ
    dualNormal : DualNormalLine
    minusOne : Shift
    tensorNormalShift : Z.Obj → DualNormalLine → Shift → Z.Obj

  private
    module Li* = FunctorData derivedRestriction

  field
    purity : (B : X.Obj) →
      Z.Hom (i!.F₀ B) (tensorNormalShift (Li*.F₀ B) dualNormal minusOne)
    purityInverse : (B : X.Obj) →
      Z.Hom (tensorNormalShift (Li*.F₀ B) dualNormal minusOne) (i!.F₀ B)
    puritySection : (B : X.Obj) →
      Z._∘_ (purityInverse B) (purity B) ≡ Z.id
    purityRetraction : (B : X.Obj) →
      Z._∘_ (purity B) (purityInverse B) ≡ Z.id

    tensorNormalMap : {B B' : X.Obj} → X.Hom B B' →
      Z.Hom (tensorNormalShift (Li*.F₀ B) dualNormal minusOne)
            (tensorNormalShift (Li*.F₀ B') dualNormal minusOne)
    purityNatural : {B B' : X.Obj} (f : X.Hom B B') →
      Z._∘_ (tensorNormalMap f) (purity B) ≡
      Z._∘_ (purity B') (i!.F₁ f)

record CartierUpperShriekCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    closedCategory ambientCategory : CategoryData {ℓ}
    adjunction : UpperShriekAdjunction closedCategory ambientCategory
    cartierIdentification :
      CartierUpperShriekIdentification closedCategory ambientCategory adjunction
