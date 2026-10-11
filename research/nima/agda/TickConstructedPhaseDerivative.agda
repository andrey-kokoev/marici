{-# OPTIONS --safe --cubical --guardedness #-}
module TickConstructedPhaseDerivative where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as N
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyNegation using (-completion_; negate-one-error-bound)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import CauchyRationalEmbedding using (embedℚ-preserves-negation)
open import ConstructiveComplexCompletion
open import DyadicallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionMetric
open import TickCompletionLimits
open import TickCompletionOrderLimits using (completion-nonnegative-isProp)
open import TickCompletionTrigSmallAngle
open import TickCompletionPhase
open import TickPhaseMetricRegularity
open import TickPhaseDerivativeReduction using (phaseLocalRemainder; LocalPhaseDerivativeBound; local-bound-to-phase-derivative)
open import TickCompletionRelativeBound
open import TickPhaseDerivativeModulus using (residualDepth; derivativeDepth; modulus-small-angle; modulus-quadratic-budget)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  negative-zero-add : (e : fst R) → (-S 0r) +S e ≡ e
  negative-zero-add e = solve! R
  negative-product : (p h : fst R) → -S (p ·S h) ≡ (-S p) ·S h
  negative-product p h = solve! R
module R = Algebra PreferredℚCommRing
module C = Algebra CompletionCommRing

abstract
  canonical-magnitude : (x : RegularCauchy) (n : ℕ) →
    MagnitudeBound (approximation x n) (dyadicRadius (canonicalDyadicExponent x))
  canonical-magnitude x n .positive-upper = upper-bound (canonicalDyadicallyBounded x) n
  canonical-magnitude x n .negative-upper = subst (Q.- approximation x n ≤_)
    (Q.+IdR (Q.- (Q.- dyadicRadius (canonicalDyadicExponent x))) ∙ Q.-Invol (dyadicRadius (canonicalDyadicExponent x)))
    (negate-one-error-bound (Q.- dyadicRadius (canonicalDyadicExponent x)) (approximation x n) 0
      (subst (Q.- dyadicRadius (canonicalDyadicExponent x) ≤_) (sym (Q.+IdR (approximation x n)))
        (lower-bound (canonicalDyadicallyBounded x) n)))

  ball-eventual-magnitude : (y : RegularCauchy) (j : ℕ) →
    CompletionWithin zeroCompletion SQ.[ y ] (suc (suc j)) →
    Eventually (λ n → MagnitudeBound (approximation y (suc n)) (precision j))
  ball-eventual-magnitude y j near = PT.map
    (λ { (threshold , bounds) → threshold , λ n hn →
      bound (approximation y (suc n)) (fst (bounds (suc n) (N.≤-trans hn N.≤-sucℕ)))
        (snd (bounds (suc n) (N.≤-trans hn N.≤-sucℕ))) })
    (within-representatives (constantCauchy 0) y j near)
    where
    bound : (q : Q.ℚ) → 0 ≤ q Q.+ precision j → q ≤ 0 Q.+ precision j → MagnitudeBound q (precision j)
    bound q lower upper .positive-upper = subst (q ≤_) (Q.+IdL (precision j)) upper
    bound q lower upper .negative-upper = subst (Q.- q ≤_) (R.negative-zero-add (precision j))
      (negate-one-error-bound 0 q (precision j) lower)

  local-residual-identification : (p h : MetricCompletionCandidate) →
    localResidualNorm p h ≡ complexNormSquared (phaseLocalRemainder p h)
  local-residual-identification p h = cong complexNormSquared
    (cong₂ complex
      (cosine-remainder-definition (-completion (preferredCompletionMultiplication p h))
        ∙ cong₂ _+completion_ (cong completionCosine (C.negative-product p h))
          (sym (embedℚ-preserves-negation 1)))
      (sine-remainder-definition (-completion (preferredCompletionMultiplication p h))
        ∙ cong₂ _+completion_ (cong completionSine (C.negative-product p h))
          (cong -completion_ (C.negative-product p h))))

  representative-local-bound : (x y : RegularCauchy) (k : ℕ) →
    CompletionWithin zeroCompletion SQ.[ y ] (derivativeDepth (canonicalDyadicExponent x) k) →
    CompletionLE (complexNormSquared (phaseLocalRemainder SQ.[ x ] SQ.[ y ]))
      (preferredCompletionMultiplication (embedMetricℚ (precision k Q.· precision k)) (squareCompletion SQ.[ y ]))
  representative-local-bound x y k near = subst
    (λ a → CompletionLE a (preferredCompletionMultiplication
      (embedMetricℚ (precision k Q.· precision k)) (squareCompletion SQ.[ y ])))
    (local-residual-identification SQ.[ x ] SQ.[ y ])
    (bounded-completion-relative-bound (dyadicRadius d) (precision (residualDepth d k)) (precision k)
      (dyadicRadius-nonnegative d) (precision-nonnegative (residualDepth d k))
      (modulus-small-angle d k) (modulus-quadratic-budget d k) x y
      ∣ zero , (λ n _ → canonical-magnitude x (suc n)) ∣₁
      (ball-eventual-magnitude y (residualDepth d k) near))
    where
    d : ℕ
    d = canonicalDyadicExponent x

  constructed-local-phase-derivative-bound : (p : MetricCompletionCandidate) → LocalPhaseDerivativeBound p
  constructed-local-phase-derivative-bound = SQ.elimProp
    (λ p → isPropΠ (λ k → isPropPropTrunc))
    (λ x k → ∣ derivativeDepth (canonicalDyadicExponent x) k ,
      SQ.elimProp
        (λ h → isPropΠ (λ _ → completion-nonnegative-isProp
          (preferredCompletionMultiplication (embedMetricℚ (precision k Q.· precision k)) (squareCompletion h)
            +completion (-completion (complexNormSquared (phaseLocalRemainder SQ.[ x ] h))))))
        (λ y → representative-local-bound x y k) ∣₁)

  operational-phase-derivative : PhaseDerivativeLaw
  operational-phase-derivative p = local-bound-to-phase-derivative p (constructed-local-phase-derivative-bound p)

  operational-phase-metric-regularity : PhaseMetricRegularity
  operational-phase-metric-regularity = operational-phase-metric-continuous , operational-phase-derivative
