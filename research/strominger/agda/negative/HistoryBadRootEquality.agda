{-# OPTIONS --safe --cubical --guardedness #-}
module HistoryBadRootEquality where
open import Cubical.Foundations.Prelude
open import InternalSourceComparisons using (package)
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
open import MixedHistoryCertificates
bad : (a : F.Object) → package (root (M.old (F.unit a)))
  ≡ package (root (M.join (M.old (F.unit a)) (M.old (F.unit a))))
bad a = refl
