{-# OPTIONS --safe --cubical --guardedness #-}
module RootHigherBadPathImport where
open import Cubical.Foundations.Prelude
open import InternalSourceComparisons using (Mode)
import FiniteComparisonTrees as F
open import CertifiedMixedRootHigher
bad : {m : Mode} {a b : F.Object} (r s : Tree m a b)
  → evaluate (direct r s) ≡ evaluate (direct r s) → Program
bad r s p = pathP (direct r s) p
