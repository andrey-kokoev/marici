{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinEndpointReduction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionCommRing
open import TickRotationDefectTransport using (Rotor; _⊗_)
open import TickOperationalRotorIncrement using (rotation; rotation-addition)
open import TickCayleyRotorComposition using (rotor-assoc; rotor-right-unit)
open import TickOperationalCayleyIdentity using (unitRotor; rotation-zero; rotor-comm; rotor-left-unit)
open import TickMachinCayleyInputs using (gridCayley; machin-fifth-cayley; machin239-cayley)
open import TickMachinPiEndpointContract using (MachinEndpoints; machinPi; machin-pi-formula; atanFifth; atan239th; fourCompletion)

square : Rotor → Rotor
square z = z ⊗ z
imaginaryRotor negativeUnit : Rotor
imaginaryRotor = embedMetricℚ 0 , embedMetricℚ 1
negativeUnit = -completion (embedMetricℚ 1) , embedMetricℚ 0

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  cancel : (a b : fst R) → (a +S (-S b)) +S b ≡ a
  cancel a b = solve! R
  inverse : (a : fst R) → a +S (-S a) ≡ 0r
  inverse a = solve! R
  square-i-real : 0r ·S 0r +S (-S (1r ·S 1r)) ≡ -S 1r
  square-i-real = solve! R
  square-i-imaginary : 0r ·S 1r +S 1r ·S 0r ≡ 0r
  square-i-imaginary = solve! R
  square-minus-real : (-S 1r) ·S (-S 1r) +S (-S (0r ·S 0r)) ≡ 1r
  square-minus-real = solve! R
  square-minus-imaginary : (-S 1r) ·S 0r +S 0r ·S (-S 1r) ≡ 0r
  square-minus-imaginary = solve! R
  machin-angle : (a b : fst R) →
    (((a +S a) +S (a +S a)) +S ((a +S a) +S (a +S a))) +S (-S (b +S b)) +S
      ((((a +S a) +S (a +S a)) +S ((a +S a) +S (a +S a))) +S (-S (b +S b))) ≡
    ((((a +S a) +S (a +S a)) +S ((a +S a) +S (a +S a))) +S
      (((a +S a) +S (a +S a)) +S ((a +S a) +S (a +S a)))) +S (-S ((b +S b) +S (b +S b)))
  machin-angle a b = solve! R
module C = Algebra CompletionCommRing

abstract
  rotation-inverse : (a : MetricCompletionCandidate) → rotation a ⊗ rotation (-completion a) ≡ unitRotor
  rotation-inverse a = sym (rotation-addition a (-completion a)) ∙ cong rotation (C.inverse a) ∙ rotation-zero

  rotor-cancel-right : (a b z zi : Rotor) → z ⊗ zi ≡ unitRotor → a ⊗ z ≡ b ⊗ z → a ≡ b
  rotor-cancel-right a b z zi inverse equation = sym (rotor-right-unit a)
    ∙ cong (a ⊗_) (sym inverse) ∙ sym (rotor-assoc a z zi)
    ∙ cong (_⊗ zi) equation ∙ rotor-assoc b z zi ∙ cong (b ⊗_) inverse ∙ rotor-right-unit b

  rotation-difference : (a b : MetricCompletionCandidate) (z : Rotor) → rotation a ≡ z ⊗ rotation b →
    rotation (a +completion (-completion b)) ≡ z
  rotation-difference a b z equation = rotor-cancel-right (rotation (a +completion (-completion b))) z
    (rotation b) (rotation (-completion b)) (rotation-inverse b)
    (sym (rotation-addition (a +completion (-completion b)) b) ∙ cong rotation (C.cancel a b) ∙ equation)

  square-imaginary : square imaginaryRotor ≡ negativeUnit
  square-imaginary = cong₂ _,_ C.square-i-real C.square-i-imaginary
  square-negative-unit : square negativeUnit ≡ unitRotor
  square-negative-unit = cong₂ _,_ C.square-minus-real C.square-minus-imaginary

  negative-half-turn : (a : MetricCompletionCandidate) → rotation a ≡ negativeUnit → rotation (-completion a) ≡ negativeUnit
  negative-half-turn a ha = rotor-cancel-right (rotation (-completion a)) negativeUnit negativeUnit negativeUnit
    square-negative-unit
    (cong (rotation (-completion a) ⊗_) (sym ha)
      ∙ rotor-comm (rotation (-completion a)) (rotation a) ∙ rotation-inverse a ∙ sym square-negative-unit)

  rotation-four : (a : MetricCompletionCandidate) → rotation (fourCompletion a) ≡ square (square (rotation a))
  rotation-four a = rotation-addition (a +completion a) (a +completion a)
    ∙ cong square (rotation-addition a a)

-- The only remaining hypothesis in this reduction is a concrete rational
-- rotor equality. No addition, inverse-trig, or endpoint law is assumed.
RationalMachinGate : Type
RationalMachinGate = square (square (gridCayley 1 4)) ≡ imaginaryRotor ⊗ gridCayley 1 238

machin-endpoints-from-rational : RationalMachinGate → MachinEndpoints
machin-endpoints-from-rational gate = cong fst result , cong snd result
  where
  a : MetricCompletionCandidate
  a = atanFifth +completion atanFifth
  b : MetricCompletionCandidate
  b = atan239th +completion atan239th
  quarter : MetricCompletionCandidate
  quarter = fourCompletion a +completion (-completion b)
  quarter-rotation : rotation quarter ≡ imaginaryRotor
  quarter-rotation = rotation-difference (fourCompletion a) b imaginaryRotor
    (rotation-four a ∙ cong (λ z → square (square z)) machin-fifth-cayley
      ∙ gate ∙ cong (imaginaryRotor ⊗_) (sym machin239-cayley))
  pi-angle : quarter +completion quarter ≡ machinPi
  pi-angle = C.machin-angle atanFifth atan239th ∙ sym machin-pi-formula
  pi-rotation : rotation machinPi ≡ negativeUnit
  pi-rotation = cong rotation (sym pi-angle) ∙ rotation-addition quarter quarter
    ∙ cong square quarter-rotation ∙ square-imaginary
  result : rotation (-completion machinPi) ≡ negativeUnit
  result = negative-half-turn machinPi pi-rotation
