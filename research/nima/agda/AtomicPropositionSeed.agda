{-# OPTIONS --safe --cubical --guardedness #-}
module AtomicPropositionSeed where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; zero)
open import TypedGeneratorLayers using (Layer1; module Histories)

-- Syntax: this constructor declares one atomic proposition name.
-- It does not construct an inhabitant of the proposition it names.
data Object : Type where
  dot : Object

-- Nullary initialization: no incoming state or witness is required.
initial : Object
initial = dot

object-is-dot : (o : Object) → o ≡ dot
object-is-dot dot = refl

record Interpretation : Type₁ where
  field
    Meaning : Object → Type
    proposition : (o : Object) → isProp (Meaning o)

-- The syntax admits an interpretation in which its sole proposition is false.
empty-interpretation : Interpretation
empty-interpretation = record
  { Meaning = λ _ → ⊥
  ; proposition = λ _ () }

no-proof-at-dot : Interpretation.Meaning empty-interpretation dot → ⊥
no-proof-at-dot p = p

-- Naming an atom does not uniformly prove its interpreted proposition.
no-uniform-proof : ((m : Interpretation) → Interpretation.Meaning m dot) → ⊥
no-uniform-proof prove = prove empty-interpretation

-- WG's transition rule remains explicit. Initialization supplies its first
-- state, not its rule, and makes no choice of a transition on the user's behalf.
module Run (Witness : Object → Object → Type)
  (generate : (s : Object) → Σ[ t ∈ Object ] Witness s t) where

  WG : Layer1 ℓ-zero
  WG = record { State = Object ; Witness = Witness ; generate = generate }

  module H = Histories WG

  first-arrow : Witness initial (fst (generate initial))
  first-arrow = snd (generate initial)

  history : (n : ℕ) → H.History initial (H.at n initial)
  history n = H.generated n initial

  zero-history : history zero ≡ H.empty
  zero-history = refl

  -- These endpoints are forced by the singleton state syntax, independently
  -- of the supplied transition rule. This does not instantiate that rule.
  ending-state : (n : ℕ) → H.at n initial ≡ dot
  ending-state n = object-is-dot (H.at n initial)

  cycle1 : H.at 1 initial ≡ dot
  cycle1 = ending-state 1
  cycle2 : H.at 2 initial ≡ dot
  cycle2 = ending-state 2
  cycle3 : H.at 3 initial ≡ dot
  cycle3 = ending-state 3
  cycle4 : H.at 4 initial ≡ dot
  cycle4 = ending-state 4
  cycle5 : H.at 5 initial ≡ dot
  cycle5 = ending-state 5

  five-witnesses : H.length (history 5) ≡ 5
  five-witnesses = H.generated-length 5 initial
