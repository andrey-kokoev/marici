{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CosineTermBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import RationalTaylorApproximants
open import TaylorTermBounds

module CosineTermPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_; -_ to -S_)

  group-step : (term q firstInverse secondInverse : fst R) →
    -S ((((term ·S q) ·S q) ·S firstInverse) ·S secondInverse) ≡
    -S ((term ·S (q ·S firstInverse)) ·S
        (q ·S secondInverse))
  group-step term q firstInverse secondInverse = solve! R

  step-scale : (T radius : fst R) →
    (((T ·S radius) ·S radius) ·S 1r) ·S 1r ≡
      (T ·S radius) ·S radius
  step-scale T radius = solve! R

cosine-term-step-bound :
  (q T R : Q.ℚ) (n : ℕ) →
  0 ≤ T → 0 ≤ R →
  MagnitudeBound (cosineTerm q n) T →
  MagnitudeBound q R →
  MagnitudeBound (cosineTerm q (suc n)) ((T Q.· R) Q.· R)
cosine-term-step-bound q T R n 0≤T 0≤R termBound qBound =
  let TRNonnegative = nonnegative-bound-product T R 0≤T 0≤R
      TRRNonnegative = nonnegative-bound-product (T Q.· R) R
        TRNonnegative 0≤R
      firstProduct = arbitrary-multiplier-bound
        (cosineTerm q n) T q R 0≤T 0≤R termBound qBound
      secondProduct = arbitrary-multiplier-bound
        (cosineTerm q n Q.· q) (T Q.· R) q R
        TRNonnegative 0≤R firstProduct qBound
      firstReciprocal = arbitrary-multiplier-bound
        ((cosineTerm q n Q.· q) Q.· q) ((T Q.· R) Q.· R)
        (reciprocalSuccessor (firstCosineDenominator n)) 1
        TRRNonnegative (dyadicRadius-nonnegative 0) secondProduct
        (reciprocal-magnitude≤one (firstCosineDenominator n))
      secondReciprocal = arbitrary-multiplier-bound
        (((cosineTerm q n Q.· q) Q.· q) Q.·
          reciprocalSuccessor (firstCosineDenominator n))
        (((T Q.· R) Q.· R) Q.· 1)
        (reciprocalSuccessor (secondCosineDenominator n)) 1
        (nonnegative-bound-product ((T Q.· R) Q.· R) 1
          TRRNonnegative (dyadicRadius-nonnegative 0))
        (dyadicRadius-nonnegative 0) firstReciprocal
        (reciprocal-magnitude≤one (secondCosineDenominator n))
      scaled = subst
        (MagnitudeBound
          ((((cosineTerm q n Q.· q) Q.· q) Q.·
            reciprocalSuccessor (firstCosineDenominator n)) Q.·
           reciprocalSuccessor (secondCosineDenominator n)))
        (CosineTermPaths.step-scale PreferredℚCommRing T R)
        secondReciprocal
  in
  negate-magnitude-bound _ _ scaled

first-cosine-denominator-at-late-index : (d extra : ℕ) →
  firstCosineDenominator (dyadicNat (suc d) ℕ.+ extra) ≡
  dyadicNat (suc d) ℕ.+
    (extra ℕ.+ (dyadicNat (suc d) ℕ.+ extra))
first-cosine-denominator-at-late-index d extra =
  sym (ℕ.+-assoc (dyadicNat (suc d)) extra
    (dyadicNat (suc d) ℕ.+ extra))

second-cosine-denominator-at-late-index : (d extra : ℕ) →
  secondCosineDenominator (dyadicNat (suc d) ℕ.+ extra) ≡
  dyadicNat (suc d) ℕ.+
    suc (extra ℕ.+ (dyadicNat (suc d) ℕ.+ extra))
second-cosine-denominator-at-late-index d extra =
  cong suc (first-cosine-denominator-at-late-index d extra) ∙
  sym (ℕ.+-suc (dyadicNat (suc d))
    (extra ℕ.+ (dyadicNat (suc d) ℕ.+ extra)))

