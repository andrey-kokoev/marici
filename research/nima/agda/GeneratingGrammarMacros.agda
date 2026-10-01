{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratingGrammarMacros where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution

-- These are actual native derivations, not new literal admissions of outputs.
-- They retain supplied operands; they neither prepare independent copies nor
-- choose grouping keys, fresh identities, or next-level endpoint fields.
module Retained (ℓ : Level)
  (Admit : Tables.Core.Package ℓ → Type (ℓ-suc ℓ)) where
  module G = Tables.Core ℓ
  module N = Rules.Native ℓ
  module Run = Resolution.Full ℓ Admit

  family : (I : Type ℓ) → (I → G.Package) → G.Package
  family = N.Pi-package

  family-run : (I : Type ℓ) (F : I → G.Package)
    → ((i : I) → Run.Resolve (F i)) → Run.Resolve (family I F)
  family-run I F ds = Run.apply (N.P-kind , I , F) (λ { (lift i) → ds i })

  family-premise : (I : Type ℓ) (F : I → G.Package)
    (ds : (i : I) → Run.Resolve (F i)) (i : I)
    → Run.premise (family I F , family-run I F ds) (lift i) ≡ (F i , ds i)
  family-premise I F ds i = refl

  family-value : (I : Type ℓ) (F : I → G.Package) (i : I)
    → N.value (family I F) i ≡ N.value (F i)
  family-value I F i = refl

  -- Lift Bool to the declared carrier universe; no finite-universe coercion.
  pair-family : G.Package → G.Package → Lift {j = ℓ} Bool → G.Package
  pair-family a b (lift false) = a
  pair-family a b (lift true) = b

  pair : G.Package → G.Package → G.Package
  pair a b = family (Lift Bool) (pair-family a b)

  pair-run : (a b : G.Package) → Run.Resolve a → Run.Resolve b → Run.Resolve (pair a b)
  pair-run a b da db = family-run (Lift Bool) (pair-family a b)
    (λ { (lift false) → da ; (lift true) → db })

  pair-left-premise : (a b : G.Package) (da : Run.Resolve a) (db : Run.Resolve b)
    → Run.premise (pair a b , pair-run a b da db) (lift (lift false)) ≡ (a , da)
  pair-left-premise a b da db = refl

  pair-right-premise : (a b : G.Package) (da : Run.Resolve a) (db : Run.Resolve b)
    → Run.premise (pair a b , pair-run a b da db) (lift (lift true)) ≡ (b , db)
  pair-right-premise a b da db = refl
