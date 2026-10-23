{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyUniformBadLookup where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Int.Base using (pos; negsuc)
open import Agda.Builtin.String using (String)
open import RamseyUniformRelative
open import RamseyUniformSigned
module L = Lookup signed-geometry
bad : L.Located origin-list (negative-letter first)
bad = L.hit first refl
