{-# OPTIONS --safe --cubical --guardedness #-}
module NewtonianPotentialJet where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (ℤ; pos; _+_; _-_; _·_)
open import NewtonianTidalKernel using
  (Axis; x; y; z; Vec; Tensor; Jet; jet; potential; gradient; hessian;
   Source; mass; inverseCubeUnits; direction)

-- Exact second-order automatic differentiation: entries are derivatives,
-- not Taylor coefficients. In particular BOTH mixed product terms are needed.
constant : ℤ → Jet
constant c = jet c (λ _ → pos 0) (λ _ _ → pos 0)
add : Jet → Jet → Jet
add f g = jet (potential f + potential g)
  (λ i → gradient f i + gradient g i)
  (λ i j → hessian f i j + hessian g i j)
scale : ℤ → Jet → Jet
scale c f = jet (c · potential f) (λ i → c · gradient f i)
  (λ i j → c · hessian f i j)
multiply : Jet → Jet → Jet
multiply f g = jet (potential f · potential g)
  (λ i → gradient f i · potential g + potential f · gradient g i)
  (λ i j → hessian f i j · potential g + gradient f i · gradient g j
    + gradient f j · gradient g i + potential f · hessian g i j)

basis : Axis → Vec
basis x x = pos 1
basis y y = pos 1
basis z z = pos 1
basis _ _ = pos 0
coordinate : Axis → Jet
coordinate i = jet (pos 0) (basis i) (λ _ _ → pos 0)

-- u=x/r about the observer, n=source/r, |n|=1 checked by the fixture.
-- |u-n|^2 = 1+t. Construct t by polynomial operations, not a Hessian formula.
offset : Vec → Axis → Jet
offset n i = add (coordinate i) (constant (pos 0 - n i))
distanceSquared : Vec → Jet
distanceSquared n = add (multiply (offset n x) (offset n x))
  (add (multiply (offset n y) (offset n y))
       (multiply (offset n z) (offset n z)))
t : Vec → Jet
t n = add (distanceSquared n) (constant (pos 0 - pos 1))

-- P=8-4t+3t^2 is 8 times the second-order jet of (1+t)^(-1/2).
-- The certificate verifies P^2*(1+t)=64 to second order, and P(0)=8.
inverseRadius8 : Vec → Jet
inverseRadius8 n = add (constant (pos 8))
  (add (scale (pos 0 - pos 4) (t n))
       (scale (pos 3) (multiply (t n) (t n))))
normalizationResidual : Vec → Jet
normalizationResidual n = multiply
  (multiply (inverseRadius8 n) (inverseRadius8 n)) (distanceSquared n)

-- Phi=-m/r * inverseRadius8/8; two x-derivatives contribute r^-2.
-- Output numerator uses denominator 8D, with inverseCubeUnits=D/r^3.
potentialTensor8 : Source → Tensor
potentialTensor8 s = hessian
  (scale (pos 0 - mass s · inverseCubeUnits s) (inverseRadius8 (direction s)))
potentialTotal8 : Source → Source → Tensor
potentialTotal8 a b i j = potentialTensor8 a i j + potentialTensor8 b i j
