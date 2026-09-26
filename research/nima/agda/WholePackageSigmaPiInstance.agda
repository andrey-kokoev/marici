{-# OPTIONS --safe --cubical --guardedness #-}
module WholePackageSigmaPiInstance where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Unit.Base using (Unit; tt)
import DependentSigmaPiCoherence as Chains
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

module Concrete {ℓ : Level}
  (I : Type ℓ) (J : I → Type ℓ)
  (K : (i : I) → J i → Type ℓ)
  (L : (i : I) (j : J i) → K i j → Type ℓ)
  (B : (i : I) (j : J i) (k : K i j) → L i j k → Type ℓ) where

  module C = Chains.Construction I J K L B
  module R = C.Retained
  open Whole.Universe ℓ
  module G = Resolution.Generators ℓ

  source : (x : C.X) → Complete
  source x = pack (atom R.SourceRecord) (C.canonicalRecord x)

  target : (x : C.X) → Complete
  target x = pack (atom R.TargetRecord) (C.transportedRecord x)

  package-comparison : (x : C.X) → Complete
  package-comparison x = comparison-package (source x) (target x) R.recordLift refl

  Seed : (x : C.X) → Complete → Type (ℓ-suc ℓ)
  Seed x q = (q ≡ source x) ⊎ (q ≡ target x)
    where open import Cubical.Data.Sum.Base using (_⊎_)

  comparison-history : (x : C.X) → G.Resolve (Seed x) (package-comparison x)
  comparison-history x = G.apply (G.compare-rule (source x) (target x) R.recordLift refl)
    (λ { (lift true) → G.seed (inl refl) ; (lift false) → G.seed (inr refl) })
    where open import Cubical.Data.Sum.Base using (inl; inr)

  -- Both a cube-like complete trace and its full derivation become input.
  next-Q : (x : C.X) → Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q x = G.reify-history (comparison-history x)

  history-is-still-present : (x : C.X)
    → snd (Whole.Universe.value (next-Q x)) ≡ comparison-history x
  history-is-still-present x = refl

  next-Pi : (x : C.X) → Whole.Universe.Complete (ℓ-suc (ℓ-suc ℓ))
  next-Pi x = Whole.Pi-whole (Lift {j = ℓ-suc ℓ} Unit) (λ _ → next-Q x)

  next-E : (x : C.X) → Whole.Universe.Complete (ℓ-suc (ℓ-suc ℓ))
  next-E x = Whole.E-whole (Lift {j = ℓ-suc ℓ} Unit) (λ _ → next-Q x) (lift tt)

  Pi-retains-Q : (x : C.X)
    → Whole.Universe.value (next-Pi x) (lift (lift tt)) ≡ next-Q x
  Pi-retains-Q x = refl

  E-retains-Q : (x : C.X)
    → snd (Whole.Universe.value (next-E x)) ≡ next-Q x
  E-retains-Q x = refl

  -- Actual higher boundaries of complete packages, at arbitrary inputs.
  whole-comparison : (a b : Complete) → a ≡ b
                   → Whole.Universe.Complete (ℓ-suc ℓ)
  whole-comparison = Whole.whole-path

  whole-higher-comparison : (a b : Complete) (p q : a ≡ b) → p ≡ q
                         → Whole.Universe.Complete (ℓ-suc ℓ)
  whole-higher-comparison = Whole.whole-higher
