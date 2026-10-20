{-# OPTIONS --safe --cubical --guardedness #-}
module HigherPacketBadProofErasure where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (Seeds)
open import CertifiedForwardHigherPackets
import WholePackageResolution as R
open R.Generators ℓ-zero
bad : (p : Program) (d : Resolve Seeds (fst (native p))) → Certificate (fst (native p) , d)
bad p d = certificate p refl
