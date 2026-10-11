{-# OPTIONS --safe --cubical --guardedness #-}
module TickSmallArctangent where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.HITs.SetQuotients as SQ
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import RationalTaylorApproximants using (finiteSum)
open import RationalLogTaylorApproximants using
  (atanhStepRatio; atanh-step-ratio-nonnegative; atanh-step-ratio≤one)
open import TaylorTermBounds using (nonnegative-value-magnitude)
open import TaylorGeometricTail
open import OrderedDifferenceRegularity

-- The alternating odd-power series: its recurrence ratio is
-- -q^2 (2n+1)/(2n+3). No inverse-trigonometric law is assumed here.
atanTerm : Q.ℚ → ℕ → Q.ℚ
atanTerm q zero = q
atanTerm q (suc n) = Q.- (((atanTerm q n Q.· q) Q.· q) Q.· atanhStepRatio n)

atanPartialSum : Q.ℚ → ℕ → Q.ℚ
atanPartialSum q = finiteSum (atanTerm q)

small-input≤one : (q : Q.ℚ) → MagnitudeBound q one-half → MagnitudeBound q 1
small-input≤one q = weaken-magnitude-bound q one-half 1 (precision-step≤ zero)

atan-term-geometric : (q : Q.ℚ) → MagnitudeBound q one-half →
  (n : ℕ) → MagnitudeBound (atanTerm q n) (precision n)
atan-term-geometric q qb zero = small-input≤one q qb
atan-term-geometric q qb (suc n) =
  let previous = atan-term-geometric q qb n
      first = arbitrary-multiplier-bound (atanTerm q n) (precision n) q one-half
        (precision-nonnegative n) one-half-nonnegative previous qb
      second = subst (MagnitudeBound ((atanTerm q n Q.· q) Q.· q))
        (Q.·IdR (precision (suc n)))
        (arbitrary-multiplier-bound (atanTerm q n Q.· q) (precision (suc n)) q 1
          (precision-nonnegative (suc n)) (precision-nonnegative zero) first (small-input≤one q qb))
      stepBound = nonnegative-value-magnitude (atanhStepRatio n) 1
        (atanh-step-ratio-nonnegative n) (atanh-step-ratio≤one n) (precision-nonnegative zero)
      third = subst (MagnitudeBound (((atanTerm q n Q.· q) Q.· q) Q.· atanhStepRatio n))
        (Q.·IdR (precision (suc n)))
        (arbitrary-multiplier-bound ((atanTerm q n Q.· q) Q.· q) (precision (suc n)) (atanhStepRatio n) 1
          (precision-nonnegative (suc n)) (precision-nonnegative zero) second stepBound)
  in negate-magnitude-bound _ _ third

atan-segment-bound : (q : Q.ℚ) → MagnitudeBound q one-half → (start count : ℕ) →
  MagnitudeBound (atanPartialSum q (start N.+ count) Q.+ (Q.- atanPartialSum q start)) (precision start)
atan-segment-bound q qb start count = subst (MagnitudeBound _)
  (Q.·IdL (precision start))
  (finiteSum-segment-difference-magnitude (atanTerm q) 1 start count (precision-nonnegative zero)
    (λ j → subst (MagnitudeBound (atanTerm q (suc j)))
      (sym (Q.·IdL (precision (suc j)))) (atan-term-geometric q qb (suc j))))

atan-ordered-bound : (q : Q.ℚ) → MagnitudeBound q one-half → (m n : ℕ) → NO._≤_ m n →
  MagnitudeBound (atanPartialSum q n Q.+ (Q.- atanPartialSum q m)) (precision m)
atan-ordered-bound q qb m n (count , path) =
  subst (λ j → MagnitudeBound (atanPartialSum q j Q.+ (Q.- atanPartialSum q m)) (precision m))
    (N.+-comm m count ∙ path) (atan-segment-bound q qb m count)

smallAtanRegular : (q : Q.ℚ) → MagnitudeBound q one-half → RegularCauchy
smallAtanRegular q qb = regular-from-ordered-differences (atanPartialSum q) (atan-ordered-bound q qb)

smallAtanValue : (q : Q.ℚ) → MagnitudeBound q one-half → MetricCompletionCandidate
smallAtanValue q qb = SQ.[ smallAtanRegular q qb ]

-- A usable all-later-cutoffs certificate, not just existence of a limit.
atan-later-error : (q : Q.ℚ) (qb : MagnitudeBound q one-half) (m n : ℕ) → NO._≤_ m n →
  MagnitudeBound (approximation (smallAtanRegular q qb) n Q.+ (Q.- atanPartialSum q m)) (precision m)
atan-later-error = atan-ordered-bound
