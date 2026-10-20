{-# OPTIONS --safe --cubical --guardedness #-}
module SourceIndexedContinuationAdapter where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Transport using (substEquiv)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
open import Cubical.Data.Maybe.Base using (just)
open import NativeExtensionFamilyAudit using (Vertex; Seeds; A; B; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons
import ContinuationSidePolicies as Policies
import InternalComparisonInterchange as Native
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Changing the source of an edge by transport preserves its target label.
transport-target : {x y : Vertex} (p : x ≡ y) (o : Out x)
  → fst (subst Out p o) ≡ fst o
transport-target {x} p o = J (λ y p → fst (subst Out p o) ≡ fst o)
  (cong fst (substRefl {B = Out} o)) p

module Adapter (m : Mode) {v : Vertex} (a : Body v) (b : Body (act m v))
  (e : El (expression (package a)) ≃ El (expression (package b)))
  (p : equivFun e (value (package a)) ≡ value (package b))
  (h : (x : El (expression (package a))) → act m (reader a x) ≡ reader b (equivFun e x)) where

  module P = Policies.Policies m a b e p h
  old : Body (act m v)
  old = compare m a b e p h
  z = value (package old)
  Request = Out (P.source z)
  routedEquiv : Request ≃ Out (act m v)
  routedEquiv = compEquiv (P.requests z) (substEquiv Out (aligned old))
  route : Request → Out (act m v)
  route = equivFun routedEquiv
  return-port : (s : Request) → act m (fst s) ≡ fst (route s)
  return-port s = edge-target m (P.source z) s
    ∙ sym (transport-target (P.ports z) (equivFun (edgeEquiv m (P.source z)) s))
    ∙ sym (transport-target (aligned old) (P.route z s))

  loopPackage = path-package (expression (package old)) z z refl
  sourcePackage : Request → Complete
  sourcePackage s = E-package Request (λ _ → loopPackage) s
  sourceDerivation : (s : Request) → Resolve Seeds (sourcePackage s)
  sourceDerivation s = apply (E-rule Request (λ _ → loopPackage) s)
    (λ _ → apply (reflexivity-rule (expression (package old)) z) (λ _ → derivation old))

  -- A separately named adapter, not a change to Body.attach or Body.reader.
  -- Its request index is source-side; its output reader routes that request.
  sourceBody : (s : Request) → Body (fst (route s))
  sourceBody s = prepared (fst (route s)) (sourcePackage s) (sourceDerivation s)
    (λ q → fst (route (fst q))) refl
  targetBody : (s : Request) → Body (fst (route s))
  targetBody s = attach old (route s)
  attachmentEquiv : (s : Request)
    → El (expression (package (sourceBody s))) ≃ El (expression (package (targetBody s)))
  attachmentEquiv s = Σ-cong-equiv routedEquiv (λ _ → idEquiv _)
  attachmentPoint : (s : Request)
    → equivFun (attachmentEquiv s) (value (package (sourceBody s))) ≡ value (package (targetBody s))
  attachmentPoint s = refl
  attachmentPorts : (s : Request) (q : El (expression (package (sourceBody s))))
    → reader (sourceBody s) q ≡ reader (targetBody s) (equivFun (attachmentEquiv s) q)
  attachmentPorts s q = refl
  loop-preserved : (s : Request) (q : El (expression (package (sourceBody s))))
    → snd (equivFun (attachmentEquiv s) q) ≡ snd q
  loop-preserved s q = refl
  full-value-recovered : (s : Request) (q : El (expression (package (sourceBody s))))
    → invEq (attachmentEquiv s) (equivFun (attachmentEquiv s) q) ≡ q
  full-value-recovered s = retEq (attachmentEquiv s)

  adapterComparison : (s : Request) → Body (fst (route s))
  adapterComparison s = compare stay (sourceBody s) (targetBody s)
    (attachmentEquiv s) (attachmentPoint s) (attachmentPorts s)
  comparison-native : (s : Request) → Resolve Seeds (package (adapterComparison s))
  comparison-native s = derivation (adapterComparison s)
  operands-retained : (s : Request)
    → Native.comparisonOperands (Native.closure (fst (route s) , adapterComparison s))
      ≡ just (Native.closure (fst (route s) , sourceBody s)
             , Native.closure (fst (route s) , targetBody s))
  operands-retained s = refl

  -- Reuse the actual native interchange, now bound to this derived adapter
  -- comparison. Every next edge is permitted; there is no fresh filler input.
  module Continued (s : Request) where
    module Law = Native.Interchange stay (fst (route s)) (sourceBody s) (targetBody s)
      (attachmentEquiv s) (attachmentPoint s) (attachmentPorts s)
    module Retained = Native.Retention stay (fst (route s)) (sourceBody s) (targetBody s)
      (attachmentEquiv s) (attachmentPoint s) (attachmentPorts s)
    interchange-native : (o : Out (fst (route s))) → Resolve Seeds (package (Law.interchange o))
    interchange-native o = derivation (Law.interchange o)
    both-routes-retained = Retained.both-routes-retained

module Example = Adapter exchange (seedBody A) (seedBody B) sigmaEquiv refl (λ x → refl)
