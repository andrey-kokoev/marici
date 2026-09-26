{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverAnchoredRecords where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Data.Sigma.Base using (Σ; _,_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import ObserverInternalComparison as C
import IndexIdentityCoherenceRegression as Cover

Fibre : C.Reply → Type
Fibre = C.Ix.Fibre Cover.F

-- Retain the actual comparison and the value in its endpoint fibre.
Record : Type
Record = Σ C.Reply (λ y → Σ (C.base ≡ y) (λ _ → Fibre y))

embed : Bool → Record
embed b = C.base , refl , b

anchor : Record → Bool
anchor (y , p , value) = subst Fibre (sym p) value

anchor-embed : (b : Bool) → anchor (embed b) ≡ b
anchor-embed b = substRefl {B = Fibre} {x = C.base} b

embed-anchor : (r : Record) → embed (anchor r) ≡ r
embed-anchor (y , p , value) =
  J (λ y p → (v : Fibre y) → embed (subst Fibre (sym p) v) ≡ (y , p , v))
    (λ v → cong embed (substRefl {B = Fibre} {x = C.base} v)) p value

record-equiv-anchor : Record ≃ Bool
record-equiv-anchor = isoToEquiv (iso anchor embed anchor-embed embed-anchor)

move : {y : C.Reply} → C.base ≡ y → Bool → Record
move {y} p b = y , p , subst Fibre p b

move-preserves-record : {y : C.Reply} (p : C.base ≡ y) (b : Bool)
  → embed b ≡ move p b
move-preserves-record p b = J
  (λ y p → embed b ≡ (y , p , subst Fibre p b))
  (cong embed (sym (substRefl {B = Fibre} {x = C.base} b))) p

move-preserves-anchor : {y : C.Reply} (p : C.base ≡ y) (b : Bool)
  → anchor (move p b) ≡ b
move-preserves-anchor p b = sym (cong anchor (move-preserves-record p b)) ∙ anchor-embed b

-- First-order comparison codes select transport; no arbitrary callback.
manifest : C.ComparisonCode → Bool → Record
manifest c b = move (C.interpret c) b

manifest-faithful : (c : C.ComparisonCode) (b : Bool) → anchor (manifest c b) ≡ b
manifest-faithful c b = move-preserves-anchor (C.interpret c) b

turned-false held-true : Record
turned-false = C.base , C.interpret C.turn , false
held-true = C.base , C.interpret C.turn , true

-- true at the anchor and false after the turn are the SAME record
-- up to its appropriate dependent path, not distinct anchored values.
coherent-presentations : embed true ≡ turned-false
coherent-presentations = move-preserves-record (C.interpret C.turn) true
  ∙ cong {B = λ _ → Record} (λ v → C.base , C.interpret C.turn , v) C.turn-read

-- Holding the visible Bool true while changing its comparison instead
-- represents the OTHER anchored value.
other-anchor : embed false ≡ held-true
other-anchor = move-preserves-record (C.interpret C.turn) false
  ∙ cong {B = λ _ → Record} (λ v → C.base , C.interpret C.turn , v) (uaβ notEquiv false)

held-value-distinct : embed true ≡ held-true → ⊥
held-value-distinct e = true≢false
  (sym (anchor-embed true) ∙ cong anchor e
    ∙ sym (cong anchor other-anchor) ∙ anchor-embed false)
