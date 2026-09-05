{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyNegation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients.Properties using (setQuotUnaryOp)
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyMetricEquivalence

module NegationRearrangement {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  left-path : (a b : fst R) → a +S ((-S a) +S (-S b)) ≡ -S b
  left-path a b = solve! R

  right-path : (a b e₁ e₂ : fst R) →
    ((b +S e₁) +S e₂) +S ((-S a) +S (-S b)) ≡
    (((-S a) +S e₁) +S e₂)
  right-path a b e₁ e₂ = solve! R

negate-two-error-bound : (a b e₁ e₂ : Q.ℚ) →
  a ≤ (b Q.+ e₁) Q.+ e₂ →
  Q.- b ≤ (Q.- a Q.+ e₁) Q.+ e₂
negate-two-error-bound a b e₁ e₂ a≤b+e₁+e₂ =
  subst2 _≤_
    (NegationRearrangement.left-path PreferredℚCommRing a b)
    (NegationRearrangement.right-path PreferredℚCommRing a b e₁ e₂)
    (≤-+o a ((b Q.+ e₁) Q.+ e₂) (Q.- a Q.+ Q.- b)
      a≤b+e₁+e₂)

negate-one-error-bound : (a b e : Q.ℚ) →
  a ≤ b Q.+ e → Q.- b ≤ Q.- a Q.+ e
negate-one-error-bound a b e a≤b+e =
  subst (λ z → Q.- b ≤ z) (Q.+IdR (Q.- a Q.+ e))
    (negate-two-error-bound a b e 0
      (subst (a ≤_) (sym (Q.+IdR (b Q.+ e))) a≤b+e))

negateRegular : RegularCauchy → RegularCauchy
negateRegular x .approximation n = Q.- approximation x n
negateRegular x .close-forward m n =
  negate-two-error-bound
    (approximation x n) (approximation x m)
    (precision m) (precision n)
    (close-backward x m n)
negateRegular x .close-backward m n =
  negate-two-error-bound
    (approximation x m) (approximation x n)
    (precision m) (precision n)
    (close-forward x m n)

negateRegular-cong : (x y : RegularCauchy) →
  x ≈metric y → negateRegular x ≈metric negateRegular y
negateRegular-cong x y r k = PT.map
  (λ { (N , bounds) → N , λ n N≤n →
    negate-one-error-bound
      (approximation y n) (approximation x n) (precision k)
      (snd (bounds n N≤n)) ,
    negate-one-error-bound
      (approximation x n) (approximation y n) (precision k)
      (fst (bounds n N≤n)) })
  (r k)

-completion_ : MetricCompletionCandidate → MetricCompletionCandidate
-completion_ = setQuotUnaryOp negateRegular negateRegular-cong
