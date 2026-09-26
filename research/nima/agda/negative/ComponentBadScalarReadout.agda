{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ComponentBadScalarReadout where
open import Cubical.Foundations.Prelude
import Cubical.Data.Int as Z
import Cubical.Data.NatPlusOne as P
import Cubical.Data.Rationals as Q
import RationalComponentArithmetic as R
import NativeRationalComponentArithmetic as A
module F = A.ScalarFixture
bad : R.asRational (F.E.readout F.expression (snd (F.E.package F.expression))) ≡ Q.[ Z.pos 7 / P.1+ 24 ]
bad = Q.eq/ _ _ refl
