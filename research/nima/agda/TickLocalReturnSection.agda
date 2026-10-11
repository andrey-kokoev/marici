{-# OPTIONS --safe --cubical --guardedness #-}
module TickLocalReturnSection where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Bool.Properties using (notEquiv)
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Empty using (⊥)
open import Cubical.Algebra.CommRing.Base using (CommRing→Ring; CommRingStr)
open import Cubical.Algebra.Ring.Properties using (module RingTheory)
open import Cubical.Data.Sigma.Base using (_×_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import CauchyMetricEquivalence using (embedMetricℚ)
open import CauchyCompletionMultiplication using
  (preferredCompletionMultiplication; preferredCompletionMultiplication-preserves-rationals)
open import CauchyCompletionMultiplicativeLaws using
  (preferred-completion-multiplication-right-unit;
   preferred-completion-multiplication-right-zero)
import TickCompletionSeparation as Separation
import ObserverCoherenceCube as Source
import TickCompletionRealization as Completion
import TickRetainedStructure as Structure
import TickJointEvolutionContinuity as Joint
open import TickBoundedProductContinuity using (BoundedNear)
open import TickQuotientContinuity using (CompletionNear)

module G = Source.Geometry Bool Bool notEquiv
module R = Completion.Realization
module B = R.ForSource (false , false)
module CompletionRingTheory = RingTheory (CommRing→Ring CompletionCommRing)
module CompletionRing = CommRingStr (snd CompletionCommRing)
open B.D.DiscreteReadout

-- The analytic return surface is parameterized by the completion scalar
-- square. Its coordinates are separate from Cubical I: no map I -> the
-- set-valued metric completion is assumed.
-- A cubical parameter cannot itself be the Cauchy scalar path parameter:
-- that would force a path between distinct completion scalars. The metric
-- path must remain external to Cubical I (or be related by a non-function
-- interface).
zero-not-one : zeroCompletion ≡ oneCompletion → ⊥
zero-not-one p = Separation.quarter-nonzero
  (sym (preferred-completion-multiplication-right-unit q)
   ∙ sym (cong (preferredCompletionMultiplication q) p)
   ∙ preferred-completion-multiplication-right-zero q)
  where
  q = embedMetricℚ Separation.quarter

-- Nor can the analytic metric evolution be represented by a Cubical path
-- in the completion-valued state space: even these endpoint states differ.
target-coordinate-zero : R.basis (true , true) (false , false) ≡ zeroCompletion
target-coordinate-zero = CompletionRingTheory.0LeftAnnihilates zeroCompletion

source-coordinate-one : R.basis (false , false) (false , false) ≡ oneCompletion
source-coordinate-one = CompletionRing.·IdL oneCompletion

no-cubical-state-path : R.basis (true , true) ≡ R.basis (false , false) → ⊥
no-cubical-state-path p = zero-not-one
  (sym target-coordinate-zero
   ∙ cong (λ v → v (false , false)) p
   ∙ source-coordinate-one)

return-target : B.D.ATick → Bool × Bool
return-target t = G.run G.leftFirst (src (B.D.extract t))

return-surface : B.D.ATick → R.Scalar → R.Scalar → R.Vector
return-surface t a b = R.U a b (R.basis (return-target t))

route-agrees : (r : G.Schedule) (q : Bool × Bool)
  → G.run G.leftFirst q ≡ G.run r q
route-agrees G.leftFirst q = refl
route-agrees G.rightFirst q = cong (λ f → f q) G.route-homotopy

run-left-involutive : (q : Bool × Bool)
  → G.run G.leftFirst (G.run G.leftFirst q) ≡ q
run-left-involutive (false , false) = refl
run-left-involutive (false , true) = refl
run-left-involutive (true , false) = refl
run-left-involutive (true , true) = refl

left-after-target : (q : Bool × Bool)
  → G.expandLeft (G.run G.leftFirst q) ≡ G.expandRight q
left-after-target (false , false) = refl
left-after-target (false , true) = refl
left-after-target (true , false) = refl
left-after-target (true , true) = refl

right-after-target : (q : Bool × Bool)
  → G.expandRight (G.run G.leftFirst q) ≡ G.expandLeft q
right-after-target (false , false) = refl
right-after-target (false , true) = refl
right-after-target (true , false) = refl
right-after-target (true , true) = refl

u00 : (v : R.Vector) → R.U zeroCompletion zeroCompletion v ≡ v
u00 v = R.leg-zero R.R _ ∙ R.leg-zero R.L v

u10 : (v : R.Vector) → R.U oneCompletion zeroCompletion v ≡ R.L v
u10 v = R.leg-zero R.R _ ∙ R.leg-one R.L v

u01 : (v : R.Vector) → R.U zeroCompletion oneCompletion v ≡ R.R v
u01 v = cong (R.leg R.R oneCompletion) (R.leg-zero R.L v)
  ∙ R.leg-one R.R v

u11 : (v : R.Vector) → R.U oneCompletion oneCompletion v ≡ R.R (R.L v)
u11 v = R.leg-one R.R (R.leg R.L oneCompletion v)
  ∙ cong R.R (R.leg-one R.L v)

return-corner-00 : (t : B.D.ATick)
  → return-surface t zeroCompletion zeroCompletion
    ≡ R.basis (G.run G.leftFirst (src (B.D.extract t)))
return-corner-00 t = u00 (R.basis (G.run G.leftFirst (src (B.D.extract t))))

return-corner-10 : (t : B.D.ATick)
  → return-surface t oneCompletion zeroCompletion
    ≡ R.basis (right-int (B.D.extract t))
return-corner-10 t =
  u10 (R.basis target)
  ∙ R.L-basis target
  ∙ cong R.basis (left-after-target (src (B.D.extract t)))
  where
  target = G.run G.leftFirst (src (B.D.extract t))

return-corner-01 : (t : B.D.ATick)
  → return-surface t zeroCompletion oneCompletion
    ≡ R.basis (left-int (B.D.extract t))
return-corner-01 t =
  u01 (R.basis target)
  ∙ R.R-basis target
  ∙ cong R.basis (right-after-target (src (B.D.extract t)))
  where
  target = G.run G.leftFirst (src (B.D.extract t))

return-corner-11 : (t : B.D.ATick)
  → return-surface t oneCompletion oneCompletion
    ≡ R.basis (src (B.D.extract t))
return-corner-11 t =
  u11 (R.basis target)
  ∙ cong R.R (R.L-basis target)
  ∙ R.R-basis (G.expandLeft target)
  ∙ cong R.basis (run-left-involutive (src (B.D.extract t)))
  where
  target = G.run G.leftFirst (src (B.D.extract t))

surface-start-at-canonical-target : (t : B.D.ATick)
  → return-surface t zeroCompletion zeroCompletion ≡ R.basis (true , true)
surface-start-at-canonical-target t =
  return-corner-00 t
  ∙ cong R.basis (cong (G.run G.leftFirst) (B.D.extract-source-attached t))

surface-end-at-attached-source : (t : B.D.ATick)
  → return-surface t oneCompletion oneCompletion ≡ R.basis (false , false)
surface-end-at-attached-source t =
  return-corner-11 t
  ∙ cong R.basis (B.D.extract-source-attached t)

-- Any single-valued Cubical state interpretation with these endpoint
-- values is impossible. A metric curve is not a Cubical path in this set.
no-cubical-return-interpreter : (f : I → R.Vector)
  → f i0 ≡ R.basis (true , true)
  → f i1 ≡ R.basis (false , false)
  → ⊥
no-cubical-return-interpreter f at-start at-end = no-cubical-state-path
  (sym at-start ∙ (λ k → f k) ∙ at-end)

-- Compatibility with the actual retained dependent section at its two
-- return endpoints. Mixed corners are attached to the extracted source
-- readout above; the section's interior is not identified pointwise with
-- the analytic scalar square.
return-section-start-compatible : (t : B.D.ATick)
  → return-surface t zeroCompletion zeroCompletion
    ≡ R.basis (B.D.Ret.RetainedReturn.return-section (B.D.ATick.returned t) i0 i0)
return-section-start-compatible t =
  return-corner-00 t
  ∙ cong R.basis
      (route-agrees (schedule-first (B.D.extract t)) (src (B.D.extract t))
       ∙ fst (B.D.extract-target-equals-run t)
       ∙ sym (B.D.extract-return-starts-at-target t))

return-section-end-compatible : (t : B.D.ATick)
  → return-surface t oneCompletion oneCompletion
    ≡ R.basis (B.D.Ret.RetainedReturn.return-section (B.D.ATick.returned t) i1 i1)
return-section-end-compatible t =
  return-corner-11 t
  ∙ sym (cong R.basis (B.D.extract-return-ends-at-source t))

-- Joint quantitative continuity on bounded regions, inherited from the
-- checked polynomial continuity theorem. The input bounds are explicit.
return-surface-continuous : (bounds : Joint.Input → ℕ) (k : ℕ)
  (t : B.D.ATick) (a a′ b b′ : R.Scalar)
  → ((j : Bool × Bool) (i : Joint.Input) → BoundedNear (bounds i)
      (Joint.C.demand (Joint.evolution-expression j) bounds k i)
      (Joint.environment a b (R.basis (return-target t)) i)
      (Joint.environment a′ b′ (R.basis (return-target t)) i))
  → ((j : Bool × Bool) → CompletionNear k
      (return-surface t a b j) (return-surface t a′ b′ j))
return-surface-continuous bounds k t a a′ b b′ h =
  Joint.evolution-vector-continuous bounds k a a′ b b′
    (R.basis (return-target t)) (R.basis (return-target t)) h

-- The path is local by construction: its two coordinates enter only
-- through the first-factor L leg and second-factor R leg.
return-surface-factorization : (t : B.D.ATick) (a b : R.Scalar)
  → return-surface t a b
    ≡ R.leg R.R b (R.leg R.L a
        (R.basis (G.run G.leftFirst (src (B.D.extract t)))) )
return-surface-factorization t a b = refl
