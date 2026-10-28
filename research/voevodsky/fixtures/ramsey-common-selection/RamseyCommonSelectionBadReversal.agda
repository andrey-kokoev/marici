{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyCommonSelectionBadReversal where
open import Cubical.Foundations.Prelude
open import RamseyCommonSelection
open import RamseyEndpointPolicy using (base; complement)
bad : ordered complement base (reverse base complement witness) ≡ ordered base complement witness
bad = refl
