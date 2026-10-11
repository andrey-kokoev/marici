{-# OPTIONS --safe --cubical --guardedness #-}
module RetainedParentSelectionAudit where

open import Cubical.Foundations.Prelude
import IndexedConstructorTables as Tables
import NativeTableRules as Rules

-- Audit the actual native retained-package constructor, not a replacement
-- syntax. Packaging supplied targets is NOT a reachability derivation.
module Audit (ℓ : Level) where
  module G = Tables.Core ℓ
  module N = Rules.Native ℓ

  module FixedParent (parent : G.Package) (B : Type ℓ) (code : G.Node B) where
    retained : B → G.Package
    retained x = N.remember parent (N.pack code x)

    active : B → B
    active x = N.value (retained x)

    target-recovered : (x : B) → active x ≡ x
    target-recovered x = refl

    same-parent-header : (x : B)
      → G.header (N.expression (retained x))
        ≡ G.retain-header (N.Ty parent) (N.value parent) B
    same-parent-header x = refl

    -- Every supplied target value remains possible at the representation
    -- level with this identical retained parent. No physical filter is added.
    active-surjective : (y : B) → Σ[ x ∈ B ] active x ≡ y
    active-surjective y = y , refl

    extra-condition : (R : B → Type ℓ)
      → ((x : B) → R (active x)) → (x : B) → R x
    extra-condition R certificate x = certificate x
