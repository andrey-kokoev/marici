{-# OPTIONS --safe --cubical --guardedness #-}
module TickMachinRotationIdentity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

-- A symbolic kernel certificate. The concrete 5/239 substitution is
-- audited separately with exact rational arithmetic, not assumed here.
module Certificate (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  Complex = fst R × fst R
  multiply : Complex → Complex → Complex
  multiply (a , b) (c , d) = (a · c + (- (b · d))) , ((a · d) + (b · c))

  square : Complex → Complex
  square z = multiply z z

  abstract
    sibling-rotation : (a s : fst R) →
      multiply (s · a , s · (a + 1r)) (a + (a + 1r) , - 1r) ≡
      multiply (0r , 1r)
        (multiply (s · a , - (s · (a + 1r))) (a + (a + 1r) , 1r))
    sibling-rotation a s = cong₂ _,_ (solve! R) (solve! R)

    imaginary-unit-squared : square (0r , 1r) ≡ (- 1r , 0r)
    imaginary-unit-squared = cong₂ _,_ (solve! R) (solve! R)
