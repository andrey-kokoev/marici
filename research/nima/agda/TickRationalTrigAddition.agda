{-# OPTIONS --safe --cubical --guardedness #-}
module TickRationalTrigAddition where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ; zero; suc; max)
import Cubical.Data.Nat.Order as N
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding
open import CauchyCompletionMultiplication
open import CanonicalDyadicallyBoundedCauchy using (canonicalDyadicExponent)
open import CanonicalCosineSchedule using (canonical-cosine-input-approximation-bound)
open import DyadicallyBoundedCauchy using (dyadicRadius; dyadicRadius-nonnegative; dyadicRadius-monotone)
open import CauchyProductBounds
open import RationalTaylorApproximants using (cosinePartialSum)
open import RationalSineTaylorApproximants using (sinePartialSum)
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
import AbsoluteTaylorSeriesMultiplication as A
import TickTrigAdditionResidual as R
open import TickTrigPartialSumTransfer
open import TickCompletionMetric
open import TickCompletionRingContinuity
open import TickCompletionLimits

cosineAdditionRHS sineAdditionRHS : MetricCompletionCandidate → MetricCompletionCandidate → MetricCompletionCandidate
cosineAdditionRHS x y =
  preferredCompletionMultiplication (completionCosine x) (completionCosine y) +completion
  (-completion (preferredCompletionMultiplication (completionSine x) (completionSine y)))
sineAdditionRHS x y =
  preferredCompletionMultiplication (completionSine x) (completionCosine y) +completion
  preferredCompletionMultiplication (completionCosine x) (completionSine y)

cosinePartialRHS sinePartialRHS : Q.ℚ → Q.ℚ → ℕ → Q.ℚ
cosinePartialRHS x y n = cosinePartialSum x n Q.· cosinePartialSum y n Q.+
  (Q.- (sinePartialSum x n Q.· sinePartialSum y n))
sinePartialRHS x y n = sinePartialSum x n Q.· cosinePartialSum y n Q.+
  (cosinePartialSum x n Q.· sinePartialSum y n)

cosineSequence sineSequence : Q.ℚ → ℕ → MetricCompletionCandidate
cosineSequence q n = embedMetricℚ (cosinePartialSum q n)
sineSequence q n = embedMetricℚ (sinePartialSum q n)

cosine-sequence-converges : (q : Q.ℚ) → Converges (cosineSequence q) (completionCosine (embedMetricℚ q))
cosine-sequence-converges q k = ∣ cosineTransferCutoff q k , cosine-partial-sum-to-operational q k ∣₁
sine-sequence-converges : (q : Q.ℚ) → Converges (sineSequence q) (completionSine (embedMetricℚ q))
sine-sequence-converges q k = ∣ sineTransferCutoff q k , sine-partial-sum-to-operational q k ∣₁

sum-limit : {u v : ℕ → MetricCompletionCandidate} {a b : MetricCompletionCandidate} →
  Converges u a → Converges v b → Converges (λ n → u n +completion v n) (a +completion b)
sum-limit {u} {v} {a} {b} = joint-continuous-limit _+completion_ addition-joint-continuous u v a b
product-limit : {u v : ℕ → MetricCompletionCandidate} {a b : MetricCompletionCandidate} →
  Converges u a → Converges v b →
  Converges (λ n → preferredCompletionMultiplication (u n) (v n)) (preferredCompletionMultiplication a b)
product-limit {u} {v} {a} {b} = joint-continuous-limit preferredCompletionMultiplication multiplication-joint-continuous u v a b
negative-limit : {u : ℕ → MetricCompletionCandidate} {a : MetricCompletionCandidate} →
  Converges u a → Converges (λ n → -completion (u n)) (-completion a)
negative-limit {u} {a} = continuous-limit -completion_ negation-metric-continuous u a

