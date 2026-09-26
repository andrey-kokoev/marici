{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NativeTableBadAttachment where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit)
import IndexedConstructorTables as Tables
module G = Tables.Core ℓ-zero
-- EXPECTED FAILURE: the declaration requires a Unit child, not Bool.
bad : G.Node (Unit → Unit)
bad = G.table-node (G.maps-header Unit Unit)
  (λ { (lift false) → G.atom-node Bool ; (lift true) → G.atom-node Unit })
