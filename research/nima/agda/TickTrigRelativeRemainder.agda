{-# OPTIONS --safe --cubical --guardedness #-}
module TickTrigRelativeRemainder where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero)
open import Cubical.Relation.Nullary using (yes; no)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure using (precision-nonnegative)
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-bound-product; nonnegative-value-magnitude)
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import TickSmallArctangent using (small-input≤one)
open import TickAtanFirstOrderBounds using (one-magnitude)
import TickOperationalTrigFirstOrder as First
module Cos = First.Cos
module Sin = First.Sin

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  negative-square : (q : fst R) → (-S q) ·S (-S q) ≡ q ·S q
  negative-square q = solve! R
  quartic-scale : (p h : fst R) →
    (((-S (p ·S h)) ·S (-S (p ·S h))) ·S ((-S (p ·S h)) ·S (-S (p ·S h)))) +S
    (((-S (p ·S h)) ·S (-S (p ·S h))) ·S ((-S (p ·S h)) ·S (-S (p ·S h)))) ≡
    (((p ·S p) ·S (p ·S p)) ·S ((h ·S h) +S (h ·S h))) ·S (h ·S h)
  quartic-scale p h = solve! R
module R = Algebra PreferredℚCommRing

squareℚ : Q.ℚ → Q.ℚ
squareℚ q = q Q.· q

abstract
  square-nonnegative : (q : Q.ℚ) → 0 ≤ squareℚ q
  square-nonnegative q with <Dec q 0
  ... | no not-negative = nonnegative-bound-product q q
    (≮→≥ q 0 not-negative) (≮→≥ q 0 not-negative)
  ... | yes negative = subst (0 ≤_) (R.negative-square q)
    (nonnegative-bound-product (Q.- q) (Q.- q)
      (nonpositive→negative-nonnegative q (<Weaken≤ q 0 negative))
      (nonpositive→negative-nonnegative q (<Weaken≤ q 0 negative)))

  square-upper : (q B : Q.ℚ) → 0 ≤ B → MagnitudeBound q B → squareℚ q ≤ squareℚ B
  square-upper q B positive bound = positive-upper
    (arbitrary-multiplier-bound q B q B positive positive bound bound)

  -- Unlike a fixed-radius estimate, this retains the actual angle squared.
  cosine-partial-quadratic : (q : Q.ℚ) → MagnitudeBound q one-half → (n : ℕ) →
    MagnitudeBound (cosinePartialSum q n Q.+ (Q.- 1)) (squareℚ q)
  cosine-partial-quadratic q small n with <Dec q 0
  ... | no not-negative = Cos.sum-remainder-bound q q small (≮→≥ q 0 not-negative)
    (nonnegative-value-magnitude q q (≮→≥ q 0 not-negative) (isRefl≤ q) (≮→≥ q 0 not-negative))
    one-magnitude n
  ... | yes negative = subst (MagnitudeBound _) (R.negative-square q)
    (Cos.sum-remainder-bound q (Q.- q) small positive
      (transport-magnitude q (Q.- (Q.- q)) (Q.- q) (sym (Q.-Invol q))
        (negate-magnitude-bound (Q.- q) (Q.- q)
          (nonnegative-value-magnitude (Q.- q) (Q.- q) positive (isRefl≤ (Q.- q)) positive)))
      one-magnitude n)
    where
    positive : 0 ≤ Q.- q
    positive = nonpositive→negative-nonnegative q (<Weaken≤ q 0 negative)

  sine-partial-quadratic : (q : Q.ℚ) → MagnitudeBound q one-half → (n : ℕ) →
    MagnitudeBound (sinePartialSum q n Q.+ (Q.- q)) (squareℚ q)
  sine-partial-quadratic q small n with <Dec q 0
  ... | no not-negative = Sin.sum-remainder-bound q q small (≮→≥ q 0 not-negative)
    (nonnegative-value-magnitude q q (≮→≥ q 0 not-negative) (isRefl≤ q) (≮→≥ q 0 not-negative))
    (small-input≤one q small) n
  ... | yes negative = subst (MagnitudeBound _) (R.negative-square q)
    (Sin.sum-remainder-bound q (Q.- q) small positive
      (transport-magnitude q (Q.- (Q.- q)) (Q.- q) (sym (Q.-Invol q))
        (negate-magnitude-bound (Q.- q) (Q.- q)
          (nonnegative-value-magnitude (Q.- q) (Q.- q) positive (isRefl≤ (Q.- q)) positive)))
      (small-input≤one q small) n)
    where
    positive : 0 ≤ Q.- q
    positive = nonpositive→negative-nonnegative q (<Weaken≤ q 0 negative)