module AtPair (x y : Q.ℚ) where
  dx = canonicalDyadicExponent (constantCauchy x)
  dy = canonicalDyadicExponent (constantCauchy y)
  d = Nat.max dx dy
  r = dyadicRadius d
  module Tail = R.AtRadius r (dyadicRadius-nonnegative d)

  x-bound : MagnitudeBound x r
  x-bound = A.weakenMagnitudeBound x (dyadicRadius dx) r
    (canonical-cosine-input-approximation-bound (constantCauchy x) zero)
    (dyadicRadius-monotone dx d N.left-≤-max)
  y-bound : MagnitudeBound y r
  y-bound = A.weakenMagnitudeBound y (dyadicRadius dy) r
    (canonical-cosine-input-approximation-bound (constantCauchy y) zero)
    (dyadicRadius-monotone dy d N.right-≤-max)

  cosExpr sinExpr : ℕ → MetricCompletionCandidate
  cosExpr n = preferredCompletionMultiplication (cosineSequence x n) (cosineSequence y n) +completion
    (-completion (preferredCompletionMultiplication (sineSequence x n) (sineSequence y n)))
  sinExpr n = preferredCompletionMultiplication (sineSequence x n) (cosineSequence y n) +completion
    preferredCompletionMultiplication (cosineSequence x n) (sineSequence y n)

  cos-expr-path : (n : ℕ) → cosExpr n ≡ embedMetricℚ (cosinePartialRHS x y n)
  cos-expr-path n = cong₂ _+completion_
    (preferredCompletionMultiplication-preserves-rationals (cosinePartialSum x n) (cosinePartialSum y n))
    (cong -completion_ (preferredCompletionMultiplication-preserves-rationals (sinePartialSum x n) (sinePartialSum y n))
      ∙ embedℚ-preserves-negation (sinePartialSum x n Q.· sinePartialSum y n))
    ∙ sym (embedℚ-preserves-sum (cosinePartialSum x n Q.· cosinePartialSum y n)
      (Q.- (sinePartialSum x n Q.· sinePartialSum y n)))

  sin-expr-path : (n : ℕ) → sinExpr n ≡ embedMetricℚ (sinePartialRHS x y n)
  sin-expr-path n = cong₂ _+completion_
    (preferredCompletionMultiplication-preserves-rationals (sinePartialSum x n) (cosinePartialSum y n))
    (preferredCompletionMultiplication-preserves-rationals (cosinePartialSum x n) (sinePartialSum y n))
    ∙ sym (embedℚ-preserves-sum (sinePartialSum x n Q.· cosinePartialSum y n)
      (cosinePartialSum x n Q.· sinePartialSum y n))

  cos-rhs-limit : Converges (λ n → embedMetricℚ (cosinePartialRHS x y n)) (cosineAdditionRHS (embedMetricℚ x) (embedMetricℚ y))
  cos-rhs-limit = converges-pointwise-path cosExpr (λ n → embedMetricℚ (cosinePartialRHS x y n))
    (cosineAdditionRHS (embedMetricℚ x) (embedMetricℚ y)) cos-expr-path
    (sum-limit (product-limit (cosine-sequence-converges x) (cosine-sequence-converges y))
      (negative-limit (product-limit (sine-sequence-converges x) (sine-sequence-converges y))))

  sin-rhs-limit : Converges (λ n → embedMetricℚ (sinePartialRHS x y n)) (sineAdditionRHS (embedMetricℚ x) (embedMetricℚ y))
  sin-rhs-limit = converges-pointwise-path sinExpr (λ n → embedMetricℚ (sinePartialRHS x y n))
    (sineAdditionRHS (embedMetricℚ x) (embedMetricℚ y)) sin-expr-path
    (sum-limit (product-limit (sine-sequence-converges x) (cosine-sequence-converges y))
      (product-limit (cosine-sequence-converges x) (sine-sequence-converges y)))

  cos-close : AsymptoticallyClose (λ n → embedMetricℚ (cosinePartialRHS x y n)) (cosineSequence (x Q.+ y))
  cos-close k = ∣ Tail.cutoffOffset Nat.+ k , (λ n hn →
    within-intro (constantCauchy (cosinePartialRHS x y n)) (constantCauchy (cosinePartialSum (x Q.+ y) n)) k
      (constant-difference-eventual (cosinePartialRHS x y n) (cosinePartialSum (x Q.+ y) n) k
        (Tail.cosine-addition-all-later x y x-bound y-bound k n hn))) ∣₁

  sin-close : AsymptoticallyClose (λ n → embedMetricℚ (sinePartialRHS x y n)) (sineSequence (x Q.+ y))
  sin-close k = ∣ Tail.cutoffOffset Nat.+ k , (λ n hn →
    within-intro (constantCauchy (sinePartialRHS x y n)) (constantCauchy (sinePartialSum (x Q.+ y) n)) k
      (constant-difference-eventual (sinePartialRHS x y n) (sinePartialSum (x Q.+ y) n) k
        (Tail.sine-addition-all-later x y x-bound y-bound k n hn))) ∣₁

abstract
  rational-cosine-addition : (x y : Q.ℚ) →
    completionCosine (embedMetricℚ (x Q.+ y)) ≡ cosineAdditionRHS (embedMetricℚ x) (embedMetricℚ y)
  rational-cosine-addition x y = sym (close-limits-equal
    (λ n → embedMetricℚ (cosinePartialRHS x y n)) (cosineSequence (x Q.+ y))
    (cosineAdditionRHS (embedMetricℚ x) (embedMetricℚ y)) (completionCosine (embedMetricℚ (x Q.+ y)))
    (AtPair.cos-rhs-limit x y) (cosine-sequence-converges (x Q.+ y)) (AtPair.cos-close x y))

  rational-sine-addition : (x y : Q.ℚ) →
    completionSine (embedMetricℚ (x Q.+ y)) ≡ sineAdditionRHS (embedMetricℚ x) (embedMetricℚ y)
  rational-sine-addition x y = sym (close-limits-equal
    (λ n → embedMetricℚ (sinePartialRHS x y n)) (sineSequence (x Q.+ y))
    (sineAdditionRHS (embedMetricℚ x) (embedMetricℚ y)) (completionSine (embedMetricℚ (x Q.+ y)))
    (AtPair.sin-rhs-limit x y) (sine-sequence-converges (x Q.+ y)) (AtPair.sin-close x y))
