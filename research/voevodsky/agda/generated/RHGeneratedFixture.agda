{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RHGeneratedFixture where

-- Generated from structured contracts. Do not edit.
-- native contract sha256: e458391ce7b9f29ed913404cc0238600d2634a56c4a056357622671a9eb6a954
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
open import RHNativeFixture using (integerAdapter; integerCompletion; fixture-completion-preserved)
open import CompletionPreservation

record Generatedℤ³ : Type where
  constructor triple
  field a b c : ℤ
open Generatedℤ³

generated∂₁ : Generatedℤ³ → Generatedℤ³
generated∂₁ v = triple ((- a v) + b v) ((- b v) + c v) (a v + (- c v))

x y z : Generatedℤ³ → ℤ
x = a
y = b
z = c

generated∂₂ : Generatedℤ³ → ℤ
generated∂₂ v = x v + y v + z v

generated-chain : (v : Generatedℤ³) → generated∂₂ (generated∂₁ v) ≡ 0
generated-chain v = solve! ℤCommRing

generated-cycle : ℤ → ℤ → Generatedℤ³
generated-cycle p q = triple p q (- (p + q))

generated-preimage : ℤ → ℤ → Generatedℤ³
generated-preimage p q = triple 0 p (p + q)

generated-exact-a : (p q : ℤ) → a (generated∂₁ (generated-preimage p q)) ≡ p
generated-exact-a p q = solve! ℤCommRing

generated-exact-b : (p q : ℤ) → b (generated∂₁ (generated-preimage p q)) ≡ q
generated-exact-b p q = solve! ℤCommRing

generated-exact-c : (p q : ℤ) → c (generated∂₁ (generated-preimage p q)) ≡ - (p + q)
generated-exact-c p q = solve! ℤCommRing

generated-exact : (p q : ℤ) → generated∂₁ (generated-preimage p q) ≡ generated-cycle p q
generated-exact p q i = triple (generated-exact-a p q i) (generated-exact-b p q i) (generated-exact-c p q i)

generated-completion-preserved :
  (n : ℤ) → map integerAdapter (inject integerCompletion n) ≡ inject integerCompletion n
generated-completion-preserved = fixture-completion-preserved
