{-# OPTIONS --safe --cubical --guardedness #-}
module WholeHistoryComparisonInstance where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥; ⊥*; rec*)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import WholePackageUniversalProperty as Universal
import WholePackageHistorySeparation as Separation
import WholeHistoryComparisons as Comparison

module Concrete (ℓ : Level) (a : Whole.Universe.Complete ℓ) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  module D = Separation.Separation ℓ a
  module U = Universal.Universal ℓ D.Seed
  module C = Comparison.Comparisons ℓ D.Seed

  -- This observer reads the actual endpoint value. The separate compared
  -- record continues to retain both full histories, including rule data.
  endpoint-algebra : U.Algebra
  endpoint-algebra = record
    { Carrier = λ q → Lift {j = ℓ-suc ℓ} (El (expression q))
    ; on-seed = λ {q} _ → lift (value q)
    ; on-rule = λ r _ → lift (value (output r)) }

  module Observed = C.Interpreted endpoint-algebra

  observed-agreement : Observed.Semantic D.by-identity D.by-general-comparison
  observed-agreement = refl

  -- The selected equation is explicitly a comparison of distinct histories,
  -- not an equality identifying the raw derivation constructors.
  data Law : (q : Complete) → Resolve D.Seed q → Resolve D.Seed q → Type (ℓ-suc ℓ) where
    identity-as-general : Law (identity-comparison a) D.by-identity D.by-general-comparison

  interpret-law : (q : Complete) (d e : Resolve D.Seed q) → Law q d e → Observed.Semantic d e
  interpret-law _ _ _ identity-as-general = observed-agreement

  module Structural = Observed.Structural Law interpret-law

  generated-comparison : Structural.Generated D.by-identity D.by-general-comparison
  generated-comparison = Structural.law identity-as-general

  retained-comparison : Structural.Certified
  retained-comparison = Structural.certify generated-comparison

  next-Q : Whole.Universe.Complete (ℓ-suc ℓ)
  next-Q = Structural.reify-certified retained-comparison

  original-history-retained :
    Structural.Certified.left-history (Whole.Universe.value next-Q) ≡ D.by-identity
  original-history-retained = refl

  alternative-history-retained :
    Structural.Certified.right-history (Whole.Universe.value next-Q) ≡ D.by-general-comparison
  alternative-history-retained = refl

  cancellation-comparison : Observed.Higher D.by-identity D.by-identity
  cancellation-comparison = Observed.cancellation
    {d = D.by-identity} {e = D.by-general-comparison}
    (Structural.sound generated-comparison)

  next-higher-Q : Whole.Universe.Complete (ℓ-suc ℓ)
  next-higher-Q = Observed.reify-higher cancellation-comparison

  -- With no selected structural laws, congruence/inversion/composition
  -- alone cannot recover even this available endpoint comparison.
  EmptyLaw : (q : Complete) → Resolve D.Seed q → Resolve D.Seed q → Type (ℓ-suc ℓ)
  EmptyLaw _ _ _ = ⊥*

  interpret-empty : (q : Complete) (d e : Resolve D.Seed q)
    → EmptyLaw q d e → Observed.Semantic d e
  interpret-empty _ _ _ = rec*

  module Bare = Observed.Structural EmptyLaw interpret-empty

  bare-reflects-identity : {q : Complete} {d e : Resolve D.Seed q}
    → Bare.Generated d e → d ≡ e
  bare-reflects-identity (Bare.reflexive d) = refl
  bare-reflects-identity (Bare.invert p) = sym (bare-reflects-identity p)
  bare-reflects-identity (Bare.concatenate p q) = bare-reflects-identity p ∙ bare-reflects-identity q
  bare-reflects-identity (Bare.law impossible) = rec* impossible
  bare-reflects-identity (Bare.congruence r ds es cs) =
    cong (apply r) (funExt (λ i → bare-reflects-identity (cs i)))

  missing-equation : Bare.Generated D.by-identity D.by-general-comparison → ⊥
  missing-equation c = D.histories-distinct (bare-reflects-identity c)

  bare-incomplete : Bare.Completeness → ⊥
  bare-incomplete complete = missing-equation
    (fst (complete (identity-comparison a) D.by-identity D.by-general-comparison observed-agreement))
