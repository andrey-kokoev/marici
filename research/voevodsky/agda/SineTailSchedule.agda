{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module SineTailSchedule where

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
open import RationalSineTaylorApproximants
open import TaylorTermBounds
open import SineTermBounds
open import TaylorGeometricTail
open import CauchyProductRegularity

module SineSchedulePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_)

  swap-errors : (a p q : fst R) →
    (a +S q) +S p ≡ (a +S p) +S q
  swap-errors a p q = solve! R

record SineTailSeed (q : Q.ℚ) : Type where
  field
    inputExponent : ℕ
    inputBound : MagnitudeBound q (dyadicRadius inputExponent)
    seedExponent : ℕ
    seedBound : MagnitudeBound
      (sineTerm q (dyadicNat (suc inputExponent)))
      (dyadicRadius seedExponent)
open SineTailSeed public

baseSineCutoff : {q : Q.ℚ} → SineTailSeed q → ℕ
baseSineCutoff seed = dyadicNat (suc (inputExponent seed))

shiftedSineTerm : {q : Q.ℚ} → SineTailSeed q → ℕ → Q.ℚ
shiftedSineTerm {q} seed n =
  sineTerm q (baseSineCutoff seed ℕ.+ n)

absorbedSineCutoff : {q : Q.ℚ} → SineTailSeed q → ℕ → ℕ
absorbedSineCutoff seed n =
  baseSineCutoff seed ℕ.+ (seedExponent seed ℕ.+ n)

absorbedSinePartialSum : {q : Q.ℚ} →
  SineTailSeed q → ℕ → Q.ℚ
absorbedSinePartialSum {q} seed n =
  sinePartialSum q (absorbedSineCutoff seed n)

shifted-sine-term-geometric-decay :
  {q : Q.ℚ} (seed : SineTailSeed q) (n : ℕ) →
  MagnitudeBound (shiftedSineTerm seed n)
    (dyadicRadius (seedExponent seed) Q.· precision n)
shifted-sine-term-geometric-decay seed =
  late-sine-term-geometric-decay
    _ (dyadicRadius (seedExponent seed)) (inputExponent seed)
    (dyadicRadius-nonnegative (seedExponent seed))
    (seedBound seed) (inputBound seed)

sine-tail-bound-after-absorption :
  {q : Q.ℚ} (seed : SineTailSeed q) (n : ℕ) →
  MagnitudeBound
    (sineTerm q (absorbedSineCutoff seed n))
    (precision n)
sine-tail-bound-after-absorption seed n =
  subst (MagnitudeBound
      (sineTerm _
        (baseSineCutoff seed ℕ.+ (seedExponent seed ℕ.+ n))))
    (radius-cancels-precision-shift (seedExponent seed) n)
    (shifted-sine-term-geometric-decay seed
      (seedExponent seed ℕ.+ n))

absorbed-sine-forward-difference :
  {q : Q.ℚ} (seed : SineTailSeed q) (m count : ℕ) →
  MagnitudeBound
    (absorbedSinePartialSum seed (m ℕ.+ count) Q.+
      (Q.- absorbedSinePartialSum seed m))
    (precision m)
absorbed-sine-forward-difference {q} seed m count =
  let base = baseSineCutoff seed
      exponent = seedExponent seed
      start = exponent ℕ.+ m
      term = sineTerm q
      shifted = shiftedSineTerm seed
      blockBound = termBlock≤scaledPrecision
        shifted (dyadicRadius exponent) start count
        (dyadicRadius-nonnegative exponent)
        (λ j → shifted-sine-term-geometric-decay seed (suc j))
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
      (absorbedSinePartialSum seed (m ℕ.+ count) Q.+
       (Q.- absorbedSinePartialSum seed m)))
    (radius-cancels-precision-shift exponent m) reindexed

absorbed-sine-close-forward :
  {q : Q.ℚ} (seed : SineTailSeed q) (m n : ℕ) →
  absorbedSinePartialSum seed m ≤
  (absorbedSinePartialSum seed n Q.+ precision m) Q.+ precision n
absorbed-sine-close-forward seed m n =
  ℕOrder.≤CaseInduction
    {P = λ i j → absorbedSinePartialSum seed i ≤
      (absorbedSinePartialSum seed j Q.+ precision i) Q.+ precision j}
    {n = m} {m = n}
    (λ { (count , count+m≡n) →
      let m+count≡n = ℕ.+-comm m count ∙ count+m≡n
          forward : MagnitudeBound
            (absorbedSinePartialSum seed n Q.+
             (Q.- absorbedSinePartialSum seed m)) (precision m)
          forward = subst
            (λ index → MagnitudeBound
              (absorbedSinePartialSum seed index Q.+
               (Q.- absorbedSinePartialSum seed m)) (precision m))
            m+count≡n (absorbed-sine-forward-difference seed m count)
          reverseDifference :
            absorbedSinePartialSum seed m Q.+
              (Q.- absorbedSinePartialSum seed n) ≤ precision m
          reverseDifference = subst (λ z → z ≤ precision m)
            (ProductSignPaths.negative-difference PreferredℚCommRing
              (absorbedSinePartialSum seed n)
              (absorbedSinePartialSum seed m))
            (negative-upper forward)
          widened :
            absorbedSinePartialSum seed m Q.+
              (Q.- absorbedSinePartialSum seed n) ≤
            precision m Q.+ precision n
          widened = isTrans≤
            (absorbedSinePartialSum seed m Q.+
             (Q.- absorbedSinePartialSum seed n))
            (precision m) (precision m Q.+ precision n) reverseDifference
            (≤-add-nonnegative (precision m) (precision n)
              (precision-nonnegative n))
      in difference-upper→directed
        (absorbedSinePartialSum seed m)
        (absorbedSinePartialSum seed n)
        (precision m) (precision n) widened })
    (λ { (count , count+n≡m) →
      let n+count≡m = ℕ.+-comm n count ∙ count+n≡m
          forward : MagnitudeBound
            (absorbedSinePartialSum seed m Q.+
             (Q.- absorbedSinePartialSum seed n)) (precision n)
          forward = subst
            (λ index → MagnitudeBound
              (absorbedSinePartialSum seed index Q.+
               (Q.- absorbedSinePartialSum seed n)) (precision n))
            n+count≡m (absorbed-sine-forward-difference seed n count)
          widened :
            absorbedSinePartialSum seed m Q.+
              (Q.- absorbedSinePartialSum seed n) ≤
            precision m Q.+ precision n
          widened = isTrans≤
            (absorbedSinePartialSum seed m Q.+
             (Q.- absorbedSinePartialSum seed n))
            (precision n) (precision m Q.+ precision n)
            (positive-upper forward)
            (subst (λ z → precision n ≤ z)
              (Q.+Comm (precision n) (precision m))
              (≤-add-nonnegative (precision n) (precision m)
                (precision-nonnegative m)))
      in difference-upper→directed
        (absorbedSinePartialSum seed m)
        (absorbedSinePartialSum seed n)
        (precision m) (precision n) widened })

absorbedSineRegular : {q : Q.ℚ} → SineTailSeed q → RegularCauchy
absorbedSineRegular seed .approximation = absorbedSinePartialSum seed
absorbedSineRegular seed .close-forward = absorbed-sine-close-forward seed
absorbedSineRegular seed .close-backward m n =
  subst (absorbedSinePartialSum seed n ≤_)
    (SineSchedulePaths.swap-errors PreferredℚCommRing
      (absorbedSinePartialSum seed m) (precision m) (precision n))
    (absorbed-sine-close-forward seed n m)
