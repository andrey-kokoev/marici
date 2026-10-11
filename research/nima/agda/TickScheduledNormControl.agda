{-# OPTIONS --safe --cubical --guardedness #-}
module TickScheduledNormControl where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAddition
open import CanonicalRegularMultiplication
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalCosineRegularity
open import CanonicalSineRegularity
open import CauchyProductBounds
open import CauchyProductErrorBounds using (weaken-magnitude-bound; bounded-value)
open import DyadicallyBoundedCauchy using (dyadicRadius; dyadicRadius-nonnegative)
open import CauchyProductCongruence using (single-difference-bound→directed)
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import TickPhaseNormError

-- Exactly the representative used by TickPhaseNormTransfer.
normRepresentative : RegularCauchy → RegularCauchy
normRepresentative x = addRegular
  (canonicalRegularProduct (canonicalCosineRegular x) (canonicalCosineRegular x))
  (canonicalRegularProduct (canonicalSineRegular x) (canonicalSineRegular x))

-- Multiplication refines by suc(d+d); addition refines by a further suc.
square-sample : RegularCauchy → ℕ → Q.ℚ
square-sample y n = approximation y
  (suc (canonicalDyadicExponent y N.+ canonicalDyadicExponent y) N.+ suc n)

cosine-sample sine-sample : RegularCauchy → ℕ → Q.ℚ
cosine-sample x = square-sample (canonicalCosineRegular x)
sine-sample x = square-sample (canonicalSineRegular x)

actual-norm-sample : (x : RegularCauchy) (n : ℕ)
  → approximation (normRepresentative x) n ≡
    (cosine-sample x n Q.· cosine-sample x n) Q.+ (sine-sample x n Q.· sine-sample x n)
actual-norm-sample x n = refl

canonical-sample-bound : (y : RegularCauchy) (n : ℕ)
  → MagnitudeBound (square-sample y n) (dyadicRadius (canonicalDyadicExponent y))
canonical-sample-bound y n = bounded-value (canonicalDyadicallyBounded y)
  (suc (canonicalDyadicExponent y N.+ canonicalDyadicExponent y) N.+ suc n)

cosine-radius sine-radius common-amplitude : RegularCauchy → Q.ℚ
cosine-radius x = dyadicRadius (canonicalDyadicExponent (canonicalCosineRegular x))
sine-radius x = dyadicRadius (canonicalDyadicExponent (canonicalSineRegular x))
common-amplitude x = cosine-radius x Q.+ sine-radius x

common-amplitude-nonnegative : (x : RegularCauchy) → 0 ≤ common-amplitude x
common-amplitude-nonnegative x = ≤Monotone+ 0 (cosine-radius x) 0 (sine-radius x)
  (dyadicRadius-nonnegative (canonicalDyadicExponent (canonicalCosineRegular x)))
  (dyadicRadius-nonnegative (canonicalDyadicExponent (canonicalSineRegular x)))

cosine-amplitude-bound : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound (cosine-sample x n) (common-amplitude x)
cosine-amplitude-bound x n = weaken-magnitude-bound _ _ _
  (≤-add-nonnegative (cosine-radius x) (sine-radius x)
    (dyadicRadius-nonnegative (canonicalDyadicExponent (canonicalSineRegular x))))
  (canonical-sample-bound (canonicalCosineRegular x) n)

sine-amplitude-bound : (x : RegularCauchy) (n : ℕ)
  → MagnitudeBound (sine-sample x n) (common-amplitude x)
sine-amplitude-bound x n = weaken-magnitude-bound _ _ _
  (subst (sine-radius x ≤_) (Q.+Comm (sine-radius x) (cosine-radius x))
    (≤-add-nonnegative (sine-radius x) (cosine-radius x)
      (dyadicRadius-nonnegative (canonicalDyadicExponent (canonicalCosineRegular x)))))
  (canonical-sample-bound (canonicalSineRegular x) n)

-- Concrete control values at a given actual output depth. No requirement
-- that the cosine and sine internal input or Taylor depths coincide.
record SampleControl (x : RegularCauchy) (k n : ℕ) : Type where
  field
    c s M ε δ : Q.ℚ
    M-nonnegative : 0 ≤ M
    ε-nonnegative : 0 ≤ ε
    actual-cosine-bound : MagnitudeBound (cosine-sample x n) M
    actual-sine-bound : MagnitudeBound (sine-sample x n) M
    control-cosine-bound : MagnitudeBound c M
    control-sine-bound : MagnitudeBound s M
    cosine-error : MagnitudeBound (cosine-sample x n Q.+ (Q.- c)) ε
    sine-error : MagnitudeBound (sine-sample x n Q.+ (Q.- s)) ε
    control-norm-error : MagnitudeBound (((c Q.· c) Q.+ (s Q.· s)) Q.+ (Q.- 1)) δ
    budget : (((ε Q.· (M Q.+ M)) Q.+ (ε Q.· (M Q.+ M))) Q.+ δ) ≤ precision k

sample-control-bound : (x : RegularCauchy) (k n : ℕ) → SampleControl x k n
  → MagnitudeBound (approximation (normRepresentative x) n Q.+ (Q.- 1)) (precision k)
sample-control-bound x k n control =
  weaken-magnitude-bound _ _ _ budget
    (norm-error-bound (cosine-sample x n) (sine-sample x n) c s M ε δ
      M-nonnegative ε-nonnegative actual-cosine-bound actual-sine-bound
      control-cosine-bound control-sine-bound cosine-error sine-error control-norm-error)
  where open SampleControl control

EventualSampleControls : Type
EventualSampleControls = (x : RegularCauchy) (k : ℕ) →
  PT.∥ Σ ℕ (λ threshold → (n : ℕ) → NO._≤_ threshold n → SampleControl x k n) ∥₁

controls-to-scheduled-norm : EventualSampleControls → (x : RegularCauchy)
  → normRepresentative x ≈metric constantCauchy 1
controls-to-scheduled-norm controls x k = PT.map
  (λ { (threshold , witness) → threshold , λ n later →
    let a = approximation (normRepresentative x) n
        bound = sample-control-bound x k n (witness n later)
    in single-difference-bound→directed a 1 (precision k) (positive-upper bound) ,
       single-difference-bound→directed 1 a (precision k)
         (subst (_≤ precision k)
           (ProductSignPaths.negative-difference PreferredℚCommRing a 1)
           (negative-upper bound)) }) (controls x k)
