{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessNativeEnvelope where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true; false)
open import NativeExtensionFamilyAudit using (Vertex; A; Seeds)
open import InternalSourceComparisons
open import WitnessContinuationHistories
open import WitnessHigherControls using (chosen-direct-staged)
import HigherWitnessAdmission as Prior
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero
module Admit = Prior.PathAdmission Seeds

-- Generic version of the EXISTING admission envelope. This consumes a total
-- native derivation function on a specified family; it does not assume a
-- generator, enumeration or choice function for all conceivable witnesses.
module NativeFamily (I : Type) (F : I → Complete)
  (d : (i : I) → Resolve Seeds (F i)) where
  Q : Code
  Q = E I (λ i → retained (F i))
  section : I → El Q
  section i = i , value (F i)
  point-native : (i : I) → Resolve Seeds (E-package I F i)
  point-native i = apply (E-rule I F i) (λ { (lift j) → d j })
  pathQ : {i j : I} → i ≡ j → Complete
  pathQ {i} {j} p = path-package Q (section i) (section j) (cong section p)
  path-native : {i j : I} (p : i ≡ j) → Resolve Seeds (pathQ p)
  path-native {i} p = Admit.from-derived-point Q (section i) (point-native i) (cong section p)
  path-recovered : {i j : I} (p : i ≡ j) → cong fst (value (pathQ p)) ≡ p
  path-recovered p = refl
  higher-native : {i j : I} (p q : i ≡ j) (alpha : p ≡ q)
    → Resolve Seeds (higher-package Q (section i) (section j)
        (cong section p) (cong section q) (cong (cong section) alpha))
  higher-native {i} {j} p q alpha = apply
    (higher-rule Q (section i) (section j) (cong section p) (cong section q) (cong (cong section) alpha))
    (λ { (lift true) → path-native p ; (lift false) → path-native q })

module Comparisons {v : Vertex} (a b : Body v) where
  asBody : Filler stay a b → Body v
  asBody (e , p , h) = compare stay a b e p h
  branch : Filler stay a b → Complete
  branch f = path-package (expression (package (asBody f)))
    (value (package (asBody f))) (value (package (asBody f))) refl
  branch-native : (f : Filler stay a b) → Resolve Seeds (branch f)
  branch-native f = apply
    (reflexivity-rule (expression (package (asBody f))) (value (package (asBody f))))
    (λ _ → derivation (asBody f))
  module Envelope = NativeFamily (Filler stay a b) branch branch-native
  -- The source boundary is EXPLICIT, not inferred from Resolve alone.
  -- No arbitrary atom seed, inverse dynamics or reader-faithfulness premise.
  body : {f g : Filler stay a b} → f ≡ g → Body v
  body alpha = prepared v (Envelope.pathQ alpha) (Envelope.path-native alpha)
    (λ _ → reader b (point b)) (aligned b)
  reuse : {f g : Filler stay a b} (alpha : f ≡ g) {t : Vertex} (h : History v t)
    → Resolve Seeds (package (runBody h (body alpha)))
  reuse alpha h = derivation (runBody h (body alpha))

-- The quantified direct/staged higher witness now has an ACTUAL native
-- retained package, exact recovery, and every boundary-admitted next history.
module Selected {v t : Vertex} (h : History A v) (k : History v t) where
  module C = Comparisons (witness (run (h ++ k) chosen))
    (runBody (mapHistory exchange (h ++ k)) (witness chosen))
  alpha = chosen-direct-staged h k
  higherQ : Complete
  higherQ = C.Envelope.pathQ alpha
  admitted : Resolve Seeds higherQ
  admitted = C.Envelope.path-native alpha
  recovered : cong fst (value higherQ) ≡ alpha
  recovered = C.Envelope.path-recovered alpha
  continue : {z : Vertex} (tail : History (act exchange t) z)
    → Resolve Seeds (package (runBody tail (C.body alpha)))
  continue = C.reuse alpha
