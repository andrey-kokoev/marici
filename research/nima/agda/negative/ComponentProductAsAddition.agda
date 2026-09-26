{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ComponentProductAsAddition where
open import Cubical.Foundations.Prelude
import ComponentArithmetic as C
-- Replacing endomorphism composition by additive combination is false.
bad : C.multiply 2 3 ≡ C.append 2 3
bad = refl
