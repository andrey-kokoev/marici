{-# OPTIONS --safe --cubical --guardedness #-}
module TickRotorQuarterTurn where
open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence
open import CauchyNegation using (-completion_)
open import CauchyCompletionCommRing
open import TickRotationDefectTransport using (_⊗_)
open import TickMachinEndpointReduction using (imaginaryRotor)
module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  real : (a b : fst R) → 0r · a + (- (1r · b)) ≡ - b
  real a b = solve! R
  imaginary : (a b : fst R) → 0r · b + 1r · a ≡ a
  imaginary a b = solve! R
abstract
  quarter-turn-components : (a b : MetricCompletionCandidate) → imaginaryRotor ⊗ (a , b) ≡ ((-completion b) , a)
  quarter-turn-components a b = cong₂ _,_ (Algebra.real CompletionCommRing a b) (Algebra.imaginary CompletionCommRing a b)
