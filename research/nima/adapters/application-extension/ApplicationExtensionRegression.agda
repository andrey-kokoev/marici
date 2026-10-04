{-# OPTIONS --safe --cubical --guardedness #-}
module ApplicationExtensionRegression where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import NativeApplicationGate as Gate
open import NativeApplicationExtension

module E = Extension ℓ-zero
module R = E.Runtime Gate.Seed
application : E.Application
application = record
  { A = Unit ; B = λ _ → Bool
  ; argument-code = Gate.unit-node ; result-code = λ _ → Gate.bool-node
  ; function-code = Gate.N.expression Gate.function
  ; function = Gate.N.value Gate.function ; argument = tt }
executed : R.New.Resolve Gate.retained-answer
executed = R.execute application (R.embed Gate.function-run) (R.embed Gate.argument-run)
not-an-old-macro : Gate.Run.Resolve Gate.retained-answer → ⊥
not-an-old-macro = Gate.no-native-retained-application
constructed-coherencer : R.New.Resolve (E.beta-package application)
constructed-coherencer = R.coherencer application executed
combined-run : R.New.Resolve (E.combined application)
combined-run = R.assemble application executed
all-as-constructor : R.UpG.Package
all-as-constructor = R.complete-step application executed
history-recovered : snd (R.UpN.value all-as-constructor) ≡ combined-run
history-recovered = refl
computed : Gate.N.value (E.result application) ≡ true
computed = refl

-- A genuinely dependent codomain changes between Unit and Bool.
module Dependent where
  module G = E.G
  module N = E.N
  B : Bool → Type
  B false = Unit
  B true = Bool
  codes : (b : Bool) → G.Node (B b)
  codes false = Gate.unit-node
  codes true = Gate.bool-node
  f : (b : Bool) → B b
  f false = tt
  f true = true
  function : G.Package
  function = N.pack (G.P-node Bool codes) f
  argument : (b : Bool) → G.Package
  argument b = N.pack Gate.bool-node b
  data Seed : G.Package → Type₁ where
    function-seed : Seed function
    argument-seed : (b : Bool) → Seed (argument b)
  module Run = E.Runtime Seed
  step : (b : Bool) → E.Application
  step b = record
    { A = Bool ; B = B ; argument-code = Gate.bool-node ; result-code = codes
    ; function-code = G.P-node Bool codes ; function = f ; argument = b }
  derive : (b : Bool) → Run.New.Resolve (E.result (step b))
  derive b = Run.execute (step b) (Run.New.seed function-seed) (Run.New.seed (argument-seed b))
  beta : (b : Bool) → N.value (E.result (step b)) ≡ f b
  beta b = refl
