{-# OPTIONS --safe --cubical --guardedness #-}
module WholePackageSemisimplicial where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sigma.Base using (_×_)

-- Index the coherent face-data construction explicitly by degree. A 0-simplex
-- is an atom; an (n+1)-simplex is its full list of n-dimensional faces,
-- subject to the condition that every pair of faces agrees on intersections.
-- The nontrivial next step is to implement those intersections recursively.
module Candidate {ℓ : Level} (A : Type ℓ) where
  ZeroSimplex : Type ℓ
  ZeroSimplex = A

-- No map is claimed yet: the whole-package generator supplies globular
-- parallel comparisons, while a semisimplicial object needs ordered faces
-- and recursively matching intersections. This file records the exact gap
-- and its first test cases, rather than postulating conversion operations.
