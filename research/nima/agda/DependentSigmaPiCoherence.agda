{-# OPTIONS --safe --cubical --guardedness #-}
module DependentSigmaPiCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
import ProofRelevantCoherenceClosure as Closure

module Construction {ℓ : Level}
  (I : Type ℓ) (J : I → Type ℓ)
  (K : (i : I) → J i → Type ℓ)
  (L : (i : I) (j : J i) → K i j → Type ℓ)
  (B : (i : I) (j : J i) (k : K i j) → L i j k → Type ℓ) where

  X : Type ℓ
  X = (i : I) → Σ[ j ∈ J i ] ((k : K i j) → Σ[ l ∈ L i j k ] B i j k l)

  F : Type ℓ
  F = (i : I) → J i

  G : F → Type ℓ
  G f = (i : I) (k : K i (f i)) → L i (f i) k

  W : (f : F) → G f → Type ℓ
  W f g = (i : I) (k : K i (f i)) → B i (f i) k (g i k)

  N : Type ℓ
  N = Σ[ f ∈ F ] Σ[ g ∈ G f ] W f g

  A1 : Type ℓ
  A1 = Σ[ f ∈ F ] ((i : I) (k : K i (f i)) → Σ[ l ∈ L i (f i) k ] B i (f i) k l)

  A2 : Type ℓ
  A2 = Σ[ f ∈ F ] ((i : I) →
         Σ[ h ∈ ((k : K i (f i)) → L i (f i) k) ]
           ((k : K i (f i)) → B i (f i) k (h k)))

  B1 : Type ℓ
  B1 = (i : I) → Σ[ j ∈ J i ]
         Σ[ h ∈ ((k : K i j) → L i j k) ] ((k : K i j) → B i j k (h k))

  C : I → Type ℓ
  C i = Σ[ j ∈ J i ] ((k : K i j) → L i j k)

  B2 : Type ℓ
  B2 = (i : I) → Σ[ c ∈ C i ] ((k : K i (fst c)) → B i (fst c) k (snd c k))

  B3 : Type ℓ
  B3 = Σ[ c ∈ ((i : I) → C i) ]
         ((i : I) (k : K i (fst (c i))) → B i (fst (c i)) k (snd (c i) k))

  edgeA1 : Iso X A1
  Iso.fun edgeA1 x = (λ i → fst (x i)) , (λ i → snd (x i))
  Iso.inv edgeA1 (f , v) i = f i , v i
  Iso.rightInv edgeA1 _ = refl
  Iso.leftInv edgeA1 _ = refl

  edgeA2 : Iso A1 A2
  Iso.fun edgeA2 (f , v) = f , (λ i → (λ k → fst (v i k)) , (λ k → snd (v i k)))
  Iso.inv edgeA2 (f , v) = f , (λ i k → fst (v i) k , snd (v i) k)
  Iso.rightInv edgeA2 _ = refl
  Iso.leftInv edgeA2 _ = refl

  edgeA3 : Iso A2 N
  Iso.fun edgeA3 (f , v) = f , (λ i → fst (v i)) , (λ i → snd (v i))
  Iso.inv edgeA3 (f , g , w) = f , (λ i → g i , w i)
  Iso.rightInv edgeA3 _ = refl
  Iso.leftInv edgeA3 _ = refl

  edgeB1 : Iso X B1
  Iso.fun edgeB1 x i = fst (x i) , (λ k → fst (snd (x i) k)) , (λ k → snd (snd (x i) k))
  Iso.inv edgeB1 v i = fst (v i) , (λ k → fst (snd (v i)) k , snd (snd (v i)) k)
  Iso.rightInv edgeB1 _ = refl
  Iso.leftInv edgeB1 _ = refl

  edgeB2 : Iso B1 B2
  Iso.fun edgeB2 v i = (fst (v i) , fst (snd (v i))) , snd (snd (v i))
  Iso.inv edgeB2 v i = fst (fst (v i)) , snd (fst (v i)) , snd (v i)
  Iso.rightInv edgeB2 _ = refl
  Iso.leftInv edgeB2 _ = refl

  edgeB3 : Iso B2 B3
  Iso.fun edgeB3 v = (λ i → fst (v i)) , (λ i → snd (v i))
  Iso.inv edgeB3 (c , w) i = c i , w i
  Iso.rightInv edgeB3 _ = refl
  Iso.leftInv edgeB3 _ = refl

  edgeB4 : Iso B3 N
  Iso.fun edgeB4 (c , w) = (λ i → fst (c i)) , (λ i → snd (c i)) , w
  Iso.inv edgeB4 (f , g , w) = (λ i → f i , g i) , w
  Iso.rightInv edgeB4 _ = refl
  Iso.leftInv edgeB4 _ = refl

  routeA : Iso X N
  routeA = compIso (compIso edgeA1 edgeA2) edgeA3

  routeB : Iso X N
  routeB = compIso (compIso (compIso edgeB1 edgeB2) edgeB3) edgeB4

  route-comparison : (x : X) → Iso.fun routeA x ≡ Iso.fun routeB x
  route-comparison x = refl

  -- Every intermediate value and its connecting equality is retained.
  record Trace (x : X) : Type ℓ where
    field
      a1 : A1
      a2 : A2
      a3 : N
      b1 : B1
      b2 : B2
      b3 : B3
      b4 : N
      linkA1 : Iso.fun edgeA1 x ≡ a1
      linkA2 : Iso.fun edgeA2 a1 ≡ a2
      linkA3 : Iso.fun edgeA3 a2 ≡ a3
      linkB1 : Iso.fun edgeB1 x ≡ b1
      linkB2 : Iso.fun edgeB2 b1 ≡ b2
      linkB3 : Iso.fun edgeB3 b2 ≡ b3
      linkB4 : Iso.fun edgeB4 b3 ≡ b4

  canonicalTrace : (x : X) → Trace x
  canonicalTrace x = record
    { a1 = Iso.fun edgeA1 x
    ; a2 = Iso.fun edgeA2 (Iso.fun edgeA1 x)
    ; a3 = Iso.fun routeA x
    ; b1 = Iso.fun edgeB1 x
    ; b2 = Iso.fun edgeB2 (Iso.fun edgeB1 x)
    ; b3 = Iso.fun edgeB3 (Iso.fun edgeB2 (Iso.fun edgeB1 x))
    ; b4 = Iso.fun routeB x
    ; linkA1 = refl ; linkA2 = refl ; linkA3 = refl
    ; linkB1 = refl ; linkB2 = refl ; linkB3 = refl ; linkB4 = refl }

  -- A comparison for every linked trace, assembled from its stored paths.
  traceComparison : (x : X) (t : Trace x) → Trace.a3 t ≡ Trace.b4 t
  traceComparison x t = sym aPath ∙ route-comparison x ∙ bPath
    where
    aPath : Iso.fun routeA x ≡ Trace.a3 t
    aPath = cong (Iso.fun edgeA3)
              (cong (Iso.fun edgeA2) (Trace.linkA1 t) ∙ Trace.linkA2 t)
              ∙ Trace.linkA3 t
    bPath : Iso.fun routeB x ≡ Trace.b4 t
    bPath = cong (Iso.fun edgeB4)
              (cong (Iso.fun edgeB3)
                (cong (Iso.fun edgeB2) (Trace.linkB1 t) ∙ Trace.linkB2 t)
                ∙ Trace.linkB3 t)
              ∙ Trace.linkB4 t

  -- Transport the endpoint witness through the inverse normalization,
  -- while retaining the entire original source and full Trace record.
  module Retained = Closure.Records Trace
    (λ x t → Trace.a3 t) (λ x t → Trace.b4 t)
    (invEquiv (isoToEquiv routeA))

  linkedRecord : (x : X) → Trace x → Retained.SourceRecord
  linkedRecord x t = x , t , traceComparison x t

  canonicalRecord : (x : X) → Retained.SourceRecord
  canonicalRecord x = x , canonicalTrace x , route-comparison x

  transportedRecord : (x : X) → Retained.TargetRecord
  transportedRecord x = equivFun Retained.recordLift (canonicalRecord x)

  full-chain-roundtrip : (x : X) →
    invEq Retained.recordLift (transportedRecord x) ≡ canonicalRecord x
  full-chain-roundtrip x = Retained.record-roundtrip (canonicalRecord x)
