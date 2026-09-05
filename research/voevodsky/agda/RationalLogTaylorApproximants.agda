{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalLogTaylorApproximants where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.NatPlusOne using (1+_)
open import Cubical.Data.Int as ℤ using (pos)
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Data.Rationals.Order
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import CauchyProductBounds
open import RationalTaylorApproximants

naturalRational : ℕ → Q.ℚ
naturalRational zero = 0
naturalRational (suc n) = naturalRational n Q.+ 1

oddIndex : ℕ → ℕ
oddIndex n = suc (n ℕ.+ n)

nextOddIndex : ℕ → ℕ
nextOddIndex n = suc (suc (oddIndex n))

positiveNaturalLogRatio : ℕ → Q.ℚ
positiveNaturalLogRatio n = Q.[ pos n / 1+ suc n ]

atanhStepRatio : ℕ → Q.ℚ
atanhStepRatio n = positiveNaturalLogRatio (oddIndex n)

atanhTerm : Q.ℚ → ℕ → Q.ℚ
atanhTerm y zero = y
atanhTerm y (suc n) =
  ((atanhTerm y n Q.· y) Q.· y) Q.· atanhStepRatio n

atanhPartialSum : Q.ℚ → ℕ → Q.ℚ
atanhPartialSum y = finiteSum (atanhTerm y)

logRatioPartialSum : Q.ℚ → ℕ → Q.ℚ
logRatioPartialSum y n = (atanhPartialSum y n Q.+ atanhPartialSum y n)

module LogZeroPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  ratio-plus-complement : (x : fst R) → x +S (1r +S (-S x)) ≡ 1r
  ratio-plus-complement x = solve! R

  complement-as-negative-difference : (x : fst R) →
    -S (x +S (-S 1r)) ≡ 1r +S (-S x)
  complement-as-negative-difference x = solve! R

  atanh-zero-step : (a ratio : fst R) →
    ((a ·S 0r) ·S 0r) ·S ratio ≡ 0r
  atanh-zero-step a ratio = solve! R

atanhTerm-at-zero : (n : ℕ) → atanhTerm 0 n ≡ 0
atanhTerm-at-zero zero = refl
atanhTerm-at-zero (suc n) =
  LogZeroPaths.atanh-zero-step PreferredℚCommRing
    (atanhTerm 0 n) (atanhStepRatio n)

atanhPartialSum-at-zero : (n : ℕ) → atanhPartialSum 0 n ≡ 0
atanhPartialSum-at-zero =
  finiteSum-all-zero (atanhTerm 0) atanhTerm-at-zero
  where
  finiteSum-all-zero : (term : ℕ → Q.ℚ) →
    ((n : ℕ) → term n ≡ 0) →
    (n : ℕ) → finiteSum term n ≡ 0
  finiteSum-all-zero term allZero zero = allZero zero
  finiteSum-all-zero term allZero (suc n) =
    cong₂ Q._+_ (finiteSum-all-zero term allZero n) (allZero (suc n)) ∙
    Q.+IdR 0

logRatioPartialSum-at-zero : (n : ℕ) → logRatioPartialSum 0 n ≡ 0
logRatioPartialSum-at-zero n =
  cong₂ Q._+_ (atanhPartialSum-at-zero n) (atanhPartialSum-at-zero n)

positive-natural-log-ratio-nonnegative : (n : ℕ) →
  0 ≤ positiveNaturalLogRatio n
positive-natural-log-ratio-nonnegative n =
  subst (pos 0 ℤOrder.≤_)
    (sym (ℤ.·IdR (pos n))) ℤOrder.zero-≤pos

positive-natural-log-ratio≤one : (n : ℕ) →
  positiveNaturalLogRatio n ≤ 1
positive-natural-log-ratio≤one n =
  subst2 ℤOrder._≤_
    (sym (ℤ.·IdR (pos n)))
    (sym (ℤ.·IdL (pos (suc (suc n)))))
    (nat≤→positive-integer≤ n (suc (suc n)) (2 , refl))

atanh-step-ratio-nonnegative : (n : ℕ) → 0 ≤ atanhStepRatio n
atanh-step-ratio-nonnegative n =
  positive-natural-log-ratio-nonnegative (oddIndex n)

atanh-step-ratio≤one : (n : ℕ) → atanhStepRatio n ≤ 1
atanh-step-ratio≤one n = positive-natural-log-ratio≤one (oddIndex n)

positiveNaturalLogRatioGapCandidate : ℕ → Q.ℚ
positiveNaturalLogRatioGapCandidate n =
  1 Q.+ (Q.- positiveNaturalLogRatio n)

positive-natural-log-ratio-gap-nonnegative : (n : ℕ) →
  0 ≤ positiveNaturalLogRatioGapCandidate n
positive-natural-log-ratio-gap-nonnegative n =
  let ratio = positiveNaturalLogRatio n
      translated : ratio Q.+ (Q.- 1) ≤ 1 Q.+ (Q.- 1)
      translated = ≤-+o ratio 1 (Q.- 1)
        (positive-natural-log-ratio≤one n)
      nonpositive : ratio Q.+ (Q.- 1) ≤ 0
      nonpositive = subst ((ratio Q.+ (Q.- 1)) ≤_)
        (Q.+InvR 1) translated
      negated = nonpositive→negative-nonnegative
        (ratio Q.+ (Q.- 1)) nonpositive
  in subst (0 ≤_)
    (LogZeroPaths.complement-as-negative-difference
      PreferredℚCommRing ratio) negated

positive-natural-log-ratio-plus-gap : (n : ℕ) →
  positiveNaturalLogRatio n Q.+ positiveNaturalLogRatioGapCandidate n ≡ 1
positive-natural-log-ratio-plus-gap n =
  LogZeroPaths.ratio-plus-complement PreferredℚCommRing
    (positiveNaturalLogRatio n)

positiveNaturalLogPartialSum : ℕ → ℕ → Q.ℚ
positiveNaturalLogPartialSum n depth =
  logRatioPartialSum (positiveNaturalLogRatio n) depth

positive-natural-log-ratio-at-one : positiveNaturalLogRatio zero ≡ 0
positive-natural-log-ratio-at-one = Q.eq/ _ _ refl

positive-natural-log-partial-sum-at-one : (depth : ℕ) →
  positiveNaturalLogPartialSum zero depth ≡ 0
positive-natural-log-partial-sum-at-one depth =
  cong (λ ratio → logRatioPartialSum ratio depth)
    positive-natural-log-ratio-at-one ∙
  logRatioPartialSum-at-zero depth
