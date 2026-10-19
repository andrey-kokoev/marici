{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionMetricInterval where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Sigma using (Σ; _×_; Σ≡Prop)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Data.Rationals as Q hiding (_+_; _·_; -_)
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure using (precision-nonnegative; ≤-add-nonnegative)
open import CauchyMetricEquivalence using (MetricCompletionCandidate; embedMetricℚ)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import CauchyRationalEmbedding using (embedℚ-preserves-sum)
open import TickCompletionMetric
open import Cubical.HITs.PropositionalTruncation as PT
open import TickCompletionRingContinuity using
  (joint-compose-continuous; addition-joint-continuous; identity-metric-continuous; constant-metric-continuous)
open import TickCompletionDerivative using (CompletionLE; CompletionNonnegative)
open import TickCompletionOrderLimits using (completion-nonnegative-isProp)
open import TickCompletionOrderArithmetic using (completion-order-refl; completion-order-trans)
open import TickCompletionCoefficientBound using (embedded-order)

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    translation : (a b c : fst R) → (b + c) + (- (a + c)) ≡ b + (- a)
    translation a b c = solve! R
    zero-plus : (a : fst R) → 0r + a ≡ a
    zero-plus a = solve! R
module A = Algebra CompletionCommRing

abstract
  order-translate : (a b c : MetricCompletionCandidate) → CompletionLE a b →
    CompletionLE (a +completion c) (b +completion c)
  order-translate a b c bound = subst CompletionNonnegative (sym (A.translation a b c)) bound

Interval : MetricCompletionCandidate → MetricCompletionCandidate → Type
Interval a b = Σ MetricCompletionCandidate (λ t → CompletionLE a t × CompletionLE t b)

interval-bounds-isProp : (a b t : MetricCompletionCandidate) → isProp (CompletionLE a t × CompletionLE t b)
interval-bounds-isProp a b t = isProp×
  (completion-nonnegative-isProp (t +completion (-completion a)))
  (completion-nonnegative-isProp (b +completion (-completion t)))

interval-ext : {a b : MetricCompletionCandidate} (s t : Interval a b) → fst s ≡ fst t → s ≡ t
interval-ext {a} {b} s t = Σ≡Prop (interval-bounds-isProp a b)

-- Metric balls are inherited from the actual completion coordinate.
IntervalWithin : {a b : MetricCompletionCandidate} → Interval a b → Interval a b → ℕ → Type
IntervalWithin s t k = CompletionWithin (fst s) (fst t) k
interval-separated : {a b : MetricCompletionCandidate} (s t : Interval a b) →
  ((k : ℕ) → IntervalWithin {a} {b} s t k) → s ≡ t
interval-separated {a} {b} s t near = interval-ext {a} {b} s t (within-separated (fst s) (fst t) near)

twoCompletion : MetricCompletionCandidate
twoCompletion = oneCompletion +completion oneCompletion
UnitInterval ReturnInterval : Type
UnitInterval = Interval zeroCompletion oneCompletion
ReturnInterval = Interval zeroCompletion twoCompletion

abstract
  zero≤one : CompletionLE zeroCompletion oneCompletion
  zero≤one = embedded-order 0 1 (precision-nonnegative 0)
  one≤two : CompletionLE oneCompletion twoCompletion
  one≤two = subst (CompletionLE oneCompletion) (embedℚ-preserves-sum 1 1)
    (embedded-order 1 (1 Q.+ 1) (≤-add-nonnegative 1 1 (precision-nonnegative 0)))
  zero≤two : CompletionLE zeroCompletion twoCompletion
  zero≤two = completion-order-trans zeroCompletion oneCompletion twoCompletion zero≤one one≤two

unitStart unitFinish : UnitInterval
unitStart = zeroCompletion , completion-order-refl zeroCompletion , zero≤one
unitFinish = oneCompletion , zero≤one , completion-order-refl oneCompletion
start seam finish : ReturnInterval
start = zeroCompletion , completion-order-refl zeroCompletion , zero≤two
seam = oneCompletion , zero≤one , one≤two
finish = twoCompletion , zero≤two , completion-order-refl twoCompletion

leftChart rightChart : UnitInterval → ReturnInterval
leftChart (t , lower , upper) = t , lower , completion-order-trans t oneCompletion twoCompletion upper one≤two
rightChart (t , lower , upper) = (t +completion oneCompletion) ,
  completion-order-trans zeroCompletion oneCompletion (t +completion oneCompletion) zero≤one
    (subst (λ a → CompletionLE a (t +completion oneCompletion)) (A.zero-plus oneCompletion)
      (order-translate zeroCompletion t oneCompletion lower)) ,
  order-translate t oneCompletion oneCompletion upper

-- The two closed pieces are restrictions of the real completion interval.
LeftPiece RightPiece : Type
LeftPiece = Σ ReturnInterval (λ t → CompletionLE (fst t) oneCompletion)
RightPiece = Σ ReturnInterval (λ t → CompletionLE oneCompletion (fst t))

ChartMetricContinuous : (UnitInterval → ReturnInterval) → Type
ChartMetricContinuous f = (u : UnitInterval) (k : ℕ) →
  ∥ Σ ℕ (λ l → (v : UnitInterval) → IntervalWithin {zeroCompletion} {oneCompletion} u v l → IntervalWithin {zeroCompletion} {twoCompletion} (f u) (f v) k) ∥₁

abstract
  left-chart-continuous : ChartMetricContinuous leftChart
  left-chart-continuous u k = ∣ k , (λ v near → near) ∣₁
  right-chart-continuous : ChartMetricContinuous rightChart
  right-chart-continuous u k = PT.map (λ { (l , control) → l , λ v near → control (fst v) near })
    (joint-compose-continuous _+completion_ (λ t → t) (λ _ → oneCompletion)
      addition-joint-continuous identity-metric-continuous (constant-metric-continuous oneCompletion) (fst u) k)

  left-chart-start : leftChart unitStart ≡ start
  left-chart-start = interval-ext {zeroCompletion} {twoCompletion} (leftChart unitStart) start refl
  left-chart-finish : leftChart unitFinish ≡ seam
  left-chart-finish = interval-ext {zeroCompletion} {twoCompletion} (leftChart unitFinish) seam refl
  right-chart-start : rightChart unitStart ≡ seam
  right-chart-start = interval-ext {zeroCompletion} {twoCompletion} (rightChart unitStart) seam (A.zero-plus oneCompletion)
  right-chart-finish : rightChart unitFinish ≡ finish
  right-chart-finish = interval-ext {zeroCompletion} {twoCompletion} (rightChart unitFinish) finish refl
  charts-share-seam : leftChart unitFinish ≡ rightChart unitStart
  charts-share-seam = left-chart-finish ∙ sym right-chart-start
