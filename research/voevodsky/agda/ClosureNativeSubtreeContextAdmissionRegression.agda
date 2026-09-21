{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureNativeSubtreeContextAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureNativeSubtreeContextAdmission using (module Native)
open import ClosureDependentEndpointNaturality using (module Along)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)

module G = Native Unit (λ _ → S¹) (λ _ _ → Unit) (λ _ → base) (λ _ → base)
  using (module C; module Trees)
open G.C.C.A.N
pairWord : Word tt tt
pairWord = cons tt (single tt)
pair : Bracket pairWord
pair = fork (leaf tt) (leaf tt)

-- All THREE rotating subtrees are non-singletons.
module N = G.Trees pair pair pair using (module R; change; coherent; module Hole; contextual)
module R = N.R using (leftTree; rightTree; nativeEquivalence)
module H = N.Hole
rootWord : Word tt tt
rootWord = (pairWord ++ pairWord) ++ pairWord
word : Word tt tt
word = pairWord ++ (rootWord ++ pairWord)
inner : H.Context (rootWord ++ pairWord)
inner = H.left H.hole pair
context : H.Context word
context = H.right pair inner

tenPieces : pieceCount word ≡ 10
tenPieces = refl
rootFrame : G.C.C.frame N.change ≡ R.nativeEquivalence
rootFrame = refl

module E = G.C.C.A.Edges word
edge : E.Admitted (H.plug context R.leftTree) (H.plug context R.rightTree)
edge = N.contextual context
retainsContextFrame : E.actionEquiv edge ≡ G.C.C.frame (G.C.Coherent.base (H.lift context N.coherent))
retainsContextFrame = H.retainsFrame context N.coherent

-- An independent computation on the ENTIRE rotating realization, not just
-- on its external endpoints. In particular native word transport remains.
onHole : (x : Realize R.leftTree) → E.action edge (PO.inr (PO.inl x)) ≡
  PO.inr (PO.inl (equivFun R.nativeEquivalence x))
onHole x = refl

module P = E.Presentations (H.plug context R.leftTree)
fullComparison : P.pack (H.plug context R.rightTree) edge ≡
  P.Views.Cuts.canonical (H.plug context R.rightTree)
fullComparison = P.agreesWithGenerated (H.plug context R.rightTree) edge

backward : E.Admitted (H.plug context R.rightTree) (H.plug context R.leftTree)
backward = E.admitted (invEq (E.actionEquiv edge)) (λ y →
  sym (E.square edge (invEq (E.actionEquiv edge) y))
  ∙ cong (equivFun (normalize (H.plug context R.rightTree))) (secEq (E.actionEquiv edge) y))
cycle : E.Route (H.plug context R.leftTree) (H.plug context R.leftTree)
cycle = E.step backward (E.step edge (E.stay (H.plug context R.leftTree)))
closedCycle : E.typeRoute cycle ≡ refl
closedCycle = E.closedTypeRoute cycle

-- Detect a circle in the rotating subtree before using equivalence to
-- show that contextual admission cannot collapse its loop.
detectRoot : Realize R.leftTree → S¹
detectRoot (PO.inl (PO.inl (PO.inl x))) = x
detectRoot (PO.inl (PO.inl (PO.inr _))) = base
detectRoot (PO.inl (PO.inl (PO.push tt i))) = base
detectRoot (PO.inl (PO.inr _)) = base
detectRoot (PO.inl (PO.push tt i)) = base
detectRoot (PO.inr _) = base
detectRoot (PO.push tt i) = base

detect : Realize (H.plug context R.leftTree) → S¹
detect (PO.inl _) = base
detect (PO.inr (PO.inl x)) = detectRoot x
detect (PO.inr (PO.inr _)) = base
detect (PO.inr (PO.push tt i)) = base
detect (PO.push tt i) = base
include : S¹ → Realize (H.plug context R.leftTree)
include x = PO.inr (PO.inl (PO.inl (PO.inl (PO.inl x))))
sourceLoop : include base ≡ include base
sourceLoop = cong include loop
observed : cong detect sourceLoop ≡ loop
observed = refl
noCollapse : cong (E.action edge) sourceLoop ≡ refl → ⊥
noCollapse h = circleLoopNotRefl (sym observed ∙ cong (cong detect)
  (sym (retEq pathFrame sourceLoop) ∙ cong (invEq pathFrame) h ∙ retEq pathFrame refl))
  where
  pathFrame : (include base ≡ include base) ≃ (E.action edge (include base) ≡ E.action edge (include base))
  pathFrame = congEquiv (E.actionEquiv edge)

attachmentNotEquivalence : isEquiv (λ (_ : Unit) → base) → ⊥
attachmentNotEquivalence proof = circleLoopNotRefl
  (isProp→isSet (isContr→isProp (base , secEq ((λ _ → base) , proof))) base base loop refl)

-- A separate transport probe with nonreflexive endpoint AND source
-- normalization witness; the latter varies dependently to reflexivity.
module Moving = Along (λ _ → S¹) (λ _ → S¹) (λ _ x → x) loop
module MovingPort = Moving.Port (refl {x = base}) (λ i j → loop (i ∨ j))
targetWitnessIsRefl : MovingPort.target ≡ refl
targetWitnessIsRefl = refl
sourceWitnessNotNull : (λ j → loop (i0 ∨ j)) ≡ refl → ⊥
sourceWitnessNotNull = circleLoopNotRefl
transportBoundary : (Moving.frame ∙ cong (λ x → x) Moving.endpoint) ∙ refl ≡
  MovingPort.source ∙ fromPathP (refl {x = base})
transportBoundary = MovingPort.boundary
