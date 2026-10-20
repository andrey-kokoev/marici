{-# OPTIONS --safe --cubical --guardedness #-}
module TwoComparisonTwoAttachmentCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using (isSetRetract; isSetΣ; isProp×; isPropΠ)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv; Σ≡Prop)
open import Cubical.Data.List.Base using (List; []; _∷_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using (Vertex; A; B; C; D; AB; BC; BA; AD; Seeds; sigma; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (Out; vertex-is-set)
open import InternalSourceComparisons
open import InternalComparisonInterchange using (graphIso; graphEquiv; module Interchange)
import RepeatedInterchangeCoherence as R
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Second exchange is an explicitly derived inverse-facing comparison of the
-- first comparison graph with its original operand. It is NOT moveInitial
-- applied twice, nor a claim that arbitrary native proof transports are C2.
backPorts : (z : El (expression (package R.First.oldComparison)))
  → sigma (reader R.First.oldComparison z) ≡ reader (seedBody A) (fst z)
backPorts (A , y , w) = cong sigma (sym w)
backPorts (B , y , w) = cong sigma (sym w)
backPorts (C , y , w) = cong sigma (sym w)
backPorts (D , y , w) = cong sigma (sym w)
module K = Interchange exchange B R.First.oldComparison (seedBody A)
  (graphEquiv sigmaEquiv) refl backPorts
module K2 = Interchange exchange A
  (attach R.First.oldComparison (edgeMap exchange R.first))
  (attach (seedBody A) R.first)
  (K.attachmentEquiv (edgeMap exchange R.first))
  (K.attachmentPoint (edgeMap exchange R.first))
  (K.attachmentPorts (edgeMap exchange R.first))
module KS = Interchange stay B
  (K.compareAfterAttach (edgeMap exchange R.first))
  (K.attachAfterCompare (edgeMap exchange R.first))
  (K.interchangeEquiv (edgeMap exchange R.first))
  (K.interchangePoint (edgeMap exchange R.first))
  (K.interchangePorts (edgeMap exchange R.first))

-- The four actual interchange cells are R.First, R.Second, K and K2.
-- K2 uses the original comparison's attached left operand, not a fresh seed.
kSource target : Body C
kSource = K2.compareAfterAttach R.movedSecond
target = attach (K.attachAfterCompare (edgeMap exchange R.first)) R.second
kSequential : El (expression (package kSource)) ≃ El (expression (package target))
kSequential = compEquiv (K2.interchangeEquiv R.movedSecond)
  (KS.attachmentEquiv R.second)
kPorts : (z : El (expression (package kSource)))
  → reader kSource z ≡ reader target (equivFun kSequential z)
kPorts (x , y , w) = sym (cong (λ z → fst (fst z)) w)

-- The first row's exact target is the second row's attached left operand.
-- Reuse its actual repeated interchange, with no reset or extra seed.
f : El (expression (package R.source)) ≃ El (expression (package R.target))
f = R.sequential
fPoint : equivFun f (value (package R.source)) ≡ value (package R.target)
fPoint = R.sequentialPoint

-- The second comparison at depth two is composed from actual interchange
-- and attachment maps. Its choice, including fPoint, is retained explicitly.
e2 : El (expression (package R.source))
  ≃ El (expression (package (attach (attach (seedBody A) R.first) R.second)))
e2 = compEquiv f (K2.attachmentEquiv R.movedSecond)
a1-is-set : isSet (El (expression (package (attach (seedBody A) R.first))))
a1-is-set = isSetΣ (R.out-is-set A) (λ _ → isProp→isSet (vertex-is-set A A))
abstract
  e2Point : equivFun e2 (value (package R.source))
    ≡ value (package (attach (attach (seedBody A) R.first) R.second))
  e2Point i = R.second , a1-is-set _ _
    (snd (equivFun e2 (value (package R.source)))) refl i
e2Ports : (z : El (expression (package R.source)))
  → sigma (reader R.source z)
    ≡ reader (attach (attach (seedBody A) R.first) R.second) (equivFun e2 z)
e2Ports z = cong sigma (R.sequentialPorts z)
  ∙ K2.attachmentPorts R.movedSecond (equivFun f z)
source : Body C
source = compare exchange R.source (attach (attach (seedBody A) R.first) R.second)
  e2 e2Point e2Ports

rebase : El (expression (package source)) ≃ El (expression (package kSource))
rebase = compEquiv (compEquiv (graphEquiv e2) f)
  (invEquiv (graphEquiv (K2.attachmentEquiv R.movedSecond)))
sequential : El (expression (package source)) ≃ El (expression (package target))
sequential = compEquiv rebase kSequential
sequentialPorts : (z : El (expression (package source)))
  → reader source z ≡ reader target (equivFun sequential z)
sequentialPorts (x , y , w) = sym (cong (λ z → fst (fst z)) w)
  ∙ kPorts (equivFun rebase (x , y , w))

-- A distinct fused route contracts both comparison graphs, then lifts the
-- resulting pointed base equivalence through both dependent attachments.
baseGraph : El (expression (package K.oldComparison)) ≃ Vertex
baseGraph = compEquiv (graphEquiv (graphEquiv sigmaEquiv)) (graphEquiv sigmaEquiv)
basePoint : invEq baseGraph (value (package (seedBody A))) ≡ value (package K.oldComparison)
basePoint = retEq baseGraph _
firstBridge : El (expression (package (attach (seedBody A) R.first)))
  ≃ El (expression (package (K.attachAfterCompare (edgeMap exchange R.first))))
firstBridge = Σ-cong-equiv (idEquiv (Out A))
  (λ _ → loopEquiv (invEquiv baseGraph) basePoint)
firstBridgePoint : equivFun firstBridge (value (package (attach (seedBody A) R.first)))
  ≡ value (package (K.attachAfterCompare (edgeMap exchange R.first)))
firstBridgePoint i = R.first , loop-refl (invEquiv baseGraph) basePoint i
lastBridge : El (expression (package (attach (attach (seedBody A) R.first) R.second)))
  ≃ El (expression (package target))
lastBridge = Σ-cong-equiv (idEquiv (Out B)) (λ _ → loopEquiv firstBridge firstBridgePoint)
direct : El (expression (package source)) ≃ El (expression (package target))
direct = compEquiv (compEquiv (graphEquiv e2) (graphEquiv (R.Second.attachmentEquiv R.second))) lastBridge

-- The full maps retain edge witnesses. This auxiliary reader law uses only
-- the proved vertex involution, NOT an involution on native proof histories.
sigma-squared : (v : Vertex) → sigma (sigma v) ≡ v
sigma-squared A = refl
sigma-squared B = refl
sigma-squared C = refl
sigma-squared D = refl
e2-reader : (z : El (expression (package R.source)))
  → reader (attach (attach (seedBody A) R.first) R.second) (equivFun e2 z)
    ≡ fst (fst (fst z))
e2-reader ((o , l) , y , w) = sigma-squared (fst o)
directPorts : (z : El (expression (package source)))
  → reader source z ≡ reader target (equivFun direct z)
directPorts (x , y , w) = sym (cong (λ z → fst (fst z)) w) ∙ e2-reader x

base-is-set : isSet (El (expression (package K.oldComparison)))
base-is-set = isSetRetract (equivFun baseGraph) (invEq baseGraph) (retEq baseGraph) vertex-is-set
first-is-set : isSet (El (expression (package (K.attachAfterCompare (edgeMap exchange R.first)))))
first-is-set = isSetΣ (R.out-is-set A) (λ _ → isProp→isSet (base-is-set _ _))
lastLoop-is-prop : isProp
  (value (package (K.attachAfterCompare (edgeMap exchange R.first)))
    ≡ value (package (K.attachAfterCompare (edgeMap exchange R.first))))
lastLoop-is-prop = first-is-set
  (value (package (K.attachAfterCompare (edgeMap exchange R.first))))
  (value (package (K.attachAfterCompare (edgeMap exchange R.first))))
target-is-set : isSet (El (expression (package target)))
target-is-set = isSetΣ (R.out-is-set B) (λ _ → isProp→isSet lastLoop-is-prop)

-- Reader injectivity is PROVED for this exact carrier; it fails in the
-- retained hidden-Boolean-fiber control. It is not a generic inference rule.
reader-injective : (x y : El (expression (package target)))
  → reader target x ≡ reader target y → x ≡ y
reader-injective (o , l) (o' , l') p = Σ≡Prop (λ _ → lastLoop-is-prop)
  (sym (R.restore-target B o) ∙ cong (R.restoreOut B) p ∙ R.restore-target B o')
abstract
  sequentialPoint : equivFun sequential (value (package source)) ≡ value (package target)
  sequentialPoint = reader-injective _ _ (sym (sequentialPorts (value (package source))))
  directPoint : equivFun direct (value (package source)) ≡ value (package target)
  directPoint = reader-injective _ _ (sym (directPorts (value (package source))))
map-coherence : equivFun sequential ≡ equivFun direct
map-coherence = funExt (λ z → reader-injective _ _ (sym (sequentialPorts z) ∙ directPorts z))
CompleteFiller : Type
CompleteFiller = Σ (El (expression (package source)) ≃ El (expression (package target)))
  (λ e → (equivFun e (value (package source)) ≡ value (package target))
    × ((z : El (expression (package source))) → reader source z ≡ reader target (equivFun e z)))
sequentialFiller directFiller : CompleteFiller
sequentialFiller = sequential , sequentialPoint , sequentialPorts
directFiller = direct , directPoint , directPorts
abstract
  filler-coherence : sequentialFiller ≡ directFiller
  filler-coherence = Σ≡Prop
    (λ e → isProp× (target-is-set _ _) (isPropΠ (λ z → vertex-is-set _ _)))
    (equivEq map-coherence)
asBody : CompleteFiller → Body C
asBody (e , p , h) = compare stay source target e p h
native-history-coherence : PathP
  (λ i → Resolve Seeds (package (asBody (filler-coherence i))))
  (derivation (asBody sequentialFiller)) (derivation (asBody directFiller))
native-history-coherence i = derivation (asBody (filler-coherence i))

-- Retain all four interchange cells, original and intermediate route Bodies.
diagram : List (Σ Vertex Body)
diagram = (B , R.First.oldComparison) ∷ (A , K.oldComparison)
  ∷ (A , R.First.interchange R.first) ∷ (D , R.Second.interchange R.second)
  ∷ (B , K.interchange (edgeMap exchange R.first)) ∷ (C , K2.interchange R.movedSecond)
  ∷ (D , R.source) ∷ (D , R.target) ∷ (C , source) ∷ (C , kSource) ∷ (C , target) ∷ []
