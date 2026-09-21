{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureProductBoundaryRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.Data.Unit
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureProductBoundary

-- Two genuinely varying family coordinates, not a singleton-index padding.
P : Type
P = Bool → Bool

p₀ : P
p₀ _ = false

flipFamily : P → P
flipFamily p i = not (p i)

reverseCircle : S¹ → S¹
reverseCircle base = base
reverseCircle (loop i) = loop (~ i)

module Example = SplitMap Bool Bool (λ _ → Bool) (λ _ → Bool)
  S¹ S¹ p₀ base flipFamily reverseCircle

-- An actual quotient of the existing model is this nontrivial product.
productFactorization : Example.Input.M.R.Quotient ≃ ((Bool → Bool) × S¹)
productFactorization = Example.Input.factorization

-- The circle boundary is retained, not replaced by a contractible witness.
includeBoundary : S¹ → Example.Input.M.R.Quotient
includeBoundary r = Example.Input.assemble (p₀ , r)

readBoundary : Example.Input.M.R.Quotient → S¹
readBoundary x = snd (Example.Input.encode x)

boundaryRetraction : (r : S¹) → readBoundary (includeBoundary r) ≡ r
boundaryRetraction r = cong snd (Example.Input.recoverCoordinates (p₀ , r))

-- Compute the actual many/many presentation, obtained from the checked
-- quotient-transport map, in its product coordinates.
coordinateAction : (p : P) (r : S¹) →
  Example.F4 (p , r) ≡ (flipFamily p , reverseCircle r)
coordinateAction p r = Example.coordinateOperationLaw (p , r)

loopOrientation : (i : I) → snd (Example.F4 (p₀ , loop i)) ≡ loop (~ i)
loopOrientation i = cong snd (coordinateAction p₀ (loop i))

fourVertexSquare : (z : P × S¹) →
  Example.outputRejoin (Example.F4 z) ≡ Example.F3 z
fourVertexSquare = Example.outputRejoin-F4

-- The contrasting model has a dependent residual and provably no uniform
-- product split that preserves its selected family observation.
module Negative = DependentCounterexample

unitFiber : fiber Negative.observe Negative.p₀ ≃ Unit
unitFiber = Negative.fiberIdentification Negative.p₀

boolFiber : fiber Negative.observe Negative.p₁ ≃ Bool
boolFiber = Negative.fiberIdentification Negative.p₁

-- The general dependent decomposition does hold for this same observable.
module Dependent = Observation Negative.observe

dependentFactorization : Negative.M.R.Quotient ≃
  (Σ[ p ∈ Negative.P ] fiber Negative.observe p)
dependentFactorization = Dependent.dependentPresentation
