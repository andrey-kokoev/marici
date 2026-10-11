{-# OPTIONS --safe --cubical --guardedness #-}
module InterfaceRecordCompletion where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (idEquiv)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.Int.Base using (ℤ; pos; negsuc; _+_)
open import Cubical.Data.Vec.Base using (Vec; []; _∷_; replicate)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Sum.Base using (inl)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeApplicationExtension as Application

-- Integer numerators with common denominator 12^exponent. This closed
-- coefficient sector represents the fixed averaging law exactly, without
-- introducing a physical clock or energy calibration.
sum : {n : ℕ} → Vec ℤ n → ℤ
sum [] = pos 0
sum (x ∷ xs) = x + sum xs

record Full : Type where
  constructor full
  field
    left right : ℤ
    exterior : Vec ℤ 10
    exponent : ℕ

record View : Type where
  constructor view
  field
    left right exterior-total : ℤ
    exponent : ℕ

observe : Full → View
observe (full a b xs n) = view a b (sum xs) n

step : Full → Full
step (full a b xs n) = full m m (replicate m) (suc n)
  where m = a + (b + sum xs)

advance : View → View
advance (view a b s n) = view m m (sum (replicate {n = 10} m)) (suc n)
  where m = a + (b + s)

commutes : (x : Full) → observe (step x) ≡ advance (observe x)
commutes (full a b xs n) = refl

-- Concrete counterexample to a two-coefficient autonomous observer.
record Coarse : Type where
  constructor coarse
  field first second : ℤ
        exponent : ℕ
forget-exterior : Full → Coarse
forget-exterior (full a b xs n) = coarse a b n
zero-source remote-source : Full
zero-source = full (pos 0) (pos 0) (replicate (pos 0)) 0
remote-source = full (pos 0) (pos 0) (pos 1 ∷ replicate (pos 0)) 0
same-coarse-input : forget-exterior zero-source ≡ forget-exterior remote-source
same-coarse-input = refl
is-zero : ℤ → Bool
is-zero (pos 0) = true
is-zero (pos (suc n)) = false
is-zero (negsuc n) = false
no-coarse-law : (h : Coarse → Coarse)
  → ((x : Full) → forget-exterior (step x) ≡ h (forget-exterior x)) → ⊥
no-coarse-law h law = true≢false
  (cong (λ c → is-zero (Coarse.first c))
    (law zero-source ∙ cong h same-coarse-input ∙ sym (law remote-source)))

-- The operation and observer are explicit admitted functions. This uses the
-- existing application EXTENSION, not a derivation from the frozen rules.
module Native (input : Full) where
  module G = Tables.Core ℓ-zero
  module N = Rules.Native ℓ-zero
  module E = Application.Extension ℓ-zero

  evolve observe-first : E.Application
  evolve = record
    { A = Full ; B = λ _ → Full
    ; argument-code = G.atom-node Full ; result-code = λ _ → G.atom-node Full
    ; function-code = G.atom-node (Full → Full)
    ; function = step ; argument = input }
  observe-first = record
    { A = Full ; B = λ _ → View
    ; argument-code = G.atom-node Full ; result-code = λ _ → G.atom-node View
    ; function-code = G.atom-node (Full → View)
    ; function = observe ; argument = input }

  observe-after update-after : E.Application
  observe-after = record
    { A = Full ; B = λ _ → View
    ; argument-code = N.expression (E.result evolve)
    ; result-code = λ _ → G.atom-node View
    ; function-code = G.atom-node (Full → View)
    ; function = observe ; argument = N.value (E.result evolve) }
  update-after = record
    { A = View ; B = λ _ → View
    ; argument-code = N.expression (E.result observe-first)
    ; result-code = λ _ → G.atom-node View
    ; function-code = G.atom-node (View → View)
    ; function = advance ; argument = N.value (E.result observe-first) }

  data Seed : G.Package → Type₁ where
    initial : Seed (E.argument-input evolve)
    evolution : Seed (E.function-input evolve)
    observation : Seed (E.function-input observe-first)
    local-update : Seed (E.function-input update-after)
  module Run = E.Runtime Seed

  full-next : Run.New.Resolve (E.result evolve)
  full-next = Run.execute evolve (Run.New.seed evolution) (Run.New.seed initial)
  local-now : Run.New.Resolve (E.result observe-first)
  local-now = Run.execute observe-first (Run.New.seed observation) (Run.New.seed initial)
  left-route : Run.New.Resolve (E.result observe-after)
  left-route = Run.execute observe-after (Run.New.seed observation) full-next
  right-route : Run.New.Resolve (E.result update-after)
  right-route = Run.execute update-after (Run.New.seed local-update) local-now

  agreement-rule : N.Rule
  agreement-rule = N.compare-kind , E.result observe-after , E.result update-after , idEquiv View , commutes input
  next-witness : Run.New.Resolve (N.output agreement-rule)
  next-witness = Run.New.apply (inl agreement-rule)
    (λ { (lift true) → left-route ; (lift false) → right-route })

  -- Promote the actual derived comparison and its derivation as the next
  -- retained object; neither its target nor its agreement was a Seed.
  next-package : Run.UpG.Package
  next-package = Run.reify (N.output agreement-rule , next-witness)
  promoted-witness-recovered : snd (Run.UpN.value next-package) ≡ next-witness
  promoted-witness-recovered = refl

  -- Full input and function are retained by the observation, even though its
  -- active View no longer lists the ten individual exterior coefficients.
  observation-keeps-source : N.expression (E.result observe-first)
    ≡ G.retain-node (N.expression (E.function-input observe-first)) (N.value (E.function-input observe-first))
        (G.retain-node (N.expression (E.argument-input observe-first)) input (G.atom-node View))
  observation-keeps-source = refl

module Fixture = Native remote-source
