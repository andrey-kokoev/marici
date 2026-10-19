{-# OPTIONS --safe --cubical --guardedness #-}
module SeedArrivalContinuationQuotient where

open import Cubical.Foundations.Prelude hiding (Path)
open import Cubical.Data.Sigma.Base using (_×_)
import ActualSeedEndpointTable as Seed
import SeedSeamPathComparisonBoundary as Paths
import SeedFirstReturnActions as Actions
import SeedArrivalEffects as Arrival
import SeedJointQuestionReadout as JointRead
import SeedTriangleJointContext as Joint

open Seed using (Vertex; Occurrence; A; AB; BC; CA; AD; DB; BA)
open Paths using (Path; stop; step)

-- The observer and continuation law are the EXISTING Effects instance.
-- This module derives their exact contextual quotient, not a new policy.
module From (initial : Arrival.Arrival A) where
  observe : {v : Vertex} → Path A v → Arrival.Arrival v
  observe p = Arrival.Read.run p initial

  continuation-square : {v w : Vertex} (p : Path A v) (k : Path v w)
    → observe (Actions.append p k) ≡ Arrival.Read.run k (observe p)
  continuation-square p k = Arrival.Read.run-append p k initial

  -- All typed finite future paths are quantified over, not just a sample
  -- or the two original triangle words. Empty continuation is included.
  FutureEqual : {v : Vertex} → Path A v → Path A v → Type
  FutureEqual {v} p q = (w : Vertex) (k : Path v w)
    → observe (Actions.append p k) ≡ observe (Actions.append q k)

  current-to-future : {v : Vertex} (p q : Path A v)
    → observe p ≡ observe q → FutureEqual p q
  current-to-future p q equal w k = continuation-square p k
    ∙ cong (Arrival.Read.run k) equal ∙ sym (continuation-square q k)

  future-to-current : {v : Vertex} (p q : Path A v)
    → FutureEqual p q → observe p ≡ observe q
  future-to-current {v} p q equal = sym (continuation-square p stop)
    ∙ equal v stop ∙ continuation-square q stop

  -- Every factorization of the current arrival observation through another
  -- summary forces equality of that summary to imply FutureEqual. This is
  -- minimality for this fixed task, not physical/minimal-memory selection.
  summary-sufficient : {v : Vertex} {S : Type}
    (summarize : Path A v → S) (read : S → Arrival.Arrival v)
    (correct : (p : Path A v) → read (summarize p) ≡ observe p)
    (p q : Path A v) → summarize p ≡ summarize q → FutureEqual p q
  summary-sufficient summarize read correct p q equal = current-to-future p q
    (sym (correct p) ∙ cong read equal ∙ correct q)

  -- Old collision, now given its exact operational meaning: different
  -- history lengths cannot be distinguished by ANY future arrival reading.
  repeated-ABC-future-equal : FutureEqual
    (Joint.execution Joint.ABC)
    JointRead.twice-ABC
  repeated-ABC-future-equal = current-to-future (Joint.execution Joint.ABC) JointRead.twice-ABC
    (JointRead.repeat-arrival-collision initial)

-- The quotient's primitive update is the old arrival update, with actual
-- seed endpoint typing. It overwrites the arriving occurrence; no matrix
-- values, reference inverses, normalized weights or filled faces enter.
primitive-transition : (e : Occurrence) → Arrival.Arrival (Seed.source e)
  → Arrival.Arrival (Seed.target e)
primitive-transition = Arrival.arrive

transition-reading : (e : Occurrence) (a : Arrival.Arrival (Seed.source e))
  → fst (primitive-transition e a) ≡ e
transition-reading e a = refl

-- Explicit reachable representatives show all six occurrence states are
-- present; the quotient has not silently discarded an off-triangle edge.
representative : (e : Occurrence) → Path A (Seed.target e)
representative AB = step AB stop
representative BC = step AB (step BC stop)
representative CA = step AB (step BC (step CA stop))
representative AD = step AD stop
representative DB = step AD (step DB stop)
representative BA = step AB (step BA stop)

representative-reading : (e : Occurrence) (initial : Arrival.Arrival A)
  → Arrival.Read.run (representative e) initial ≡ (e , refl)
representative-reading AB initial = refl
representative-reading BC initial = refl
representative-reading CA initial = refl
representative-reading AD initial = refl
representative-reading DB initial = refl
representative-reading BA initial = refl

-- The new quotient never identifies retained histories as paths. The old
-- distinction is still available as soon as history-length questions are
-- admitted, rather than only current/future arrival observations.
retained-repeat-distinction = JointRead.repeat-histories-distinct
