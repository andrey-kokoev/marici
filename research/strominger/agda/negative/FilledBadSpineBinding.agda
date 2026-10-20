{-# OPTIONS --safe --cubical --guardedness #-}
module FilledBadSpineBinding where
open import Cubical.Foundations.Prelude
import SeedTetrahedronBridge as Graph
import SeedNativePromotionBindingGate as Gate
open import FilledSourceReturnClassification
bad : Gate.SourceFull
bad = Graph.spine-completed , refl , refl
