{-# OPTIONS --safe --cubical --guardedness #-}
module negative.RecursiveTablesBadCoverage where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit)
import RecursiveConstructorTables as Tables
module G = Tables.Core ℓ-zero
-- EXPECTED FAILURE: the independent grammar does not yet cover maps codes.
bad : G.Supported (G.O.maps (G.O.atom Unit) (G.O.atom Unit))
bad = G.atom-supported
