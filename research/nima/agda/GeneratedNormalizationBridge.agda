{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratedNormalizationBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import WholePackageUniversalProperty as Universal
import WholeHistoryComparisons as Comparison
import DependentPackageNormalization as Normal
import ProofRelevantCoherenceClosure as Witness

module Bridge (ℓ : Level)
  (S : Whole.Universe.Complete ℓ → Type (ℓ-suc ℓ))
  (A : Universal.Universal.Algebra ℓ S)
  (CarrierCode : Whole.Universe.Complete ℓ → Whole.Universe.Code (ℓ-suc ℓ))
  (encode : (q : Whole.Universe.Complete ℓ)
    → Universal.Universal.Algebra.Carrier A q ≃ Whole.Universe.El (ℓ-suc ℓ) (CarrierCode q)) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  module U = Universal.Universal ℓ S
  module C = Comparison.Comparisons ℓ S
  module O = C.Interpreted A
  module N = Normal.Normalization (ℓ-suc ℓ)
  open U.Algebra

  NormalCarrier : Complete → Type (ℓ-suc ℓ)
  NormalCarrier q = N.Value (N.normal (CarrierCode q))

  coordinates : (q : Complete) → Carrier A q ≃ NormalCarrier q
  coordinates q = compEquiv (encode q) (N.normalize-equiv (CarrierCode q))

  observe : {q : Complete} → Resolve S q → NormalCarrier q
  observe {q} d = equivFun (coordinates q) (U.evaluate A d)

  NormalSemantic : {q : Complete} → Resolve S q → Resolve S q → Type (ℓ-suc ℓ)
  NormalSemantic d e = observe d ≡ observe e

  witness-equiv : {q : Complete} (d e : Resolve S q)
    → O.Semantic d e ≃ NormalSemantic d e
  witness-equiv {q} d e = Witness.pathLift (coordinates q)

  -- Transport the actual rule algebra, including its full dependent arity.
  normalized-algebra : U.Algebra
  normalized-algebra = record
    { Carrier = NormalCarrier
    ; on-seed = λ {q} s → equivFun (coordinates q) (on-seed A s)
    ; on-rule = λ r xs → equivFun (coordinates (output r))
        (on-rule A r (λ i → invEq (coordinates (input r i)) (xs i))) }

  rule-compatibility : (r : Rule) (xs : (i : Arity r) → Carrier A (input r i))
    → equivFun (coordinates (output r)) (on-rule A r xs)
      ≡ on-rule normalized-algebra r (λ i → equivFun (coordinates (input r i)) (xs i))
  rule-compatibility r xs = sym (cong
    (λ ys → equivFun (coordinates (output r)) (on-rule A r ys))
    (funExt (λ i → retEq (coordinates (input r i)) (xs i))))

  evaluation-compatible : (q : Complete) (d : Resolve S q)
    → observe d ≡ U.evaluate normalized-algebra d
  evaluation-compatible = U.fusion A normalized-algebra
    (λ q → equivFun (coordinates q)) (λ _ _ → refl) rule-compatibility

  module Structural
    (Law : (q : Complete) → Resolve S q → Resolve S q → Type (ℓ-suc ℓ))
    (interpret-law : (q : Complete) (d e : Resolve S q) → Law q d e → O.Semantic d e) where
    module G = O.Structural Law interpret-law

    -- This consumes the existing datatype, with no new witness-import rule.
    normal-sound : {q : Complete} {d e : Resolve S q}
      → G.Generated d e → NormalSemantic d e
    normal-sound {q} c = cong (equivFun (coordinates q)) (G.sound c)

    dependent-congruence : (r : Rule)
      (ds es : (i : Arity r) → Resolve S (input r i))
      (cs : (i : Arity r) → G.Generated (ds i) (es i))
      → normal-sound (G.congruence r ds es cs)
        ≡ cong (equivFun (coordinates (output r)))
            (cong (on-rule A r) (funExt (λ i → G.sound (cs i))))
    dependent-congruence r ds es cs = refl

    NormalCompleteness : Type (ℓ-suc ℓ)
    NormalCompleteness = (q : Complete) (d e : Resolve S q) (p : NormalSemantic d e)
      → Σ[ c ∈ G.Generated d e ] (normal-sound c ≡ p)

    completeness-forward : G.Completeness → NormalCompleteness
    completeness-forward complete q d e p =
      let w = witness-equiv d e
          c , agrees = complete q d e (invEq w p)
      in c , cong (equivFun w) agrees ∙ secEq w p

    completeness-backward : NormalCompleteness → G.Completeness
    completeness-backward complete q d e p =
      let w = witness-equiv d e
          c , agrees = complete q d e (equivFun w p)
      in c , sym (retEq w (G.sound c)) ∙ cong (invEq w) agrees ∙ retEq w p

    record Retained : Type (ℓ-suc ℓ) where
      constructor retained-bridge
      field
        endpoint : Complete
        left right : Resolve S endpoint
        derivation : G.Generated left right
        original-witness : O.Semantic left right
        normalized-witness : NormalSemantic left right
        original-agreement : G.sound derivation ≡ original-witness
        normalized-agreement : normal-sound derivation ≡ normalized-witness
        reconstructed-witness : invEq (witness-equiv left right) normalized-witness ≡ original-witness

    retain-derivation : {q : Complete} {d e : Resolve S q} → G.Generated d e → Retained
    retain-derivation {q} {d} {e} c = retained-bridge q d e c (G.sound c) (normal-sound c)
      refl refl (retEq (witness-equiv d e) (G.sound c))

    next-Q : Retained → Whole.Universe.Complete (ℓ-suc ℓ)
    next-Q r = Whole.Universe.pack (Whole.Universe.atom Retained) r
