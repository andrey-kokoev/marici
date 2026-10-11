{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralLocalInverse where

open import Cubical.Foundations.Prelude
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import ConstructiveComplexCompletion
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
open import TickConstructedScheduledNorm using (operational-phase-unit-norm)
import TickComplexCompletionRing as Ring
import TickComplexConjugation as Conj
import TickSpectralLocalOperators as L
import TickSpectralProjectorLaws as P

abstract
  phase-right-inverse : (p t : MetricCompletionCandidate) →
    phase p t ·complex conjugateComplex (phase p t) ≡ oneComplex
  phase-right-inverse p t = Conj.Operational.conjugate-product (phase p t)
    ∙ cong Conj.Operational.real (operational-phase-unit-norm p t)

  phase-left-inverse : (p t : MetricCompletionCandidate) →
    conjugateComplex (phase p t) ·complex phase p t ≡ oneComplex
  phase-left-inverse p t = Ring.Operational.mul-comm (conjugateComplex (phase p t)) (phase p t)
    ∙ phase-right-inverse p t

leftInverse rightInverse : MetricCompletionCandidate → L.V.Vector → L.V.Vector
leftInverse t = P.Left.spectral (conjugateComplex (phase machinPi t))
rightInverse t = P.Right.spectral (conjugateComplex (phase machinPi t))

abstract
  left-spectral-one : (v : L.V.Vector) → P.Left.spectral oneComplex v ≡ v
  left-spectral-one v = funExt λ j → L.A.at-one L.halfComplex L.halfComplex-double (v j) (L.V.left v j)
  right-spectral-one : (v : L.V.Vector) → P.Right.spectral oneComplex v ≡ v
  right-spectral-one v = funExt λ j → L.A.at-one L.halfComplex L.halfComplex-double (v j) (L.V.right v j)

  left-inverse-after : (t : MetricCompletionCandidate) (v : L.V.Vector) → leftInverse t (L.leftLocal t v) ≡ v
  left-inverse-after t v = P.Left.spectral-composition (conjugateComplex (phase machinPi t)) (phase machinPi t) v
    ∙ cong (λ z → P.Left.spectral z v) (phase-left-inverse machinPi t) ∙ left-spectral-one v
  left-inverse-before : (t : MetricCompletionCandidate) (v : L.V.Vector) → L.leftLocal t (leftInverse t v) ≡ v
  left-inverse-before t v = P.Left.spectral-composition (phase machinPi t) (conjugateComplex (phase machinPi t)) v
    ∙ cong (λ z → P.Left.spectral z v) (phase-right-inverse machinPi t) ∙ left-spectral-one v
  right-inverse-after : (t : MetricCompletionCandidate) (v : L.V.Vector) → rightInverse t (L.rightLocal t v) ≡ v
  right-inverse-after t v = P.Right.spectral-composition (conjugateComplex (phase machinPi t)) (phase machinPi t) v
    ∙ cong (λ z → P.Right.spectral z v) (phase-left-inverse machinPi t) ∙ right-spectral-one v
  right-inverse-before : (t : MetricCompletionCandidate) (v : L.V.Vector) → L.rightLocal t (rightInverse t v) ≡ v
  right-inverse-before t v = P.Right.spectral-composition (phase machinPi t) (conjugateComplex (phase machinPi t)) v
    ∙ cong (λ z → P.Right.spectral z v) (phase-right-inverse machinPi t) ∙ right-spectral-one v
