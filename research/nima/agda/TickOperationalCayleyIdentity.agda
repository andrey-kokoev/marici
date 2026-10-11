{-# OPTIONS --safe --cubical --guardedness #-}
module TickOperationalCayleyIdentity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (one-half)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyCompletionCommRing
open import TickRotationDefectTransport using (Rotor; _⊗_)
open import TickCayleyGridIncrement using (gridValue)
open import TickCayleyOuterRotor using (cayleyRotor; inverseCayleyRotor; cayley-inverse-law; cayleyReal; cayleyImaginary)
open import TickCayleyRotorComposition using (rotor-assoc; rotor-right-unit)
open import TickOperationalRotorIncrement using (rotation; gridAngle)
open import TickCayleyConcreteTransport using (gridInvariant)
open import TickCayleyDyadicTelescoping using (zero-small)
open import TickCayleyInvariantConstancy using (invariant-constant)
open import TickAtanCompletionSlope using (atan-completion-zero)
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import OperationalAnalyticZeroLaws using (completion-cosine-zero; completion-sine-zero)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  comm-real : (a b c d : fst R) → a ·S c +S (-S (b ·S d)) ≡ c ·S a +S (-S (d ·S b))
  comm-real a b c d = solve! R
  comm-imaginary : (a b c d : fst R) → a ·S d +S b ·S c ≡ c ·S b +S d ·S a
  comm-imaginary a b c d = solve! R
module C = Algebra CompletionCommRing

unitRotor : Rotor
unitRotor = embedMetricℚ 1 , embedMetricℚ 0

abstract
  rotor-comm : (a b : Rotor) → a ⊗ b ≡ b ⊗ a
  rotor-comm (a , b) (c , d) = cong₂ _,_ (C.comm-real a b c d) (C.comm-imaginary a b c d)
  rotor-left-unit : (a : Rotor) → unitRotor ⊗ a ≡ a
  rotor-left-unit a = rotor-comm unitRotor a ∙ rotor-right-unit a

  grid-angle-zero : gridAngle zero zero zero-small ≡ embedMetricℚ 0
  grid-angle-zero = cong₂ _+completion_ (atan-completion-zero zero-small) (atan-completion-zero zero-small)
    ∙ CommRingStr.+IdL (snd CompletionCommRing) (embedMetricℚ 0)

  rotation-zero : rotation (embedMetricℚ 0) ≡ unitRotor
  rotation-zero = cong₂ _,_ completion-cosine-zero completion-sine-zero

  inverse-rotor-zero : inverseCayleyRotor zero zero ≡ unitRotor
  inverse-rotor-zero = refl

  invariant-zero : gridInvariant zero zero zero-small ≡ unitRotor
  invariant-zero = cong₂ _⊗_ (cong rotation grid-angle-zero ∙ rotation-zero) inverse-rotor-zero
    ∙ rotor-right-unit unitRotor

  -- Both sides use the implemented completion operations. Inputs are the
  -- nonnegative rational grid presentations bounded by one half.
  operational-cayley-grid : (N d : ℕ) (h : MagnitudeBound (gridValue N d) one-half) →
    rotation (gridAngle N d h) ≡ cayleyRotor N d
  operational-cayley-grid N d h = sym (rotor-right-unit (rotation (gridAngle N d h)))
    ∙ cong (rotation (gridAngle N d h) ⊗_)
      (sym (rotor-comm (inverseCayleyRotor N d) (cayleyRotor N d) ∙ cayley-inverse-law N d))
    ∙ sym (rotor-assoc (rotation (gridAngle N d h)) (inverseCayleyRotor N d) (cayleyRotor N d))
    ∙ cong (_⊗ cayleyRotor N d) (sym (invariant-constant N d h) ∙ invariant-zero)
    ∙ rotor-left-unit (cayleyRotor N d)

  operational-cayley-cosine : (N d : ℕ) (h : MagnitudeBound (gridValue N d) one-half) →
    completionCosine (gridAngle N d h) ≡ embedMetricℚ (cayleyReal N d)
  operational-cayley-cosine N d h = cong fst (operational-cayley-grid N d h)

  operational-cayley-sine : (N d : ℕ) (h : MagnitudeBound (gridValue N d) one-half) →
    completionSine (gridAngle N d h) ≡ embedMetricℚ (cayleyImaginary N d)
  operational-cayley-sine N d h = cong snd (operational-cayley-grid N d h)
