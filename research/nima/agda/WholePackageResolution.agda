{-# OPTIONS --safe --cubical --guardedness #-}
module WholePackageResolution where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
import WholePackageSigmaPi as Whole

module Generators (ℓ : Level) where
  open Whole.Universe ℓ

  -- Each generator carries its complete typed boundary and actual evidence.
  -- These are schemas, not a procedure for inventing arbitrary fillers.
  data Rule : Type (ℓ-suc ℓ) where
    E-rule : (I : Type ℓ) (F : I → Complete) → I → Rule
    Pi-rule : (I : Type ℓ) → (I → Complete) → Rule
    compare-rule : (a b : Complete)
      (e : El (expression a) ≃ El (expression b))
      → equivFun e (value a) ≡ value b → Rule
    identity-rule : Complete → Rule
    inverse-rule : (a b : Complete)
      (e : El (expression a) ≃ El (expression b))
      → equivFun e (value a) ≡ value b → Rule
    compose-rule : (a b c : Complete)
      (e : El (expression a) ≃ El (expression b))
      (f : El (expression b) ≃ El (expression c))
      → equivFun e (value a) ≡ value b
      → equivFun f (value b) ≡ value c → Rule
    higher-rule : (Q : Code) (x y : El Q) (p q : x ≡ y) → p ≡ q → Rule
    reflexivity-rule : (Q : Code) → El Q → Rule
    path-lift-rule : (Q R : Code) → El Q ≃ El R → El Q → El Q → Rule
    distribution-rule : (I : Type ℓ) (J : I → Type ℓ)
      (F : (i : I) → J i → Complete)
      → El (Distribution.left I J F) → Rule
    E-congruence-rule : (I : Type ℓ) (F G : I → Complete)
      (e : (i : I) → El (expression (F i)) ≃ El (expression (G i)))
      (p : (i : I) → equivFun (e i) (value (F i)) ≡ value (G i)) → I → Rule
    Pi-congruence-rule : (I : Type ℓ) (F G : I → Complete)
      (e : (i : I) → El (expression (F i)) ≃ El (expression (G i)))
      (p : (i : I) → equivFun (e i) (value (F i)) ≡ value (G i)) → Rule

  Arity : Rule → Type (ℓ-suc ℓ)
  Arity (E-rule I _ _) = Lift I
  Arity (Pi-rule I _) = Lift I
  Arity (compare-rule _ _ _ _) = Lift Bool
  Arity (identity-rule _) = Lift Unit
  Arity (inverse-rule _ _ _ _) = Lift Unit
  Arity (compose-rule _ _ _ _ _ _ _) = Lift Bool
  Arity (higher-rule _ _ _ _ _ _) = Lift Bool
  Arity (reflexivity-rule _ _) = Lift Unit
  Arity (path-lift-rule _ _ _ _ _) = Lift Unit
  Arity (distribution-rule I J _ _) = Lift {j = ℓ-suc ℓ} (Σ I J) ⊎ Lift {j = ℓ-suc ℓ} Unit
  Arity (E-congruence-rule I _ _ _ _ _) = Lift I
  Arity (Pi-congruence-rule I _ _ _ _) = Lift I

  input : (r : Rule) → Arity r → Complete
  input (E-rule _ F _) (lift i) = F i
  input (Pi-rule _ F) (lift i) = F i
  input (compare-rule a b _ _) (lift true) = a
  input (compare-rule a b _ _) (lift false) = b
  input (identity-rule a) _ = a
  input (inverse-rule a b e p) _ = comparison-package a b e p
  input (compose-rule a b c e f p q) (lift true) = comparison-package a b e p
  input (compose-rule a b c e f p q) (lift false) = comparison-package b c f q
  input (higher-rule Q x y p q _) (lift true) = path-package Q x y p
  input (higher-rule Q x y p q _) (lift false) = path-package Q x y q
  input (reflexivity-rule Q x) _ = pack Q x
  input (path-lift-rule Q R e x y) _ = pack (equivalences Q R) e
  input (distribution-rule I J F v) (inl (lift (i , j))) = F i j
  input (distribution-rule I J F v) (inr _) = pack (Distribution.left I J F) v
  input (E-congruence-rule _ F G e p _) (lift i) = comparison-package (F i) (G i) (e i) (p i)
  input (Pi-congruence-rule _ F G e p) (lift i) = comparison-package (F i) (G i) (e i) (p i)

  output : Rule → Complete
  output (E-rule I F i) = E-package I F i
  output (Pi-rule I F) = Pi-package I F
  output (compare-rule a b e p) = comparison-package a b e p
  output (identity-rule a) = identity-comparison a
  output (inverse-rule a b e p) = inverse-comparison a b e p
  output (compose-rule a b c e f p q) = compose-comparisons a b c e f p q
  output (higher-rule Q x y p q alpha) = higher-package Q x y p q alpha
  output (reflexivity-rule Q x) = path-package Q x x refl
  output (path-lift-rule Q R e x y) = lift-paths Q R e x y
  output (distribution-rule I J F v) = Distribution.generator I J F v
  output (E-congruence-rule I F G e p i) = Congruence.E-comparison I F G e p i
  output (Pi-congruence-rule I F G e p) = Congruence.Pi-comparison I F G e p

  -- Arbitrary small dependent arities replace the earlier unary/binary
  -- restriction. Histories are well-founded trees, potentially infinitely
  -- branching when the supplied index type is infinite.
  data Resolve (S : Complete → Type (ℓ-suc ℓ)) : Complete → Type (ℓ-suc ℓ) where
    seed : {q : Complete} → S q → Resolve S q
    apply : (r : Rule) → ((i : Arity r) → Resolve S (input r i)) → Resolve S (output r)

  Closure : (Complete → Type (ℓ-suc ℓ)) → Type (ℓ-suc ℓ)
  Closure S = Σ Complete (Resolve S)

  mapSeeds : {S T : Complete → Type (ℓ-suc ℓ)}
    → ((q : Complete) → S q → T q) → {q : Complete} → Resolve S q → Resolve T q
  mapSeeds f (seed s) = seed (f _ s)
  mapSeeds f (apply r ds) = apply r (λ i → mapSeeds f (ds i))

  flatten : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete}
    → Resolve (Resolve S) q → Resolve S q
  flatten (seed d) = d
  flatten (apply r ds) = apply r (λ i → flatten (ds i))

  unit-left : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete} (d : Resolve S q)
    → flatten (seed d) ≡ d
  unit-left d = refl

  unit-right : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete} (d : Resolve S q)
    → flatten (mapSeeds (λ _ → seed) d) ≡ d
  unit-right (seed s) = refl
  unit-right (apply r ds) j = apply r (λ i → unit-right (ds i) j)

  associative : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete}
    (d : Resolve (Resolve (Resolve S)) q)
    → flatten (flatten d) ≡ flatten (mapSeeds (λ _ → flatten) d)
  associative (seed d) = refl
  associative (apply r ds) j = apply r (λ i → associative (ds i) j)

  -- The complete closure history itself is a next-level package value.
  -- Its endpoint, all intermediate packages and every rule witness survive.
  reify-history : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete}
    → Resolve S q → Whole.Universe.Complete (ℓ-suc ℓ)
  reify-history {S} {q} d = Whole.Universe.pack
    (Whole.Universe.atom (Closure S)) (q , d)

  history-retained : {S : Complete → Type (ℓ-suc ℓ)} {q : Complete}
    (d : Resolve S q) → snd (Whole.Universe.value (reify-history d)) ≡ d
  history-retained d = refl
