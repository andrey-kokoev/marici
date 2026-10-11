{-# OPTIONS --safe --cubical --guardedness #-}
module TickConstructedUnitaryHalfTurn where

open import Cubical.Foundations.Prelude
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (oneCompletion)
open import ConstructiveComplexCompletion using (complex; oneComplex)
open import TickCompletionPhase using (phase; phase-start)
open import TickMachinPiEndpointContract using (machinPi)
open import TickMachinEndpoints using (machin-phase-half-turn)
open import TickConstructedUnitCircleFlow

-- Opaque presentations avoid expanding operational schedules during record
-- positivity checking. Public paths expose the exact endpoint obligations.
abstract
  MachinStartLaw MachinFinishLaw : Type
  MachinStartLaw = phase machinPi zeroCompletion ≡ oneComplex
  MachinFinishLaw = phase machinPi oneCompletion ≡ complex (-completion oneCompletion) zeroCompletion

  machin-start-law-definition : MachinStartLaw ≡ (phase machinPi zeroCompletion ≡ oneComplex)
  machin-start-law-definition = refl
  machin-finish-law-definition : MachinFinishLaw ≡
    (phase machinPi oneCompletion ≡ complex (-completion oneCompletion) zeroCompletion)
  machin-finish-law-definition = refl

  constructed-machin-start : MachinStartLaw
  constructed-machin-start = phase-start machinPi
  constructed-machin-finish : MachinFinishLaw
  constructed-machin-finish = machin-phase-half-turn

-- The flow's public law definitions quantify over every scale, including the
-- SAME machinPi used in both endpoint fields. Standard-real identification
-- is deliberately not asserted by this Agda type; its accepted proof is external.
record OperationalMachinHalfTurn : Type where
  field
    flow : OperationalUnitCircleFlow
    start : MachinStartLaw
    finish : MachinFinishLaw

abstract
  operational-machin-half-turn : OperationalMachinHalfTurn
  operational-machin-half-turn .OperationalMachinHalfTurn.flow = operational-unit-circle-flow
  operational-machin-half-turn .OperationalMachinHalfTurn.start = constructed-machin-start
  operational-machin-half-turn .OperationalMachinHalfTurn.finish = constructed-machin-finish
