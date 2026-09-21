{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureBooleanArityCofiberBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (false; true)
open import Cubical.HITs.Pushout.Base using (cofib)
open import ClosureCanonicalRejoin using (module Rejoin)
open import ClosureFourPresentations using (module Presentations)
open import ClosureBooleanArity using (module Arity)

module Bridge {A B C A′ B′ C′ : Type}
  (f : A → B) (g : B → C) (f′ : A′ → B′) (g′ : B′ → C′)
  (u : A → A′) (v : B → B′) (w : C → C′)
  (Hf : (a : A) → v (f a) ≡ f′ (u a))
  (Hg : (b : B) → w (g b) ≡ g′ (v b))
  (I J : Type) (Ai : I → Type) (Bj : J → Type)
  -- These are real additional realization data, NOT supplied by the flags.
  (inputFrame : (Σ I Ai) ≃ Rejoin.Quotient f g)
  (outputFrame : Rejoin.Quotient f′ g′ ≃ ((j : J) → Bj j)) where

  module Old = Presentations f g f′ g′ u v w Hf Hg
  module M = Arity (cofib g) (cofib g′) I J Ai Bj

  inputAssembly : M.Input true ≃ cofib g
  inputAssembly = compEquiv inputFrame Old.S.rejoinEquiv

  outputObservation : cofib g′ ≃ M.Output true
  outputObservation = compEquiv
    (isoToEquiv (invIso Old.T.rejoinIso)) outputFrame

  module Square = M.Reversible inputAssembly outputObservation

  baseOperation : M.F false false
  baseOperation _ _ = Old.F1

  generatedOperation : M.F true true
  generatedOperation = Square.inputIndex true (Square.outputIndex false baseOperation)

  -- Independently constructed ladder map, merely expressed in the frames.
  independentOperation : M.F true true
  independentOperation i j x =
    equivFun outputFrame (Old.F4 (equivFun inputFrame (i , x))) j

  operationComparison : independentOperation ≡ generatedOperation
  operationComparison = funExt λ i → funExt λ j → funExt λ x →
    cong (λ z → equivFun outputFrame z j)
      (Old.F4-as-transport (equivFun inputFrame (i , x)))

  roundTrip : Square.cycle baseOperation ≡ baseOperation
  roundTrip = Square.cycleLaw baseOperation

-- The input frame is a SUM frame, unlike the earlier joint-input product
-- example. No claim that arbitrary analytical arities admit these frames is
-- made; the regression supplies an actual non-singleton cofiber instance.
