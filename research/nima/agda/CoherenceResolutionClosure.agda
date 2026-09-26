{-# OPTIONS --safe --cubical --guardedness #-}
module CoherenceResolutionClosure where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Sigma.Properties using (Σ-cong-equiv-snd)
open import Cubical.HITs.PropositionalTruncation.Base

-- P ranges over complete packages, not their underlying vertices/types.
-- U and V specify admitted one- and two-premise resolution steps.
-- Their inhabitants retain the actual rule/comparison witness.
-- Neither the package types nor the derivations are assumed truncated.
module Closure {ℓ : Level}
  (P : Type ℓ)
  (U : P → P → Type ℓ)
  (V : P → P → P → Type ℓ) where

  data Resolve (S : P → Type ℓ) : P → Type ℓ where
    seed : {p : P} → S p → Resolve S p
    unary : {p q : P} → U p q → Resolve S p → Resolve S q
    binary : {p q r : P} → V p q r → Resolve S p → Resolve S q → Resolve S r

  -- The entire family is the witness-bearing closure: every finite
  -- derivation, in every admitted order, with all its rule witnesses.
  PackageClosure : (P → Type ℓ) → Type ℓ
  PackageClosure S = Σ P (Resolve S)

  mapSeeds : {S T : P → Type ℓ} → ((p : P) → S p → T p)
           → {p : P} → Resolve S p → Resolve T p
  mapSeeds f (seed s) = seed (f _ s)
  mapSeeds f (unary u d) = unary u (mapSeeds f d)
  mapSeeds f (binary v d e) = binary v (mapSeeds f d) (mapSeeds f e)

  -- A resolution of resolutions substitutes the retained inner histories.
  flatten : {S : P → Type ℓ} {p : P} → Resolve (Resolve S) p → Resolve S p
  flatten (seed d) = d
  flatten (unary u d) = unary u (flatten d)
  flatten (binary v d e) = binary v (flatten d) (flatten e)

  unit-left : {S : P → Type ℓ} {p : P} (d : Resolve S p)
            → flatten (seed d) ≡ d
  unit-left d = refl

  unit-right : {S : P → Type ℓ} {p : P} (d : Resolve S p)
             → flatten (mapSeeds (λ _ → seed) d) ≡ d
  unit-right (seed s) = refl
  unit-right (unary u d) = cong (unary u) (unit-right d)
  unit-right (binary v d e) i = binary v (unit-right d i) (unit-right e i)

  associative : {S : P → Type ℓ} {p : P}
                (d : Resolve (Resolve (Resolve S)) p)
              → flatten (flatten d) ≡ flatten (mapSeeds (λ _ → flatten) d)
  associative (seed d) = refl
  associative (unary u d) = cong (unary u) (associative d)
  associative (binary v d e) i = binary v (associative d i) (associative e i)

  map-id : {S : P → Type ℓ} {p : P} (d : Resolve S p)
         → mapSeeds (λ _ s → s) d ≡ d
  map-id (seed s) = refl
  map-id (unary u d) = cong (unary u) (map-id d)
  map-id (binary v d e) i = binary v (map-id d i) (map-id e i)

  map-compose : {S T W : P → Type ℓ}
                (f : (p : P) → S p → T p) (g : (p : P) → T p → W p)
                {p : P} (d : Resolve S p)
              → mapSeeds g (mapSeeds f d) ≡ mapSeeds (λ p s → g p (f p s)) d
  map-compose f g (seed s) = refl
  map-compose f g (unary u d) = cong (unary u) (map-compose f g d)
  map-compose f g (binary v d e) i = binary v (map-compose f g d i) (map-compose f g e i)

  -- A separate reachability view answers only which packages occur.
  -- Truncation is confined to membership; PackageClosure above keeps histories.
  Reach : (P → Type ℓ) → P → Type ℓ
  Reach S p = ∥ Resolve S p ∥₁

  truncMap : {A B : Type ℓ} → (A → B) → ∥ A ∥₁ → ∥ B ∥₁
  truncMap f ∣ a ∣₁ = ∣ f a ∣₁
  truncMap f (squash₁ x y i) = squash₁ (truncMap f x) (truncMap f y) i

  truncBinary : {A B C : Type ℓ} → (A → B → C)
              → ∥ A ∥₁ → ∥ B ∥₁ → ∥ C ∥₁
  truncBinary f ∣ a ∣₁ b = truncMap (f a) b
  truncBinary f (squash₁ x y i) b = squash₁ (truncBinary f x b) (truncBinary f y b) i

  reachFold : {S : P → Type ℓ} {p : P} → Resolve (Reach S) p → Reach S p
  reachFold (seed d) = d
  reachFold (unary u d) = truncMap (unary u) (reachFold d)
  reachFold (binary v d e) = truncBinary (binary v) (reachFold d) (reachFold e)

  saturate : {S : P → Type ℓ} {p : P} → Reach (Reach S) p → Reach S p
  saturate ∣ d ∣₁ = reachFold d
  saturate (squash₁ x y i) = squash₁ (saturate x) (saturate y) i

  reach-idempotent : (S : P → Type ℓ) (p : P) → Reach (Reach S) p ≃ Reach S p
  reach-idempotent S p = isoToEquiv
    (iso saturate (λ d → ∣ seed d ∣₁)
      (λ d → squash₁ _ d) (λ d → squash₁ _ d))

  -- Actual package data p are unchanged by this membership equivalence.
  support-idempotent : (S : P → Type ℓ)
                    → (Σ P (Reach (Reach S))) ≃ (Σ P (Reach S))
  support-idempotent S = Σ-cong-equiv-snd (reach-idempotent S)
