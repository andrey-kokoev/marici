{-# OPTIONS --safe --cubical --guardedness #-}
module MixedOriginBadSkipCore where
open import InternalSourceComparisons using (Mode)
import FiniteComparisonTrees as F
open import CertifiedMixedHistoryOrigins
bad : {m n : Mode} {a b c : F.Object} (r : F.Tree m a b) (s : F.Tree n b c)
  → CoreOrigins r → CoreOrigins (F.then r s)
bad r s cr = cr
