{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralPiecewiseDerivative where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma using (_×_; Σ)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence using (MetricCompletionCandidate; embedMetricℚ)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import TickCompletionCoefficientBound using (precisionSquared)
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import ConstructiveComplexCompletion
open import TickCompletionDerivative
open import TickSpectralLocalContinuity using (Control; combine)
open import TickCompletionClippedTime using (afterOne)
import TickCompletionMetricInterval as I
import TickSpectralLocalOperators as L
import TickSpectralLocalDynamics as D
import TickSpectralHamiltonian as H
import TickSpectralGlobalPath as Path
import TickSpectralRetainedReturn as Return
import TickSpectralProjectorLaws as P
module V = L.V
module G = Return.G

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    translate-increment : (t h c : fst R) → (t + h) + c ≡ (t + c) + h
    translate-increment t h c = solve! R
module A = Algebra CompletionCommRing

NearAgreement : (MetricCompletionCandidate → V.Vector) → (MetricCompletionCandidate → V.Vector) → MetricCompletionCandidate → Type
NearAgreement f g t = Control zeroCompletion (λ h → f (t +completion h) ≡ g (t +completion h))

-- Metric-interior formulation, with the center bound explicit. No comparison
-- decision or differentiability at the boundary is inferred.
BeforeSeam AfterSeam : MetricCompletionCandidate → Type
BeforeSeam t = CompletionLE t oneCompletion × Control zeroCompletion (λ h → CompletionLE (t +completion h) oneCompletion)
AfterSeam t = CompletionLE oneCompletion t × Control zeroCompletion (λ h → CompletionLE oneCompletion (t +completion h))

abstract
  derivative-local-agreement : (f g : MetricCompletionCandidate → V.Vector)
    (t : MetricCompletionCandidate) (v : V.Vector) → f t ≡ g t → NearAgreement f g t →
    D.HasVectorMetricDerivative g t v → D.HasVectorMetricDerivative f t v
  derivative-local-agreement f g t v center nearby derivative k = PT.map
    (λ { (l , control) → l , λ h near j →
      subst (λ n → CompletionLE n (preferredCompletionMultiplication (embedMetricℚ (precisionSquared k)) (squareCompletion h))) (sym (cong complexNormSquared
        (cong₂ (λ x y → (x +complex negComplex y) +complex negComplex (scaleComplex h (v j)))
          (cong (λ w → w j) (snd (control h near))) (cong (λ w → w j) center))))
        (fst (control h near) j) }) (combine (derivative k) nearby)

  derivative-translate : (f : MetricCompletionCandidate → V.Vector)
    (t c : MetricCompletionCandidate) (v : V.Vector) → D.HasVectorMetricDerivative f (t +completion c) v →
    D.HasVectorMetricDerivative (λ s → f (s +completion c)) t v
  derivative-translate f t c v derivative k = PT.map
    (λ { (l , bound) → l , λ h near j → subst (λ n → CompletionLE n (preferredCompletionMultiplication (embedMetricℚ (precisionSquared k)) (squareCompletion h)))
      (sym (cong complexNormSquared
        (cong (λ x → (x +complex negComplex (f (t +completion c) j)) +complex negComplex (scaleComplex h (v j)))
          (cong (λ s → f s j) (A.translate-increment t h c))))) (bound h near j) }) (derivative k)

  glued-first-derivative : (a b : Path.IndexMap) (t : MetricCompletionCandidate) (v : V.Vector) → BeforeSeam t →
    D.HasVectorMetricDerivative (λ s → Path.glued a b s v) t (H.localDerivativeCandidate (Path.permute a) t v)
  glued-first-derivative a b t v (center , nearby) = derivative-local-agreement
    (λ s → Path.glued a b s v) (λ s → L.local (Path.permute a) s v) t (H.localDerivativeCandidate (Path.permute a) t v)
    (Path.glued-on-left a b t v center)
    (PT.map (λ { (l , bound) → l , λ h near → Path.glued-on-left a b (t +completion h) v (bound h near) }) nearby)
    (D.local-vector-derivative (Path.permute a) t v)

  glued-second-derivative : (a b : Path.IndexMap) (t : MetricCompletionCandidate) (v : V.Vector) → AfterSeam t →
    D.HasVectorMetricDerivative (λ s → Path.glued a b s v) t
      (H.localDerivativeCandidate (Path.permute b) (afterOne t) (Path.permute a v))
  glued-second-derivative a b t v (center , nearby) = derivative-local-agreement
    (λ s → Path.glued a b s v) (λ s → L.local (Path.permute b) (afterOne s) (Path.permute a v)) t
    (H.localDerivativeCandidate (Path.permute b) (afterOne t) (Path.permute a v))
    (Path.glued-on-right a b t v center)
    (PT.map (λ { (l , bound) → l , λ h near → Path.glued-on-right a b (t +completion h) v (bound h near) }) nearby)
    (derivative-translate (λ s → L.local (Path.permute b) s (Path.permute a v)) t (-completion oneCompletion)
      (H.localDerivativeCandidate (Path.permute b) (afterOne t) (Path.permute a v))
      (D.local-vector-derivative (Path.permute b) (afterOne t) (Path.permute a v)))

firstIndex secondIndex : G.Schedule → Path.IndexMap
firstIndex G.leftFirst = P.rightIndex
firstIndex G.rightFirst = P.leftIndex
secondIndex G.leftFirst = P.leftIndex
secondIndex G.rightFirst = P.rightIndex

returnCurve : G.Schedule → V.Label → MetricCompletionCandidate → V.Vector
returnCurve r s t = Path.glued (firstIndex r) (secondIndex r) t (Return.nativeTarget s)
return-curve-correspondence : (r : G.Schedule) (s : V.Label) (t : I.ReturnInterval) → returnCurve r s (fst t) ≡ Return.returnPath r s t
return-curve-correspondence G.leftFirst s t = refl
return-curve-correspondence G.rightFirst s t = refl

abstract
  first-generator : (r : G.Schedule) (t : MetricCompletionCandidate) (v : V.Vector) →
    H.localDerivativeCandidate (Path.permute (firstIndex r)) t v ≡
    V.scale H.minusI (H.hamiltonian (Path.permute (firstIndex r)) (L.local (Path.permute (firstIndex r)) t v))
  first-generator G.leftFirst = H.right-generator-formula
  first-generator G.rightFirst = H.left-generator-formula
  second-generator : (r : G.Schedule) (t : MetricCompletionCandidate) (v : V.Vector) →
    H.localDerivativeCandidate (Path.permute (secondIndex r)) t v ≡
    V.scale H.minusI (H.hamiltonian (Path.permute (secondIndex r)) (L.local (Path.permute (secondIndex r)) t v))
  second-generator G.leftFirst = H.left-generator-formula
  second-generator G.rightFirst = H.right-generator-formula

  return-first-hamiltonian : (r : G.Schedule) (s : V.Label) (t : MetricCompletionCandidate) → BeforeSeam t →
    D.HasVectorMetricDerivative (returnCurve r s) t
      (V.scale H.minusI (H.hamiltonian (Path.permute (firstIndex r)) (returnCurve r s t)))
  return-first-hamiltonian r s t region = subst (D.HasVectorMetricDerivative (returnCurve r s) t)
    (first-generator r t (Return.nativeTarget s)
      ∙ cong (λ w → V.scale H.minusI (H.hamiltonian (Path.permute (firstIndex r)) w))
        (sym (Path.glued-on-left (firstIndex r) (secondIndex r) t (Return.nativeTarget s) (fst region))))
    (glued-first-derivative (firstIndex r) (secondIndex r) t (Return.nativeTarget s) region)

  return-second-hamiltonian : (r : G.Schedule) (s : V.Label) (t : MetricCompletionCandidate) → AfterSeam t →
    D.HasVectorMetricDerivative (returnCurve r s) t
      (V.scale H.minusI (H.hamiltonian (Path.permute (secondIndex r)) (returnCurve r s t)))
  return-second-hamiltonian r s t region = subst (D.HasVectorMetricDerivative (returnCurve r s) t)
    (second-generator r (afterOne t) (Path.permute (firstIndex r) (Return.nativeTarget s))
      ∙ cong (λ w → V.scale H.minusI (H.hamiltonian (Path.permute (secondIndex r)) w))
        (sym (Path.glued-on-right (firstIndex r) (secondIndex r) t (Return.nativeTarget s) (fst region))))
    (glued-second-derivative (firstIndex r) (secondIndex r) t (Return.nativeTarget s) region)
