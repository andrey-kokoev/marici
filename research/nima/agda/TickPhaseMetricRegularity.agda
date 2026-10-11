{-# OPTIONS --safe --cubical --guardedness #-}
module TickPhaseMetricRegularity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_)
open import CauchyMetricEquivalence
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import ConstructiveComplexCompletion
open import TickCompletionPhase
open import TickCompletionDerivative public
open import TickPhaseMetricContinuity public

phaseGenerator : MetricCompletionCandidate → MetricCompletionCandidate → ComplexCompletion
phaseGenerator p t = complex zeroCompletion (-completion p) ·complex phase p t

PhaseDerivativeLaw : Type
PhaseDerivativeLaw = (p t : MetricCompletionCandidate) → HasMetricDerivative (phase p) t (phaseGenerator p t)

-- The exact full goal, NOT a claimed inhabitant. Continuity is constructed;
-- the all-increment first-order remainder estimate is still OPEN.
PhaseMetricRegularity : Type
PhaseMetricRegularity =
  ((p : MetricCompletionCandidate) → ComplexMetricContinuous (phase p)) × PhaseDerivativeLaw
