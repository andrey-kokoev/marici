{-# OPTIONS --safe --cubical --guardedness #-}
module ScalarSixKernel where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_; _-_; _·_)
open import Cubical.Data.List.Base using (List; []; _∷_; _++_; map)

-- Forward realization of one fixed phi^4 sample, not a QFT axiom proof.
data Label : Type where
  l0 l1 l2 l3 l4 l5 : Label

record Momentum : Type where
  constructor p
  field e x y z : ℤ
open Momentum

add : Momentum → Momentum → Momentum
add a b = p (e a + e b) (x a + x b) (y a + y b) (z a + z b)

square : Momentum → ℤ
square a = (e a · e a) - (x a · x a) - (y a · y a) - (z a · z a)

record Pair : Type where
  constructor pair
  field left right : Label
open Pair

pairs : List Label → List Pair
pairs [] = []
pairs (a ∷ rest) = map (pair a) rest ++ pairs rest

channels : List Pair
channels = pairs (l1 ∷ l2 ∷ l3 ∷ l4 ∷ l5 ∷ [])

allLabels : List Label
allLabels = l0 ∷ l1 ∷ l2 ∷ l3 ∷ l4 ∷ l5 ∷ []

sumZ : List ℤ → ℤ
sumZ [] = pos 0
sumZ (a ∷ rest) = a + sumZ rest

sumP : List Momentum → Momentum
sumP [] = p (pos 0) (pos 0) (pos 0) (pos 0)
sumP (a ∷ rest) = add a (sumP rest)

denominators : (Label → Momentum) → List ℤ
denominators momenta = map (λ c → square (add (momenta l0)
  (add (momenta (left c)) (momenta (right c))))) channels

-- Restricted reciprocal table. The certificate checks d * units(d) = 24
-- for EVERY generated channel, so the unsupported fallback cannot certify.
units : ℤ → ℤ
units (pos 8) = pos 3
units (negsuc 3) = negsuc 5
units (negsuc 5) = negsuc 3
units _ = pos 0

inverseChecks : List ℤ → List ℤ
inverseChecks = map (λ d → d · units d)

amplitudeNumerator : ℤ → List ℤ → ℤ
amplitudeNumerator couplingSquaredNumerator ds =
  (pos 0 - couplingSquaredNumerator) · sumZ (map units ds)
