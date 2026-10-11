{-# OPTIONS --safe --cubical --guardedness #-}
module TickSpectralProjectorLaws where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Data.Sigma.Base using (_,_)
open import TickComplexCompletionRing using (ComplexCompletionCommRing)
import TickSpectralLocalOperators as L
open import CauchyMetricEquivalence using (MetricCompletionCandidate)
open import CauchyAdditionCongruence using (_+completion_)
open import TickCompletionPhase using (phase)
open import TickMachinPiEndpointContract using (machinPi)
open import TickPhaseComposition using (operational-phase-addition)

module Polynomial (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  open L.Algebra R using (plus; minus; spectral)
  abstract
    pp : (h x y : fst R) → plus h (plus h x y) (plus h y x) ≡ (h + h) · plus h x y
    pp h x y = solve! R
    mm : (h x y : fst R) → minus h (minus h x y) (minus h y x) ≡ (h + h) · minus h x y
    mm h x y = solve! R
    pm : (h x y : fst R) → plus h (minus h x y) (minus h y x) ≡ 0r
    pm h x y = solve! R
    mp : (h x y : fst R) → minus h (plus h x y) (plus h y x) ≡ 0r
    mp h x y = solve! R
    sum : (h x y : fst R) → plus h x y + minus h x y ≡ (h + h) · x
    sum h x y = solve! R
    composition : (h z w x y : fst R) →
      spectral h z (spectral h w x y) (spectral h w y x) ≡ (h + h) · spectral h (z · w) x y
    composition h z w x y = solve! R

-- Every involutive index permutation, in particular both native flips.
module Permutation (R : CommRing ℓ-zero) (J : Type) (k : J → J)
  (kk : (j : J) → k (k j) ≡ j) (h : fst R)
  (double : CommRingStr._+_ (snd R) h h ≡ CommRingStr.1r (snd R)) where
  open CommRingStr (snd R)
  module A = L.Algebra R
  module P = Polynomial R
  Vector = J → fst R
  positive negative : Vector → Vector
  positive v j = A.plus h (v j) (v (k j))
  negative v j = A.minus h (v j) (v (k j))
  spectral : fst R → Vector → Vector
  spectral z v j = A.spectral h z (v j) (v (k j))

  abstract
    positive-idempotent : (v : Vector) → positive (positive v) ≡ positive v
    positive-idempotent v = funExt λ j →
      cong (λ x → A.plus h (positive v j) (A.plus h (v (k j)) x)) (cong v (kk j))
      ∙ P.pp h (v j) (v (k j)) ∙ A.normalized h (positive v j) double
    negative-idempotent : (v : Vector) → negative (negative v) ≡ negative v
    negative-idempotent v = funExt λ j →
      cong (λ x → A.minus h (negative v j) (A.minus h (v (k j)) x)) (cong v (kk j))
      ∙ P.mm h (v j) (v (k j)) ∙ A.normalized h (negative v j) double
    positive-negative-zero : (v : Vector) → positive (negative v) ≡ (λ _ → 0r)
    positive-negative-zero v = funExt λ j →
      cong (λ x → A.plus h (negative v j) (A.minus h (v (k j)) x)) (cong v (kk j))
      ∙ P.pm h (v j) (v (k j))
    negative-positive-zero : (v : Vector) → negative (positive v) ≡ (λ _ → 0r)
    negative-positive-zero v = funExt λ j →
      cong (λ x → A.minus h (positive v j) (A.plus h (v (k j)) x)) (cong v (kk j))
      ∙ P.mp h (v j) (v (k j))
    decomposition : (v : Vector) → (λ j → positive v j + negative v j) ≡ v
    decomposition v = funExt λ j → P.sum h (v j) (v (k j)) ∙ A.normalized h (v j) double
    spectral-composition : (z w : fst R) (v : Vector) → spectral z (spectral w v) ≡ spectral (z · w) v
    spectral-composition z w v = funExt λ j →
      cong (λ x → A.spectral h z (spectral w v j) (A.spectral h w (v (k j)) x)) (cong v (kk j))
      ∙ P.composition h z w (v j) (v (k j))
      ∙ A.normalized h (spectral (z · w) v j) double

module V = L.V
leftIndex rightIndex : V.Label → V.Label
leftIndex (a , b) = V.flip a , b
rightIndex (a , b) = a , V.flip b
leftIndex-involutive : (j : V.Label) → leftIndex (leftIndex j) ≡ j
leftIndex-involutive (a , b) = cong (λ x → x , b) (V.flip-involutive a)
rightIndex-involutive : (j : V.Label) → rightIndex (rightIndex j) ≡ j
rightIndex-involutive (a , b) = cong (λ x → a , x) (V.flip-involutive b)

module Left = Permutation ComplexCompletionCommRing V.Label leftIndex leftIndex-involutive L.halfComplex L.halfComplex-double
module Right = Permutation ComplexCompletionCommRing V.Label rightIndex rightIndex-involutive L.halfComplex L.halfComplex-double

-- Public exact links to the operators constructed in the previous component.
left-positive-correspondence : Left.positive ≡ L.positiveProjector V.left
left-positive-correspondence = refl
left-negative-correspondence : Left.negative ≡ L.negativeProjector V.left
left-negative-correspondence = refl
right-positive-correspondence : Right.positive ≡ L.positiveProjector V.right
right-positive-correspondence = refl
right-negative-correspondence : Right.negative ≡ L.negativeProjector V.right
right-negative-correspondence = refl

abstract
  left-local-composition : (s t : MetricCompletionCandidate) (v : V.Vector) →
    L.leftLocal s (L.leftLocal t v) ≡ L.leftLocal (s +completion t) v
  left-local-composition s t v = Left.spectral-composition (phase machinPi s) (phase machinPi t) v
    ∙ cong (λ z → Left.spectral z v) (sym (operational-phase-addition machinPi s t))
  right-local-composition : (s t : MetricCompletionCandidate) (v : V.Vector) →
    L.rightLocal s (L.rightLocal t v) ≡ L.rightLocal (s +completion t) v
  right-local-composition s t v = Right.spectral-composition (phase machinPi s) (phase machinPi t) v
    ∙ cong (λ z → Right.spectral z v) (sym (operational-phase-addition machinPi s t))
