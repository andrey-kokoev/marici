{-# OPTIONS --safe --cubical --guardedness #-}
module TickConstructedScheduledNorm where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import CauchyCompletionCommRing using (oneCompletion)
open import DyadicallyBoundedCauchy using (dyadicRadius; dyadicRadius-nonnegative; dyadicNat)
open import CanonicalDyadicallyBoundedCauchy using (canonicalDyadicExponent)
open import CanonicalCosineRegularity using (canonicalCosineRegular)
open import CanonicalSineRegularity using (canonicalSineRegular)
open import CanonicalCosineSchedule using (canonicalCosineSeriesDepth; canonical-cosine-input-approximation-bound)
open import UniformCosineSeedBounds using (uniformCosineSeedExponent)
open import CauchyProductBounds
open import RationalArchimedean using (exponent; dominates)
import AbsoluteTaylorSeriesMultiplication as A
import AutomaticRationalExponentialMultiplication as Auto
import TickCommonTaylorControls as C
import TickScheduledNormControl as S
import TickUniformTrigResidual as U
import TickPhaseNormTransfer as Transfer
open import TickCompletionPhase using (phase)

module BudgetPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)
  collect : (M K e : fst R)
    → ((e ·S (M +S M)) +S (e ·S (M +S M))) +S (K ·S e)
      ≡ (((M +S M) +S (M +S M)) +S K) ·S e
  collect M K e = solve! R

depth-lower-bound : (y : RegularCauchy) (n : ℕ) → NO._≤_ n (C.depth y n)
depth-lower-bound y n = NO.≤-trans {m = suc n} NO.≤-sucℕ
  (NO.≤SumRight {n = suc n} {k = suc (canonicalDyadicExponent y N.+ canonicalDyadicExponent y)})

series-lower-bound : (x : RegularCauchy) (n : ℕ) → NO._≤_ n (canonicalCosineSeriesDepth x n)
series-lower-bound x n = NO.≤-trans {m = suc n} NO.≤-sucℕ
  (NO.≤-trans {m = uniformCosineSeedExponent (canonicalDyadicExponent x) N.+ suc n}
    (NO.≤SumRight {n = suc n} {k = uniformCosineSeedExponent (canonicalDyadicExponent x)})
    (NO.≤SumRight {n = uniformCosineSeedExponent (canonicalDyadicExponent x) N.+ suc n}
      {k = dyadicNat (suc (canonicalDyadicExponent x))}))

common-terms-lower-bound : (x : RegularCauchy) (n : ℕ) → NO._≤_ n (C.commonTerms x n)
common-terms-lower-bound x n = NO.≤-trans {m = C.cosDepth x n}
  (depth-lower-bound (canonicalCosineRegular x) n)
  (NO.≤-trans {m = canonicalCosineSeriesDepth x (C.cosDepth x n)}
    (series-lower-bound x (C.cosDepth x n)) NO.left-≤-max)

