{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NativeTableBadRetentionErasure where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import NativeTableRegression using (module G; module N; family; unit-graph)
-- EXPECTED FAILURE: omit the retained input values from a native E result.
bad : fst (N.E-package Unit family tt) ≡ G.E-table Unit (λ _ → unit-graph)
bad = refl
