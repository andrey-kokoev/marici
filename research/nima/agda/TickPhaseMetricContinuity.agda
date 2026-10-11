{-# OPTIONS --safe --cubical --guardedness #-}
module TickPhaseMetricContinuity where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat as Nat using (ℕ; suc; max; _+_)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Sigma using (Σ; _×_)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyRationalDensity using (eventuallyWithin-weaken)
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalCosineRegularity
open import CanonicalSineRegularity
open import CanonicalCosineComparisonSchedule
open import CanonicalSineComparisonSchedule
open import CanonicalCosineUniformComparison
open import CanonicalSineUniformComparison
open import UniformCosineInputStabilityContract
open import UniformSineInputStabilityContract
open import UniformCosineLateDifference using (operationalUniformCosinePartialSumInputStability)
open import UniformSineLateDifference using (operationalUniformSinePartialSumInputStability)
open import OperationalCosineMetric
open import OperationalSineMetric
open import CauchyProductCongruence using (bounded-product-preserves-right-eventual)
open import CanonicalRegularMultiplication
open import CauchyCompletionMultiplication
open import CauchyNegation using (-completion_)
open import ConstructiveComplexCompletion
open import TickCompletionPhase
open import TickCompletionMetric
open import TickLocalRadiusBound

-- Upgrade pair-dependent moduli to genuine local continuity. The chosen
-- precision is independent of the subsequently quantified neighbour y.
local-from-pair-bound : (f : RegularCauchy → RegularCauchy) (depth : ℕ → ℕ → ℕ) →
  ((x y : RegularCauchy) (k : ℕ) →
    EventuallyWithin x y (depth (Nat.max (canonicalDyadicExponent x) (canonicalDyadicExponent y)) k) →
    EventuallyWithin (f x) (f y) k) → LocallyContinuous f
localModulus (local-from-pair-bound f depth pair) x k =
  envelope (λ d → depth d k) (nearbyExponent x)
localPreserves (local-from-pair-bound f depth pair) x y k h =
  pair x y k (eventuallyWithin-weaken x y
    (depth (Nat.max (canonicalDyadicExponent x) (canonicalDyadicExponent y)) k)
    (envelope (λ d → depth d k) (nearbyExponent x))
    (envelope-covers (λ d → depth d k)
      (Nat.max (canonicalDyadicExponent x) (canonicalDyadicExponent y)) (nearbyExponent x)
      (max-bounded (canonicalDyadicExponent x) (canonicalDyadicExponent y) (nearbyExponent x)
        (center-exponent≤nearby x)
        (nearby-exponent-bound x y (eventuallyWithin-weaken x y 0
          (envelope (λ d → depth d k) (nearbyExponent x)) N.zero-≤ h)))) h)

cosineDepth : ℕ → ℕ → ℕ
cosineDepth d k = uniformCosineMetricDepth operationalUniformCosinePartialSumInputStability d (suc (suc (suc k)))

cosine-pair-continuity : (x y : RegularCauchy) (k : ℕ) →
  EventuallyWithin x y (cosineDepth (comparisonCosineExponent x y) k) →
  EventuallyWithin (canonicalCosineRegular x) (canonicalCosineRegular y) k
cosine-pair-continuity x y k = PT.rec isPropPropTrunc λ { (threshold , bounds) →
  ∣ Nat.max threshold (suc (suc (suc k))) , (λ n hn →
    let threshold≤n = N.≤-trans N.left-≤-max hn
        k3≤n = N.≤-trans N.right-≤-max hn
        h = bounds (comparisonCosineInputDepth x y n)
          (N.≤-trans threshold≤n (cosine-comparison-input-depth-above-output x y n))
    in canonical-cosine-uniform-pointwise-forward operationalUniformCosinePartialSumInputStability
         x y k n k3≤n (fst h) (snd h) ,
       canonical-cosine-uniform-pointwise-backward operationalUniformCosinePartialSumInputStability
         x y k n k3≤n (fst h) (snd h)) ∣₁ }

sineDepth : ℕ → ℕ → ℕ
sineDepth d k = uniformSineMetricDepth operationalUniformSinePartialSumInputStability d (suc (suc (suc k)))

sine-pair-continuity : (x y : RegularCauchy) (k : ℕ) →
  EventuallyWithin x y (sineDepth (comparisonSineExponent x y) k) →
  EventuallyWithin (canonicalSineRegular x) (canonicalSineRegular y) k
sine-pair-continuity x y k = PT.rec isPropPropTrunc λ { (threshold , bounds) →
  ∣ Nat.max threshold (suc (suc (suc k))) , (λ n hn →
    let threshold≤n = N.≤-trans N.left-≤-max hn
        k3≤n = N.≤-trans N.right-≤-max hn
        h = bounds (comparisonSineInputDepth x y n)
          (N.≤-trans threshold≤n (sine-comparison-input-depth-above-output x y n))
    in canonical-sine-uniform-pointwise-forward operationalUniformSinePartialSumInputStability
         x y k n k3≤n (fst h) (snd h) ,
       canonical-sine-uniform-pointwise-backward operationalUniformSinePartialSumInputStability
         x y k n k3≤n (fst h) (snd h)) ∣₁ }

operational-cosine-metric-continuous : MetricContinuous completionCosine
operational-cosine-metric-continuous = lift-local-continuity canonicalCosineRegular completionCosine
  (λ x → refl) (local-from-pair-bound canonicalCosineRegular cosineDepth cosine-pair-continuity)

operational-sine-metric-continuous : MetricContinuous completionSine
operational-sine-metric-continuous = lift-local-continuity canonicalSineRegular completionSine
  (λ x → refl) (local-from-pair-bound canonicalSineRegular sineDepth sine-pair-continuity)

fixed-product-depth : RegularCauchy → ℕ → ℕ → ℕ
fixed-product-depth a d k =
  suc (Nat.max (canonicalDyadicExponent a) (canonicalDyadicExponent a) Nat.+ d) Nat.+ suc (suc k)

fixed-product-local : (a : RegularCauchy) → LocallyContinuous (canonicalRegularProduct a)
fixed-product-local a = local-from-pair-bound (canonicalRegularProduct a) (fixed-product-depth a)
  (λ x y k h → bounded-product-preserves-right-eventual
    (canonicalDyadicallyBounded a) (canonicalDyadicallyBounded x) (canonicalDyadicallyBounded y) k h)

fixed-product-metric-continuous : (a : MetricCompletionCandidate) →
  MetricContinuous (preferredCompletionMultiplication a)
fixed-product-metric-continuous = SQ.elimProp
  (λ a → metric-continuity-isProp (preferredCompletionMultiplication a))
  (λ a → lift-local-continuity (canonicalRegularProduct a) (preferredCompletionMultiplication SQ.[ a ])
    (canonicalRegularProductClass a) (fixed-product-local a))

angle-metric-continuous : (p : MetricCompletionCandidate) → MetricContinuous (angle p)
angle-metric-continuous p = fixed-product-metric-continuous (-completion p)

phase-real-metric-continuous : (p : MetricCompletionCandidate) → MetricContinuous (λ t → realPart (phase p t))
phase-real-metric-continuous p = subst MetricContinuous (sym (funExt (phase-real p)))
  (compose-metric-continuous operational-cosine-metric-continuous (angle-metric-continuous p))

phase-imaginary-metric-continuous : (p : MetricCompletionCandidate) → MetricContinuous (λ t → imaginaryPart (phase p t))
phase-imaginary-metric-continuous p = subst MetricContinuous (sym (funExt (phase-imaginary p)))
  (compose-metric-continuous operational-sine-metric-continuous (angle-metric-continuous p))

ComplexWithin : ComplexCompletion → ComplexCompletion → ℕ → Type
ComplexWithin z w k = CompletionWithin (realPart z) (realPart w) k ×
  CompletionWithin (imaginaryPart z) (imaginaryPart w) k

ComplexMetricContinuous : (MetricCompletionCandidate → ComplexCompletion) → Type
ComplexMetricContinuous f = (a : MetricCompletionCandidate) (k : ℕ) →
  ∥ Σ ℕ (λ l → (b : MetricCompletionCandidate) →
    CompletionWithin a b l → ComplexWithin (f a) (f b) k) ∥₁

operational-phase-metric-continuous : (p : MetricCompletionCandidate) → ComplexMetricContinuous (phase p)
operational-phase-metric-continuous p a k = PT.rec isPropPropTrunc
  (λ { (r , hr) → PT.map (λ { (s , hs) → Nat.max r s , λ b h →
    hr b (within-weaken a b r (Nat.max r s) N.left-≤-max h) ,
    hs b (within-weaken a b s (Nat.max r s) N.right-≤-max h) })
    (phase-imaginary-metric-continuous p a k) })
  (phase-real-metric-continuous p a k)
