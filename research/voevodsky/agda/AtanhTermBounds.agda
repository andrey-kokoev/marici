{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module AtanhTermBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Properties as ℕProperties
import Cubical.Data.Int.Order
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import TaylorTermBounds
open import RationalLogTaylorApproximants
open import RationalLogConvergenceContract

module AtanhTermBoundPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_)

  group-square-scale : (T y : fst R) →
    (T ·S y) ·S y ≡ T ·S (y ·S y)
  group-square-scale T y = solve! R

  iterated-square-scale : (T power y : fst R) →
    ((T ·S power) ·S y) ·S y ≡ T ·S (power ·S (y ·S y))
  iterated-square-scale T power y = solve! R

  remove-final-unit : (T y : fst R) →
    (((T ·S y) ·S y) ·S 1r) ≡ (T ·S y) ·S y
  remove-final-unit T y = solve! R

atanh-initial-term-bound :
  (ratio : Q.ℚ) → AtanhContractionInput ratio →
  MagnitudeBound (atanhTerm ratio zero) 1
atanh-initial-term-bound ratio contraction =
  nonnegative-value-magnitude ratio 1
    (ratioNonnegative contraction)
    (atanh-contraction-ratio≤one ratio contraction)
    Cubical.Data.Int.Order.zero-≤pos

atanh-ratio-self-magnitude :
  (ratio : Q.ℚ) → AtanhContractionInput ratio →
  MagnitudeBound ratio ratio
atanh-ratio-self-magnitude ratio contraction =
  nonnegative-value-magnitude ratio ratio
    (ratioNonnegative contraction) (isRefl≤ ratio)
    (ratioNonnegative contraction)

atanh-step-ratio-magnitude≤one : (n : ℕ) →
  MagnitudeBound (atanhStepRatio n) 1
atanh-step-ratio-magnitude≤one n =
  nonnegative-value-magnitude (atanhStepRatio n) 1
    (atanh-step-ratio-nonnegative n) (atanh-step-ratio≤one n)
    (Cubical.Data.Int.Order.zero-≤pos)

atanh-term-step-square-bound :
  (ratio T : Q.ℚ) (n : ℕ) →
  AtanhContractionInput ratio → 0 ≤ T →
  MagnitudeBound (atanhTerm ratio n) T →
  MagnitudeBound (atanhTerm ratio (suc n)) ((T Q.· ratio) Q.· ratio)
atanh-term-step-square-bound ratio T n contraction 0≤T termBound =
  let ratioBound = atanh-ratio-self-magnitude ratio contraction
      firstScaleNonnegative = nonnegative-bound-product T ratio 0≤T
        (ratioNonnegative contraction)
      secondScaleNonnegative = nonnegative-bound-product
        (T Q.· ratio) ratio firstScaleNonnegative
        (ratioNonnegative contraction)
      firstProduct = arbitrary-multiplier-bound
        (atanhTerm ratio n) T ratio ratio
        0≤T (ratioNonnegative contraction) termBound ratioBound
      secondProduct = arbitrary-multiplier-bound
        (atanhTerm ratio n Q.· ratio) (T Q.· ratio) ratio ratio
        firstScaleNonnegative (ratioNonnegative contraction)
        firstProduct ratioBound
      withStepRatio = arbitrary-multiplier-bound
        ((atanhTerm ratio n Q.· ratio) Q.· ratio)
        ((T Q.· ratio) Q.· ratio)
        (atanhStepRatio n) 1 secondScaleNonnegative
        (Cubical.Data.Int.Order.zero-≤pos) secondProduct
        (atanh-step-ratio-magnitude≤one n)
  in subst
    (MagnitudeBound (atanhTerm ratio (suc n)))
    (AtanhTermBoundPaths.remove-final-unit PreferredℚCommRing T ratio)
    withStepRatio

atanhRationalPower : Q.ℚ → ℕ → Q.ℚ
atanhRationalPower base zero = 1
atanhRationalPower base (suc n) = atanhRationalPower base n Q.· base

atanh-rational-power-nonnegative : (base : Q.ℚ) → 0 ≤ base →
  (n : ℕ) → 0 ≤ atanhRationalPower base n
atanh-rational-power-nonnegative base 0≤base zero = Cubical.Data.Int.Order.zero-≤pos
atanh-rational-power-nonnegative base 0≤base (suc n) =
  nonnegative-bound-product
    (atanhRationalPower base n) base
    (atanh-rational-power-nonnegative base 0≤base n) 0≤base

atanh-rational-power-monotone : (a b : Q.ℚ) →
  0 ≤ a → 0 ≤ b → a ≤ b →
  (n : ℕ) → atanhRationalPower a n ≤ atanhRationalPower b n
