{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureReferenceNormalFormRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Univalence
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.HITs.Pushout.Base using (cofib)
open import ClosureTypedRealization using (TypedRealization; module AlongEquivalence)
open import ClosureReferenceNormalForm
open import ClosureRealizationHolonomy
import ClosureAllDimensionalCutRegression as Previous

module Old = Previous.Test
module E = Previous.Example

-- Reuse the existing cofiber realization, frames, operation, and routes.
-- This regression supplies no new abstract compatibility assumptions.
module M = Model Old.Cut
  (λ c → Old.M.Input (fst c)) (λ c → Old.M.Output (snd c))
  (cofib E.Model.g) (cofib E.Model.g)
  (λ c → Old.inputFrame (fst c)) (λ c → Old.outputFrame (snd c)) E.Test.Old.F1

independentNormalization : Previous.actualCofiberPresentation ≡
  M.Cuts.canonical Previous.c11
independentNormalization = M.normalize Previous.c11 Previous.actualCofiberPresentation

independentTypedPath :
  M.typed Previous.c11 Previous.actualCofiberPresentation ≡ M.reference
independentTypedPath = M.toReference Previous.c11 Previous.actualCofiberPresentation

clockwiseIsTrivial : M.closedCycle Previous.clockwise Previous.start ≡ refl
clockwiseIsTrivial = M.closedCycleIsTrivial Previous.clockwise Previous.start

counterclockwiseIsTrivial : M.closedCycle Previous.counterclockwise Previous.start ≡ refl
counterclockwiseIsTrivial = M.closedCycleIsTrivial Previous.counterclockwise Previous.start

typedCyclesAgree : M.closedCycle Previous.clockwise Previous.start ≡
  M.closedCycle Previous.counterclockwise Previous.start
typedCyclesAgree = clockwiseIsTrivial ∙ sym counterclockwiseIsTrivial

module FixedValueDoesNotImplyTrivialLoop where
  T : Type
  T = Bool × Bool

  selected probe : T
  selected = false , false
  probe = true , false

  swap : T → T
  swap (x , y) = y , x

  swapIso : Iso T T
  swapIso = iso swap swap (λ _ → refl) (λ _ → refl)

  swapEquiv : T ≃ T
  swapEquiv = isoToEquiv swapIso

  fixesSelected : equivFun swapEquiv selected ≡ selected
  fixesSelected = refl

  module Travel = AlongEquivalence swapEquiv
    {a = selected} {b = selected} fixesSelected

  typedLoop : Path TypedRealization (T , selected) (T , selected)
  typedLoop = Travel.together

  residualMatchesSwap : (x : T) → residualAction typedLoop x ≡ swap x
  residualMatchesSwap x = uaβ swapEquiv x

  valueReturns : residualAction typedLoop selected ≡ selected
  valueReturns = residualFixesValue typedLoop

  -- The selected value returns, but the loop is NOT homotopic to doing
  -- nothing: it swaps another pair. A null-homotopy would force false=true.
  notTrivial : typedLoop ≡ refl → ⊥
  notTrivial h = false≢true (cong fst
    (sym (uaβ swapEquiv probe)
      ∙ cong (λ p → residualAction p probe) h
      ∙ transportRefl probe))
