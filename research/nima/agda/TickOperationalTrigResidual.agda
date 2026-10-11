{-# OPTIONS --safe --cubical --guardedness #-}
module TickOperationalTrigResidual where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using
  (finiteSum; finiteSum-with-zero-tail; exponentialTerm; cosinePartialSum)
open import RationalSineTaylorApproximants using (sinePartialSum)
open import RegularCauchyStructure using (precision)
open import CauchyProductBounds
open import RationalArchimedean using (exponent; dominates)
import AbsoluteTaylorSeriesMultiplication as A
import AutomaticRationalExponentialMultiplication as Auto
import TickDenseTrigCutoffs as P
import TickNormalizedTrigConvolution as C
import TickTrigCoefficientCancellation as D₀
module D = D₀.Cancellation PreferredℚCommRing

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  split : (x y u v : fst R)
    → (x +S y) +S (-S (u +S v)) ≡ (x +S (-S u)) +S (y +S (-S v))
  split x y u v = solve! R
  collect : (x y z : fst R) → (x ·S z) +S (y ·S z) ≡ (x +S y) ·S z
  collect x y z = solve! R

triangle-norm-one : (q : Q.ℚ) (k : ℕ)
  → A.finiteTriangularCauchyProduct (C.denseCosine q) (C.denseCosine q) k Q.+
    A.finiteTriangularCauchyProduct (C.denseSine q) (C.denseSine q) k ≡ 1
triangle-norm-one q k = sym (A.finiteSumAdd
  (A.cauchyProductCoefficient (C.denseCosine q) (C.denseCosine q))
  (A.cauchyProductCoefficient (C.denseSine q) (C.denseSine q)) k)
  ∙ finiteSum-with-zero-tail (C.denseNormCoefficient q)
      (C.norm-coefficient-zero q) (C.norm-coefficient-positive q) k

normDefect : Q.ℚ → ℕ → Q.ℚ
normDefect q n =
  ((cosinePartialSum q n Q.· cosinePartialSum q n) Q.+
   (sinePartialSum q n Q.· sinePartialSum q n)) Q.+ (Q.- 1)

-- The actual operational partial sums, not a separate formal derivative model.
norm-defect-is-two-residuals : (q : Q.ℚ) (n : ℕ)
  → normDefect q n ≡
    A.finiteTriangularResidual (C.denseCosine q) (C.denseCosine q) (suc (n N.+ n)) Q.+
    A.finiteTriangularResidual (C.denseSine q) (C.denseSine q) (suc (n N.+ n))
norm-defect-is-two-residuals q n =
  cong (Q._+ (Q.- 1)) (cong₂ Q._+_
    (cong₂ Q._·_ (sym (P.cosine-dense-cutoff q n)) (sym (P.cosine-dense-cutoff q n)))
    (cong₂ Q._·_ (sym (P.sine-dense-cutoff q n)) (sym (P.sine-dense-cutoff q n))))
  ∙ cong (λ z → (cs Q.· cs Q.+ ss Q.· ss) Q.+ (Q.- z)) (sym (triangle-norm-one q k))
  ∙ Paths.split PreferredℚCommRing (cs Q.· cs) (ss Q.· ss)
      (A.finiteTriangularCauchyProduct (C.denseCosine q) (C.denseCosine q) k)
      (A.finiteTriangularCauchyProduct (C.denseSine q) (C.denseSine q) k)
  ∙ cong₂ Q._+_
      (A.finite-product-minus-triangle-is-residual (C.denseCosine q) (C.denseCosine q) k)
      (A.finite-product-minus-triangle-is-residual (C.denseSine q) (C.denseSine q) k)
  where
  k = suc (n N.+ n)
  cs = finiteSum (C.denseCosine q) k
  ss = finiteSum (C.denseSine q) k

zero-bound : (M : Q.ℚ) → 0 ≤ M → MagnitudeBound 0 M
zero-bound M h .positive-upper = h
zero-bound M h .negative-upper = subst (_≤ M)
  (sym (P.Paths.negative-zero PreferredℚCommRing)) h

-- Derivative weights are only 0, 1, -1; multiplication by them never
-- increases a magnitude bound. The mutual recurrence avoids a parity split.
mutual
  cos-weight-bound : (k : ℕ) (z M : Q.ℚ) → 0 ≤ M → MagnitudeBound z M
    → MagnitudeBound (D.cosineDerivative k Q.· z) M
  cos-weight-bound zero z M h bound = transport-magnitude _ _ M (Q.·IdL z) bound
  cos-weight-bound (suc k) z M h bound = transport-magnitude _ _ M
    (D.negative-left-product (D.sineDerivative k) z)
    (negate-magnitude-bound _ M (sin-weight-bound k z M h bound))

  sin-weight-bound : (k : ℕ) (z M : Q.ℚ) → 0 ≤ M → MagnitudeBound z M
    → MagnitudeBound (D.sineDerivative k Q.· z) M
  sin-weight-bound zero z M h bound = transport-magnitude _ _ M
    (P.Paths.zero-times PreferredℚCommRing z) (zero-bound M h)
  sin-weight-bound (suc k) z M h bound = cos-weight-bound k z M h bound

module AtRational (q : Q.ℚ) where
  majorant = Auto.preferredExponentialMajorant q
  T = A.globalScale majorant
  F = A.fourfoldProductCoefficient T T
  coefficient = F Q.+ F
  absorption = Auto.preferredExponent coefficient
  cutoffOffset = exponent absorption

  cos-bound : (k : ℕ) → MagnitudeBound (C.denseCosine q k) (A.scaledPrecisionMajorant T k)
  cos-bound k = cos-weight-bound k (exponentialTerm q k) (A.scaledPrecisionMajorant T k)
    (A.scaledPrecisionMajorantNonnegative T (A.globalScaleNonnegative majorant) k)
    (A.globalTermBound majorant k)

  sin-bound : (k : ℕ) → MagnitudeBound (C.denseSine q k) (A.scaledPrecisionMajorant T k)
  sin-bound k = sin-weight-bound k (exponentialTerm q k) (A.scaledPrecisionMajorant T k)
    (A.scaledPrecisionMajorantNonnegative T (A.globalScaleNonnegative majorant) k)
    (A.globalTermBound majorant k)

  residual-bound : (a : ℕ → Q.ℚ)
    → ((k : ℕ) → MagnitudeBound (a k) (A.scaledPrecisionMajorant T k))
    → (n : ℕ) → MagnitudeBound (A.finiteTriangularResidual a a (suc (n N.+ n))) (F Q.· precision n)
  residual-bound a bound n = subst
    (λ k → MagnitudeBound (A.finiteTriangularResidual a a k) (F Q.· precision n))
    (N.+-suc n n)
    (A.scaledPrecisionTriangularResidualMagnitudeBound a a T T
      (A.globalScaleNonnegative majorant) (A.globalScaleNonnegative majorant) bound bound n)

  norm-defect-bound : (n : ℕ) → MagnitudeBound (normDefect q n) (coefficient Q.· precision n)
  norm-defect-bound n = transport-magnitude _ _ _ (norm-defect-is-two-residuals q n)
    (subst (MagnitudeBound
      (A.finiteTriangularResidual (C.denseCosine q) (C.denseCosine q) (suc (n N.+ n)) Q.+
       A.finiteTriangularResidual (C.denseSine q) (C.denseSine q) (suc (n N.+ n))))
      (Paths.collect PreferredℚCommRing F F (precision n))
      (add-magnitude-bounds _ _ _ _
        (residual-bound (C.denseCosine q) cos-bound n)
        (residual-bound (C.denseSine q) sin-bound n)))

  -- A constructed modulus for every fixed rational input, no unproved
  -- majorant or convergence premise remains in this partial-sum theorem.
  norm-defect-vanishes : (n : ℕ)
    → MagnitudeBound (normDefect q (cutoffOffset N.+ n)) (precision n)
  norm-defect-vanishes n = A.weakenMagnitudeBound _ _ _
    (norm-defect-bound (cutoffOffset N.+ n))
    (A.scaledCoefficientAbsorption coefficient cutoffOffset n (dominates absorption))
