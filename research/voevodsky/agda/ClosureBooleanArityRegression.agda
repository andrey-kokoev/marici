{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureBooleanArityRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (idfun)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Bool using (Bool; false; true; not)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.HITs.S1.Base using (S¹; base; loop)
open import ClosureBooleanArity
open import ClosureBooleanArityCofiberBridge
open import ClosureProductBoundary using (module PointedModel)

module CofiberExample where
  X : Type
  X = Bool × Bool

  module Model = PointedModel X (false , false)

  swap : X → X
  swap (b , c) = c , b

  toFamily : X → Bool → Bool
  toFamily (b , c) false = b
  toFamily (b , c) true = c

  fromFamily : (Bool → Bool) → X
  fromFamily p = p false , p true

  familyIso : Iso X (Bool → Bool)
  familyIso = iso toFamily fromFamily
    (λ p → funExt λ { false → refl ; true → refl }) (λ x → refl)

  -- Both indices are Bool. Input alternatives are a sum of two Bool types;
  -- outputs are a product of two Bool types. No singleton-index padding.
  inputFrame : (Σ[ i ∈ Bool ] Bool) ≃ Model.R.Quotient
  inputFrame = invEquiv Model.presentation

  outputFrame : Model.R.Quotient ≃ (Bool → Bool)
  outputFrame = compEquiv Model.presentation (isoToEquiv familyIso)

  module Test = Bridge Model.f Model.g Model.f Model.g
    not (idfun Unit) swap (λ _ → refl) (λ _ → refl)
    Bool Bool (λ _ → Bool) (λ _ → Bool) inputFrame outputFrame

  agreesWithExistingCofiberMap : Test.independentOperation ≡ Test.generatedOperation
  agreesWithExistingCofiberMap = Test.operationComparison

  fourCornerCycle : Test.Square.cycle Test.baseOperation ≡ Test.baseOperation
  fourCornerCycle = Test.roundTrip

module HigherPathExample where
  module M = Arity S¹ S¹ Bool Bool (λ _ → S¹) (λ _ → S¹)

  separateFunctions : M.F true true
  separateFunctions false false x = x
  separateFunctions false true x = base
  separateFunctions true false x = base
  separateFunctions true true x = x

  -- Assembly retains the input tag; it neither collects both input values
  -- nor discards the path structure within the selected input component.
  retainsLoop : (i : I) →
    M.assemble true true separateFunctions (true , loop i) true ≡ loop i
  retainsLoop i = refl

  otherOutput : (i : I) →
    M.assemble true true separateFunctions (true , loop i) false ≡ base
  otherOutput i = refl

  wholeRoundTrip : M.disassemble true true
    (M.assemble true true separateFunctions) ≡ separateFunctions
  wholeRoundTrip = Iso.leftInv (M.sumProductIso true true) separateFunctions

module NoAutomaticCycle where
  -- Nonempty index sets do NOT make arbitrary corners equivalent: the
  -- unindexed target is empty, while every indexed output is Unit.
  module M = Arity Unit ⊥ Bool Bool (λ _ → Unit) (λ _ → Unit)

  indexedOperation : M.F false true
  indexedOperation _ _ _ = tt

  noOutputReverse : (M.F false true → M.F false false) → ⊥
  noOutputReverse reverse = reverse indexedOperation tt tt tt

  noCornerEquivalence : M.F false false ≃ M.F false true → ⊥
  noCornerEquivalence e = noOutputReverse (invEq e)
