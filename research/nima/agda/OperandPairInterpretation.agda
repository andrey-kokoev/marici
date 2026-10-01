{-# OPTIONS --safe --cubical --guardedness #-}
module OperandPairInterpretation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit)
open import Cubical.Data.Sigma.Base using (_×_)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

-- Explicit supplied operands, not independent preparation or fresh labels.
module Pairing where
  open Whole.Universe ℓ-zero
  open Resolution.Generators ℓ-zero

  family : Complete → Complete → Bool → Complete
  family a b false = a
  family a b true = b

  pair : Complete → Complete → Complete
  pair a b = Pi-package Bool (family a b)

  run : {S : Complete → Type₁} (a b : Complete)
    → Resolve S a → Resolve S b → Resolve S (pair a b)
  run a b da db = apply (Pi-rule Bool (family a b))
    (λ { (lift false) → da ; (lift true) → db })

  left-value : (a b : Complete) → value (pair a b) false ≡ value a
  left-value a b = refl

  right-value : (a b : Complete) → value (pair a b) true ≡ value b
  right-value a b = refl

  -- The whole output value, not merely its code, is equivalent to a pair.
  unpack : (a b : Complete) → El (expression (pair a b))
    → El (expression a) × El (expression b)
  unpack a b v = v false , v true

  assemble : (a b : Complete) → El (expression a) × El (expression b)
    → El (expression (pair a b))
  assemble a b (x , y) false = x
  assemble a b (x , y) true = y

  unpack-assemble : (a b : Complete)
    (v : El (expression a) × El (expression b))
    → unpack a b (assemble a b v) ≡ v
  unpack-assemble a b (x , y) = refl

  assemble-unpack : (a b : Complete) (v : El (expression (pair a b)))
    → assemble a b (unpack a b v) ≡ v
  assemble-unpack a b v = funExt (λ { false → refl ; true → refl })

  -- Inspect the actual apply node. These equalities certify that neither
  -- operand derivation has been replaced by a fresh seed of the result.
  Branch : {S : Complete → Type₁} {q : Complete} → Resolve S q → Type₁
  Branch (seed _) = Lift Unit
  Branch (apply r ds) = Arity r

  premise : {S : Complete → Type₁} {q : Complete}
    (d : Resolve S q) → Branch d → Closure S
  premise {q = q} (seed s) _ = q , seed s
  premise (apply r ds) i = input r i , ds i

  left-premise : {S : Complete → Type₁} (a b : Complete)
    (da : Resolve S a) (db : Resolve S b)
    → premise (run a b da db) (lift false) ≡ (a , da)
  left-premise a b da db = refl

  right-premise : {S : Complete → Type₁} (a b : Complete)
    (da : Resolve S a) (db : Resolve S b)
    → premise (run a b da db) (lift true) ≡ (b , db)
  right-premise a b da db = refl
