{-# OPTIONS --safe --cubical --guardedness #-}
module SeedGeometricResponseState where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism using (Iso)
open import Cubical.Foundations.Path using (compPathrEquiv; compPathlEquiv)
open import Cubical.Foundations.GroupoidLaws using (lUnit; assoc)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (notEquiv; true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Maybe.Base using (just)
import ActualSeedEndpointTable as Seed
import SeedSeamPathComparisonBoundary as Paths
import SeedTetrahedronBridge as Geometry
import SeedFaceObstruction as ForwardProbe
import SeedFirstReturnActions as Actions
import SeedPortResponseDescentGate as Gate
import BoundaryGeneratedQuestions as Native
import WholePackageSigmaPi as Whole
import RetainedTransportResolution as Transport

open Seed using (Vertex; Occurrence; source; target; A; B; C; D; AB; BC; CA; AD; DB; BA)
open Geometry using (Realization; node; edge)

-- A source-defined reversible state in the ALREADY DECLARED free geometric
-- interpretation. It is not a finite matrix state or physical excitation.
State : Vertex → Type
State v = node A ≡ node v

edge-equiv : (e : Occurrence) → State (source e) ≃ State (target e)
edge-equiv e = compPathrEquiv (edge e)

advance : (e : Occurrence) → State (source e) → State (target e)
advance e = equivFun (edge-equiv e)

cancel : (e : Occurrence) (x y : State (source e)) → advance e x ≡ advance e y → x ≡ y
cancel e x y p = sym (Iso.leftInv iso x) ∙ cong (Iso.inv iso) p ∙ Iso.leftInv iso y
  where iso = equivToIso (edge-equiv e)

module Response = Actions.Effects State advance
module PortGate = Gate.Gate State advance cancel

-- Existing interpretation executes actual occurrences in chronological order.
-- Directed histories remain separately attached by Response.returned.
forward-direct : Response.run Paths.x0 refl ≡ edge AB
forward-direct = sym (lUnit (edge AB))
forward-indirect : Response.run Paths.x1 refl ≡ edge AD ∙ edge DB
forward-indirect = cong (λ p → p ∙ edge DB) (sym (lUnit (edge AD)))

forward-distinct : Response.run Paths.x0 refl ≡ Response.run Paths.x1 refl → ⊥
forward-distinct p = ForwardProbe.no-forward-face
  (sym forward-indirect ∙ sym p ∙ forward-direct)

-- A mathematical separator for the independent BA occurrence, not a new
-- physical response assignment. Other primitive edges preserve this fiber.
ReturnProbe : Realization → Type
ReturnProbe (node v) = Bool
ReturnProbe (edge AB i) = Bool
ReturnProbe (edge BC i) = Bool
ReturnProbe (edge CA i) = Bool
ReturnProbe (edge AD i) = Bool
ReturnProbe (edge DB i) = Bool
ReturnProbe (edge BA i) = ua notEquiv i

return-direct-reading : subst ReturnProbe (edge BA) false ≡ true
return-direct-reading = uaβ notEquiv false
return-indirect-reading : subst ReturnProbe (edge BC ∙ edge CA) false ≡ false
return-indirect-reading = substComposite ReturnProbe (edge BC) (edge CA) false
  ∙ cong (subst ReturnProbe (edge CA)) (transportRefl false) ∙ transportRefl false

return-paths-distinct : edge BA ≡ edge BC ∙ edge CA → ⊥
return-paths-distinct p = true≢false
  (sym return-direct-reading ∙ cong (λ q → subst ReturnProbe q false) p ∙ return-indirect-reading)

ba-not-reverse-ab : edge BA ≡ sym (edge AB) → ⊥
ba-not-reverse-ab p = true≢false
  (sym return-direct-reading ∙ cong (λ q → subst ReturnProbe q false) p ∙ transportRefl false)

-- Use an ACTUAL based state at B, namely the independent AB edge.
-- Cancel its common prefix, rather than identifying BA with reverse AB.
return-distinct : Response.run Paths.y0 (edge AB) ≡ Response.run Paths.y1 (edge AB) → ⊥
return-distinct p = return-paths-distinct
  (sym (Iso.leftInv prefix (edge BA))
    ∙ cong (Iso.inv prefix) (p ∙ sym (assoc (edge AB) (edge BC) (edge CA)))
    ∙ Iso.leftInv prefix (edge BC ∙ edge CA))
  where prefix = equivToIso (compPathlEquiv (edge AB))

not-a-port-response : PortGate.PortCompatible → ⊥
not-a-port-response compatible = forward-distinct (PortGate.forward-comparison compatible refl)

-- Native comparison boundary: the actual equivalence moves the current
-- marked value to its computed successor. No parallel-path equality needed.
open Whole.Universe ℓ-zero
at : (v : Vertex) → State v → Complete
at v p = pack (atom (State v)) p

filler : (e : Occurrence) (p : State (source e))
  → Native.Filler (at (source e) p) (at (target e) (advance e p))
filler e p = edge-equiv e , refl

-- Reuse the source-only RETAINED UNARY EXTENSION explicitly. This is not
-- claimed to be derivable from the unchanged original Resolve signature.
module T = Transport.Extension ℓ-zero
module OneStep (e : Occurrence) (p : State (source e)) where
  input = at (source e) p
  R = atom (State (target e))
  OnlyInput : Complete → Type₁
  OnlyInput q = q ≡ input
  root : T.ResolveT OnlyInput input
  root = T.seedT refl
  output = T.transported input R (edge-equiv e)
  execution : T.ResolveT OnlyInput output
  execution = T.transportT input R (edge-equiv e) root
  one-seed : T.TransportOnly execution
  one-seed = T.one-step input R (edge-equiv e) root (T.one-seed refl)
  previous-preserved : T.previous output ≡ just input
  previous-preserved = T.previous-retained input R (edge-equiv e)
  computed-value : value output ≡ advance e p
  computed-value = T.computed-value input R (edge-equiv e)

-- Execute a supplied typed seed word through the SAME retained extension.
-- The view exposes the current value type without unwrapping its predecessor
-- packet. Every step retains its exact input, and no target seed is added.
module RunFrom (start : Vertex) (initial : State start) where
  input = at start initial
  OnlyInput : Complete → Type₁
  OnlyInput q = q ≡ input

  record Running (v : Vertex) : Type₁ where
    constructor running
    field
      packet : Complete
      view : El (expression packet) ≃ State v
      history : T.ResolveT OnlyInput packet
      single-source : T.TransportOnly history
  open Running

  current : {v : Vertex} → Running v → State v
  current r = equivFun (view r) (value (packet r))

  root : Running start
  root = running input (idEquiv _) (T.seedT refl) (T.one-seed refl)

  step-native : (e : Occurrence) → Running (source e) → Running (target e)
  step-native e r = running next (idEquiv _)
    (T.transportT (packet r) R map (history r))
    (T.one-step (packet r) R map (history r) (single-source r))
    where
    R = atom (State (target e))
    map = compEquiv (view r) (edge-equiv e)
    next = T.transported (packet r) R map

  step-value : (e : Occurrence) (r : Running (source e))
    → current (step-native e r) ≡ advance e (current r)
  step-value e r = refl

  step-parent : (e : Occurrence) (r : Running (source e))
    → T.previous (packet (step-native e r)) ≡ just (packet r)
  step-parent e r = T.previous-retained (packet r) (atom (State (target e)))
    (compEquiv (view r) (edge-equiv e))

  execute : {s t : Vertex} → Paths.Path s t → Running s → Running t
  execute Paths.stop r = r
  execute (Paths.step e rest) r = execute rest (step-native e r)

  execute-value : {s t : Vertex} (p : Paths.Path s t) (r : Running s)
    → current (execute p r) ≡ Response.run p (current r)
  execute-value Paths.stop r = refl
  execute-value (Paths.step e rest) r = execute-value rest (step-native e r)

  record RetainedRun (t : Vertex) : Type₁ where
    constructor retained-run
    field
      route : Paths.Path start t
      native : Running t
      effect-agrees : current native ≡ Response.run route initial

  run : {t : Vertex} → Paths.Path start t → RetainedRun t
  run p = retained-run p (execute p root) (execute-value p root)

  route-retained : {t : Vertex} (p : Paths.Path start t) → RetainedRun.route (run p) ≡ p
  route-retained p = refl

module FromA = RunFrom A refl
module FromB = RunFrom B (edge AB)

native-forward-distinct : FromA.current (FromA.RetainedRun.native (FromA.run Paths.x0))
  ≡ FromA.current (FromA.RetainedRun.native (FromA.run Paths.x1)) → ⊥
native-forward-distinct p = forward-distinct
  (sym (FromA.RetainedRun.effect-agrees (FromA.run Paths.x0))
    ∙ p ∙ FromA.RetainedRun.effect-agrees (FromA.run Paths.x1))

native-return-distinct : FromB.current (FromB.RetainedRun.native (FromB.run Paths.y0))
  ≡ FromB.current (FromB.RetainedRun.native (FromB.run Paths.y1)) → ⊥
native-return-distinct p = return-distinct
  (sym (FromB.RetainedRun.effect-agrees (FromB.run Paths.y0))
    ∙ p ∙ FromB.RetainedRun.effect-agrees (FromB.run Paths.y1))

-- Scope: free geometric state + retained directed provenance. No filled
-- tetrahedron, comparison of unequal effects, finite truncation, scalar
-- mixed reader, physical units, intended T9, or matrix J4 is supplied.
