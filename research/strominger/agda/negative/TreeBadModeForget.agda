{-# OPTIONS --safe --cubical --guardedness #-}
module TreeBadModeForget where
open import InternalSourceComparisons using (exchange)
open import FiniteComparisonTrees
bad : (a : Object) → Full exchange a a
bad a = identity a
