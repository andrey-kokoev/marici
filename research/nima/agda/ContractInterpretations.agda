{-# OPTIONS --safe --cubical --guardedness #-}
module ContractInterpretations where
------------------------------------------------------------------------
-- ContractInterpretations.agda
--
-- Checked Agda interpretations for comparison-successor contract
-- operations, following the pattern established by
-- BoundaryGeneratedQuestions.Application.perform and
-- PassiveFrameTransport.
--
-- Operations covered:
--   reference.substitute  →  compose-rule + identity-rule
--   record.reindex        →  Pi-congruence-rule
--   family.admit          →  Pi-congruence-rule
--
-- All operations are at universe level ℓ-zero, matching the existing
-- BoundaryGeneratedQuestions and WholePackageResolution conventions.
------------------------------------------------------------------------

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_; fst; snd)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import BoundaryGeneratedQuestions as B

module Interpret where
  open Whole.Universe ℓ-zero
  open Resolution.Generators ℓ-zero

  -------------------------------------------------------------------
  -- 1. reference.substitute
  --    Version reference via compose-rule with identity comparison.
  -------------------------------------------------------------------
  substitute : {S : Complete → Type (ℓ-suc ℓ-zero)} {a b : Complete}
    (e : El (expression a) ≃ El (expression b))
    (p : equivFun e (value a) ≡ value b)
    (da : Resolve S a) (db : Resolve S b)
    → Resolve S (output (compose-rule a b b e (idEquiv (El (expression b))) p refl))
  substitute {S} {a} {b} e p da db =
    let module A = B.Application S
    in apply (compose-rule a b b e (idEquiv (El (expression b))) p refl)
      (λ { (lift true)  → A.perform {a = a} {b = b} (e , p) da db
         ; (lift false) → apply (identity-rule b) (λ _ → db)
         })

  -------------------------------------------------------------------
  -- 2. record.reindex
  --    Re-index a family via Pi-congruence-rule.
  -------------------------------------------------------------------
  reindex : {S : Complete → Type (ℓ-suc ℓ-zero)} {I : Type ℓ-zero} {F G : I → Complete}
    (e : (i : I) → El (expression (F i)) ≃ El (expression (G i)))
    (p : (i : I) → equivFun (e i) (value (F i)) ≡ value (G i))
    (dF : (i : I) → Resolve S (F i))
    (dG : (i : I) → Resolve S (G i))
    → Resolve S (output (Pi-congruence-rule I F G e p))
  reindex {S} {I} {F} {G} e p dF dG =
    let module A = B.Application S
    in apply (Pi-congruence-rule I F G e p)
      (λ (lift i) → A.perform {a = F i} {b = G i} (e i , p i) (dF i) (dG i))

  -------------------------------------------------------------------
  -- 3. family.admit  (same Pi-congruence pattern)
  -------------------------------------------------------------------
  admit : {S : Complete → Type (ℓ-suc ℓ-zero)} {I : Type ℓ-zero} {F G : I → Complete}
    (e : (i : I) → El (expression (F i)) ≃ El (expression (G i)))
    (p : (i : I) → equivFun (e i) (value (F i)) ≡ value (G i))
    (dF : (i : I) → Resolve S (F i))
    (dG : (i : I) → Resolve S (G i))
    → Resolve S (output (Pi-congruence-rule I F G e p))
  admit = reindex