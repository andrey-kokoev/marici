{-# OPTIONS --safe --cubical --guardedness #-}
module TickUniformTrigResidual where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using (exponentialTerm; reciprocalSuccessor; reciprocalSuccessor-nonnegative)
open import RegularCauchyStructure using (precision; precision-nonnegative)
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-bound-product; nonnegative-value-magnitude)
import AbsoluteTaylorSeriesMultiplication as A
import AutomaticRationalExponentialMultiplication as Auto
import TickNormalizedTrigConvolution as C
import TickOperationalTrigResidual as R

nonnegative-add : (a b : Q.ℚ) → 0 ≤ a → 0 ≤ b → 0 ≤ a Q.+ b
nonnegative-add a b ha hb = subst (_≤ a Q.+ b) (Q.+IdL 0) (≤Monotone+ 0 a 0 b ha hb)

positive-exponential-term : (r : Q.ℚ) → 0 ≤ r → (k : ℕ) → 0 ≤ exponentialTerm r k
positive-exponential-term r h zero = precision-nonnegative zero
positive-exponential-term r h (suc k) = nonnegative-bound-product
  (exponentialTerm r k Q.· r) (reciprocalSuccessor k)
  (nonnegative-bound-product (exponentialTerm r k) r (positive-exponential-term r h k) h)
  (reciprocalSuccessor-nonnegative k)

-- One positive input radius dominates every Taylor term for all inputs in
-- that radius. This is the uniformity missing from a separate majorant per q.
exponential-term-domination : (q r : Q.ℚ) → 0 ≤ r → MagnitudeBound q r
  → (k : ℕ) → MagnitudeBound (exponentialTerm q k) (exponentialTerm r k)
exponential-term-domination q r h bound zero = nonnegative-value-magnitude 1 1
  (precision-nonnegative zero) (isRefl≤ 1) (precision-nonnegative zero)
exponential-term-domination q r h bound (suc k) = nonnegative-multiplier-bound
  (exponentialTerm q k Q.· q) (exponentialTerm r k Q.· r)
  (reciprocalSuccessor k) (reciprocalSuccessor k)
  (nonnegative-bound-product (exponentialTerm r k) r (positive-exponential-term r h k) h)
  (arbitrary-multiplier-bound (exponentialTerm q k) (exponentialTerm r k) q r
    (positive-exponential-term r h k) h (exponential-term-domination q r h bound k) bound)
  (reciprocalSuccessor-nonnegative k) (isRefl≤ (reciprocalSuccessor k))

module AtRadius (r : Q.ℚ) (r-nonnegative : 0 ≤ r) where
  majorant = Auto.preferredExponentialMajorant r
  T = A.globalScale majorant
  F = A.fourfoldProductCoefficient T T
  coefficient = F Q.+ F

  coefficient-nonnegative : 0 ≤ coefficient
  coefficient-nonnegative = nonnegative-add F F four four
    where
    product-positive = nonnegative-bound-product T T (A.globalScaleNonnegative majorant) (A.globalScaleNonnegative majorant)
    two = nonnegative-add (T Q.· T) (T Q.· T) product-positive product-positive
    four = nonnegative-add ((T Q.· T) Q.+ (T Q.· T)) ((T Q.· T) Q.+ (T Q.· T)) two two

  term-bound : (q : Q.ℚ) → MagnitudeBound q r → (k : ℕ)
    → MagnitudeBound (exponentialTerm q k) (A.scaledPrecisionMajorant T k)
  term-bound q bound k = A.weakenMagnitudeBound _ _ _
    (exponential-term-domination q r r-nonnegative bound k)
    (positive-upper (A.globalTermBound majorant k))

  cos-bound : (q : Q.ℚ) → MagnitudeBound q r → (k : ℕ)
    → MagnitudeBound (C.denseCosine q k) (A.scaledPrecisionMajorant T k)
  cos-bound q bound k = R.cos-weight-bound k (exponentialTerm q k) (A.scaledPrecisionMajorant T k)
    (A.scaledPrecisionMajorantNonnegative T (A.globalScaleNonnegative majorant) k)
    (term-bound q bound k)

  sin-bound : (q : Q.ℚ) → MagnitudeBound q r → (k : ℕ)
    → MagnitudeBound (C.denseSine q k) (A.scaledPrecisionMajorant T k)
  sin-bound q bound k = R.sin-weight-bound k (exponentialTerm q k) (A.scaledPrecisionMajorant T k)
    (A.scaledPrecisionMajorantNonnegative T (A.globalScaleNonnegative majorant) k)
    (term-bound q bound k)

  residual-bound : (a : ℕ → Q.ℚ)
    → ((k : ℕ) → MagnitudeBound (a k) (A.scaledPrecisionMajorant T k))
    → (n : ℕ) → MagnitudeBound (A.finiteTriangularResidual a a (suc (n N.+ n))) (F Q.· precision n)
  residual-bound a bound n = subst
    (λ k → MagnitudeBound (A.finiteTriangularResidual a a k) (F Q.· precision n))
    (N.+-suc n n)
    (A.scaledPrecisionTriangularResidualMagnitudeBound a a T T
      (A.globalScaleNonnegative majorant) (A.globalScaleNonnegative majorant) bound bound n)

  -- The coefficient depends only on r, not q or n.
  uniform-norm-defect-bound : (q : Q.ℚ) → MagnitudeBound q r → (n : ℕ)
    → MagnitudeBound (R.normDefect q n) (coefficient Q.· precision n)
  uniform-norm-defect-bound q bound n = transport-magnitude _ _ _ (R.norm-defect-is-two-residuals q n)
    (subst (MagnitudeBound
      (A.finiteTriangularResidual (C.denseCosine q) (C.denseCosine q) (suc (n N.+ n)) Q.+
       A.finiteTriangularResidual (C.denseSine q) (C.denseSine q) (suc (n N.+ n))))
      (R.Paths.collect PreferredℚCommRing F F (precision n))
      (add-magnitude-bounds _ _ _ _
        (residual-bound (C.denseCosine q) (cos-bound q bound) n)
        (residual-bound (C.denseSine q) (sin-bound q bound) n)))
