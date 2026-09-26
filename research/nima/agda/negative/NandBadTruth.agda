{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NandBadTruth where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true)
open import NandConstructions
-- EXPECTED FAILURE: NAND of two inhabited truth types is false.
bad : nand true true ≡ true
bad = refl
