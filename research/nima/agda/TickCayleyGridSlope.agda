{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyGridSlope where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (one-half)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyCompletionCommRing
open import CauchyCompletionMultiplication
open import TickAtanGeometricCompletion
open import TickCayleyGridIncrement

module Inverses {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_; ·IdR to unit-right; ·IdL to unit-left)
  abstract
    rearrange : (d a b : fst R) → a ·S (d ·S b) ≡ (d ·S a) ·S b
    rearrange d a b = solve! R
    unique-inverse : (d a b : fst R) → d ·S a ≡ 1r → d ·S b ≡ 1r → a ≡ b
    unique-inverse d a b da db = sym (unit-right a)
      ∙ cong (a ·S_) (sym db) ∙ rearrange d a b ∙ cong (_·S b) da ∙ unit-left b
module I = Inverses CompletionCommRing

abstract
  rational-product-equation : (d r c : Q.ℚ) → d Q.· r ≡ c →
    preferredCompletionMultiplication (embedMetricℚ d) (embedMetricℚ r) ≡ embedMetricℚ c
  rational-product-equation d r c p = preferredCompletionMultiplication-preserves-rationals d r
    ∙ cong embedMetricℚ p

  completion-inverse-matches-rational : (d r : Q.ℚ) (a : MetricCompletionCandidate) →
    d Q.· r ≡ 1 → preferredCompletionMultiplication (embedMetricℚ d) a ≡ embedMetricℚ 1 →
    a ≡ embedMetricℚ r
  completion-inverse-matches-rational d r a law completion-law = I.unique-inverse
    (embedMetricℚ d) a (embedMetricℚ r) completion-law (rational-product-equation d r 1 law)

-- The arctangent geometric slope is exactly the constructed rational inverse
-- on these grids. The completion inverse and rational inverse were proved
-- independently; uniqueness connects them without assuming a Cayley law.
abstract
  grid-slope-is-rational : (n d : ℕ) (h : MagnitudeBound (gridValue n d) one-half) →
    geometricValue (gridValue n d) h ≡ embedMetricℚ (gridProductInverse n n d)
  grid-slope-is-rational n d h = completion-inverse-matches-rational
    (1 Q.+ gridValue n d Q.· gridValue n d) (gridProductInverse n n d) (geometricValue (gridValue n d) h)
    (grid-product-inverse-law n n d) (geometric-completion-inverse (gridValue n d) h)
