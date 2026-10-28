{-# OPTIONS --safe --cubical --guardedness #-}
module OriginalTransportShapeObstruction where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Bool using (Bool; true; false; false≢true)
open import Cubical.Data.Empty using (⊥; rec)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import RetainedTransportResolution as Extension
import NativeExtensionFamilyAudit as N
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero
module T = Extension.Extension ℓ-zero

-- The precise retained unary-extension output shape. This is NOT an
-- invariant of interpreted carriers or of every alternative encoding.
transport-shape : Code → Bool
transport-shape (retain (comparison _ _ _) _ (atom _)) = true
transport-shape _ = false
rule-shape : (r : Rule) → transport-shape (expression (output r)) ≡ false
rule-shape (E-rule _ _ _) = refl
rule-shape (Pi-rule _ _) = refl
rule-shape (compare-rule _ _ _ _) = refl
rule-shape (identity-rule _) = refl
rule-shape (inverse-rule _ _ _ _) = refl
rule-shape (compose-rule _ _ _ _ _ _ _) = refl
rule-shape (higher-rule _ _ _ _ _ _) = refl
rule-shape (reflexivity-rule _ _) = refl
rule-shape (path-lift-rule _ _ _ _ _) = refl
rule-shape (distribution-rule _ _ _ _) = refl
rule-shape (E-congruence-rule _ _ _ _ _ _) = refl
rule-shape (Pi-congruence-rule _ _ _ _ _) = refl

seed-required : (S : Complete → Type₁) {q : Complete}
  → transport-shape (expression q) ≡ true → Resolve S q → S q
seed-required S shape (seed s) = s
seed-required S shape (apply r ds) = rec (false≢true (sym (rule-shape r) ∙ shape))
seed-shape : {q : Complete} → N.Seeds q → transport-shape (expression q) ≡ false
seed-shape (N.source v) = refl
no-exact-transport : (a : Complete) (X : Type) (e : El (expression a) ≃ X)
  → Resolve N.Seeds (T.transported a (atom X) e) → ⊥
no-exact-transport a X e d = false≢true (sym (seed-shape (seed-required N.Seeds refl d)))

-- The failure persists even if the raw initial atom is explicitly seeded:
-- the unary extension cannot in general be eliminated under that policy.
module OneInput (X Y : Type) (x : X) (e : X ≃ Y) where
  sourceInput = pack (atom X) x
  OnlyInput : Complete → Type₁
  OnlyInput q = q ≡ sourceInput
  no-unary-elimination : Resolve OnlyInput (T.transported sourceInput (atom Y) e) → ⊥
  no-unary-elimination d = false≢true
    (sym (cong (λ q → transport-shape (expression q)) (seed-required OnlyInput refl d)))
