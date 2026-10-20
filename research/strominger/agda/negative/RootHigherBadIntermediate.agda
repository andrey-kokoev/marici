{-# OPTIONS --safe --cubical --guardedness #-}
module RootHigherBadIntermediate where
open import InternalSourceComparisons using (Mode)
import FiniteComparisonTrees as F
open import CertifiedMixedRootHigher
bad : {m : Mode} {a b : F.Object} (r s t : Tree m a b)
  → Boundary r s → Boundary r t → Boundary r t
bad r s t u v = compose u v
