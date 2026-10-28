{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyOriginZeroPaths where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import Cubical.Data.Empty as Empty

Zero : ℕ → Type
Zero zero = Unit
Zero (suc n) = ⊥
suc-not-zero : {n : ℕ} → suc n ≡ zero → ⊥
suc-not-zero p = transport (cong Zero (sym p)) tt

module Paths (State Ref : Type) (origin : State → ℕ) (reference : State → Ref) where
  data Step (s t : State) : Type where
    fixed : origin t ≡ origin s → reference t ≡ reference s → Step s t
    advance : origin t ≡ suc (origin s) → Step s t
  data Walk : State → State → Type where
    done : (s : State) → Walk s s
    more : {s t u : State} → Step s t → Walk t u → Walk s u
  zero-start : {s t : State} → Walk s t → origin t ≡ zero → origin s ≡ zero
  zero-start (done s) at-zero = at-zero
  zero-start (more (fixed phase refs) rest) at-zero = sym phase ∙ zero-start rest at-zero
  zero-start (more (advance phase) rest) at-zero =
    Empty.rec (suc-not-zero (sym phase ∙ zero-start rest at-zero))
  zero-references : {s t : State} → Walk s t → origin t ≡ zero → reference s ≡ reference t
  zero-references (done s) at-zero = refl
  zero-references (more (fixed phase refs) rest) at-zero = sym refs ∙ zero-references rest at-zero
  zero-references (more (advance phase) rest) at-zero =
    Empty.rec (suc-not-zero (sym phase ∙ zero-start rest at-zero))
