{-# OPTIONS --safe --cubical --guardedness #-}
module TickCommonTaylorControls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; suc; max)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalCosineRegularity
open import CanonicalSineRegularity
open import CanonicalCosineSchedule
open import CanonicalSineSchedule
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import CosinePartialSumInputDifference
open import SinePartialSumInputDifference
open import CauchyProductBounds
open import CauchyProductErrorBounds
import CanonicalCosineComparisonSchedule as CC
import CanonicalSineComparisonSchedule as SC
import TickScheduledNormControl as Actual

module ErrorPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  combine : (a b c : fst R) → a +S (-S c) ≡ (a +S (-S b)) +S (-S (c +S (-S b)))
  combine a b c = solve! R
  recover : (a c : fst R) → c ≡ a +S (-S (a +S (-S c)))
  recover a c = solve! R

combine-errors : (a b c e f : Q.ℚ)
  → MagnitudeBound (a Q.+ (Q.- b)) e → MagnitudeBound (c Q.+ (Q.- b)) f
  → MagnitudeBound (a Q.+ (Q.- c)) (e Q.+ f)
combine-errors a b c e f ab cb = transport-magnitude _ _ _
  (ErrorPaths.combine PreferredℚCommRing a b c)
  (add-magnitude-bounds _ e _ f ab (negate-magnitude-bound _ f cb))

control-amplitude : (a c M e : Q.ℚ) → MagnitudeBound a M
  → MagnitudeBound (a Q.+ (Q.- c)) e → MagnitudeBound c (M Q.+ e)
control-amplitude a c M e amplitude error = transport-magnitude _ _ _
  (ErrorPaths.recover PreferredℚCommRing a c)
  (add-magnitude-bounds a M _ e amplitude (negate-magnitude-bound _ e error))

-- An arbitrary common input at least as deep as the native input schedule
-- retains that schedule's input error budget.
input-budget : (scale n j : ℕ) → NO._≤_ (scale N.+ suc n) j
  → dyadicRadius scale Q.· (precision (scale N.+ suc n) Q.+ precision j) ≤ precision n
input-budget scale n j deep =
  subst2 _≤_
    (sym (Q.·DistL+ (dyadicRadius scale) (precision (scale N.+ suc n)) (precision j)))
    (precision-refines-double n)
    (≤Monotone+
      (dyadicRadius scale Q.· precision (scale N.+ suc n)) (precision (suc n))
      (dyadicRadius scale Q.· precision j) (precision (suc n))
      (subst (dyadicRadius scale Q.· precision (scale N.+ suc n) ≤_)
        (radius-cancels-precision-shift scale (suc n))
        (isRefl≤ (dyadicRadius scale Q.· precision (scale N.+ suc n))))
      (subst (dyadicRadius scale Q.· precision j ≤_)
        (radius-cancels-precision-shift scale (suc n))
        (left-multiply-monotone (dyadicRadius scale) (precision j) (precision (scale N.+ suc n))
          (dyadicRadius-nonnegative scale) (precision-antitone _ _ deep))))

cosine-input-control : (x : RegularCauchy) (m j : ℕ)
  → NO._≤_ (canonicalCosineInputDepth x m) j
  → MagnitudeBound
      (approximation (canonicalCosineRegular x) m Q.+
       (Q.- cosinePartialSum (approximation x j) (canonicalCosineSeriesDepth x m))) (precision m)
cosine-input-control x m j deep = weaken-magnitude-bound _ _ _
  (input-budget (canonicalCosineInputScale x m) m j deep)
  (cosine-partial-sum-input-difference-bound
    (approximation x (canonicalCosineInputDepth x m)) (approximation x j)
    (precision (canonicalCosineInputDepth x m) Q.+ precision j)
    (canonicalDyadicExponent x) (canonicalCosineSeriesDepth x m)
    (precision-sum-nonnegative (canonicalCosineInputDepth x m) j)
    (canonical-cosine-input-approximation-bound x _) (canonical-cosine-input-approximation-bound x j)
    (cauchy-difference-bound x _ j))

sine-input-control : (x : RegularCauchy) (m j : ℕ)
  → NO._≤_ (canonicalSineInputDepth x m) j
  → MagnitudeBound
      (approximation (canonicalSineRegular x) m Q.+
       (Q.- sinePartialSum (approximation x j) (canonicalSineSeriesDepth x m))) (precision m)
sine-input-control x m j deep = weaken-magnitude-bound _ _ _
  (input-budget (canonicalSineInputScale x m) m j deep)
  (sine-partial-sum-input-difference-bound
    (approximation x (canonicalSineInputDepth x m)) (approximation x j)
    (precision (canonicalSineInputDepth x m) Q.+ precision j)
    (canonicalDyadicExponent x) (canonicalSineSeriesDepth x m)
    (precision-sum-nonnegative (canonicalSineInputDepth x m) j)
    (canonical-sine-input-approximation-bound x _) (canonical-sine-input-approximation-bound x j)
    (cauchy-difference-bound x _ j))

