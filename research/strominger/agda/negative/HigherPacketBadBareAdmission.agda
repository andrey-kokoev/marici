{-# OPTIONS --safe --cubical --guardedness #-}
module HigherPacketBadBareAdmission where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; Seeds; root)
import CertifiedForwardHigherPackets
import ForwardForwardHigherAdmission as Higher
import WholePackageResolution as R
open R.Generators ℓ-zero
module H = Higher.Admit (root A)
bad : Resolve Seeds H.barePackage
bad = H.admitted-higher
