{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDerivedComparisonBadRoot where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Unit.Base using (tt)
open import RamseyNativeDerivedComparison
open import RamseyDerivedComparisonExamples
bad : snd (equivFun (P.equivalence false tt false true) (N.value (P.display false tt false))) ≡ (true , tt)
bad = refl
