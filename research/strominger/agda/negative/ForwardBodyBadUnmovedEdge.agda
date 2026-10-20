{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardBodyBadUnmovedEdge where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (B; AB)
open import SourceIndexedExtensionFamilies using (Out)
open import ForwardForwardBodyBinding
bad : Out B
bad = B , AB
