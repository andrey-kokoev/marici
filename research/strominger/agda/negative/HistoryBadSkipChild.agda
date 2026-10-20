{-# OPTIONS --safe --cubical --guardedness #-}
module HistoryBadSkipChild where
open import Cubical.Foundations.Prelude
open import InternalSourceComparisons using (Mode)
open import SourceIndexedExtensionFamilies using (Out)
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
open import MixedHistoryCertificates
bad : {m : Mode} {a b : F.Object} (t : M.Tree m a b) (o : Out (fst a)) → Evidence (M.attach t o)
bad t o = nodeEvidence t
