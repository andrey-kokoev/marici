{-# OPTIONS --safe --cubical --guardedness #-}
module WholeHistoryComparisons where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (assoc; rUnit; rCancel)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import WholePackageUniversalProperty as Universal

module Comparisons (ℓ : Level)
  (S : Whole.Universe.Complete ℓ → Type (ℓ-suc ℓ)) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  module U = Universal.Universal ℓ S
  open U.Algebra

  module Interpreted (A : U.Algebra) where
    -- Same complete endpoint, potentially different complete histories.
    Semantic : {q : Complete} → Resolve S q → Resolve S q → Type (ℓ-suc ℓ)
    Semantic d e = U.evaluate A d ≡ U.evaluate A e

    record Compared : Type (ℓ-suc ℓ) where
      constructor compared
      field
        endpoint : Complete
        left-history : Resolve S endpoint
        right-history : Resolve S endpoint
        witness : Semantic left-history right-history
    open Compared public

    identity : {q : Complete} (d : Resolve S q) → Compared
    identity {q} d = compared q d d refl

    reverse : Compared → Compared
    reverse (compared q d e p) = compared q e d (sym p)

    compose : {q : Complete} {d e f : Resolve S q}
      → Semantic d e → Semantic e f → Compared
    compose {q} {d} {e} {f} p r = compared q d f (p ∙ r)

    -- A higher record preserves both distinct comparison witnesses.
    record Higher {q : Complete} (d e : Resolve S q) : Type (ℓ-suc ℓ) where
      constructor higher
      field
        left-witness : Semantic d e
        right-witness : Semantic d e
        filler : left-witness ≡ right-witness

    associativity : {q : Complete} {d e f g : Resolve S q}
      (p : Semantic d e) (r : Semantic e f) (s : Semantic f g) → Higher d g
    associativity p r s = higher (p ∙ (r ∙ s)) ((p ∙ r) ∙ s) (assoc p r s)

    right-unit : {q : Complete} {d e : Resolve S q} (p : Semantic d e) → Higher d e
    right-unit p = higher p (p ∙ refl) (rUnit p)

    cancellation : {q : Complete} {d e : Resolve S q} (p : Semantic d e) → Higher d d
    cancellation p = higher (p ∙ sym p) refl (rCancel p)

    package : Compared → Whole.Universe.Complete (ℓ-suc ℓ)
    package c = Whole.Universe.pack (Whole.Universe.atom Compared) c

    recover-comparison : (c : Compared) → Whole.Universe.value (package c) ≡ c
    recover-comparison c = refl

    reify-higher : {q : Complete} {d e : Resolve S q}
      → Higher d e → Whole.Universe.Complete (ℓ-suc ℓ)
    reify-higher {q} {d} {e} h = Whole.Universe.pack
      (Whole.Universe.atom (Σ[ q ∈ Complete ] Σ[ d ∈ Resolve S q ]
                             Σ[ e ∈ Resolve S q ] Higher d e))
      (q , d , e , h)

    -- Chosen structural laws are supplied separately from arbitrary
    -- Semantic witnesses. No semantic-import constructor is present.
    module Structural
      (Law : (q : Complete) → Resolve S q → Resolve S q → Type (ℓ-suc ℓ))
      (interpret-law : (q : Complete) (d e : Resolve S q) → Law q d e → Semantic d e)
      where

      data Generated : {q : Complete} → Resolve S q → Resolve S q → Type (ℓ-suc ℓ) where
        reflexive : {q : Complete} (d : Resolve S q) → Generated d d
        invert : {q : Complete} {d e : Resolve S q} → Generated d e → Generated e d
        concatenate : {q : Complete} {d e f : Resolve S q}
          → Generated d e → Generated e f → Generated d f
        law : {q : Complete} {d e : Resolve S q} → Law q d e → Generated d e
        congruence : (r : Rule)
          (ds es : (i : Arity r) → Resolve S (input r i))
          → ((i : Arity r) → Generated (ds i) (es i))
          → Generated (apply r ds) (apply r es)

      sound : {q : Complete} {d e : Resolve S q} → Generated d e → Semantic d e
      sound (reflexive d) = refl
      sound (invert c) = sym (sound c)
      sound (concatenate c c') = sound c ∙ sound c'
      sound (law {q} {d} {e} witness) = interpret-law q d e witness
      sound (congruence r ds es cs) =
        cong (on-rule A r) (funExt (λ i → sound (cs i)))

      -- Derivation AND interpreted witness survive in the retained record.
      record Certified : Type (ℓ-suc ℓ) where
        constructor certified
        field
          endpoint : Complete
          left-history : Resolve S endpoint
          right-history : Resolve S endpoint
          derivation : Generated left-history right-history
          semantic-witness : Semantic left-history right-history
          agrees-with-derivation : sound derivation ≡ semantic-witness

      certify : {q : Complete} {d e : Resolve S q} → Generated d e → Certified
      certify {q} {d} {e} c = certified q d e c (sound c) refl

      reify-certified : Certified → Whole.Universe.Complete (ℓ-suc ℓ)
      reify-certified c = Whole.Universe.pack (Whole.Universe.atom Certified) c

      -- Completeness, if later established, must account for the actual
      -- semantic witness, not just find some comparison of the endpoints.
      Completeness : Type (ℓ-suc ℓ)
      Completeness = (q : Complete) (d e : Resolve S q) (p : Semantic d e)
        → Σ[ c ∈ Generated d e ] (sound c ≡ p)
