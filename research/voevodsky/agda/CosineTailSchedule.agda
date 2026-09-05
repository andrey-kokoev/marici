{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CosineTailSchedule where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import RationalTaylorApproximants
open import TaylorTermBounds
open import CosineTermBounds
open import TaylorGeometricTail
open import CauchyProductRegularity

module CosineSchedulePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_)

  swap-errors : (a p q : fst R) →
    (a +S q) +S p ≡ (a +S p) +S q
  swap-errors a p q = solve! R

record CosineTailSeed (q : Q.ℚ) : Type where
  field
    inputExponent : ℕ
    inputBound : MagnitudeBound q (dyadicRadius inputExponent)
    seedExponent : ℕ
    seedBound : MagnitudeBound
      (cosineTerm q (dyadicNat (suc inputExponent)))
      (dyadicRadius seedExponent)
open CosineTailSeed public

baseCosineCutoff : {q : Q.ℚ} → CosineTailSeed q → ℕ
baseCosineCutoff seed = dyadicNat (suc (inputExponent seed))

shiftedCosineTerm : {q : Q.ℚ} → CosineTailSeed q → ℕ → Q.ℚ
shiftedCosineTerm {q} seed n =
  cosineTerm q (baseCosineCutoff seed ℕ.+ n)

absorbedCosineCutoff : {q : Q.ℚ} → CosineTailSeed q → ℕ → ℕ
absorbedCosineCutoff seed n =
  baseCosineCutoff seed ℕ.+ (seedExponent seed ℕ.+ n)

absorbedCosinePartialSum : {q : Q.ℚ} →
  CosineTailSeed q → ℕ → Q.ℚ
absorbedCosinePartialSum {q} seed n =
  cosinePartialSum q (absorbedCosineCutoff seed n)

shifted-cosine-term-geometric-decay :
  {q : Q.ℚ} (seed : CosineTailSeed q) (n : ℕ) →
  MagnitudeBound (shiftedCosineTerm seed n)
    (dyadicRadius (seedExponent seed) Q.· precision n)
shifted-cosine-term-geometric-decay seed =
  late-cosine-term-geometric-decay
    _ (dyadicRadius (seedExponent seed)) (inputExponent seed)
    (dyadicRadius-nonnegative (seedExponent seed))
    (seedBound seed) (inputBound seed)

cosine-tail-bound-after-absorption :
  {q : Q.ℚ} (seed : CosineTailSeed q) (n : ℕ) →
  MagnitudeBound
    (cosineTerm q (absorbedCosineCutoff seed n))
    (precision n)
cosine-tail-bound-after-absorption seed n =
  subst (MagnitudeBound
      (cosineTerm _
        (baseCosineCutoff seed ℕ.+ (seedExponent seed ℕ.+ n))))
    (radius-cancels-precision-shift (seedExponent seed) n)
    (shifted-cosine-term-geometric-decay seed
      (seedExponent seed ℕ.+ n))

absorbed-cosine-forward-difference :
  {q : Q.ℚ} (seed : CosineTailSeed q) (m count : ℕ) →
  MagnitudeBound
    (absorbedCosinePartialSum seed (m ℕ.+ count) Q.+
      (Q.- absorbedCosinePartialSum seed m))
    (precision m)
absorbed-cosine-forward-difference {q} seed m count =
  let base = baseCosineCutoff seed
      exponent = seedExponent seed
      start = exponent ℕ.+ m
      term = cosineTerm q
      shifted = shiftedCosineTerm seed
      blockBound = termBlock≤scaledPrecision
        shifted (dyadicRadius exponent) start count
        (dyadicRadius-nonnegative exponent)
        (λ j → shifted-cosine-term-geometric-decay seed (suc j))
      old-to-new-index =
        sym (ℕ.+-assoc base start count) ∙
        cong (base ℕ.+_) (sym (ℕ.+-assoc exponent m count))
      difference-to-shifted-block =
        cong (λ index → finiteSum term index Q.+
          (Q.- finiteSum term (base ℕ.+ start)))
          (sym old-to-new-index) ∙
        cong (Q._+ (Q.- finiteSum term (base ℕ.+ start)))
          (finiteSum-segment term (base ℕ.+ start) count) ∙
        PartialSumPaths.remove-base PreferredℚCommRing
          (finiteSum term (base ℕ.+ start))
          (termBlock term (base ℕ.+ start) count) ∙
        termBlock-shift term base start count
      reindexed = transport-magnitude _ _
        (dyadicRadius exponent Q.· precision start)
        difference-to-shifted-block blockBound
  in
  subst (MagnitudeBound
      (absorbedCosinePartialSum seed (m ℕ.+ count) Q.+
       (Q.- absorbedCosinePartialSum seed m)))
    (radius-cancels-precision-shift exponent m)
    reindexed

