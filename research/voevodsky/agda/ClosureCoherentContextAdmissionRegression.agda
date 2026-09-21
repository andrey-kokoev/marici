{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureCoherentContextAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureCoherentContextAdmission using (module Contexts)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
import ClosureContextualForkAdmissionRegression as Previous

module G = Contexts Unit (λ _ → S¹) (λ _ _ → Unit) (λ _ → base) (λ _ → base)
open G.C.A.N
module H = G.InHole (single tt)

point : Bracket (single tt)
point = leaf tt
pair : Bracket (cons tt (single tt))
pair = fork point point

change : G.Coherent point point
change = G.coherent Previous.turn Previous.port Previous.port
  Previous.firstCoherence Previous.coherence

word : Word tt tt
word = ((cons tt (single tt)) ++ (single tt ++ cons tt (single tt))) ++ cons tt (single tt)
context : H.Context word
context = H.left (H.right pair (H.left H.hole pair)) pair

sevenPieces : pieceCount word ≡ 7
sevenPieces = refl
fourDeep : depth (H.plug context point) ≡ 4
fourDeep = refl

lifted : G.Coherent (H.plug context point) (H.plug context point)
lifted = H.lift context change
module E = G.C.A.Edges word
module P = E.Presentations (H.plug context point)

edge : E.Admitted (H.plug context point) (H.plug context point)
edge = H.admitted context change
retainsFrame : E.actionEquiv edge ≡ G.C.frame (G.Coherent.base lifted)
retainsFrame = H.retainsFrame context change

fullCompatibility : P.pack (H.plug context point) edge ≡ P.Views.Cuts.canonical (H.plug context point)
fullCompatibility = P.agreesWithGenerated (H.plug context point) edge

-- A constructor-level detector for the hole through all three ancestors.
-- Each intervening attachment face is checked, not only the vertices.
detect : Realize (H.plug context point) → S¹
detect (PO.inr _) = base
detect (PO.inl (PO.inl _)) = base
detect (PO.inl (PO.inr (PO.inl x))) = x
detect (PO.inl (PO.inr (PO.inr _))) = base
detect (PO.inl (PO.inr (PO.push tt i))) = base
detect (PO.inl (PO.push tt i)) = base
detect (PO.push tt i) = base

include : S¹ → Realize (H.plug context point)
include x = PO.inl (PO.inr (PO.inl x))

holeLoop : Path (Realize (H.plug context point)) (include base) (include base)
holeLoop = cong include loop
holeDetected : cong detect holeLoop ≡ loop
holeDetected = refl
holeNotNull : holeLoop ≡ refl → ⊥
holeNotNull h = circleLoopNotRefl (sym holeDetected ∙ cong (cong detect) h)

noCollapse : cong (E.action edge) holeLoop ≡ refl → ⊥
noCollapse h = holeNotNull
  (sym (retEq (congEquiv (E.actionEquiv edge)) holeLoop)
    ∙ cong (invEq (congEquiv (E.actionEquiv edge))) h
    ∙ retEq (congEquiv (E.actionEquiv edge)) refl)
