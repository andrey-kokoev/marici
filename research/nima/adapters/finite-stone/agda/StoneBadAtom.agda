{-# OPTIONS --safe --cubical --guardedness #-}
module StoneBadAtom where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false)
open import FiniteStoneDomain
bad : IsAtom one
bad = snd (point false)
