{-# OPTIONS --safe --cubical --guardedness #-}
module AdapterBadJudgmentalPackage where
open import Cubical.Foundations.Prelude
open import InternalSourceComparisons using (package)
open import ContinuationSidePolicies using (ab)
open import SourceIndexedContinuationAdapter
bad : Example.sourcePackage ab ≡ package (Example.targetBody ab)
bad = refl
