{-# OPTIONS --safe --cubical --guardedness #-}
module TwoComparisonBadRawEquality where
open import Cubical.Foundations.Prelude
open import InternalSourceComparisons using (package)
import TwoComparisonTwoAttachmentCoherence as T
bad : package T.source ≡ package T.target
bad = refl
