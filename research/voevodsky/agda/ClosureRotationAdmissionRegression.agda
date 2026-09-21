{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureRotationAdmissionRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties using (congEquiv)
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
import Cubical.HITs.Pushout.Base as PO
open import ClosureRotationAdmission using (module Admission)
open import ClosureGluingTreeRegression using (circleLoopNotRefl)
import ClosureFiniteGluingNormalizationRegression

-- Nonempty HIGHER attachment boundaries: each span glues circle copies
-- along identity maps. No set or contractibility assumption is made on S¹.
module A = Admission Unit (λ _ → S¹) (λ _ _ → S¹) (λ x → x) (λ x → x)
module R = A.ThreeLeaf tt tt tt (snd (idEquiv S¹)) (snd (idEquiv S¹))
module E = R.E
module P = E.Presentations R.leftTree

nativeCompatibleComparison :
  P.pack R.rightTree R.forward ≡ P.Views.Cuts.canonical R.rightTree
nativeCompatibleComparison = P.agreesWithGenerated R.rightTree R.forward

cycle : E.Route R.leftTree R.leftTree
cycle = E.step R.backward (E.step R.forward (E.stay R.leftTree))

actualTypeCycleIsTrivial : E.typeRoute cycle ≡ refl
actualTypeCycleIsTrivial = E.closedTypeRoute cycle

allResidualValuesReturn : (x : A.N.Realize R.leftTree) → transport (E.typeRoute cycle) x ≡ x
allResidualValuesReturn = E.residualIsIdentity cycle

sourcePoint : A.N.Realize R.leftTree
sourcePoint = PO.inr base

sourceLoop : sourcePoint ≡ sourcePoint
sourceLoop i = PO.inr (loop i)

-- A circle-valued detector respects BOTH attachment path families.
detect : A.N.Realize R.rightTree → S¹
detect (PO.inl x) = x
detect (PO.inr (PO.inl x)) = x
detect (PO.inr (PO.inr x)) = x
detect (PO.inr (PO.push x i)) = x
detect (PO.push x i) = x

nativePreservesLoop : cong (λ x → detect (R.Raw.associate x)) sourceLoop ≡ loop
nativePreservesLoop = refl

sourceLoopNontrivial : sourceLoop ≡ refl → ⊥
sourceLoopNontrivial h = circleLoopNotRefl
  (cong (cong (λ x → detect (R.Raw.associate x))) h)

nativeLoopNontrivial : cong R.Raw.associate sourceLoop ≡ refl → ⊥
nativeLoopNontrivial h = circleLoopNotRefl (cong (cong detect) h)

-- A constant replacement cannot be granted the same admission square.
-- If it could, the generic gate would certify it as an equivalence, and its
-- induced equivalence on loops would incorrectly collapse sourceLoop.
constant : A.N.Realize R.leftTree → A.N.Realize R.rightTree
constant _ = PO.inr (PO.inr base)

noConstantAdmission :
  ((x : A.N.Realize R.leftTree) →
    equivFun (A.N.normalize R.rightTree) (constant x) ≡
    equivFun (A.N.normalize R.leftTree) x) → ⊥
noConstantAdmission square = sourceLoopNontrivial
  (sym (retEq paths sourceLoop) ∙ retEq paths refl)
  where
  edge : E.Admitted R.leftTree R.rightTree
  edge = E.admitted constant square

  paths : (sourcePoint ≡ sourcePoint) ≃ (constant sourcePoint ≡ constant sourcePoint)
  paths = congEquiv (E.actionEquiv edge)

-- The positive admission above uses invertible left legs. The earlier
-- Bool-to-Unit circle-producing spans are NOT covered by that hypothesis.
