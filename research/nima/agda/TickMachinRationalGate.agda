{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinRationalGate where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; suc)
open import Cubical.Data.NatPlusOne using (ℕ₊₁; 1+_)
open import Cubical.Data.NatPlusOne.Properties using (_·₊₁_)
import Cubical.Data.Int as Z
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import CauchyMetricEquivalence
open import CauchyRationalEmbedding using (embedℚ-preserves-negation)
open import TickRotorQuarterTurn using (quarter-turn-components)
open import TickRotationDefectTransport using (Rotor; _⊗_)
open import TickCayleyOuterRotor using (embedded-product)
open import TickCayleyGridIncrement using (inverseIndex)
open import TickCayleyRationalNormalization
open import TickMachinCayleyInputs using (gridCayley; grid-cayley-definition)
open import TickMachinEndpointReduction using (square; imaginaryRotor; RationalMachinGate)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  turn-real : (a b : fst R) → 0r ·S a +S (-S (1r ·S b)) ≡ -S b
  turn-real a b = solve! R
  turn-imaginary : (a b : fst R) → 0r ·S b +S 1r ·S a ≡ a
  turn-imaginary a b = solve! R
module R = Algebra PreferredℚCommRing

abstract
  fractionRotor : Z.ℤ → Z.ℤ → ℕ₊₁ → Rotor
  fractionRotor a b D = embedMetricℚ Q.[ a / D ] , embedMetricℚ Q.[ b / D ]

  grid-fraction-rotor : (n d : ℕ) → gridCayley n d ≡
    fractionRotor ((Z.pos (suc d N.· suc d)) Z.+ (Z.- (Z.pos n Z.· Z.pos n)))
      ((Z.pos n Z.+ Z.pos n) Z.· Z.pos (suc d)) (1+ inverseIndex n n d)
  grid-fraction-rotor n d = grid-cayley-definition n d
    ∙ cong₂ _,_ (cong embedMetricℚ (cayley-real-fraction n d)) (cong embedMetricℚ (cayley-imaginary-fraction n d))

  cancel-two-rotor : (a b : Z.ℤ) (D : ℕ₊₁) →
    fractionRotor (Z.pos 2 Z.· a) (Z.pos 2 Z.· b) ((1+ 1) ·₊₁ D) ≡ fractionRotor a b D
  cancel-two-rotor a b D = cong₂ _,_
    (cong embedMetricℚ (cancel-two-fraction a D))
    (cong embedMetricℚ (cancel-two-fraction b D))

  square-fraction-rotor : (a b : Z.ℤ) (D : ℕ₊₁) → square (fractionRotor a b D) ≡
    fractionRotor ((a Z.· a) Z.+ (Z.- (b Z.· b))) ((a Z.· b) Z.+ (b Z.· a)) (D ·₊₁ D)
  square-fraction-rotor a b D = embedded-product Q.[ a / D ] Q.[ b / D ] Q.[ a / D ] Q.[ b / D ]
    ∙ cong₂ _,_
      (cong embedMetricℚ (cong (Q.[ a Z.· a / D ·₊₁ D ] Q.+_) (fraction-negative (b Z.· b) (D ·₊₁ D))
        ∙ same-denominator-add (a Z.· a) (Z.- (b Z.· b)) (D ·₊₁ D)))
      (cong embedMetricℚ (same-denominator-add (a Z.· b) (b Z.· a) (D ·₊₁ D)))

  quarter-turn-fraction : (a b : Z.ℤ) (D : ℕ₊₁) → imaginaryRotor ⊗ fractionRotor a b D ≡ fractionRotor (Z.- b) a D
  quarter-turn-fraction a b D = quarter-turn-components (embedMetricℚ Q.[ a / D ]) (embedMetricℚ Q.[ b / D ])
    ∙ cong (λ z → z , embedMetricℚ Q.[ a / D ]) (embedℚ-preserves-negation Q.[ b / D ] ∙ cong embedMetricℚ (fraction-negative b D))

unit-grid-fraction-rotor : (d : ℕ) → gridCayley 1 d ≡
  fractionRotor (Z.pos (d N.· (d N.+ 2))) (Z.pos (2 N.· suc d)) (1+ inverseIndex 1 1 d)
unit-grid-fraction-rotor d = grid-fraction-rotor 1 d ∙ cong₂
  (λ a b → fractionRotor a b (1+ inverseIndex 1 1 d)) (unit-real-numerator d) (unit-imaginary-numerator d)

fifth-normalized : gridCayley 1 4 ≡ fractionRotor (Z.pos 12) (Z.pos 5) (1+ 12)
fifth-normalized = grid-fraction-rotor 1 4 ∙ cancel-two-rotor (Z.pos 12) (Z.pos 5) (1+ 12)

small239-normalized : gridCayley 1 238 ≡ fractionRotor (Z.pos 28560) (Z.pos 239) (1+ 28560)
small239-normalized = unit-grid-fraction-rotor 238 ∙ cancel-two-rotor (Z.pos 28560) (Z.pos 239) (1+ 28560)

fifth-square : square (fractionRotor (Z.pos 12) (Z.pos 5) (1+ 12)) ≡ fractionRotor (Z.pos 119) (Z.pos 120) (1+ 168)
fifth-square = square-fraction-rotor (Z.pos 12) (Z.pos 5) (1+ 12)

fifth-fourth : square (fractionRotor (Z.pos 119) (Z.pos 120) (1+ 168)) ≡ fractionRotor (Z.negsuc 238) (Z.pos 28560) (1+ 28560)
fifth-fourth = square-fraction-rotor (Z.pos 119) (Z.pos 120) (1+ 168)

rational-machin-gate : RationalMachinGate
rational-machin-gate = cong (λ z → square (square z)) fifth-normalized ∙ cong square fifth-square ∙ fifth-fourth
  ∙ sym (quarter-turn-fraction (Z.pos 28560) (Z.pos 239) (1+ 28560))
  ∙ cong (imaginaryRotor ⊗_) (sym small239-normalized)
