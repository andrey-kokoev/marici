{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NativeTableBadFirstJetReadout where
open import Cubical.Foundations.Prelude
open import NewtonianTidalKernel using (x)
open import NativeTidalTableReadout using (read-tensor; zero-jet; bump-jet)
-- EXPECTED FAILURE: identical scalar/gradient entries do not imply equal
-- Hessian entries. The positive module proves the general no-factor theorem.
bad : read-tensor zero-jet x x ≡ read-tensor bump-jet x x
bad = refl