module AtSource (x : RegularCauchy) where
  module Bound = U.AtRadius (dyadicRadius (canonicalDyadicExponent x))
    (dyadicRadius-nonnegative (canonicalDyadicExponent x))
  M₀ = S.common-amplitude x
  M = M₀ Q.+ 1
  K = Bound.coefficient
  budgetCoefficient = ((M Q.+ M) Q.+ (M Q.+ M)) Q.+ K
  absorption = Auto.preferredExponent budgetCoefficient

  M-nonnegative : 0 ≤ M
  M-nonnegative = U.nonnegative-add M₀ 1 (S.common-amplitude-nonnegative x) (precision-nonnegative zero)

  M₀≤M : M₀ ≤ M
  M₀≤M = ≤-add-nonnegative M₀ 1 (precision-nonnegative zero)

  budgetCoefficient-nonnegative : 0 ≤ budgetCoefficient
  budgetCoefficient-nonnegative = U.nonnegative-add ((M Q.+ M) Q.+ (M Q.+ M)) K
    (U.nonnegative-add (M Q.+ M) (M Q.+ M)
      (U.nonnegative-add M M M-nonnegative M-nonnegative)
      (U.nonnegative-add M M M-nonnegative M-nonnegative))
    Bound.coefficient-nonnegative

  cos-error≤one : (n : ℕ) → C.cosError x n ≤ 1
  cos-error≤one n = isTrans≤ (C.cosError x n) (precision n) 1
    (C.sample-error-decays (canonicalCosineRegular x) n) (precision-antitone zero n NO.zero-≤)

  sin-error≤one : (n : ℕ) → C.sinError x n ≤ 1
  sin-error≤one n = isTrans≤ (C.sinError x n) (precision n) 1
    (C.sample-error-decays (canonicalSineRegular x) n) (precision-antitone zero n NO.zero-≤)

  control-norm-bound : (n : ℕ)
    → MagnitudeBound
        (((C.controlCosine x n Q.· C.controlCosine x n) Q.+
          (C.controlSine x n Q.· C.controlSine x n)) Q.+ (Q.- 1)) (K Q.· precision n)
  control-norm-bound n = A.weakenMagnitudeBound _ _ _
    (Bound.uniform-norm-defect-bound (approximation x (C.commonInput x n))
      (canonical-cosine-input-approximation-bound x (C.commonInput x n)) (C.commonTerms x n))
    (left-multiply-monotone K (precision (C.commonTerms x n)) (precision n)
      Bound.coefficient-nonnegative (precision-antitone n (C.commonTerms x n) (common-terms-lower-bound x n)))

  -- One threshold depending on x and the requested precision. All later
  -- samples satisfy it, even though their rational input and cutoffs move.
  threshold : ℕ → ℕ
  threshold k = exponent absorption N.+ k

  control : (k n : ℕ) → NO._≤_ (threshold k) n → S.SampleControl x k n
  control k n later = record
    { c = C.controlCosine x n
    ; s = C.controlSine x n
    ; M = M
    ; ε = precision n
    ; δ = K Q.· precision n
    ; M-nonnegative = M-nonnegative
    ; ε-nonnegative = precision-nonnegative n
    ; actual-cosine-bound = A.weakenMagnitudeBound _ _ _ (S.cosine-amplitude-bound x n) M₀≤M
    ; actual-sine-bound = A.weakenMagnitudeBound _ _ _ (S.sine-amplitude-bound x n) M₀≤M
    ; control-cosine-bound = A.weakenMagnitudeBound _ _ _ (C.cosine-control-amplitude x n)
        (≤Monotone+ M₀ M₀ (C.cosError x n) 1 (isRefl≤ M₀) (cos-error≤one n))
    ; control-sine-bound = A.weakenMagnitudeBound _ _ _ (C.sine-control-amplitude x n)
        (≤Monotone+ M₀ M₀ (C.sinError x n) 1 (isRefl≤ M₀) (sin-error≤one n))
    ; cosine-error = A.weakenMagnitudeBound _ _ _ (C.cosine-control-error x n)
        (C.sample-error-decays (canonicalCosineRegular x) n)
    ; sine-error = A.weakenMagnitudeBound _ _ _ (C.sine-control-error x n)
        (C.sample-error-decays (canonicalSineRegular x) n)
    ; control-norm-error = control-norm-bound n
    ; budget = subst (_≤ precision k)
        (sym (BudgetPaths.collect PreferredℚCommRing M K (precision n)))
        (isTrans≤ (budgetCoefficient Q.· precision n) (budgetCoefficient Q.· precision (threshold k)) (precision k)
          (left-multiply-monotone budgetCoefficient (precision n) (precision (threshold k))
            budgetCoefficient-nonnegative (precision-antitone (threshold k) n later))
          (A.scaledCoefficientAbsorption budgetCoefficient (exponent absorption) k (dominates absorption)))
    }

constructed-eventual-controls : S.EventualSampleControls
constructed-eventual-controls x k = PT.∣ AtSource.threshold x k , AtSource.control x k ∣₁

constructed-scheduled-norm-bound : Transfer.ScheduledNormBound
constructed-scheduled-norm-bound = S.controls-to-scheduled-norm constructed-eventual-controls

operational-trig-unit-norm : (x : MetricCompletionCandidate) → Transfer.trigNorm x ≡ oneCompletion
operational-trig-unit-norm = Transfer.completion-unit-norm constructed-scheduled-norm-bound

operational-phase-unit-norm : (p t : MetricCompletionCandidate)
  → Transfer.normSquared (phase p t) ≡ oneCompletion
operational-phase-unit-norm = Transfer.phase-unit-norm constructed-scheduled-norm-bound
