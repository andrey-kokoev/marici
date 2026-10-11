{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyOuterRotor where

open import Cubical.Foundations.Prelude
import AbsoluteTaylorSeriesMultiplication
import Cubical.Data.Int.Order as ZO
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import RegularCauchyStructure using (precision-nonnegative)
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-value-magnitude)
open import CauchyMetricEquivalence
open import CauchyAdditionCongruence using (_+completion_)
open import CauchyNegation using (-completion_)
open import CauchyCompletionMultiplication using (preferredCompletionMultiplication)
open import CauchyRationalEmbedding using (embedℚ-preserves-sum; embedℚ-preserves-negation)
open import TickCompletionMagnitudeBounds
open import TickCayleyGridSlope using (rational-product-equation)
open import TickCayleyGridIncrement using (gridValue; gridProductInverse; grid-product-inverse-law; grid-product-inverse-nonnegative; grid-product-inverse≤one)
open import TickAtanFirstOrderBounds using (one-magnitude)
open import TickRotationDefectTransport using (Rotor; RotorBound; _⊗_)

cayleyReal cayleyImaginary : ℕ → ℕ → Q.ℚ
cayleyReal n d = (1 Q.+ (Q.- (gridValue n d Q.· gridValue n d))) Q.· gridProductInverse n n d
cayleyImaginary n d = (gridValue n d Q.+ gridValue n d) Q.· gridProductInverse n n d

cayleyRotor inverseCayleyRotor : ℕ → ℕ → Rotor
cayleyRotor n d = embedMetricℚ (cayleyReal n d) , embedMetricℚ (cayleyImaginary n d)
inverseCayleyRotor n d = embedMetricℚ (cayleyReal n d) , embedMetricℚ (Q.- cayleyImaginary n d)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  norm : (x u : fst R) →
    ((1r +S (-S (x ·S x))) ·S u) ·S ((1r +S (-S (x ·S x))) ·S u) +S
      (-S (((x +S x) ·S u) ·S (-S ((x +S x) ·S u)))) ≡
    ((1r +S x ·S x) ·S u) ·S ((1r +S x ·S x) ·S u)
  norm x u = solve! R
  cancel : (a b : fst R) → a ·S (-S b) +S b ·S a ≡ 0r
  cancel a b = solve! R
module R = Algebra PreferredℚCommRing

abstract
  rational-inverse-real : (n d : ℕ) →
    cayleyReal n d Q.· cayleyReal n d Q.+ (Q.- (cayleyImaginary n d Q.· (Q.- cayleyImaginary n d))) ≡ 1
  rational-inverse-real n d = R.norm (gridValue n d) (gridProductInverse n n d)
    ∙ cong₂ Q._·_ (grid-product-inverse-law n n d) (grid-product-inverse-law n n d) ∙ Q.·IdR 1

  embedded-product : (a b c d : Q.ℚ) →
    ((embedMetricℚ a , embedMetricℚ b) ⊗ (embedMetricℚ c , embedMetricℚ d)) ≡
      (embedMetricℚ (a Q.· c Q.+ (Q.- (b Q.· d))) , embedMetricℚ (a Q.· d Q.+ b Q.· c))
  embedded-product a b c d = cong₂ _,_
    (cong₂ _+completion_ (rational-product-equation a c (a Q.· c) refl)
      (cong -completion_ (rational-product-equation b d (b Q.· d) refl) ∙ embedℚ-preserves-negation (b Q.· d))
      ∙ sym (embedℚ-preserves-sum (a Q.· c) (Q.- (b Q.· d))))
    (cong₂ _+completion_ (rational-product-equation a d (a Q.· d) refl) (rational-product-equation b c (b Q.· c) refl)
      ∙ sym (embedℚ-preserves-sum (a Q.· d) (b Q.· c)))

  cayley-inverse-law : (n d : ℕ) → cayleyRotor n d ⊗ inverseCayleyRotor n d ≡ (embedMetricℚ 1 , embedMetricℚ 0)
  cayley-inverse-law n d = embedded-product (cayleyReal n d) (cayleyImaginary n d) (cayleyReal n d) (Q.- cayleyImaginary n d)
    ∙ cong₂ _,_ (cong embedMetricℚ (rational-inverse-real n d)) (cong embedMetricℚ (R.cancel (cayleyReal n d) (cayleyImaginary n d)))

module Bound (n d : ℕ) (hx : MagnitudeBound (gridValue n d) one-half) where
  x = gridValue n d
  u = gridProductInverse n n d
  uh : MagnitudeBound u 1
  uh = nonnegative-value-magnitude u 1 (grid-product-inverse-nonnegative n n d) (grid-product-inverse≤one n n d) (precision-nonnegative 0)
  real-bound : MagnitudeBound (cayleyReal n d) (1 Q.+ one-half Q.· one-half)
  real-bound = subst (MagnitudeBound (cayleyReal n d)) (Q.·IdR (1 Q.+ one-half Q.· one-half))
    (arbitrary-multiplier-bound (1 Q.+ (Q.- (x Q.· x))) (1 Q.+ one-half Q.· one-half) u 1
      ZO.zero-≤pos (precision-nonnegative 0)
      (add-magnitude-bounds 1 1 (Q.- (x Q.· x)) (one-half Q.· one-half) one-magnitude
        (negate-magnitude-bound (x Q.· x) (one-half Q.· one-half)
          (arbitrary-multiplier-bound x one-half x one-half (precision-nonnegative 1) (precision-nonnegative 1) hx hx))) uh)
  imaginary-bound : MagnitudeBound (cayleyImaginary n d) (one-half Q.+ one-half)
  imaginary-bound = subst (MagnitudeBound (cayleyImaginary n d)) (Q.·IdR (one-half Q.+ one-half))
    (arbitrary-multiplier-bound (x Q.+ x) (one-half Q.+ one-half) u 1
      ZO.zero-≤pos (precision-nonnegative 0) (add-magnitude-bounds x one-half x one-half hx hx) uh)
  inverse-bound : RotorBound (inverseCayleyRotor n d) 2
  inverse-bound = embedded-magnitude-bound (cayleyReal n d) 2
    (AbsoluteTaylorSeriesMultiplication.weakenMagnitudeBound (cayleyReal n d) (1 Q.+ one-half Q.· one-half) 2 real-bound (3 , refl)) ,
    embedded-magnitude-bound (Q.- cayleyImaginary n d) 2
    (AbsoluteTaylorSeriesMultiplication.weakenMagnitudeBound (Q.- cayleyImaginary n d) (one-half Q.+ one-half) 2
      (negate-magnitude-bound (cayleyImaginary n d) (one-half Q.+ one-half) imaginary-bound) (4 , refl))
