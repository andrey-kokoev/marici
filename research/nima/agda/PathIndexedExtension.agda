{-# OPTIONS --safe --cubical --guardedness #-}
module PathIndexedExtension where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv; equivAdjointEquiv)
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Path using (compPathrEquiv; symIso)
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import Cubical.Foundations.HLevels using (isOfHLevelRespectEquiv)

-- Dependent path Yoneda: a value at x extends uniquely when the actual path
-- from x remains an argument. This is NOT endpoint-only extension.
module PathYoneda {ℓ : Level} (A : Type ℓ) (x : A) where
  Based : Type ℓ
  Based = Σ[ y ∈ A ] (x ≡ y)

  based-contractible : isContr Based
  based-contractible = (x , refl) , λ { (y , p) i → p i , (λ j → p (i ∧ j)) }

  Sections : {ℓ' : Level} (Y : A → Type ℓ') → Type (ℓ-max ℓ ℓ')
  Sections Y = (y : A) → (x ≡ y) → Y y

  evaluate : {ℓ' : Level} (Y : A → Type ℓ') → Sections Y → Y x
  evaluate Y f = f x refl

  extend : {ℓ' : Level} (Y : A → Type ℓ') → Y x → Sections Y
  extend Y v y p = subst Y p v

  path-yoneda-iso : {ℓ' : Level} (Y : A → Type ℓ') → Iso (Sections Y) (Y x)
  path-yoneda-iso Y = record
    { fun = evaluate Y
    ; inv = extend Y
    ; rightInv = transportRefl
    ; leftInv = λ f → funExt λ y → funExt λ p →
        J (λ y p → subst Y p (f x refl) ≡ f y p)
          (transportRefl (f x refl)) p }

  Extension : {ℓ' : Level} (Y : A → Type ℓ') (v : Y x) → Type (ℓ-max ℓ ℓ')
  Extension Y v = Σ[ f ∈ Sections Y ] (evaluate Y f ≡ v)

  unique-extension : {ℓ' : Level} (Y : A → Type ℓ') (v : Y x)
    → isContr (Extension Y v)
  unique-extension Y v = equiv-proof (snd (isoToEquiv (path-yoneda-iso Y))) v

-- Equivalence fibers are the same universal property in another description.
-- D may depend on the missing value itself, not only on the supplied horn.
module FiberYoneda {ℓX ℓY : Level} {X : Type ℓX} {Y : Type ℓY}
  (e : X ≃ Y) (target : Y) where
  center : X
  center = invEq e target

  Witness : X → Type ℓY
  Witness x = equivFun e x ≡ target

  module Based = PathYoneda X center

  witness-view : (x : X) → Witness x ≃ (center ≡ x)
  witness-view x = compEquiv (invEquiv (equivAdjointEquiv e)) (isoToEquiv symIso)

  Sections : {ℓD : Level} (D : X → Type ℓD) → Type (ℓ-max (ℓ-max ℓX ℓY) ℓD)
  Sections D = (x : X) → Witness x → D x

  section-view : {ℓD : Level} (D : X → Type ℓD) → Iso (Sections D) (Based.Sections D)
  section-view D = record
    { fun = λ f x p → f x (invEq (witness-view x) p)
    ; inv = λ g x w → g x (equivFun (witness-view x) w)
    ; rightInv = λ g → funExt λ x → funExt λ p → cong (g x) (secEq (witness-view x) p)
    ; leftInv = λ f → funExt λ x → funExt λ w → cong (f x) (retEq (witness-view x) w) }

  universal : {ℓD : Level} (D : X → Type ℓD) → Sections D ≃ D center
  universal D = compEquiv (isoToEquiv (section-view D)) (isoToEquiv (Based.path-yoneda-iso D))

  unique-extension : {ℓD : Level} (D : X → Type ℓD) (v : D center)
    → isContr (Σ[ f ∈ Sections D ] (equivFun (universal D) f ≡ v))
  unique-extension D v = equiv-proof (snd (universal D)) v

-- The residual freedom with BOTH endpoints fixed. No contractibility of the
-- ambient type, its loop space, or its fixed-endpoint path space is assumed.
module Parallel {ℓ : Level} (A : Type ℓ) (x y : A) where
  Paths Loops : Type ℓ
  Paths = x ≡ y
  Loops = x ≡ x

  coordinates : Paths → Paths ≃ Loops
  coordinates base = compPathrEquiv (sym base)

  base-normalizes : (base : Paths) → equivFun (coordinates base) base ≡ refl
  base-normalizes = rCancel

  uniqueness-criterion : (base : Paths) → isContr Paths ≃ isContr Loops
  uniqueness-criterion base = propBiimpl→Equiv isPropIsContr isPropIsContr
    (isOfHLevelRespectEquiv 0 (coordinates base))
    (isOfHLevelRespectEquiv 0 (invEquiv (coordinates base)))

  -- Comparing two actual paths is precisely nullhomotopy of their residual
  -- loop, including the comparison witness rather than just its existence.
  residual-test : (p q : Paths) → (p ≡ q) ≃ (p ∙ sym q ≡ refl)
  residual-test p q = compEquiv (congEquiv (coordinates q)) (compPathrEquiv (rCancel q))

  change-base : (base next : Paths) → Loops ≃ Loops
  change-base base next = compEquiv (invEquiv (coordinates base)) (coordinates next)

  change-base-correct : (base next p : Paths)
    → equivFun (change-base base next) (equivFun (coordinates base) p)
      ≡ equivFun (coordinates next) p
  change-base-correct base next p = cong (equivFun (coordinates next)) (retEq (coordinates base) p)
