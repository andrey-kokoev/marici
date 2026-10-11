{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralLocalNorm where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_,_)
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence using (MetricCompletionCandidate; embedMetricℚ)
open import CauchyCompletionCommRing using (CompletionCommRing)
open import CauchyAdditionCongruence using (_+completion_)
open import ConstructiveComplexCompletion using (realPart)
open import RationalAnalyticSubstrate using (one-half)
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
open import TickConstructedScheduledNorm using (operational-phase-unit-norm)
import TickComplexConjugation as C
import TickSpectralLocalOperators as L
-- Together with norm preservation below these give norm-preserving bijections.
-- No adjoint characterization is asserted here.
open import TickSpectralLocalInverse public using
  (leftInverse; rightInverse; left-inverse-after; left-inverse-before;
   right-inverse-after; right-inverse-before)

module PairEnergy (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module N = C.Laws R
  module P = N.P
  module A = L.Algebra P.ring
  energy : P.C → P.C → fst R
  energy x y = N.normSquared x + N.normSquared y
  step : fst R → P.C → P.C → P.C → P.C
  step h z x y = A.spectral (N.real h) z x y

  abstract
    expansion : (h : fst R) (z x y : P.C) →
      energy (step h z x y) (step h z y x) ≡
      ((h + h) · (h + h)) · energy x y +
      (((h + h) · h) · (N.normSquared z + (- 1r))) · N.normSquared (P.add x (P.neg y))
    expansion h (a , b) (c , d) (e , f) = solve! R

    neutral : (h n d : fst R) →
      (1r · 1r) · n + (((1r · h) · (1r + (- 1r))) · d) ≡ n
    neutral h n d = solve! R

    preservation : (h : fst R) → h + h ≡ 1r → (z : P.C) → N.normSquared z ≡ 1r →
      (x y : P.C) → energy (step h z x y) (step h z y x) ≡ energy x y
    preservation h half z unit x y = expansion h z x y
      ∙ cong₂ (λ a b → (a · a) · energy x y +
          (((a · h) · (b + (- 1r))) · N.normSquared (P.add x (P.neg y)))) half unit
      ∙ neutral h (energy x y) (N.normSquared (P.add x (P.neg y)))

    regroup : (a b c d : fst R) → (a + b) + (c + d) ≡ (a + c) + (b + d)
    regroup a b c d = solve! R

module E = PairEnergy CompletionCommRing
module N = C.Operational
module V = L.V

-- The usual sum of the four scalar squared moduli, in row-major order.
vectorNormSquared : V.Vector → MetricCompletionCandidate
vectorNormSquared v =
  (N.normSquared (v (false , false)) +completion N.normSquared (v (false , true))) +completion
  (N.normSquared (v (true , false)) +completion N.normSquared (v (true , true)))

abstract
  right-local-norm : (t : MetricCompletionCandidate) (v : V.Vector) →
    vectorNormSquared (L.rightLocal t v) ≡ vectorNormSquared v
  right-local-norm t v = cong₂ _+completion_
    (E.preservation (embedMetricℚ one-half) (cong realPart L.halfComplex-double)
      (phase machinPi t) (operational-phase-unit-norm machinPi t) (v (false , false)) (v (false , true)))
    (E.preservation (embedMetricℚ one-half) (cong realPart L.halfComplex-double)
      (phase machinPi t) (operational-phase-unit-norm machinPi t) (v (true , false)) (v (true , true)))

  left-local-norm : (t : MetricCompletionCandidate) (v : V.Vector) →
    vectorNormSquared (L.leftLocal t v) ≡ vectorNormSquared v
  left-local-norm t v =
    E.regroup (N.normSquared (L.leftLocal t v (false , false)))
      (N.normSquared (L.leftLocal t v (false , true)))
      (N.normSquared (L.leftLocal t v (true , false)))
      (N.normSquared (L.leftLocal t v (true , true)))
    ∙ cong₂ _+completion_
      (E.preservation (embedMetricℚ one-half) (cong realPart L.halfComplex-double)
        (phase machinPi t) (operational-phase-unit-norm machinPi t) (v (false , false)) (v (true , false)))
      (E.preservation (embedMetricℚ one-half) (cong realPart L.halfComplex-double)
        (phase machinPi t) (operational-phase-unit-norm machinPi t) (v (false , true)) (v (true , true)))
    ∙ E.regroup (N.normSquared (v (false , false))) (N.normSquared (v (true , false)))
      (N.normSquared (v (false , true))) (N.normSquared (v (true , true)))
