{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralWitnessCorrespondence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_,_)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import CauchyMetricEquivalence using (MetricCompletionCandidate; embedMetricℚ)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import CauchyNegation using (-completion_)
open import RationalAnalyticSubstrate using (one-half)
open import ConstructiveComplexCompletion
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
import TickComplexCompletionRing as Ring
import TickComplexConjugation as Conj
import TickSpectralLocalOperators as L
import TickSpectralFactorOperators as F
import TickSpectralRetainedReturn as R
import TickSpectralGlobalPath as Path
import TickSpectralProjectorLaws as P
import TickCompletionMetricInterval as I
import TickCompletionClippedTime as Time
import TickComplexNativeBasis as Basis
module V = L.V
module G = R.G

-- Independent coefficient presentation of the exported 2x2 spectral rule.
-- It is instantiated at the actual operational phase, not standard exp.
module Coefficients (Real : CommRing ℓ-zero) where
  open CommRingStr (snd Real)
  module C = Conj.Laws Real
  module Pair = C.P
  module M = F.Factor Pair.ring
  abstract
    conjugate-plus : (h : fst Real) (z : Pair.C) →
      C.conjugate (Pair.mul (C.real h) (Pair.add Pair.one z)) ≡
      Pair.mul (C.real h) (Pair.add Pair.one (C.conjugate z))
    conjugate-plus h (a , b) = cong₂ _,_ (solve! Real) (solve! Real)
    conjugate-minus : (h : fst Real) (z : Pair.C) →
      C.conjugate (Pair.mul (C.real h) (Pair.add Pair.one (Pair.neg z))) ≡
      Pair.mul (C.real h) (Pair.add Pair.one (Pair.neg (C.conjugate z)))
    conjugate-minus h (a , b) = cong₂ _,_ (solve! Real) (solve! Real)
    real-product : (p h : fst Real) → C.conjugate (Pair.mul (C.real p) (C.real h)) ≡ Pair.mul (C.real p) (C.real h)
    real-product p h = cong₂ _,_ refl (solve! Real)
    real-negative-product : (p h : fst Real) → C.conjugate (Pair.neg (Pair.mul (C.real p) (C.real h))) ≡ Pair.neg (Pair.mul (C.real p) (C.real h))
    real-negative-product p h = cong₂ _,_ (solve! Real) (solve! Real)

module C = Coefficients CompletionCommRing
adjoint : F.F.Matrix → F.F.Matrix
adjoint A i j = conjugateComplex (A j i)

abstract
  local-adjoint-is-inverse : (t : MetricCompletionCandidate) → adjoint (F.localMatrix t) ≡ F.inverseMatrix t
  local-adjoint-is-inverse t = funExt λ
    { false → funExt λ
      { false → C.conjugate-plus (embedMetricℚ one-half) (phase machinPi t)
      ; true → C.conjugate-minus (embedMetricℚ one-half) (phase machinPi t) }
    ; true → funExt λ
      { false → C.conjugate-minus (embedMetricℚ one-half) (phase machinPi t)
      ; true → C.conjugate-plus (embedMetricℚ one-half) (phase machinPi t) } }

  hamiltonian-self-adjoint : adjoint F.hamiltonianMatrix ≡ F.hamiltonianMatrix
  hamiltonian-self-adjoint = funExt λ
    { false → funExt λ
      { false → C.real-product machinPi (embedMetricℚ one-half)
      ; true → C.real-negative-product machinPi (embedMetricℚ one-half) }
    ; true → funExt λ
      { false → C.real-negative-product machinPi (embedMetricℚ one-half)
      ; true → C.real-product machinPi (embedMetricℚ one-half) } }

