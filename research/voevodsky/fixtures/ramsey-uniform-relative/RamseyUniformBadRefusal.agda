{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyUniformBadRefusal where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Int.Base using (pos; negsuc)
open import Agda.Builtin.String using (String)
open import RamseyUniformRelative
open import RamseyUniformSigned
bad : NegativeWord.L.Missing origin-list zero3
bad = negative-refusal
