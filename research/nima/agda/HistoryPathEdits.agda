{-# OPTIONS --safe --cubical --guardedness #-}
module HistoryPathEdits where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import BoundaryGeneratedQuestions as B

-- Sufficient, intentionally restricted edit policy: an actual path of history
-- values. This does not assert that DG exact edits are paths, or decide a cost
-- gate. Unit/triangle laws may be supplied as a dependent invariant; they are
-- transported from the parent, not assumed afresh at the edited endpoint.
module Edits (S : Whole.Universe.Complete ℓ-zero → Type₁)
  (Q : Whole.Universe.Code ℓ-zero)
  (Readout : Type) (observe : Whole.Universe.El ℓ-zero Q → Readout)
  (Invariant : Whole.Universe.El ℓ-zero Q → Type)
  (Cost : Type)
  (Allowed : Whole.Universe.El ℓ-zero Q → Whole.Universe.El ℓ-zero Q → Cost → Type)
  where
  open Whole.Universe ℓ-zero
  open Resolution.Generators ℓ-zero
  module App = B.Application S

  record Edit : Type₁ where
    constructor edit
    field
      before after : El Q
      change : before ≡ after
      parent : Resolve S (pack Q before)
      edited : Resolve S (pack Q after)
      parent-laws : Invariant before
      cost : Cost
      permission : Allowed before after cost
  open Edit public

  readout-preserved : (e : Edit) → observe (before e) ≡ observe (after e)
  readout-preserved e = cong observe (change e)

  laws-preserved : (e : Edit) → Invariant (after e)
  laws-preserved e = subst Invariant (change e) (parent-laws e)

  -- A dependent witness connecting the old laws with the transported laws.
  laws-coherent : (e : Edit)
    → PathP (λ i → Invariant (change e i)) (parent-laws e) (laws-preserved e)
  laws-coherent e = toPathP refl

  edit-comparison : (e : Edit) → Complete
  edit-comparison e = comparison-package (pack Q (before e)) (pack Q (after e))
    (idEquiv (El Q)) (change e)

  run : (e : Edit) → Resolve S (edit-comparison e)
  run e = App.perform (idEquiv (El Q) , change e) (parent e) (edited e)

  -- Retain the edit certificate itself at the next universe, including BOTH
  -- derivations, original invariant witness, path, permission and declared cost.
  retained-edit : Edit → Whole.Universe.Complete (ℓ-suc ℓ-zero)
  retained-edit e = Whole.Universe.pack (Whole.Universe.atom Edit) e

  recover-edit : (e : Edit) → Whole.Universe.value (retained-edit e) ≡ e
  recover-edit e = refl

  recover-parent : (e : Edit)
    → parent (Whole.Universe.value (retained-edit e)) ≡ parent e
  recover-parent e = refl

  recover-cost : (e : Edit)
    → cost (Whole.Universe.value (retained-edit e)) ≡ cost e
  recover-cost e = refl
