{-# OPTIONS --safe --cubical --guardedness #-}
module OriginalRuleGeometricCompiler where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Foundations.Equiv using (_≃_)
open import Cubical.Data.Bool using (Bool; true; false; true≢false; isSetBool)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Unit using (Unit; tt)
open import ObserverAdmissibleImages using (ImageFactors)
import ObserverSetImageDescent as Descent
open import Cubical.Data.Maybe using (Maybe; just; nothing)
open import ActualSeedEndpointTable hiding (seed)
import WholePackageSigmaPi as Whole
import WholePackageResolution as Resolution
import NativeExtensionFamilyAudit as N
import SourceGraphFreeRealization as SourceBinding
import SeedSeamPathComparisonBoundary as W
import SeedFirstReturnActions as Actions
import SeedGeometricResponseState as G
import TransportObservationPartialCorrespondence as Partial
import OriginalTransportShapeObstruction as Obstruction
open Whole.Universe ℓ-zero
open Resolution.Generators ℓ-zero

-- Actual occurrence binding, not identification merely by vertex names.
occurrence-recovered : (e : Occurrence)
  → SourceBinding.outOfNative (SourceBinding.intoNative e) ≡ e
occurrence-recovered = SourceBinding.occurrence-section

-- All compiler leaves have the single original graph-retaining source A.
-- E arities may duplicate this ancestry; no unary/one-leaf claim is made.
OnlyA : Complete → Type₁
OnlyA q = q ≡ N.pointQ N.A
into-original : (q : Complete) → OnlyA q → N.Seeds q
into-original q p = subst N.Seeds (sym p) (N.source N.A)

-- Internal evaluator interface. The closed public front door below takes
-- only a typed source word, not a Running value, Type, Body or equivalence.
record Running (v : Vertex) : Type₁ where
  constructor running
  field
    packet : Complete
    ancestry : Resolve OnlyA packet
    decode : El (expression packet) → G.State v
open Running
current : {v : Vertex} → Running v → G.State v
current r = decode r (value (packet r))
native : {v : Vertex} (r : Running v) → Resolve N.Seeds (packet r)
native r = mapSeeds into-original (ancestry r)

-- Computed E/reflexivity family. Every branch consumes the actual parent.
branch : Complete → Complete
branch q = path-package (expression q) (value q) (value q) refl
branch-derived : {q : Complete} → Resolve OnlyA q → Resolve OnlyA (branch q)
branch-derived {q} d = apply (reflexivity-rule (expression q) (value q)) (λ _ → d)
root : Running A
root = running (E-package (G.State A) (λ _ → branch (N.pointQ N.A)) refl)
  (apply (E-rule (G.State A) (λ _ → branch (N.pointQ N.A)) refl)
    (λ _ → branch-derived (seed refl))) fst
step : (e : Occurrence) → Running (source e) → Running (target e)
step e r = running (E-package (G.State (target e)) (λ _ → branch (packet r)) next)
  (apply (E-rule (G.State (target e)) (λ _ → branch (packet r)) next)
    (λ _ → branch-derived (ancestry r))) fst
  where next = G.advance e (current r)

-- Recover the actual ORIGINAL native premise, including its derivation.
reflexive-parent : {q : Complete} → Resolve N.Seeds q → Maybe (Closure N.Seeds)
reflexive-parent (apply (reflexivity-rule Q x) ds) = just (pack Q x , ds (lift tt))
reflexive-parent _ = nothing
previous : {q : Complete} → Resolve N.Seeds q → Maybe (Closure N.Seeds)
previous (apply (E-rule I F i) ds) = reflexive-parent (ds (lift i))
previous _ = nothing
step-parent : (e : Occurrence) (r : Running (source e))
  → previous (native (step e r)) ≡ just (packet r , native r)
step-parent e r = refl
root-parent : previous (native root) ≡ just (N.pointQ N.A , N.root N.A)
root-parent = cong (λ s → just (N.pointQ N.A , seed s)) (transportRefl (N.source N.A))

execute : {s t : Vertex} → W.Path s t → Running s → Running t
execute W.stop r = r
execute (W.step e rest) r = execute rest (step e r)
execute-value : {s t : Vertex} (w : W.Path s t) (r : Running s)
  → current (execute w r) ≡ G.Response.run w (current r)
execute-value W.stop r = refl
execute-value (W.step e rest) r = execute-value rest (step e r)
execute-append : {s m t : Vertex} (p : W.Path s m) (q : W.Path m t) (r : Running s)
  → execute (Actions.append p q) r ≡ execute q (execute p r)
execute-append W.stop q r = refl
execute-append (W.step e rest) q r = execute-append rest q (step e r)

compile : {v : Vertex} → W.Path A v → Running v
compile w = execute w root
compiled-record : {v : Vertex} → W.Path A v → Σ (W.Path A v) (λ _ → Running v)
compiled-record w = w , compile w
route-recovered : {v : Vertex} (w : W.Path A v) → fst (compiled-record w) ≡ w
route-recovered w = refl
extension-agrees : {v : Vertex} (w : W.Path A v)
  → current (compile w) ≡ G.FromA.current (G.FromA.RetainedRun.native (G.FromA.run w))
extension-agrees w = execute-value w root ∙ sym (G.FromA.RetainedRun.effect-agrees (G.FromA.run w))

module Observe (v : Vertex) (probe : G.State v → Bool) where
  module P = Partial.At v probe
  read : W.Path A v → Bool
  read w = probe (current (compile w))
  agrees : (w : W.Path A v) → read w ≡ P.observed w
  agrees w = cong probe (extension-agrees w)
  -- Compatibility and separating collisions transfer to the ORIGINAL
  -- compiler's readout, without identifying the two retained packages.
  module Summary (Y : Type) (f : W.Path A v → Y) where
    module Old = P.Through Y f
    module New = Descent.Criterion f read
    module SetOutput = New.SetOutput isSetBool
    Preserves = New.Preserves
    transfer : Old.Compatible → Preserves
    transfer ok x y p = agrees x ∙ ok x y p ∙ sym (agrees y)
    refuse : Old.Collision → Preserves → ⊥
    refuse c ok = Old.Collision.separated c
      (sym (agrees (Old.Collision.left c))
       ∙ ok (Old.Collision.left c) (Old.Collision.right c) (Old.Collision.merged c)
       ∙ agrees (Old.Collision.right c))
    accept : Old.Compatible → ImageFactors f read
    accept ok = SetOutput.sufficient (transfer ok)
    no-factor : Old.Collision → ImageFactors f read → ⊥
    no-factor c factor = refuse c (New.necessary factor)

-- The native output packages are NOT the unary extension's raw packages.
module BoolProbe = Observe A Partial.probe
native-short : BoolProbe.read Partial.short ≡ true
native-short = BoolProbe.agrees Partial.short ∙ Partial.short-reading
native-long : BoolProbe.read Partial.long ≡ false
native-long = BoolProbe.agrees Partial.long ∙ Partial.long-reading
module ParityBinding = BoolProbe.Summary Bool Partial.parity
parity-factor : ImageFactors Partial.parity BoolProbe.read
parity-factor = ParityBinding.accept
  (λ x y p → Partial.native-parity x ∙ p ∙ sym (Partial.native-parity y))
module ForgetBinding = BoolProbe.Summary Unit (λ _ → tt)
no-constant-factor : ImageFactors (λ (_ : W.Path A A) → tt) BoolProbe.read → ⊥
no-constant-factor = ForgetBinding.no-factor Partial.collision

not-exact-output : {v : Vertex} (w : W.Path A v) (a : Complete)
  (X : Type) (e : El (expression a) ≃ X)
  → packet (compile w) ≡ Obstruction.T.transported a (atom X) e → ⊥
not-exact-output w a X e p = Obstruction.no-exact-transport a X e
  (subst (Resolve N.Seeds) p (native (compile w)))
