{-# OPTIONS --safe --cubical --guardedness #-}
module negative.NandBadChoiceCollapse where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
Choice = Unit ⊎ Unit
left right : Choice
left = inl tt
right = inr tt
-- EXPECTED FAILURE: two tags remain distinct even when both prove inhabitation.
bad : left ≡ right
bad = refl
