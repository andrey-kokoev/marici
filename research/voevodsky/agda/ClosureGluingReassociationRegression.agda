{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGluingReassociationRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (cong-∙; rUnit)
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureGluingReassociation using (module Chain)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)

-- Three vertices with TWO two-point attachment boundaries. The example
-- retains two separately detectable loops, rather than collapsing to a set.
attach : Bool → Unit
attach _ = tt

module C = Chain Unit Unit Unit Bool Bool attach attach attach attach

includeAB : C.AB → C.Left
includeAB = PO.inl

includeBC : C.BC → C.Right
includeBC = PO.inr

firstLeft : Path C.Left (PO.inl (PO.inl tt)) (PO.inl (PO.inl tt))
firstLeft = cong includeAB (PO.push false ∙ sym (PO.push true))

secondLeft : Path C.Left (PO.inl (PO.inr tt)) (PO.inl (PO.inr tt))
secondLeft = PO.push false ∙ sym (PO.push true)

firstRight : Path C.Right (PO.inl tt) (PO.inl tt)
firstRight = PO.push false ∙ sym (PO.push true)

secondRight : Path C.Right (PO.inr (PO.inl tt)) (PO.inr (PO.inl tt))
secondRight = cong includeBC (PO.push false ∙ sym (PO.push true))

preservesFirst : cong C.associate firstLeft ≡ firstRight
preservesFirst = cong-∙ (λ x → C.associate (PO.inl x))
  (PO.push false) (sym (PO.push true))

preservesSecond : cong C.associate secondLeft ≡ secondRight
preservesSecond = cong-∙ C.associate (PO.push false) (sym (PO.push true))
  ∙ sym (cong-∙ includeBC (PO.push false) (sym (PO.push true)))

detectFirst : C.Right → S¹
detectFirst (PO.inl tt) = base
detectFirst (PO.inr _) = base
detectFirst (PO.push false i) = loop i
detectFirst (PO.push true i) = base

detectSecond : C.Right → S¹
detectSecond (PO.inl tt) = base
detectSecond (PO.inr (PO.inl tt)) = base
detectSecond (PO.inr (PO.inr tt)) = base
detectSecond (PO.inr (PO.push false i)) = loop i
detectSecond (PO.inr (PO.push true i)) = base
detectSecond (PO.push s i) = base

firstDetected : cong detectFirst firstRight ≡ loop
firstDetected = cong-∙ detectFirst (PO.push false) (sym (PO.push true))
  ∙ sym (rUnit loop)

secondIgnoredByFirst : cong detectFirst secondRight ≡ refl
secondIgnoredByFirst = refl

firstIgnoredBySecond : cong detectSecond firstRight ≡ refl
firstIgnoredBySecond = cong-∙ detectSecond (PO.push false) (sym (PO.push true))
  ∙ sym (rUnit refl)

secondDetected : cong detectSecond secondRight ≡ loop
secondDetected = cong-∙ (λ x → detectSecond (PO.inr x))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit loop)

firstNontrivial : firstRight ≡ refl → ⊥
firstNontrivial h = circleLoopNotRefl
  (sym firstDetected ∙ cong (cong detectFirst) h)

secondNontrivial : secondRight ≡ refl → ⊥
secondNontrivial h = circleLoopNotRefl
  (sym secondDetected ∙ cong (cong detectSecond) h)

actualGeneratedComparison : C.Views.view C.rightFull ≡ C.throughReassociation
actualGeneratedComparison = C.generatedIsReassociation

crossArrangementCycle :
  C.Views.closedCycle C.cycle C.identityPresentation ≡ refl
crossArrangementCycle = C.cycleIsTrivial

-- No claim that these computations alone classify the entire loop space,
-- nor that an independently chosen four-piece pentagon has been compared.
