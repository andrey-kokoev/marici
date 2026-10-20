{-# OPTIONS --safe --cubical --guardedness #-}
module SourceCertifiedCoherentAssembly where

open import Cubical.Foundations.Prelude
open import Cubical.Data.List.Base using (List; []; _∷_; map)
open import Cubical.Data.Maybe.Base using (just)
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Relation.Nullary.Base using (¬_)
open import NativeExtensionFamilyAudit using (Vertex; A; B; AB; Seeds; pointQ)
open import InternalSourceComparisons using (Mode; act; stay; exchange)
import GeneratedReaderClassification as G
import ForwardCertifiedPrograms as P
import CertifiedFramedCells as Cell
import CertifiedContinuationPolicies as Policy
import ContinuationPolicyFamily as Tags
import FiniteComparisonTrees as F
import MixedComparisonTrees as M
import MixedHistoryCertificates as History
import CertifiedMixedHistoryOrigins as Mixed
import CertifiedMixedRootHigher as Higher
import MixedRootHistoryCoherence as Root
import InternalComparisonInterchange as Native
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero hiding (output)

data AllEvidence : List Higher.Program → Type₁ where
  nilE : AllEvidence []
  _∷E_ : {p : Higher.Program} {ps : List Higher.Program}
    → Higher.ProgramEvidence p → AllEvidence ps → AllEvidence (p ∷ ps)
infixr 5 _∷E_

-- One actual source/cell/request context, not a collection of independent
-- successes. Supplied compatible cells are certified against computed ones.
module Context (m : Mode) {v : Vertex} (a : G.Fragment v) (b : G.Fragment (act m v))
  (ca : P.Certificate a) (cb : P.Certificate b) (f : G.Comparisons.Filler m a b)
  (r : Policy.Model.Request m a b f) where
  module Model = Policy.Model m a b f
  target : F.Object
  target = fst (Model.F.S.route r) , Model.targetFragment r
  targetOrigin : P.Certificate (snd target)
  targetOrigin = Policy.target-certificate m ca cb f r
  targetClosure : Closure Seeds
  targetClosure = Native.closure (fst target , G.body (snd target))
  raw : Tags.Presentation → Closure Seeds
  raw k = Native.closure (Model.value r k Policy.output)

  record Binding (k : Tags.Presentation) : Type₁ where
    field
      cellOrigin : Cell.Certificate (F.from-generated m a b f)
      output : Policy.Certificate (Model.value r k Policy.output)
      bridge : Policy.Certificate (Model.value r k Policy.comparison)
      generatedTarget : P.Certificate (snd target)
      target-is-actual : raw Tags.target ≡ targetClosure
      bridge-inputs : Native.comparisonOperands (Policy.native (Policy.Certificate.producer bridge))
        ≡ just (raw k , targetClosure)
      -- This is an ADDITIONAL chosen-tag condition, not source selection.
      chosen-tag : isContr (Σ[ tag ∈ Tags.Presentation ] tag ≡ k)
  bind : (k : Tags.Presentation) → Binding k
  Binding.cellOrigin (bind k) = Cell.certify ca cb (F.from-generated m a b f)
  Binding.output (bind k) = Policy.certify m ca cb f r k Policy.output
  Binding.bridge (bind k) = Policy.certify m ca cb f r k Policy.comparison
  Binding.generatedTarget (bind k) = targetOrigin
  Binding.target-is-actual (bind k) = refl
  Binding.bridge-inputs (bind k) = Policy.comparison-operands m ca cb f r k
  Binding.chosen-tag (bind k) = Tags.selected-tag k
  port-only-not-unique : ¬ isProp (Model.F.PortChoices (λ _ → Unit) r)
  port-only-not-unique = Model.F.port-task-does-not-select (λ _ → Unit) r tt

  -- The source endpoint below IS the actual policy target, including its
  -- native history. No fresh seed or raw-presentation-as-Fragment cast.
  module Continuations {n : Mode} {z : F.Object} (t u w : Higher.Tree n target z) where
    first : Higher.Boundary t w
    first = Higher.direct t w
    composed : Higher.Boundary t w
    composed = Higher.compose (Higher.direct t u) (Higher.direct u w)
    via : Higher.Boundary t w
    via = Higher.compose (Higher.direct t t) (Higher.direct t w)
    module Q = Root.Higher (Higher.Tree.tree t) (Higher.Tree.tree w)
    actualHigher : List (Closure Seeds)
    actualHigher = Higher.rootClosure t w (Higher.evaluate first)
      ∷ (Q.E.encoded (Higher.evaluate first) , Q.E.native (Higher.evaluate first))
      ∷ Higher.triangleClosure t u w ∷ Higher.Square.closure composed first via ∷ []
    programs : List Higher.Program
    programs = Higher.compareP first ∷ Higher.envelopeP first
      ∷ Higher.triangleProgram t u w ∷ Higher.squareP composed first via ∷ []
    programs-match : map Higher.native programs ≡ actualHigher
    programs-match = refl
    all-inputs : AllEvidence programs
    all-inputs = Higher.programEvidence (Higher.compareP first)
      ∷E Higher.programEvidence (Higher.envelopeP first)
      ∷E Higher.programEvidence (Higher.triangleProgram t u w)
      ∷E Higher.programEvidence (Higher.squareP composed first via) ∷E nilE

    compiled-inputs : (x : Higher.Tree n target z)
      → Native.comparisonOperands (History.endClosure (M.fold (Higher.Tree.tree x)))
        ≡ just (targetClosure , Native.closure (fst z , G.body (snd z)))
    compiled-inputs x = refl

    record Assembly (k : Tags.Presentation) : Type₁ where
      field
        policy : Binding k
        left : Mixed.CertifiedTree (Higher.Tree.tree t)
        middle : Mixed.CertifiedTree (Higher.Tree.tree u)
        right : Mixed.CertifiedTree (Higher.Tree.tree w)
        left-packet : map Mixed.native (Mixed.compileList (Mixed.CertifiedTree.nodes left))
          ≡ map Native.closure (Mixed.packet (Higher.Tree.tree t))
        middle-packet : map Mixed.native (Mixed.compileList (Mixed.CertifiedTree.nodes middle))
          ≡ map Native.closure (Mixed.packet (Higher.Tree.tree u))
        right-packet : map Mixed.native (Mixed.compileList (Mixed.CertifiedTree.nodes right))
          ≡ map Native.closure (Mixed.packet (Higher.Tree.tree w))
        higherPrograms : List Higher.Program
        higher-matches : map Higher.native higherPrograms ≡ actualHigher
        higher-inputs : AllEvidence higherPrograms
        actual-continuation-inputs : (x : Higher.Tree n target z)
          → Native.comparisonOperands (History.endClosure (M.fold (Higher.Tree.tree x)))
            ≡ just (targetClosure , Native.closure (fst z , G.body (snd z)))
        actual-root-inputs : Native.comparisonOperands (Higher.native (Higher.compareP first))
          ≡ just (Native.closure (fst z , History.root (Higher.Tree.tree t))
                 , Native.closure (fst z , History.root (Higher.Tree.tree w)))
    assemble : (k : Tags.Presentation) → Assembly k
    Assembly.policy (assemble k) = bind k
    Assembly.left (assemble k) = Higher.bundle t
    Assembly.middle (assemble k) = Higher.bundle u
    Assembly.right (assemble k) = Higher.bundle w
    Assembly.left-packet (assemble k) = Mixed.list-match (Mixed.CertifiedTree.nodes (Higher.bundle t))
    Assembly.middle-packet (assemble k) = Mixed.list-match (Mixed.CertifiedTree.nodes (Higher.bundle u))
    Assembly.right-packet (assemble k) = Mixed.list-match (Mixed.CertifiedTree.nodes (Higher.bundle w))
    Assembly.higherPrograms (assemble k) = programs
    Assembly.higher-matches (assemble k) = programs-match
    Assembly.higher-inputs (assemble k) = all-inputs
    Assembly.actual-continuation-inputs (assemble k) = compiled-inputs
    Assembly.actual-root-inputs (assemble k) = Higher.operands-recovered first

  -- An inhabited continuation family on THIS actual target, not another
  -- root. It includes core composition and a mixed composition.
  identity : Higher.Tree stay target target
  identity = Higher.checked (M.old (F.unit target)) targetOrigin
  core : Higher.Tree stay target target
  core = Higher.checked (M.old (F.then (F.unit target) (F.unit target))) (targetOrigin , targetOrigin)
  mixed : Higher.Tree stay target target
  mixed = Higher.checked (M.join (Higher.Tree.tree core) (Higher.Tree.tree identity))
    ((targetOrigin , targetOrigin) , targetOrigin)
  module Default = Continuations identity core mixed
  default-assembly : (k : Tags.Presentation) → Default.Assembly k
  default-assembly = Default.assemble

-- A computed front door: no supplied full filler or synchronization path.
module Closed (m : Mode) {v : Vertex} (p : P.Program v) (q : P.Program (act m v))
  (ok : P.Pair.Guard m p q) (s : Policy.Compiled.Control m p q ok) where
  module C = Policy.Compiled m p q ok
  module Bound = Context m (P.decode p) (P.decode q) (P.certificate p refl) (P.certificate q refl)
    C.filler (C.R.synchronize s)

module Regression = Closed exchange (P.initialP (P.rootI A)) (P.initialP (P.rootI B)) refl (B , AB)

-- Exact original forward witnesses instantiate the SAME assembled context.
module Forward (d : Resolve Seeds (pointQ A)) (c0 : P.InitialCertificate A d) where
  module D = P.Diagram d c0
  module Inputs = Policy.Model stay D.D.source D.D.target D.D.sequential
  module At (r : Inputs.Request) = Context stay D.D.source D.D.target
    D.source-certificate D.target-certificate D.D.sequential r
