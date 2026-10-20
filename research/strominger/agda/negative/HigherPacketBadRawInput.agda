{-# OPTIONS --safe --cubical --guardedness #-}
module HigherPacketBadRawInput where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; Seeds; pointQ)
open import CertifiedForwardHigherPackets
import WholePackageResolution as R
open R.Generators ℓ-zero
bad : Resolve Seeds (pointQ A) → Program
bad d = higherP d higherPath
