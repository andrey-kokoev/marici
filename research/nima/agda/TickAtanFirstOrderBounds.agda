{-# OPTIONS --safe --cubical --guardedness #-}
module TickAtanFirstOrderBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds using (weaken-magnitude-bound)
open import TaylorTermBounds using (nonnegative-bound-product; nonnegative-value-magnitude)
open import RationalTaylorApproximants using (finiteSum)
open import RationalLogTaylorApproximants using
  (atanhStepRatio; atanh-step-ratio-nonnegative; atanh-step-ratio≤one)
open import DyadicallyBoundedCauchy using (dyadicRadius; dyadicRadius-nonnegative)
open import RationalArchimedean using (exponent; dominates)
import AutomaticRationalExponentialMultiplication as Auto
import AbsoluteTaylorSeriesMultiplication as A
open import TickSmallArctangent
open import TickAtanDerivativeAlgebra

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  collect-budget : (c k s p : fst R) →
    c ·S ((k ·S s) ·S p) +S s ·S (p +S p) ≡ (c ·S k +S (1r +S 1r)) ·S (s ·S p)
  collect-budget c k s p = solve! R
  reorder-budget : (k h s p : fst R) → (k ·S h) ·S (s ·S p) ≡ (k ·S s) ·S (p ·S h)
  reorder-budget k h s p = solve! R
  split-remainder : (a b c d e f h : fst R) →
    ((a +S b) +S (-S (c +S d))) +S (-S (h ·S (e +S f))) ≡
    ((a +S (-S c)) +S (-S (h ·S e))) +S ((b +S (-S d)) +S (-S (h ·S f)))
  split-remainder a b c d e f h = solve! R
  clear-denominator : (d a h g : fst R) →
    d ·S a +S (-S h) ≡ d ·S (a +S (-S (h ·S g))) +S h ·S (d ·S g +S (-S 1r))
  clear-denominator d a h g = solve! R
  cancel-one : (g : fst R) → (1r +S (-S g)) +S (-S 1r) ≡ -S g
  cancel-one g = solve! R
  double-product : (a : fst R) → (1r +S 1r) ·S (a +S a) ≡ (a +S a) +S (a +S a)
  double-product a = solve! R
module B = Algebra PreferredℚCommRing

eight : Q.ℚ
eight = dyadicRadius 3
scale : Q.ℚ → Q.ℚ
scale e = eight Q.· (e Q.· e)
quadraticBudget : Q.ℚ → Q.ℚ
quadraticBudget e = (scale e Q.+ scale e) Q.+ (scale e Q.+ scale e)

nonnegative-add : (a b : Q.ℚ) → 0 ≤ a → 0 ≤ b → 0 ≤ a Q.+ b
nonnegative-add a b ha hb = subst (_≤ a Q.+ b) (Q.+IdL 0) (≤Monotone+ 0 a 0 b ha hb)
scale-nonnegative : (e : Q.ℚ) → 0 ≤ e → 0 ≤ scale e
scale-nonnegative e eh = nonnegative-bound-product eight (e Q.· e) (dyadicRadius-nonnegative 3)
  (nonnegative-bound-product e e eh eh)

abstract
  budget-coefficient : precision 2 Q.· eight Q.+ (1 Q.+ 1) ≡ eight Q.· one-half
  budget-coefficient = Q.eq/ _ _ refl

  recurrence-budget : (e : Q.ℚ) (n : ℕ) →
    precision 2 Q.· (scale e Q.· precision n) Q.+ (e Q.· e) Q.· (precision n Q.+ precision n) ≡
    scale e Q.· precision (suc n)
  recurrence-budget e n = B.collect-budget (precision 2) eight (e Q.· e) (precision n)
    ∙ cong (Q._· ((e Q.· e) Q.· precision n)) budget-coefficient
    ∙ B.reorder-budget eight one-half (e Q.· e) (precision n)

zero-magnitude : (r : Q.ℚ) → 0 ≤ r → MagnitudeBound 0 r
zero-magnitude r h .positive-upper = h
zero-magnitude r h .negative-upper = h

one-magnitude : MagnitudeBound 1 1
one-magnitude = nonnegative-value-magnitude 1 1 (precision-nonnegative zero) (isRefl≤ 1) (precision-nonnegative zero)

square-small : (q : Q.ℚ) → MagnitudeBound q one-half → MagnitudeBound (q Q.· q) (precision 2)
square-small q h = arbitrary-multiplier-bound q one-half q one-half one-half-nonnegative one-half-nonnegative h h

geometric-term-bound : (q : Q.ℚ) → MagnitudeBound q one-half → (n : ℕ) →
  MagnitudeBound (geometricTerm q n) (precision n)
geometric-term-bound q h zero = one-magnitude
geometric-term-bound q h (suc n) = negate-magnitude-bound _ _
  (subst (MagnitudeBound ((geometricTerm q n Q.· q) Q.· q)) (Q.·IdR (precision (suc n)))
    (arbitrary-multiplier-bound (geometricTerm q n Q.· q) (precision (suc n)) q 1
      (precision-nonnegative (suc n)) (precision-nonnegative zero)
      (arbitrary-multiplier-bound (geometricTerm q n) (precision n) q one-half
        (precision-nonnegative n) one-half-nonnegative (geometric-term-bound q h n) h)
      (small-input≤one q h)))

-- A uniform quadratic bound; no differentiation theorem is assumed.
term-remainder-bound : (x y e : Q.ℚ) → MagnitudeBound x one-half → MagnitudeBound y one-half →
  0 ≤ e → MagnitudeBound (y Q.+ (Q.- x)) e → (n : ℕ) →
  MagnitudeBound (termRemainder x y n) (scale e Q.· precision n)
term-remainder-bound x y e hx hy eh dh zero = transport-magnitude _ _ _ (R.zero-remainder x y)
  (zero-magnitude _ (nonnegative-bound-product (scale e) (precision zero) (scale-nonnegative e eh) (precision-nonnegative zero)))
term-remainder-bound x y e hx hy eh dh (suc n) = transport-magnitude _ _ _ (term-remainder-recurrence x y n)
  (negate-magnitude-bound _ _ (subst (MagnitudeBound _) (Q.·IdR target)
    (nonnegative-multiplier-bound _ target (atanhStepRatio n) 1 target≥0 raw
      (atanh-step-ratio-nonnegative n) (atanh-step-ratio≤one n))))
  where
  h = y Q.+ (Q.- x)
  target = scale e Q.· precision (suc n)
  e²≥0 = nonnegative-bound-product e e eh eh
  target≥0 = nonnegative-bound-product (scale e) (precision (suc n)) (scale-nonnegative e eh) (precision-nonnegative (suc n))
  previous≥0 = nonnegative-bound-product (scale e) (precision n) (scale-nonnegative e eh) (precision-nonnegative n)
  sum≥0 = nonnegative-add (precision n) (precision n) (precision-nonnegative n) (precision-nonnegative n)
  sum-input : MagnitudeBound (x Q.+ y) 1
  sum-input = subst (MagnitudeBound (x Q.+ y)) (precision-refines-double zero) (add-magnitude-bounds _ _ _ _ hx hy)
  driving : MagnitudeBound (((x Q.+ y) Q.· geometricTerm x n) Q.+ atanTerm x n) (precision n Q.+ precision n)
  driving = add-magnitude-bounds _ _ _ _
    (subst (MagnitudeBound ((x Q.+ y) Q.· geometricTerm x n)) (Q.·IdL (precision n))
      (arbitrary-multiplier-bound (x Q.+ y) 1 (geometricTerm x n) (precision n)
        (precision-nonnegative zero) (precision-nonnegative n) sum-input (geometric-term-bound x hx n)))
    (atan-term-geometric x hx n)
  raw : MagnitudeBound ((y Q.· y) Q.· termRemainder x y n Q.+
    (h Q.· h) Q.· (((x Q.+ y) Q.· geometricTerm x n) Q.+ atanTerm x n)) target
  raw = subst (MagnitudeBound _) (recurrence-budget e n)
    (add-magnitude-bounds _ _ _ _
      (arbitrary-multiplier-bound (y Q.· y) (precision 2) (termRemainder x y n) (scale e Q.· precision n)
        (precision-nonnegative 2) previous≥0 (square-small y hy) (term-remainder-bound x y e hx hy eh dh n))
      (arbitrary-multiplier-bound (h Q.· h) (e Q.· e) _ (precision n Q.+ precision n) e²≥0 sum≥0
        (arbitrary-multiplier-bound h e h e eh eh dh dh) driving))

partialRemainder : Q.ℚ → Q.ℚ → ℕ → Q.ℚ
partialRemainder x y n = (atanPartialSum y n Q.+ (Q.- atanPartialSum x n)) Q.+
  (Q.- ((y Q.+ (Q.- x)) Q.· geometricSum x n))

abstract
  partial-remainder-is-sum : (x y : Q.ℚ) (n : ℕ) → partialRemainder x y n ≡ finiteSum (termRemainder x y) n
  partial-remainder-is-sum x y zero = refl
  partial-remainder-is-sum x y (suc n) = B.split-remainder
    (atanPartialSum y n) (atanTerm y (suc n)) (atanPartialSum x n) (atanTerm x (suc n))
    (geometricSum x n) (geometricTerm x (suc n)) (y Q.+ (Q.- x))
    ∙ cong (Q._+ termRemainder x y (suc n)) (partial-remainder-is-sum x y n)

partial-remainder-bound : (x y e : Q.ℚ) → MagnitudeBound x one-half → MagnitudeBound y one-half →
  0 ≤ e → MagnitudeBound (y Q.+ (Q.- x)) e → (n : ℕ) →
  MagnitudeBound (partialRemainder x y n) (scale e Q.+ scale e)
partial-remainder-bound x y e hx hy eh dh n = transport-magnitude _ _ _ (partial-remainder-is-sum x y n)
  (A.weakenMagnitudeBound _ _ _
    (A.finiteSumMagnitudeBound (termRemainder x y) (λ j → scale e Q.· precision j)
      (term-remainder-bound x y e hx hy eh dh) n)
    (A.scaledPrecisionFiniteSumBound (scale e) (scale-nonnegative e eh) n))

clearedRemainder : Q.ℚ → Q.ℚ → ℕ → Q.ℚ
clearedRemainder x y n = (1 Q.+ x Q.· x) Q.· (atanPartialSum y n Q.+ (Q.- atanPartialSum x n)) Q.+ (Q.- (y Q.+ (Q.- x)))

abstract
  cleared-remainder-decomposition : (x y : Q.ℚ) (n : ℕ) → clearedRemainder x y n ≡
    (1 Q.+ x Q.· x) Q.· partialRemainder x y n Q.+ ((y Q.+ (Q.- x)) Q.· (Q.- geometricTerm x (suc n)))
  cleared-remainder-decomposition x y n = B.clear-denominator (1 Q.+ x Q.· x)
    (atanPartialSum y n Q.+ (Q.- atanPartialSum x n)) (y Q.+ (Q.- x)) (geometricSum x n)
    ∙ cong (λ d → (1 Q.+ x Q.· x) Q.· partialRemainder x y n Q.+ ((y Q.+ (Q.- x)) Q.· d))
      (cong (Q._+ (Q.- 1)) (geometric-denominator-identity x n) ∙ B.cancel-one (geometricTerm x (suc n)))

cleared-remainder-bound : (x y e : Q.ℚ) → MagnitudeBound x one-half → MagnitudeBound y one-half →
  0 ≤ e → MagnitudeBound (y Q.+ (Q.- x)) e → (n : ℕ) →
  MagnitudeBound (clearedRemainder x y n) (quadraticBudget e Q.+ e Q.· precision n)
cleared-remainder-bound x y e hx hy eh dh n = transport-magnitude _ _ _ (cleared-remainder-decomposition x y n)
  (add-magnitude-bounds _ _ _ _
    (subst (MagnitudeBound ((1 Q.+ x Q.· x) Q.· partialRemainder x y n)) (B.double-product (scale e))
      (arbitrary-multiplier-bound (1 Q.+ x Q.· x) (1 Q.+ 1) (partialRemainder x y n) (scale e Q.+ scale e)
        (dyadicRadius-nonnegative 1) (nonnegative-add (scale e) (scale e) (scale-nonnegative e eh) (scale-nonnegative e eh))
        (add-magnitude-bounds 1 1 (x Q.· x) 1 one-magnitude
          (weaken-magnitude-bound (x Q.· x) (precision 2) 1 (precision-antitone zero 2 NO.zero-≤) (square-small x hx)))
        (partial-remainder-bound x y e hx hy eh dh n)))
    (arbitrary-multiplier-bound (y Q.+ (Q.- x)) e (Q.- geometricTerm x (suc n)) (precision n) eh (precision-nonnegative n) dh
      (negate-magnitude-bound _ _ (weaken-magnitude-bound _ _ _ (precision-step≤ n) (geometric-term-bound x hx (suc n))))))

errorOffset : Q.ℚ → ℕ
errorOffset e = exponent (Auto.preferredExponent e)

cleared-remainder-all-later : (x y e : Q.ℚ) → MagnitudeBound x one-half → MagnitudeBound y one-half →
  0 ≤ e → MagnitudeBound (y Q.+ (Q.- x)) e → (k n : ℕ) → NO._≤_ (errorOffset e N.+ k) n →
  MagnitudeBound (clearedRemainder x y n) (quadraticBudget e Q.+ precision k)
cleared-remainder-all-later x y e hx hy eh dh k n hn = A.weakenMagnitudeBound _ _ _ (cleared-remainder-bound x y e hx hy eh dh n)
  (≤Monotone+ (quadraticBudget e) (quadraticBudget e) (e Q.· precision n) (precision k) (isRefl≤ (quadraticBudget e))
    (isTrans≤ (e Q.· precision n) (e Q.· precision (errorOffset e N.+ k)) (precision k)
      (left-multiply-monotone e (precision n) (precision (errorOffset e N.+ k)) eh (precision-antitone _ _ hn))
      (A.scaledCoefficientAbsorption e (errorOffset e) k (dominates (Auto.preferredExponent e)))))
