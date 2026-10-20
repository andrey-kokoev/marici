{-# OPTIONS --safe --cubical --guardedness #-}
module MixedBadJudgmentalRouting where
open import Cubical.Foundations.Prelude
open import InternalSourceComparisons using (Mode)
open import SourceIndexedExtensionFamilies using (Out)
import FiniteComparisonTrees as F
open import MixedComparisonTrees
bad : {m n : Mode} {a b c : F.Object} (f : F.Full m a b) (g : F.Full n b c) (o : Out (fst a))
  → route (F.compose f g) o ≡ route g (route f o)
bad f g o = refl
