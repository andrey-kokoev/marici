{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralLocalUnitary where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import ConstructiveComplexCompletion using (ComplexCompletion)
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
open import TickComplexCompletionRing using (ComplexCompletionCommRing)
import TickSpectralLocalOperators as L
import TickSpectralLocalNorm as N

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  open L.Algebra R using (spectral)
  abstract
    additive : (h z x y a b : fst R) →
      spectral h z (x + a) (y + b) ≡ spectral h z x y + spectral h z a b
    additive h z x y a b = solve! R
    homogeneous : (h z c x y : fst R) →
      spectral h z (c · x) (c · y) ≡ c · spectral h z x y
    homogeneous h z c x y = solve! R

module A = Algebra ComplexCompletionCommRing
module V = L.V

abstract
  left-additive : (t : MetricCompletionCandidate) (v w : V.Vector) →
    L.leftLocal t (V.add v w) ≡ V.add (L.leftLocal t v) (L.leftLocal t w)
  left-additive t v w = funExt λ j → A.additive L.halfComplex (phase machinPi t)
    (v j) (V.left v j) (w j) (V.left w j)
  right-additive : (t : MetricCompletionCandidate) (v w : V.Vector) →
    L.rightLocal t (V.add v w) ≡ V.add (L.rightLocal t v) (L.rightLocal t w)
  right-additive t v w = funExt λ j → A.additive L.halfComplex (phase machinPi t)
    (v j) (V.right v j) (w j) (V.right w j)
  left-homogeneous : (t : MetricCompletionCandidate) (c : ComplexCompletion) (v : V.Vector) →
    L.leftLocal t (V.scale c v) ≡ V.scale c (L.leftLocal t v)
  left-homogeneous t c v = funExt λ j → A.homogeneous L.halfComplex (phase machinPi t) c (v j) (V.left v j)
  right-homogeneous : (t : MetricCompletionCandidate) (c : ComplexCompletion) (v : V.Vector) →
    L.rightLocal t (V.scale c v) ≡ V.scale c (L.rightLocal t v)
  right-homogeneous t c v = funExt λ j → A.homogeneous L.halfComplex (phase machinPi t) c (v j) (V.right v j)

-- Generic certificate syntax avoids unfolding Cauchy schedules in record
-- positivity checking. Norm means squared norm in the operational instance.
-- This is a linear norm-preserving equivalence, not an adjoint presentation.
module Certificate (Scalar Vector NormValue : Type)
  (add : Vector → Vector → Vector) (scale : Scalar → Vector → Vector)
  (norm : Vector → NormValue) where
  record LinearNormEquivalence (U : Vector → Vector) : Type where
    field
      inverse : Vector → Vector
      additive : (v w : Vector) → U (add v w) ≡ add (U v) (U w)
      homogeneous : (c : Scalar) (v : Vector) → U (scale c v) ≡ scale c (U v)
      preserves-norm : (v : Vector) → norm (U v) ≡ norm v
      inverse-after : (v : Vector) → inverse (U v) ≡ v
      inverse-before : (v : Vector) → U (inverse v) ≡ v

module Operational = Certificate ComplexCompletion V.Vector MetricCompletionCandidate
  V.add V.scale N.vectorNormSquared
open Operational using (LinearNormEquivalence)

abstract
  left-local-unitary : (t : MetricCompletionCandidate) → LinearNormEquivalence (L.leftLocal t)
  left-local-unitary t .LinearNormEquivalence.inverse = N.leftInverse t
  left-local-unitary t .LinearNormEquivalence.additive = left-additive t
  left-local-unitary t .LinearNormEquivalence.homogeneous = left-homogeneous t
  left-local-unitary t .LinearNormEquivalence.preserves-norm = N.left-local-norm t
  left-local-unitary t .LinearNormEquivalence.inverse-after = N.left-inverse-after t
  left-local-unitary t .LinearNormEquivalence.inverse-before = N.left-inverse-before t

  right-local-unitary : (t : MetricCompletionCandidate) → LinearNormEquivalence (L.rightLocal t)
  right-local-unitary t .LinearNormEquivalence.inverse = N.rightInverse t
  right-local-unitary t .LinearNormEquivalence.additive = right-additive t
  right-local-unitary t .LinearNormEquivalence.homogeneous = right-homogeneous t
  right-local-unitary t .LinearNormEquivalence.preserves-norm = N.right-local-norm t
  right-local-unitary t .LinearNormEquivalence.inverse-after = N.right-inverse-after t
  right-local-unitary t .LinearNormEquivalence.inverse-before = N.right-inverse-before t
