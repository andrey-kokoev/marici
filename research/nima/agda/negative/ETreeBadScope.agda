{-# OPTIONS --safe --cubical --guardedness #-}
module negative.ETreeBadScope where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false)
open import ETreeSubstitution using (Tree; leaf)
open import ECurriedTemplates
-- EXPECTED FAILURE: supplying slot zero must not capture the second slot.
body : Template 2 Bool
body = leaf (slot (there here))
bad : partial body (leaf false) ≡ embed (leaf false)
bad = refl
