{-# OPTIONS --safe --cubical --guardedness #-}
module FiniteDomainInterfaceAudit where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sum.Base using (inl; inr)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Empty.Base using (⊥)
open import DomainWitnessCompiler
open import TypedGeneratorLayers using (module Histories)

-- Actual compiler iteration, not repeated untagged domain computation.
module Execution {ℓ : Level} (P : Presentation ℓ) where
  open Presentation P
  module G = Compile P
  module H = Histories G.layer

  response-stationary : (n : ℕ) (i : Input) (y : Output i)
    → H.at n (inr (i , y)) ≡ inr (i , y)
  response-stationary zero i y = refl
  response-stationary (suc n) i y = response-stationary n i y

  request-endpoint : (n : ℕ) (i : Input)
    → H.at (suc n) (inl i) ≡ inr (i , compute i)
  request-endpoint n i = response-stationary n i (compute i)

  -- The trace still grows even though its endpoint is stationary.
  retained-length : (n : ℕ) (i : Input)
    → H.length (H.generated (suc n) (inl i)) ≡ suc n
  retained-length n i = H.generated-length (suc n) (inl i)

  evaluated-then-idle : (i : Input)
    → H.History (inl i) (inr (i , compute i))
  evaluated-then-idle i = H.join (H.single (G.evaluated i))
    (H.single (G.idle i (compute i)))

  two-edges-retained : (i : Input) → H.length (evaluated-then-idle i) ≡ 2
  two-edges-retained i = refl

module B = Execution bool-presentation

boolean-twice-is-response-true :
  B.H.at 2 (inl false) ≡ inr (false , true)
boolean-twice-is-response-true = refl

-- The proposed relabelling violates the actual restricted admission type.
no-output-as-admitted-request : true ≡ false → ⊥
no-output-as-admitted-request p = false≢true (sym p)

-- Inspect proof provenance directly, without assuming proof irrelevance.
module LawOrigin {ℓ : Level} (D : DomainPresentation ℓ) where
  open DomainPresentation D
  module C = CompileDomain D
  supplied-law-recovered : (k : LawInput)
    → snd (snd (C.execute-law k)) ≡ law k
  supplied-law-recovered k = refl

  same-operation-response : (k : LawInput)
    → fst (C.execute-law k) ≡ inr (request k , compute (fst (request k)))
  same-operation-response k = refl
