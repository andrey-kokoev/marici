{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPEConstructorBadLeaf where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseyPEConstructorExamples
bad : Fixed.Correspondence (Fixed.T.leaf false) (Fixed.T.leaf true)
bad = Fixed.leaf false true refl
