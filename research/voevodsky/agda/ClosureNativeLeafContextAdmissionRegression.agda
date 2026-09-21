{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureNativeLeafContextAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureNativeLeafContextAdmission using (module Native)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
import ClosureContextualForkAdmissionRegression as Previous

module G = Native Unit (λ _ → S¹) (λ _ _ → Unit) (λ _ → base) (λ _ → base)
module R = G.Three tt tt tt
open G.G.A.N
module H = R.Hole

pair : Bracket (cons tt (single tt))
pair = fork (leaf tt) (leaf tt)
word : Word tt tt
word = ((cons tt (single tt)) ++ (R.T.word ++ cons tt (single tt))) ++ cons tt (single tt)
inner : H.Context (R.T.word ++ cons tt (single tt))
inner = H.left H.hole pair
middle : H.Context ((cons tt (single tt)) ++ (R.T.word ++ cons tt (single tt)))
middle = H.right pair inner
context : H.Context word
context = H.left middle pair

ninePieces : pieceCount word ≡ 9
ninePieces = refl
sourceDepth : depth (H.plug context R.T.leftTree) ≡ 5
sourceDepth = refl
targetDepth : depth (H.plug context R.T.rightTree) ≡ 5
targetDepth = refl

module E = G.G.A.Edges word
edge : E.Admitted (H.plug context R.T.leftTree) (H.plug context R.T.rightTree)
edge = R.contextual context

-- Independent strict contextual implementation: attachment paths are
-- mapped directly to attachment paths, without LiftSpan's unit padding.
strictInner : Realize (H.plug inner R.T.leftTree) → Realize (H.plug inner R.T.rightTree)
strictInner (PO.inl x) = PO.inl (R.T.Raw.associate x)
strictInner (PO.inr x) = PO.inr x
strictInner (PO.push tt i) = PO.push tt i
strictMiddle : Realize (H.plug middle R.T.leftTree) → Realize (H.plug middle R.T.rightTree)
strictMiddle (PO.inl x) = PO.inl x
strictMiddle (PO.inr x) = PO.inr (strictInner x)
strictMiddle (PO.push tt i) = PO.push tt i
strict : Realize (H.plug context R.T.leftTree) → Realize (H.plug context R.T.rightTree)
strict (PO.inl x) = PO.inl (strictMiddle x)
strict (PO.inr x) = PO.inr x
strict (PO.push tt i) = PO.push tt i

innerAgrees : (x : Realize (H.plug inner R.T.leftTree)) →
  G.G.A.Edges.action (R.contextual inner) x ≡ strictInner x
innerAgrees (PO.inl x) = refl
innerAgrees (PO.inr x) = refl
innerAgrees (PO.push tt i) j = sym (rUnit (PO.push tt)) j i
middleAgrees : (x : Realize (H.plug middle R.T.leftTree)) →
  G.G.A.Edges.action (R.contextual middle) x ≡ strictMiddle x
middleAgrees (PO.inl x) = refl
middleAgrees (PO.inr x) j = PO.inr (innerAgrees x j)
middleAgrees (PO.push tt i) j = sym (rUnit (PO.push tt)) j i
agrees : (x : Realize (H.plug context R.T.leftTree)) → E.action edge x ≡ strict x
agrees (PO.inl x) j = PO.inl (middleAgrees x j)
agrees (PO.inr x) = refl
agrees (PO.push tt i) j = sym (rUnit (PO.push tt)) j i

strictEdge : E.Admitted (H.plug context R.T.leftTree) (H.plug context R.T.rightTree)
strictEdge = E.admitted strict (λ x →
  cong (equivFun (normalize (H.plug context R.T.rightTree))) (sym (agrees x)) ∙ E.square edge x)

backward : E.Admitted (H.plug context R.T.rightTree) (H.plug context R.T.leftTree)
backward = E.admitted (invEq (E.actionEquiv strictEdge)) (λ y →
  sym (E.square strictEdge (invEq (E.actionEquiv strictEdge) y))
  ∙ cong (equivFun (normalize (H.plug context R.T.rightTree))) (secEq (E.actionEquiv strictEdge) y))

cycle : E.Route (H.plug context R.T.leftTree) (H.plug context R.T.leftTree)
cycle = E.step backward (E.step strictEdge (E.stay (H.plug context R.T.leftTree)))
closedCycle : E.typeRoute cycle ≡ refl
closedCycle = E.closedTypeRoute cycle
residualIdentity : (x : Realize (H.plug context R.T.leftTree)) → transport (E.typeRoute cycle) x ≡ x
residualIdentity = E.residualIsIdentity cycle

module P = E.Presentations (H.plug context R.T.leftTree)
fullComparison : P.pack (H.plug context R.T.rightTree) strictEdge ≡
  P.Views.Cuts.canonical (H.plug context R.T.rightTree)
fullComparison = P.agreesWithGenerated (H.plug context R.T.rightTree) strictEdge

-- Detect a loop of the rotating subtree AFTER the strict contextual map.
detectRoot : R.T.Raw.Right → S¹
detectRoot (PO.inl x) = x
detectRoot (PO.inr _) = base
detectRoot (PO.push tt i) = base
detect : Realize (H.plug context R.T.rightTree) → S¹
detect (PO.inr _) = base
detect (PO.inl (PO.inl _)) = base
detect (PO.inl (PO.inr (PO.inl x))) = detectRoot x
detect (PO.inl (PO.inr (PO.inr _))) = base
detect (PO.inl (PO.inr (PO.push tt i))) = base
detect (PO.inl (PO.push tt i)) = base
detect (PO.push tt i) = base

include : S¹ → Realize (H.plug context R.T.leftTree)
include x = PO.inl (PO.inr (PO.inl (PO.inl (PO.inl x))))
sourceLoop : include base ≡ include base
sourceLoop = cong include loop
observed : cong (λ x → detect (strict x)) sourceLoop ≡ loop
observed = refl
noCollapse : cong strict sourceLoop ≡ refl → ⊥
noCollapse h = circleLoopNotRefl (sym observed ∙ cong (cong detect) h)

attachmentNotEquivalence : isEquiv (λ (_ : Unit) → base) → ⊥
attachmentNotEquivalence = Previous.attachmentNotEquivalence
