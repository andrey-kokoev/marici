{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGeneralRotationAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹)
open import ClosureGeneralRotationAdmission using (module General)
import ClosureGluingReassociationRegression as Earlier
import ClosureRotationAdmissionRegression as Previous

-- The actual two-loop example excluded by the old invertible-leg gate.
attach : Bool → Unit
attach _ = tt

module G = General Unit (λ _ → Unit) (λ _ _ → Bool) attach attach
module R = G.ThreeLeaf tt tt tt
module E = R.E

leftLegIsNotInvertible : isEquiv attach → ⊥
leftLegIsNotInvertible proof = false≢true
  (sym (retEq (attach , proof) false) ∙ retEq (attach , proof) true)

-- The independently constructed associator is now admitted despite that
-- obstruction. Both internal loops remain the previously detected loops.
firstLoopRetained : cong R.Raw.associate Earlier.firstLeft ≡ Earlier.firstRight
firstLoopRetained = Earlier.preservesFirst

secondLoopRetained : cong R.Raw.associate Earlier.secondLeft ≡ Earlier.secondRight
secondLoopRetained = Earlier.preservesSecond

firstImageNontrivial : cong R.Raw.associate Earlier.firstLeft ≡ refl → ⊥
firstImageNontrivial h = Earlier.firstNontrivial (sym firstLoopRetained ∙ h)

secondImageNontrivial : cong R.Raw.associate Earlier.secondLeft ≡ refl → ⊥
secondImageNontrivial h = Earlier.secondNontrivial (sym secondLoopRetained ∙ h)

fullCompatibleComparison : R.Presentations.pack R.rightTree R.forward ≡
  R.Presentations.Views.Cuts.canonical R.rightTree
fullCompatibleComparison = R.compatibleComparison

cycle : E.Route R.leftTree R.leftTree
cycle = E.step R.backward (E.step R.forward (E.stay R.leftTree))

actualTypeCycleIsTrivial : E.typeRoute cycle ≡ refl
actualTypeCycleIsTrivial = E.closedTypeRoute cycle

residualIsIdentity : (x : G.A.N.Realize R.leftTree) → transport (E.typeRoute cycle) x ≡ x
residualIsIdentity = E.residualIsIdentity cycle

-- On the earlier circle-valued identity spans, compare the two independently
-- constructed admission records. This is a comparison of FULL compatible
-- presentations, not an assertion of proof irrelevance for their squares.
module Circles = General Unit (λ _ → S¹) (λ _ _ → S¹) (λ x → x) (λ x → x)
module C = Circles.ThreeLeaf tt tt tt

agreesWithEarlierAdmission :
  C.Presentations.pack C.rightTree C.forward ≡
  C.Presentations.pack C.rightTree Previous.R.forward
agreesWithEarlierAdmission = C.Presentations.Views.Cuts.compare C.rightTree _ _
