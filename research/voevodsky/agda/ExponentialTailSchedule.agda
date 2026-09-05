{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ExponentialTailSchedule where

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
open import TaylorGeometricTail
open import CauchyProductRegularity

module ExponentialSchedulePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_)

  swap-errors : (a p q : fst R) →
    (a +S q) +S p ≡ (a +S p) +S q
  swap-errors a p q = solve! R

record ExponentialTailSeed (q : Q.ℚ) : Type where
  field
    inputExponent : ℕ
    inputBound : MagnitudeBound q (dyadicRadius inputExponent)
    seedExponent : ℕ
    seedBound : MagnitudeBound
      (exponentialTerm q (dyadicNat (ℕ.suc inputExponent)))
      (dyadicRadius seedExponent)
open ExponentialTailSeed public

baseTaylorCutoff : {q : Q.ℚ} → ExponentialTailSeed q → ℕ
baseTaylorCutoff seed = dyadicNat (ℕ.suc (inputExponent seed))

shiftedExponentialTerm : {q : Q.ℚ} →
  ExponentialTailSeed q → ℕ → Q.ℚ
shiftedExponentialTerm {q} seed n =
  exponentialTerm q (baseTaylorCutoff seed ℕ.+ n)

shiftedExponentialPartialSum : {q : Q.ℚ} →
  ExponentialTailSeed q → ℕ → Q.ℚ
shiftedExponentialPartialSum seed =
  finiteSum (shiftedExponentialTerm seed)

absorbedTaylorCutoff : {q : Q.ℚ} →
  ExponentialTailSeed q → ℕ → ℕ
absorbedTaylorCutoff seed n =
  baseTaylorCutoff seed ℕ.+ (seedExponent seed ℕ.+ n)

seed-bound-nonnegative : {q : Q.ℚ} →
  (seed : ExponentialTailSeed q) →
  0 ≤ dyadicRadius (seedExponent seed)
seed-bound-nonnegative seed = dyadicRadius-nonnegative (seedExponent seed)

exponential-tail-bound-before-absorption :
  {q : Q.ℚ} (seed : ExponentialTailSeed q) (extra : ℕ) →
  MagnitudeBound
    (exponentialTerm q (baseTaylorCutoff seed ℕ.+ extra))
    (dyadicRadius (seedExponent seed) Q.· precision extra)
exponential-tail-bound-before-absorption seed =
  late-exponential-term-geometric-decay
    _ (dyadicRadius (seedExponent seed)) (inputExponent seed)
    (seed-bound-nonnegative seed) (seedBound seed) (inputBound seed)

shifted-exponential-term-geometric-decay :
  {q : Q.ℚ} (seed : ExponentialTailSeed q) (n : ℕ) →
  MagnitudeBound (shiftedExponentialTerm seed n)
    (dyadicRadius (seedExponent seed) Q.· precision n)
shifted-exponential-term-geometric-decay =
  exponential-tail-bound-before-absorption

absorbedExponentialPartialSum : {q : Q.ℚ} →
  ExponentialTailSeed q → ℕ → Q.ℚ
absorbedExponentialPartialSum {q} seed n =
  exponentialPartialSum q (absorbedTaylorCutoff seed n)

exponential-tail-bound-after-absorption :
  {q : Q.ℚ} (seed : ExponentialTailSeed q) (n : ℕ) →
  MagnitudeBound
    (exponentialTerm q (absorbedTaylorCutoff seed n))
    (precision n)
exponential-tail-bound-after-absorption seed n =
  subst (MagnitudeBound
      (exponentialTerm _
        (baseTaylorCutoff seed ℕ.+ (seedExponent seed ℕ.+ n))))
    (radius-cancels-precision-shift (seedExponent seed) n)
    (exponential-tail-bound-before-absorption seed
      (seedExponent seed ℕ.+ n))

absorbed-partial-sum-forward-difference :
  {q : Q.ℚ} (seed : ExponentialTailSeed q) (m count : ℕ) →
  MagnitudeBound
    (absorbedExponentialPartialSum seed (m ℕ.+ count) Q.+
      (Q.- absorbedExponentialPartialSum seed m))
    (precision m)
