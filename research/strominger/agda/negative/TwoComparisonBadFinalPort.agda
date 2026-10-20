{-# OPTIONS --safe --cubical --guardedness #-}
module TwoComparisonBadFinalPort where
open import NativeExtensionFamilyAudit using (D)
open import InternalSourceComparisons using (Body)
import TwoComparisonTwoAttachmentCoherence as T
bad : Body D
bad = T.source
