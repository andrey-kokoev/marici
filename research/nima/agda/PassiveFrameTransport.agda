{-# OPTIONS --safe --cubical --guardedness #-}
module PassiveFrameTransport where
------------------------------------------------------------------------
-- PassiveFrameTransport.agda
--
-- Operational interpretation of "Passive frame change" (frame.passive
-- in the comparison-successor contract) as a native compare-rule
-- application, following the pattern of
-- BoundaryGeneratedQuestions.Application.perform.
--
-- A FramePackage is modelled as a Complete package (the frame's
-- carrier and value) together with a Filler (the frame equivalence
-- with pointed witness).  A passive frame change applies the filler
-- via compare-rule to transport the frame, following the existing
-- checked Agda construction in BoundaryGeneratedQuestions.
--
-- This demonstrates the interpretation pattern for one of the nine
-- comparison-successor contract operations.  The remaining eight rows
-- follow the same structure: define the typed data as a Complete +
-- Filler/Family, apply the corresponding native rule via seed/apply,
-- and verify the preservation laws.
------------------------------------------------------------------------

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Sigma.Base using (_×_; fst; snd)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import BoundaryGeneratedQuestions as B

module Interpretation where
  open Whole.Universe ℓ-zero
  open Resolution.Generators ℓ-zero

  -- A FramePackage is a Complete package (carrier + value) together
  -- with a frame equivalence Filler a a (equivalence + pointed witness
  -- that the equivalence maps value a to itself).
  record FramePackage : Type (ℓ-suc ℓ-zero) where
    constructor pack
    field
      carrier : Complete
      frame-equiv : B.Filler carrier carrier
  open FramePackage public

  -- The passive frame change operation:
  -- Given a FramePackage and a derivation for its carrier,
  -- apply the compare-rule to produce the comparison package
  -- that records the frame-equivalence transport.
  module Passive (S : Complete → Type (ℓ-suc ℓ-zero)) where
    module App = B.Application S

    change : (fp : FramePackage) (da : Resolve S (carrier fp))
      → Resolve S (output (compare-rule
           (carrier fp) (carrier fp)
           (fst (frame-equiv fp)) (snd (frame-equiv fp))))
    change fp da =
      App.perform {a = carrier fp} {b = carrier fp}
        (frame-equiv fp) da da
