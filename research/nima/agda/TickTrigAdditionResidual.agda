{-# OPTIONS --safe --cubical --guardedness #-}
module TickTrigAdditionResidual where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using (finiteSum; cosinePartialSum)
open import RationalSineTaylorApproximants using (sinePartialSum)
open import RegularCauchyStructure using (precision; precision-antitone)
open import CauchyProductBounds
open import RationalArchimedean using (exponent; dominates)
import AbsoluteTaylorSeriesMultiplication as A
import AutomaticRationalExponentialMultiplication as Auto
import TickDenseTrigCutoffs as Cut
import TickNormalizedTrigConvolution as C
import TickOperationalTrigResidual as Old
import TickUniformTrigResidual as U
import TickTrigAdditionCoefficients as Coeff

cosineAdditionDefect sineAdditionDefect : Q.ℚ → Q.ℚ → ℕ → Q.ℚ
cosineAdditionDefect x y n =
  (cosinePartialSum x n Q.· cosinePartialSum y n Q.+
    (Q.- (sinePartialSum x n Q.· sinePartialSum y n))) Q.+
    (Q.- cosinePartialSum (x Q.+ y) n)
sineAdditionDefect x y n =
  (sinePartialSum x n Q.· cosinePartialSum y n Q.+
    (cosinePartialSum x n Q.· sinePartialSum y n)) Q.+
    (Q.- sinePartialSum (x Q.+ y) n)

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  split-minus : (a b c d : fst R) →
    (a +S (-S b)) +S (-S (c +S (-S d))) ≡ (a +S (-S c)) +S (-S (b +S (-S d)))
  split-minus a b c d = solve! R

abstract
  triangle-cosine-addition : (x y : Q.ℚ) (n : ℕ) →
    A.finiteTriangularCauchyProduct (C.denseCosine x) (C.denseCosine y) (suc (n N.+ n)) Q.+
      (Q.- A.finiteTriangularCauchyProduct (C.denseSine x) (C.denseSine y) (suc (n N.+ n))) ≡
    cosinePartialSum (x Q.+ y) n
  triangle-cosine-addition x y n =
    cong (A.finiteTriangularCauchyProduct (C.denseCosine x) (C.denseCosine y) k Q.+_)
      (sym (Coeff.finiteSum-negate (A.cauchyProductCoefficient (C.denseSine x) (C.denseSine y)) k))
    ∙ sym (A.finiteSumAdd _ _ k)
    ∙ A.finiteSumCongruence _ _ (Coeff.cosine-addition-coefficient x y) k
    ∙ Cut.cosine-dense-cutoff (x Q.+ y) n
    where
    k : ℕ
    k = suc (n N.+ n)

  triangle-sine-addition : (x y : Q.ℚ) (n : ℕ) →
    A.finiteTriangularCauchyProduct (C.denseSine x) (C.denseCosine y) (suc (n N.+ n)) Q.+
      A.finiteTriangularCauchyProduct (C.denseCosine x) (C.denseSine y) (suc (n N.+ n)) ≡
    sinePartialSum (x Q.+ y) n
  triangle-sine-addition x y n = sym (A.finiteSumAdd _ _ k)
    ∙ A.finiteSumCongruence _ _ (Coeff.sine-addition-coefficient x y) k
    ∙ Cut.sine-dense-cutoff (x Q.+ y) n
    where
    k : ℕ
    k = suc (n N.+ n)

  cosine-defect-is-residuals : (x y : Q.ℚ) (n : ℕ) → cosineAdditionDefect x y n ≡
    A.finiteTriangularResidual (C.denseCosine x) (C.denseCosine y) (suc (n N.+ n)) Q.+
      (Q.- A.finiteTriangularResidual (C.denseSine x) (C.denseSine y) (suc (n N.+ n)))
  cosine-defect-is-residuals x y n =
    cong₂ Q._+_
      (cong₂ Q._+_
        (cong₂ Q._·_ (sym (Cut.cosine-dense-cutoff x n)) (sym (Cut.cosine-dense-cutoff y n)))
        (cong Q.-_ (cong₂ Q._·_ (sym (Cut.sine-dense-cutoff x n)) (sym (Cut.sine-dense-cutoff y n)))))
      (cong Q.-_ (sym (triangle-cosine-addition x y n)))
    ∙ Paths.split-minus PreferredℚCommRing
        (finiteSum (C.denseCosine x) k Q.· finiteSum (C.denseCosine y) k)
        (finiteSum (C.denseSine x) k Q.· finiteSum (C.denseSine y) k)
        (A.finiteTriangularCauchyProduct (C.denseCosine x) (C.denseCosine y) k)
        (A.finiteTriangularCauchyProduct (C.denseSine x) (C.denseSine y) k)
    ∙ cong₂ Q._+_
        (A.finite-product-minus-triangle-is-residual (C.denseCosine x) (C.denseCosine y) k)
        (cong Q.-_ (A.finite-product-minus-triangle-is-residual (C.denseSine x) (C.denseSine y) k))
    where
    k : ℕ
    k = suc (n N.+ n)

  sine-defect-is-residuals : (x y : Q.ℚ) (n : ℕ) → sineAdditionDefect x y n ≡
    A.finiteTriangularResidual (C.denseSine x) (C.denseCosine y) (suc (n N.+ n)) Q.+
      A.finiteTriangularResidual (C.denseCosine x) (C.denseSine y) (suc (n N.+ n))
  sine-defect-is-residuals x y n =
    cong₂ Q._+_
      (cong₂ Q._+_
        (cong₂ Q._·_ (sym (Cut.sine-dense-cutoff x n)) (sym (Cut.cosine-dense-cutoff y n)))
        (cong₂ Q._·_ (sym (Cut.cosine-dense-cutoff x n)) (sym (Cut.sine-dense-cutoff y n))))
      (cong Q.-_ (sym (triangle-sine-addition x y n)))
    ∙ Old.Paths.split PreferredℚCommRing
        (finiteSum (C.denseSine x) k Q.· finiteSum (C.denseCosine y) k)
        (finiteSum (C.denseCosine x) k Q.· finiteSum (C.denseSine y) k)
        (A.finiteTriangularCauchyProduct (C.denseSine x) (C.denseCosine y) k)
        (A.finiteTriangularCauchyProduct (C.denseCosine x) (C.denseSine y) k)
    ∙ cong₂ Q._+_
        (A.finite-product-minus-triangle-is-residual (C.denseSine x) (C.denseCosine y) k)
        (A.finite-product-minus-triangle-is-residual (C.denseCosine x) (C.denseSine y) k)
    where
    k : ℕ
    k = suc (n N.+ n)

-- One bound and cutoff offset work simultaneously for both inputs throughout
-- the radius, not merely at one pair or one sequence of sampled cutoffs.
module AtRadius (r : Q.ℚ) (r-nonnegative : 0 ≤ r) where
  module B = U.AtRadius r r-nonnegative
  open B using (T; F; coefficient; coefficient-nonnegative; majorant; cos-bound; sin-bound)
  absorption = Auto.preferredExponent coefficient
  cutoffOffset = exponent absorption

  residual-bound : (a b : ℕ → Q.ℚ) →
    ((k : ℕ) → MagnitudeBound (a k) (A.scaledPrecisionMajorant T k)) →
    ((k : ℕ) → MagnitudeBound (b k) (A.scaledPrecisionMajorant T k)) →
    (n : ℕ) → MagnitudeBound (A.finiteTriangularResidual a b (suc (n N.+ n))) (F Q.· precision n)
  residual-bound a b ha hb n = subst
    (λ k → MagnitudeBound (A.finiteTriangularResidual a b k) (F Q.· precision n))
    (N.+-suc n n)
    (A.scaledPrecisionTriangularResidualMagnitudeBound a b T T
      (A.globalScaleNonnegative majorant) (A.globalScaleNonnegative majorant) ha hb n)

  cosine-addition-bound : (x y : Q.ℚ) → MagnitudeBound x r → MagnitudeBound y r →
    (n : ℕ) → MagnitudeBound (cosineAdditionDefect x y n) (coefficient Q.· precision n)
  cosine-addition-bound x y hx hy n = transport-magnitude _ _ _ (cosine-defect-is-residuals x y n)
    (subst (MagnitudeBound _) (Old.Paths.collect PreferredℚCommRing F F (precision n))
      (add-magnitude-bounds _ _ _ _
        (residual-bound _ _ (cos-bound x hx) (cos-bound y hy) n)
        (negate-magnitude-bound _ _ (residual-bound _ _ (sin-bound x hx) (sin-bound y hy) n))))

  sine-addition-bound : (x y : Q.ℚ) → MagnitudeBound x r → MagnitudeBound y r →
    (n : ℕ) → MagnitudeBound (sineAdditionDefect x y n) (coefficient Q.· precision n)
  sine-addition-bound x y hx hy n = transport-magnitude _ _ _ (sine-defect-is-residuals x y n)
    (subst (MagnitudeBound _) (Old.Paths.collect PreferredℚCommRing F F (precision n))
      (add-magnitude-bounds _ _ _ _
        (residual-bound _ _ (sin-bound x hx) (cos-bound y hy) n)
        (residual-bound _ _ (cos-bound x hx) (sin-bound y hy) n)))

  later-budget : (n m : ℕ) → NO._≤_ (cutoffOffset N.+ n) m →
    coefficient Q.· precision m ≤ precision n
  later-budget n m nm = isTrans≤ (coefficient Q.· precision m)
    (coefficient Q.· precision (cutoffOffset N.+ n)) (precision n)
    (left-multiply-monotone coefficient (precision m) (precision (cutoffOffset N.+ n))
      coefficient-nonnegative (precision-antitone _ _ nm))
    (A.scaledCoefficientAbsorption coefficient cutoffOffset n (dominates absorption))

  cosine-addition-all-later : (x y : Q.ℚ) → MagnitudeBound x r → MagnitudeBound y r →
    (n m : ℕ) → NO._≤_ (cutoffOffset N.+ n) m → MagnitudeBound (cosineAdditionDefect x y m) (precision n)
  cosine-addition-all-later x y hx hy n m nm = A.weakenMagnitudeBound _ _ _
    (cosine-addition-bound x y hx hy m) (later-budget n m nm)

  sine-addition-all-later : (x y : Q.ℚ) → MagnitudeBound x r → MagnitudeBound y r →
    (n m : ℕ) → NO._≤_ (cutoffOffset N.+ n) m → MagnitudeBound (sineAdditionDefect x y m) (precision n)
  sine-addition-all-later x y hx hy n m nm = A.weakenMagnitudeBound _ _ _
    (sine-addition-bound x y hx hy m) (later-budget n m nm)
