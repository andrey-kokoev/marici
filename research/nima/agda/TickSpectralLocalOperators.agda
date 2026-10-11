{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralLocalOperators where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import ConstructiveComplexCompletion
open import CauchyMetricEquivalence using (MetricCompletionCandidate; embedMetricℚ)
open import CauchyCompletionCommRing using (CompletionCommRing; oneCompletion)
open import CauchyCompletionAbGroup using (zeroCompletion; completion-+IdR)
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding using (embedℚ-preserves-sum)
open import RationalAnalyticSubstrate using (one-half; one-half-double)
open import TickComplexCompletionRing using (ComplexCompletionCommRing)
import TickComplexNativeOperators as N
open import TickCompletionPhase using (phase; phase-start)
open import TickMachinPiEndpointContract using (machinPi)
open import TickMachinEndpoints using (machin-phase-half-turn)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  plus minus : fst R → fst R → fst R → fst R
  plus h x y = h · (x + y)
  minus h x y = h · (x + (- y))
  spectral : fst R → fst R → fst R → fst R → fst R
  spectral h z x y = plus h x y + z · minus h x y

  abstract
    at-one-expand : (h x y : fst R) → spectral h 1r x y ≡ (h + h) · x
    at-one-expand h x y = solve! R
    at-negative-one-expand : (h x y : fst R) → spectral h (- 1r) x y ≡ (h + h) · y
    at-negative-one-expand h x y = solve! R
    normalized : (h x : fst R) → h + h ≡ 1r → (h + h) · x ≡ x
    normalized h x double = cong (_· x) double ∙ ·IdL x
    at-one : (h : fst R) → h + h ≡ 1r → (x y : fst R) → spectral h 1r x y ≡ x
    at-one h double x y = at-one-expand h x y ∙ normalized h x double
    at-negative-one : (h : fst R) → h + h ≡ 1r → (x y : fst R) → spectral h (- 1r) x y ≡ y
    at-negative-one h double x y = at-negative-one-expand h x y ∙ normalized h y double
    neg-zero : - 0r ≡ 0r
    neg-zero = solve! R

module A = Algebra ComplexCompletionCommRing
module Real = Algebra CompletionCommRing
module V = N.Operational

halfComplex : ComplexCompletion
halfComplex = complex (embedMetricℚ one-half) zeroCompletion

abstract
  halfComplex-double : halfComplex +complex halfComplex ≡ oneComplex
  halfComplex-double = complex-ext _ _
    (sym (embedℚ-preserves-sum one-half one-half) ∙ cong embedMetricℚ one-half-double)
    (completion-+IdR zeroCompletion)

  phase-finish-negative-one : phase machinPi oneCompletion ≡ negComplex oneComplex
  phase-finish-negative-one = machin-phase-half-turn
    ∙ complex-ext _ _ refl (sym Real.neg-zero)

-- E+ = (I+P)/2, E- = (I-P)/2, U(t) = E+ + phase(pi,t) E-.
-- The same native flip P appears in both spectral components.
positiveProjector negativeProjector : (V.Vector → V.Vector) → V.Vector → V.Vector
positiveProjector P v j = A.plus halfComplex (v j) (P v j)
negativeProjector P v j = A.minus halfComplex (v j) (P v j)

local : (V.Vector → V.Vector) → MetricCompletionCandidate → V.Vector → V.Vector
local P t v j = A.spectral halfComplex (phase machinPi t) (v j) (P v j)

abstract
  local-start : (P : V.Vector → V.Vector) (v : V.Vector) → local P zeroCompletion v ≡ v
  local-start P v = funExt λ j →
    cong (λ z → A.spectral halfComplex z (v j) (P v j)) (phase-start machinPi)
    ∙ A.at-one halfComplex halfComplex-double (v j) (P v j)

  local-finish : (P : V.Vector → V.Vector) (v : V.Vector) → local P oneCompletion v ≡ P v
  local-finish P v = funExt λ j →
    cong (λ z → A.spectral halfComplex z (v j) (P v j)) phase-finish-negative-one
    ∙ A.at-negative-one halfComplex halfComplex-double (v j) (P v j)

leftLocal rightLocal : MetricCompletionCandidate → V.Vector → V.Vector
leftLocal = local V.left
rightLocal = local V.right

left-start : (v : V.Vector) → leftLocal zeroCompletion v ≡ v
left-start = local-start V.left
left-finish : (v : V.Vector) → leftLocal oneCompletion v ≡ V.left v
left-finish = local-finish V.left
right-start : (v : V.Vector) → rightLocal zeroCompletion v ≡ v
right-start = local-start V.right
right-finish : (v : V.Vector) → rightLocal oneCompletion v ≡ V.right v
right-finish = local-finish V.right
