{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardProducerBadUncheckedComparison where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; B; AB)
open import InternalSourceComparisons using (exchange)
open import ForwardCertifiedPrograms
bad : Program B
bad = compareP exchange (initialP (rootI A)) (attachP (initialP (rootI A)) (B , AB)) refl
