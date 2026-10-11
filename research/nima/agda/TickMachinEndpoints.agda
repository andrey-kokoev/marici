{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinEndpoints where

open import Cubical.Foundations.Prelude
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (oneCompletion)
open import ConstructiveComplexCompletion using (complex)
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (MachinEndpoints; machinPi; machin-endpoints-to-phase)
open import TickMachinEndpointReduction using (machin-endpoints-from-rational)
open import TickMachinRationalGate using (rational-machin-gate)

-- Exact operational endpoints of the constructed Machin candidate.
-- Identification with standard pi is a separate remaining obligation.
abstract
  machin-endpoints : MachinEndpoints
  machin-endpoints = machin-endpoints-from-rational rational-machin-gate

  machin-phase-half-turn : phase machinPi oneCompletion ≡ complex (-completion oneCompletion) zeroCompletion
  machin-phase-half-turn = machin-endpoints-to-phase machin-endpoints
