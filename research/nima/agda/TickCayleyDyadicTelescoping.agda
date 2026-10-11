{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyDyadicTelescoping where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc; min)
import Cubical.Data.Nat.Order as NO
import Cubical.Data.Empty as Empty
open import Cubical.Data.Rationals as Q hiding (min)
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate using (one-half)
open import RegularCauchyStructure using (precision; precision-nonnegative; precision-antitone)
open import DyadicallyBoundedCauchy using (dyadicNat)
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-value-magnitude)
open import TickRotationDefectTransport using (Rotor; RotorBound; _⊖_)
open import TickCayleyConcreteTransport using (gridInvariant)
open import TickCayleyInvariantStep using (invariantCoefficient; invariant-step-bound)
open import TickCayleyInvariantRepresentation using (invariant-representation)
open import TickCayleyDyadicMesh
open import TickCayleyGridIncrement using (gridValue)
open import TickCompletionTelescoping using (fine-quadratic-dyadic-partition-constant)

abstract
  min-within : (j k : ℕ) → NO._≤_ j k → min j k ≡ j
  min-within zero k h = refl
  min-within (suc j) zero h = Empty.rec (NO.¬-<-zero h)
  min-within (suc j) (suc k) h = cong suc (min-within j k (NO.pred-≤-pred h))

zero-small : MagnitudeBound (gridValue zero zero) one-half
zero-small = nonnegative-value-magnitude 0 one-half (isRefl≤ 0) (precision-nonnegative 1) (precision-nonnegative 1)

module Partition (N d : ℕ) (h : MagnitudeBound (gridValue N d) one-half) where
  at : (n j : ℕ) → NO._≤_ j (dyadicNat n) → Rotor
  at n j hj = gridInvariant (j N.· N) (meshDenominator n d) (mesh-small N d h n j hj)
  grid : ℕ → ℕ → Rotor
  grid n j = at n (min j (dyadicNat n)) NO.min-≤-right

  abstract
    grid-within : (n j : ℕ) (hj : NO._≤_ j (dyadicNat n)) → grid n j ≡ at n j hj
    grid-within n j hj = invariant-representation
      ((min j (dyadicNat n)) N.· N) (meshDenominator n d) (j N.· N) (meshDenominator n d)
      (mesh-small N d h n (min j (dyadicNat n)) NO.min-≤-right) (mesh-small N d h n j hj)
      (cong (meshPoint N d n) (min-within j (dyadicNat n) hj))

    first : (n : ℕ) → grid n zero ≡ gridInvariant zero zero zero-small
    first n = grid-within n zero NO.zero-≤ ∙ invariant-representation
      (zero N.· N) (meshDenominator n d) zero zero (mesh-small N d h n zero NO.zero-≤) zero-small (mesh-first N d n)

    last : (n : ℕ) → grid n (dyadicNat n) ≡ gridInvariant N d h
    last n = grid-within n (dyadicNat n) NO.≤-refl ∙ invariant-representation
      ((dyadicNat n) N.· N) (meshDenominator n d) N d (mesh-small N d h n (dyadicNat n) NO.≤-refl) h (mesh-last N d n)

    local : (n j : ℕ) → NO._≤_ 6 n → NO._<_ j (dyadicNat n) →
      RotorBound (grid n (suc j) ⊖ grid n j) (invariantCoefficient Q.· (precision n Q.· precision n))
    local n j fine hj = subst (λ z → RotorBound z (invariantCoefficient Q.· (precision n Q.· precision n)))
      (cong₂ _⊖_ (sym (grid-within n (suc j) hj)) (sym (grid-within n j (NO.≤-trans NO.≤-sucℕ hj))))
      (invariant-step-bound (j N.· N) ((suc j) N.· N) (meshDenominator n d) (precision n)
        (mesh-small N d h n j (NO.≤-trans NO.≤-sucℕ hj)) (mesh-small N d h n (suc j) hj)
        (precision-nonnegative n) (precision-antitone 6 n fine) (mesh-step-bound N d h n j))


