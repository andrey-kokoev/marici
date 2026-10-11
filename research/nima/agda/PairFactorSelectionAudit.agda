{-# OPTIONS --safe --cubical --guardedness #-}
module PairFactorSelectionAudit where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sigma.Base using (_×_)

-- Every function of an exchange-invariant distance inherits exchange
-- symmetry. The function itself is not selected by that certificate.
module DistanceFactors
  (ℓ : Level) (Configuration Distance Scalar : Type ℓ)
  (swap : Configuration → Configuration)
  (distance : Configuration → Distance)
  (distance-symmetric : (x : Configuration) → distance (swap x) ≡ distance x)
  where
  factor : (Distance → Scalar) → Configuration → Scalar
  factor h x = h (distance x)

  exchange : (h : Distance → Scalar) (x : Configuration)
    → factor h (swap x) ≡ factor h x
  exchange h x = cong h (distance-symmetric x)

  -- The pointwise certificate composes twice without constraining h.
  double-exchange : (h : Distance → Scalar) (x : Configuration)
    → factor h (swap (swap x)) ≡ factor h x
  double-exchange h x = exchange h (swap x) ∙ exchange h x

-- A bounded logical countermodel: a symmetric distance distinguishes equal
-- and unequal labels. Two scalar factors agree at coincidence, differ away
-- from it, and both satisfy the same exchange certificate.
module Countermodel where
  Configuration : Type
  Configuration = Bool × Bool
  swap : Configuration → Configuration
  swap (a , b) = b , a
  distance : Configuration → Bool
  distance (false , false) = false
  distance (false , true) = true
  distance (true , false) = true
  distance (true , true) = false
  symmetric : (x : Configuration) → distance (swap x) ≡ distance x
  symmetric (false , false) = refl
  symmetric (false , true) = refl
  symmetric (true , false) = refl
  symmetric (true , true) = refl
  module D = DistanceFactors ℓ-zero Configuration Bool Bool swap distance symmetric

  constant contrasting : Bool → Bool
  constant _ = true
  contrasting false = true
  contrasting true = false

  same-at-coincidence : constant false ≡ contrasting false
  same-at-coincidence = refl

  distinct-factors : D.factor constant ≡ D.factor contrasting → ⊥
  distinct-factors equality = true≢false (cong (λ f → f (false , true)) equality)

  constant-exchange = D.exchange constant
  contrasting-exchange = D.exchange contrasting
