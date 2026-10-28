{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPEConstructorBadSelection where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false)
open import RamseyPEConstructorExamples
bad : C.Correspondence source source
bad = C.selection Bool Bool swap C.T.leaf C.T.leaf false false refl branch
