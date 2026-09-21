{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGluingTreeRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.GroupoidLaws using (rUnit; cong-∙)
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true; true≢false)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Sum.Base using (inl; inr)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import Cubical.HITs.Susp.Base using (S¹≃SuspBool)
import Cubical.HITs.Pushout.Base as PO
open import ClosureDependentRefinementTrees
import ClosureDependentRefinementRegression as Previous

-- Unit <- Bool -> Unit is a circle, not a disjoint sum of two points.
f g : Bool → Unit
f _ = tt
g _ = tt

circleEquiv : PO.Pushout f g ≃ S¹
circleEquiv = compEquiv PO.PushoutSusp≃Susp (invEquiv S¹≃SuspBool)

-- Refine the shared boundary into two labelled point slots. This leaves the
-- number of attachments unchanged while changing its actual presentation.
boundaryIso : Iso (Σ[ b ∈ Bool ] Unit) Bool
boundaryIso = iso fst (λ b → b , tt) (λ _ → refl) (λ _ → refl)

boundaryTree : Tree Bool 1
boundaryTree = sigmaNode (isoToEquiv boundaryIso) (λ b → leaf)

gluedTree : Tree S¹ 2
gluedTree = glueNode f g circleEquiv leaf boundaryTree leaf

Full : Type
Full = At gluedTree (full gluedTree)

unfolded : Full ≃ S¹
unfolded = frame gluedTree (full gluedTree)

-- The two refined attachment paths remain separate. Their difference forms
-- the loop; identifying or dropping them would destroy this computation.
gluedLoop : Path Full (PO.inl tt) (PO.inl tt)
gluedLoop = PO.push (false , tt) ∙ sym (PO.push (true , tt))

falseAttachment : cong (equivFun unfolded) (PO.push (false , tt)) ≡ loop
falseAttachment = cong (cong (equivFun circleEquiv)) (sym (rUnit (PO.push false)))

trueAttachment : cong (equivFun unfolded) (PO.push (true , tt)) ≡ refl
trueAttachment = cong (cong (equivFun circleEquiv)) (sym (rUnit (PO.push true)))

preservesLoop : cong (equivFun unfolded) gluedLoop ≡ loop
preservesLoop =
  cong-∙ (equivFun unfolded) (PO.push (false , tt)) (sym (PO.push (true , tt)))
  ∙ cong₂ _∙_ falseAttachment (cong sym trueAttachment)
  ∙ sym (rUnit loop)

module T = Realization (leaf {A = S¹} {n = 0}) gluedTree (idfun S¹)

-- Expose the pushout while keeping the boundary unrefined, then expose its
-- two slots, then return. This is a tree containing BOTH gluing and Σ nodes.
exposed : T.Cuts
exposed = tt , inr (tt , (root boundaryTree , tt))

cycle : T.Views.Cuts.Route T.rootCut T.rootCut
cycle = T.Views.Cuts.step T.rootCut (T.Views.Cuts.step T.fullCut
  (T.Views.Cuts.step exposed (T.Views.Cuts.stay T.rootCut)))

cycleIsTrivial : T.Views.closedCycle cycle (T.Views.Cuts.canonical T.rootCut) ≡ refl
cycleIsTrivial = T.Views.closedCycleIsTrivial cycle (T.Views.Cuts.canonical T.rootCut)

-- Keep the existing dependent/twisted-boundary regression in this closure.
-- Its swap monodromy proves the surviving circle loop is not refl.
module Cover = Previous.TwistedBoundary

circleLoopNotRefl : loop ≡ refl → ⊥
circleLoopNotRefl h = true≢false
  (sym (Cover.monodromy false)
    ∙ cong (λ p → transport (cong Cover.Cover p) false) h
    ∙ transportRefl false)

gluedLoopNotRefl : gluedLoop ≡ refl → ⊥
gluedLoopNotRefl h = circleLoopNotRefl
  (sym preservesLoop ∙ cong (cong (equivFun unfolded)) h)

-- Replacing gluing by a coproduct cannot preserve the labelled vertices:
-- even a single attachment path would then give false=true in Bool.
noDiscreteReplacement : (tag : Full → Bool) →
  tag (PO.inl tt) ≡ false → tag (PO.inr tt) ≡ true → ⊥
noDiscreteReplacement tag left right = false≢true
  (sym left ∙ cong tag (PO.push (false , tt)) ∙ right)
