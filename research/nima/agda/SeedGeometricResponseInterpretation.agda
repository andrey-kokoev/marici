{-# OPTIONS --safe --cubical --guardedness #-}
module SeedGeometricResponseInterpretation where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism using (Iso)
open import Cubical.Foundations.Path using (compPathr-cancel)
open import Cubical.Foundations.Univalence using (ua; uaβ)
open import Cubical.Foundations.Transport using (substComposite)
import ActualSeedEndpointTable as Seed
import SeedSeamPathComparisonBoundary as Paths
import SeedTetrahedronBridge as Geometry
import SeedFirstReturnActions as Actions
import SeedGeometricResponseState as G

-- The free realization has no face equations to obstruct this interpretation.
-- Edge equivalences and initial response are EXPLICIT interpretation inputs.
module Interpret (X : Seed.Vertex → Type)
  (edge-map : (e : Seed.Occurrence) → X (Seed.source e) ≃ X (Seed.target e))
  (initial : X Seed.A) where

  Family : Geometry.Realization → Type
  Family (Geometry.node v) = X v
  Family (Geometry.edge e i) = ua (edge-map e) i

  read : {v : Seed.Vertex} → G.State v → X v
  read p = subst Family p initial

  act : (e : Seed.Occurrence) → X (Seed.source e) → X (Seed.target e)
  act e = equivFun (edge-map e)

  primitive-square : (e : Seed.Occurrence) (p : G.State (Seed.source e))
    → read (G.advance e p) ≡ act e (read p)
  primitive-square e p = substComposite Family p (Geometry.edge e) initial
    ∙ uaβ (edge-map e) (read p)

  -- Geometric inverses are available in the declared realization. This
  -- theorem does not add inverse occurrences to the directed seed alphabet.
  inverse-square : (e : Seed.Occurrence) (p : G.State (Seed.target e))
    → read (p ∙ sym (Geometry.edge e)) ≡ equivFun (invEquiv (edge-map e)) (read p)
  inverse-square e p = sym (Iso.leftInv iso (read (p ∙ sym (Geometry.edge e))))
    ∙ cong (Iso.inv iso)
      (sym (primitive-square e (p ∙ sym (Geometry.edge e)))
        ∙ cong read (compPathr-cancel (Geometry.edge e) p))
    where iso = equivToIso (edge-map e)

  module E = Actions.Effects X act

  route-square : {s t : Seed.Vertex} (p : Paths.Path s t) (h : G.State s)
    → read (G.Response.run p h) ≡ E.run p (read h)
  route-square Paths.stop h = refl
  route-square (Paths.step e rest) h = route-square rest (G.advance e h)
    ∙ cong (E.run rest) (primitive-square e h)

  base-reading : read (refl {x = Geometry.node Seed.A}) ≡ initial
  base-reading = transportRefl initial

  native-square : {t : Seed.Vertex} (p : Paths.Path Seed.A t)
    → read (G.FromA.current (G.FromA.RetainedRun.native (G.FromA.run p))) ≡ E.run p initial
  native-square p = cong read (G.FromA.RetainedRun.effect-agrees (G.FromA.run p))
    ∙ route-square p refl ∙ cong (E.run p) base-reading

-- This universal theorem does not select X, edge-map, or initial. Numerical
-- matrix instances require invertibility and their own representation check.
-- Directed route provenance stays in the native packet even if read is coarse.
