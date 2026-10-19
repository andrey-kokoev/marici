{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionClippedTime where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import TickCompletionMetric
open import TickCompletionDerivative using (CompletionLE; CompletionNonnegative)
open import TickCompletionRingContinuity
open import TickCompletionPositivePart using
  (positiveCompletion; positive-metric-continuous; positive-vanishes-nonpositive; positive-fixes-nonnegative)

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    negative-difference : (t : fst R) → - (t + (- 1r)) ≡ 1r + (- t)
    negative-difference t = solve! R
    subtract-zero : (t : fst R) → t + (- 0r) ≡ t
    subtract-zero t = solve! R
    subtract-difference : (t : fst R) → t + (- (t + (- 1r))) ≡ 1r
    subtract-difference t = solve! R
module A = Algebra CompletionCommRing

afterOne firstTime secondTime : MetricCompletionCandidate → MetricCompletionCandidate
afterOne t = t +completion (-completion oneCompletion)
secondTime t = positiveCompletion (afterOne t)
firstTime t = t +completion (-completion (secondTime t))

abstract
  after-one-continuous : MetricContinuous afterOne
  after-one-continuous = joint-compose-continuous _+completion_ (λ t → t) (λ _ → -completion oneCompletion)
    addition-joint-continuous identity-metric-continuous (constant-metric-continuous (-completion oneCompletion))
  second-time-continuous : MetricContinuous secondTime
  second-time-continuous = compose-metric-continuous positive-metric-continuous after-one-continuous
  first-time-continuous : MetricContinuous firstTime
  first-time-continuous = joint-compose-continuous _+completion_ (λ t → t) (λ t → -completion (secondTime t))
    addition-joint-continuous identity-metric-continuous
    (compose-metric-continuous negation-metric-continuous second-time-continuous)

  second-on-left : (t : MetricCompletionCandidate) → CompletionLE t oneCompletion → secondTime t ≡ zeroCompletion
  second-on-left t bound = positive-vanishes-nonpositive (afterOne t)
    (subst CompletionNonnegative (sym (A.negative-difference t)) bound)
  first-on-left : (t : MetricCompletionCandidate) → CompletionLE t oneCompletion → firstTime t ≡ t
  first-on-left t bound = cong (λ s → t +completion (-completion s)) (second-on-left t bound) ∙ A.subtract-zero t
  second-on-right : (t : MetricCompletionCandidate) → CompletionLE oneCompletion t → secondTime t ≡ afterOne t
  second-on-right t bound = positive-fixes-nonnegative (afterOne t) bound
  first-on-right : (t : MetricCompletionCandidate) → CompletionLE oneCompletion t → firstTime t ≡ oneCompletion
  first-on-right t bound = cong (λ s → t +completion (-completion s)) (second-on-right t bound) ∙ A.subtract-difference t
