{-# OPTIONS --safe --cubical --guardedness #-}
module TickAtanCayleyIncrement where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure using (one-half-nonnegative)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyRationalEmbedding
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import CauchyCompletionCommRing
open import TickCompletionMagnitudeBounds
open import TickAtanFirstOrderBounds using (scale)
open import TickAtanCompletionFirstOrder using (atanIncrement)
open import TickAtanCompletionSlope using (atanSlope; atanSlopeRemainder; atan-slope-completion-bound)
open import TickCayleyGridIncrement using (gridValue; gridProductInverse; grid-increment-quadratic-bound)
open import TickCayleyGridSlope using (rational-product-equation; grid-slope-is-rational)

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  split-difference : (a b c : fst R) → a +S (-S c) ≡ (a +S (-S b)) +S (b +S (-S c))
  split-difference a b c = solve! R
module C = Paths CompletionCommRing

abstract
  reverse-difference-bound : (s t B : Q.ℚ) → MagnitudeBound (t Q.+ (Q.- s)) B → MagnitudeBound (s Q.+ (Q.- t)) B
  reverse-difference-bound s t B h = transport-magnitude (s Q.+ (Q.- t)) (Q.- (t Q.+ (Q.- s))) B
    (sym (ProductSignPaths.negative-difference PreferredℚCommRing t s))
    (negate-magnitude-bound (t Q.+ (Q.- s)) B h)

  rational-slope-product : (delta r : Q.ℚ) (g : MetricCompletionCandidate) → g ≡ embedMetricℚ r →
    preferredCompletionMultiplication (embedMetricℚ delta) g ≡ embedMetricℚ (delta Q.· r)
  rational-slope-product delta r g path = cong (preferredCompletionMultiplication (embedMetricℚ delta)) path
    ∙ rational-product-equation delta r (delta Q.· r) refl

  relative-remainder-decomposition : (a b : MetricCompletionCandidate) (s t : Q.ℚ) → b ≡ embedMetricℚ s →
    (a +completion (-completion (embedMetricℚ t))) ≡
    (a +completion (-completion b)) +completion embedMetricℚ (s Q.+ (Q.- t))
  relative-remainder-decomposition a b s t path = C.split-difference a b (embedMetricℚ t)
    ∙ cong ((a +completion (-completion b)) +completion_)
      (cong₂ _+completion_ path (embedℚ-preserves-negation t) ∙ sym (embedℚ-preserves-sum s (Q.- t)))

  relative-clock-bound : (a b : MetricCompletionCandidate) (s t B E : Q.ℚ) → b ≡ embedMetricℚ s →
    CompletionMagnitudeBound (a +completion (-completion b)) B → MagnitudeBound (s Q.+ (Q.- t)) E →
    CompletionMagnitudeBound (a +completion (-completion (embedMetricℚ t))) (B Q.+ E)
  relative-clock-bound a b s t B E path bound correction = completion-bound-path
    ((a +completion (-completion b)) +completion embedMetricℚ (s Q.+ (Q.- t)))
    (a +completion (-completion (embedMetricℚ t))) (B Q.+ E)
    (sym (relative-remainder-decomposition a b s t path))
    (completion-magnitude-add (a +completion (-completion b)) (embedMetricℚ (s Q.+ (Q.- t))) B E
      bound (embedded-magnitude-bound (s Q.+ (Q.- t)) E correction))

relativeParameter : ℕ → ℕ → ℕ → Q.ℚ
relativeParameter n m d = (gridValue m d Q.+ (Q.- gridValue n d)) Q.· gridProductInverse n m d

relativeAtanRemainder : (n m d : ℕ) →
  MagnitudeBound (gridValue n d) one-half → MagnitudeBound (gridValue m d) one-half → MetricCompletionCandidate
relativeAtanRemainder n m d hx hy = atanIncrement (gridValue n d) (gridValue m d) hx hy
  +completion (-completion (embedMetricℚ (relativeParameter n m d)))

relativeBudget : Q.ℚ → Q.ℚ
relativeBudget e = (scale e Q.+ scale e) Q.+ one-half Q.· (e Q.· e)

-- Exact identification with the original arctangent completion values is
-- inherited from atanIncrement/atanCompletion. No Cayley trig law is used.
relative-atan-grid-bound : (n m d : ℕ) (e : Q.ℚ)
  (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half) →
  0 ≤ e → MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e →
  CompletionMagnitudeBound (relativeAtanRemainder n m d hx hy) (relativeBudget e)
relative-atan-grid-bound n m d e hx hy eh hd = relative-clock-bound
  (atanIncrement (gridValue n d) (gridValue m d) hx hy)
  (preferredCompletionMultiplication (embedMetricℚ (gridValue m d Q.+ (Q.- gridValue n d))) (atanSlope (gridValue n d) hx))
  ((gridValue m d Q.+ (Q.- gridValue n d)) Q.· gridProductInverse n n d) (relativeParameter n m d)
  (scale e Q.+ scale e) (one-half Q.· (e Q.· e))
  (rational-slope-product (gridValue m d Q.+ (Q.- gridValue n d)) (gridProductInverse n n d)
    (atanSlope (gridValue n d) hx) (grid-slope-is-rational n d hx))
  (atan-slope-completion-bound (gridValue n d) (gridValue m d) e hx hy eh hd) correction
  where
  x y delta s t : Q.ℚ
  x = gridValue n d
  y = gridValue m d
  delta = y Q.+ (Q.- x)
  s = delta Q.· gridProductInverse n n d
  t = relativeParameter n m d
  correction : MagnitudeBound (s Q.+ (Q.- t)) (one-half Q.· (e Q.· e))
  correction = reverse-difference-bound s t (one-half Q.· (e Q.· e))
    (grid-increment-quadratic-bound n m d one-half e one-half-nonnegative eh hx hd)