cosineResidual sineResidual : Q.ℚ → ℕ → Q.ℚ
cosineResidual q n = cosinePartialSum q n Q.+ (Q.- 1)
sineResidual q n = sinePartialSum q n Q.+ (Q.- q)

abstract
  partial-residual-norm-bound : (q : Q.ℚ) → MagnitudeBound q one-half → (n m : ℕ) →
    squareℚ (cosineResidual q n) Q.+ squareℚ (sineResidual q m) ≤
    squareℚ (squareℚ q) Q.+ squareℚ (squareℚ q)
  partial-residual-norm-bound q small n m = ≤Monotone+
    (squareℚ (cosineResidual q n)) (squareℚ (squareℚ q))
    (squareℚ (sineResidual q m)) (squareℚ (squareℚ q))
    (square-upper (cosineResidual q n) (squareℚ q) (square-nonnegative q) (cosine-partial-quadratic q small n))
    (square-upper (sineResidual q m) (squareℚ q) (square-nonnegative q) (sine-partial-quadratic q small m))

  -- The explicit radius budget will later be instantiated by a dyadic modulus.
  -- Both Taylor cutoffs are arbitrary and independent. No nonzero h premise.
  scaled-relative-residual-bound : (p h P d e : Q.ℚ) → 0 ≤ P → 0 ≤ d →
    MagnitudeBound p P → MagnitudeBound h d → MagnitudeBound (Q.- (p Q.· h)) one-half →
    squareℚ (squareℚ P) Q.· (squareℚ d Q.+ squareℚ d) ≤ squareℚ e →
    (n m : ℕ) →
    squareℚ (cosineResidual (Q.- (p Q.· h)) n) Q.+ squareℚ (sineResidual (Q.- (p Q.· h)) m) ≤
    squareℚ e Q.· squareℚ h
  scaled-relative-residual-bound p h P d e Ppositive dpositive pbound hbound small budget n m =
    isTrans≤ (squareℚ (cosineResidual (Q.- (p Q.· h)) n) Q.+ squareℚ (sineResidual (Q.- (p Q.· h)) m))
      (squareℚ (squareℚ (Q.- (p Q.· h))) Q.+ squareℚ (squareℚ (Q.- (p Q.· h))))
      (squareℚ e Q.· squareℚ h) (partial-residual-norm-bound (Q.- (p Q.· h)) small n m)
      (subst (_≤ squareℚ e Q.· squareℚ h) (sym (R.quartic-scale p h))
        (≤-·o (squareℚ (squareℚ p) Q.· (squareℚ h Q.+ squareℚ h)) (squareℚ e)
          (squareℚ h) (square-nonnegative h)
          (isTrans≤ (squareℚ (squareℚ p) Q.· (squareℚ h Q.+ squareℚ h))
            (squareℚ (squareℚ P) Q.· (squareℚ d Q.+ squareℚ d)) (squareℚ e) coefficient budget)))
    where
    p²bound : squareℚ p ≤ squareℚ P
    p²bound = square-upper p P Ppositive pbound
    p⁴bound : squareℚ (squareℚ p) ≤ squareℚ (squareℚ P)
    p⁴bound = square-upper (squareℚ p) (squareℚ P) (square-nonnegative P)
      (nonnegative-value-magnitude (squareℚ p) (squareℚ P) (square-nonnegative p) p²bound (square-nonnegative P))
    h²bound : squareℚ h ≤ squareℚ d
    h²bound = square-upper h d dpositive hbound
    hsum-positive : 0 ≤ squareℚ h Q.+ squareℚ h
    hsum-positive = subst (_≤ squareℚ h Q.+ squareℚ h) (Q.+IdL 0)
      (≤Monotone+ 0 (squareℚ h) 0 (squareℚ h) (square-nonnegative h) (square-nonnegative h))
    coefficient : squareℚ (squareℚ p) Q.· (squareℚ h Q.+ squareℚ h) ≤
      squareℚ (squareℚ P) Q.· (squareℚ d Q.+ squareℚ d)
    coefficient = isTrans≤
      (squareℚ (squareℚ p) Q.· (squareℚ h Q.+ squareℚ h))
      (squareℚ (squareℚ P) Q.· (squareℚ h Q.+ squareℚ h))
      (squareℚ (squareℚ P) Q.· (squareℚ d Q.+ squareℚ d))
      (≤-·o (squareℚ (squareℚ p)) (squareℚ (squareℚ P)) (squareℚ h Q.+ squareℚ h) hsum-positive p⁴bound)
      (left-multiply-monotone (squareℚ (squareℚ P)) (squareℚ h Q.+ squareℚ h)
        (squareℚ d Q.+ squareℚ d) (square-nonnegative (squareℚ P))
        (≤Monotone+ (squareℚ h) (squareℚ d) (squareℚ h) (squareℚ d) h²bound h²bound))
