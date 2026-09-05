{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module BadIncidence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver

record ℤ³ : Type where
  constructor triple
  field x y z : ℤ
open ℤ³

-- Wrong first incidence sign.
bad∂₁ : ℤ³ → ℤ³
bad∂₁ v = triple (x v + y v) ((- y v) + z v) ((- z v) + x v)

∂₂ : ℤ³ → ℤ
∂₂ v = (x v + y v) + z v

-- Deliberate failure: the composite is 2*x, not zero.
bad-chain : (v : ℤ³) → ∂₂ (bad∂₁ v) ≡ 0
bad-chain v = solve! ℤCommRing
