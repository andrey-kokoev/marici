{-# OPTIONS --safe --cubical --guardedness #-}
module OriginalBridgeBadSeedReset where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Maybe using (just)
open import ActualSeedEndpointTable using (AB)
import NativeExtensionFamilyAudit as N
import OriginalRuleGeometricCompiler as C
bad : C.previous (C.native (C.step AB C.root)) ≡ just (N.pointQ N.A , N.root N.A)
bad = refl
