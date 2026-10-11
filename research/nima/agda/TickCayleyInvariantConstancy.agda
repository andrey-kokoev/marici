{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyInvariantConstancy where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero)
open import RationalAnalyticSubstrate using (one-half)
open import CauchyProductBounds
open import TickCayleyGridIncrement using (gridValue)
open import TickCayleyConcreteTransport using (gridInvariant)
open import TickCayleyInvariantStep using (invariantCoefficient)
open import TickCayleyDyadicTelescoping using (zero-small; module Partition)
open import TickRotorTelescoping using (rotor-fine-partition-constant)

abstract
  invariant-constant : (N d : ℕ) (h : MagnitudeBound (gridValue N d) one-half) →
    gridInvariant zero zero zero-small ≡ gridInvariant N d h
  invariant-constant N d h = rotor-fine-partition-constant
    (gridInvariant zero zero zero-small) (gridInvariant N d h) (Partition.grid N d h) invariantCoefficient 6
    (Partition.first N d h) (Partition.last N d h) (Partition.local N d h)
