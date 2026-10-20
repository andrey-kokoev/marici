{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardBodyBadBareAdmission where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; Seeds; pointQ)
import ForwardForwardHigherAdmission as Higher
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero
module Test (d : Resolve Seeds (pointQ A)) where
  module H = Higher.Admit d
  bad : Resolve Seeds H.barePackage
  bad = H.admitted-higher
