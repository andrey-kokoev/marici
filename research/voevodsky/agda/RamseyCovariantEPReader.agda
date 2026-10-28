{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyCovariantEPReader where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import RamseyEPReaderObstruction using (Slot; s0; s1; s2; s3; s4)

module Natural (A : Type) where
  Vector = Slot → A
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
  -- Outside reference interpretation is explicit, not an occurrence identity.
  body : (A → A) → Vector → Vector
  body context x s0 = x s3
  body context x s1 = x s4
  body context x s2 = x s1
  body context x s3 = x s2
  body context x s4 = context (x s0)
  square : (context : A → A) (x : Vector)
    → readerP (body context x) ≡ body context (readerE x)
  square context x = funExt (λ { s0 → refl ; s1 → refl ; s2 → refl ; s3 → refl ; s4 → refl })
  Psteps Esteps : ℕ → Vector → Vector
  Psteps zero x = x
  Psteps (suc n) x = readerP (Psteps n x)
  Esteps zero x = x
  Esteps (suc n) x = readerE (Esteps n x)
  all-readers : (n : ℕ) (context : A → A) (x : Vector)
    → Psteps n (body context x) ≡ body context (Esteps n x)
  all-readers zero context x = refl
  all-readers (suc n) context x =
    cong readerP (all-readers n context x) ∙ square context (Esteps n x)
  all-reader-PN : (n : ℕ) (context : A → A) (x : Vector)
    → pn (Psteps n (body context x)) ≡ pn (body context (Esteps n x))
  all-reader-PN n context x = cong pn (all-readers n context x)