absorbed-partial-sum-forward-difference {q} seed m count =
  let base = baseTaylorCutoff seed
      exponent = seedExponent seed
      start = exponent ℕ.+ m
      term = exponentialTerm q
      shifted = shiftedExponentialTerm seed
      blockBound = termBlock≤scaledPrecision
        shifted (dyadicRadius exponent) start count
        (dyadicRadius-nonnegative exponent)
        (λ j → shifted-exponential-term-geometric-decay seed (suc j))
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
      (absorbedExponentialPartialSum seed (m ℕ.+ count) Q.+
       (Q.- absorbedExponentialPartialSum seed m)))
    (radius-cancels-precision-shift exponent m)
    reindexed

absorbed-partial-sum-close-forward :
  {q : Q.ℚ} (seed : ExponentialTailSeed q) (m n : ℕ) →
  absorbedExponentialPartialSum seed m ≤
  (absorbedExponentialPartialSum seed n Q.+ precision m) Q.+ precision n
absorbed-partial-sum-close-forward seed m n =
  ℕOrder.≤CaseInduction
    {P = λ i j → absorbedExponentialPartialSum seed i ≤
      (absorbedExponentialPartialSum seed j Q.+ precision i) Q.+ precision j}
    {n = m} {m = n}
    (λ { (count , count+m≡n) →
      let m+count≡n = ℕ.+-comm m count ∙ count+m≡n
          forward : MagnitudeBound
            (absorbedExponentialPartialSum seed n Q.+
             (Q.- absorbedExponentialPartialSum seed m)) (precision m)
          forward = subst
            (λ index → MagnitudeBound
              (absorbedExponentialPartialSum seed index Q.+
               (Q.- absorbedExponentialPartialSum seed m)) (precision m))
            m+count≡n
            (absorbed-partial-sum-forward-difference seed m count)
          reverseDifference :
            absorbedExponentialPartialSum seed m Q.+
              (Q.- absorbedExponentialPartialSum seed n) ≤ precision m
          reverseDifference = subst (λ z → z ≤ precision m)
            (ProductSignPaths.negative-difference PreferredℚCommRing
              (absorbedExponentialPartialSum seed n)
              (absorbedExponentialPartialSum seed m))
            (negative-upper forward)
          widened :
            absorbedExponentialPartialSum seed m Q.+
              (Q.- absorbedExponentialPartialSum seed n) ≤
            precision m Q.+ precision n
          widened = isTrans≤
            (absorbedExponentialPartialSum seed m Q.+
             (Q.- absorbedExponentialPartialSum seed n))
            (precision m) (precision m Q.+ precision n) reverseDifference
            (≤-add-nonnegative (precision m) (precision n)
              (precision-nonnegative n))
      in difference-upper→directed
        (absorbedExponentialPartialSum seed m)
        (absorbedExponentialPartialSum seed n)
        (precision m) (precision n) widened })
    (λ { (count , count+n≡m) →
      let n+count≡m = ℕ.+-comm n count ∙ count+n≡m
          forward : MagnitudeBound
            (absorbedExponentialPartialSum seed m Q.+
             (Q.- absorbedExponentialPartialSum seed n)) (precision n)
          forward = subst
            (λ index → MagnitudeBound
              (absorbedExponentialPartialSum seed index Q.+
               (Q.- absorbedExponentialPartialSum seed n)) (precision n))
            n+count≡m
            (absorbed-partial-sum-forward-difference seed n count)
          widened :
            absorbedExponentialPartialSum seed m Q.+
              (Q.- absorbedExponentialPartialSum seed n) ≤
            precision m Q.+ precision n
          widened = isTrans≤
            (absorbedExponentialPartialSum seed m Q.+
             (Q.- absorbedExponentialPartialSum seed n))
            (precision n) (precision m Q.+ precision n)
            (positive-upper forward)
            (subst (λ z → precision n ≤ z)
              (Q.+Comm (precision n) (precision m))
              (≤-add-nonnegative (precision n) (precision m)
                (precision-nonnegative m)))
      in difference-upper→directed
        (absorbedExponentialPartialSum seed m)
        (absorbedExponentialPartialSum seed n)
        (precision m) (precision n) widened })

absorbedExponentialRegular : {q : Q.ℚ} →
  ExponentialTailSeed q → RegularCauchy
absorbedExponentialRegular seed .approximation =
  absorbedExponentialPartialSum seed
absorbedExponentialRegular seed .close-forward =
  absorbed-partial-sum-close-forward seed
absorbedExponentialRegular seed .close-backward m n =
  subst (absorbedExponentialPartialSum seed n ≤_)
    (ExponentialSchedulePaths.swap-errors PreferredℚCommRing
      (absorbedExponentialPartialSum seed m) (precision m) (precision n))
    (absorbed-partial-sum-close-forward seed n m)
