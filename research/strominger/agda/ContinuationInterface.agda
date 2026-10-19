{-# OPTIONS --safe --cubical --guardedness #-}
module ContinuationInterface where

open import Cubical.Foundations.Prelude
open import Cubical.Data.List.Base using (List; []; _∷_)

-- Command and observation domains are part of the declared task, not inferred
-- from equal dimensions or equal current scalar observations.
module Task (Command Observation : Type) where
  record System : Type₁ where
    field
      State : Type
      step : State → Command → State
      observe : State → Observation
  open System

  record Map (A B : System) : Type where
    field
      on-state : State A → State B
      step-law : (s : State A) (c : Command)
        → on-state (step A s c) ≡ step B (on-state s) c
      observation-law : (s : State A) → observe B (on-state s) ≡ observe A s
  open Map

  identity : (A : System) → Map A A
  on-state (identity A) s = s
  step-law (identity A) s c = refl
  observation-law (identity A) s = refl

  compose : {A B C : System} → Map A B → Map B C → Map A C
  on-state (compose f g) s = on-state g (on-state f s)
  step-law (compose f g) s c = cong (on-state g) (step-law f s c)
    ∙ step-law g (on-state f s) c
  observation-law (compose f g) s = observation-law g (on-state f s)
    ∙ observation-law f s

  run : (A : System) → List Command → State A → State A
  run A [] s = s
  run A (c ∷ cs) s = run A cs (step A s c)

  map-run : {A B : System} (f : Map A B) (cs : List Command) (s : State A)
    → on-state f (run A cs s) ≡ run B cs (on-state f s)
  map-run f [] s = refl
  map-run {B = B} f (c ∷ cs) s = map-run f cs _
    ∙ cong (run B cs) (step-law f s c)

  preserves-continuations : {A B : System} (f : Map A B)
    (cs : List Command) (s : State A)
    → observe A (run A cs s) ≡ observe B (run B cs (on-state f s))
  preserves-continuations {A} {B} f cs s =
    sym (observation-law f (run A cs s)) ∙ cong (observe B) (map-run f cs s)

  -- Reflection/full-source recovery would require additional inverse data;
  -- it is deliberately NOT a field inferred from a forward task map.
