{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ComponentMultiplicityCollapse where
open import Cubical.Foundations.Prelude
import ComponentArithmetic as C
-- Boolean/idempotent union is not the conditional additive component monoid.
bad : C.append C.unit C.unit ≡ C.unit
bad = refl
