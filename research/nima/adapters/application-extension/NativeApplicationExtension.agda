{-# OPTIONS --safe --cubical --guardedness #-}
module NativeApplicationExtension where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
import IndexedResolutionTransport as Transport

-- An explicit extension, NOT an implementation inside the frozen twelve rules.
module Extension (ℓ : Level) where
  module G = Tables.Core ℓ
  module N = Rules.Native ℓ
  record Application : Type (ℓ-suc ℓ) where
    field
      A : Type ℓ
      B : A → Type ℓ
      argument-code : G.Node A
      result-code : (a : A) → G.Node (B a)
      function-code : G.Node ((a : A) → B a)
      function : (a : A) → B a
      argument : A
  open Application
  function-input : Application → G.Package
  function-input p = N.pack (function-code p) (function p)
  argument-input : Application → G.Package
  argument-input p = N.pack (argument-code p) (argument p)
  result : Application → G.Package
  result p = N.remember (function-input p) (N.remember (argument-input p)
    (N.pack (result-code p (argument p)) (function p (argument p))))
  beta : (p : Application) → N.value (result p) ≡ function p (argument p)
  beta p = refl

  Rule : Type (ℓ-suc ℓ)
  Rule = N.Rule ⊎ Application
  Arity : Rule → Type (ℓ-suc ℓ)
  Arity (inl r) = N.Arity r
  Arity (inr p) = Lift Bool
  input : (r : Rule) → Arity r → G.Package
  input (inl r) i = N.input r i
  input (inr p) (lift false) = function-input p
  input (inr p) (lift true) = argument-input p
  output : Rule → G.Package
  output (inl r) = N.output r
  output (inr p) = result p
  old-output-unchanged : (r : N.Rule) → output (inl r) ≡ N.output r
  old-output-unchanged r = refl

  beta-package : Application → G.Package
  beta-package p = N.path-package (N.Ty (result p) , N.expression (result p))
    (N.value (result p)) (function p (argument p)) (beta p)
  fields : Application → Lift {j = ℓ} Bool → G.Package
  fields p (lift false) = result p
  fields p (lift true) = beta-package p
  combined : Application → G.Package
  combined p = N.Pi-package (Lift Bool) (fields p)

  module Runtime (Admit : G.Package → Type (ℓ-suc ℓ)) where
    module Old = Resolution.Full ℓ Admit
    module New = Transport.Theory G.Package Rule Arity input output Admit
    embed : {q : G.Package} → Old.Resolve q → New.Resolve q
    embed (Old.seed a) = New.seed a
    embed (Old.apply r ds) = New.apply (inl r) (λ i → embed (ds i))

    execute : (p : Application) → New.Resolve (function-input p)
      → New.Resolve (argument-input p) → New.Resolve (result p)
    execute p df dx = New.apply (inr p) (λ { (lift false) → df ; (lift true) → dx })

    -- No beta witness seed: the existing reflexivity rule builds the filler,
    -- because the dependent application beta equation is definitional.
    coherencer : (p : Application) → New.Resolve (result p) → New.Resolve (beta-package p)
    coherencer p d = New.apply (inl (N.reflexivity-kind , result p)) (λ _ → d)
    assemble : (p : Application) → New.Resolve (result p) → New.Resolve (combined p)
    assemble p d = New.apply (inl (N.P-kind , Lift Bool , fields p))
      (λ { (lift (lift false)) → d ; (lift (lift true)) → coherencer p d })

    module UpG = Tables.Core (ℓ-suc ℓ)
    module UpN = Rules.Native (ℓ-suc ℓ)
    reify : New.Closed → UpG.Package
    reify d = UpN.pack (UpG.atom-node New.Closed) d
    reify-recovery : (d : New.Closed) → UpN.value (reify d) ≡ d
    reify-recovery d = refl
    complete-step : (p : Application) → New.Resolve (result p) → UpG.Package
    complete-step p d = reify (combined p , assemble p d)
    recover-combined : (p : Application) (d : New.Resolve (result p))
      → fst (UpN.value (complete-step p d)) ≡ combined p
    recover-combined p d = refl
    recover-history : (p : Application) (d : New.Resolve (result p))
      → snd (UpN.value (complete-step p d)) ≡ assemble p d
    recover-history p d = refl
