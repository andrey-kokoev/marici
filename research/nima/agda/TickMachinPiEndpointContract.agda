{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinPiEndpointContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (oneCompletion)
open import ConstructiveComplexCompletion
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionPhase
open import TickMachinPiCandidate public
import TickMachinRotationIdentity

-- These exact endpoint equalities are still open. Constructing the
-- convergent Machin series or checking rational rotations does not fill them.
MachinEndpoints : Type
MachinEndpoints =
  (completionCosine (-completion machinPi) ≡ (-completion oneCompletion)) ×
  (completionSine (-completion machinPi) ≡ zeroCompletion)

abstract
  machin-endpoints-to-phase : MachinEndpoints →
    phase machinPi oneCompletion ≡ complex (-completion oneCompletion) zeroCompletion
  machin-endpoints-to-phase endpoints = phase-finish-components machinPi
    ∙ complex-ext _ _ (fst endpoints) (snd endpoints)