atanh-rational-power-monotone a b 0≤a 0≤b a≤b zero = isRefl≤ 1
atanh-rational-power-monotone a b 0≤a 0≤b a≤b (suc n) =
  let previous = atanh-rational-power-monotone a b 0≤a 0≤b a≤b n
      firstRaw = left-multiply-monotone a
        (atanhRationalPower a n) (atanhRationalPower b n) 0≤a previous
      first = subst2 _≤_
        (Q.·Comm a (atanhRationalPower a n))
        (Q.·Comm a (atanhRationalPower b n)) firstRaw
      second = left-multiply-monotone (atanhRationalPower b n) a b
        (atanh-rational-power-nonnegative b 0≤b n) a≤b
  in isTrans≤
    (atanhRationalPower a n Q.· a)
    (atanhRationalPower b n Q.· a)
    (atanhRationalPower b n Q.· b)
    first second

square-power-below-power : (base : Q.ℚ) →
  0 ≤ base → base ≤ 1 → (n : ℕ) →
  atanhRationalPower (base Q.· base) n ≤ atanhRationalPower base n
square-power-below-power base 0≤base base≤one n =
  atanh-rational-power-monotone (base Q.· base) base
    (nonnegative-bound-product base base 0≤base 0≤base) 0≤base
    (subst (base Q.· base ≤_)
      (Q.·IdR base)
      (left-multiply-monotone base base 1 0≤base base≤one)) n

module RationalPowerPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_)

  regroup-product : (x y a b : fst R) →
    (x ·S y) ·S (a ·S b) ≡ (x ·S a) ·S (y ·S b)
  regroup-product x y a b = solve! R

atanh-rational-power-one : (n : ℕ) → atanhRationalPower 1 n ≡ 1
atanh-rational-power-one zero = refl
atanh-rational-power-one (suc n) =
  cong (Q._· 1) (atanh-rational-power-one n) ∙ Q.·IdR 1

atanh-rational-power-product : (a b : Q.ℚ) (n : ℕ) →
  atanhRationalPower (a Q.· b) n ≡
  atanhRationalPower a n Q.· atanhRationalPower b n
atanh-rational-power-product a b zero = sym (Q.·IdR 1)
atanh-rational-power-product a b (suc n) =
  cong (Q._· (a Q.· b)) (atanh-rational-power-product a b n) ∙
  RationalPowerPaths.regroup-product PreferredℚCommRing
    (atanhRationalPower a n) (atanhRationalPower b n) a b

rational-power-below-one : (base : Q.ℚ) →
  0 ≤ base → base ≤ 1 → (n : ℕ) → atanhRationalPower base n ≤ 1
rational-power-below-one base 0≤base base≤one n =
  subst (atanhRationalPower base n ≤_)
    (atanh-rational-power-one n)
    (atanh-rational-power-monotone base 1 0≤base
      Cubical.Data.Int.Order.zero-≤pos base≤one n)

atanh-rational-power-add : (base : Q.ℚ) (m n : ℕ) →
  atanhRationalPower base (m ℕ.+ n) ≡
  atanhRationalPower base m Q.· atanhRationalPower base n
atanh-rational-power-add base m zero =
  cong (atanhRationalPower base) (ℕ.+-zero m) ∙ sym (Q.·IdR _)
atanh-rational-power-add base m (suc n) =
  cong (atanhRationalPower base) (ℕ.+-suc m n) ∙
  cong (Q._· base) (atanh-rational-power-add base m n) ∙
  sym (Q.·Assoc
    (atanhRationalPower base m) (atanhRationalPower base n) base)

atanh-rational-power-multiply : (base : Q.ℚ) (block stage : ℕ) →
  atanhRationalPower base (block ℕ.· stage) ≡
  atanhRationalPower (atanhRationalPower base block) stage
atanh-rational-power-multiply base block zero =
  cong (atanhRationalPower base) (sym (ℕProperties.0≡m·0 block))
atanh-rational-power-multiply base block (suc stage) =
  cong (atanhRationalPower base) (ℕ.·-suc block stage) ∙
  atanh-rational-power-add base block (block ℕ.· stage) ∙
  cong (atanhRationalPower base block Q.·_)
    (atanh-rational-power-multiply base block stage) ∙
  Q.·Comm (atanhRationalPower base block)
    (atanhRationalPower (atanhRationalPower base block) stage)

rational-power≤precision : (base : Q.ℚ) →
  0 ≤ base → base ≤ one-half →
  (n : ℕ) → atanhRationalPower base n ≤ precision n
