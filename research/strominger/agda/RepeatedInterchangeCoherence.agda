{-# OPTIONS --safe --cubical --guardedness #-}
module RepeatedInterchangeCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.HLevels using
  (isSetRetract; isSetΣ; isProp×; isPropΠ)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv; Σ≡Prop)
open import Cubical.Data.List.Base using (List; []; _∷_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import InterchangeHiddenFiberObstruction
open import NativeExtensionFamilyAudit using
  (Vertex; A; B; C; D; AB; BC; CA; BA; AD; DB; Seeds; sigmaEquiv)
open import SourceIndexedExtensionFamilies using (Out; vertex-is-set)
open import InternalSourceComparisons
open import InternalComparisonInterchange using (graphIso; graphEquiv; module Interchange)
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Source incidence is simple: the target identifies an outgoing witness.
-- Retraction proves sethood without assuming proof irrelevance of Code or
-- arbitrary native derivation types.
restoreOut : (v : Vertex) → Vertex → Out v
restoreOut A B = B , AB
restoreOut A _ = D , AD
restoreOut B A = A , BA
restoreOut B _ = C , BC
restoreOut C _ = A , CA
restoreOut D _ = B , DB
restore-target : (v : Vertex) (o : Out v) → restoreOut v (fst o) ≡ o
restore-target _ (_ , AB) = refl
restore-target _ (_ , BC) = refl
restore-target _ (_ , CA) = refl
restore-target _ (_ , BA) = refl
restore-target _ (_ , AD) = refl
restore-target _ (_ , DB) = refl
out-is-set : (v : Vertex) → isSet (Out v)
out-is-set v = isSetRetract fst (restoreOut v) (restore-target v) vertex-is-set

module First = Interchange exchange A (seedBody A) (seedBody B) sigmaEquiv refl (λ x → refl)
first : Out A
first = B , AB
second : Out B
second = C , BC
movedSecond : Out A
movedSecond = edgeMap exchange second

module Second = Interchange exchange B
  (attach (seedBody A) first) (attach (seedBody B) (edgeMap exchange first))
  (First.attachmentEquiv first) (First.attachmentPoint first) (First.attachmentPorts first)
module Slide = Interchange stay A
  (First.compareAfterAttach first) (First.attachAfterCompare first)
  (First.interchangeEquiv first) (First.interchangePoint first) (First.interchangePorts first)

source middle target : Body D
source = Second.compareAfterAttach second
middle = Second.attachAfterCompare second
target = attach (First.attachAfterCompare first) movedSecond

sequential : El (expression (package source)) ≃ El (expression (package target))
sequential = compEquiv (Second.interchangeEquiv second) (Slide.attachmentEquiv movedSecond)
sequentialPorts : (z : El (expression (package source)))
  → reader source z ≡ reader target (equivFun sequential z)
sequentialPorts (x , y , w) = sym (cong (λ z → fst (fst z)) w)

-- Direct route: compare the earlier attachment with its comparison-first
-- presentation, then lift that bridge to the last loop fiber in one step.
firstGraph : El (expression (package (First.compareAfterAttach first)))
  ≃ El (expression (package (attach (seedBody A) first)))
firstGraph = graphEquiv (First.attachmentEquiv first)
bridge : El (expression (package (attach (seedBody A) first)))
  ≃ El (expression (package (First.attachAfterCompare first)))
bridge = compEquiv (invEquiv firstGraph) (First.interchangeEquiv first)
bridgePoint : equivFun bridge (value (package (attach (seedBody A) first)))
  ≡ value (package (First.attachAfterCompare first))
bridgePoint = cong (equivFun (First.interchangeEquiv first))
  (retEq firstGraph (value (package (First.compareAfterAttach first))))
  ∙ First.interchangePoint first

direct : El (expression (package source)) ≃ El (expression (package target))
direct = compEquiv (graphEquiv (Second.attachmentEquiv second))
  (Σ-cong-equiv (edgeEquiv exchange B) (λ _ → loopEquiv bridge bridgePoint))
directPorts : (z : El (expression (package source)))
  → reader source z ≡ reader target (equivFun direct z)
directPorts (x , y , w) = sym (cong (λ z → fst (fst z)) w)

-- This particular diagram has set-valued interpreted carriers. Establish
-- that fact; do not promote endpoint agreement into arbitrary higher filling.
oldGraph-is-set : isSet (El (expression (package First.oldComparison)))
oldGraph-is-set = isSetRetract (Iso.fun (graphIso sigmaEquiv))
  (Iso.inv (graphIso sigmaEquiv)) (Iso.leftInv (graphIso sigmaEquiv)) vertex-is-set
firstTarget-is-set : isSet (El (expression (package (First.attachAfterCompare first))))
firstTarget-is-set = isSetΣ (out-is-set B)
  (λ _ → isProp→isSet (oldGraph-is-set
    (value (package First.oldComparison)) (value (package First.oldComparison))))
lastLoop-is-prop : isProp
  (value (package (First.attachAfterCompare first)) ≡ value (package (First.attachAfterCompare first)))
lastLoop-is-prop = firstTarget-is-set _ _
target-is-set : isSet (El (expression (package target)))
target-is-set = isSetΣ (out-is-set A) (λ _ → isProp→isSet lastLoop-is-prop)

-- At this concrete set-valued boundary, selected-value witnesses are unique.
-- Construct them through the same local loop contraction rather than expanding
-- large nested path-composition normal forms. Original leg witnesses remain
-- retained separately in the certificate diagram.
sequentialPoint : equivFun sequential (value (package source)) ≡ value (package target)
sequentialPoint i = movedSecond , lastLoop-is-prop
  (snd (equivFun sequential (value (package source)))) refl i
directPoint : equivFun direct (value (package source)) ≡ value (package target)
directPoint i = movedSecond , lastLoop-is-prop
  (snd (equivFun direct (value (package source)))) refl i

-- The final outgoing-edge components compute identically. Their retained
-- loop components agree by the proved local sethood, not a global truncation.
map-coherence : equivFun sequential ≡ equivFun direct
map-coherence = funExt (λ z i → fst (equivFun direct z)
  , lastLoop-is-prop (snd (equivFun sequential z)) (snd (equivFun direct z)) i)
equivalence-coherence : sequential ≡ direct
equivalence-coherence = equivEq map-coherence

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
    equivalence-coherence

asBody : CompleteFiller → Body D
asBody (e , p , h) = compare stay source target e p h
whole-comparison-coherence : asBody sequentialFiller ≡ asBody directFiller
whole-comparison-coherence = cong asBody filler-coherence
native-history-coherence : PathP
  (λ i → Resolve Seeds (package (asBody (filler-coherence i))))
  (derivation (asBody sequentialFiller)) (derivation (asBody directFiller))
native-history-coherence i = derivation (asBody (filler-coherence i))

-- Retain the diagram, intermediate comparison legs, both whole fillers and
-- their higher witness. The higher path is formed, not falsely declared to
-- have an automatic native higher-rule derivation from these seeds.
closureOf : {v : Vertex} → Body v → Closure Seeds
closureOf b = package b , derivation b
record Certificate : Type₁ where
  field
    rawDiagram : List (Σ Vertex Body)
    diagram : List (Closure Seeds)
    left right : CompleteFiller
    leftHistory : Resolve Seeds (package (asBody left))
    rightHistory : Resolve Seeds (package (asBody right))
    higher : left ≡ right
certificate : Certificate
Certificate.rawDiagram certificate = (D , source) ∷ (D , middle) ∷ (D , target)
  ∷ (A , First.interchange first) ∷ (D , Second.interchange second)
  ∷ (D , compare stay middle target (Slide.attachmentEquiv movedSecond)
      (Slide.attachmentPoint movedSecond) (Slide.attachmentPorts movedSecond)) ∷ []
Certificate.diagram certificate = closureOf source ∷ closureOf middle ∷ closureOf target
  ∷ closureOf (First.interchange first) ∷ closureOf (Second.interchange second)
  ∷ closureOf (compare stay middle target (Slide.attachmentEquiv movedSecond)
      (Slide.attachmentPoint movedSecond) (Slide.attachmentPorts movedSecond)) ∷ []
Certificate.left certificate = sequentialFiller
Certificate.right certificate = directFiller
Certificate.leftHistory certificate = derivation (asBody sequentialFiller)
Certificate.rightHistory certificate = derivation (asBody directFiller)
Certificate.higher certificate = filler-coherence
reified : Whole.Universe.Complete (ℓ-suc ℓ-zero)
reified = Whole.Universe.pack (Whole.Universe.atom Certificate) certificate
recovery : Whole.Universe.value reified ≡ certificate
recovery = refl
higher-package-formed : Complete
higher-package-formed = path-package (atom CompleteFiller) sequentialFiller directFiller filler-coherence
