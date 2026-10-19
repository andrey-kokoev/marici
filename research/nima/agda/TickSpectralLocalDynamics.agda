{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralLocalDynamics where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Sigma using (Σ)
open import Cubical.HITs.PropositionalTruncation as PT
open import CauchyMetricEquivalence using (MetricCompletionCandidate; embedMetricℚ)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import TickCompletionDerivative
open import TickCompletionCoefficientBound using (precisionSquared)
open import TickComplexAffineDerivative using (affine-metric-derivative)
open import TickCompletionPhase using (phase)
open import TickPhaseMetricRegularity using (phaseGenerator)
open import TickConstructedPhaseDerivative using (operational-phase-derivative)
open import TickMachinPiEndpointContract using (machinPi)
open import TickSpectralLocalContinuity using (Control; combine; VectorMetricContinuous; left-local-metric-continuous; right-local-metric-continuous)
import TickSpectralLocalOperators as L
import TickSpectralLocalUnitary as U
import TickSpectralHamiltonian as H
module V = L.V

-- Derivative in the finite product metric: one precision controls every
-- coordinate remainder for every completion-valued increment, including 0.
HasVectorMetricDerivative : (MetricCompletionCandidate → V.Vector) → MetricCompletionCandidate → V.Vector → Type
HasVectorMetricDerivative f t v = (k : ℕ) → Control zeroCompletion (λ h → (j : V.Label) →
  CompletionLE (complexNormSquared (firstOrderRemainder (λ s → f s j) t (v j) h))
    (preferredCompletionMultiplication (embedMetricℚ (precisionSquared k)) (squareCompletion h)))

vector-derivative-from-coordinates : {f : MetricCompletionCandidate → V.Vector}
  {t : MetricCompletionCandidate} {v : V.Vector} →
  ((j : V.Label) → HasMetricDerivative (λ s → f s j) t (v j)) → HasVectorMetricDerivative f t v
vector-derivative-from-coordinates derivatives k = PT.map
  (λ { (l , hl) → l , λ h near → λ
    { (false , false) → fst (fst (hl h near))
    ; (false , true) → snd (fst (hl h near))
    ; (true , false) → fst (snd (hl h near))
    ; (true , true) → snd (snd (hl h near)) } })
  (combine (combine (derivatives (false , false) k) (derivatives (false , true) k))
    (combine (derivatives (true , false) k) (derivatives (true , true) k)))

abstract
  local-vector-derivative : (P : V.Vector → V.Vector) (t : MetricCompletionCandidate) (v : V.Vector) →
    HasVectorMetricDerivative (λ s → L.local P s v) t (H.localDerivativeCandidate P t v)
  local-vector-derivative P t v = vector-derivative-from-coordinates
    {f = λ s → L.local P s v} {t = t} {v = H.localDerivativeCandidate P t v} λ j →
    affine-metric-derivative (L.positiveProjector P v j) (L.negativeProjector P v j)
      (phase machinPi) t (phaseGenerator machinPi t) (operational-phase-derivative machinPi t)

  left-hamiltonian-derivative : (t : MetricCompletionCandidate) (v : V.Vector) →
    HasVectorMetricDerivative (λ s → L.leftLocal s v) t (V.scale H.minusI (H.hamiltonian V.left (L.leftLocal t v)))
  left-hamiltonian-derivative t v = subst (HasVectorMetricDerivative (λ s → L.leftLocal s v) t)
    (H.left-generator-formula t v) (local-vector-derivative V.left t v)
  right-hamiltonian-derivative : (t : MetricCompletionCandidate) (v : V.Vector) →
    HasVectorMetricDerivative (λ s → L.rightLocal s v) t (V.scale H.minusI (H.hamiltonian V.right (L.rightLocal t v)))
  right-hamiltonian-derivative t v = subst (HasVectorMetricDerivative (λ s → L.rightLocal s v) t)
    (H.right-generator-formula t v) (local-vector-derivative V.right t v)

-- Generic predicate parameters keep record checking from unfolding schedules.
module Certificate (Time Vector : Type)
  (Unitary : (Vector → Vector) → Type)
  (Continuous : (Time → Vector) → Type)
  (Derivative : (Time → Vector) → Time → Vector → Type) where
  record LocalDynamics (flow generator : Time → Vector → Vector) : Type where
    field
      unitary : (t : Time) → Unitary (flow t)
      continuous : (v : Vector) → Continuous (λ t → flow t v)
      derivative : (t : Time) (v : Vector) → Derivative (λ s → flow s v) t (generator t v)

module Operational = Certificate MetricCompletionCandidate V.Vector U.Operational.LinearNormEquivalence
  VectorMetricContinuous HasVectorMetricDerivative
open Operational using (LocalDynamics)

leftGenerator rightGenerator : MetricCompletionCandidate → V.Vector → V.Vector
leftGenerator t v = V.scale H.minusI (H.hamiltonian V.left (L.leftLocal t v))
rightGenerator t v = V.scale H.minusI (H.hamiltonian V.right (L.rightLocal t v))

abstract
  left-local-dynamics : LocalDynamics L.leftLocal leftGenerator
  left-local-dynamics .LocalDynamics.unitary = U.left-local-unitary
  left-local-dynamics .LocalDynamics.continuous = left-local-metric-continuous
  left-local-dynamics .LocalDynamics.derivative = left-hamiltonian-derivative
  right-local-dynamics : LocalDynamics L.rightLocal rightGenerator
  right-local-dynamics .LocalDynamics.unitary = U.right-local-unitary
  right-local-dynamics .LocalDynamics.continuous = right-local-metric-continuous
  right-local-dynamics .LocalDynamics.derivative = right-hamiltonian-derivative