rational-power≤precision base 0≤base base≤half zero = isRefl≤ 1
rational-power≤precision base 0≤base base≤half (suc n) =
  let previous = rational-power≤precision base 0≤base base≤half n
      firstRaw = left-multiply-monotone base
        (atanhRationalPower base n) (precision n) 0≤base previous
      first = subst2 _≤_
        (Q.·Comm base (atanhRationalPower base n))
        (Q.·Comm base (precision n)) firstRaw
      second = left-multiply-monotone (precision n) base one-half
        (precision-nonnegative n) base≤half
  in isTrans≤
    (atanhRationalPower base n Q.· base)
    (precision n Q.· base)
    (precision n Q.· one-half) first second

atanh-term-iterated-square-bound :
  (ratio T : Q.ℚ) (start count : ℕ) →
  AtanhContractionInput ratio → 0 ≤ T →
  MagnitudeBound (atanhTerm ratio start) T →
  MagnitudeBound (atanhTerm ratio (start ℕ.+ count))
    (T Q.· atanhRationalPower (ratio Q.· ratio) count)
atanh-term-iterated-square-bound ratio T start zero contraction 0≤T initial =
  subst (MagnitudeBound (atanhTerm ratio (start ℕ.+ zero)))
    (sym (Q.·IdR T))
    (transport-magnitude _ _ T
      (cong (atanhTerm ratio) (ℕ.+-zero start)) initial)
atanh-term-iterated-square-bound ratio T start (suc count)
  contraction 0≤T initial =
  let squareNonnegative = nonnegative-bound-product ratio ratio
        (ratioNonnegative contraction) (ratioNonnegative contraction)
      previousScaleNonnegative = nonnegative-bound-product T
        (atanhRationalPower (ratio Q.· ratio) count) 0≤T
        (atanh-rational-power-nonnegative (ratio Q.· ratio)
          squareNonnegative count)
      previous = atanh-term-iterated-square-bound
        ratio T start count contraction 0≤T initial
      stepped = atanh-term-step-square-bound ratio
        (T Q.· atanhRationalPower (ratio Q.· ratio) count)
        (start ℕ.+ count) contraction previousScaleNonnegative previous
      reindexed = transport-magnitude _ _
        (((T Q.· atanhRationalPower (ratio Q.· ratio) count) Q.· ratio) Q.· ratio)
        (cong (atanhTerm ratio) (ℕ.+-suc start count)) stepped
  in subst (MagnitudeBound (atanhTerm ratio (start ℕ.+ suc count)))
    (AtanhTermBoundPaths.iterated-square-scale PreferredℚCommRing
      T (atanhRationalPower (ratio Q.· ratio) count) ratio)
    reindexed

atanh-term-step-nonincreasing :
  (ratio T : Q.ℚ) (n : ℕ) →
  AtanhContractionInput ratio → 0 ≤ T →
  MagnitudeBound (atanhTerm ratio n) T →
  MagnitudeBound (atanhTerm ratio (suc n)) T
atanh-term-step-nonincreasing ratio T n contraction 0≤T termBound =
  let square≤one = isTrans≤
        (ratio Q.· ratio) ratio 1
        (atanh-contraction-square≤ratio ratio contraction)
        (atanh-contraction-ratio≤one ratio contraction)
      groupedScale = AtanhTermBoundPaths.group-square-scale
        PreferredℚCommRing T ratio
      scale≤T = subst (_≤ T) (sym groupedScale)
        (subst (T Q.· (ratio Q.· ratio) ≤_)
          (Q.·IdR T)
          (left-multiply-monotone T (ratio Q.· ratio) 1
            0≤T square≤one))
  in weaken-magnitude-bound _ _ T scale≤T
    (atanh-term-step-square-bound
      ratio T n contraction 0≤T termBound)

atanh-term-later-nonincreasing :
  (ratio T : Q.ℚ) (start count : ℕ) →
  AtanhContractionInput ratio → 0 ≤ T →
  MagnitudeBound (atanhTerm ratio start) T →
  MagnitudeBound (atanhTerm ratio (start ℕ.+ count)) T
atanh-term-later-nonincreasing ratio T start zero contraction 0≤T initial =
  transport-magnitude _ _ T
    (cong (atanhTerm ratio) (ℕ.+-zero start)) initial
atanh-term-later-nonincreasing ratio T start (suc count)
  contraction 0≤T initial =
  transport-magnitude _ _ T
    (cong (atanhTerm ratio) (ℕ.+-suc start count))
    (atanh-term-step-nonincreasing ratio T (start ℕ.+ count)
      contraction 0≤T
      (atanh-term-later-nonincreasing
        ratio T start count contraction 0≤T initial))
