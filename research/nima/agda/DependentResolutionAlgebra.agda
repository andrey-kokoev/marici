{-# OPTIONS --safe --cubical --guardedness #-}
module DependentResolutionAlgebra where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import WholePackageUniversalProperty as Universal
import DependentPackageNormalization as Normal
import DependentNormalizationCoherence as Coherence

module Interpretation (ℓ : Level) where
  open Whole.Universe ℓ
  open Resolution.Generators ℓ
  module N = Normal.Normalization ℓ
  module H (Q : Code) = Coherence.Coherence ℓ Q

  NormalMap : Code → Type ℓ
  NormalMap Q = (x : El Q) → Σ[ y ∈ N.Value (N.normal Q) ] (y ≡ N.normalize Q x)

  Seed : Complete → Type (ℓ-suc ℓ)
  Seed q = H.Route (expression q) (H.original (expression q)) (H.normal (expression q))

  module U = Universal.Universal ℓ Seed

  sum-map : (I : Type ℓ) (F : I → Complete)
    → ((i : I) → NormalMap (expression (F i)))
    → NormalMap (E I (λ i → retained (F i)))
  sum-map I F fs (i , x) =
    ((i , fst (fst (fs i x))) , snd (fst (fs i x))) ,
    cong (λ v → (i , fst v) , snd v) (snd (fs i x))

  product-map : (I : Type ℓ) (F : I → Complete)
    → ((i : I) → NormalMap (expression (F i)))
    → NormalMap (Pi I (λ i → retained (F i)))
  product-map I F fs x =
    equivFun (N.product-equiv I (λ i → N.normal (expression (F i)))) (λ i → fst (fs i (x i))) ,
    cong (equivFun (N.product-equiv I (λ i → N.normal (expression (F i)))))
      (funExt (λ i → snd (fs i (x i))))

  rule-map : (r : Rule)
    → ((i : Arity r) → Lift {j = ℓ-suc ℓ} (NormalMap (expression (input r i))))
    → Lift {j = ℓ-suc ℓ} (NormalMap (expression (output r)))
  rule-map (E-rule I F i) fs = lift (sum-map I F (λ j → lower (fs (lift j))))
  rule-map (Pi-rule I F) fs = lift (product-map I F (λ j → lower (fs (lift j))))
  -- Other rule outputs carry comparison/path evidence in their code/value.
  -- Normalize that complete output type, without replacing its witnesses.
  rule-map r fs = lift (λ x → N.normalize (expression (output r)) x , refl)

  algebra : U.Algebra
  algebra = record
    { Carrier = λ q → Lift {j = ℓ-suc ℓ} (NormalMap (expression q))
    ; on-seed = λ {q} route → lift (H.evaluate (expression q) route)
    ; on-rule = rule-map }

  -- Unlike an endpoint-value observer, this acts on EVERY value of the
  -- expression. The route/tree is retained independently of its evaluation.
  evaluation-preserves : {q : Complete} (d : Resolve Seed q) (x : El (expression q))
    → fst (lower (U.evaluate algebra d) x) ≡ N.normalize (expression q) x
  evaluation-preserves d x = snd (lower (U.evaluate algebra d) x)

  carrier-code : Complete → Whole.Universe.Code (ℓ-suc ℓ)
  carrier-code q = Whole.Universe.atom (U.Algebra.Carrier algebra q)

  append : {Q : Code} {P R T : H.Presentation Q}
    → H.Route Q P R → H.Route Q R T → H.Route Q P T
  append H.stop s = s
  append (H.next {R = R} f r) s = H.next {R = R} f (append r s)
