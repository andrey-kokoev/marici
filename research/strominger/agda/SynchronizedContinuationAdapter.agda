{-# OPTIONS --safe --cubical --guardedness #-}
module SynchronizedContinuationAdapter where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
open import Cubical.Data.Maybe.Base using (just)
open import NativeExtensionFamilyAudit using (Vertex; Seeds; A; B; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons
import SourceIndexedContinuationAdapter as Source
import InternalComparisonInterchange as Native
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

module Adapter (m : Mode) {v : Vertex} (a : Body v) (b : Body (act m v))
  (e : El (expression (package a)) ≃ El (expression (package b)))
  (p : equivFun e (value (package a)) ≡ value (package b))
  (h : (x : El (expression (package a))) → act m (reader a x) ≡ reader b (equivFun e x)) where
  module S = Source.Adapter m a b e p h
  Request = S.P.Synchronized S.z
  route : Request → Out (act m v)
  route r = S.route (fst r)
  syncPackage : Request → Complete
  syncPackage r = E-package Request (λ _ → S.loopPackage) r
  syncDerivation : (r : Request) → Resolve Seeds (syncPackage r)
  syncDerivation r = apply (E-rule Request (λ _ → S.loopPackage) r)
    (λ _ → apply (reflexivity-rule (expression (package S.old)) S.z) (λ _ → derivation S.old))
  syncBody : (r : Request) → Body (fst (route r))
  syncBody r = prepared (fst (route r)) (syncPackage r) (syncDerivation r)
    (λ q → fst (route (fst q))) refl
  toSource : (r : Request)
    → El (expression (package (syncBody r))) ≃ El (expression (package (S.sourceBody (fst r))))
  toSource r = Σ-cong-equiv (S.P.synchronized-source S.z) (λ _ → idEquiv _)
  toTarget : (r : Request)
    → El (expression (package (syncBody r))) ≃ El (expression (package (S.targetBody (fst r))))
  toTarget r = Σ-cong-equiv (compEquiv (S.P.synchronized-source S.z) S.routedEquiv)
    (λ _ → idEquiv _)
  direct-via-source : (r : Request)
    → toTarget r ≡ compEquiv (toSource r) (S.attachmentEquiv (fst r))
  direct-via-source r = equivEq refl

  -- Recovery includes the original target request AND synchronization path.
  -- It is a path, not a claim of judgmental restoration of an arbitrary tuple.
  request-recovered : (r : Request)
    → invEq (S.P.synchronized-source S.z) (fst r) ≡ r
  request-recovered = retEq (S.P.synchronized-source S.z)
  full-source-recovery : (r : Request) (q : El (expression (package (syncBody r))))
    → invEq (toSource r) (equivFun (toSource r) q) ≡ q
  full-source-recovery r = retEq (toSource r)
  full-target-recovery : (r : Request) (q : El (expression (package (syncBody r))))
    → invEq (toTarget r) (equivFun (toTarget r) q) ≡ q
  full-target-recovery r = retEq (toTarget r)
  loop-preserved : (r : Request) (q : El (expression (package (syncBody r))))
    → snd (equivFun (toTarget r) q) ≡ snd q
  loop-preserved r q = refl
  return-port : (r : Request) → act m (fst (fst r)) ≡ fst (route r)
  return-port r = S.return-port (fst r)

  sourceComparison : (r : Request) → Body (fst (route r))
  sourceComparison r = compare stay (syncBody r) (S.sourceBody (fst r)) (toSource r) refl (λ _ → refl)
  targetComparison : (r : Request) → Body (fst (route r))
  targetComparison r = compare stay (syncBody r) (S.targetBody (fst r)) (toTarget r) refl (λ _ → refl)
  source-native : (r : Request) → Resolve Seeds (package (sourceComparison r))
  source-native r = derivation (sourceComparison r)
  target-native : (r : Request) → Resolve Seeds (package (targetComparison r))
  target-native r = derivation (targetComparison r)
  source-operands : (r : Request)
    → Native.comparisonOperands (Native.closure (fst (route r) , sourceComparison r))
      ≡ just (Native.closure (fst (route r) , syncBody r)
             , Native.closure (fst (route r) , S.sourceBody (fst r)))
  source-operands r = refl
  target-operands : (r : Request)
    → Native.comparisonOperands (Native.closure (fst (route r) , targetComparison r))
      ≡ just (Native.closure (fst (route r) , syncBody r)
             , Native.closure (fst (route r) , S.targetBody (fst r)))
  target-operands r = refl

  module Continued (r : Request) where
    module SourceLaw = Native.Interchange stay (fst (route r)) (syncBody r) (S.sourceBody (fst r))
      (toSource r) refl (λ _ → refl)
    module TargetLaw = Native.Interchange stay (fst (route r)) (syncBody r) (S.targetBody (fst r))
      (toTarget r) refl (λ _ → refl)
    source-interchange-native : (o : Out (fst (route r))) → Resolve Seeds (package (SourceLaw.interchange o))
    source-interchange-native o = derivation (SourceLaw.interchange o)
    target-interchange-native : (o : Out (fst (route r))) → Resolve Seeds (package (TargetLaw.interchange o))
    target-interchange-native o = derivation (TargetLaw.interchange o)

module Example = Adapter exchange (seedBody A) (seedBody B) sigmaEquiv refl (λ x → refl)
