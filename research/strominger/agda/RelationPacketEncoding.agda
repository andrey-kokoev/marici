{-# OPTIONS --safe --cubical --guardedness #-}
module RelationPacketEncoding where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Sum.Base using (_⊎_; inl; inr)
open import TypedGeneratorLayers using (Layer1)
import WholePackageSigmaPi as W

-- Injective tree serialization of the finite seam keys and parent records.
-- Algebraic evaluation is checked by the source exporter, not postulated here.
data Datum : Type where
  nat : ℕ → Datum
  neg : ℕ → Datum
  edge-tag vertex-tag : Datum
  tuple : List Datum → Datum

record Term : Type where
  constructor term
  field
    word marks : List ℕ
    negative : Bool
    magnitude : ℕ

record Arrow : Type where
  constructor arrow
  field
    start end : ℕ
    terms : List Term

record Factors : Type where
  constructor factors
  field
    left right product : Arrow
    raw balanced : Datum
    composable : Arrow.end left ≡ Arrow.start right
    source-correct : Arrow.start product ≡ Arrow.start left
    target-correct : Arrow.end product ≡ Arrow.end right

record Request : Type where
  constructor request
  field
    a middle b : Arrow

leading : List Term → ℕ
leading [] = 0
leading (x ∷ xs) = Term.magnitude x

record Case : Type where
  field
    original : Request
    cut-left cut-right : Factors
    -- Complete four-event attachment evidence serialized separately from
    -- the five-event balancing comparison. No change of cutoff is concealed.
    attachment : Datum
    same-product : Factors.product cut-left ≡ Factors.product cut-right
    same-balanced : Factors.balanced cut-left ≡ Factors.balanced cut-right
    nonzero-detector : leading (Arrow.terms (Factors.product cut-left)) ≡ 1

-- The whole certified case is retained, rather than only its shared product.
record Answer (c : Case) : Type where
  constructor answer
  field
    retained : Case
    retained-correct : retained ≡ c
    value : Arrow
    value-correct : value ≡ Factors.product (Case.cut-left c)

solve : (c : Case) → Answer c
solve c = answer c refl (Factors.product (Case.cut-left c)) refl

State : Type
State = Case ⊎ (Σ[ c ∈ Case ] Answer c)
data Witness : State → State → Type where
  reconciled : (c : Case) → Witness (inl c) (inr (c , solve c))
  retained : (c : Case) (a : Answer c) → Witness (inr (c , a)) (inr (c , a))

generate : (s : State) → Σ[ t ∈ State ] Witness s t
generate (inl c) = inr (c , solve c) , reconciled c
generate (inr (c , a)) = inr (c , a) , retained c a
WG : Layer1 ℓ-zero
WG = record { State = State ; Witness = Witness ; generate = generate }

complete-answer : (c : Case) → W.Universe.Complete ℓ-zero
complete-answer c = W.Universe.pack (W.Universe.atom (Answer c)) (solve c)

recover-request : (c : Case)
  → Case.original (Answer.retained (W.Universe.value (complete-answer c)))
    ≡ Case.original c
recover-request c = refl

recover-left : (c : Case)
  → Case.cut-left (Answer.retained (W.Universe.value (complete-answer c)))
    ≡ Case.cut-left c
recover-left c = refl
recover-right : (c : Case)
  → Case.cut-right (Answer.retained (W.Universe.value (complete-answer c)))
    ≡ Case.cut-right c
recover-right c = refl
recover-attachment : (c : Case)
  → Case.attachment (Answer.retained (W.Universe.value (complete-answer c)))
    ≡ Case.attachment c
recover-attachment c = refl

next-input : (c : Case) → W.Universe.Complete (ℓ-suc ℓ-zero)
next-input c = W.reify (complete-answer c)
next-recovers : (c : Case) → W.Universe.value (next-input c) ≡ complete-answer c
next-recovers c = refl