absorbed-cosine-close-forward :
  {q : Q.ℚ} (seed : CosineTailSeed q) (m n : ℕ) →
  absorbedCosinePartialSum seed m ≤
  (absorbedCosinePartialSum seed n Q.+ precision m) Q.+ precision n
absorbed-cosine-close-forward seed m n =
  ℕOrder.≤CaseInduction
    {P = λ i j → absorbedCosinePartialSum seed i ≤
      (absorbedCosinePartialSum seed j Q.+ precision i) Q.+ precision j}
    {n = m} {m = n}
    (λ { (count , count+m≡n) →
      let m+count≡n = ℕ.+-comm m count ∙ count+m≡n
          forward : MagnitudeBound
            (absorbedCosinePartialSum seed n Q.+
             (Q.- absorbedCosinePartialSum seed m)) (precision m)
          forward = subst
            (λ index → MagnitudeBound
              (absorbedCosinePartialSum seed index Q.+
               (Q.- absorbedCosinePartialSum seed m)) (precision m))
            m+count≡n
            (absorbed-cosine-forward-difference seed m count)
          reverseDifference :
            absorbedCosinePartialSum seed m Q.+
              (Q.- absorbedCosinePartialSum seed n) ≤ precision m
          reverseDifference = subst (λ z → z ≤ precision m)
            (ProductSignPaths.negative-difference PreferredℚCommRing
              (absorbedCosinePartialSum seed n)
              (absorbedCosinePartialSum seed m))
            (negative-upper forward)
          widened :
            absorbedCosinePartialSum seed m Q.+
              (Q.- absorbedCosinePartialSum seed n) ≤
            precision m Q.+ precision n
          widened = isTrans≤
            (absorbedCosinePartialSum seed m Q.+
             (Q.- absorbedCosinePartialSum seed n))
            (precision m) (precision m Q.+ precision n) reverseDifference
            (≤-add-nonnegative (precision m) (precision n)
              (precision-nonnegative n))
      in difference-upper→directed
        (absorbedCosinePartialSum seed m)
        (absorbedCosinePartialSum seed n)
        (precision m) (precision n) widened })
    (λ { (count , count+n≡m) →
      let n+count≡m = ℕ.+-comm n count ∙ count+n≡m
          forward : MagnitudeBound
            (absorbedCosinePartialSum seed m Q.+
             (Q.- absorbedCosinePartialSum seed n)) (precision n)
          forward = subst
            (λ index → MagnitudeBound
              (absorbedCosinePartialSum seed index Q.+
               (Q.- absorbedCosinePartialSum seed n)) (precision n))
            n+count≡m
            (absorbed-cosine-forward-difference seed n count)
          widened :
            absorbedCosinePartialSum seed m Q.+
              (Q.- absorbedCosinePartialSum seed n) ≤
            precision m Q.+ precision n
          widened = isTrans≤
            (absorbedCosinePartialSum seed m Q.+
             (Q.- absorbedCosinePartialSum seed n))
            (precision n) (precision m Q.+ precision n)
            (positive-upper forward)
            (subst (λ z → precision n ≤ z)
              (Q.+Comm (precision n) (precision m))
              (≤-add-nonnegative (precision n) (precision m)
                (precision-nonnegative m)))
      in difference-upper→directed
        (absorbedCosinePartialSum seed m)
        (absorbedCosinePartialSum seed n)
        (precision m) (precision n) widened })

absorbedCosineRegular : {q : Q.ℚ} →
  CosineTailSeed q → RegularCauchy
absorbedCosineRegular seed .approximation = absorbedCosinePartialSum seed
absorbedCosineRegular seed .close-forward = absorbed-cosine-close-forward seed
absorbedCosineRegular seed .close-backward m n =
  subst (absorbedCosinePartialSum seed n ≤_)
    (CosineSchedulePaths.swap-errors PreferredℚCommRing
      (absorbedCosinePartialSum seed m) (precision m) (precision n))
    (absorbed-cosine-close-forward seed n m)
