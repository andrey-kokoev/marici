{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ComponentZeroDenominator where
import RationalComponentArithmetic as R
open import Cubical.Data.NatPlusOne
allowed : R.Denominator
allowed = 1
-- The literal constraint must reject a zero denominator.
bad : R.Denominator
bad = 0
