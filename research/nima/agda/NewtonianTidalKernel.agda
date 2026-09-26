{-# OPTIONS --safe --cubical --guardedness #-}
module NewtonianTidalKernel where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ; pos; _+_; _-_; _·_)

data Axis : Type where
  x y z : Axis
Vec = Axis → ℤ
Tensor = Axis → Axis → ℤ

record Source : Type where
  constructor source
  field mass radius inverseCubeUnits : ℤ
        direction : Vec
open Source public

delta : Tensor
delta x x = pos 1
delta y y = pos 1
delta z z = pos 1
delta _ _ = pos 0

normSquared : Vec → ℤ
normSquared v = v x · v x + v y · v y + v z · v z
position : Source → Vec
position s i = radius s · direction s i
reciprocalCheck : Source → ℤ
reciprocalCheck s = radius s · radius s · radius s · inverseCubeUnits s

-- Assumed Newtonian Hessian: m/r^3 (delta_ij - 3 n_i n_j), G=1.
-- Units represent a COMMON denominator, checked separately in the certificate.
contribution : Source → Tensor
contribution s i j = mass s · inverseCubeUnits s ·
  (delta i j - pos 3 · direction s i · direction s j)
tidal : Source → Source → Tensor
tidal a b i j = contribution a i j + contribution b i j

record Jet : Type where
  constructor jet
  field potential : ℤ
        gradient : Vec
        hessian : Tensor
open Jet public

-- Algebraic second-jet action of adding c + b.x to a potential.
-- This does not assert that all physical changes of frame are affine.
addAffine : ℤ → Vec → Jet → Jet
addAffine c b j = jet (potential j + c)
  (λ i → gradient j i + b i) (hessian j)
affine-invariance : (c : ℤ) (b : Vec) (j : Jet)
  → hessian (addAffine c b j) ≡ hessian j
affine-invariance c b j = refl

relativeAcceleration : Tensor → Vec → Vec
relativeAcceleration e v i = pos 0 -
  (e i x · v x + e i y · v y + e i z · v z)
