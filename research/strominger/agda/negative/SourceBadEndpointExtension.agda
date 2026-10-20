{-# OPTIONS --safe --cubical --guardedness #-}
module SourceBadEndpointExtension where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (C; D; CA)
open import SourceIndexedExtensionFamilies using (Out)

-- CA cannot certify an attachment from C to D.
bad : Out C
bad = D , CA
