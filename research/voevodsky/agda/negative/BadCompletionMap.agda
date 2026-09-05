{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module BadCompletionMap where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat
open import CompletionPreservation

natCone : CompletionCone ℕ
Completed natCone = ℕ
inject natCone n = n

-- Deliberate failure: successor does not preserve the completion injection.
badMap : CompletionMap natCone natCone
map badMap n = suc n
preserves-completion badMap n i = suc n
