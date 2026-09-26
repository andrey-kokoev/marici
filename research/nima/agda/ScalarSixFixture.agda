{-# OPTIONS --safe --cubical --guardedness #-}
module ScalarSixFixture where
open import ScalarSixKernel
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc)

momenta : Label → Momentum
momenta l0 = p (pos 2) (pos 0) (pos 0) (pos 2)
momenta l1 = p (pos 2) (pos 0) (pos 0) (negsuc 1)
momenta l2 = p (negsuc 0) (negsuc 0) (pos 0) (pos 0)
momenta l3 = p (negsuc 0) (pos 1) (pos 0) (pos 0)
momenta l4 = p (negsuc 0) (pos 0) (negsuc 0) (pos 0)
momenta l5 = p (negsuc 0) (pos 0) (pos 1) (pos 0)

couplingNumerator couplingDenominator exportedNumerator exportedDenominator : ℤ
couplingNumerator = (pos 3)
couplingDenominator = (pos 5)
exportedNumerator = (pos 6)
exportedDenominator = (pos 25)
