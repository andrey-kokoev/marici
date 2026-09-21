{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureAllDimensionalCutRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.HITs.Pushout.Base using (cofib)
open import Cubical.HITs.S1.Base using (S¹; loop)
open import ClosureAllDimensionalCutCoherence
open import ClosureArityCutCoherence
import ClosureBooleanArityRegression as Previous

module Example = Previous.CofiberExample
module Test = ArityCuts (cofib Example.Model.g) (cofib Example.Model.g)
  Bool Bool (λ _ → Bool) (λ _ → Bool)
  Example.Test.inputAssembly Example.Test.outputObservation Example.Test.Old.F1

c00 c01 c10 c11 : Test.Cut
c00 = false , false
c01 = false , true
c10 = true , false
c11 = true , true

-- Admit the independently constructed cofiber operation using the equality
-- already checked against the generated indexed operation, not by assumption.
actualCofiberPresentation : Test.Cuts.Compatible c11
actualCofiberPresentation = Test.attach c11 Example.Test.independentOperation
  Example.Test.operationComparison

clockwise counterclockwise : Test.Cuts.Route c00 c00
clockwise = Test.Cuts.step c00 (Test.Cuts.step c10
  (Test.Cuts.step c11 (Test.Cuts.step c01 (Test.Cuts.stay c00))))
counterclockwise = Test.Cuts.step c00 (Test.Cuts.step c01
  (Test.Cuts.step c11 (Test.Cuts.step c10 (Test.Cuts.stay c00))))

start : Test.Cuts.Compatible c00
start = Test.at c00

short long : Test.Cuts.run clockwise start ≡ start
short = Test.Cuts.cycleLaw clockwise start
long = Test.Cuts.routeComparison clockwise counterclockwise start
  ∙ Test.Cuts.cycleLaw counterclockwise start

comparison : long ≡ short
comparison = Test.Cuts.routeComparisonCoherence clockwise (Test.Cuts.stay c00)
  start long short

reverseComparison : short ≡ long
reverseComparison = Test.Cuts.routeComparisonCoherence clockwise (Test.Cuts.stay c00)
  start short long

-- A third-dimensional comparison of separately assembled higher witnesses.
thirdComparison : comparison ≡ sym reverseComparison
thirdComparison = Test.Cuts.Higher.fillCell c00 3
  (((tt , (Test.Cuts.run clockwise start , start)) , (long , short)) ,
    (comparison , sym reverseComparison))

-- This statement quantifies over ALL finite levels, not only levels 0..3.
allFiniteLevels : (n : ℕ) (b : Test.Cuts.Higher.Boundary c11 n) →
  isContr (Test.Cuts.Higher.Cell c11 n b)
allFiniteLevels = Test.Cuts.Higher.allCellsContractible c11

module CircleRetained where
  module C = FramedCuts Bool (λ _ → S¹) (λ _ → S¹) S¹ S¹
    (λ _ → idEquiv S¹) (λ _ → idEquiv S¹) (idfun S¹)

  circleStillThere : (i : I) → fst (C.canonical false) (loop i) ≡ loop i
  circleStillThere i = refl

module IndependentEquivalencesDoNotSuffice where
  -- An independently chosen invertible transition can have nontrivial
  -- holonomy: the Bool flip does not give an identity loop. It cannot be
  -- admitted as the identity operation with these fixed common frames.
  flipIso : Iso Bool Bool
  flipIso = iso not not (λ { false → refl ; true → refl })
    (λ { false → refl ; true → refl })

  flipEquiv : Bool ≃ Bool
  flipEquiv = isoToEquiv flipIso

  noRawCycleLaw : ((b : Bool) → equivFun flipEquiv b ≡ b) → ⊥
  noRawCycleLaw close = true≢false (close false)

  module C = FramedCuts Unit (λ _ → Bool) (λ _ → Bool) Bool Bool
    (λ _ → idEquiv Bool) (λ _ → idEquiv Bool) (idfun Bool)

  noCompatibleFlip : (C.post tt not ≡ C.target tt) → ⊥
  noCompatibleFlip p = true≢false (cong (λ F → F false) p)
