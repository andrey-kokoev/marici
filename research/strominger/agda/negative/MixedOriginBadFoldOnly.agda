{-# OPTIONS --safe --cubical --guardedness #-}
module MixedOriginBadFoldOnly where
open import InternalSourceComparisons using (Mode)
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import CertifiedFramedCells as Cell
open import CertifiedMixedHistoryOrigins
bad : {m : Mode} {a b : F.Object} (t : M.Tree m a b) → Cell.Certificate (M.fold t) → Origins t
bad t c = c
