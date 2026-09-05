{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CompletionPreservation where

open import Cubical.Foundations.Prelude

record CompletionCone (Base : Type) : Type₁ where
  field
    Completed : Type
    inject : Base → Completed
open CompletionCone public

record CompletionMap
  {Base : Type}
  (source target : CompletionCone Base) : Type where
  field
    map : Completed source → Completed target
    preserves-completion :
      (x : Base) → map (inject source x) ≡ inject target x
open CompletionMap public

identityCompletionMap :
  {Base : Type} (cone : CompletionCone Base) → CompletionMap cone cone
map (identityCompletionMap cone) x = x
preserves-completion (identityCompletionMap cone) x = refl

composeCompletionMap :
  {Base : Type} {a b c : CompletionCone Base} →
  CompletionMap b c → CompletionMap a b → CompletionMap a c
map (composeCompletionMap g f) x = map g (map f x)
preserves-completion (composeCompletionMap g f) x =
  cong (map g) (preserves-completion f x)
  ∙ preserves-completion g x

-- Composition therefore remains inside the completion-preserving maps;
-- an arbitrary function between completed carriers is not an adapter.
