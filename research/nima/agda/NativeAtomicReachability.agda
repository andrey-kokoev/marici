{-# OPTIONS --safe --cubical --guardedness #-}
module NativeAtomicReachability where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥; rec)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

module Reachability (ℓ : Level) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ

  atomic-code : Code → Bool
  atomic-code (atom _) = true
  atomic-code _ = false

  atomic : Complete → Bool
  atomic q = atomic-code (expression q)

  -- Exhaustive over the CURRENT native signature, with arbitrary indices.
  -- A future atomic-producing constructor must discharge a new proof case.
  rule-nonatomic : (r : Rule) → atomic (output r) ≡ false
  rule-nonatomic (E-rule _ _ _) = refl
  rule-nonatomic (Pi-rule _ _) = refl
  rule-nonatomic (compare-rule _ _ _ _) = refl
  rule-nonatomic (identity-rule _) = refl
  rule-nonatomic (inverse-rule _ _ _ _) = refl
  rule-nonatomic (compose-rule _ _ _ _ _ _ _) = refl
  rule-nonatomic (higher-rule _ _ _ _ _ _) = refl
  rule-nonatomic (reflexivity-rule _ _) = refl
  rule-nonatomic (path-lift-rule _ _ _ _ _) = refl
  rule-nonatomic (distribution-rule _ _ _ _) = refl
  rule-nonatomic (E-congruence-rule _ _ _ _ _ _) = refl
  rule-nonatomic (Pi-congruence-rule _ _ _ _ _) = refl

  seed-required : (S : Complete → Type (ℓ-suc ℓ)) (q : Complete)
    → atomic q ≡ true → Resolve S q → S q
  seed-required S q is-atomic (seed s) = s
  seed-required S .(output r) is-atomic (apply r ds) =
    rec (false≢true (sym (rule-nonatomic r) ∙ is-atomic))

  atom-seed-required : (S : Complete → Type (ℓ-suc ℓ)) (A : Type ℓ) (x : A)
    → Resolve S (pack (atom A) x) → S (pack (atom A) x)
  atom-seed-required S A x = seed-required S (pack (atom A) x) refl

  OnlySource : Complete → Complete → Type (ℓ-suc ℓ)
  OnlySource source q = q ≡ source

  source-available : (source : Complete) → Resolve (OnlySource source) source
  source-available source = seed refl

  no-new-atom : (source : Complete) → atomic source ≡ false
    → (A : Type ℓ) (x : A) → Resolve (OnlySource source) (pack (atom A) x) → ⊥
  no-new-atom source not-atomic A x d = true≢false
    (cong atomic (atom-seed-required (OnlySource source) A x d) ∙ not-atomic)
