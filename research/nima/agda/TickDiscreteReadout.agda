{-# OPTIONS --safe --cubical --guardedness #-}

-- TickDiscreteReadout.agda
--
-- What the Tick genuinely determines, proved in Agda.  The module extracts
-- a discrete readout from an actual Tick term (not a matrix model) and
-- proves its preservation laws.  It also states explicitly what structure
-- the Tick does NOT determine.
--
-- This is the bridge theorem called for in the audit: a machine-checked
-- discrete bridge from the Tick to a readout structure, with clearly
-- labeled uninterpreted data.
module TickDiscreteReadout where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (notEquiv)
open import Cubical.Data.Empty.Base using (⊥)

open import ObserverCoherenceCube as Source
open import RetainedSquareReversal as RSR
open import RetainedSquareConeClock as Tick

private variable ℓ : Level

-- ====================================================================
--  1. Discrete readout extracted from the Tick
-- ====================================================================

module Readout {O R : Type ℓ} (e : O ≃ R) (s : O × O) where
  open Source.Geometry O R e
  module Ret = RSR.Construction O R e

  module T = Tick.Bridge O R e
  open T.AtSource s renaming (Tick to ATick) public

  -- The readout records only the discrete combinatorial data that the
  -- Tick certifies.  It does NOT record any continuous or temporal data
  -- or the functional content of the return section.
  record DiscreteReadout : Type ℓ where
    constructor discrete-readout
    field
      -- The four corners of the square (heterogeneous types)
      src             : O × O
      left-int        : R × O     -- expandLeft s
      right-int       : O × R     -- expandRight s
      tgt             : R × R

      -- The ordered schedule tags actually retained by the Tick
      schedule-first  : Schedule
      schedule-second : Schedule

      -- Return endpoints: target -> source
      return-starts-at : R × R
      return-ends-at   : O × O

  open DiscreteReadout

  -- Extract a readout from an actual Tick term.
  extract : ATick -> DiscreteReadout
  extract tk = discrete-readout
    (RealizedSquare.source orig)
    (expandLeft (RealizedSquare.source orig))
    (expandRight (RealizedSquare.source orig))
    (RealizedSquare.target orig)
    (ComparedRoutes.first (RealizedSquare.comparison orig))
    (ComparedRoutes.second (RealizedSquare.comparison orig))
    (RealizedSquare.target orig)
    (RealizedSquare.source orig)
    where
    orig = Ret.RetainedReturn.original (ATick.returned tk)

  -- ====================================================================
  --  2. Preservation laws
  -- ====================================================================

  -- Source: preserved identically.
  extract-preserves-source : (t : ATick)
    -> src (extract t) ≡ RealizedSquare.source (Ret.RetainedReturn.original (ATick.returned t))
  extract-preserves-source t = refl

  -- The retained source is attached to the source parameter of this module.
  extract-source-attached : (t : ATick) -> src (extract t) ≡ s
  extract-source-attached t = ATick.attachment t

  -- Left intermediate = expandLeft(source).
  extract-preserves-left-int : (t : ATick)
    -> left-int (extract t) ≡ expandLeft (src (extract t))
  extract-preserves-left-int t = refl

  -- Right intermediate = expandRight(source).
  extract-preserves-right-int : (t : ATick)
    -> right-int (extract t) ≡ expandRight (src (extract t))
  extract-preserves-right-int t = refl

  extract-preserves-first-schedule : (t : ATick)
    -> schedule-first (extract t) ≡ ComparedRoutes.first
         (RealizedSquare.comparison (Ret.RetainedReturn.original (ATick.returned t)))
  extract-preserves-first-schedule t = refl

  extract-preserves-second-schedule : (t : ATick)
    -> schedule-second (extract t) ≡ ComparedRoutes.second
         (RealizedSquare.comparison (Ret.RetainedReturn.original (ATick.returned t)))
  extract-preserves-second-schedule t = refl

  -- Target = run(leftFirst, source) = run(rightFirst, source).
  extract-target-equals-run : (t : ATick)
    -> (run (ComparedRoutes.first (RealizedSquare.comparison (Ret.RetainedReturn.original (ATick.returned t))))
           (RealizedSquare.source (Ret.RetainedReturn.original (ATick.returned t))) ≡
         RealizedSquare.target (Ret.RetainedReturn.original (ATick.returned t)))
     × (run (ComparedRoutes.second (RealizedSquare.comparison (Ret.RetainedReturn.original (ATick.returned t))))
           (RealizedSquare.source (Ret.RetainedReturn.original (ATick.returned t))) ≡
         RealizedSquare.target (Ret.RetainedReturn.original (ATick.returned t)))
  extract-target-equals-run t = (first-component , second-component)
    where
    orig = Ret.RetainedReturn.original (ATick.returned t)
    cmp : ComparedRoutes
    cmp = RealizedSquare.comparison orig
    source-value : O × O
    source-value = RealizedSquare.source orig
    target-value : R × R
    target-value = RealizedSquare.target orig
    first-component : run (ComparedRoutes.first cmp) source-value ≡ target-value
    first-component = sym (RealizedSquare.target-law orig)
    route-equality : run (ComparedRoutes.first cmp) source-value ≡ run (ComparedRoutes.second cmp) source-value
    route-equality = cong (λ (f : O × O → R × R) → f source-value) (ComparedRoutes.witness cmp)
    second-component : run (ComparedRoutes.second cmp) source-value ≡ target-value
    second-component = sym route-equality ∙ first-component

  -- The extracted endpoints agree with the actual retained return section.
  extract-return-starts-at-target : (t : ATick)
    -> Ret.RetainedReturn.return-section (ATick.returned t) i0 i0
       ≡ return-starts-at (extract t)
  extract-return-starts-at-target t = Ret.RetainedReturn.start-law (ATick.returned t)

  extract-return-ends-at-source : (t : ATick)
    -> Ret.RetainedReturn.return-section (ATick.returned t) i1 i1
       ≡ return-ends-at (extract t)
  extract-return-ends-at-source t = Ret.RetainedReturn.end-law (ATick.returned t)

  -- ====================================================================
  --  3. What the readout does NOT capture
  -- ====================================================================

  -- The readout does NOT record:
  --
  -- (a) The Agda-level witness certificate (ComparedRoutes.witness).
  --     Its consequence is used in extract-target-equals-run, but neither
  --     the path nor its proof term is stored in DiscreteReadout.
  --
  -- (b) The return section as a function (i j : I) -> backward-cell i j.
  --     Only its start and end points are recorded.
  --
  -- (c) The source attachment proof term itself. Its consequence is
  --     available as extract-source-attached, but the proof term is not
  --     stored in the readout.
  --
  -- (d) Any continuous or temporal data.
  --     No rate, duration, or intermediate states are recorded.
  --
  -- (e) The parameterization by O, R, e.
  --     The readout works for any equivalence, but the specific choice
  --     is not reflected in the readout structure.

  -- ====================================================================
  --  4. Summary
  -- ====================================================================

  -- The discrete readout records:
  --   - Four corners of the square
  --   - The two ordered schedule tags from the retained comparison
  --   - Return endpoints (target, source)
  --
  -- The readout omits the following full structure:
  --   - The comparison witness proof term
  --   - The return section function (i j : I -> backward-cell i j), beyond
  --     its two endpoints
  --   - The source attachment certificate
  --   - Any continuous data
  --
  -- To determine a continuous evolution from the readout, the following
  -- additional data are needed beyond what the Tick supplies:
  --
  --   1. A concrete representation of O and R (e.g., Hilbert space).
  --   2. An interpretation of expandLeft/expandRight as unitary operators.
  --   3. A choice of continuous interpolation between the discrete corners.
  --   4. A notion of time/rate along the chosen continuous path.
  --
  -- None of these are provided by the Tick's type-level structure.
  -- ====================================================================

-- ====================================================================
--  5. Concrete Bool instance: non-uniqueness example
-- ====================================================================

-- The standard and swapped Bool ticks have different ordered schedule
-- tags, and extraction preserves that difference.
module BoolInst = Readout {ℓ = ℓ-zero} {O = Bool} {R = Bool} notEquiv (false , false)
module BoolGeometry = Source.Geometry Bool Bool notEquiv

fresh-first : BoolInst.DiscreteReadout.schedule-first (BoolInst.extract BoolInst.fresh) ≡ BoolGeometry.leftFirst
fresh-first = refl

swapped-first : BoolInst.DiscreteReadout.schedule-first (BoolInst.extract BoolInst.swapped) ≡ BoolGeometry.rightFirst
swapped-first = refl

ticks-distinct : BoolInst.fresh ≡ BoolInst.swapped -> ⊥
ticks-distinct = BoolInst.schedule-records-distinct