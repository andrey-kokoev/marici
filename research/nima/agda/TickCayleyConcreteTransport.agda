{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyConcreteTransport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.Data.Int.Order as ZO
open import RationalAnalyticSubstrate using (one-half)
open import RegularCauchyStructure using (precision)
open import CauchyProductBounds
open import TickCayleyGridIncrement using (gridValue)
open import TickOperationalRotorIncrement using (rotation; gridAngle; grid-rotation-increment)
open import TickOperationalOuterRotorBound using (rotorRadius; rotor-radius-nonnegative; grid-outer-rotation-bound)
open import TickCayleyOuterRotor using (inverseCayleyRotor)
import TickCayleyOuterRotor as Rational
open import TickRotationDefectTransport using (Rotor; RotorBound; _⊗_; _⊖_; transportBudget)
import TickRotationDefectTransport as Transport

gridInvariant : (n d : ℕ) → MagnitudeBound (gridValue n d) one-half → Rotor
gridInvariant n d h = rotation (gridAngle n d h) ⊗ inverseCayleyRotor n d

module Grid (n m d : ℕ) (e : Q.ℚ)
  (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half)
  (eh : 0 ≤ e) (small : e ≤ precision 6)
  (hd : MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e) where
  module Inner = Transport.Grid n m d e hx hy eh small hd

  -- Both outer factors below are the concrete intended rotations, and their
  -- bounds are proved, not extra assumptions. The second product still needs
  -- rational composition to identify it with gridInvariant n d hx.
  concrete-transport-bound : RotorBound
    ((gridInvariant m d hy) ⊖
      ((rotation (gridAngle n d hx) ⊗ Inner.reference) ⊗ inverseCayleyRotor m d))
    (transportBudget (rotorRadius 4) 2 (99 Q.· (e Q.· e)))
  concrete-transport-bound = subst
    (λ z → RotorBound (z ⊖ ((rotation (gridAngle n d hx) ⊗ Inner.reference) ⊗ inverseCayleyRotor m d))
      (transportBudget (rotorRadius 4) 2 (99 Q.· (e Q.· e))))
    (cong (_⊗ inverseCayleyRotor m d) (sym (grid-rotation-increment n m d hx hy)))
    (Inner.transported-grid-bracket (rotation (gridAngle n d hx)) (inverseCayleyRotor m d)
      (rotorRadius 4) 2 (rotor-radius-nonnegative 4) ZO.zero-≤pos
      (grid-outer-rotation-bound n d hx) (Rational.Bound.inverse-bound m d hy))
