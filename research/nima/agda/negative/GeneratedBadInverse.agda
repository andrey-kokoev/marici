{-# OPTIONS --safe --cubical --guardedness #-}
module negative.GeneratedBadInverse where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import GeneratedContinuationContexts
B = ground Bool
-- EXPECTED FAILURE: projection followed by duplication loses the second input.
bad : Inverse (first {A = B} {B = B}) (pair identity identity)
Inverse.left bad (a , b) = refl
Inverse.right bad a = refl
