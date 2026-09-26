{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverAccessClassification where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isSetΣ)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (isSetBool; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Empty.Properties using (isProp⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
import ObserverInternalInterface as O
import ObserverNonuniqueHistory as H

-- A total structural decision, retaining an access witness.
classify : (c : O.Code) → O.ResultOnly c ⊎ O.RuleAccess c
classify O.result = inl O.just-result
classify O.rule = inr O.here
classify (O.both c d) with classify c | classify d
... | inl a | inl b = inl (O.combine-results a b)
... | inl a | inr b = inr (O.on-right b)
... | inr a | _ = inr (O.on-left a)

exclusive : {c : O.Code} → O.ResultOnly c → O.RuleAccess c → ⊥
exclusive {c} a b = O.no-result-only-recovery a (O.recover {c} b) (O.faithful b)

reply-set : (c : O.Code) → isSet (O.Reply c)
reply-set O.result = isProp→isSet (λ _ _ → refl)
reply-set O.rule = isSetBool
reply-set (O.both c d) = isSetΣ (reply-set c) (λ _ → reply-set d)

-- Truncate origin membership, NOT the reply or its equality structure.
Admissible : (c : O.Code) → O.Reply c → Type
Admissible c r = ∥ Σ H.History (λ h → O.readout c h ≡ r) ∥₁

Image : O.Code → Type
Image c = Σ (O.Reply c) (Admissible c)

embed : (c : O.Code) → H.History → Image c
embed c h = O.readout c h , ∣ h , refl ∣₁

result-contract : {c : O.Code} → O.ResultOnly c → (q : Image c) → embed c H.red-history ≡ q
result-contract {c} a q = Σ≡Prop (λ _ → squash₁)
  (Trunc.rec (reply-set c _ _) (λ { (h , e) → O.noninterference a H.red-history h ∙ e }) (snd q))

result-image : {c : O.Code} → O.ResultOnly c → Image c ≃ Unit
result-image a = isoToEquiv (iso (λ _ → tt) (λ _ → embed _ H.red-history)
  (λ _ → refl) (result-contract a))

rule-roundtrip : {c : O.Code} (a : O.RuleAccess c) (q : Image c)
  → embed c (O.recover a (fst q)) ≡ q
rule-roundtrip {c} a q = Σ≡Prop (λ _ → squash₁)
  (Trunc.rec (reply-set c _ _)
    (λ { (h , e) → cong (λ r → O.readout c (O.recover a r)) (sym e)
      ∙ cong (O.readout c) (O.faithful a h) ∙ e }) (snd q))

rule-image-history : {c : O.Code} → O.RuleAccess c → Image c ≃ H.History
rule-image-history {c} a = isoToEquiv (iso (λ q → O.recover a (fst q)) (embed c)
  (O.faithful a) (rule-roundtrip a))

rule-image : {c : O.Code} → O.RuleAccess c → Image c ≃ Bool
rule-image a = compEquiv (rule-image-history a) H.history-equiv-bit

-- Exhaustive normalization for the current finite history fixture.
Normal : O.Code → Type
Normal c with classify c
... | inl _ = Unit
... | inr _ = Bool

normalize : (c : O.Code) → Image c ≃ Normal c
normalize c with classify c
... | inl a = result-image a
... | inr a = rule-image a

-- Repeated access shares ONE underlying history; arbitrary independent
-- reply pairs are not necessarily manifestations of that history.
duplicate-rule : Image (O.both O.rule O.rule) ≃ Bool
duplicate-rule = rule-image (O.on-left O.here)

inconsistent-duplicate : Admissible (O.both O.rule O.rule) (true , false) → ⊥
inconsistent-duplicate = Trunc.rec isProp⊥
  (λ { (h , e) → true≢false (sym (cong fst e) ∙ cong snd e) })
