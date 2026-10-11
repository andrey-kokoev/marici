{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralHamiltonian where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Data.Sigma.Base using (_,_)
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import CauchyNegation using (-completion_)
open import ConstructiveComplexCompletion
open import TickCompletionPhase using (phase)
open import TickPhaseMetricRegularity using (phaseGenerator)
open import TickMachinPiEndpointContract using (machinPi)
import TickComplexCompletionRing as Ring
import TickSpectralLocalOperators as L
import TickSpectralProjectorLaws as P

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module A = L.Algebra R
  abstract
    eigen-expand : (h z x y : fst R) →
      A.minus h (A.spectral h z x y) (A.spectral h z y x) ≡ (h + h) · (z · A.minus h x y)
    eigen-expand h z x y = solve! R
    reassociate : (a b z d : fst R) → ((a · b) · z) · d ≡ a · (b · (z · d))
    reassociate a b z d = solve! R

module Eigen (R : CommRing ℓ-zero) (J : Type) (k : J → J)
  (kk : (j : J) → k (k j) ≡ j) (h : fst R)
  (double : CommRingStr._+_ (snd R) h h ≡ CommRingStr.1r (snd R)) where
  open CommRingStr (snd R)
  module M = P.Permutation R J k kk h double
  module A = L.Algebra R
  module B = Algebra R
  abstract
    negative-eigen : (z : fst R) (v : M.Vector) → M.negative (M.spectral z v) ≡ (λ j → z · M.negative v j)
    negative-eigen z v = funExt λ j →
      cong (λ x → A.minus h (M.spectral z v j) (A.spectral h z (v (k j)) x)) (cong v (kk j))
      ∙ B.eigen-expand h z (v j) (v (k j))
      ∙ A.normalized h (z · M.negative v j) double

module RealIdentity (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  module C = Ring.PairRing R
  abstract
    minus-i-times-real : (p : fst R) → C.mul (0r , (- 1r)) (p , 0r) ≡ (0r , (- p))
    minus-i-times-real p = cong₂ _,_ (solve! R) (solve! R)

module V = L.V
module Left = Eigen Ring.ComplexCompletionCommRing V.Label P.leftIndex P.leftIndex-involutive L.halfComplex L.halfComplex-double
module Right = Eigen Ring.ComplexCompletionCommRing V.Label P.rightIndex P.rightIndex-involutive L.halfComplex L.halfComplex-double
module B = Algebra Ring.ComplexCompletionCommRing
module RI = RealIdentity CompletionCommRing

minusI piComplex : ComplexCompletion
minusI = complex zeroCompletion (-completion oneCompletion)
piComplex = complex machinPi zeroCompletion

-- The actual negative projector already contains the factor one half.
hamiltonian : (V.Vector → V.Vector) → V.Vector → V.Vector
hamiltonian P v = V.scale piComplex (L.negativeProjector P v)

-- Candidate obtained by differentiating only the scalar phase coefficient.
-- This definition does NOT assert HasMetricDerivative for vector coordinates.
localDerivativeCandidate : (V.Vector → V.Vector) → MetricCompletionCandidate → V.Vector → V.Vector
localDerivativeCandidate P t v = V.scale (phaseGenerator machinPi t) (L.negativeProjector P v)

abstract
  scalar-generator-reassociate : (t : MetricCompletionCandidate) (d : ComplexCompletion) →
    phaseGenerator machinPi t ·complex d ≡ minusI ·complex (piComplex ·complex (phase machinPi t ·complex d))
  scalar-generator-reassociate t d =
    cong (λ a → (a ·complex phase machinPi t) ·complex d) (sym (RI.minus-i-times-real machinPi))
    ∙ B.reassociate minusI piComplex (phase machinPi t) d

  left-generator-formula : (t : MetricCompletionCandidate) (v : V.Vector) →
    localDerivativeCandidate V.left t v ≡ V.scale minusI (hamiltonian V.left (L.leftLocal t v))
  left-generator-formula t v = funExt λ j →
    scalar-generator-reassociate t (L.negativeProjector V.left v j)
    ∙ cong (λ d → minusI ·complex (piComplex ·complex d))
      (sym (funExt⁻ (Left.negative-eigen (phase machinPi t) v) j))

  right-generator-formula : (t : MetricCompletionCandidate) (v : V.Vector) →
    localDerivativeCandidate V.right t v ≡ V.scale minusI (hamiltonian V.right (L.rightLocal t v))
  right-generator-formula t v = funExt λ j →
    scalar-generator-reassociate t (L.negativeProjector V.right v j)
    ∙ cong (λ d → minusI ·complex (piComplex ·complex d))
      (sym (funExt⁻ (Right.negative-eigen (phase machinPi t) v) j))
