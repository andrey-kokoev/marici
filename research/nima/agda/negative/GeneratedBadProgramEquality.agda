{-# OPTIONS --safe --cubical --guardedness #-}
module negative.GeneratedBadProgramEquality where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import GeneratedContinuationContexts
-- EXPECTED FAILURE: equal interpreted maps do not identify retained programs.
bad : identity {ground Bool} ≡ (identity then identity)
bad = refl
