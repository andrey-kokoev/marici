{-# OPTIONS --safe --cubical --guardedness #-}
module YonedaBadNaturality where
open import Cubical.Foundations.Prelude
open import YonedaControls
bad : T.NaturalLaw raw-constant
bad x y f g = refl
