{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CosineInputDifference where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import Cubical.Data.Rationals.Order
open import RationalTaylorApproximants
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import TaylorTermBounds
open import CosineTermBounds
open import UniformCosineSeedBounds

module CosineDifferencePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  negative-step-difference :
    (a b firstInverse secondInverse : fst R) →
    (-S ((a ·S firstInverse) ·S secondInverse)) +S
      (-S (-S ((b ·S firstInverse) ·S secondInverse))) ≡
    -S (((a +S (-S b)) ·S firstInverse) ·S secondInverse)
  negative-step-difference a b firstInverse secondInverse = solve! R

  quadratic-product-difference : (t s q r : fst R) →
    ((t ·S q) ·S q) +S (-S ((s ·S r) ·S r)) ≡
    ((((t +S (-S s)) ·S q) ·S q) +S
     ((s ·S (q +S (-S r))) ·S q)) +S
    ((s ·S r) ·S (q +S (-S r)))
  quadratic-product-difference t s q r = solve! R

  reciprocal-linear :
    (a b firstInverse secondInverse : fst R) →
    (-S (((a +S b) ·S firstInverse) ·S secondInverse)) ≡
    (-S ((a ·S firstInverse) ·S secondInverse)) +S
    (-S ((b ·S firstInverse) ·S secondInverse))
  reciprocal-linear a b firstInverse secondInverse = solve! R

  reciprocal-linear-three :
    (a b c firstInverse secondInverse : fst R) →
    (-S ((((a +S b) +S c) ·S firstInverse) ·S secondInverse)) ≡
    ((-S ((a ·S firstInverse) ·S secondInverse)) +S
     (-S ((b ·S firstInverse) ·S secondInverse))) +S
    (-S ((c ·S firstInverse) ·S secondInverse))
  reciprocal-linear-three a b c firstInverse secondInverse = solve! R

  propagated-scale : (D e radius : fst R) →
    (((D ·S e) ·S radius) ·S radius) ≡
      ((D ·S radius) ·S radius) ·S e
  propagated-scale D e radius = solve! R

  fresh-scale : (T e radius : fst R) →
    ((T ·S e) ·S radius) ≡ (T ·S radius) ·S e
  fresh-scale T e radius = solve! R

  factor-three-errors : (A B C e : fst R) →
    ((A ·S e) +S (B ·S e)) +S (C ·S e) ≡
      ((A +S B) +S C) ·S e
  factor-three-errors A B C e = solve! R

  strip-unit-scales : (scale : fst R) →
    (scale ·S 1r) ·S 1r ≡ scale
  strip-unit-scales scale = solve! R

cosineTermDifferenceExponent : ℕ → ℕ → ℕ
cosineTermDifferenceExponent d zero = zero
cosineTermDifferenceExponent d (suc n) =
  let propagated = (cosineTermDifferenceExponent d n ℕ.+ d) ℕ.+ d
      fresh = cosineTermGrowthExponent d n ℕ.+ d
  in suc (suc (propagated ℕ.+ fresh) ℕ.+ fresh)

cosine-term-difference-scale-step : (d n : ℕ) →
  let propagatedExponent =
        (cosineTermDifferenceExponent d n ℕ.+ d) ℕ.+ d
      freshExponent = cosineTermGrowthExponent d n ℕ.+ d
  in
  (dyadicRadius propagatedExponent Q.+ dyadicRadius freshExponent) Q.+
    dyadicRadius freshExponent ≤
  dyadicRadius (cosineTermDifferenceExponent d (suc n))
cosine-term-difference-scale-step d n =
  let propagatedExponent =
        (cosineTermDifferenceExponent d n ℕ.+ d) ℕ.+ d
      freshExponent = cosineTermGrowthExponent d n ℕ.+ d
      first = radius-sum≤successor-combined
        propagatedExponent freshExponent
      second = radius-sum≤successor-combined
        (suc (propagatedExponent ℕ.+ freshExponent)) freshExponent
  in
  isTrans≤
    ((dyadicRadius propagatedExponent Q.+ dyadicRadius freshExponent) Q.+
      dyadicRadius freshExponent)
    (dyadicRadius (suc (propagatedExponent ℕ.+ freshExponent)) Q.+
      dyadicRadius freshExponent)
    (dyadicRadius (cosineTermDifferenceExponent d (suc n)))
    (≤Monotone+
      (dyadicRadius propagatedExponent Q.+ dyadicRadius freshExponent)
      (dyadicRadius (suc (propagatedExponent ℕ.+ freshExponent)))
      (dyadicRadius freshExponent) (dyadicRadius freshExponent)
      first (isRefl≤ (dyadicRadius freshExponent)))
    second

cosine-term-difference-step : (q r : Q.ℚ) (n : ℕ) →
  cosineTerm q (suc n) Q.+ (Q.- cosineTerm r (suc n)) ≡
  let difference = cosineTerm q n Q.+ (Q.- cosineTerm r n)
      inputDifference = q Q.+ (Q.- r)
      firstInverse = reciprocalSuccessor (firstCosineDenominator n)
      secondInverse = reciprocalSuccessor (secondCosineDenominator n)
      propagated = Q.- (((((difference Q.· q) Q.· q) Q.· firstInverse) Q.·
        secondInverse))
      freshLeft = Q.- (((((cosineTerm r n Q.· inputDifference) Q.· q) Q.·
        firstInverse) Q.· secondInverse))
      freshRight = Q.- (((((cosineTerm r n Q.· r) Q.· inputDifference) Q.·
        firstInverse) Q.· secondInverse))
  in (propagated Q.+ freshLeft) Q.+ freshRight
three-factor-reciprocal-magnitude-bound :
  (value first second A B C : Q.ℚ) (firstIndex secondIndex : ℕ) →
  0 ≤ A → 0 ≤ B → 0 ≤ C →
  MagnitudeBound value A →
  MagnitudeBound first B →
  MagnitudeBound second C →
  MagnitudeBound
    (Q.- (((((value Q.· first) Q.· second) Q.·
      reciprocalSuccessor firstIndex) Q.· reciprocalSuccessor secondIndex)))
    ((A Q.· B) Q.· C)
three-factor-reciprocal-magnitude-bound value first second A B C
  firstIndex secondIndex 0≤A 0≤B 0≤C valueBound firstBound secondBound =
  let ABNonnegative = nonnegative-bound-product A B 0≤A 0≤B
      ABCNonnegative = nonnegative-bound-product (A Q.· B) C ABNonnegative 0≤C
      firstProduct = arbitrary-multiplier-bound value A first B
        0≤A 0≤B valueBound firstBound
      secondProduct = arbitrary-multiplier-bound (value Q.· first) (A Q.· B)
        second C ABNonnegative 0≤C firstProduct secondBound
      firstReciprocal = arbitrary-multiplier-bound
        ((value Q.· first) Q.· second) ((A Q.· B) Q.· C)
        (reciprocalSuccessor firstIndex) 1
        ABCNonnegative (dyadicRadius-nonnegative 0) secondProduct
        (reciprocal-magnitude≤one firstIndex)
      secondReciprocal = arbitrary-multiplier-bound
        (((value Q.· first) Q.· second) Q.· reciprocalSuccessor firstIndex)
        (((A Q.· B) Q.· C) Q.· 1)
        (reciprocalSuccessor secondIndex) 1
        (nonnegative-bound-product ((A Q.· B) Q.· C) 1
          ABCNonnegative (dyadicRadius-nonnegative 0))
        (dyadicRadius-nonnegative 0) firstReciprocal
        (reciprocal-magnitude≤one secondIndex)
      normalized = subst
        (MagnitudeBound
          ((((value Q.· first) Q.· second) Q.· reciprocalSuccessor firstIndex) Q.·
            reciprocalSuccessor secondIndex))
        (CosineDifferencePaths.strip-unit-scales PreferredℚCommRing
          ((A Q.· B) Q.· C))
        secondReciprocal
  in negate-magnitude-bound _ _ normalized

cosine-term-difference-step q r n =
  let tq = cosineTerm q n
      tr = cosineTerm r n
      difference = tq Q.+ (Q.- tr)
      inputDifference = q Q.+ (Q.- r)
      firstInverse = reciprocalSuccessor (firstCosineDenominator n)
      secondInverse = reciprocalSuccessor (secondCosineDenominator n)
      a = (difference Q.· q) Q.· q
      b = (tr Q.· inputDifference) Q.· q
      c = (tr Q.· r) Q.· inputDifference
  in
  CosineDifferencePaths.negative-step-difference PreferredℚCommRing
    ((tq Q.· q) Q.· q) ((tr Q.· r) Q.· r)
    firstInverse secondInverse ∙
  cong (λ z → Q.- ((z Q.· firstInverse) Q.· secondInverse))
    (CosineDifferencePaths.quadratic-product-difference
      PreferredℚCommRing tq tr q r) ∙
  CosineDifferencePaths.reciprocal-linear-three
    PreferredℚCommRing a b c firstInverse secondInverse

cosine-term-input-difference-bound :
  (q r error : Q.ℚ) (d n : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (cosineTerm q n Q.+ (Q.- cosineTerm r n))
    (dyadicRadius (cosineTermDifferenceExponent d n) Q.· error)
cosine-term-input-difference-bound q r error d zero errorNonnegative
  qBound rBound differenceBound =
  let zeroBound = nonnegative-value-magnitude 0 error
        (isRefl≤ 0) errorNonnegative errorNonnegative
      scaled = subst (MagnitudeBound 0) (sym (Q.·IdL error)) zeroBound
  in transport-magnitude _ 0 _ (Q.+InvR 1) scaled
cosine-term-input-difference-bound q r error d (suc n) errorNonnegative
  qBound rBound differenceBound =
  let DExponent = cosineTermDifferenceExponent d n
      TExponent = cosineTermGrowthExponent d n
      propagatedExponent = (DExponent ℕ.+ d) ℕ.+ d
      freshExponent = TExponent ℕ.+ d
      D = dyadicRadius DExponent
      T = dyadicRadius TExponent
      radius = dyadicRadius d
      difference = cosineTerm q n Q.+ (Q.- cosineTerm r n)
      inputDifference = q Q.+ (Q.- r)
      firstIndex = firstCosineDenominator n
      secondIndex = secondCosineDenominator n
      propagatedRaw = three-factor-reciprocal-magnitude-bound
        difference q q (D Q.· error) radius radius firstIndex secondIndex
        (nonnegative-bound-product D error
          (dyadicRadius-nonnegative DExponent) errorNonnegative)
        (dyadicRadius-nonnegative d) (dyadicRadius-nonnegative d)
        (cosine-term-input-difference-bound q r error d n
          errorNonnegative qBound rBound differenceBound)
        qBound qBound
      propagatedRadiusPath =
        cong (Q._· radius) (sym (dyadicRadius-add DExponent d)) ∙
        sym (dyadicRadius-add (DExponent ℕ.+ d) d)
      propagatedScalePath =
        CosineDifferencePaths.propagated-scale PreferredℚCommRing
          D error radius ∙
        cong (Q._· error) propagatedRadiusPath
      propagated = subst
        (MagnitudeBound
          (Q.- (((((difference Q.· q) Q.· q) Q.·
            reciprocalSuccessor firstIndex) Q.· reciprocalSuccessor secondIndex))))
        propagatedScalePath propagatedRaw
      termBound = cosine-term-uniform-growth-bound r d n rBound
      freshLeftRaw = three-factor-reciprocal-magnitude-bound
        (cosineTerm r n) inputDifference q T error radius
        firstIndex secondIndex
        (dyadicRadius-nonnegative TExponent) errorNonnegative
        (dyadicRadius-nonnegative d) termBound differenceBound qBound
      freshRightRaw = three-factor-reciprocal-magnitude-bound
        (cosineTerm r n) r inputDifference T radius error
        firstIndex secondIndex
        (dyadicRadius-nonnegative TExponent) (dyadicRadius-nonnegative d)
        errorNonnegative termBound rBound differenceBound
      freshRadiusPath = sym (dyadicRadius-add TExponent d)
      freshLeftScalePath =
        CosineDifferencePaths.fresh-scale PreferredℚCommRing T error radius ∙
        cong (Q._· error) freshRadiusPath
      freshRightScalePath =
        cong (Q._· error) freshRadiusPath
      freshLeft = subst (MagnitudeBound _)
        freshLeftScalePath freshLeftRaw
      freshRight = subst (MagnitudeBound _)
        freshRightScalePath freshRightRaw
      firstCombined = add-magnitude-bounds _ _ _ _ propagated freshLeft
      combined = add-magnitude-bounds _ _ _ _ firstCombined freshRight
      factored = subst (MagnitudeBound _)
        (CosineDifferencePaths.factor-three-errors PreferredℚCommRing
          (dyadicRadius propagatedExponent) (dyadicRadius freshExponent)
          (dyadicRadius freshExponent) error)
        combined
      scale≤ = ≤-·o
        ((dyadicRadius propagatedExponent Q.+ dyadicRadius freshExponent) Q.+
          dyadicRadius freshExponent)
        (dyadicRadius (cosineTermDifferenceExponent d (suc n)))
        error errorNonnegative (cosine-term-difference-scale-step d n)
      weakened = weaken-magnitude-bound _ _ _ scale≤ factored
  in
  transport-magnitude _ _ _ (cosine-term-difference-step q r n) weakened

