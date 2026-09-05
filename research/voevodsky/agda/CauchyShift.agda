{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyShift where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence

shift-error≤ : (k n : ℕ) → ℕOrder._≤_ (suc k) n →
  precision n Q.+ precision (suc n) ≤ precision k
shift-error≤ k n sk≤n =
  subst (precision n Q.+ precision (suc n) ≤_)
    (precision-refines-double k)
    (≤Monotone+
      (precision n) (precision (suc k))
      (precision (suc n)) (precision (suc k))
      (precision-antitone (suc k) n sk≤n)
      (precision-antitone (suc k) (suc n)
        (ℕOrder.≤-trans sk≤n ℕOrder.≤-sucℕ)))

tighten-two-errors : (a b e₁ e₂ e : Q.ℚ) →
  e₁ Q.+ e₂ ≤ e →
  a ≤ (b Q.+ e₁) Q.+ e₂ →
  a ≤ b Q.+ e
tighten-two-errors a b e₁ e₂ e e₁+e₂≤e a≤b+e₁+e₂ =
  isTrans≤ a ((b Q.+ e₁) Q.+ e₂) (b Q.+ e)
    a≤b+e₁+e₂
    (subst (λ z → z ≤ b Q.+ e) (Q.+Assoc b e₁ e₂)
      (≤-o+ (e₁ Q.+ e₂) e b e₁+e₂≤e))

loosen-two-errors : (a b e₁ e₂ E₁ E₂ : Q.ℚ) →
  e₁ ≤ E₁ → e₂ ≤ E₂ →
  a ≤ (b Q.+ e₁) Q.+ e₂ →
  a ≤ (b Q.+ E₁) Q.+ E₂
loosen-two-errors a b e₁ e₂ E₁ E₂ e₁≤E₁ e₂≤E₂ bound =
  isTrans≤ a ((b Q.+ e₁) Q.+ e₂) ((b Q.+ E₁) Q.+ E₂)
    bound
    (≤Monotone+ (b Q.+ e₁) (b Q.+ E₁) e₂ E₂
      (≤-o+ e₁ E₁ b e₁≤E₁) e₂≤E₂)

shiftRegular : RegularCauchy → RegularCauchy
shiftRegular x .approximation n = approximation x (suc n)
shiftRegular x .close-forward m n =
  loosen-two-errors
    (approximation x (suc m)) (approximation x (suc n))
    (precision (suc m)) (precision (suc n))
    (precision m) (precision n)
    (precision-step≤ m) (precision-step≤ n)
    (close-forward x (suc m) (suc n))
shiftRegular x .close-backward m n =
  loosen-two-errors
    (approximation x (suc n)) (approximation x (suc m))
    (precision (suc m)) (precision (suc n))
    (precision m) (precision n)
    (precision-step≤ m) (precision-step≤ n)
    (close-backward x (suc m) (suc n))

shift-equivalent : (x : RegularCauchy) → shiftRegular x ≈metric x
shift-equivalent x k =
  ∣ (suc k , λ n sk≤n →
    tighten-two-errors
      (approximation x (suc n)) (approximation x n)
      (precision n) (precision (suc n)) (precision k)
      (shift-error≤ k n sk≤n)
      (close-backward x n (suc n)) ,
    tighten-two-errors
      (approximation x n) (approximation x (suc n))
      (precision n) (precision (suc n)) (precision k)
      (shift-error≤ k n sk≤n)
      (close-forward x n (suc n))) ∣₁

iterateShift : ℕ → RegularCauchy → RegularCauchy
iterateShift zero x = x
iterateShift (suc d) x = shiftRegular (iterateShift d x)

iterateShift-approximation : (d n : ℕ) (x : RegularCauchy) →
  approximation (iterateShift d x) n ≡ approximation x (d ℕ.+ n)
iterateShift-approximation zero n x = refl
iterateShift-approximation (suc d) n x =
  iterateShift-approximation d (suc n) x ∙
  cong (approximation x) (ℕ.+-suc d n)

iterateShift-equivalent : (d : ℕ) (x : RegularCauchy) →
  iterateShift d x ≈metric x
iterateShift-equivalent zero x = ≈metric-refl x
iterateShift-equivalent (suc d) x =
  ≈metric-trans
    (iterateShift (suc d) x) (iterateShift d x) x
    (shift-equivalent (iterateShift d x))
    (iterateShift-equivalent d x)

iterateShift-choice-independent : (d e : ℕ) (x : RegularCauchy) →
  iterateShift d x ≈metric iterateShift e x
iterateShift-choice-independent d e x =
  ≈metric-trans
    (iterateShift d x) x (iterateShift e x)
    (iterateShift-equivalent d x)
    (≈metric-sym (iterateShift e x) x (iterateShift-equivalent e x))
