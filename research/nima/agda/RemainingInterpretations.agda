{-# OPTIONS --safe --cubical --guardedness #-}
module RemainingInterpretations where
------------------------------------------------------------------------
-- RemainingInterpretations.agda
--
-- Partial checked rule applications, NOT full contract interpretations.
-- Names below are retained for compatibility; their types delimit coverage:
--
--   history.edit      →  identity-rule
--   operand.pair      →  E-rule with Bool index
--   comparison.fixed_frame  →  compare-rule + compose-rule
--   frame.active      →  one compose-rule (no inverse or frame certificate)
--
-- All operations are at universe level ℓ-zero.
------------------------------------------------------------------------

open import Cubical.Foundations.Prelude renaming (_∙_ to trans)
open import Cubical.Foundations.Equiv
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_; fst; snd)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import BoundaryGeneratedQuestions as B

module Remaining where
  open Whole.Universe ℓ-zero
  open Resolution.Generators ℓ-zero

  -----------------------------------------------------------------
  -- Helper: Bool-indexed family for pairing.
  -----------------------------------------------------------------
  pair-family : Complete → Complete → Bool → Complete
  pair-family a b false = a
  pair-family a b true  = b

  -----------------------------------------------------------------
  -- 1. history.edit
  --    identity-rule: produce identity comparison on the package.
  -----------------------------------------------------------------
  history-edit : {S : Complete → Type (ℓ-suc ℓ-zero)} {a : Complete}
    (da : Resolve S a)
    → Resolve S (output (identity-rule a))
  history-edit {S} {a} da =
    apply (identity-rule a) (λ _ → da)

  -----------------------------------------------------------------
  -- 2. operand.pair
  --    E-rule with Bool index: tagged selection, NOT a pair of values.
  --    Both premises are supplied but only the false value is selected.
  -----------------------------------------------------------------
  operand-pair : {S : Complete → Type (ℓ-suc ℓ-zero)} {a b : Complete}
    (da : Resolve S a) (db : Resolve S b)
    → Resolve S (output (E-rule Bool (pair-family a b) false))
  operand-pair {S} {a} {b} da db =
    apply (E-rule Bool (pair-family a b) false)
      (λ { (lift false) → da ; (lift true) → db })

  -----------------------------------------------------------------
  -- 3. comparison.fixed_frame
  --    C_new = C2 * r * C1, where C1: a→b, C2: b→c, r: b→b.
  --
  --    Strategy: combine C1 and r via a single compare-rule with
  --    combined equivalence compEquiv e_ab e_r and combined witness
  --    trans (cong (equivFun e_r) p_ab) p_r.  Then compose the
  --    result with C2 via compose-rule.
  --
  --    The correction is absorbed into the first leg. Separate retention
  --    of its factors and contract higher witnesses is not established.
  -----------------------------------------------------------------
  fixed-frame : {S : Complete → Type (ℓ-suc ℓ-zero)}
    {a b c : Complete}
    (e_ab : El (expression a) ≃ El (expression b))
    (p_ab : equivFun e_ab (value a) ≡ value b)
    (e_bc : El (expression b) ≃ El (expression c))
    (p_bc : equivFun e_bc (value b) ≡ value c)
    (e_r  : El (expression b) ≃ El (expression b))
    (p_r  : equivFun e_r (value b) ≡ value b)
    (da : Resolve S a) (db : Resolve S b) (dc : Resolve S c)
    → Resolve S (output (compose-rule a b c
         (compEquiv e_ab e_r) e_bc
         (trans (cong (equivFun e_r) p_ab) p_r) p_bc))
  fixed-frame {S} {a} {b} {c} e_ab p_ab e_bc p_bc e_r p_r da db dc =
    let
      module A = B.Application S
      -- C1r: combined comparison a→b (with reference correction)
      C1r = A.perform {a = a} {b = b}
              (compEquiv e_ab e_r , trans (cong (equivFun e_r) p_ab) p_r) da db
      -- C2: comparison b→c (unchanged)
      C2  = A.perform {a = b} {b = c} (e_bc , p_bc) db dc
    in apply (compose-rule a b c
               (compEquiv e_ab e_r) e_bc
               (trans (cong (equivFun e_r) p_ab) p_r) p_bc)
         (λ { (lift true)  → C1r
            ; (lift false) → C2
            })

  -----------------------------------------------------------------
  -- 4. frame.active
  --
  -- Active permutation g acting on a FramePackage:
  --   C' = g*C, d' = g*d, r' = r*g^-1
  --
  -- The frame C: a→b with equivalence f-eq, witness f-wit.
  -- The permutation g: a→a with equivalence g-eq, witness g-wit.
  -- No inverse is computed here; d, r, u, v and W are not represented.
  --
  -- Result: first g, then C (C ∘ g), using compose-rule.
  -- This is not the full active-frame action stated above.
  -----------------------------------------------------------------
  frame-active : {S : Complete → Type (ℓ-suc ℓ-zero)}
    {a b : Complete}
    -- Frame equivalence f : a ≃ b (maps, witnesses, metric carrier)
    (f-eq  : El (expression a) ≃ El (expression b))
    (f-wit : equivFun f-eq (value a) ≡ value b)
    -- Active permutation g : a ≃ a (stabiliser)
    (g-eq  : El (expression a) ≃ El (expression a))
    (g-wit : equivFun g-eq (value a) ≡ value a)
    -- Derivations for the frame endpoints
    (da : Resolve S a) (db : Resolve S b)
    → Resolve S (output (compose-rule a a b g-eq f-eq g-wit f-wit))
  frame-active {S} {a} {b} f-eq f-wit g-eq g-wit da db =
    let
      module A = B.Application S
      -- Frame comparison C: a→b
      C = A.perform {a = a} {b = b} (f-eq , f-wit) da db
      -- Permutation g: a→a
      g = A.perform {a = a} {b = a} (g-eq , g-wit) da da
    in apply (compose-rule a a b g-eq f-eq g-wit f-wit)
         (λ { (lift true)  → g
            ; (lift false) → C
            })