late-cosine-first-factor-magnitude≤half :
  (q : Q.ℚ) (d extra : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound
    (q Q.· reciprocalSuccessor
      (firstCosineDenominator (dyadicNat (suc d) ℕ.+ extra)))
    one-half
late-cosine-first-factor-magnitude≤half q d extra qBound =
  subst (λ index → MagnitudeBound
      (q Q.· reciprocalSuccessor index) one-half)
    (sym (first-cosine-denominator-at-late-index d extra))
    (later-scaled-input-magnitude≤half q d
      (extra ℕ.+ (dyadicNat (suc d) ℕ.+ extra)) qBound)

late-cosine-second-factor-magnitude≤half :
  (q : Q.ℚ) (d extra : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound
    (q Q.· reciprocalSuccessor
      (secondCosineDenominator (dyadicNat (suc d) ℕ.+ extra)))
    one-half
late-cosine-second-factor-magnitude≤half q d extra qBound =
  subst (λ index → MagnitudeBound
      (q Q.· reciprocalSuccessor index) one-half)
    (sym (second-cosine-denominator-at-late-index d extra))
    (later-scaled-input-magnitude≤half q d
      (suc (extra ℕ.+ (dyadicNat (suc d) ℕ.+ extra))) qBound)

late-cosine-term-contraction :
  (q T : Q.ℚ) (d extra : ℕ) →
  0 ≤ T →
  MagnitudeBound
    (cosineTerm q (dyadicNat (suc d) ℕ.+ extra)) T →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound
    (cosineTerm q (suc (dyadicNat (suc d) ℕ.+ extra)))
    (T Q.· one-half)
late-cosine-term-contraction q T d extra 0≤T termBound qBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      firstFactor = q Q.· reciprocalSuccessor
        (firstCosineDenominator index)
      secondFactor = q Q.· reciprocalSuccessor
        (secondCosineDenominator index)
      firstBound = arbitrary-multiplier-bound
        (cosineTerm q index) T firstFactor one-half
        0≤T one-half-nonnegative termBound
        (late-cosine-first-factor-magnitude≤half q d extra qBound)
      T-half-nonnegative = nonnegative-bound-product
        T one-half 0≤T one-half-nonnegative
      quarterBound = arbitrary-multiplier-bound
        (cosineTerm q index Q.· firstFactor) (T Q.· one-half)
        secondFactor one-half
        T-half-nonnegative one-half-nonnegative firstBound
        (late-cosine-second-factor-magnitude≤half q d extra qBound)
      quarter≤half = subst
        (((T Q.· one-half) Q.· one-half) ≤_)
        (Q.·IdR (T Q.· one-half))
        (left-multiply-monotone (T Q.· one-half) one-half 1
          T-half-nonnegative (precision-step≤ zero))
      halfBound = weaken-magnitude-bound _ _ (T Q.· one-half)
        quarter≤half quarterBound
      grouped = transport-magnitude _ _ (T Q.· one-half)
        (CosineTermPaths.group-step PreferredℚCommRing
          (cosineTerm q index) q
          (reciprocalSuccessor (firstCosineDenominator index))
          (reciprocalSuccessor (secondCosineDenominator index)))
        (negate-magnitude-bound _ _ halfBound)
  in grouped

late-cosine-term-geometric-decay :
  (q T : Q.ℚ) (d : ℕ) →
  0 ≤ T →
  MagnitudeBound (cosineTerm q (dyadicNat (suc d))) T →
  MagnitudeBound q (dyadicRadius d) →
  (extra : ℕ) →
  MagnitudeBound
    (cosineTerm q (dyadicNat (suc d) ℕ.+ extra))
    (T Q.· precision extra)
late-cosine-term-geometric-decay q T d 0≤T initial qBound zero =
  subst (MagnitudeBound
      (cosineTerm q (dyadicNat (suc d) ℕ.+ zero)))
    (sym (Q.·IdR T))
    (transport-magnitude _ _ T
      (cong (cosineTerm q) (ℕ.+-zero (dyadicNat (suc d)))) initial)
late-cosine-term-geometric-decay q T d 0≤T initial qBound (suc extra) =
  let previous = late-cosine-term-geometric-decay
        q T d 0≤T initial qBound extra
      previousBoundNonnegative = nonnegative-bound-product
        T (precision extra) 0≤T (precision-nonnegative extra)
      contracted = late-cosine-term-contraction
        q (T Q.· precision extra) d extra
        previousBoundNonnegative previous qBound
      reindexed = transport-magnitude _ _
        ((T Q.· precision extra) Q.· one-half)
        (cong (cosineTerm q)
          (ℕ.+-suc (dyadicNat (suc d)) extra))
        contracted
  in
  subst (MagnitudeBound
      (cosineTerm q (dyadicNat (suc d) ℕ.+ suc extra)))
    (sym (Q.·Assoc T (precision extra) one-half))
    reindexed
