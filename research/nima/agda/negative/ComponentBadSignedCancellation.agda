{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ComponentBadSignedCancellation where
open import Cubical.Foundations.Prelude
import Cubical.Data.Int as Z
import SignedComponentArithmetic as S
bad : S.add (S.fromInt (Z.pos 3)) (S.fromInt (Z.negsuc 2)) ≡ S.one
bad = S.faithful refl
