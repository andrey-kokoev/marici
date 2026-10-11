{-# OPTIONS --safe --cubical --guardedness #-}
module TickContinuousSchedules where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool)
open import Cubical.Data.Sigma.Base using (_×_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (oneCompletion)
open import TickCompletionRealization
open import TickQuotientContinuity
import TickEvolutionBridge as EB

-- Each schedule is two completion-parameterized legs, joined by an exact
-- equality at the intermediate corner. We do not identify this with the
-- original dependent cubical return section or a unitary evolution.
firstLeg : EB.G.Schedule → Bool × Bool → Realization.Scalar → Realization.Vector
firstLeg EB.G.leftFirst q a = Realization.leg Realization.L a (Realization.basis q)
firstLeg EB.G.rightFirst q a = Realization.leg Realization.R a (Realization.basis q)

middle : EB.G.Schedule → Bool × Bool → Bool × Bool
middle EB.G.leftFirst = EB.G.expandLeft
middle EB.G.rightFirst = EB.G.expandRight

secondLeg : EB.G.Schedule → Bool × Bool → Realization.Scalar → Realization.Vector
secondLeg EB.G.leftFirst q a = Realization.leg Realization.R a (Realization.basis (middle EB.G.leftFirst q))
secondLeg EB.G.rightFirst q a = Realization.leg Realization.L a (Realization.basis (middle EB.G.rightFirst q))

first-start : (r : EB.G.Schedule) (q : Bool × Bool)
  → firstLeg r q zeroCompletion ≡ Realization.basis q
first-start EB.G.leftFirst q = Realization.leg-zero Realization.L _
first-start EB.G.rightFirst q = Realization.leg-zero Realization.R _

first-end : (r : EB.G.Schedule) (q : Bool × Bool)
  → firstLeg r q oneCompletion ≡ Realization.basis (middle r q)
first-end EB.G.leftFirst q = Realization.leg-one Realization.L (Realization.basis q) ∙ Realization.L-basis q
first-end EB.G.rightFirst q = Realization.leg-one Realization.R (Realization.basis q) ∙ Realization.R-basis q

second-start : (r : EB.G.Schedule) (q : Bool × Bool)
  → secondLeg r q zeroCompletion ≡ Realization.basis (middle r q)
second-start EB.G.leftFirst q = Realization.leg-zero Realization.R _
second-start EB.G.rightFirst q = Realization.leg-zero Realization.L _

legs-join : (r : EB.G.Schedule) (q : Bool × Bool)
  → firstLeg r q oneCompletion ≡ secondLeg r q zeroCompletion
legs-join r q = first-end r q ∙ sym (second-start r q)

second-end : (r : EB.G.Schedule) (q : Bool × Bool)
  → secondLeg r q oneCompletion ≡ Realization.basis (EB.G.run r q)
second-end EB.G.leftFirst q = Realization.leg-one Realization.R (Realization.basis (middle EB.G.leftFirst q)) ∙ Realization.R-basis (middle EB.G.leftFirst q)
second-end EB.G.rightFirst q = Realization.leg-one Realization.L (Realization.basis (middle EB.G.rightFirst q)) ∙ Realization.L-basis (middle EB.G.rightFirst q)

first-continuous : (r : EB.G.Schedule) (q j : Bool × Bool)
  → CompletionContinuous (λ a → firstLeg r q a j)
first-continuous EB.G.leftFirst = left-completion-continuous
first-continuous EB.G.rightFirst = right-completion-continuous

second-continuous : (r : EB.G.Schedule) (q j : Bool × Bool)
  → CompletionContinuous (λ a → secondLeg r q a j)
second-continuous EB.G.leftFirst q = right-completion-continuous (middle EB.G.leftFirst q)
second-continuous EB.G.rightFirst q = left-completion-continuous (middle EB.G.rightFirst q)

module FromTick (s : Bool × Bool) where
  module B = Realization.ForSource s
  open B.D.DiscreteReadout

  -- The ordered schedule is read from the ACTUAL retained Tick.
  retained-first-start : (t : B.D.ATick)
    → firstLeg (schedule-first (B.D.extract t)) (src (B.D.extract t)) zeroCompletion
      ≡ Realization.basis s
  retained-first-start t = first-start (schedule-first (B.D.extract t)) (src (B.D.extract t))
    ∙ cong Realization.basis (B.D.extract-source-attached t)

  retained-first-end : (t : B.D.ATick)
    → secondLeg (schedule-first (B.D.extract t)) (src (B.D.extract t)) oneCompletion
      ≡ Realization.basis (tgt (B.D.extract t))
  retained-first-end t = second-end (schedule-first (B.D.extract t)) (src (B.D.extract t))
    ∙ cong Realization.basis (fst (B.D.extract-target-equals-run t))

  retained-second-end : (t : B.D.ATick)
    → secondLeg (schedule-second (B.D.extract t)) (src (B.D.extract t)) oneCompletion
      ≡ Realization.basis (tgt (B.D.extract t))
  retained-second-end t = second-end (schedule-second (B.D.extract t)) (src (B.D.extract t))
    ∙ cong Realization.basis (snd (B.D.extract-target-equals-run t))
