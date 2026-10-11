{-# OPTIONS --safe --cubical --guardedness #-}
module TickConstructedUnitCircleFlow where

open import Cubical.Foundations.Prelude
open import CauchyMetricEquivalence
open import CauchyCompletionCommRing using (oneCompletion)
import TickPhaseNormTransfer as Norm
open import TickCompletionPhase
open import TickPhaseMetricRegularity
open import TickConstructedScheduledNorm using (operational-phase-unit-norm)
open import TickConstructedPhaseDerivative using (operational-phase-metric-regularity)

-- Opaque law presentations prevent record positivity checking from unfolding
-- the operational Taylor schedules. Public paths specify their exact types.
abstract
  UnitNormLaw RegularityLaw : Type
  UnitNormLaw = (p t : MetricCompletionCandidate) → Norm.normSquared (phase p t) ≡ oneCompletion
  RegularityLaw = PhaseMetricRegularity

  unit-norm-law-definition : UnitNormLaw ≡ ((p t : MetricCompletionCandidate) → Norm.normSquared (phase p t) ≡ oneCompletion)
  unit-norm-law-definition = refl
  regularity-law-definition : RegularityLaw ≡ PhaseMetricRegularity
  regularity-law-definition = refl

  constructed-unit-norm : UnitNormLaw
  constructed-unit-norm = operational-phase-unit-norm
  constructed-regularity : RegularityLaw
  constructed-regularity = operational-phase-metric-regularity

-- Both fields are laws of the SAME fixed operational phase, not witnesses
-- of separately chosen curves or an alternate real-number interpretation.
record OperationalUnitCircleFlow : Type where
  field
    unit-norm : UnitNormLaw
    metric-regularity : RegularityLaw

abstract
  operational-unit-circle-flow : OperationalUnitCircleFlow
  operational-unit-circle-flow .OperationalUnitCircleFlow.unit-norm = constructed-unit-norm
  operational-unit-circle-flow .OperationalUnitCircleFlow.metric-regularity = constructed-regularity
