{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformExponentialDifferenceWeights where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
import Cubical.Data.Int.Order as ℤOrder
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import TaylorTermBounds

-- If a late term difference has weight w, its propagated part contracts by
-- one half.  The fresh part is bounded by the current seed precision; the
-- available reciprocal estimate for that part is only ≤ 1, not ≤ 1/2.
lateDifferenceWeight : ℕ → Q.ℚ
lateDifferenceWeight zero = 1
lateDifferenceWeight (suc n) =
  (lateDifferenceWeight n Q.· one-half) Q.+ precision n

lateDifferenceWeightSum : ℕ → Q.ℚ
lateDifferenceWeightSum zero = 0
lateDifferenceWeightSum (suc n) =
  lateDifferenceWeightSum n Q.+ lateDifferenceWeight n

late-difference-weight-nonnegative : (n : ℕ) → 0 ≤ lateDifferenceWeight n
late-difference-weight-nonnegative zero = ℤOrder.zero-≤pos
late-difference-weight-nonnegative (suc n) =
  ≤Monotone+ 0 (lateDifferenceWeight n Q.· one-half) 0 (precision n)
    (nonnegative-bound-product (lateDifferenceWeight n) one-half
      (late-difference-weight-nonnegative n) one-half-nonnegative)
    (precision-nonnegative n)

late-difference-weight-sum-nonnegative : (n : ℕ) →
  0 ≤ lateDifferenceWeightSum n
late-difference-weight-sum-nonnegative zero = isRefl≤ 0
late-difference-weight-sum-nonnegative (suc n) =
  ≤Monotone+ 0 (lateDifferenceWeightSum n) 0 (lateDifferenceWeight n)
    (late-difference-weight-sum-nonnegative n)
    (late-difference-weight-nonnegative n)

late-difference-weight-step : (n : ℕ) →
  lateDifferenceWeight (suc n) ≡
  (lateDifferenceWeight n Q.· one-half) Q.+ precision n
late-difference-weight-step n = refl

late-difference-weight-sum-step : (n : ℕ) →
  lateDifferenceWeightSum (suc n) ≡
  lateDifferenceWeightSum n Q.+ lateDifferenceWeight n
late-difference-weight-sum-step n = refl

precisionPrefixSum : ℕ → Q.ℚ
precisionPrefixSum zero = 0
precisionPrefixSum (suc n) = precisionPrefixSum n Q.+ precision n

precision-prefix-complement : (n : ℕ) →
  precisionPrefixSum n Q.+ (precision n Q.+ precision n) ≡ 2
precision-prefix-complement zero = refl
precision-prefix-complement (suc n) =
  sym (Q.+Assoc (precisionPrefixSum n) (precision n)
    (precision (suc n) Q.+ precision (suc n))) ∙
  cong (precisionPrefixSum n Q.+_)
    (cong (precision n Q.+_) (precision-refines-double n)) ∙
  precision-prefix-complement n

precision-prefix-sum≤two : (n : ℕ) → precisionPrefixSum n ≤ 2
precision-prefix-sum≤two n =
  subst (precisionPrefixSum n ≤_) (precision-prefix-complement n)
    (≤-add-nonnegative (precisionPrefixSum n)
      (precision n Q.+ precision n)
      (≤Monotone+ 0 (precision n) 0 (precision n)
        (precision-nonnegative n) (precision-nonnegative n)))

module WeightConservationPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  recurrence-rearrange : (S w h p : fst R) →
    (S +S w) +S (((w ·S h) +S p) +S ((w ·S h) +S p)) ≡
    (S +S (w +S ((w ·S h) +S (w ·S h)))) +S (p +S p)
  recurrence-rearrange S w h p = solve! R

  prefix-rearrange : (two P p : fst R) →
    (two +S (P +S P)) +S (p +S p) ≡
    two +S ((P +S p) +S (P +S p))
  prefix-rearrange two P p = solve! R

late-weight-conservation : (n : ℕ) →
  lateDifferenceWeightSum n Q.+
    (lateDifferenceWeight n Q.+ lateDifferenceWeight n) ≡
  2 Q.+ (precisionPrefixSum n Q.+ precisionPrefixSum n)
late-weight-conservation zero = refl
late-weight-conservation (suc n) =
  let S = lateDifferenceWeightSum n
      w = lateDifferenceWeight n
      p = precision n
      halfPair = (w Q.· one-half) Q.+ (w Q.· one-half)
  in
  WeightConservationPaths.recurrence-rearrange
    PreferredℚCommRing S w one-half p ∙
  cong (λ z → (S Q.+ (w Q.+ z)) Q.+ (p Q.+ p))
    (half-double w) ∙
  cong (Q._+ (p Q.+ p)) (late-weight-conservation n) ∙
  WeightConservationPaths.prefix-rearrange
    PreferredℚCommRing 2 (precisionPrefixSum n) p

late-difference-weight-sum≤six : (n : ℕ) →
  lateDifferenceWeightSum n ≤ 6
late-difference-weight-sum≤six n =
  let S = lateDifferenceWeightSum n
      w = lateDifferenceWeight n
      S≤conserved = ≤-add-nonnegative S (w Q.+ w)
        (≤Monotone+ 0 w 0 w
          (late-difference-weight-nonnegative n)
          (late-difference-weight-nonnegative n))
      S≤rhs = subst (S ≤_) (late-weight-conservation n) S≤conserved
      rhs≤six = subst
        ((2 Q.+ (precisionPrefixSum n Q.+ precisionPrefixSum n)) ≤_)
        refl
        (≤Monotone+ 2 2
          (precisionPrefixSum n Q.+ precisionPrefixSum n) (2 Q.+ 2)
          (isRefl≤ 2)
          (≤Monotone+ (precisionPrefixSum n) 2
            (precisionPrefixSum n) 2
            (precision-prefix-sum≤two n) (precision-prefix-sum≤two n)))
  in isTrans≤ S
    (2 Q.+ (precisionPrefixSum n Q.+ precisionPrefixSum n)) 6
    S≤rhs rhs≤six

lateExtensionWeightSum : ℕ → Q.ℚ
lateExtensionWeightSum zero = 0
lateExtensionWeightSum (suc n) =
  lateExtensionWeightSum n Q.+ lateDifferenceWeight (suc n)

initial-plus-extension-weight-sum : (n : ℕ) →
  1 Q.+ lateExtensionWeightSum n ≡ lateDifferenceWeightSum (suc n)
initial-plus-extension-weight-sum zero = Q.+IdR 1
initial-plus-extension-weight-sum (suc n) =
  Q.+Assoc 1 (lateExtensionWeightSum n) (lateDifferenceWeight (suc n)) ∙
  cong (Q._+ lateDifferenceWeight (suc n))
    (initial-plus-extension-weight-sum n)

late-extension-weight-sum≤prefix : (n : ℕ) →
  lateExtensionWeightSum n ≤ lateDifferenceWeightSum (suc n)
late-extension-weight-sum≤prefix zero =
  ≤-add-nonnegative 0 1 ℤOrder.zero-≤pos
late-extension-weight-sum≤prefix (suc n) =
  ≤Monotone+
    (lateExtensionWeightSum n) (lateDifferenceWeightSum (suc n))
    (lateDifferenceWeight (suc n)) (lateDifferenceWeight (suc n))
    (late-extension-weight-sum≤prefix n)
    (isRefl≤ (lateDifferenceWeight (suc n)))

late-extension-weight-sum≤six : (n : ℕ) →
  lateExtensionWeightSum n ≤ 6
late-extension-weight-sum≤six n =
  isTrans≤ (lateExtensionWeightSum n)
    (lateDifferenceWeightSum (suc n)) 6
    (late-extension-weight-sum≤prefix n)
    (late-difference-weight-sum≤six (suc n))
