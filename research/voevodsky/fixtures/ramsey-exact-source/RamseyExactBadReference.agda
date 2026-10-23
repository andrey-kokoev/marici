{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyExactBadReference where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Int.Base using (pos)
open import Cubical.Data.Unit.Base using (tt)
open import RamseyUniformRelative using (Slot; first; next; nil; cons)
open import RamseyUniformSigned using (zero3)
open import RamseyExactSource
bad : reference (prepared zero3) C2 ≡ reference (prepared zero3) C0
bad = refl
