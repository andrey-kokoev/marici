{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TaylorInputDifference where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RationalTaylorApproximants
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import TaylorTermBounds
open import TaylorUniformSeedBounds

module InputDifferencePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  product-step-difference : (a b q r c : fst R) →
    ((a ·S q) ·S c) +S (-S ((b ·S r) ·S c)) ≡
    ((((a +S (-S b)) ·S q) +S (b ·S (q +S (-S r)))) ·S c)
  product-step-difference a b q r c = solve! R

  difference-scale : (D T e radius : fst R) →
    (((D ·S e) ·S radius) +S (T ·S e)) ·S 1r ≡
    ((D ·S radius) +S T) ·S e
  difference-scale D T e radius = solve! R

exponential-term-difference-step :
  (q r : Q.ℚ) (n : ℕ) →
  exponentialTerm q (suc n) Q.+ (Q.- exponentialTerm r (suc n)) ≡
  (((exponentialTerm q n Q.+ (Q.- exponentialTerm r n)) Q.· q) Q.+
   (exponentialTerm r n Q.· (q Q.+ (Q.- r)))) Q.·
  reciprocalSuccessor n
exponential-term-difference-step q r n =
  InputDifferencePaths.product-step-difference PreferredℚCommRing
    (exponentialTerm q n) (exponentialTerm r n) q r
    (reciprocalSuccessor n)

exponential-term-input-difference-bound :
  (q r e : Q.ℚ) (d n : ℕ) →
  0 ≤ e →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) e →
  MagnitudeBound
    (exponentialTerm q n Q.+ (Q.- exponentialTerm r n))
    (dyadicRadius (termDifferenceExponent d n) Q.· e)
exponential-term-input-difference-bound q r e d zero
    eNonnegative qBound rBound differenceBound =
  let zeroBound = nonnegative-value-magnitude 0 e
        (isRefl≤ 0) eNonnegative eNonnegative
      scaledZeroBound = subst (MagnitudeBound 0)
        (sym (Q.·IdL e)) zeroBound
  in
  transport-magnitude _ 0 _ (Q.+InvR 1) scaledZeroBound
exponential-term-input-difference-bound q r e d (suc n)
    eNonnegative qBound rBound differenceBound =
  let differenceScale = dyadicRadius (termDifferenceExponent d n)
      termScale = dyadicRadius (termPowerExponent d n)
      radius = dyadicRadius d
      previous = exponential-term-input-difference-bound
        q r e d n eNonnegative qBound rBound differenceBound
      rTerm = exponential-term-dyadic-power-bound r d n rBound
      previousScaleNonnegative = nonnegative-bound-product differenceScale e
        (dyadicRadius-nonnegative (termDifferenceExponent d n)) eNonnegative
      propagatedScale = (differenceScale Q.· e) Q.· radius
      freshScale = termScale Q.· e
      propagatedValue =
        (exponentialTerm q n Q.+ (Q.- exponentialTerm r n)) Q.· q
      freshValue = exponentialTerm r n Q.· (q Q.+ (Q.- r))
      propagatedScaleNonnegative = nonnegative-bound-product
        (differenceScale Q.· e) radius previousScaleNonnegative
        (dyadicRadius-nonnegative d)
      freshScaleNonnegative = nonnegative-bound-product termScale e
        (dyadicRadius-nonnegative (termPowerExponent d n)) eNonnegative
      propagated = arbitrary-multiplier-bound
        (exponentialTerm q n Q.+ (Q.- exponentialTerm r n))
        (differenceScale Q.· e) q radius
        previousScaleNonnegative (dyadicRadius-nonnegative d)
        previous qBound
      fresh = arbitrary-multiplier-bound
        (exponentialTerm r n) termScale
        (q Q.+ (Q.- r)) e
        (dyadicRadius-nonnegative (termPowerExponent d n))
        eNonnegative rTerm differenceBound
      combined = add-magnitude-bounds
        propagatedValue propagatedScale freshValue freshScale
        propagated fresh
      combinedScaleNonnegative = ≤Monotone+
        0 propagatedScale 0 freshScale
        propagatedScaleNonnegative freshScaleNonnegative
      combinedValue = propagatedValue Q.+ freshValue
      combinedScale = propagatedScale Q.+ freshScale
      scaled = arbitrary-multiplier-bound
        combinedValue combinedScale (reciprocalSuccessor n) 1
        combinedScaleNonnegative (dyadicRadius-nonnegative 0)
        combined (reciprocal-magnitude≤one n)
      rearranged = subst (MagnitudeBound (combinedValue Q.· reciprocalSuccessor n))
        (InputDifferencePaths.difference-scale PreferredℚCommRing
          differenceScale termScale e radius)
        scaled
      weakened = weaken-magnitude-bound
        (combinedValue Q.· reciprocalSuccessor n)
        ((differenceScale Q.· radius Q.+ termScale) Q.· e)
        (dyadicRadius (termDifferenceExponent d (suc n)) Q.· e)
        (subst2 _≤_
          (Q.·Comm e (differenceScale Q.· radius Q.+ termScale))
          (Q.·Comm e (dyadicRadius (termDifferenceExponent d (suc n))))
          (left-multiply-monotone e
            (differenceScale Q.· radius Q.+ termScale)
            (dyadicRadius (termDifferenceExponent d (suc n)))
            eNonnegative (term-difference-scale-step d n)))
        rearranged
  in
  transport-magnitude _ _ _
    (exponential-term-difference-step q r n) weakened
