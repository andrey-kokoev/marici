{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module DyadicallyBoundedCauchy where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Int as ℤ using (pos)
open import Cubical.Data.NatPlusOne.Base using (fromNatℕ₊₁)
import Cubical.Data.Int.Order
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
import CauchyNegation

-- A computable magnitude scale for the multiplication lane.
dyadicRadius : ℕ → Q.ℚ
dyadicRadius zero = 1
dyadicRadius (suc n) = dyadicRadius n Q.+ dyadicRadius n

natℚ : ℕ → Q.ℚ
natℚ zero = 0
natℚ (suc n) = natℚ n Q.+ 1

rational-successor-representative : (n : ℕ) →
  Q.[ pos n / 1 ] Q.+ 1 ≡ Q.[ pos (suc n) / 1 ]
rational-successor-representative n =
  Q.eq/ _ _
    (cong (ℤ._· 1)
       (cong₂ ℤ._+_ (ℤ.·IdR (pos n)) (ℤ.·IdR (pos 1))) ∙
     ℤ.·IdR (pos n ℤ.+ pos 1) ∙
     sym (ℤ.·IdR (pos (suc n))))

natℚ-representative : (n : ℕ) →
  natℚ n ≡ Q.[ pos n / 1 ]
natℚ-representative zero = refl
natℚ-representative (suc n) =
  cong (Q._+ 1) (natℚ-representative n) ∙
  rational-successor-representative n

natℚ-add : (m n : ℕ) →
  natℚ (m ℕ.+ n) ≡ natℚ m Q.+ natℚ n
natℚ-add m zero =
  cong natℚ (ℕ.+-zero m) ∙ sym (Q.+IdR (natℚ m))
natℚ-add m (suc n) =
  cong natℚ (ℕ.+-suc m n) ∙
  cong (λ z → z Q.+ 1) (natℚ-add m n) ∙
  sym (Q.+Assoc (natℚ m) (natℚ n) 1)

dyadicNat : ℕ → ℕ
dyadicNat zero = 1
dyadicNat (suc n) = dyadicNat n ℕ.+ dyadicNat n

natℚ-dyadicNat : (n : ℕ) →
  natℚ (dyadicNat n) ≡ dyadicRadius n
natℚ-dyadicNat zero = Q.+IdL 1
natℚ-dyadicNat (suc n) =
  natℚ-add (dyadicNat n) (dyadicNat n) ∙
  cong₂ Q._+_ (natℚ-dyadicNat n) (natℚ-dyadicNat n)

dyadicNat-at-least-one : (n : ℕ) → ℕOrder._≤_ 1 (dyadicNat n)
dyadicNat-at-least-one zero = ℕOrder.≤-refl
dyadicNat-at-least-one (suc n) =
  ℕOrder.≤-trans (dyadicNat-at-least-one n) ℕOrder.≤SumLeft

dyadicRadius-nonnegative : (n : ℕ) → 0 ≤ dyadicRadius n
dyadicRadius-nonnegative zero =
  Cubical.Data.Int.Order.zero-≤pos
dyadicRadius-nonnegative (suc n) =
  ≤Monotone+ 0 (dyadicRadius n) 0 (dyadicRadius n)
    (dyadicRadius-nonnegative n) (dyadicRadius-nonnegative n)

dyadicRadius-at-least-one : (n : ℕ) → 1 ≤ dyadicRadius n
dyadicRadius-at-least-one zero = isRefl≤ 1
dyadicRadius-at-least-one (suc n) =
  isTrans≤ 1 (dyadicRadius n)
    (dyadicRadius n Q.+ dyadicRadius n)
    (dyadicRadius-at-least-one n)
    (≤-add-nonnegative (dyadicRadius n) (dyadicRadius n)
      (dyadicRadius-nonnegative n))

natℚ≤dyadicRadius : (n : ℕ) → natℚ n ≤ dyadicRadius n
natℚ≤dyadicRadius zero = dyadicRadius-nonnegative 0
natℚ≤dyadicRadius (suc n) =
  ≤Monotone+ (natℚ n) (dyadicRadius n) 1 (dyadicRadius n)
    (natℚ≤dyadicRadius n) (dyadicRadius-at-least-one n)

module ScalePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  double-half : (r p h : fst R) →
    (r +S r) ·S (p ·S h) ≡ (r ·S p) ·S (h +S h)
  double-half r p h = solve! R

  double-product : (a b : fst R) →
    (a ·S b) +S (a ·S b) ≡ (a +S a) ·S b
  double-product a b = solve! R

  reassociate-half : (a b h : fst R) →
    (a ·S b) ·S h ≡ (a ·S h) ·S b
  reassociate-half a b h = solve! R

  reassociate-scale : (r p q : fst R) →
    r ·S (p ·S q) ≡ (r ·S p) ·S q
  reassociate-scale r p q = solve! R

dyadicRadius-add : (m n : ℕ) →
  dyadicRadius (m ℕ.+ n) ≡ dyadicRadius m Q.· dyadicRadius n
dyadicRadius-add zero n = sym (Q.·IdL (dyadicRadius n))
dyadicRadius-add (suc m) n =
  cong₂ Q._+_ (dyadicRadius-add m n) (dyadicRadius-add m n) ∙
  ScalePaths.double-product PreferredℚCommRing
    (dyadicRadius m) (dyadicRadius n)

left-radius≤combined-radius : (m n : ℕ) →
  dyadicRadius m ≤ dyadicRadius (m ℕ.+ n)
left-radius≤combined-radius m n =
  subst2 _≤_
    (Q.·IdL (dyadicRadius m))
    (Q.·Comm (dyadicRadius n) (dyadicRadius m) ∙
     sym (dyadicRadius-add m n))
    (≤-·o 1 (dyadicRadius n) (dyadicRadius m)
      (dyadicRadius-nonnegative m) (dyadicRadius-at-least-one n))

right-radius≤combined-radius : (m n : ℕ) →
  dyadicRadius n ≤ dyadicRadius (m ℕ.+ n)
right-radius≤combined-radius m n =
  subst2 _≤_
    (Q.·IdL (dyadicRadius n))
    (sym (dyadicRadius-add m n))
    (≤-·o 1 (dyadicRadius m) (dyadicRadius n)
      (dyadicRadius-nonnegative n) (dyadicRadius-at-least-one m))

radius-sum≤successor-combined : (m n : ℕ) →
  dyadicRadius m Q.+ dyadicRadius n ≤
  dyadicRadius (suc (m ℕ.+ n))
radius-sum≤successor-combined m n =
  ≤Monotone+
    (dyadicRadius m) (dyadicRadius (m ℕ.+ n))
    (dyadicRadius n) (dyadicRadius (m ℕ.+ n))
    (left-radius≤combined-radius m n)
    (right-radius≤combined-radius m n)

dyadicRadius-monotone : (m n : ℕ) → ℕOrder._≤_ m n →
  dyadicRadius m ≤ dyadicRadius n
dyadicRadius-monotone m n (k , k+m≡n) =
  subst (dyadicRadius m ≤_)
    (cong dyadicRadius (ℕ.+-comm m k ∙ k+m≡n))
    (left-radius≤combined-radius m k)

negative-radius-antitone : (m n : ℕ) → ℕOrder._≤_ m n →
  Q.- dyadicRadius n ≤ Q.- dyadicRadius m
negative-radius-antitone m n m≤n =
  subst (Q.- dyadicRadius n ≤_)
    (Q.+IdR (Q.- dyadicRadius m))
    (CauchyNegation.negate-one-error-bound
      (dyadicRadius m) (dyadicRadius n) 0
      (subst (dyadicRadius m ≤_)
        (sym (Q.+IdR (dyadicRadius n)))
        (dyadicRadius-monotone m n m≤n)))

precision-add : (m n : ℕ) →
  precision (m ℕ.+ n) ≡ precision m Q.· precision n
precision-add zero n = sym (Q.·IdL (precision n))
precision-add (suc m) n =
  cong (Q._· one-half) (precision-add m n) ∙
  ScalePaths.reassociate-half PreferredℚCommRing
    (precision m) (precision n) one-half

dyadicRadius-times-precision : (n : ℕ) →
  dyadicRadius n Q.· precision n ≡ 1
dyadicRadius-times-precision zero = Q.·IdR 1
dyadicRadius-times-precision (suc n) =
  ScalePaths.double-half PreferredℚCommRing
    (dyadicRadius n) (precision n) one-half ∙
  cong ((dyadicRadius n Q.· precision n) Q.·_) one-half-double ∙
  Q.·IdR (dyadicRadius n Q.· precision n) ∙
  dyadicRadius-times-precision n

radius-cancels-precision-shift : (d n : ℕ) →
  dyadicRadius d Q.· precision (d ℕ.+ n) ≡ precision n
radius-cancels-precision-shift d n =
  cong (dyadicRadius d Q.·_) (precision-add d n) ∙
  ScalePaths.reassociate-scale PreferredℚCommRing
    (dyadicRadius d) (precision d) (precision n) ∙
  cong (Q._· precision n) (dyadicRadius-times-precision d) ∙
  Q.·IdL (precision n)

module SignPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  left : (r : fst R) → 0r +S (-S r) ≡ -S r
  left r = solve! R

  right : (r : fst R) → r +S (-S r) ≡ 0r
  right r = solve! R

negative-nonpositive : (r : Q.ℚ) → 0 ≤ r → Q.- r ≤ 0
negative-nonpositive r 0≤r =
  subst2 _≤_
    (SignPaths.left PreferredℚCommRing r)
    (SignPaths.right PreferredℚCommRing r)
    (≤-+o 0 r (Q.- r) 0≤r)

record DyadicallyBoundedRegularCauchy : Type where
  field
    regular : RegularCauchy
    radius-exponent : ℕ
    lower-bound : (n : ℕ) →
      Q.- dyadicRadius radius-exponent ≤ approximation regular n
    upper-bound : (n : ℕ) →
      approximation regular n ≤ dyadicRadius radius-exponent
open DyadicallyBoundedRegularCauchy public

widenDyadicBound : (x : DyadicallyBoundedRegularCauchy) (d : ℕ) →
  ℕOrder._≤_ (radius-exponent x) d →
  DyadicallyBoundedRegularCauchy
widenDyadicBound x d exponent≤ .regular = regular x
widenDyadicBound x d exponent≤ .radius-exponent = d
widenDyadicBound x d exponent≤ .lower-bound n =
  isTrans≤
    (Q.- dyadicRadius d)
    (Q.- dyadicRadius (radius-exponent x))
    (approximation (regular x) n)
    (negative-radius-antitone (radius-exponent x) d exponent≤)
    (lower-bound x n)
widenDyadicBound x d exponent≤ .upper-bound n =
  isTrans≤
    (approximation (regular x) n)
    (dyadicRadius (radius-exponent x))
    (dyadicRadius d)
    (upper-bound x n)
    (dyadicRadius-monotone (radius-exponent x) d exponent≤)

rationalApproximationDyadicallyBounded :
  DyadicallyBoundedRegularCauchy → ℕ → DyadicallyBoundedRegularCauchy
rationalApproximationDyadicallyBounded x N .regular =
  constantCauchy (approximation (regular x) N)
rationalApproximationDyadicallyBounded x N .radius-exponent =
  radius-exponent x
rationalApproximationDyadicallyBounded x N .lower-bound n =
  lower-bound x N
rationalApproximationDyadicallyBounded x N .upper-bound n =
  upper-bound x N

rationalApproximationDyadicallyBounded-regular :
  (x : DyadicallyBoundedRegularCauchy) (N : ℕ) →
  regular (rationalApproximationDyadicallyBounded x N) ≡
  constantCauchy (approximation (regular x) N)
rationalApproximationDyadicallyBounded-regular x N = refl

rationalApproximationDyadicallyBounded-preserves-exponent :
  (x : DyadicallyBoundedRegularCauchy) (N : ℕ) →
  radius-exponent (rationalApproximationDyadicallyBounded x N) ≡
  radius-exponent x
rationalApproximationDyadicallyBounded-preserves-exponent x N = refl

boundedZero : DyadicallyBoundedRegularCauchy
boundedZero .regular = constantCauchy 0
boundedZero .radius-exponent = 0
boundedZero .lower-bound n =
  negative-nonpositive 1 dyadicRadius-nonnegative-zero
  where
  dyadicRadius-nonnegative-zero : 0 ≤ dyadicRadius 0
  dyadicRadius-nonnegative-zero = dyadicRadius-nonnegative 0
boundedZero .upper-bound n = dyadicRadius-nonnegative 0

boundedOne : DyadicallyBoundedRegularCauchy
boundedOne .regular = constantCauchy 1
boundedOne .radius-exponent = 0
boundedOne .lower-bound n =
  isTrans≤ (Q.- 1) 0 1
    (negative-nonpositive 1 (dyadicRadius-nonnegative 0))
    (dyadicRadius-nonnegative 0)
boundedOne .upper-bound n = isRefl≤ 1

-- A rational point can enter the bounded multiplication lane only with an
-- explicit symmetric dyadic bound; no global Archimedean extraction is hidden.
boundedConstant : (q : Q.ℚ) (d : ℕ) →
  Q.- dyadicRadius d ≤ q → q ≤ dyadicRadius d →
  DyadicallyBoundedRegularCauchy
boundedConstant q d lower upper .regular = constantCauchy q
boundedConstant q d lower upper .radius-exponent = d
boundedConstant q d lower upper .lower-bound n = lower
boundedConstant q d lower upper .upper-bound n = upper
