{-# OPTIONS --safe --cubical --guardedness #-}
module TickAtanGridSmallAngle where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.Data.Int.Order as ZO
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionCommRing
open import TickCompletionMagnitudeBounds
open import TickSmallAngleDensity using (completion-bound-weaken)
open import TickAtanFirstOrderBounds using (scale; eight)
open import TickAtanCompletionFirstOrder using (atanIncrement)
open import TickAtanCayleyIncrement using (relativeParameter; relativeAtanRemainder; relativeBudget; relative-atan-grid-bound)
open import TickCayleyGridIncrement using (gridValue; gridProductInverse; grid-product-inverse-nonnegative; grid-product-inverse≤one)

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  restore : (a b : fst R) → (a +S (-S b)) +S b ≡ a
  restore a b = solve! R
  budget-factor : (c h e : fst R) → ((c ·S (e ·S e)) +S (c ·S (e ·S e))) +S h ·S (e ·S e) ≡
    (((c +S c) +S h) ·S e) ·S e
  budget-factor c h e = solve! R
module C = Paths CompletionCommRing
module R = Paths PreferredℚCommRing

abstract
  restore-increment-bound : (a : MetricCompletionCandidate) (t B e : Q.ℚ) →
    CompletionMagnitudeBound (a +completion (-completion (embedMetricℚ t))) B → MagnitudeBound t e →
    CompletionMagnitudeBound a (B Q.+ e)
  restore-increment-bound a t B e remainder ht = completion-bound-path
    ((a +completion (-completion (embedMetricℚ t))) +completion embedMetricℚ t) a (B Q.+ e)
    (C.restore a (embedMetricℚ t))
    (completion-magnitude-add (a +completion (-completion (embedMetricℚ t))) (embedMetricℚ t) B e
      remainder (embedded-magnitude-bound t e ht))

  coefficient-small : ((eight Q.+ eight) Q.+ one-half) Q.· precision 6 ≤ 1
  coefficient-small = 95 , refl

  relative-budget≤step : (e : Q.ℚ) → 0 ≤ e → e ≤ precision 6 → relativeBudget e ≤ e
  relative-budget≤step e eh small = subst2 _≤_
    (sym (R.budget-factor eight one-half e)) (Q.·IdL e)
    (≤-·o (((eight Q.+ eight) Q.+ one-half) Q.· e) 1 e eh
      (isTrans≤ (((eight Q.+ eight) Q.+ one-half) Q.· e)
        (((eight Q.+ eight) Q.+ one-half) Q.· precision 6) 1
        (left-multiply-monotone ((eight Q.+ eight) Q.+ one-half) e (precision 6)
          coefficient≥0 small) coefficient-small))
    where
    coefficient≥0 : 0 ≤ ((eight Q.+ eight) Q.+ one-half)
    coefficient≥0 = ZO.zero-≤pos

relative-parameter-bound : (n m d : ℕ) (e : Q.ℚ) → 0 ≤ e →
  MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e → MagnitudeBound (relativeParameter n m d) e
relative-parameter-bound n m d e eh hd = subst (MagnitudeBound (relativeParameter n m d)) (Q.·IdR e)
  (nonnegative-multiplier-bound (gridValue m d Q.+ (Q.- gridValue n d)) e (gridProductInverse n m d) 1 eh hd
    (grid-product-inverse-nonnegative n m d) (grid-product-inverse≤one n m d))

atan-grid-increment-bound : (n m d : ℕ) (e : Q.ℚ)
  (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half) →
  0 ≤ e → e ≤ precision 6 → MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e →
  CompletionMagnitudeBound (atanIncrement (gridValue n d) (gridValue m d) hx hy) (e Q.+ e)
atan-grid-increment-bound n m d e hx hy eh small hd = completion-bound-weaken
  (atanIncrement (gridValue n d) (gridValue m d) hx hy) (relativeBudget e Q.+ e) (e Q.+ e)
  (≤Monotone+ (relativeBudget e) e e e (relative-budget≤step e eh small) (isRefl≤ e))
  (restore-increment-bound (atanIncrement (gridValue n d) (gridValue m d) hx hy)
    (relativeParameter n m d) (relativeBudget e) e
    (relative-atan-grid-bound n m d e hx hy eh hd) (relative-parameter-bound n m d e eh hd))

fourStep : Q.ℚ → Q.ℚ
fourStep e = (e Q.+ e) Q.+ (e Q.+ e)

doubledAtanIncrement : (n m d : ℕ) → MagnitudeBound (gridValue n d) one-half →
  MagnitudeBound (gridValue m d) one-half → MetricCompletionCandidate
doubledAtanIncrement n m d hx hy = atanIncrement (gridValue n d) (gridValue m d) hx hy
  +completion atanIncrement (gridValue n d) (gridValue m d) hx hy

doubled-atan-grid-bound : (n m d : ℕ) (e : Q.ℚ)
  (hx : MagnitudeBound (gridValue n d) one-half) (hy : MagnitudeBound (gridValue m d) one-half) →
  0 ≤ e → e ≤ precision 6 → MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e →
  CompletionMagnitudeBound (doubledAtanIncrement n m d hx hy) (fourStep e)
doubled-atan-grid-bound n m d e hx hy eh small hd = completion-magnitude-add
  (atanIncrement (gridValue n d) (gridValue m d) hx hy) (atanIncrement (gridValue n d) (gridValue m d) hx hy)
  (e Q.+ e) (e Q.+ e) (atan-grid-increment-bound n m d e hx hy eh small hd)
  (atan-grid-increment-bound n m d e hx hy eh small hd)

four-step-small : (e : Q.ℚ) → e ≤ precision 6 → fourStep e ≤ precision 2
four-step-small e h = isTrans≤ (fourStep e) (precision 4) (precision 2)
  (subst (fourStep e ≤_) (cong₂ Q._+_ (precision-refines-double 5) (precision-refines-double 5)
    ∙ precision-refines-double 4)
    (≤Monotone+ (e Q.+ e) (precision 6 Q.+ precision 6) (e Q.+ e) (precision 6 Q.+ precision 6)
      (≤Monotone+ e (precision 6) e (precision 6) h h) (≤Monotone+ e (precision 6) e (precision 6) h h)))
  (precision-antitone 2 4 (2 , refl))
