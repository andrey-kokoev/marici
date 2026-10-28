{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyFieldInterpretationBadIdentity where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import RamseyFieldInterpretationExamples
bad : S.transfer false true false ≡ false
bad = refl
