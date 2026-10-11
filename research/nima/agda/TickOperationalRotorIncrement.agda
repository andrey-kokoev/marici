{-# OPTIONS --safe --cubical --guardedness #-}
module TickOperationalRotorIncrement where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (one-half)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyCompletionCommRing
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import OperationalCosineMetric using (completionCosine)
open import OperationalSineMetric using (completionSine)
open import TickCompletionTrigAddition using (completion-cosine-addition; completion-sine-addition)
open import TickAtanCompletionFirstOrder using (atanCompletion)
open import TickAtanGridSmallAngle using (doubledAtanIncrement)
open import TickCayleyGridIncrement using (gridValue)
open import TickRotationDefectTransport using (Rotor; _⊗_)

rotation : MetricCompletionCandidate → Rotor
rotation a = completionCosine a , completionSine a

gridAngle : (n d : ℕ) → MagnitudeBound (gridValue n d) one-half → MetricCompletionCandidate
gridAngle n d h = atanCompletion (gridValue n d) h +completion atanCompletion (gridValue n d) h

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  increment : (a b : fst R) → (a +S a) +S ((b +S (-S a)) +S (b +S (-S a))) ≡ b +S b
  increment a b = solve! R

abstract
  rotation-addition : (a b : MetricCompletionCandidate) → rotation (a +completion b) ≡ rotation a ⊗ rotation b
  rotation-addition a b = cong₂ _,_ (completion-cosine-addition a b)
    (completion-sine-addition a b ∙ CommRingStr.+Comm (snd CompletionCommRing)
      (preferredCompletionMultiplication (completionSine a) (completionCosine b))
      (preferredCompletionMultiplication (completionCosine a) (completionSine b)))

  grid-angle-increment : (n m d : ℕ)
    (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half) →
    gridAngle n d hx +completion doubledAtanIncrement n m d hx hy ≡ gridAngle m d hy
  grid-angle-increment n m d hx hy = Algebra.increment CompletionCommRing
    (atanCompletion (gridValue n d) hx) (atanCompletion (gridValue m d) hy)

  grid-rotation-increment : (n m d : ℕ)
    (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half) →
    rotation (gridAngle m d hy) ≡ rotation (gridAngle n d hx) ⊗ rotation (doubledAtanIncrement n m d hx hy)
  grid-rotation-increment n m d hx hy = cong rotation (sym (grid-angle-increment n m d hx hy))
    ∙ rotation-addition (gridAngle n d hx) (doubledAtanIncrement n m d hx hy)
