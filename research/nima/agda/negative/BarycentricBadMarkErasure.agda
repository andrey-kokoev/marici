{-# OPTIONS --safe --cubical --guardedness #-}
module BarycentricBadMarkErasure where
open import Cubical.Foundations.Prelude
open import BarycentricWitnessPacket
-- The two faces carry the same type and term, but have different marks.
bad : is-first v0 ≡ is-first v1
bad = refl
