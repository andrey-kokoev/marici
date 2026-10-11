{-# OPTIONS --safe --cubical --guardedness #-}
module TickRotorTelescoping where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure using (precision)
open import DyadicallyBoundedCauchy using (dyadicNat)
open import TickRotationDefectTransport using (Rotor; RotorBound; _⊖_)
open import TickCompletionTelescoping using (fine-quadratic-dyadic-partition-constant)

abstract
  rotor-fine-partition-constant : (a b : Rotor) (grid : ℕ → ℕ → Rotor) (L : Q.ℚ) (depth : ℕ) →
    ((n : ℕ) → grid n zero ≡ a) → ((n : ℕ) → grid n (dyadicNat n) ≡ b) →
    ((n j : ℕ) → NO._≤_ depth n → NO._<_ j (dyadicNat n) →
      RotorBound (grid n (suc j) ⊖ grid n j) (L Q.· (precision n Q.· precision n))) → a ≡ b
  rotor-fine-partition-constant a b grid L depth first last local = cong₂ _,_
    (fine-quadratic-dyadic-partition-constant (fst a) (fst b) (λ n j → fst (grid n j)) L depth
      (λ n → cong fst (first n)) (λ n → cong fst (last n)) (λ n j hn hj → fst (local n j hn hj)))
    (fine-quadratic-dyadic-partition-constant (snd a) (snd b) (λ n j → snd (grid n j)) L depth
      (λ n → cong snd (first n)) (λ n → cong snd (last n)) (λ n j hn hj → snd (local n j hn hj)))
