{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyAddition where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Tactics.CommRingSolver
open import Cubical.Algebra.CommRing
open import RationalAnalyticSubstrate

open CommRingStr (snd PreferredℚCommRing) renaming (_+_ to _+R_)
open import RegularCauchyStructure

module AdditiveRearrangement {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_)

  rearrange : (a b u v : fst R) →
    ((a +S u) +S v) +S ((b +S u) +S v) ≡
    ((a +S b) +S (u +S u)) +S (v +S v)
  rearrange a b u v = solve! R

combine-refined-errors : (a b : Q.ℚ) (m n : ℕ) →
  ((a +R precision (suc m)) +R precision (suc n)) +R
  ((b +R precision (suc m)) +R precision (suc n))
  ≡ ((a +R b) +R precision m) +R precision n
combine-refined-errors a b m n =
  AdditiveRearrangement.rearrange PreferredℚCommRing
    a b (precision (suc m)) (precision (suc n)) ∙
  cong₂ (λ u v → ((a +R b) +R u) +R v)
    (precision-refines-double m)
    (precision-refines-double n)

-- Binary addition refines each input by one approximation depth so the two
-- input error budgets contract back to the output budget.
addRegular : RegularCauchy → RegularCauchy → RegularCauchy
addRegular x y .approximation n =
  approximation x (suc n) Q.+ approximation y (suc n)
addRegular x y .close-forward m n =
  subst
    (λ z →
      approximation x (suc m) Q.+ approximation y (suc m) ≤ z)
    (combine-refined-errors
      (approximation x (suc n)) (approximation y (suc n)) m n)
    (≤Monotone+
      (approximation x (suc m))
      ((approximation x (suc n) Q.+ precision (suc m)) Q.+ precision (suc n))
      (approximation y (suc m))
      ((approximation y (suc n) Q.+ precision (suc m)) Q.+ precision (suc n))
      (close-forward x (suc m) (suc n))
      (close-forward y (suc m) (suc n)))
addRegular x y .close-backward m n =
  subst
    (λ z →
      approximation x (suc n) Q.+ approximation y (suc n) ≤ z)
    (combine-refined-errors
      (approximation x (suc m)) (approximation y (suc m)) m n)
    (≤Monotone+
      (approximation x (suc n))
      ((approximation x (suc m) Q.+ precision (suc m)) Q.+ precision (suc n))
      (approximation y (suc n))
      ((approximation y (suc m) Q.+ precision (suc m)) Q.+ precision (suc n))
      (close-backward x (suc m) (suc n))
      (close-backward y (suc m) (suc n)))
