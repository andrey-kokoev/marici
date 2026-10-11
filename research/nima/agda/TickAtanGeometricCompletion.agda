{-# OPTIONS --safe --cubical --guardedness #-}
module TickAtanGeometricCompletion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RationalAnalyticSubstrate using (one-half)
open import RegularCauchyStructure
open import OrderedDifferenceRegularity
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyProductErrorBounds using (weaken-magnitude-bound)
open import TaylorGeometricTail
open import TickCompletionMetric
open import TickCompletionLimits
open import TaylorRegularityComposition using (magnitude-bound-forward; magnitude-bound-backward)
open import TickSmallArctangent
open import TickAtanDerivativeAlgebra
open import TickAtanFirstOrderBounds using (geometric-term-bound)
import TickAtanFirstOrderBounds as Bounds
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import TickRationalProductLimits

constant-difference-eventual : (a b : Q.ℚ) (k : ℕ) →
  MagnitudeBound (a Q.+ (Q.- b)) (precision k) → EventuallyWithin (constantCauchy a) (constantCauchy b) k
constant-difference-eventual a b k h = ∣ zero , (λ n hn →
  magnitude-bound-forward a b (precision k) h , magnitude-bound-backward a b (precision k) h) ∣₁

geometric-segment-bound : (q : Q.ℚ) → MagnitudeBound q one-half → (start count : ℕ) →
  MagnitudeBound (geometricSum q (start N.+ count) Q.+ (Q.- geometricSum q start)) (precision start)
geometric-segment-bound q h start count = subst (MagnitudeBound _) (Q.·IdL (precision start))
  (finiteSum-segment-difference-magnitude (geometricTerm q) 1 start count (precision-nonnegative zero)
    (λ j → subst (MagnitudeBound (geometricTerm q (suc j))) (sym (Q.·IdL (precision (suc j))))
      (geometric-term-bound q h (suc j))))

geometric-ordered-bound : (q : Q.ℚ) → MagnitudeBound q one-half → (m n : ℕ) → NO._≤_ m n →
  MagnitudeBound (geometricSum q n Q.+ (Q.- geometricSum q m)) (precision m)
geometric-ordered-bound q h m n (count , path) =
  subst (λ j → MagnitudeBound (geometricSum q j Q.+ (Q.- geometricSum q m)) (precision m))
    (N.+-comm m count ∙ path) (geometric-segment-bound q h m count)

geometricRegular : (q : Q.ℚ) → MagnitudeBound q one-half → RegularCauchy
geometricRegular q h = regular-from-ordered-differences (geometricSum q) (geometric-ordered-bound q h)

-- Keep the completion value opaque so multiplication does not evaluate its
-- canonical Archimedean schedule while elaborating limit identities.
abstract
  geometricValue : (q : Q.ℚ) → MagnitudeBound q one-half → MetricCompletionCandidate
  geometricValue q h = SQ.[ geometricRegular q h ]

  geometric-value-class : (q : Q.ℚ) (h : MagnitudeBound q one-half) →
    geometricValue q h ≡ SQ.[ geometricRegular q h ]
  geometric-value-class q h = refl

  -- Unshifted finite sums converge to the actual series classes.
  atan-sequence-converges : (q : Q.ℚ) (h : MagnitudeBound q one-half) →
    Converges (λ n → embedMetricℚ (atanPartialSum q n)) (smallAtanValue q h)
  atan-sequence-converges q h k = ∣ k , (λ n hn →
    within-intro (smallAtanRegular q h) (constantCauchy (atanPartialSum q n)) k
      ∣ n , (λ j hj →
        magnitude-bound-forward (atanPartialSum q j) (atanPartialSum q n) (precision k)
          (weaken-magnitude-bound _ _ _ (precision-antitone k n hn) (atan-ordered-bound q h n j hj)) ,
        magnitude-bound-backward (atanPartialSum q j) (atanPartialSum q n) (precision k)
          (weaken-magnitude-bound _ _ _ (precision-antitone k n hn) (atan-ordered-bound q h n j hj))) ∣₁) ∣₁

  geometric-sequence-converges : (q : Q.ℚ) (h : MagnitudeBound q one-half) →
    Converges (λ n → embedMetricℚ (geometricSum q n)) (geometricValue q h)
  geometric-sequence-converges q h k = ∣ k , (λ n hn →
    within-intro (geometricRegular q h) (constantCauchy (geometricSum q n)) k
      ∣ n , (λ j hj →
        magnitude-bound-forward (geometricSum q j) (geometricSum q n) (precision k)
          (weaken-magnitude-bound _ _ _ (precision-antitone k n hn) (geometric-ordered-bound q h n j hj)) ,
        magnitude-bound-backward (geometricSum q j) (geometricSum q n) (precision k)
          (weaken-magnitude-bound _ _ _ (precision-antitone k n hn) (geometric-ordered-bound q h n j hj))) ∣₁) ∣₁

-- Denominator-cleared rational approximants converge to one.
geometric-denominator-error : (q : Q.ℚ) (h : MagnitudeBound q one-half) (n : ℕ) →
  MagnitudeBound ((1 Q.+ q Q.· q) Q.· geometricSum q n Q.+ (Q.- 1)) (precision n)
geometric-denominator-error q h n = transport-magnitude
  ((1 Q.+ q Q.· q) Q.· geometricSum q n Q.+ (Q.- 1)) (Q.- geometricTerm q (suc n)) (precision n)
  (cong (Q._+ (Q.- 1)) (geometric-denominator-identity q n) ∙ Bounds.B.cancel-one (geometricTerm q (suc n)))
  (negate-magnitude-bound _ _ (weaken-magnitude-bound _ _ _ (precision-step≤ n) (geometric-term-bound q h (suc n))))

geometric-denominator-converges : (q : Q.ℚ) (h : MagnitudeBound q one-half) →
  Converges (λ n → embedMetricℚ ((1 Q.+ q Q.· q) Q.· geometricSum q n)) (embedMetricℚ 1)
geometric-denominator-converges q h k = ∣ k , (λ n hn → within-sym
  (embedMetricℚ ((1 Q.+ q Q.· q) Q.· geometricSum q n)) (embedMetricℚ 1) k
  (within-intro (constantCauchy ((1 Q.+ q Q.· q) Q.· geometricSum q n)) (constantCauchy 1) k
    (constant-difference-eventual ((1 Q.+ q Q.· q) Q.· geometricSum q n) 1 k
      (weaken-magnitude-bound ((1 Q.+ q Q.· q) Q.· geometricSum q n Q.+ (Q.- 1)) (precision n) (precision k)
        (precision-antitone k n hn) (geometric-denominator-error q h n))))) ∣₁

geometric-completion-inverse : (q : Q.ℚ) (h : MagnitudeBound q one-half) →
  preferredCompletionMultiplication (embedMetricℚ (1 Q.+ q Q.· q)) (geometricValue q h) ≡ embedMetricℚ 1
geometric-completion-inverse q h = convergent-limits-equal
  (λ n → embedMetricℚ ((1 Q.+ q Q.· q) Q.· geometricSum q n))
  (preferredCompletionMultiplication (embedMetricℚ (1 Q.+ q Q.· q)) (geometricValue q h)) (embedMetricℚ 1)
  (rational-product-sequence-converges (1 Q.+ q Q.· q) (geometricSum q) (geometricValue q h)
    (geometric-sequence-converges q h))
  (geometric-denominator-converges q h)
