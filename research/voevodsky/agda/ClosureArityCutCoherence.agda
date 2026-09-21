{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureArityCutCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Unit
open import Cubical.Data.Bool using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_)
open import ClosureBooleanArity using (module Arity)
open import ClosureAllDimensionalCutCoherence using (module FramedCuts)

-- Instantiate the general finite-route/all-globular-dimensions theorem on
-- the user's four indexing cuts, retaining the SUM-input interpretation.
module ArityCuts (A B I J : Type) (Ai : I → Type) (Bj : J → Type)
  (inputEquiv : (Σ I Ai) ≃ A)
  (outputEquiv : B ≃ ((j : J) → Bj j)) (baseOperation : A → B) where
  module M = Arity A B I J Ai Bj

  Cut : Type
  Cut = Bool × Bool

  singletonInputIso : Iso (M.Input false) A
  Iso.fun singletonInputIso z = snd z
  Iso.inv singletonInputIso a = tt , a
  Iso.rightInv singletonInputIso a = refl
  Iso.leftInv singletonInputIso z = refl

  singletonOutputIso : Iso (M.Output false) B
  Iso.fun singletonOutputIso f = f tt
  Iso.inv singletonOutputIso b _ = b
  Iso.rightInv singletonOutputIso b = refl
  Iso.leftInv singletonOutputIso f = refl

  inputFrame : (s : Bool) → M.Input s ≃ A
  inputFrame false = isoToEquiv singletonInputIso
  inputFrame true = inputEquiv

  outputFrame : (t : Bool) → M.Output t ≃ B
  outputFrame false = isoToEquiv singletonOutputIso
  outputFrame true = invEquiv outputEquiv

  module Cuts = FramedCuts Cut
    (λ c → M.Input (fst c)) (λ c → M.Output (snd c)) A B
    (λ c → inputFrame (fst c)) (λ c → outputFrame (snd c)) baseOperation

  operation : (s t : Bool) → M.F s t
  operation false false _ _ a = baseOperation a
  operation false true _ j a = equivFun outputEquiv (baseOperation a) j
  operation true false i _ a = baseOperation (equivFun inputEquiv (i , a))
  operation true true i j a =
    equivFun outputEquiv (baseOperation (equivFun inputEquiv (i , a))) j

  -- The four previously discussed operations, now carrying compatible-square
  -- witnesses in the common-operation fiber. This is not an arbitrary point
  -- in an unrelated contractible type.
  at : (c : Cut) → Cuts.Compatible c
  fst (at (s , t)) = M.assemble s t (operation s t)
  snd (at (false , false)) = refl
  snd (at (true , false)) = refl
  snd (at (false , true)) = funExt λ x → retEq outputEquiv (baseOperation (snd x))
  snd (at (true , true)) = funExt λ x →
    retEq outputEquiv (baseOperation (equivFun inputEquiv x))

  -- Admit an independently constructed operation only via a PROVED equality
  -- to this operation. The cofiber regression supplies the previous theorem.
  attach : (c : Cut) (F : M.F (fst c) (snd c)) →
    F ≡ operation (fst c) (snd c) → Cuts.Compatible c
  fst (attach (s , t) F p) = M.assemble s t F
  snd (attach (s , t) F p) =
    cong (λ G → Cuts.post (s , t) (M.assemble s t G)) p ∙ snd (at (s , t))

  routeAgreement : {i j : Cut} (r : Cuts.Route i j) →
    Cuts.run r (at i) ≡ at j
  routeAgreement {j = j} r = Cuts.compare j _ _

-- This does not identify the new comparison paths with all previously chosen
-- pentagon or ladder-composition witnesses. Such an identification requires
-- their lifts, including square coherence, into Cuts.Compatible.
