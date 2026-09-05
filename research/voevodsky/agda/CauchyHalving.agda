{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyHalving where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.SetQuotients as SQ
open import Cubical.HITs.SetQuotients.Properties using (setQuotUnaryOp)
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition
open import CauchyAdditionCongruence
open import CauchyShift
open import CauchyAdditiveLaws using (pointwise-equivalent)

half-two-error-bound : (a b e₁ e₂ : Q.ℚ) →
  a ≤ (b Q.+ e₁) Q.+ e₂ →
  halfℚ a ≤ (halfℚ b Q.+ halfℚ e₁) Q.+ halfℚ e₂
half-two-error-bound a b e₁ e₂ bound =
  subst (halfℚ a ≤_)
    (Q.·DistR+ (b Q.+ e₁) e₂ one-half ∙
     cong (λ z → z Q.+ halfℚ e₂) (Q.·DistR+ b e₁ one-half))
    (≤-·o a ((b Q.+ e₁) Q.+ e₂) one-half
      one-half-nonnegative bound)

half-one-error-bound : (a b e : Q.ℚ) →
  0 ≤ e → a ≤ b Q.+ e → halfℚ a ≤ halfℚ b Q.+ e
half-one-error-bound a b e 0≤e bound =
  isTrans≤ (halfℚ a) (halfℚ b Q.+ halfℚ e) (halfℚ b Q.+ e)
    (subst (halfℚ a ≤_)
      (Q.·DistR+ b e one-half)
      (≤-·o a (b Q.+ e) one-half one-half-nonnegative bound))
    (≤-o+ (halfℚ e) e (halfℚ b)
      (subst (halfℚ e ≤_) (half-double e)
        (≤-add-nonnegative (halfℚ e) (halfℚ e)
          (half-nonnegative e 0≤e))))

halfRegular : RegularCauchy → RegularCauchy
halfRegular x .approximation n = halfℚ (approximation x n)
halfRegular x .close-forward m n =
  loosen-two-errors
    (halfℚ (approximation x m)) (halfℚ (approximation x n))
    (precision (Cubical.Data.Nat.suc m))
    (precision (Cubical.Data.Nat.suc n))
    (precision m) (precision n)
    (precision-step≤ m) (precision-step≤ n)
    (half-two-error-bound
      (approximation x m) (approximation x n)
      (precision m) (precision n) (close-forward x m n))
halfRegular x .close-backward m n =
  loosen-two-errors
    (halfℚ (approximation x n)) (halfℚ (approximation x m))
    (precision (Cubical.Data.Nat.suc m))
    (precision (Cubical.Data.Nat.suc n))
    (precision m) (precision n)
    (precision-step≤ m) (precision-step≤ n)
    (half-two-error-bound
      (approximation x n) (approximation x m)
      (precision m) (precision n) (close-backward x m n))

halfRegular-cong : (x y : RegularCauchy) →
  x ≈metric y → halfRegular x ≈metric halfRegular y
halfRegular-cong x y r k = PT.map
  (λ { (N , bounds) → N , λ n N≤n →
    half-one-error-bound
      (approximation x n) (approximation y n) (precision k)
      (precision-nonnegative k) (fst (bounds n N≤n)) ,
    half-one-error-bound
      (approximation y n) (approximation x n) (precision k)
      (precision-nonnegative k) (snd (bounds n N≤n)) })
  (r k)

halfCompletion : MetricCompletionCandidate → MetricCompletionCandidate
halfCompletion = setQuotUnaryOp halfRegular halfRegular-cong

half-add-self : (x : RegularCauchy) →
  addRegular (halfRegular x) (halfRegular x) ≈metric x
half-add-self x =
  ≈metric-trans
    (addRegular (halfRegular x) (halfRegular x)) (shiftRegular x) x
    (pointwise-equivalent
      (addRegular (halfRegular x) (halfRegular x)) (shiftRegular x)
      (λ n → half-double
        (approximation x (Cubical.Data.Nat.suc n))))
    (shift-equivalent x)

completion-half-add-self : (x : MetricCompletionCandidate) →
  halfCompletion x +completion halfCompletion x ≡ x
completion-half-add-self = SQ.elimProp
  (λ _ → metric-candidate-isSet _ _)
  (λ x → SQ.eq/ _ _ (half-add-self x))
