{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyUniformBadSubstitution where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Int.Base using (pos; negsuc)
open import Agda.Builtin.String using (String)
open import RamseyUniformRelative
open import RamseyUniformSigned
module A = Arithmetic signed-geometry (Slot 1) negative-letter
bad : A.phi (A.instantiate (cons A.hole-token nil) first) ≡ A.base (cons A.hole-token nil)
bad = refl
