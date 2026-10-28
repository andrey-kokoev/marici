{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyOriginZeroExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import RamseyOriginZeroPaths
module P = Paths (ℕ × Bool) Bool fst snd
no-zero-complement : P.Walk (0 , false) (0 , true) → ⊥
no-zero-complement walk = false≢true (P.zero-references walk refl)
