{-# OPTIONS --safe --cubical --guardedness #-}
module SeedFirstReturnActions where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sigma.Base using (_×_)
open import ActualSeedEndpointTable
open import SeedSeamPathComparisonBoundary

-- Canonical action on retained free histories, not on physical payloads.
append : {s m t : Vertex} → Path s m → Path m t → Path s t
append stop q = q
append (step e p) q = step e (append p q)

History : Vertex → Type
History v = Path A v

advance : (e : Occurrence) → History (source e) → History (target e)
advance e h = append h (step e stop)

out-AB : History A → History B
out-AB = advance AB
out-AD : History A → History D
out-AD = advance AD
in-BA : History B → History A
in-BA = advance BA
in-CA : History C → History A
in-CA = advance CA

r00 r01 r10 r11 : History A
r00 = append x0 y0
r01 = append x0 y1
r10 = append x1 y0
r11 = append x1 y1

execution-00 : in-BA (out-AB stop) ≡ r00
execution-00 = refl
execution-01 : in-CA (advance BC (out-AB stop)) ≡ r01
execution-01 = refl
execution-10 : in-BA (advance DB (out-AD stop)) ≡ r10
execution-10 = refl
execution-11 : in-CA (advance BC (advance DB (out-AD stop))) ≡ r11
execution-11 = refl

is-AB : Occurrence → Bool
is-AB AB = true
is-AB BC = false
is-AB CA = false
is-AB AD = false
is-AB DB = false
is-AB BA = false
starts-AB : {s t : Vertex} → Path s t → Bool
starts-AB stop = false
starts-AB (step e p) = is-AB e
is-two is-three : ℕ → Bool
is-two 0 = false
is-two (suc 0) = false
is-two (suc (suc 0)) = true
is-two (suc (suc (suc n))) = false
is-three 0 = false
is-three (suc 0) = false
is-three (suc (suc 0)) = false
is-three (suc (suc (suc 0))) = true
is-three (suc (suc (suc (suc n)))) = false

distinct-00-01 : r00 ≡ r01 → ⊥
distinct-00-01 p = true≢false (cong (λ h → is-two (length h)) p)
distinct-00-10 : r00 ≡ r10 → ⊥
distinct-00-10 p = true≢false (cong starts-AB p)
distinct-00-11 : r00 ≡ r11 → ⊥
distinct-00-11 p = true≢false (cong starts-AB p)
distinct-01-10 : r01 ≡ r10 → ⊥
distinct-01-10 p = true≢false (cong starts-AB p)
distinct-01-11 : r01 ≡ r11 → ⊥
distinct-01-11 p = true≢false (cong starts-AB p)
distinct-10-11 : r10 ≡ r11 → ⊥
distinct-10-11 p = true≢false (cong (λ h → is-three (length h)) p)

-- An effect interpretation is additional data. Preserve its history separately.
module Effects (X : Vertex → Type)
  (act : (e : Occurrence) → X (source e) → X (target e)) where
  Retained : Vertex → Type
  Retained v = History v × X v

  advance-retained : (e : Occurrence) → Retained (source e) → Retained (target e)
  advance-retained e (h , a) = advance e h , act e a

  run : {s t : Vertex} → Path s t → X s → X t
  run stop a = a
  run (step e p) a = run p (act e a)

  run-append : {s m t : Vertex} (p : Path s m) (q : Path m t) (a : X s)
    → run (append p q) a ≡ run q (run p a)
  run-append stop q a = refl
  run-append (step e p) q a = run-append p q (act e a)

  returned : (p : History A) → X A → Retained A
  returned p a = p , run p a

  -- These are exact next witness types, not fields inferred from endpoints.
  ForwardEffectComparison ReturnEffectComparison : Type
  ForwardEffectComparison = (a : X A) → run x0 a ≡ run x1 a
  ReturnEffectComparison = (b : X B) → run y0 b ≡ run y1 b

  module WithComparisons (α : ForwardEffectComparison) (β : ReturnEffectComparison) where
    compare-00-10 : (a : X A) → run r00 a ≡ run r10 a
    compare-00-10 a = cong (run y0) (α a)
    compare-00-01 : (a : X A) → run r00 a ≡ run r01 a
    compare-00-01 a = β (run x0 a)
    compare-10-11 : (a : X A) → run r10 a ≡ run r11 a
    compare-10-11 a = β (run x1 a)
    compare-01-11 : (a : X A) → run r01 a ≡ run r11 a
    compare-01-11 a = cong (run y1) (α a)

    -- The pointwise return witness supplies the mixed square, conditional on
    -- BOTH witnesses. Its boundaries are the four comparisons above.
    mixed : (a : X A) → I → I → X A
    mixed a i j = β (α a i) j
    mixed-bottom : (a : X A) → (λ i → mixed a i i0) ≡ compare-00-10 a
    mixed-bottom a = refl
    mixed-top : (a : X A) → (λ i → mixed a i i1) ≡ compare-01-11 a
    mixed-top a = refl
    mixed-left : (a : X A) → (λ j → mixed a i0 j) ≡ compare-00-01 a
    mixed-left a = refl
    mixed-right : (a : X A) → (λ j → mixed a i1 j) ≡ compare-10-11 a
    mixed-right a = refl

  -- Equal effect values never imply equality of the complete retained states.
  retained-01-10-distinct : (a : X A) → returned r01 a ≡ returned r10 a → ⊥
  retained-01-10-distinct a p = distinct-01-10 (cong fst p)

-- Control: a deliberately trivial supplied interpretation has equal effects,
-- while the retained histories remain different. This is not a physical model.
module Trivial = Effects (λ _ → Unit) (λ _ a → a)
trivial-forward : Trivial.ForwardEffectComparison
trivial-forward a = refl
trivial-return : Trivial.ReturnEffectComparison
trivial-return a = refl
