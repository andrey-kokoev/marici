{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverDirectionRecords where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (pathToEquiv)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)

-- Comparison evidence yields an equivalence, not a privileged clock arrow.
comparison-equiv : {X : Type} (F : X → Type) {x y : X}
  → x ≡ y → F x ≃ F y
comparison-equiv F p = pathToEquiv (cong F p)

module Information {X : Type} where
  -- g contains no more discriminating information than f when it can
  -- be obtained by postprocessing f. This is not temporal precedence.
  Factors : {A B : Type} → (X → A) → (X → B) → Type
  Factors {A} {B} f g = Σ (A → B) (λ post → (x : X) → post (f x) ≡ g x)

  factors-id : {A : Type} (f : X → A) → Factors f f
  factors-id f = (λ a → a) , (λ _ → refl)

  factors-compose : {A B C : Type} {f : X → A} {g : X → B} {h : X → C}
    → Factors f g → Factors g h → Factors f h
  factors-compose (post , p) (next , q) =
    (λ a → next (post a)) , (λ x → cong next (p x) ∙ q x)

  distinctions-cannot-return : {A B : Type} {f : X → A} {g : X → B}
    → Factors f g → {x y : X} → f x ≡ f y → g x ≡ g y
  distinctions-cannot-return (post , p) {x} {y} e = sym (p x) ∙ cong post e ∙ p y

module Records {X Y : Type} (observe : X → Y) where
  -- Retain the source witness AND its relation to the visible output.
  -- This is a logical lossless refinement, not a physical storage claim.
  Recorded = Σ Y (λ y → Σ X (λ x → observe x ≡ y))

  retain : X → Recorded
  retain x = observe x , x , refl

  recover : Recorded → X
  recover (_ , x , _) = x

  source-roundtrip : (x : X) → recover (retain x) ≡ x
  source-roundtrip x = refl

  record-roundtrip : (r : Recorded) → retain (recover r) ≡ r
  record-roundtrip (y , x , e) i = e i , x , (λ j → e (i ∧ j))

  lossless : X ≃ Recorded
  lossless = isoToEquiv (iso retain recover record-roundtrip source-roundtrip)

  visible : Recorded → Y
  visible = fst

  same-visible-result : (x : X) → visible (retain x) ≡ observe x
  same-visible-result x = refl

module StrictLoss where
  fine : Bool → Bool
  fine b = b
  coarse : Bool → Unit
  coarse _ = tt
  open Information {X = Bool}

  loses : Factors fine coarse
  loses = (λ _ → tt) , (λ _ → refl)

  cannot-restore : Factors coarse fine → ⊥
  cannot-restore (post , exact) = true≢false (sym (exact true) ∙ exact false)

  -- Both output spaces are inhabited. Positivity alone does not tell
  -- whether an observation distinguishes or loses the source bit.
  fine-inhabited : Bool
  fine-inhabited = true
  coarse-inhabited : Unit
  coarse-inhabited = tt

  module R = Records coarse
  records-still-distinguish : R.retain true ≡ R.retain false → ⊥
  records-still-distinguish eq = true≢false (cong R.recover eq)

  visible-records-agree : R.visible (R.retain true) ≡ R.visible (R.retain false)
  visible-records-agree = refl
