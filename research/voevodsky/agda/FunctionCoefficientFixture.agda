{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module FunctionCoefficientFixture where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.AbGroup
open import Cubical.Data.Int
open import Cubical.Algebra.AbGroup.Instances.Int
open import Cubical.Algebra.AbGroup.Instances.Pi
open import GenericPastingComplex

private variable ℓ ℓ' : Level

module PointwiseCoefficients {X : Type ℓ} (M : AbGroup ℓ') where
  FunctionGroup : AbGroup (ℓ-max ℓ ℓ')
  FunctionGroup = ΠAbGroup {X = X} (λ _ → M)

  module Exact = Triangle FunctionGroup

  function-chain : (v : Exact.M³) → Exact.∂₂ (Exact.∂₁ v) ≡ FunctionGroup .snd .AbGroupStr.0g
  function-chain = Exact.chain

  function-middle-exact :
    (v : Exact.M³) →
    Exact.∂₂ v ≡ FunctionGroup .snd .AbGroupStr.0g →
    Σ[ u ∈ Exact.M³ ] Exact.∂₁ u ≡ v
  function-middle-exact = Exact.middle-exact

module IntegerRegression where
  module Exact = Triangle ℤAbGroup

  integer-chain : (v : Exact.M³) → Exact.∂₂ (Exact.∂₁ v) ≡ 0
  integer-chain = Exact.chain

  integer-middle-exact :
    (v : Exact.M³) → Exact.∂₂ v ≡ 0 → Σ[ u ∈ Exact.M³ ] Exact.∂₁ u ≡ v
  integer-middle-exact = Exact.middle-exact
