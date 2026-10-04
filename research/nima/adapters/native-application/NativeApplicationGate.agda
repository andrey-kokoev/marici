{-# OPTIONS --safe --cubical --guardedness #-}
module NativeApplicationGate where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
import Cubical.Data.Bool.Properties as B
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Unit.Properties using (isPropUnit)
open import Cubical.Data.Empty.Base using (⊥; rec)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
import GeneratingGrammarMacros as Macros

module Invariant (ℓ : Level) where
  module G = Tables.Core ℓ
  module N = Rules.Native ℓ
  principal-atomic : {A : Type ℓ} → G.Node A → Bool
  principal-atomic (G.table-node (G.retain-header A x B) children) =
    principal-atomic (children (lift true))
  principal-atomic (G.table-node (G.atom-header A) children) = true
  principal-atomic (G.table-node (G.E-header I F) children) = false
  principal-atomic (G.table-node (G.P-header I F) children) = false
  principal-atomic (G.table-node (G.paths-header A x y) children) = false
  principal-atomic (G.table-node (G.maps-header A B) children) = false
  principal-atomic (G.table-node (G.equivalences-header A B) children) = false
  principal-atomic (G.table-node (G.comparison-header A B e) children) = false
  atomic : G.Package → Bool
  atomic q = principal-atomic (N.expression q)

  -- Exhaustive over the actual twelve native rule schemas, not a search bound.
  rule-output-not-atomic : (r : N.Rule) → atomic (N.output r) ≡ false
  rule-output-not-atomic (N.E-kind , p) = refl
  rule-output-not-atomic (N.P-kind , p) = refl
  rule-output-not-atomic (N.compare-kind , p) = refl
  rule-output-not-atomic (N.identity-kind , p) = refl
  rule-output-not-atomic (N.inverse-kind , p) = refl
  rule-output-not-atomic (N.compose-kind , p) = refl
  rule-output-not-atomic (N.higher-kind , p) = refl
  rule-output-not-atomic (N.reflexivity-kind , p) = refl
  rule-output-not-atomic (N.path-lift-kind , p) = refl
  rule-output-not-atomic (N.distribution-kind , p) = refl
  rule-output-not-atomic (N.E-congruence-kind , p) = refl
  rule-output-not-atomic (N.P-congruence-kind , p) = refl

  module Policy (Admit : G.Package → Type (ℓ-suc ℓ)) where
    module Run = Resolution.Full ℓ Admit
    atomic-needs-admission : {q : G.Package} → Run.Resolve q → atomic q ≡ true → Admit q
    atomic-needs-admission (Run.seed a) marker = a
    atomic-needs-admission (Run.apply r ds) marker = rec
      (B.false≢true (sym (rule-output-not-atomic r) ∙ marker))

-- Positive general case already supported by the retained-family interface:
-- specialize a P-kind application by recovering its certified premise.
module CertifiedFamily (ℓ : Level) (Admit : Tables.Core.Package ℓ → Type (ℓ-suc ℓ)) where
  module G = Tables.Core ℓ
  module N = Rules.Native ℓ
  module M = Macros.Retained ℓ Admit
  module Run = Resolution.Full ℓ Admit
  specialize : (I : Type ℓ) (F : I → G.Package)
    → ((i : I) → Run.Resolve (F i)) → (i : I) → Run.Resolve (F i)
  specialize I F ds i = snd (Run.premise (M.family I F , M.family-run I F ds) (lift i))
  specialization-beta : (I : Type ℓ) (F : I → G.Package)
    (ds : (i : I) → Run.Resolve (F i)) (i : I) → specialize I F ds i ≡ ds i
  specialization-beta I F ds i = refl

module I = Invariant ℓ-zero
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero
unit-node : G.Node Unit
unit-node = G.atom-node Unit
bool-node : G.Node Bool
bool-node = G.atom-node Bool
function argument answer : G.Package
function = N.pack (G.maps-node unit-node bool-node) (λ _ → true)
argument = N.pack unit-node tt
answer = N.pack bool-node (N.value function (N.value argument))

-- Only the function and argument are seed constructors. No evaluated answer.
data Seed : G.Package → Type₁ where
  function-seed : Seed function
  argument-seed : Seed argument
module P = I.Policy Seed
module Run = P.Run

-- Avoid raw-value discrimination across univalent package carrier paths:
-- the admitted atomic carrier is propositional; Bool is not.
seed-atomic-prop : {q : G.Package} → Seed q → I.atomic q ≡ true → isProp (N.Ty q)
seed-atomic-prop function-seed marker = rec (B.false≢true marker)
seed-atomic-prop argument-seed marker = isPropUnit
answer-not-admitted : Seed answer → ⊥
answer-not-admitted seed = B.false≢true (seed-atomic-prop seed refl false true)
no-native-atomic-application : Run.Resolve answer → ⊥
no-native-atomic-application d = answer-not-admitted (P.atomic-needs-admission d refl)

-- Host-language computation succeeds; native endpoint derivability is different.
external-beta : N.value answer ≡ true
external-beta = refl
function-run : Run.Resolve function
function-run = Run.seed function-seed
argument-run : Run.Resolve argument
argument-run = Run.seed argument-seed

-- Retaining both inputs does not evade the invariant: peel only retain nodes.
retained-answer : G.Package
retained-answer = N.remember function (N.remember argument answer)
no-native-retained-application : Run.Resolve retained-answer → ⊥
no-native-retained-application d = B.false≢true
  (seed-atomic-prop (P.atomic-needs-admission d refl) refl false true)

-- Positive boundary: native P genuinely retains both admitted operands.
inputs : Bool → G.Package
inputs false = function
inputs true = argument
pair-rule : N.Rule
pair-rule = N.P-kind , Bool , inputs
paired-run : Run.Resolve (N.output pair-rule)
paired-run = Run.apply pair-rule (λ { (lift false) → function-run ; (lift true) → argument-run })
readout : N.Ty (N.output pair-rule) → Bool
readout v = v false (v true)
readout-beta : readout (N.value (N.output pair-rule)) ≡ true
readout-beta = refl
