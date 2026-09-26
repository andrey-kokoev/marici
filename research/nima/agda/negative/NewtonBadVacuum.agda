{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NewtonBadVacuum where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos; negsuc)
open import NewtonRadialCoefficients
-- r^-2 is not a harmonic radial potential in 3D.
bad : radialLaplacianCoefficient (negsuc 1) ≡ pos 0
bad = refl
