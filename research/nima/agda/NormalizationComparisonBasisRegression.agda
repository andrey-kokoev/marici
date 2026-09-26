{-# OPTIONS --safe --cubical --guardedness #-}
module NormalizationComparisonBasisRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import NormalizationComparisonBasis as Basis
import DependentReorderingLawRegression as Example

module B = Basis.Basis ℓ-zero
module R = Example.R
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

x = Example.source
q = R.endpoint x
left = R.outer-history x
right = R.inner-history x

-- The earlier named dependent-reorder law is now DERIVED using only the
-- two normalization schemas. Its actual previous witness is reconstructed.
derived-reordering : B.G.Generated left right
derived-reordering = B.compare left right

previous-witness : B.O.Semantic left right
previous-witness = R.G.sound (R.generated x)

reconstructed-reordering :
  Σ[ c ∈ B.G.Generated left right ] (B.G.sound c ≡ previous-witness)
reconstructed-reordering = B.completeness q left right previous-witness

infinite-context-derived = B.compare (R.pi-left ℕ (λ _ → x)) (R.pi-right ℕ (λ _ → x))

retained-result = B.realize left right previous-witness
next-input = B.next-Q retained-result

requested-witness-retained :
  B.Requested.witness (Whole.Universe.value next-input) ≡ previous-witness
requested-witness-retained = refl

module Next = Basis.Basis (ℓ-suc ℓ-zero)

nested-input = Next.next-Q
  (Next.realize (Next.canonical next-input) (Next.canonical next-input) refl)

whole-previous-package-retained :
  Next.Requested.endpoint (Whole.Universe.value nested-input) ≡ next-input
whole-previous-package-retained = refl

raw-histories-distinct : left ≡ right → ⊥
raw-histories-distinct = R.history-records-distinct x

-- Derivations are not quotiented by completeness.
direct : B.G.Generated (B.canonical q) (B.canonical q)
direct = B.G.reflexive (B.canonical q)
redundant : B.G.Generated (B.canonical q) (B.canonical q)
redundant = B.G.invert direct

is-reflexive : {q : Complete} {d e : Resolve B.A.Seed q} → B.G.Generated d e → Bool
is-reflexive (B.G.reflexive _) = true
is-reflexive _ = false

derivations-distinct : direct ≡ redundant → ⊥
derivations-distinct p = true≢false (cong is-reflexive p)

-- Remove the rule-normalization schema: root constructors cannot change.
data SeedLaw : (q : Complete) → Resolve B.A.Seed q → Resolve B.A.Seed q → Type₁ where
  only-seed : (q : Complete) (s : B.A.Seed q) → SeedLaw q (seed s) (B.canonical q)

seed-interpret : (q : Complete) (d e : Resolve B.A.Seed q) → SeedLaw q d e → B.O.Semantic d e
seed-interpret q d e _ = fst (B.semantic-contractible d e)
module SeedOnly = B.O.Structural SeedLaw seed-interpret

root-tag : {q : Complete} → Resolve B.A.Seed q → Bool
root-tag (seed _) = false
root-tag (apply _ _) = true

seed-only-preserves : {q : Complete} {d e : Resolve B.A.Seed q}
  → SeedOnly.Generated d e → root-tag d ≡ root-tag e
seed-only-preserves (SeedOnly.reflexive _) = refl
seed-only-preserves (SeedOnly.invert c) = sym (seed-only-preserves c)
seed-only-preserves (SeedOnly.concatenate c c') = seed-only-preserves c ∙ seed-only-preserves c'
seed-only-preserves (SeedOnly.law (only-seed _ _)) = refl
seed-only-preserves (SeedOnly.congruence _ _ _ _) = refl

missing-rule-schema : (r : Rule)
  → SeedOnly.Generated (apply r (B.canonical-children r)) (B.canonical (output r)) → ⊥
missing-rule-schema r c = true≢false (seed-only-preserves c)

-- Remove seed normalization: canonical rule contraction does not supply
-- the missing comparison of two genuinely different route seeds.
data RuleLaw : (q : Complete) → Resolve B.A.Seed q → Resolve B.A.Seed q → Type₁ where
  only-rule : (r : Rule) → RuleLaw (output r)
    (apply r (B.canonical-children r)) (B.canonical (output r))

rule-interpret : (q : Complete) (d e : Resolve B.A.Seed q) → RuleLaw q d e → B.O.Semantic d e
rule-interpret q d e _ = fst (B.semantic-contractible d e)
module RuleOnly = B.O.Structural RuleLaw rule-interpret

seed-tag : {q : Complete} → Resolve B.A.Seed q → Bool
seed-tag (seed s) = R.is-four s
seed-tag (apply _ _) = false

rule-only-preserves : {q : Complete} {d e : Resolve B.A.Seed q}
  → RuleOnly.Generated d e → seed-tag d ≡ seed-tag e
rule-only-preserves (RuleOnly.reflexive _) = refl
rule-only-preserves (RuleOnly.invert c) = sym (rule-only-preserves c)
rule-only-preserves (RuleOnly.concatenate c c') = rule-only-preserves c ∙ rule-only-preserves c'
rule-only-preserves (RuleOnly.law (only-rule _)) = refl
rule-only-preserves (RuleOnly.congruence _ _ _ _) = refl

missing-seed-schema : RuleOnly.Generated left right → ⊥
missing-seed-schema c = true≢false (rule-only-preserves c)
