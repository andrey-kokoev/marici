{-# OPTIONS --safe --cubical --guardedness #-}
module TickOperationalTrigFirstOrder where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.HITs.PropositionalTruncation as PT
open import RationalAnalyticSubstrate using (one-half; PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyProductErrorBounds using (weaken-magnitude-bound)
open import TaylorTermBounds using (nonnegative-bound-product)
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import TaylorGeometricTail
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionLimits
open import TickCompletionMagnitudeBounds
open import TickRationalProductLimits
open import TickRationalTrigAddition using (cosine-sequence-converges; sine-sequence-converges)
open import TickSmallArctangent using (small-input≤one)
open import TickAtanFirstOrderBounds using (one-magnitude; zero-magnitude)

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_)
  bound-base : (e h : fst R) → ((1r ·S e) ·S e) ·S h ≡ (e ·S e) ·S h
  bound-base e h = solve! R
  bound-step : (a h : fst R) → ((a ·S 1r) ·S 1r) ·S h ≡ a ·S h
  bound-step a h = solve! R
module P = Paths PreferredℚCommRing

advance : Q.ℚ → Q.ℚ → ℕ → ℕ → Q.ℚ
advance a q i j = Q.- ((((a Q.· q) Q.· q) Q.· reciprocalSuccessor i) Q.· reciprocalSuccessor (suc j))

advance-bound : (a A q e : Q.ℚ) (i j : ℕ) → 0 ≤ A → 0 ≤ e →
  MagnitudeBound a A → MagnitudeBound q e →
  MagnitudeBound (advance a q i j) (((A Q.· e) Q.· e) Q.· one-half)
advance-bound a A q e i j Ah eh ha hq = negate-magnitude-bound _ _
  (nonnegative-multiplier-bound _ _ (reciprocalSuccessor (suc j)) one-half
    Aeeh
    (subst (MagnitudeBound _) (Q.·IdR ((A Q.· e) Q.· e))
      (nonnegative-multiplier-bound _ _ (reciprocalSuccessor i) 1 Aeeh
        (arbitrary-multiplier-bound (a Q.· q) (A Q.· e) q e Aeh eh
          (arbitrary-multiplier-bound a A q e Ah eh ha hq) hq)
        (reciprocalSuccessor-nonnegative i) (reciprocalSuccessor≤one i)))
    (reciprocalSuccessor-nonnegative (suc j)) (reciprocalSuccessor-after-zero≤half j))
  where
  Aeh = nonnegative-bound-product A e Ah eh
  Aeeh = nonnegative-bound-product (A Q.· e) e Aeh eh

module Tail (term : Q.ℚ → ℕ → Q.ℚ) (first second : ℕ → ℕ)
  (step : (q : Q.ℚ) (n : ℕ) → term q (suc n) ≡ advance (term q n) q (first n) (second n)) where

  tail-bound : (q e : Q.ℚ) → MagnitudeBound q one-half → 0 ≤ e → MagnitudeBound q e →
    MagnitudeBound (term q zero) 1 → (n : ℕ) →
    MagnitudeBound (term q (suc n)) ((e Q.· e) Q.· precision (suc n))
  tail-bound q e hq eh he h0 zero = transport-magnitude _ _ _ (step q zero)
    (subst (MagnitudeBound _) (P.bound-base e one-half)
      (advance-bound (term q zero) 1 q e (first zero) (second zero) (precision-nonnegative zero) eh h0 he))
  tail-bound q e hq eh he h0 (suc n) = transport-magnitude _ _ _ (step q (suc n))
    (subst (MagnitudeBound _) (P.bound-step A one-half ∙ sym (Q.·Assoc (e Q.· e) (precision (suc n)) one-half))
      (advance-bound (term q (suc n)) A q 1 (first (suc n)) (second (suc n)) Ah (precision-nonnegative zero)
        (tail-bound q e hq eh he h0 n) (small-input≤one q hq)))
    where
    A = (e Q.· e) Q.· precision (suc n)
    Ah = nonnegative-bound-product (e Q.· e) (precision (suc n))
      (nonnegative-bound-product e e eh eh) (precision-nonnegative (suc n))

  sum-remainder-bound : (q e : Q.ℚ) → MagnitudeBound q one-half → 0 ≤ e → MagnitudeBound q e →
    MagnitudeBound (term q zero) 1 → (n : ℕ) →
    MagnitudeBound (finiteSum (term q) n Q.+ (Q.- term q zero)) (e Q.· e)
  sum-remainder-bound q e hq eh he h0 n = subst (MagnitudeBound _) (Q.·IdR (e Q.· e))
    (finiteSum-segment-difference-magnitude (term q) (e Q.· e) zero n
      (nonnegative-bound-product e e eh eh) (tail-bound q e hq eh he h0))

module Cos = Tail cosineTerm (λ n → n N.+ n) (λ n → n N.+ n) (λ q n → refl)
module Sin = Tail sineTerm (λ n → suc (n N.+ n)) (λ n → suc (n N.+ n)) (λ q n → refl)

-- Opaque presentations keep canonical schedules out of elaboration; these
-- class paths identify them with the implemented operational functions.
abstract
  cosineValue sineValue : Q.ℚ → MetricCompletionCandidate
  cosineValue q = completionCosine (embedMetricℚ q)
  sineValue q = completionSine (embedMetricℚ q)
  cosine-value-class : (q : Q.ℚ) → cosineValue q ≡ completionCosine (embedMetricℚ q)
  cosine-value-class q = refl
  sine-value-class : (q : Q.ℚ) → sineValue q ≡ completionSine (embedMetricℚ q)
  sine-value-class q = refl
  cosine-value-converges : (q : Q.ℚ) → Converges (λ n → embedMetricℚ (cosinePartialSum q n)) (cosineValue q)
  cosine-value-converges = cosine-sequence-converges
  sine-value-converges : (q : Q.ℚ) → Converges (λ n → embedMetricℚ (sinePartialSum q n)) (sineValue q)
  sine-value-converges = sine-sequence-converges

-- First-order estimates for the actual operational functions at embedded
-- small rational angles. These are analytic inputs to the Cayley bridge,
-- not the bridge itself and not a statement about an alternate trig backend.
cosine-value-small-remainder : (q e : Q.ℚ) → MagnitudeBound q one-half →
  0 ≤ e → MagnitudeBound q e →
  CompletionMagnitudeBound (cosineValue q +completion embedMetricℚ (Q.- 1)) (e Q.· e)
cosine-value-small-remainder q e hq eh he = rational-remainder-limit-magnitude
  (cosinePartialSum q) (cosineValue q) 1 (e Q.· e)
  (cosine-value-converges q)
  (λ k → ∣ zero , (λ n hn → weaken-magnitude-bound _ (e Q.· e) ((e Q.· e) Q.+ precision k)
    (≤-add-nonnegative (e Q.· e) (precision k) (precision-nonnegative k))
    (Cos.sum-remainder-bound q e hq eh he one-magnitude n)) ∣₁)

sine-value-small-remainder : (q e : Q.ℚ) → MagnitudeBound q one-half →
  0 ≤ e → MagnitudeBound q e →
  CompletionMagnitudeBound (sineValue q +completion embedMetricℚ (Q.- q)) (e Q.· e)
sine-value-small-remainder q e hq eh he = rational-remainder-limit-magnitude
  (sinePartialSum q) (sineValue q) q (e Q.· e)
  (sine-value-converges q)
  (λ k → ∣ zero , (λ n hn → weaken-magnitude-bound _ (e Q.· e) ((e Q.· e) Q.+ precision k)
    (≤-add-nonnegative (e Q.· e) (precision k) (precision-nonnegative k))
    (Sin.sum-remainder-bound q e hq eh he (small-input≤one q hq) n)) ∣₁)

-- Use cosine-value-class and sine-value-class when transporting these
-- estimates. Keeping their presentations opaque avoids normalization of the
-- independently scheduled operational representatives during elaboration.

