{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyAttachmentChoiceBadInverse where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false)
-- A constant map out of the one-choice carrier cannot have this inverse law.
bad : (b : Bool) → false ≡ b
bad b = refl
