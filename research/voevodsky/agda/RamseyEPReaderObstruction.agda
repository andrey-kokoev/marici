{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyEPReaderObstruction where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)

data Slot : Type where
  s0 s1 s2 s3 s4 : Slot

module Obstruction (A : Type) (zero one : A) (distinct : zero ≡ one → ⊥) where
  Vector = Slot → A
  Context = Vector → A × A
  readerP : Vector → Vector
  readerP x s0 = x s2
  readerP x s1 = x s3
  readerP x s2 = x s0
  readerP x s3 = x s1
  readerP x s4 = x s4
  readerE : Vector → Vector
  readerE x s0 = x s0
  readerE x s1 = x s3
  readerE x s2 = x s4
  readerE x s3 = x s1
  readerE x s4 = x s2
  pn : Vector → Vector
  pn x s0 = x s3
  pn x s1 = x s1
  pn x s2 = x s2
  pn x s3 = x s0
  pn x s4 = x s4
  adapter : Context → Vector → Vector
  adapter u x s0 = x s3
  adapter u x s1 = x s4
  adapter u x s2 = x s2
  adapter u x s3 = fst (u x)
  adapter u x s4 = snd (u x)
  unit1 : Vector
  unit1 s0 = zero
  unit1 s1 = one
  unit1 s2 = zero
  unit1 s3 = zero
  unit1 s4 = zero

  -- Arbitrary context functions are allowed: this is stronger than U,V in U(2).
  no-square : (u v : Context)
    → ((x : Vector) → readerP (adapter u x) ≡ adapter v (readerE x)) → ⊥
  no-square u v square = distinct (cong (λ x → x s0) (square unit1))
  no-pn-square : (u v : Context)
    → ((x : Vector) → pn (readerP (adapter u x)) ≡ pn (adapter v (readerE x))) → ⊥
  no-pn-square u v square = distinct (cong (λ x → x s3) (square unit1))

  -- Even allowing a completely different target adapter cannot repair the
  -- square while keeping its first value the genuinely retained C occurrence.
  no-retaining-target : (u : Context) (target : Vector → Vector)
    → ((x : Vector) → target x s0 ≡ x s3)
    → ((x : Vector) → readerP (adapter u x) ≡ target (readerE x)) → ⊥
  no-retaining-target u target retained square =
    distinct (cong (λ x → x s0) (square unit1) ∙ retained (readerE unit1))

  -- Exact necessary replacement for the third source coefficient, rather
  -- than a vague assertion that some new comparison might work.
  necessary-third : (source target : Vector → Vector)
    → ((x : Vector) → target x s0 ≡ x s3)
    → ((x : Vector) → readerP (source x) ≡ target (readerE x))
    → (x : Vector) → source x s2 ≡ x s1
  necessary-third source target retained square x =
    cong (λ y → y s0) (square x) ∙ retained (readerE x)
