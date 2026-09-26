{-# OPTIONS --safe --cubical --guardedness #-}
module DependentSigmaPiResolutionClosure where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import Cubical.Data.Empty.Base using (⊥*)
import CoherenceResolutionClosure as Free
import DependentSigmaPiCoherence as Chains

-- A concrete first signature: the complete checked trace/witness packages,
-- their reversible transport, and their internal equality witnesses.
module Concrete {ℓ : Level}
  (I : Type ℓ) (J : I → Type ℓ)
  (K : (i : I) → J i → Type ℓ)
  (L : (i : I) (j : J i) → K i j → Type ℓ)
  (B : (i : I) (j : J i) (k : K i j) → L i j k → Type ℓ) where

  module C = Chains.Construction I J K L B
  module R = C.Retained

  Package : Type ℓ
  Package = R.SourceRecord ⊎ R.TargetRecord

  data Step : Package → Package → Type ℓ where
    forward : (r : R.SourceRecord)
            → Step (inl r) (inr (equivFun R.recordLift r))
    backward : (r : R.TargetRecord)
             → Step (inr r) (inl (invEq R.recordLift r))
    compare : {p q : Package} → p ≡ q → Step p q

  module All = Free.Closure Package Step (λ _ _ _ → ⊥*)

  Seed : C.X → Package → Type ℓ
  Seed x p = p ≡ inl (C.canonicalRecord x)

  begin : (x : C.X) → All.Resolve (Seed x) (inl (C.canonicalRecord x))
  begin x = All.seed refl

  out : (x : C.X) → All.Resolve (Seed x) (inr (C.transportedRecord x))
  out x = All.unary (forward (C.canonicalRecord x)) (begin x)

  back : (x : C.X) → All.Resolve (Seed x)
    (inl (invEq R.recordLift (C.transportedRecord x)))
  back x = All.unary (backward (C.transportedRecord x)) (out x)

  -- The roundtrip proof is explicitly stored as the final rule witness.
  closed-route : (x : C.X) → All.Resolve (Seed x) (inl (C.canonicalRecord x))
  closed-route x = All.unary
    (compare (cong inl (C.full-chain-roundtrip x))) (back x)

  reapply : (x : C.X) → All.Resolve (All.Resolve (Seed x))
    (inl (C.canonicalRecord x))
  reapply x = All.seed (closed-route x)

  reapply-flattens : (x : C.X) → All.flatten (reapply x) ≡ closed-route x
  reapply-flattens x = refl
