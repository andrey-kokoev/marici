{-# OPTIONS --safe --cubical --guardedness #-}
module ReSpecializeWitnessSelection where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sum.Base using (inl; inr)
open import Cubical.Data.Unit.Base using (Unit; tt)
import MetaWitnessGenerator as Meta
import WitnessSelectionGenerator as Selection

-- Apply the SAME meta-WG to the already compiled, certified selection WG.
-- The input state now contains native derivations, hence the universe rise.
module M = Meta.Specialize Selection.State Selection.SelectionWitness

selection-domain : M.Domain
selection-domain = record
  { compute = λ s → fst (Selection.select s)
  ; Allowed = λ { (inl q) → Lift {j = ℓ-suc ℓ-zero} Unit
                ; (inr (q , a)) → fst a ≡ Selection.execute q }
  ; LawInput = Selection.Request
  ; request = inl
  ; expected = λ q → inr (q , (Selection.execute q , refl))
  ; law = λ q → refl }

selection-pair : M.Compatible
selection-pair = record
  { domain = selection-domain
  ; base = Selection.select
  ; agrees = λ s → refl
  ; closed = λ { (inl q) ok → refl
               ; (inr (q , a)) ok → ok } }

module Specialized = M.Compiled selection-pair

admitted-request : Specialized.State
admitted-request = inl Selection.request-false , lift tt

specialized-selection :
  fst (Specialized.generator admitted-request) ≡
    (inr (Selection.request-false ,
      (Selection.execute Selection.request-false , refl)) , refl)
specialized-selection = refl

-- The second specialization retains the exact first-layer WG and its domain;
-- it does not assert a new computation law or collapse the input history.
recovered-selection-pair : fst Specialized.compiled ≡ selection-pair
recovered-selection-pair = Specialized.source-recovered

meta-selection :
  fst (M.meta-generate (inl selection-pair)) ≡
    inr (selection-pair , Specialized.domain-WG)
meta-selection = refl
