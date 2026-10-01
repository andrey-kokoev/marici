{-# OPTIONS --safe --cubical --guardedness #-}
module DGHistoryEditPolicy where

open import Cubical.Foundations.Prelude
open import DGFrameUpdates
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution

-- A policy wrapper around the DERIVED DG exact edit. Permissions, support and
-- budget remain explicit inputs. No arbitrary observation is silently declared
-- invariant and no fresh seed for the computed output is manufactured.
module Policy (A : FrameAlgebra)
  (S : Whole.Universe.Complete ℓ-zero → Type₁)
  (Readout Cost : Type) where
  open FrameAlgebra A
  module U = Updates A
  open U using (Frame; exact-edit)
  open U.Frame
  open Whole.Universe ℓ-zero hiding (retained)
  open Resolution.Generators ℓ-zero

  frame-package : Frame → Complete
  frame-package f = pack (atom Frame) f

  module Declared (observe : Frame → Readout)
    (Allowed : Frame → D2 → Cost → Type) where

    record Ticket : Type₁ where
      constructor ticket
      field
        before : Frame
        parent : Resolve S (frame-package before)
        generator : D2
        cost : Cost
        permission : Allowed before generator cost
        readout-witness : observe before ≡ observe (exact-edit before generator)
    open Ticket public

    after : Ticket → Frame
    after t = exact-edit (before t) (generator t)

    -- Both unit equations and triangle follow from exact-edit, not fields
    -- requested anew from the policy caller.
    after-unit-u : (t : Ticket)
      → delta1 (u (after t)) ≡ sub0 (m00 (r (after t)) (d (after t))) one
    after-unit-u t = unit-u (after t)

    after-unit-v : (t : Ticket)
      → delta1 (v (after t)) ≡ sub0 (m00 (d (after t)) (r (after t))) one
    after-unit-v t = unit-v (after t)

    after-triangle : (t : Ticket)
      → delta2 (W (after t)) ≡ U.T.boundary (d (after t)) (u (after t)) (v (after t))
    after-triangle t = triangle (after t)

    readout-preserved : (t : Ticket) → observe (before t) ≡ observe (after t)
    readout-preserved = readout-witness

    -- Retention at the next universe keeps the actual original derivation
    -- together with the computed result and all permission/readout evidence.
    retained : Ticket → Whole.Universe.Complete (ℓ-suc ℓ-zero)
    retained t = Whole.Universe.pack
      (Whole.Universe.atom (Σ Ticket (λ _ → Frame))) (t , after t)

    recover-parent : (t : Ticket)
      → parent (fst (Whole.Universe.value (retained t))) ≡ parent t
    recover-parent t = refl

    recover-cost : (t : Ticket)
      → cost (fst (Whole.Universe.value (retained t))) ≡ cost t
    recover-cost t = refl

    recover-permission : (t : Ticket)
      → permission (fst (Whole.Universe.value (retained t))) ≡ permission t
    recover-permission t = refl

    recover-result : (t : Ticket)
      → snd (Whole.Universe.value (retained t)) ≡ after t
    recover-result t = refl

  -- A useful class of readouts for which preservation is PROVED rather than
  -- supplied. Reading v or W is intentionally excluded: exact edits change
  -- those fields. Permission remains required even for these readouts.
  module FixedReadout (read-fixed : D0 → D0 → D0 → D1 → Readout)
    (Allowed : Frame → D2 → Cost → Type) where
    observe : Frame → Readout
    observe f = read-fixed (C f) (d f) (r f) (u f)

    module Checked = Declared observe Allowed

    preserve : (f : Frame) (z : D2) → observe f ≡ observe (exact-edit f z)
    preserve f z = refl

    admit : (f : Frame) → Resolve S (frame-package f)
      → (z : D2) (cost : Cost) → Allowed f z cost → Checked.Ticket
    admit f parent z cost permission =
      Checked.ticket f parent z cost permission (preserve f z)
