{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedComparisonReduction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Bool.Properties using (isSetBool)
open import RetainedComparisonStructure using (Structure; example; module Example)

-- Inputs deliberately omit BOTH the right-unit and right-inverse witnesses.
module FromLeftLaws {ℓ : Level}
  (P : Type ℓ)
  (E : P → P → Type ℓ)
  (unit : {p : P} → E p p)
  (comp : {p q r : P} → E q r → E p q → E p r)
  (inv : {p q : P} → E p q → E q p)
  (unitL : {p q : P} (a : E p q) → comp unit a ≡ a)
  (assoc : {p q r s : P} (c : E r s) (b : E q r) (a : E p q)
    → comp c (comp b a) ≡ comp (comp c b) a)
  (inverseL : {p q : P} (a : E p q) → comp (inv a) a ≡ unit)
  where

  cancel-step : {p q r : P} (a : E q r) (b : E p q)
    → comp (inv a) (comp a b) ≡ b
  cancel-step a b = assoc (inv a) a b
    ∙ cong (λ h → comp h b) (inverseL a) ∙ unitL b

  cancel-left : {p q r : P} (a : E q r) (b c : E p q)
    → comp a b ≡ comp a c → b ≡ c
  cancel-left a b c eq = sym (cancel-step a b)
    ∙ cong (comp (inv a)) eq ∙ cancel-step a c

  unitR : {p q : P} (a : E p q) → comp a unit ≡ a
  unitR a = cancel-left (inv a) (comp a unit) a
    (assoc (inv a) a unit
      ∙ cong (λ h → comp h unit) (inverseL a)
      ∙ unitL unit ∙ sym (inverseL a))

  inverse-involutive : {p q : P} (a : E p q) → inv (inv a) ≡ a
  inverse-involutive a = sym (unitR (inv (inv a)))
    ∙ cong (comp (inv (inv a))) (sym (inverseL a))
    ∙ assoc (inv (inv a)) (inv a) a
    ∙ cong (λ h → comp h a) (inverseL (inv a))
    ∙ unitL a

  inverseR : {p q : P} (a : E p q) → comp a (inv a) ≡ unit
  inverseR a = sym (cong (λ h → comp h (inv a)) (inverse-involutive a))
    ∙ inverseL (inv a)

module ForStructure {ℓ : Level} (S : Structure ℓ) where
  open Structure S
  module Derived = FromLeftLaws P E idE compE invE unitLE assocE inverseLE

  -- Equality of law statements is not equality of their chosen witnesses.
  -- Set-valued E makes these proof fields unique, without identifying distinct
  -- change arrows. No set restriction is added to the original Structure.
  right-unit-agreement : ((p q : P) → isSet (E p q))
    → {p q : P} (a : E p q) → unitRE a ≡ Derived.unitR a
  right-unit-agreement homSet {p} {q} a = homSet p q _ _ _ _

  right-inverse-agreement : ((p q : P) → isSet (E p q))
    → {p q : P} (a : E p q) → inverseRE a ≡ Derived.inverseR a
  right-inverse-agreement homSet {p} {q} a = homSet q q _ _ _ _

module Checked = ForStructure example

example-change-homs-are-sets : (p q : Example.P) → isSet (Example.E p q)
example-change-homs-are-sets p q = isSetΣ isSetBool (λ _ → isSetBool)

example-right-unit-recovered : {p q : Example.P} (a : Example.E p q)
  → Example.unitRE {p} {q} a ≡ Checked.Derived.unitR {p} {q} a
example-right-unit-recovered {p} {q} a =
  Checked.right-unit-agreement example-change-homs-are-sets {p} {q} a

example-right-inverse-recovered : {p q : Example.P} (a : Example.E p q)
  → Example.inverseRE {p} {q} a ≡ Checked.Derived.inverseR {p} {q} a
example-right-inverse-recovered {p} {q} a =
  Checked.right-inverse-agreement example-change-homs-are-sets {p} {q} a
