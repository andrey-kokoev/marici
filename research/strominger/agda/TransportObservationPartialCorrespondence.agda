{-# OPTIONS --safe --cubical --guardedness #-}
module TransportObservationPartialCorrespondence where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Data.Bool using (Bool; true; false; not; notEquiv; true≢false; isSetBool)
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Sigma using (_×_)
open import ActualSeedEndpointTable
open import SeedTetrahedronBridge using (edge)
import SeedSeamPathComparisonBoundary as Words
import SeedGeometricResponseState as G
open import ObserverAdmissibleImages using (Image; ImageFactors; arrive)
import ObserverSetImageDescent as Descent

-- Signature choice is explicit: G.FromA uses RetainedTransportResolution.
-- Extension. No derivation in the original twelve-rule calculus is claimed.
module At (v : Vertex) (probe : G.State v → Bool) where
  Word = Words.Path A v
  execute : Word → G.FromA.RetainedRun v
  execute = G.FromA.run
  observed : Word → Bool
  observed w = probe (G.FromA.current (G.FromA.RetainedRun.native (execute w)))
  semantic : Word → Bool
  semantic w = probe (G.Response.run w refl)
  execution-square : (w : Word) → observed w ≡ semantic w
  execution-square w = cong probe (G.FromA.RetainedRun.effect-agrees (execute w))
  word-recovered : (w : Word) → G.FromA.RetainedRun.route (execute w) ≡ w
  word-recovered = G.FromA.route-retained

  module Through (Y : Type) (summary : Word → Y) where
    module C = Descent.Criterion summary observed
    module S = C.SetOutput isSetBool
    Compatible = C.Preserves
    Factor = ImageFactors summary observed
    certify : Compatible → Factor
    certify = S.sufficient
    necessary : Factor → Compatible
    necessary = C.necessary

    -- A positive certificate carries the actual native executions too.
    record Accepted : Type₁ where
      field
        factor : Factor
        retained : (w : Word) → G.FromA.RetainedRun v
        same-execution : (w : Word) → retained w ≡ execute w
        readout-square : (w : Word)
          → fst (fst factor (arrive summary w)) ≡ observed w
    accept : Compatible → Accepted
    Accepted.factor (accept ok) = certify ok
    Accepted.retained (accept ok) = execute
    Accepted.same-execution (accept ok) w = refl
    Accepted.readout-square (accept ok) w = cong fst (snd (certify ok) w)

    -- Supplied separation is a constructive refusal, not a total decision
    -- procedure for arbitrary observers or unbounded route languages.
    record Collision : Type where
      field
        left right : Word
        merged : summary left ≡ summary right
        separated : observed left ≡ observed right → ⊥
    refuse : Collision → Factor → ⊥
    refuse c factor = Collision.separated c
      (necessary factor (Collision.left c) (Collision.right c) (Collision.merged c))

  module Full = Through Word (λ w → w)
  full-input-accepted : Full.Accepted
  full-input-accepted = Full.accept (λ x y p → cong observed p)

-- A mathematical comparison-sensitive probe already present in the prior
-- source packet. It is a declared observer, not a source-selected detector.
probe : G.State A → Bool
probe p = subst G.ReturnProbe p false
module Test = At A probe
short long : Test.Word
short = Words.step AB Words.y0
long = Words.step AB Words.y1

short-reading : Test.observed short ≡ true
short-reading = Test.execution-square short
  ∙ cong (λ p → probe (G.Response.run Words.y0 p)) G.forward-direct
  ∙ substComposite G.ReturnProbe (edge AB) (edge BA) false
  ∙ cong (subst G.ReturnProbe (edge BA)) (transportRefl false)
  ∙ G.return-direct-reading
long-reading : Test.observed long ≡ false
long-reading = Test.execution-square long
  ∙ cong (λ p → probe (G.Response.run Words.y1 p)) G.forward-direct
  ∙ substComposite G.ReturnProbe (edge AB ∙ edge BC) (edge CA) false
  ∙ cong (subst G.ReturnProbe (edge CA))
      (substComposite G.ReturnProbe (edge AB) (edge BC) false
       ∙ cong (subst G.ReturnProbe (edge BC)) (transportRefl false)
       ∙ transportRefl false)
  ∙ transportRefl false

module Forget = Test.Through Unit (λ _ → tt)
collision : Forget.Collision
Forget.Collision.left collision = short
Forget.Collision.right collision = long
Forget.Collision.merged collision = refl
Forget.Collision.separated collision p = true≢false (sym short-reading ∙ p ∙ long-reading)
no-forgotten-factor : Forget.Factor → ⊥
no-forgotten-factor = Forget.refuse collision

-- An independently computed two-state interpreter of the directed word.
-- Only the already declared BA probe transition flips its bit.
flip-edge : Occurrence → Bool → Bool
flip-edge AB b = b
flip-edge BC b = b
flip-edge CA b = b
flip-edge AD b = b
flip-edge DB b = b
flip-edge BA b = not b
edge-reading : (e : Occurrence) (b : Bool)
  → subst G.ReturnProbe (edge e) b ≡ flip-edge e b
edge-reading AB b = transportRefl b
edge-reading BC b = transportRefl b
edge-reading CA b = transportRefl b
edge-reading AD b = transportRefl b
edge-reading DB b = transportRefl b
edge-reading BA b = uaβ notEquiv b
read-state : {v : Vertex} → G.State v → Bool
read-state p = subst G.ReturnProbe p false
step-reading : (e : Occurrence) (p : G.State (source e))
  → read-state (G.advance e p) ≡ flip-edge e (read-state p)
step-reading e p = substComposite G.ReturnProbe p (edge e) false
  ∙ edge-reading e (read-state p)
run-bit : {s t : Vertex} → Words.Path s t → Bool → Bool
run-bit Words.stop b = b
run-bit (Words.step e rest) b = run-bit rest (flip-edge e b)
run-square : {s t : Vertex} (w : Words.Path s t) (p : G.State s)
  → read-state (G.Response.run w p) ≡ run-bit w (read-state p)
run-square Words.stop p = refl
run-square (Words.step e rest) p = run-square rest (G.advance e p)
  ∙ cong (run-bit rest) (step-reading e p)
parity : Test.Word → Bool
parity w = run-bit w false
native-parity : (w : Test.Word) → Test.observed w ≡ parity w
native-parity w = Test.execution-square w ∙ run-square w refl
  ∙ cong (run-bit w) (transportRefl false)
module Parity = Test.Through Bool parity
parity-accepted : Parity.Accepted
parity-accepted = Parity.accept (λ x y p → native-parity x ∙ p ∙ sym (native-parity y))
