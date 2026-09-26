{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverInternalRestriction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Sum.Base using (inl; inr)
open import Cubical.Data.Unit.Base using (tt)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (squash₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
import ObserverInternalInterface as O
import ObserverAccessClassification as A
import ObserverNonuniqueHistory as H

-- First-order transformations: no constructor contains a reply callback.
data Restrict : O.Code → O.Code → Type where
  identity : {c : O.Code} → Restrict c c
  discard : {c : O.Code} → Restrict c O.result
  left : {c d : O.Code} → Restrict (O.both c d) c
  right : {c d : O.Code} → Restrict (O.both c d) d
  pair : {c d e : O.Code} → Restrict c d → Restrict c e → Restrict c (O.both d e)
  then : {c d e : O.Code} → Restrict c d → Restrict d e → Restrict c e

run : {c d : O.Code} → Restrict c d → O.Reply c → O.Reply d
run identity x = x
run discard x = tt
run left x = fst x
run right x = snd x
run (pair r s) x = run r x , run s x
run (then r s) x = run s (run r x)

preserves : {c d : O.Code} (r : Restrict c d) (h : H.History)
  → run r (O.readout c h) ≡ O.readout d h
preserves identity h = refl
preserves discard h = refl
preserves left h = refl
preserves right h = refl
preserves (pair r s) h i = preserves r h i , preserves s h i
preserves (then r s) h = cong (run s) (preserves r h) ∙ preserves s h

image-map : {c d : O.Code} → Restrict c d → A.Image c → A.Image d
image-map r (x , origin) = run r x , Trunc.map
  (λ { (h , e) → h , sym (preserves r h) ∙ cong (run r) e }) origin

-- All parallel restrictions agree ON admissible replies, even when their
-- syntax and behavior on impossible raw replies differ.
coherent : {c d : O.Code} (r s : Restrict c d) (q : A.Image c)
  → image-map r q ≡ image-map s q
coherent {d = d} r s q = Σ≡Prop (λ _ → squash₁)
  (Trunc.rec (A.reply-set d _ _) (λ { (h , e) →
    cong (run r) (sym e) ∙ preserves r h ∙ sym (preserves s h) ∙ cong (run s) e }) (snd q))

image-identity : {c : O.Code} (q : A.Image c) → image-map identity q ≡ q
image-identity q = Σ≡Prop (λ _ → squash₁) refl

image-composition : {c d e : O.Code} (r : Restrict c d) (s : Restrict d e) (q : A.Image c)
  → image-map (then r s) q ≡ image-map s (image-map r q)
image-composition r s q = Σ≡Prop (λ _ → squash₁) refl

select-rule : {c : O.Code} → O.RuleAccess c → Restrict c O.rule
select-rule O.here = identity
select-rule (O.on-left a) = then left (select-rule a)
select-rule (O.on-right a) = then right (select-rule a)

absurd : {X : Type} → ⊥ → X
absurd ()

-- Necessity: a restriction cannot create rule-sensitive access.
transfer-access : {c d : O.Code} → Restrict c d → O.RuleAccess d → O.RuleAccess c
transfer-access {c} r access with A.classify c
... | inr a = a
... | inl a = absurd (O.no-result-only-recovery a (λ x → O.recover access (run r x))
  (λ h → cong (O.recover access) (preserves r h) ∙ O.faithful access h))

-- Sufficiency: compile the capability implication into structural syntax.
-- The resulting restriction contains no function field.
build : {c : O.Code} (d : O.Code) → (O.RuleAccess d → O.RuleAccess c) → Restrict c d
build O.result capability = discard
build O.rule capability = select-rule (capability O.here)
build (O.both d e) capability = pair
  (build d (λ a → capability (O.on-left a)))
  (build e (λ a → capability (O.on-right a)))

no-information-gain : Restrict O.result O.rule → ⊥
no-information-gain r = A.exclusive O.just-result (transfer-access r O.here)

-- Projection choice is observable outside the admissible image.
raw-projections-differ :
  run (left {O.rule} {O.rule}) (true , false)
    ≡ run (right {O.rule} {O.rule}) (true , false) → ⊥
raw-projections-differ = true≢false

admissible-projections-agree : (q : A.Image (O.both O.rule O.rule))
  → image-map left q ≡ image-map right q
admissible-projections-agree = coherent left right
