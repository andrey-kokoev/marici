{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessHistoryFamily where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Nat.Properties using (snotz)
open import Cubical.Data.Empty.Base using (⊥)
import MetaWitnessGenerator as M
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
import NativeApplicationGate as Gate
import GeneratingGrammarMacros as Macros
import NativeApplicationExtension as Application

module C = M.BooleanSpecialized
module H = C.H
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

start : Bool → C.State
start b = b , true

-- The history, not just its composite readout, retains both original
-- witnessed transitions and their intermediate admitted state.
two-steps : (b : Bool) → H.History (start b) (H.at 2 (start b))
two-steps b = H.generated 2 (start b)

two-steps-length : (b : Bool) → H.length (two-steps b) ≡ 2
two-steps-length b = H.generated-length 2 (start b)

-- A dependent Pi-package indexed by initial states contains the complete
-- pointwise history as a value; the index survives in each component code.
component : Bool → G.Package
component b = N.pack (G.atom-node (H.History (start b) (H.at 2 (start b))))
  (two-steps b)

history-family : G.Package
history-family = N.Pi-package Bool component

history-readback : (b : Bool) → N.value history-family b ≡ two-steps b
history-readback b = refl

-- The two-step Boolean loop returns to its starting Boolean coordinate.
-- This equality does NOT equate the nonempty history with an empty one.
return-value : (b : Bool) → fst (H.at 2 (start b)) ≡ b
return-value false = refl
return-value true = refl

return-admission : (b : Bool) → snd (H.at 2 (start b)) ≡ true
return-admission false = refl
return-admission true = refl

nonempty-return : two-steps false ≡ H.empty → ⊥
nonempty-return p = snotz (cong H.length p)

-- An admitted whole Pi-family is not an old-rule derivation of a pointwise
-- atom. The principal-node invariant is insensitive to package equivalence.
module Inv = Gate.Invariant ℓ-zero
data FamilySeed : G.Package → Type (ℓ-suc ℓ-zero) where
  family-seed : FamilySeed history-family
module SeedPolicy = Inv.Policy FamilySeed
family-seed-nonatomic : {q : G.Package} → FamilySeed q → Inv.atomic q ≡ false
family-seed-nonatomic family-seed = refl
no-component-admission : FamilySeed (component false) → ⊥
no-component-admission seed = true≢false (family-seed-nonatomic seed)
no-old-component-from-family-seed : SeedPolicy.Run.Resolve (component false) → ⊥
no-old-component-from-family-seed d =
  no-component-admission (SeedPolicy.atomic-needs-admission d refl)

-- Conversely, if the two pointwise derivations are separately supplied,
-- P-kind can assemble the family and preserve exact premise provenance.
module CertifiedFamily (Admit : G.Package → Type (ℓ-suc ℓ-zero)) where
  module Old = Macros.Retained ℓ-zero Admit
  module WithPremises (ds : (b : Bool) → Old.Run.Resolve (component b)) where
    assembled : Old.Run.Resolve history-family
    assembled = Old.family-run Bool component ds
    selected-premise : (b : Bool)
      → Old.Run.premise (history-family , assembled) (lift b)
        ≡ (component b , ds b)
    selected-premise b = Old.family-premise Bool component ds b

-- The extended native application rule consumes a *certified* family package
-- and a certified index; it yields a retained evaluated history, with beta.
module HistoryApplication where
  module E = Application.Extension ℓ-zero
  argument : G.Package
  argument = N.pack (G.atom-node Bool) false
  apply-history : E.Application
  apply-history = record
    { A = Bool ; B = λ b → H.History (start b) (H.at 2 (start b))
    ; argument-code = G.atom-node Bool
    ; result-code = λ b → G.atom-node (H.History (start b) (H.at 2 (start b)))
    ; function-code = G.P-node Bool (λ b → N.retained (component b))
    ; function = two-steps ; argument = false }
  function-is-family : E.function-input apply-history ≡ history-family
  function-is-family = refl
  data Seed : G.Package → Type (ℓ-suc ℓ-zero) where
    certified-family : Seed history-family
    certified-index : Seed argument
  module Run = E.Runtime Seed
  function-proof : Run.New.Resolve (E.function-input apply-history)
  function-proof = Run.New.seed certified-family
  index-proof : Run.New.Resolve (E.argument-input apply-history)
  index-proof = Run.New.seed certified-index
  evaluated-history : Run.New.Resolve (E.result apply-history)
  evaluated-history = Run.execute apply-history function-proof index-proof
  beta-proof : Run.New.Resolve (E.beta-package apply-history)
  beta-proof = Run.coherencer apply-history evaluated-history
  readback : N.value (E.result apply-history) ≡ two-steps false
  readback = refl
