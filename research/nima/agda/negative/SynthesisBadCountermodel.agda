{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisBadCountermodel where
open import Cubical.Foundations.Prelude
open import GeneratedLowerRefutations
open Models ℓ-zero
-- This algebra satisfies all 32 formerly unresolved cheaper identities,
-- but it cannot have the commutative NAND of a Boolean structure.
bad : table0 f0 f1 ≡ table0 f1 f0
bad = refl
