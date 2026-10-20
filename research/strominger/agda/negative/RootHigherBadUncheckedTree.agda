{-# OPTIONS --safe --cubical --guardedness #-}
module RootHigherBadUncheckedTree where
open import InternalSourceComparisons using (Mode)
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
open import CertifiedMixedRootHigher
bad : {m : Mode} {a b : F.Object} → M.Tree m a b → Program
bad t = compareP (direct t t)
