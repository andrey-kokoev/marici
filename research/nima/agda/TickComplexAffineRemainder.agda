{-# OPTIONS --safe --cubical --guardedness #-}
module TickComplexAffineRemainder where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_,_)
open import Cubical.HITs.PropositionalTruncation as PT
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence using (MetricCompletionCandidate; embedMetricℚ)
open import CauchyAdditionCongruence using (_+completion_)
open import RegularCauchyStructure using (precision)
import Cubical.Data.Rationals as Q
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import ConstructiveComplexCompletion
open import TickCompletionDerivative
import TickComplexConjugation as C

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module N = C.Laws R
  module P = N.P
  scale : fst R → P.C → P.C
  scale h (a , b) = (h · a) , (h · b)
  affine : P.C → P.C → P.C → P.C
  affine a z b = P.add a (P.mul z b)
  remainder : P.C → P.C → P.C → fst R → P.C
  remainder x y d h = P.add (P.add x (P.neg y)) (P.neg (scale h d))

  abstract
    factor : (a b x y d : P.C) (h : fst R) →
      remainder (affine a x b) (affine a y b) (P.mul d b) h ≡ P.mul (remainder x y d h) b
    factor (a , ai) (b , bi) (x , xi) (y , yi) (d , di) h = cong₂ _,_ (solve! R) (solve! R)
    norm-unit-product : (z b : P.C) → N.normSquared b ≡ 1r → N.normSquared (P.mul z b) ≡ N.normSquared z
    norm-unit-product z b unit = N.norm-product z b ∙ cong (N.normSquared z ·_) unit ∙ ·IdR (N.normSquared z)

module A = Algebra CompletionCommRing
module N = C.Operational

affineCurve : ComplexCompletion → ComplexCompletion →
  (MetricCompletionCandidate → ComplexCompletion) → MetricCompletionCandidate → ComplexCompletion
affineCurve a b f t = a +complex (f t ·complex b)

abstract
  affine-remainder-factor : (a b : ComplexCompletion) (f : MetricCompletionCandidate → ComplexCompletion)
    (t : MetricCompletionCandidate) (v : ComplexCompletion) (h : MetricCompletionCandidate) →
    firstOrderRemainder (affineCurve a b f) t (v ·complex b) h ≡ firstOrderRemainder f t v h ·complex b
  affine-remainder-factor a b f t v h = A.factor a b (f (t +completion h)) (f t) v h

  affine-remainder-norm : (a b : ComplexCompletion) (f : MetricCompletionCandidate → ComplexCompletion)
    (t : MetricCompletionCandidate) (v : ComplexCompletion) (h : MetricCompletionCandidate) →
    complexNormSquared (firstOrderRemainder (affineCurve a b f) t (v ·complex b) h) ≡
    preferredCompletionMultiplication (complexNormSquared (firstOrderRemainder f t v h)) (complexNormSquared b)
  affine-remainder-norm a b f t v h = cong complexNormSquared (affine-remainder-factor a b f t v h)
    ∙ N.norm-product (firstOrderRemainder f t v h) b

  affine-unit-remainder-norm : (a b : ComplexCompletion) → complexNormSquared b ≡ oneCompletion →
    (f : MetricCompletionCandidate → ComplexCompletion) (t : MetricCompletionCandidate)
    (v : ComplexCompletion) (h : MetricCompletionCandidate) →
    complexNormSquared (firstOrderRemainder (affineCurve a b f) t (v ·complex b) h) ≡
    complexNormSquared (firstOrderRemainder f t v h)
  affine-unit-remainder-norm a b unit f t v h = cong complexNormSquared (affine-remainder-factor a b f t v h)
    ∙ A.norm-unit-product (firstOrderRemainder f t v h) b unit

  -- A genuine all-increment derivative rule at the existing metric notion.
  -- Its unit-norm coefficient premise is essential; arbitrary spectral
  -- coefficients still require an Archimedean bound and precision loss.
  affine-unit-derivative : (a b : ComplexCompletion) → complexNormSquared b ≡ oneCompletion →
    (f : MetricCompletionCandidate → ComplexCompletion) (t : MetricCompletionCandidate) (v : ComplexCompletion) →
    HasMetricDerivative f t v → HasMetricDerivative (affineCurve a b f) t (v ·complex b)
  affine-unit-derivative a b unit f t v derivative k = PT.map
    (λ { (l , bound) → l , λ h near → subst (λ n → CompletionLE n
        (preferredCompletionMultiplication (embedMetricℚ (precision k Q.· precision k)) (squareCompletion h)))
      (sym (affine-unit-remainder-norm a b unit f t v h)) (bound h near) }) (derivative k)
