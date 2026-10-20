{-# OPTIONS --safe --cubical --guardedness #-}
module HigherBadAtomicReinterpretation where
open import Cubical.Foundations.Prelude
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero
open import NativeExtensionFamilyAudit using (Seeds)
import RepeatedInterchangeCoherence as R
open import HigherWitnessAdmission using (admitted-higher-witness)

-- Interpreted equivalence is not literal equality of retained Code or of
-- indexed admission. The envelope witness cannot masquerade as the bare atom.
bad : Resolve Seeds R.higher-package-formed
bad = admitted-higher-witness
