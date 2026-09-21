{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureGluingPentagonRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (cong-∙; rUnit)
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureGluingPentagon using (module FourPieces)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
-- Recheck the previous three-piece regression in this dependency closure.
import ClosureGluingReassociationRegression

attach : Bool → Unit
attach _ = tt

module P = FourPieces Unit Unit Unit Unit Bool Bool Bool
  attach attach attach attach attach attach

includeAB : P.ABC.AB → P.Start
includeAB x = PO.inl (PO.inl x)

includeABC : P.ABC.Left → P.Start
includeABC = PO.inl

loopS : Path P.Start (PO.inl (PO.inl (PO.inl tt))) (PO.inl (PO.inl (PO.inl tt)))
loopS = cong includeAB (PO.push false ∙ sym (PO.push true))

loopT : Path P.Start (PO.inl (PO.inl (PO.inr tt))) (PO.inl (PO.inl (PO.inr tt)))
loopT = cong includeABC (PO.push false ∙ sym (PO.push true))

loopU : Path P.Start (PO.inl (PO.inr tt)) (PO.inl (PO.inr tt))
loopU = PO.push false ∙ sym (PO.push true)

-- Assign independently chosen circle loops to the three attachment pairs.
-- This is a detector, not an asserted classification of the whole loop space.
observe : (p q r : base ≡ base) → P.Finish → S¹
observe p q r (PO.inl tt) = base
observe p q r (PO.inr (PO.inl tt)) = base
observe p q r (PO.inr (PO.inr (PO.inl tt))) = base
observe p q r (PO.inr (PO.inr (PO.inr tt))) = base
observe p q r (PO.inr (PO.inr (PO.push false i))) = r i
observe p q r (PO.inr (PO.inr (PO.push true i))) = base
observe p q r (PO.inr (PO.push false i)) = q i
observe p q r (PO.inr (PO.push true i)) = base
observe p q r (PO.push false i) = p i
observe p q r (PO.push true i) = base

longS : (p q r : base ≡ base) →
  cong (λ x → observe p q r (P.longRoute x)) loopS ≡ p
longS p q r = cong-∙ (λ x → observe p q r (P.longRoute (includeAB x)))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit p)

longT : (p q r : base ≡ base) →
  cong (λ x → observe p q r (P.longRoute x)) loopT ≡ q
longT p q r = cong-∙ (λ x → observe p q r (P.longRoute (includeABC x)))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit q)

longU : (p q r : base ≡ base) →
  cong (λ x → observe p q r (P.longRoute x)) loopU ≡ r
longU p q r = cong-∙ (λ x → observe p q r (P.longRoute x))
  (PO.push false) (sym (PO.push true)) ∙ sym (rUnit r)

shortS : (p q r : base ≡ base) →
  cong (λ x → observe p q r (P.shortRoute x)) loopS ≡ p
shortS p q r = sym (cong (λ F → cong (λ x → observe p q r (F x)) loopS) P.pentagon)
  ∙ longS p q r

shortT : (p q r : base ≡ base) →
  cong (λ x → observe p q r (P.shortRoute x)) loopT ≡ q
shortT p q r = sym (cong (λ F → cong (λ x → observe p q r (F x)) loopT) P.pentagon)
  ∙ longT p q r

shortU : (p q r : base ≡ base) →
  cong (λ x → observe p q r (P.shortRoute x)) loopU ≡ r
shortU p q r = sym (cong (λ F → cong (λ x → observe p q r (F x)) loopU) P.pentagon)
  ∙ longU p q r

-- With one detector set to loop and the others to refl, each attachment
-- loop remains nontrivial while the other two have trivial detected action.
noLossS : cong P.longRoute loopS ≡ refl → ⊥
noLossS h = circleLoopNotRefl
  (sym (longS loop refl refl) ∙ cong (cong (observe loop refl refl)) h)

noLossT : cong P.longRoute loopT ≡ refl → ⊥
noLossT h = circleLoopNotRefl
  (sym (longT refl loop refl) ∙ cong (cong (observe refl loop refl)) h)

noLossU : cong P.longRoute loopU ≡ refl → ⊥
noLossU h = circleLoopNotRefl
  (sym (longU refl refl loop) ∙ cong (cong (observe refl refl loop)) h)

liftRetainsActualPentagon : cong fst P.compatiblePentagon ≡ P.pentagon
liftRetainsActualPentagon = P.forgetCompatiblePentagon

liftAgreesWithGenerated : P.compatiblePentagon ≡
  P.Witnesses.Cuts.compare tt P.longPresentation P.shortPresentation
liftAgreesWithGenerated = P.agreesWithGenerated
