{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessHigherAdmissionObstruction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Bool.Properties using (false≢true)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import RepeatedInterchangeCoherence as Existing
import HigherWitnessAdmission as Admission
open import NativeExtensionFamilyAudit using (Seeds)
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Reuse the prior exhaustive rule invariant and the EXACT prior obstruction.
-- atomicSpine peels only leading paths; all twelve native schemas preserve
-- its falsity on the actual retained Seeds. No axiom K or proof erasure.
no-higher-package-admission : Resolve Seeds Existing.higher-package-formed → ⊥
no-higher-package-admission = Admission.exact-atomic-path-not-admitted
no-atom-admission : (A : Type) (a : A) → Resolve Seeds (pack (atom A) a) → ⊥
no-atom-admission A a d = false≢true (sym (Admission.resolution-spine d))
no-atom-path-admission : (A : Type) (a b : A) (p : a ≡ b)
  → Resolve Seeds (path-package (atom A) a b p) → ⊥
no-atom-path-admission A a b p d = false≢true (sym (Admission.resolution-spine d))
missing-reflexivity-premise :
  Resolve Seeds (pack (atom Existing.CompleteFiller) Existing.sequentialFiller) → ⊥
missing-reflexivity-premise = no-atom-admission Existing.CompleteFiller Existing.sequentialFiller

module PathAdmission = Admission.PathAdmission Seeds
if-carrier-admitted :
  Resolve Seeds (pack (atom Existing.CompleteFiller) Existing.sequentialFiller)
  → Resolve Seeds Existing.higher-package-formed
if-carrier-admitted d = PathAdmission.from-derived-point (atom Existing.CompleteFiller)
  Existing.sequentialFiller d Existing.filler-coherence

-- Native higher-rule exists and consumes BOTH actual path derivations.
higher-from-premises : (Q : Code) (x y : El Q) (p q : x ≡ y) (alpha : p ≡ q)
  → Resolve Seeds (path-package Q x y p)
  → Resolve Seeds (path-package Q x y q)
  → Resolve Seeds (higher-package Q x y p q alpha)
higher-from-premises Q x y p q alpha dp dq =
  apply (higher-rule Q x y p q alpha) (λ { (lift true) → dp ; (lift false) → dq })

-- The existing source also gives the positive retained representation.
-- It is NOT the atom-coded package above, and its projection recovers the
-- original higher witness exactly. Do not reconstruct the old diagram.
retained-higher-admitted : Resolve Seeds Admission.admittedPathPackage
retained-higher-admitted = Admission.admitted-higher-witness
next-native-higher-admitted : Resolve Seeds Admission.nextHigherPackage
next-native-higher-admitted = Admission.next-higher-derived
original-higher-recovered : cong fst (value Admission.admittedPathPackage) ≡ Existing.filler-coherence
original-higher-recovered = Admission.path-recovery
