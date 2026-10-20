{-# OPTIONS --safe --cubical --guardedness #-}
module NativeAttachmentHistoryBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv)
open import Cubical.Data.Maybe.Base using (just)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Relation.Nullary.Base using (¬_)
open import NativeExtensionFamilyAudit using (Seeds)
open import SourceIndexedExtensionFamilies using (Out)
open import InternalSourceComparisons using
  (Mode; stay; Body; prepared; compare; attach; package; derivation; reader; aligned; loopEquiv; loop-refl)
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import GeneratedReaderClassification as G
import InternalComparisonInterchange as Native
import RetainedPackageFeedback as Feedback
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

module Bridge {m : Mode} {a b : F.Object} (f : F.Full m a b) (o : Out (fst a)) where
  e = fst (F.Full.payload f)
  oldPackage = F.asPackage f
  oldBody : Body (fst b)
  oldBody = prepared (fst b) oldPackage (F.admitted f)
    (λ z → F.readPort b (fst (snd z))) (aligned (G.body (snd b)))
  retainedBody : Body (fst (M.route f o))
  retainedBody = attach oldBody (M.route f o)
  retainedPackage = package retainedBody
  retained-native : Resolve Seeds retainedPackage
  retained-native = derivation retainedBody
  old-premise-recovered : Feedback.peel (Feedback.peel (retainedPackage , retained-native))
    ≡ (oldPackage , F.admitted f)
  old-premise-recovered = refl

  compiledPackage = F.asPackage (M.attachment f o)
  compiled-native : Resolve Seeds compiledPackage
  compiled-native = F.admitted (M.attachment f o)
  compiledBody : Body (fst (M.route f o))
  compiledBody = prepared _ compiledPackage compiled-native
    (λ z → F.readPort (M.attachObject b (M.route f o)) (fst (snd z)))
    (aligned (G.body (snd (M.attachObject b (M.route f o)))))
  graph = Native.graphEquiv e
  oldLoops = loopEquiv graph {x = value oldPackage} {y = F.point a} refl
  backward-refl : invEq oldLoops refl ≡ refl
  backward-refl = cong (invEq oldLoops)
    (sym (loop-refl graph {x = value oldPackage} {y = F.point a} refl)) ∙ retEq oldLoops refl
  attachmentEquiv = fst (F.Full.payload (M.attachment f o))
  carrierEquiv : El (expression compiledPackage) ≃ El (expression retainedPackage)
  carrierEquiv = compEquiv (Native.graphEquiv attachmentEquiv)
    (Σ-cong-equiv (M.requests f) (λ _ → invEquiv oldLoops))
  selected : equivFun carrierEquiv (value compiledPackage) ≡ value retainedPackage
  selected i = M.route f o , backward-refl i
  ports : (z : El (expression compiledPackage))
    → reader compiledBody z ≡ reader retainedBody (equivFun carrierEquiv z)
  ports (x , y , w) = sym (cong (λ z → fst (fst z)) w)
  bridgeBody : Body (fst (M.route f o))
  bridgeBody = compare stay compiledBody retainedBody carrierEquiv selected ports
  bridge-native : Resolve Seeds (package bridgeBody)
  bridge-native = derivation bridgeBody
  both-orders-recovered : Native.comparisonOperands
      (Native.closure (fst (M.route f o) , bridgeBody))
    ≡ just ((compiledPackage , compiled-native) , (retainedPackage , retained-native))
  both-orders-recovered = refl
  packages-not-equal : ¬ (compiledPackage ≡ retainedPackage)
  packages-not-equal p = false≢true (cong (λ q → Native.outerE (expression q)) p)
  module Continued = Native.Interchange stay (fst (M.route f o)) compiledBody retainedBody
    carrierEquiv selected ports
  continued-native : (next : Out (fst (M.route f o))) → Resolve Seeds (package (Continued.interchange next))
  continued-native next = derivation (Continued.interchange next)
