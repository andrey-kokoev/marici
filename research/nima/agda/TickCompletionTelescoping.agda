{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionTelescoping where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q using (fromNatℚ)
open import Cubical.Data.Nat.Literals
import RegularCauchyStructure
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionCommRing
open import CauchyProductBounds
open import TickCompletionMagnitudeBounds
open import TickSmallAngleDensity using (completion-bound-weaken)
open import DyadicallyBoundedCauchy using (natℚ; dyadicNat; dyadicRadius; natℚ-dyadicNat; dyadicRadius-times-precision)
open import RegularCauchyStructure using (precision; precision-antitone)
open import RationalArchimedean using (dominates)
import AutomaticRationalExponentialMultiplication as Auto
import AbsoluteTaylorSeriesMultiplication as A
open import TickAtanFirstOrderBounds using (errorOffset)

module FiniteTelescoping {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  sumCount : (ℕ → fst R) → ℕ → fst R
  sumCount u zero = 0r
  sumCount u (suc n) = sumCount u n + u n

  abstract
    negate-zero : - 0r ≡ 0r
    negate-zero = solve! R
    count-zero : (r : fst R) → 0r ≡ 0r · r
    count-zero r = solve! R
    count-step : (m r : fst R) → (m · r) + r ≡ (m + 1r) · r
    count-step m r = solve! R
    dyadic-budget : (d L p : fst R) → d · (L · (p · p)) ≡ L · ((d · p) · p)
    dyadic-budget d L p = solve! R
    empty-sum : (a : fst R) → 0r ≡ a + (- a)
    empty-sum a = solve! R
    cancel : (a b c : fst R) → (b + (- a)) + (c + (- b)) ≡ c + (- a)
    cancel a b c = solve! R
    difference-zero-to-path : (a b : fst R) → b + (- a) ≡ 0r → a ≡ b
    difference-zero-to-path a b p = sym (+IdR a) ∙ cong (a +_) (sym p)
      ∙ (solve! R)

  telescope : (u : ℕ → fst R) (n : ℕ) →
    sumCount (λ j → u (suc j) + (- u j)) n ≡ u n + (- u zero)
  telescope u zero = empty-sum (u zero)
  telescope u (suc n) = cong (_+ (u (suc n) + (- u n))) (telescope u n)
    ∙ cancel (u zero) (u n) (u (suc n))

module C = FiniteTelescoping CompletionCommRing

radiusSum : (ℕ → Q.ℚ) → ℕ → Q.ℚ
radiusSum r zero = 0
radiusSum r (suc n) = radiusSum r n Q.+ r n

abstract
  constant-radius-sum : (r : Q.ℚ) (n : ℕ) → radiusSum (λ _ → r) n ≡ natℚ n Q.· r
  constant-radius-sum r zero = FiniteTelescoping.count-zero PreferredℚCommRing r
  constant-radius-sum r (suc n) = cong (Q._+ r) (constant-radius-sum r n)
    ∙ FiniteTelescoping.count-step PreferredℚCommRing (natℚ n) r

  quadratic-dyadic-budget : (L : Q.ℚ) (n : ℕ) →
    radiusSum (λ _ → L Q.· (precision n Q.· precision n)) (dyadicNat n) ≡ L Q.· precision n
  quadratic-dyadic-budget L n = constant-radius-sum (L Q.· (precision n Q.· precision n)) (dyadicNat n)
    ∙ cong (Q._· (L Q.· (precision n Q.· precision n))) (natℚ-dyadicNat n)
    ∙ FiniteTelescoping.dyadic-budget PreferredℚCommRing (dyadicRadius n) L (precision n)
    ∙ cong (λ d → L Q.· (d Q.· precision n)) (dyadicRadius-times-precision n)
    ∙ cong (L Q.·_) (Q.·IdL (precision n))

  zero-magnitude : MagnitudeBound 0 0
  zero-magnitude .positive-upper = isRefl≤ 0
  zero-magnitude .negative-upper = subst (_≤ 0) (sym (FiniteTelescoping.negate-zero PreferredℚCommRing)) (isRefl≤ 0)

  completion-sum-bound : (u : ℕ → MetricCompletionCandidate) (r : ℕ → Q.ℚ) (n : ℕ) →
    ((j : ℕ) → NO._<_ j n → CompletionMagnitudeBound (u j) (r j)) →
    CompletionMagnitudeBound (C.sumCount u n) (radiusSum r n)
  completion-sum-bound u r zero bounds = embedded-magnitude-bound 0 0 zero-magnitude
  completion-sum-bound u r (suc n) bounds = completion-magnitude-add
    (C.sumCount u n) (u n) (radiusSum r n) (r n)
    (completion-sum-bound u r n (λ j hj → bounds j (NO.≤-trans hj NO.≤-sucℕ)))
    (bounds n NO.≤-refl)

  completion-telescope-bound : (u : ℕ → MetricCompletionCandidate) (r : ℕ → Q.ℚ) (n : ℕ) →
    ((j : ℕ) → NO._<_ j n → CompletionMagnitudeBound (u (suc j) +completion (-completion (u j))) (r j)) →
    CompletionMagnitudeBound (u n +completion (-completion (u zero))) (radiusSum r n)
  completion-telescope-bound u r n bounds = subst
    (λ a → CompletionMagnitudeBound a (radiusSum r n)) (C.telescope u n)
    (completion-sum-bound (λ j → u (suc j) +completion (-completion (u j))) r n bounds)

  -- Exact equality follows only when the actual local bounds and accumulated
  -- budgets are supplied. No estimate for a particular Cayley defect is
  -- assumed implicitly by this general finite-partition theorem.
  completion-partition-constant : (a b : MetricCompletionCandidate)
    (grid : ℕ → ℕ → MetricCompletionCandidate) (count : ℕ → ℕ) (r : ℕ → ℕ → Q.ℚ) →
    ((k : ℕ) → grid k zero ≡ a) → ((k : ℕ) → grid k (count k) ≡ b) →
    ((k j : ℕ) → NO._<_ j (count k) →
      CompletionMagnitudeBound (grid k (suc j) +completion (-completion (grid k j))) (r k j)) →
    ((k : ℕ) → radiusSum (r k) (count k) ≤ RegularCauchyStructure.precision k) → a ≡ b
  completion-partition-constant a b grid count r first last local budget = C.difference-zero-to-path a b
    (completion-magnitude-shrinks (b +completion (-completion a)) (λ k →
      completion-bound-weaken (b +completion (-completion a)) (radiusSum (r k) (count k))
        (RegularCauchyStructure.precision k) (budget k)
        (subst (λ z → CompletionMagnitudeBound z (radiusSum (r k) (count k)))
          (cong₂ _+completion_ (last k) (cong -completion_ (first k)))
          (completion-telescope-bound (grid k) (r k) (count k) (local k)))))

  -- 2^n steps each bounded by L*(2^-n)^2 have total bound L*2^-n.
  -- Archimedean absorption supplies n=errorOffset(L)+k for every precision.
  quadratic-dyadic-partition-constant : (a b : MetricCompletionCandidate)
    (grid : ℕ → ℕ → MetricCompletionCandidate) (L : Q.ℚ) →
    ((n : ℕ) → grid n zero ≡ a) → ((n : ℕ) → grid n (dyadicNat n) ≡ b) →
    ((n j : ℕ) → NO._<_ j (dyadicNat n) →
      CompletionMagnitudeBound (grid n (suc j) +completion (-completion (grid n j)))
        (L Q.· (precision n Q.· precision n))) → a ≡ b
  quadratic-dyadic-partition-constant a b grid L first last local = completion-partition-constant a b
    (λ k → grid (errorOffset L N.+ k)) (λ k → dyadicNat (errorOffset L N.+ k))
    (λ k _ → L Q.· (precision (errorOffset L N.+ k) Q.· precision (errorOffset L N.+ k)))
    (λ k → first (errorOffset L N.+ k)) (λ k → last (errorOffset L N.+ k))
    (λ k → local (errorOffset L N.+ k))
    (λ k → subst (_≤ precision k) (sym (quadratic-dyadic-budget L (errorOffset L N.+ k)))
      (A.scaledCoefficientAbsorption L (errorOffset L) k (dominates (Auto.preferredExponent L))))

  -- Local small-angle estimates need only hold beyond a fixed mesh depth.
  -- The count remains 2^n; shifting the precision request does not silently
  -- replace it by 2^(n-depth).
  fine-quadratic-dyadic-partition-constant : (a b : MetricCompletionCandidate)
    (grid : ℕ → ℕ → MetricCompletionCandidate) (L : Q.ℚ) (depth : ℕ) →
    ((n : ℕ) → grid n zero ≡ a) → ((n : ℕ) → grid n (dyadicNat n) ≡ b) →
    ((n j : ℕ) → NO._≤_ depth n → NO._<_ j (dyadicNat n) →
      CompletionMagnitudeBound (grid n (suc j) +completion (-completion (grid n j)))
        (L Q.· (precision n Q.· precision n))) → a ≡ b
  fine-quadratic-dyadic-partition-constant a b grid L depth first last local = completion-partition-constant a b
    (λ k → grid (errorOffset L N.+ (depth N.+ k)))
    (λ k → dyadicNat (errorOffset L N.+ (depth N.+ k)))
    (λ k _ → L Q.· (precision (errorOffset L N.+ (depth N.+ k)) Q.· precision (errorOffset L N.+ (depth N.+ k))))
    (λ k → first (errorOffset L N.+ (depth N.+ k)))
    (λ k → last (errorOffset L N.+ (depth N.+ k)))
    (λ k j hj → local (errorOffset L N.+ (depth N.+ k)) j (NO.≤-trans (NO.≤SumLeft {n = depth} {k = k}) (NO.≤SumRight {n = depth N.+ k} {k = errorOffset L})) hj)
    (λ k → subst (_≤ precision k) (sym (quadratic-dyadic-budget L (errorOffset L N.+ (depth N.+ k))))
      (isTrans≤ (L Q.· precision (errorOffset L N.+ (depth N.+ k))) (precision (depth N.+ k)) (precision k)
        (A.scaledCoefficientAbsorption L (errorOffset L) (depth N.+ k) (dominates (Auto.preferredExponent L)))
        (precision-antitone k (depth N.+ k) NO.≤SumRight)))
