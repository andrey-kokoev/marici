{-# OPTIONS --safe --cubical --guardedness #-}
module PhaseSelectionBadUniqueness where
open import Cubical.Foundations.Prelude
open import PhaseAlgebraSelectionBoundary
import RetainedCliffordProfiles as C
bad : fst (interpret trivial C.RL) ≡ fst (interpret clifford C.RL)
bad = refl
