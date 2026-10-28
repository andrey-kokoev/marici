{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyCovariantEPReaderExamples where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Nat.Base using (ℕ)
open import RamseyCovariantEPReader
module C = Natural Bool
all : (n : ℕ) (x : C.Vector) → C.pn (C.Psteps n (C.body (λ y → y) x)) ≡ C.pn (C.body (λ y → y) (C.Esteps n x))
all n x = C.all-reader-PN n (λ y → y) x
