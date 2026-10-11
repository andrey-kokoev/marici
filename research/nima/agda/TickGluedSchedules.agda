{-# OPTIONS --safe --cubical --guardedness #-}
module TickGluedSchedules where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (hProp)
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Sigma using (_×_; Σ-syntax)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.Pushout.Base using (Pushout; inl; inr; push)
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (oneCompletion)
open import TickCompletionRealization
open import TickContinuousSchedules
open import TickQuotientContinuity
import TickEvolutionBridge as EB

-- Two entire completion charts glued at first-chart 1 = second-chart 0.
-- This is NOT asserted to be [0,2], nor are the charts restricted to [0,1].
ScheduleParameter : Type
ScheduleParameter = Pushout {A = Unit}
  (λ _ → oneCompletion) (λ _ → zeroCompletion)

start finish : ScheduleParameter
start = inl zeroCompletion
finish = inr oneCompletion

-- A single function, including its value along the gluing constructor.
glued : EB.G.Schedule → Bool × Bool → ScheduleParameter → Realization.Vector
glued r q (inl a) = firstLeg r q a
glued r q (inr b) = secondLeg r q b
glued r q (push tt i) = legs-join r q i

glued-start : (r : EB.G.Schedule) (q : Bool × Bool)
  → glued r q start ≡ Realization.basis q
glued-start = first-start

glued-finish : (r : EB.G.Schedule) (q : Bool × Bool)
  → glued r q finish ≡ Realization.basis (EB.G.run r q)
glued-finish = second-end

glued-seam : (r : EB.G.Schedule) (q : Bool × Bool)
  → cong (glued r q) (push tt) ≡ legs-join r q
glued-seam r q = refl

-- Explicit openness/continuity criterion, derived from CompletionNear.
-- Precision witnesses are truncated; the construction requires no choice.
Predicate : Type → Type₁
Predicate X = X → hProp ℓ-zero

ScalarOpen : Predicate MetricCompletionCandidate → Type
ScalarOpen P = (x : MetricCompletionCandidate) → fst (P x) →
  ∥ Σ[ k ∈ ℕ ] ((y : MetricCompletionCandidate) → CompletionNear k x y → fst (P y)) ∥₁

-- Final openness: a predicate is open precisely when both chart pullbacks
-- meet ScalarOpen. No equivalence with a separately defined metric topology
-- or with the standard real interval is assumed here.
FinalOpen : Predicate ScheduleParameter → Type
FinalOpen P = ScalarOpen (λ a → P (inl a)) × ScalarOpen (λ b → P (inr b))

quantitative-preimage-open : (F : MetricCompletionCandidate → MetricCompletionCandidate)
  → CompletionContinuous F → (P : Predicate MetricCompletionCandidate)
  → ScalarOpen P → ScalarOpen (λ x → P (F x))
quantitative-preimage-open F continuous P openP x member = PT.map
  (λ { (k , ball) → precision-modulus continuous k ,
    λ y close → ball (F y) (preserves-near continuous x y k close) })
  (openP (F x) member)

glued-continuous : (r : EB.G.Schedule) (q j : Bool × Bool)
  (P : Predicate MetricCompletionCandidate) → ScalarOpen P
  → FinalOpen (λ t → P (glued r q t j))
glued-continuous r q j P openP =
  quantitative-preimage-open (λ a → firstLeg r q a j) (first-continuous r q j) P openP ,
  quantitative-preimage-open (λ b → secondLeg r q b j) (second-continuous r q j) P openP

module FromRetainedTick (s : Bool × Bool) where
  module T = FromTick s
  module B = T.B
  open B.D.DiscreteReadout

  first-realization second-realization : B.D.ATick → ScheduleParameter → Realization.Vector
  first-realization t = glued (schedule-first (B.D.extract t)) (src (B.D.extract t))
  second-realization t = glued (schedule-second (B.D.extract t)) (src (B.D.extract t))

  first-source : (t : B.D.ATick) → first-realization t start ≡ Realization.basis s
  first-source = T.retained-first-start

  second-source : (t : B.D.ATick) → second-realization t start ≡ Realization.basis s
  second-source t = glued-start (schedule-second (B.D.extract t)) (src (B.D.extract t))
    ∙ cong Realization.basis (B.D.extract-source-attached t)

  first-target : (t : B.D.ATick)
    → first-realization t finish ≡ Realization.basis (tgt (B.D.extract t))
  first-target = T.retained-first-end

  second-target : (t : B.D.ATick)
    → second-realization t finish ≡ Realization.basis (tgt (B.D.extract t))
  second-target = T.retained-second-end

  first-continuity : (t : B.D.ATick) (j : Bool × Bool)
    (P : Predicate MetricCompletionCandidate) → ScalarOpen P
    → FinalOpen (λ a → P (first-realization t a j))
  first-continuity t = glued-continuous (schedule-first (B.D.extract t)) (src (B.D.extract t))

  second-continuity : (t : B.D.ATick) (j : Bool × Bool)
    (P : Predicate MetricCompletionCandidate) → ScalarOpen P
    → FinalOpen (λ a → P (second-realization t a j))
  second-continuity t = glued-continuous (schedule-second (B.D.extract t)) (src (B.D.extract t))
