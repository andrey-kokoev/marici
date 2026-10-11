{-# OPTIONS --safe --cubical --guardedness #-}
module TickConcreteImageObstruction where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Unit using (Unit; tt)
open import Cubical.Data.Empty using (⊥; isProp⊥)
open import Cubical.Data.Sigma using (_×_)
open import Cubical.Data.Nat as Nat using ()
import Cubical.Data.Nat.Order as NatOrder
open import Cubical.Data.Rationals as Q using (fromNatℚ)
open import Cubical.Data.Nat.Literals
import Cubical.Data.Rationals.Order as QOrder
open import Cubical.Relation.Nullary using (Dec; yes; no)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.HITs.Pushout.Base using (inl; inr; push)
open import Cubical.Algebra.CommRing.Base
open import Cubical.Tactics.CommRingSolver
open import RegularCauchyStructure
open import RationalAnalyticSubstrate using (one-half)
open import CauchyMetricEquivalence
open import MetricCompletionEffectiveness
open import CauchyCompletionCommRing
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionMultiplication
open import CauchyRationalEmbedding
open import TickCompletionRealization
open import TickGluedSchedules
open import TickInterpretationBoundary using (Substitution; image-obstruction; module RetainedInterpretation)
import TickEvolutionBridge as EB

open import TickCompletionSeparation using (quarter; quarter-nonzero)

module Algebra (K : CommRing ℓ-zero) where
  open CommRingStr (snd K)
  missing-straight : (a d e : fst K)
    → (1r + (- a)) · (d · 0r) + a · (0r · e) ≡ 0r
  missing-straight a d e = solve! K

  missing-bowed : (a : fst K)
    → ((1r + (- a)) · (1r + (- a))) · (1r · 0r)
      + a · (0r · 0r) + (a · (1r + (- a))) · (1r · 1r)
      ≡ a · (1r + (- a))
  missing-bowed a = solve! K

  bowed-start : (x y z : fst K)
    → ((1r + (- 0r)) · (1r + (- 0r))) · x + 0r · y
      + (0r · (1r + (- 0r))) · z ≡ x
  bowed-start x y z = solve! K

  bowed-end : (x y z : fst K)
    → ((1r + (- 1r)) · (1r + (- 1r))) · x + 1r · y
      + (1r · (1r + (- 1r))) · z ≡ y
  bowed-end x y z = solve! K

module C = CommRingStr (snd CompletionCommRing)
module A = Algebra CompletionCommRing

origin missing : Bool × Bool
origin = false , false
missing = false , true

straight : ScheduleParameter → Realization.Vector
straight = glued EB.G.leftFirst origin

straight-missing : (p : ScheduleParameter) → straight p missing ≡ zeroCompletion
straight-missing (inl a) = A.missing-straight a oneCompletion zeroCompletion
straight-missing (inr b) = A.missing-straight b zeroCompletion oneCompletion
straight-missing (push tt i) = isProp→PathP
  (λ i → metric-candidate-isSet (straight (push tt i) missing) zeroCompletion)
  (A.missing-straight oneCompletion oneCompletion zeroCompletion)
  (A.missing-straight zeroCompletion zeroCompletion oneCompletion) i

-- Bowed first leg, on the SAME completion scalar and four-coordinate
-- vector carrier as the earlier bridge. No floating-point calculation.
bowed : (Realization.Vector → Realization.Vector)
  → (Realization.Vector → Realization.Vector)
  → Realization.Scalar → Realization.Vector → Realization.Vector
bowed active other a v j = C._+_
  (C._+_
    (C._·_ (C._·_ (C._+_ oneCompletion (C.-_ a)) (C._+_ oneCompletion (C.-_ a))) (v j))
    (C._·_ a (active v j)))
  (C._·_ (C._·_ a (C._+_ oneCompletion (C.-_ a))) (other v j))

bowed-left bowed-right : Realization.Scalar → Realization.Vector → Realization.Vector
bowed-left = bowed Realization.L Realization.R
bowed-right = bowed Realization.R Realization.L

bowed-zero : (active other : Realization.Vector → Realization.Vector) (v : Realization.Vector)
  → bowed active other zeroCompletion v ≡ v
bowed-zero active other v = funExt λ j → A.bowed-start (v j) (active v j) (other v j)

bowed-one : (active other : Realization.Vector → Realization.Vector) (v : Realization.Vector)
  → bowed active other oneCompletion v ≡ active v
bowed-one active other v = funExt λ j → A.bowed-end (v j) (active v j) (other v j)

bowed-model : EB.EndpointModel Realization.Vector Realization.Scalar
EB.EndpointModel.encode bowed-model = Realization.basis
EB.EndpointModel.zero bowed-model = zeroCompletion
EB.EndpointModel.end bowed-model = oneCompletion
EB.EndpointModel.evolve bowed-model a b v = bowed-right b (bowed-left a v)
EB.EndpointModel.at00 bowed-model q = bowed-zero Realization.R Realization.L _
  ∙ bowed-zero Realization.L Realization.R _
EB.EndpointModel.at10 bowed-model q = bowed-zero Realization.R Realization.L _
  ∙ bowed-one Realization.L Realization.R (Realization.basis q) ∙ Realization.L-basis q
EB.EndpointModel.at01 bowed-model q = cong (bowed-right oneCompletion)
  (bowed-zero Realization.L Realization.R (Realization.basis q))
  ∙ bowed-one Realization.R Realization.L (Realization.basis q) ∙ Realization.R-basis q
EB.EndpointModel.at11 bowed-model q =
  bowed-one Realization.R Realization.L (bowed-left oneCompletion (Realization.basis q))
  ∙ cong Realization.R (bowed-one Realization.L Realization.R (Realization.basis q) ∙ Realization.L-basis q)
  ∙ Realization.R-basis (EB.G.expandLeft q)

-- Both models are admitted by the SAME source-retaining endpoint contract.
module StraightInterpretation = RetainedInterpretation Realization.model origin
module BowedInterpretation = RetainedInterpretation bowed-model origin

bowed-join : bowed-left oneCompletion (Realization.basis origin)
  ≡ bowed-right zeroCompletion (Realization.basis (EB.G.expandLeft origin))
bowed-join = bowed-one Realization.L Realization.R (Realization.basis origin)
  ∙ Realization.L-basis origin
  ∙ sym (bowed-zero Realization.R Realization.L (Realization.basis (EB.G.expandLeft origin)))

bowed-global : ScheduleParameter → Realization.Vector
bowed-global (inl a) = bowed-left a (Realization.basis origin)
bowed-global (inr b) = bowed-right b (Realization.basis (EB.G.expandLeft origin))
bowed-global (push tt i) = bowed-join i

bowed-source : bowed-global start ≡ Realization.basis origin
bowed-source = bowed-zero Realization.L Realization.R (Realization.basis origin)

bowed-target : bowed-global finish ≡ Realization.basis (true , true)
bowed-target = bowed-one Realization.R Realization.L (Realization.basis (EB.G.expandLeft origin))
  ∙ Realization.R-basis (EB.G.expandLeft origin)

midpoint : Realization.Vector
midpoint = bowed-left (embedMetricℚ one-half) (Realization.basis origin)

midpoint-missing : midpoint missing ≡ embedMetricℚ quarter
midpoint-missing = A.missing-bowed (embedMetricℚ one-half)
  ∙ cong (C._·_ (embedMetricℚ one-half))
    (cong (C._+_ oneCompletion) (embedℚ-preserves-negation one-half)
      ∙ sym (embedℚ-preserves-sum 1 (Q.- one-half)))
  ∙ preferredCompletionMultiplication-preserves-rationals one-half (1 Q.+ (Q.- one-half))

midpoint-outside : (p : ScheduleParameter) → straight p ≡ midpoint → ⊥
midpoint-outside p equality = quarter-nonzero
  (sym midpoint-missing ∙ sym (cong (λ v → v missing) equality) ∙ straight-missing p)

-- Already rules out ANY substitution matching the bowed first leg to
-- the whole straight schedule; a full bowed path contains this leg.
no-first-leg-substitution :
  Substitution straight (λ a → bowed-left a (Realization.basis origin)) → ⊥
no-first-leg-substitution = image-obstruction straight
  (λ a → bowed-left a (Realization.basis origin))
  (λ v → v missing ≡ zeroCompletion)
  straight-missing (embedMetricℚ one-half)
  (λ h → quarter-nonzero (sym midpoint-missing ∙ h))

no-global-substitution : Substitution straight bowed-global → ⊥
no-global-substitution (ρ , agrees) = no-first-leg-substitution
  ((λ a → ρ (inl a)) , (λ a → agrees (inl a)))
