{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralGlobalPath where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Sigma using (Σ)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import ConstructiveComplexCompletion
open import TickCompletionMetric
open import TickCompletionDerivative using (CompletionLE)
open import TickCompletionRingContinuity using (negation-metric-continuous)
open import TickPhaseMetricContinuity using
  (ComplexMetricContinuous; phase-real-metric-continuous; phase-imaginary-metric-continuous)
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
open import TickCompletionClippedTime using
  (firstTime; secondTime; afterOne; first-time-continuous; second-time-continuous;
   first-on-left; second-on-left; first-on-right; second-on-right)
import TickCompletionMetricInterval as I
import TickSpectralLocalOperators as L
import TickSpectralLocalContinuity as C
import TickSpectralProjectorLaws as P
import TickSpectralLocalNorm as N
module V = L.V

IndexMap : Type
IndexMap = V.Label → V.Label
permute : IndexMap → V.Vector → V.Vector
permute k v j = v (k j)

-- Positive continuation in order a then b, NOT an inverse-phase return.
glued : IndexMap → IndexMap → MetricCompletionCandidate → V.Vector → V.Vector
glued a b t v = L.local (permute b) (secondTime t) (L.local (permute a) (firstTime t) v)
intervalPath : IndexMap → IndexMap → V.Vector → I.ReturnInterval → V.Vector
intervalPath a b v t = glued a b (fst t) v

complex-negative-continuous : {f : MetricCompletionCandidate → ComplexCompletion} →
  ComplexMetricContinuous f → ComplexMetricContinuous (λ t → negComplex (f t))
complex-negative-continuous fc = C.complex-components
  (compose-metric-continuous negation-metric-continuous (C.real-continuous fc))
  (compose-metric-continuous negation-metric-continuous (C.imaginary-continuous fc))

moving-local-continuous : (a : IndexMap) (s : MetricCompletionCandidate → MetricCompletionCandidate)
  (w : MetricCompletionCandidate → V.Vector) → MetricContinuous s →
  ((j : V.Label) → ComplexMetricContinuous (λ t → w t j)) →
  (j : V.Label) → ComplexMetricContinuous (λ t → L.local (permute a) (s t) (w t) j)
moving-local-continuous a s w sc wc j = C.complex-add-continuous
  (C.complex-product-continuous (C.complex-constant-continuous L.halfComplex)
    (C.complex-add-continuous (wc j) (wc (a j))))
  (C.complex-product-continuous
    (C.complex-components
      (compose-metric-continuous (phase-real-metric-continuous machinPi) sc)
      (compose-metric-continuous (phase-imaginary-metric-continuous machinPi) sc))
    (C.complex-product-continuous (C.complex-constant-continuous L.halfComplex)
      (C.complex-add-continuous (wc j) (complex-negative-continuous (wc (a j))))))

IntervalPathContinuous : (I.ReturnInterval → V.Vector) → Type
IntervalPathContinuous f = (t : I.ReturnInterval) (k : ℕ) →
  ∥ Σ ℕ (λ l → (u : I.ReturnInterval) → CompletionWithin (fst t) (fst u) l → C.VectorWithin (f t) (f u) k) ∥₁

abstract
  glued-metric-continuous : (a b : IndexMap) (v : V.Vector) → C.VectorMetricContinuous (λ t → glued a b t v)
  glued-metric-continuous a b v = C.vector-from-coordinates {f = λ t → glued a b t v}
    (moving-local-continuous b secondTime (λ t → L.local (permute a) (firstTime t) v) second-time-continuous
      (moving-local-continuous a firstTime (λ _ → v) first-time-continuous
        (λ j → C.complex-constant-continuous (v j))))

  interval-path-continuous : (a b : IndexMap) (v : V.Vector) → IntervalPathContinuous (intervalPath a b v)
  interval-path-continuous a b v t k = PT.map
    (λ { (l , control) → l , λ u near → control (fst u) near }) (glued-metric-continuous a b v (fst t) k)

  glued-on-left : (a b : IndexMap) (t : MetricCompletionCandidate) (v : V.Vector) →
    CompletionLE t oneCompletion → glued a b t v ≡ L.local (permute a) t v
  glued-on-left a b t v bound = cong₂ (λ s u → L.local (permute b) s (L.local (permute a) u v))
    (second-on-left t bound) (first-on-left t bound)
    ∙ L.local-start (permute b) (L.local (permute a) t v)

  glued-on-right : (a b : IndexMap) (t : MetricCompletionCandidate) (v : V.Vector) →
    CompletionLE oneCompletion t → glued a b t v ≡ L.local (permute b) (afterOne t) (permute a v)
  glued-on-right a b t v bound = cong₂ (λ s u → L.local (permute b) s (L.local (permute a) u v))
    (second-on-right t bound) (first-on-right t bound)
    ∙ cong (L.local (permute b) (afterOne t)) (L.local-finish (permute a) v)

  interval-start : (a b : IndexMap) (v : V.Vector) → intervalPath a b v I.start ≡ v
  interval-start a b v = glued-on-left a b zeroCompletion v I.zero≤one ∙ L.local-start (permute a) v

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    after-two : (1r + 1r) + (- 1r) ≡ 1r
    after-two = solve! R
module A = Algebra CompletionCommRing

abstract
  interval-finish : (a b : IndexMap) (v : V.Vector) → intervalPath a b v I.finish ≡ permute b (permute a v)
  interval-finish a b v = glued-on-right a b I.twoCompletion v I.one≤two
    ∙ cong (λ t → L.local (permute b) t (permute a v)) A.after-two
    ∙ L.local-finish (permute b) (permute a v)

  left-then-right-norm : (t : MetricCompletionCandidate) (v : V.Vector) →
    N.vectorNormSquared (glued P.leftIndex P.rightIndex t v) ≡ N.vectorNormSquared v
  left-then-right-norm t v = N.right-local-norm (secondTime t) (L.leftLocal (firstTime t) v)
    ∙ N.left-local-norm (firstTime t) v
  right-then-left-norm : (t : MetricCompletionCandidate) (v : V.Vector) →
    N.vectorNormSquared (glued P.rightIndex P.leftIndex t v) ≡ N.vectorNormSquared v
  right-then-left-norm t v = N.left-local-norm (secondTime t) (L.rightLocal (firstTime t) v)
    ∙ N.right-local-norm (firstTime t) v
