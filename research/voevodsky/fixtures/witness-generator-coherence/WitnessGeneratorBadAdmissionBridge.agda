{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessGeneratorBadAdmissionBridge where
open import Cubical.Foundations.Prelude
import WholePackageSigmaPi as W
import WholePackageResolution as R
open W.Universe ℓ-zero
open R.Generators ℓ-zero
open import NativeExtensionFamilyAudit using (Seeds)
open import InternalSourceComparisons using (derivation)
open import RepeatedInterchangeCoherence
-- A comparison derivation cannot be relabelled as admission of its filler atom.
bad : Resolve Seeds (pack (atom CompleteFiller) sequentialFiller)
bad = derivation (asBody sequentialFiller)
