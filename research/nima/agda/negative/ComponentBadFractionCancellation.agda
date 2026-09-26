{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ComponentBadFractionCancellation where
open import Cubical.Foundations.Prelude
import Cubical.Data.Int as Z
import Cubical.Data.NatPlusOne as P
import Cubical.Data.Rationals as Q
import SignedComponentArithmetic as S
import RationalComponentArithmetic as R
-- Claiming 2/4 = 1/3 forces the false cross-product identity 6 = 4.
bad : R.fraction (S.fromInt (Z.pos 2)) (P.1+ 3) ≡ R.fraction S.one (P.1+ 2)
bad = R.faithful (Q.eq/ _ _ refl)
