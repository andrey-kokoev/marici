{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyDerivedComparisonExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import RamseyNativeDerivedComparison
view : Bool → Bool → Bool
view false a = a
view true a = not a
module P = Presentations Bool Bool Bool (λ _ → Unit) view
native-comparison : P.R.Resolve (P.comparison false tt false true)
native-comparison = P.comparison-proof false tt false true
native-composition : P.R.Resolve (P.composed false tt false true false)
native-composition = P.composed-proof false tt false true false
