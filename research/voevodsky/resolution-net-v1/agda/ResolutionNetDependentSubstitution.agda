{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetDependentSubstitution where

open import Cubical.Foundations.Prelude hiding (Sub)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Bool.Base using (true; false)
open import Cubical.Data.Empty.Base using (⊥)
import IndexIdentityCoherenceRegression as Cover
import IndexIdentityCoherence as Indexed
module Ix = Indexed.Indexed ℓ-zero

-- Contexts and substitutions are types and functions here. This is a
-- semantic model of dependent composition, not a new syntax or evaluator.
module Dependent {ℓ : Level} where
  Sub : Type ℓ → Type ℓ → Type ℓ
  Sub Γ Δ = Γ → Δ

  identity : {Γ : Type ℓ} → Sub Γ Γ
  identity γ = γ

  compose : {Γ Δ Θ : Type ℓ} → Sub Δ Θ → Sub Γ Δ → Sub Γ Θ
  compose τ σ γ = τ (σ γ)

  left-unit : {Γ Δ : Type ℓ} (σ : Sub Γ Δ) → compose identity σ ≡ σ
  left-unit σ = refl

  right-unit : {Γ Δ : Type ℓ} (σ : Sub Γ Δ) → compose σ identity ≡ σ
  right-unit σ = refl

  associative : {Γ Δ Θ Ξ : Type ℓ}
    (υ : Sub Θ Ξ) (τ : Sub Δ Θ) (σ : Sub Γ Δ)
    → compose υ (compose τ σ) ≡ compose (compose υ τ) σ
  associative υ τ σ = refl

  -- Supplying x determines which type the second input must inhabit.
  extend : {Γ X : Type ℓ} {Y : X → Type ℓ}
    (x : Γ → X) → ((γ : Γ) → Y (x γ)) → Γ → Σ X Y
  extend x y γ = x γ , y γ

  -- The continuation's result type depends on BOTH supplied inputs.
  execute : {Γ X : Type ℓ} {Y : X → Type ℓ}
    (Z : Σ X Y → Type ℓ)
    (k : (z : Σ X Y) → Z z)
    (x : Γ → X) (y : (γ : Γ) → Y (x γ))
    → (γ : Γ) → Z (extend x y γ)
  execute Z k x y γ = k (extend x y γ)

  -- Executing after substituting an environment and substituting into
  -- the executed dependent result are definitionally the same function.
  execute-substitution : {Γ Δ X : Type ℓ} {Y : X → Type ℓ}
    (Z : Σ X Y → Type ℓ) (k : (z : Σ X Y) → Z z)
    (x : Γ → X) (y : (γ : Γ) → Y (x γ)) (σ : Δ → Γ)
    → execute Z k (compose x σ) (λ δ → y (σ δ))
      ≡ (λ δ → execute Z k x y (σ δ))
  execute-substitution Z k x y σ = refl

  -- Context extension commutes with reindexing.
  extend-substitution : {Γ Δ X : Type ℓ} {Y : X → Type ℓ}
    (x : Γ → X) (y : (γ : Γ) → Y (x γ)) (σ : Δ → Γ)
    → extend {Y = Y} (compose x σ) (λ δ → y (σ δ)) ≡ compose (extend {Y = Y} x y) σ
  extend-substitution x y σ = refl

-- A nontrivial dependent family prevents collapsing equality evidence
-- to endpoint identity. This is mathematical transport, not a clock tick.
loop-computes : subst (λ x → Ix.Fibre Cover.F x) Cover.index-loop true ≡ false
loop-computes = ua-flip
  where
  open import Cubical.Foundations.Univalence using (uaβ)
  open import Cubical.Data.Bool.Properties using (notEquiv)
  ua-flip = uaβ notEquiv true

-- The upstream counterexample rules out endpoint-only transport.
endpoint-erasure-impossible : Cover.index-loop ≡ refl → ⊥
endpoint-erasure-impossible = Cover.loop-is-not-reflexive
