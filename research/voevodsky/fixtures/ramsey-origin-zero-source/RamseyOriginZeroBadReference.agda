{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyOriginZeroBadReference where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseyOriginZeroExamples
bad : P.Step (0 , false) (0 , true)
bad = P.fixed refl refl
