{-# OPTIONS --safe --cubical --guardedness #-}
module NestedExchangeNextCell where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv; equivFun)
open import Cubical.Foundations.Isomorphism using (Iso; isoToEquiv)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Sum.Base using (inl)
open import Cubical.Data.Empty.Base using (⊥)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeApplicationExtension as Application
open import NestedWitnessTransport

module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero
module E = Application.Extension ℓ-zero

exchange-iso : Iso Term Term
Iso.fun exchange-iso = exchange
Iso.inv exchange-iso = exchange
Iso.rightInv exchange-iso = exchange-twice
Iso.leftInv exchange-iso = exchange-twice

exchange-equiv = isoToEquiv exchange-iso

step : E.Application
step = record
  { A = Term ; B = λ _ → Term
  ; argument-code = G.atom-node Term
  ; result-code = λ _ → G.atom-node Term
  ; function-code = G.atom-node (Term → Term)
  ; function = exchange ; argument = nested }

source : G.Package
source = E.argument-input step
transported : G.Package
transported = E.result step

-- The existing comparison constructor receives an actual equivalence and
-- its value-preservation proof. Neither is inferred from matching readouts.
comparison-rule : N.Rule
comparison-rule = N.compare-kind , source , transported , exchange-equiv , refl

back : E.Application
back = record
  { A = Term ; B = λ _ → Term
  ; argument-code = N.expression transported
  ; result-code = λ _ → G.atom-node Term
  ; function-code = G.atom-node (Term → Term)
  ; function = exchange ; argument = N.value transported }

returned : G.Package
returned = E.result back

return-rule : N.Rule
return-rule = N.compare-kind , returned , source , idEquiv Term , exchange-twice nested

-- Exactly two admitted inputs: a declared relabeling function and the
-- existing marked source. Neither target nor comparison is seeded.
data Seed : G.Package → Type₁ where
  relabel-function : Seed (E.function-input step)
  source-object : Seed source

module Run = E.Runtime Seed

function-proof : Run.New.Resolve (E.function-input step)
function-proof = Run.New.seed relabel-function
source-proof : Run.New.Resolve source
source-proof = Run.New.seed source-object
transported-proof : Run.New.Resolve transported
transported-proof = Run.execute step function-proof source-proof

next-cell : Run.New.Resolve (N.output comparison-rule)
next-cell = Run.New.apply (inl comparison-rule)
  (λ { (lift true) → source-proof ; (lift false) → transported-proof })

returned-proof : Run.New.Resolve returned
returned-proof = Run.execute back function-proof transported-proof

return-cell : Run.New.Resolve (N.output return-rule)
return-cell = Run.New.apply (inl return-rule)
  (λ { (lift true) → returned-proof ; (lift false) → source-proof })

return-value : N.value returned ≡ N.value source
return-value = exchange-twice nested

-- Identity equivalence cannot substitute for the declared exchange on the
-- first comparison: the marked terms really differ.
no-untransported-identification : N.value source ≡ N.value transported → ⊥
no-untransported-identification = nested-distinct

-- Return output keeps its transported input expression as a retained child.
-- Equality of active values above is not equality/erasure of packages.
return-keeps-intermediate : N.expression returned
  ≡ G.retain-node (N.expression (E.function-input back)) (N.value (E.function-input back))
      (G.retain-node (N.expression transported) (N.value transported) (G.atom-node Term))
return-keeps-intermediate = refl