-- Both controls use exactly the same rational input and term cutoff.
depth : RegularCauchy → ℕ → ℕ
depth y n = suc (canonicalDyadicExponent y N.+ canonicalDyadicExponent y) N.+ suc n
cosDepth sinDepth commonInput commonTerms : RegularCauchy → ℕ → ℕ
cosDepth x n = depth (canonicalCosineRegular x) n
sinDepth x n = depth (canonicalSineRegular x) n
commonInput x n = N.max (canonicalCosineInputDepth x (cosDepth x n)) (canonicalSineInputDepth x (sinDepth x n))
commonTerms x n = N.max (canonicalCosineSeriesDepth x (cosDepth x n)) (canonicalSineSeriesDepth x (sinDepth x n))

controlCosine controlSine : RegularCauchy → ℕ → Q.ℚ
controlCosine x n = cosinePartialSum (approximation x (commonInput x n)) (commonTerms x n)
controlSine x n = sinePartialSum (approximation x (commonInput x n)) (commonTerms x n)

cosine-input-error : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound
      (Actual.cosine-sample x n Q.+ (Q.- cosinePartialSum (approximation x (commonInput x n))
        (canonicalCosineSeriesDepth x (cosDepth x n)))) (precision (cosDepth x n))
cosine-input-error x n = cosine-input-control x (cosDepth x n) (commonInput x n) NO.left-≤-max

sine-input-error : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound
      (Actual.sine-sample x n Q.+ (Q.- sinePartialSum (approximation x (commonInput x n))
        (canonicalSineSeriesDepth x (sinDepth x n)))) (precision (sinDepth x n))
sine-input-error x n = sine-input-control x (sinDepth x n) (commonInput x n) NO.right-≤-max

cosine-extension-error : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound
      (controlCosine x n Q.+ (Q.- cosinePartialSum (approximation x (commonInput x n))
        (canonicalCosineSeriesDepth x (cosDepth x n)))) (precision (suc (cosDepth x n)))
cosine-extension-error x n = CC.common-series-extension-bound _ (canonicalDyadicExponent x)
  (cosDepth x n) (commonTerms x n)
  (canonical-cosine-input-approximation-bound x (commonInput x n)) NO.left-≤-max

sine-extension-error : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound
      (controlSine x n Q.+ (Q.- sinePartialSum (approximation x (commonInput x n))
        (canonicalSineSeriesDepth x (sinDepth x n)))) (precision (suc (sinDepth x n)))
sine-extension-error x n = SC.sine-common-series-extension-bound _ (canonicalDyadicExponent x)
  (sinDepth x n) (commonTerms x n)
  (canonical-sine-input-approximation-bound x (commonInput x n)) NO.right-≤-max

sample-error-decays : (y : RegularCauchy) (n : ℕ)
  → precision (depth y n) Q.+ precision (suc (depth y n)) ≤ precision n
sample-error-decays y n = subst (precision (depth y n) Q.+ precision (suc (depth y n)) ≤_) (precision-refines-double n)
  (≤Monotone+ (precision (depth y n)) (precision (suc n))
    (precision (suc (depth y n))) (precision (suc n))
    (precision-antitone (suc n) (depth y n)
      (NO.≤SumRight {n = suc n} {k = suc (canonicalDyadicExponent y N.+ canonicalDyadicExponent y)}))
    (precision-antitone (suc n) (suc (depth y n))
      (NO.≤-trans {m = depth y n}
        (NO.≤SumRight {n = suc n} {k = suc (canonicalDyadicExponent y N.+ canonicalDyadicExponent y)}) NO.≤-sucℕ)))

cosError sinError : RegularCauchy → ℕ → Q.ℚ
cosError x n = precision (cosDepth x n) Q.+ precision (suc (cosDepth x n))
sinError x n = precision (sinDepth x n) Q.+ precision (suc (sinDepth x n))

cosine-control-error : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound (Actual.cosine-sample x n Q.+ (Q.- controlCosine x n)) (cosError x n)
cosine-control-error x n = combine-errors (Actual.cosine-sample x n)
  (cosinePartialSum (approximation x (commonInput x n)) (canonicalCosineSeriesDepth x (cosDepth x n)))
  (controlCosine x n) (precision (cosDepth x n)) (precision (suc (cosDepth x n)))
  (cosine-input-error x n) (cosine-extension-error x n)
sine-control-error : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound (Actual.sine-sample x n Q.+ (Q.- controlSine x n)) (sinError x n)
sine-control-error x n = combine-errors (Actual.sine-sample x n)
  (sinePartialSum (approximation x (commonInput x n)) (canonicalSineSeriesDepth x (sinDepth x n)))
  (controlSine x n) (precision (sinDepth x n)) (precision (suc (sinDepth x n)))
  (sine-input-error x n) (sine-extension-error x n)

cosine-control-amplitude : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound (controlCosine x n) (Actual.common-amplitude x Q.+ cosError x n)
cosine-control-amplitude x n = control-amplitude (Actual.cosine-sample x n) (controlCosine x n)
  (Actual.common-amplitude x) (cosError x n)
  (Actual.cosine-amplitude-bound x n) (cosine-control-error x n)
sine-control-amplitude : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound (controlSine x n) (Actual.common-amplitude x Q.+ sinError x n)
sine-control-amplitude x n = control-amplitude (Actual.sine-sample x n) (controlSine x n)
  (Actual.common-amplitude x) (sinError x n)
  (Actual.sine-amplitude-bound x n) (sine-control-error x n)
