{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NativeTableBadConstructorErasure where
open import Cubical.Foundations.Prelude
open import NativeTableRegression using (function-atom; function-map)
-- EXPECTED FAILURE: equal carriers do not identify constructor declarations.
bad : function-atom ≡ function-map
bad = refl
