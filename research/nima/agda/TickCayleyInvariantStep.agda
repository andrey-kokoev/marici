{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyInvariantStep where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure using (precision)
open import CauchyProductBounds
open import TickCayleyGridIncrement using (gridValue)
open import TickRotationDefectTransport using (RotorBound; _⊗_; _⊖_; transportBudget)
open import TickOperationalRotorIncrement using (rotation; gridAngle)
open import TickOperationalOuterRotorBound using (rotorRadius)
open import TickCayleyOuterRotor using (inverseCayleyRotor)
open import TickCayleyRotorComposition using (relativeRotor; rotor-assoc; relative-inverse-cancellation)
open import TickCayleyConcreteTransport using (gridInvariant)
import TickCayleyConcreteTransport as Concrete

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)
  budget : (P Q c e : fst R) →
    ((P ·S (c ·S (e ·S e)) +S P ·S (c ·S (e ·S e))) ·S Q) +S
      ((P ·S (c ·S (e ·S e)) +S P ·S (c ·S (e ·S e))) ·S Q) ≡
    (((P ·S c +S P ·S c) ·S Q) +S ((P ·S c +S P ·S c) ·S Q)) ·S (e ·S e)
  budget P Q c e = solve! R

invariantCoefficient : Q.ℚ
invariantCoefficient = transportBudget (rotorRadius 4) 2 99

abstract
  comparison-product-path : (n m d : ℕ) (hx : MagnitudeBound (gridValue n d) one-half) →
    (rotation (gridAngle n d hx) ⊗ relativeRotor n m d) ⊗ inverseCayleyRotor m d ≡ gridInvariant n d hx
  comparison-product-path n m d hx = rotor-assoc (rotation (gridAngle n d hx)) (relativeRotor n m d) (inverseCayleyRotor m d)
    ∙ cong (rotation (gridAngle n d hx) ⊗_) (relative-inverse-cancellation n m d)

  invariant-step-bound : (n m d : ℕ) (e : Q.ℚ)
    (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half) →
    0 ≤ e → e ≤ precision 6 → MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e →
    RotorBound (gridInvariant m d hy ⊖ gridInvariant n d hx) (invariantCoefficient Q.· (e Q.· e))
  invariant-step-bound n m d e hx hy eh small hd = subst
    (λ B → RotorBound (gridInvariant m d hy ⊖ gridInvariant n d hx) B)
    (Algebra.budget PreferredℚCommRing (rotorRadius 4) 2 99 e)
    (subst (λ z → RotorBound (gridInvariant m d hy ⊖ z) (transportBudget (rotorRadius 4) 2 (99 Q.· (e Q.· e))))
      (comparison-product-path n m d hx) (Concrete.Grid.concrete-transport-bound n m d e hx hy eh small hd))