-- Matrix specification written independently of the implemented stencil.
referenceLocalMatrix : MetricCompletionCandidate → F.F.Matrix
referenceLocalMatrix t false false = L.halfComplex ·complex (oneComplex +complex phase machinPi t)
referenceLocalMatrix t false true = L.halfComplex ·complex (oneComplex +complex negComplex (phase machinPi t))
referenceLocalMatrix t true false = L.halfComplex ·complex (oneComplex +complex negComplex (phase machinPi t))
referenceLocalMatrix t true true = L.halfComplex ·complex (oneComplex +complex phase machinPi t)
referenceHamiltonian : F.F.Matrix
referenceHamiltonian false false = complex machinPi zeroCompletion ·complex L.halfComplex
referenceHamiltonian false true = negComplex (complex machinPi zeroCompletion ·complex L.halfComplex)
referenceHamiltonian true false = negComplex (complex machinPi zeroCompletion ·complex L.halfComplex)
referenceHamiltonian true true = complex machinPi zeroCompletion ·complex L.halfComplex

local-matrix-specification : (t : MetricCompletionCandidate) → F.localMatrix t ≡ referenceLocalMatrix t
local-matrix-specification t = funExt λ { false → funExt λ { false → refl ; true → refl } ; true → funExt λ { false → refl ; true → refl } }
hamiltonian-matrix-specification : F.hamiltonianMatrix ≡ referenceHamiltonian
hamiltonian-matrix-specification = funExt λ { false → funExt λ { false → refl ; true → refl } ; true → funExt λ { false → refl ; true → refl } }

abstract
  left-free-linearization : (s : V.Label) → V.left (Basis.basis s) ≡ Basis.basis (P.leftIndex s)
  left-free-linearization = Basis.Operational.basis-left
  right-free-linearization : (s : V.Label) → V.right (Basis.basis s) ≡ Basis.basis (P.rightIndex s)
  right-free-linearization = Basis.Operational.basis-right
  left-spectral-specification : (t : MetricCompletionCandidate) (v : V.Vector) → L.leftLocal t v ≡ F.F.left (referenceLocalMatrix t) v
  left-spectral-specification t v = sym (F.left-matrix t v) ∙ cong (λ A → F.F.left A v) (local-matrix-specification t)
  right-spectral-specification : (t : MetricCompletionCandidate) (v : V.Vector) → L.rightLocal t v ≡ F.F.right (referenceLocalMatrix t) v
  right-spectral-specification t v = sym (F.right-matrix t v) ∙ cong (λ A → F.F.right A v) (local-matrix-specification t)

first second : G.Schedule → Path.IndexMap
first G.leftFirst = P.rightIndex
first G.rightFirst = P.leftIndex
second G.leftFirst = P.leftIndex
second G.rightFirst = P.rightIndex

-- The exact exported reversed-order formula is verified on both pieces.
abstract
  return-first-piece-specification : (r : G.Schedule) (s : V.Label) (t : I.LeftPiece) →
    R.returnPath r s (fst t) ≡ L.local (Path.permute (first r)) (fst (fst t)) (R.nativeTarget s)
  return-first-piece-specification G.leftFirst s (t , bound) = Path.glued-on-left P.rightIndex P.leftIndex (fst t) (R.nativeTarget s) bound
  return-first-piece-specification G.rightFirst s (t , bound) = Path.glued-on-left P.leftIndex P.rightIndex (fst t) (R.nativeTarget s) bound
  return-second-piece-specification : (r : G.Schedule) (s : V.Label) (t : I.RightPiece) →
    R.returnPath r s (fst t) ≡ L.local (Path.permute (second r)) (Time.afterOne (fst (fst t))) (Path.permute (first r) (R.nativeTarget s))
  return-second-piece-specification G.leftFirst s (t , bound) = Path.glued-on-right P.rightIndex P.leftIndex (fst t) (R.nativeTarget s) bound
  return-second-piece-specification G.rightFirst s (t , bound) = Path.glued-on-right P.leftIndex P.rightIndex (fst t) (R.nativeTarget s) bound

-- These are kernel structural correspondence theorems. They deliberately do
-- NOT assert that a standard-real interpretation of phase equals standard exp.
