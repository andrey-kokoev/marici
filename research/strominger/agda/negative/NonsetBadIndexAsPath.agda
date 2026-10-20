{-# OPTIONS --safe --cubical --guardedness #-}
module NonsetBadIndexAsPath where
open import Cubical.Foundations.Prelude
open import NonsetWitnessEnvelopes
bad : left ≡ right
bad = same-index
