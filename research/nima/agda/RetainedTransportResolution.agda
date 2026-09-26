{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedTransportResolution where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

-- A separate extension: the old Rule and Resolve are not changed.
module Extension (ℓ : Level) where
  open Whole.Universe ℓ
  module Old = Resolution.Generators ℓ

  target : (a : Complete) (R : Code) → El (expression a) ≃ El R → Complete
  target a R e = pack R (equivFun e (value a))

  evidence : (a : Complete) (R : Code) → El (expression a) ≃ El R → Complete
  evidence a R e = comparison-package a (target a R e) e refl

  transported : (a : Complete) (R : Code) → El (expression a) ≃ El R → Complete
  transported a R e = remember (evidence a R e) (target a R e)

  data ResolveT (S : Complete → Type (ℓ-suc ℓ)) : Complete → Type (ℓ-suc ℓ) where
    seedT : {q : Complete} → S q → ResolveT S q
    nativeT : (r : Old.Rule) → ((i : Old.Arity r) → ResolveT S (Old.input r i))
      → ResolveT S (Old.output r)
    transportT : (a : Complete) (R : Code) (e : El (expression a) ≃ El R)
      → ResolveT S a → ResolveT S (transported a R e)

  embed-native : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete}
    → Old.Resolve S q → ResolveT S q
  embed-native (Old.seed s) = seedT s
  embed-native (Old.apply r ds) = nativeT r (λ i → embed-native (ds i))

  -- This certificate admits one leaf and unary transport only: no hidden
  -- intermediate seed, native branching node or opaque route seed is added.
  data TransportOnly {S : Complete → Type (ℓ-suc ℓ)}
    : {q : Complete} → ResolveT S q → Type (ℓ-suc ℓ) where
    one-seed : {q : Complete} (s : S q) → TransportOnly (seedT s)
    one-step : (a : Complete) (R : Code) (e : El (expression a) ≃ El R)
      (d : ResolveT S a) → TransportOnly d → TransportOnly (transportT a R e d)

  comparison-source : Code → Maybe Complete
  comparison-source (comparison A B e) = recover A
  comparison-source _ = nothing

  previous : Complete → Maybe Complete
  previous q with recover (expression q)
  ... | nothing = nothing
  ... | just certificate = comparison-source (expression certificate)

  evidence-retained : (a : Complete) (R : Code) (e : El (expression a) ≃ El R)
    → recover (expression (transported a R e)) ≡ just (evidence a R e)
  evidence-retained a R e = refl

  previous-retained : (a : Complete) (R : Code) (e : El (expression a) ≃ El R)
    → previous (transported a R e) ≡ just a
  previous-retained a R e = refl

  computed-value : (a : Complete) (R : Code) (e : El (expression a) ≃ El R)
    → value (transported a R e) ≡ equivFun e (value a)
  computed-value a R e = refl
