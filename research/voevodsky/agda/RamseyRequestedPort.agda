{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRequestedPort where
open import Cubical.Foundations.Prelude
open import Cubical.Relation.Nullary using (Dec; yes; no)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Agda.Builtin.String using (String)
import RamseyNativePNOverlapSpan as Span

module Request (Chart Face : Type) (Permit : Chart → Face → Type)
  (packet : (c : Chart) (f : Face) → Permit c f → String)
  (decide : (c : Chart) (f : Face) → Dec (Permit c f)) where
  module S = Span.Spans Chart Face Permit packet
  data Answer (a b : Chart) (f : Face) (p : Permit a f) : Type (ℓ-suc ℓ-zero) where
    accepted : (q : Permit b f) → S.R.Resolve (S.selected-package a b (f , (p , q))) → Answer a b f p
    refused : (Permit b f → ⊥) → Answer a b f p
  run : (a b : Chart) (f : Face) (p : Permit a f) → Answer a b f p
  run a b f p with decide b f
  ... | yes q = accepted q (S.selected-proof a b (f , (p , q)))
  ... | no unavailable = refused unavailable
  isAccepted : {a b : Chart} {f : Face} {p : Permit a f} → Answer a b f p → Bool
  isAccepted (accepted q proof) = true
  isAccepted (refused unavailable) = false
  -- No new span or composition rule is introduced; the accepted branch
  -- uses S.selected-proof, with S.retained-source/target and S.middle-seam.
