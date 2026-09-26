{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NativeTableBadFillerErasure where
open import Cubical.Foundations.Prelude
open import NativeTableRegression using (filler-id; filler-swap)
-- EXPECTED FAILURE: two fillers at the same fixed boundary are not equal.
bad : filler-id ≡ filler-swap
bad = refl
