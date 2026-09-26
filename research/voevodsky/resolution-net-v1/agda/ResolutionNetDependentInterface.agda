{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetDependentInterface where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Empty.Base using (⊥)
import IndexIdentityCoherenceRegression as Cover
import IndexIdentityCoherence as Indexed
module Ix = Indexed.Indexed ℓ-zero

module Interface {ℓ : Level} (Γ X : Type ℓ) (Y : X → Type ℓ) where
  -- The mathematical specification of providing dependent inputs.
  Supply : Type ℓ
  Supply = Σ (Γ → X) (λ x → (γ : Γ) → Y (x γ))

  -- The same provision viewed as one map into an extended context.
  pack : Supply → (Γ → Σ X Y)
  pack (x , y) γ = x γ , y γ

  unpack : (Γ → Σ X Y) → Supply
  unpack f = (λ γ → fst (f γ)) , (λ γ → snd (f γ))

  -- This is the comprehension property, with explicit inverse laws.
  -- It retains the second input's dependency, not merely its endpoint.
  supply-equiv : Supply ≃ (Γ → Σ X Y)
  supply-equiv = isoToEquiv (iso pack unpack (λ f → refl) (λ s → refl))

  -- A continuation is a dependent function on the resulting context.
  module Continuation (Z : Σ X Y → Type ℓ) where
    Curried = (x : X) → (y : Y x) → Z (x , y)
    Uncurried = (z : Σ X Y) → Z z

    curry : Uncurried → Curried
    curry k x y = k (x , y)

    uncurry : Curried → Uncurried
    uncurry k z = k (fst z) (snd z)

    continuation-equiv : Curried ≃ Uncurried
    continuation-equiv = isoToEquiv
      (iso uncurry curry (λ k → refl) (λ k → refl))

    -- This evaluates by the SAME dependent application, in either view.
    execute : Curried → (s : Supply) → (γ : Γ) → Z (pack s γ)
    execute k s γ = uncurry k (pack s γ)

-- Equality witnesses compose operationally by transport, but this law
-- is a path, not an assertion of strict definitional associativity.
transport-composition : {ℓ : Level} {X : Type ℓ} (Y : X → Type ℓ)
  {x y z : X} (p : x ≡ y) (q : y ≡ z) (v : Y x)
  → subst Y (p ∙ q) v ≡ subst Y q (subst Y p v)
transport-composition = substComposite

-- A sharp limitation: a well-formed dependent interface need not have
-- a total coherent supplier. This rules out an internal polymorphic
-- solver for this particular family, not arbitrary external algorithms.
no-total-supplier : ((x : Ix.Index Cover.F) → Ix.Fibre Cover.F x) → ⊥
no-total-supplier = Cover.no-section
