{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalLogConvergenceContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Nat.Properties as ℕProperties
open import Cubical.Data.NatPlusOne as ℕ₊₁ using (1+_)
open import Cubical.Data.NatPlusOne.Properties as ℕ₊₁Properties using (_·₊₁_; ℕ₊₁→ℕ-inj)
open import Cubical.Data.Int as ℤ using (pos)
open import Cubical.Data.Int.Properties as ℤProperties
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import RationalLogTaylorApproximants

natural-times-two : (n : ℕ) → n ℕ.· 2 ≡ n ℕ.+ n
natural-times-two n =
  ℕ.·-suc n 1 ∙ cong (n ℕ.+_) (ℕProperties.·-identityʳ n)

dyadicReciprocalIndex : ℕ → ℕ
dyadicReciprocalIndex zero = zero
dyadicReciprocalIndex (suc n) = suc (dyadicReciprocalIndex n ℕ.+ dyadicReciprocalIndex n)

dyadic-reciprocal-index-step≤ : (n : ℕ) →
  ℕOrder._≤_ (dyadicReciprocalIndex n) (dyadicReciprocalIndex (suc n))
dyadic-reciprocal-index-step≤ n =
  ℕOrder.≤-trans ℕOrder.≤SumLeft ℕOrder.≤-sucℕ

dyadic-reciprocal-index-advance≤ : (m extra : ℕ) →
  ℕOrder._≤_ (dyadicReciprocalIndex m)
    (dyadicReciprocalIndex (extra ℕ.+ m))
dyadic-reciprocal-index-advance≤ m zero = ℕOrder.≤-refl
dyadic-reciprocal-index-advance≤ m (suc extra) =
  ℕOrder.≤-trans
    (dyadic-reciprocal-index-advance≤ m extra)
    (dyadic-reciprocal-index-step≤ (extra ℕ.+ m))

dyadic-reciprocal-index-monotone : (m n : ℕ) →
  ℕOrder._≤_ m n →
  ℕOrder._≤_ (dyadicReciprocalIndex m) (dyadicReciprocalIndex n)
dyadic-reciprocal-index-monotone m n (extra , path) =
  subst (ℕOrder._≤_ (dyadicReciprocalIndex m))
    (cong dyadicReciprocalIndex path)
    (dyadic-reciprocal-index-advance≤ m extra)

dyadic-reciprocal-denominator-step : (n : ℕ) →
  suc (dyadicReciprocalIndex (suc n)) ≡
  suc (dyadicReciprocalIndex n) ℕ.+ suc (dyadicReciprocalIndex n)
dyadic-reciprocal-denominator-step n =
  sym
    (ℕ.+-suc (suc index) index ∙
     cong suc (ℕ.+-comm (suc index) index ∙ ℕ.+-suc index index))
  where index = dyadicReciprocalIndex n

dyadic-reciprocal-index-denominator : (n : ℕ) →
  suc (dyadicReciprocalIndex n) ≡ dyadicNat n
dyadic-reciprocal-index-denominator zero = refl
dyadic-reciprocal-index-denominator (suc n) =
  dyadic-reciprocal-denominator-step n ∙
  cong₂ ℕ._+_
    (dyadic-reciprocal-index-denominator n)
    (dyadic-reciprocal-index-denominator n)

half-dyadic-reciprocal-step : (n : ℕ) →
  halfℚ (reciprocalSuccessor (dyadicReciprocalIndex n)) ≡
  reciprocalSuccessor (dyadicReciprocalIndex (suc n))
half-dyadic-reciprocal-step n =
  cong (Q.[ pos 1 /_]) denominatorPath
  where
  index = dyadicReciprocalIndex n
  denominatorPath : (1+ index) ·₊₁ (1+ 1) ≡ 1+ suc (index ℕ.+ index)
  denominatorPath = ℕ₊₁→ℕ-inj (cong suc (cong suc (natural-times-two index)))

precision-as-dyadic-reciprocal : (n : ℕ) →
  precision n ≡ reciprocalSuccessor (dyadicReciprocalIndex n)
precision-as-dyadic-reciprocal zero = refl
precision-as-dyadic-reciprocal (suc n) =
  cong halfℚ (precision-as-dyadic-reciprocal n) ∙
  half-dyadic-reciprocal-step n

natural-index≤dyadic-index : (n : ℕ) →
  ℕOrder._≤_ n (dyadicNat n)
natural-index≤dyadic-index zero = ℕOrder.zero-≤
natural-index≤dyadic-index (suc n) =
  ℕOrder.≤-trans
    (ℕOrder.suc-≤-suc (natural-index≤dyadic-index n))
    (ℕOrder.≤-+-≤ (dyadicNat-at-least-one n) ℕOrder.≤-refl)

log-denominator≤candidate-dyadic : (n : ℕ) →
  ℕOrder._≤_ (suc (suc n)) (dyadicNat (suc (suc n)))
log-denominator≤candidate-dyadic n =
  natural-index≤dyadic-index (suc (suc n))

precision-below-log-reciprocal : (n : ℕ) →
  precision (suc (suc n)) ≤ reciprocalSuccessor (suc n)
precision-below-log-reciprocal n =
  subst (_≤ reciprocalSuccessor (suc n))
    (sym (precision-as-dyadic-reciprocal (suc (suc n))))
    (reciprocalSuccessor-antitone (suc n)
      (dyadicReciprocalIndex (suc (suc n)))
      (ℕOrder.pred-≤-pred
        (subst (suc (suc n) ℕOrder.≤_)
          (sym (dyadic-reciprocal-index-denominator (suc (suc n))))
          (log-denominator≤candidate-dyadic n))))

module IntegerRatioNormalization where
  open import Cubical.Algebra.CommRing.Instances.Int
  open CommRingStr (snd ℤCommRing)
    renaming (_·_ to _·I_; _+_ to _+I_)

  cross-normalization : (a d : ℤ.ℤ) →
    ((a ·I d) +I (1 ·I d)) ·I d ≡ (a +I 1) ·I (d ·I d)
  cross-normalization a d = solve! ℤCommRing

positive-log-ratio-plus-reciprocal-normalizes : (n : ℕ) →
  positiveNaturalLogRatio n Q.+ reciprocalSuccessor (suc n) ≡
  Q.[ pos (suc n) / 1+ suc n ]
positive-log-ratio-plus-reciprocal-normalizes n =
  Q.eq/ _ _
    (IntegerRatioNormalization.cross-normalization
      (pos n) denominator ∙
     cong (λ z → pos (suc n) ℤ.· z)
       (sym (ℤProperties.pos·pos (suc (suc n)) (suc (suc n)))))
  where denominator = pos (suc (suc n))

successor-over-double-successor≤one : (n : ℕ) →
  Q.[ pos (suc n) / 1+ suc n ] ≤ 1
successor-over-double-successor≤one n =
  subst2 ℤOrder._≤_
    (sym (ℤ.·IdR (pos (suc n))))
    (sym (ℤ.·IdL (pos (suc (suc n)))))
    (nat≤→positive-integer≤ (suc n) (suc (suc n)) (1 , refl))

positive-log-ratio-plus-reciprocal≤one : (n : ℕ) →
  positiveNaturalLogRatio n Q.+ reciprocalSuccessor (suc n) ≤ 1
positive-log-ratio-plus-reciprocal≤one n =
  subst (_≤ 1)
    (sym (positive-log-ratio-plus-reciprocal-normalizes n))
    (successor-over-double-successor≤one n)

ratio-plus-reciprocal-bound-gives-reciprocal-below-gap : (n : ℕ) →
  positiveNaturalLogRatio n Q.+ reciprocalSuccessor (suc n) ≤ 1 →
  reciprocalSuccessor (suc n) ≤ positiveNaturalLogRatioGapCandidate n
ratio-plus-reciprocal-bound-gives-reciprocal-below-gap n ratioAndReciprocal≤one =
  ≤-o+-cancel
    (reciprocalSuccessor (suc n))
    (positiveNaturalLogRatioGapCandidate n)
    (positiveNaturalLogRatio n)
    (subst
      ((positiveNaturalLogRatio n Q.+ reciprocalSuccessor (suc n)) ≤_)
      (sym (positive-natural-log-ratio-plus-gap n))
      ratioAndReciprocal≤one)

record PositiveNaturalLogReciprocalBridge : Type where
  field
    precisionBelowReciprocal : (n : ℕ) →
      precision (suc (suc n)) ≤ reciprocalSuccessor (suc n)
    reciprocalBelowGap : (n : ℕ) →
      reciprocalSuccessor (suc n) ≤ positiveNaturalLogRatioGapCandidate n
open PositiveNaturalLogReciprocalBridge public

record PositiveNaturalLogArithmeticBridge : Type where
  field
    precisionBelowReciprocalArithmetic : (n : ℕ) →
      precision (suc (suc n)) ≤ reciprocalSuccessor (suc n)
    ratioPlusReciprocal≤one : (n : ℕ) →
      positiveNaturalLogRatio n Q.+ reciprocalSuccessor (suc n) ≤ 1
open PositiveNaturalLogArithmeticBridge public

record PositiveNaturalLogRatioArithmetic : Type where
  field
    ratioPlusReciprocalBound : (n : ℕ) →
      positiveNaturalLogRatio n Q.+ reciprocalSuccessor (suc n) ≤ 1
open PositiveNaturalLogRatioArithmetic public

canonicalPositiveNaturalLogRatioArithmetic : PositiveNaturalLogRatioArithmetic
canonicalPositiveNaturalLogRatioArithmetic .ratioPlusReciprocalBound =
  positive-log-ratio-plus-reciprocal≤one

ratio-arithmetic-gives-arithmetic-bridge :
  PositiveNaturalLogRatioArithmetic → PositiveNaturalLogArithmeticBridge
ratio-arithmetic-gives-arithmetic-bridge ratioArithmetic
  .precisionBelowReciprocalArithmetic = precision-below-log-reciprocal
ratio-arithmetic-gives-arithmetic-bridge ratioArithmetic
  .ratioPlusReciprocal≤one = ratioPlusReciprocalBound ratioArithmetic

canonicalPositiveNaturalLogArithmeticBridge : PositiveNaturalLogArithmeticBridge
canonicalPositiveNaturalLogArithmeticBridge =
  ratio-arithmetic-gives-arithmetic-bridge
    canonicalPositiveNaturalLogRatioArithmetic

arithmetic-bridge-gives-reciprocal-bridge :
  PositiveNaturalLogArithmeticBridge → PositiveNaturalLogReciprocalBridge
arithmetic-bridge-gives-reciprocal-bridge arithmetic .precisionBelowReciprocal =
  precisionBelowReciprocalArithmetic arithmetic
arithmetic-bridge-gives-reciprocal-bridge arithmetic .reciprocalBelowGap n =
  ratio-plus-reciprocal-bound-gives-reciprocal-below-gap n
    (ratioPlusReciprocal≤one arithmetic n)

record PositiveNaturalLogGapCertificate (n : ℕ) : Type where
  field
    gapExponent : ℕ
    precisionFitsGap :
      precision gapExponent ≤ positiveNaturalLogRatioGapCandidate n
open PositiveNaturalLogGapCertificate public

reciprocal-bridge-gives-gap-certificate :
  PositiveNaturalLogReciprocalBridge →
  (n : ℕ) → PositiveNaturalLogGapCertificate n
reciprocal-bridge-gives-gap-certificate bridge n .gapExponent = suc (suc n)
reciprocal-bridge-gives-gap-certificate bridge n .precisionFitsGap =
  isTrans≤
    (precision (suc (suc n)))
    (reciprocalSuccessor (suc n))
    (positiveNaturalLogRatioGapCandidate n)
    (precisionBelowReciprocal bridge n) (reciprocalBelowGap bridge n)

canonicalPositiveNaturalLogReciprocalBridge : PositiveNaturalLogReciprocalBridge
canonicalPositiveNaturalLogReciprocalBridge =
  arithmetic-bridge-gives-reciprocal-bridge
    canonicalPositiveNaturalLogArithmeticBridge

module LogGapPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  one-minus-zero : 1r +S (-S 0r) ≡ 1r
  one-minus-zero = solve! R

positive-natural-log-gap-at-one :
  positiveNaturalLogRatioGapCandidate ℕ.zero ≡ 1
positive-natural-log-gap-at-one =
  cong (λ ratio → 1 Q.+ (Q.- ratio))
    positive-natural-log-ratio-at-one ∙
  LogGapPaths.one-minus-zero PreferredℚCommRing

positive-natural-log-gap-certificate-at-one :
  PositiveNaturalLogGapCertificate ℕ.zero
positive-natural-log-gap-certificate-at-one .gapExponent = ℕ.zero
positive-natural-log-gap-certificate-at-one .precisionFitsGap =
  subst (1 ≤_) (sym positive-natural-log-gap-at-one) (isRefl≤ 1)

log-gap-certificate-gives-separated-upper-bound :
  (n : ℕ) → (certificate : PositiveNaturalLogGapCertificate n) →
  positiveNaturalLogRatio n Q.+ precision (gapExponent certificate) ≤ 1
log-gap-certificate-gives-separated-upper-bound n certificate =
  subst
    ((positiveNaturalLogRatio n Q.+ precision (gapExponent certificate)) ≤_)
    (positive-natural-log-ratio-plus-gap n)
    (≤Monotone+
      (positiveNaturalLogRatio n) (positiveNaturalLogRatio n)
      (precision (gapExponent certificate))
      (positiveNaturalLogRatioGapCandidate n)
      (isRefl≤ (positiveNaturalLogRatio n))
      (precisionFitsGap certificate))

positive-natural-log-separated-upper-bound-at-one :
  positiveNaturalLogRatio ℕ.zero Q.+ precision ℕ.zero ≤ 1
positive-natural-log-separated-upper-bound-at-one =
  log-gap-certificate-gives-separated-upper-bound ℕ.zero
    positive-natural-log-gap-certificate-at-one

record AtanhContractionInput (ratio : Q.ℚ) : Type where
  field
    contractionExponent : ℕ
    ratioNonnegative : 0 ≤ ratio
    ratioSeparatedFromOne :
      ratio Q.+ precision contractionExponent ≤ 1
open AtanhContractionInput public

atanh-contraction-ratio≤one :
  (ratio : Q.ℚ) → AtanhContractionInput ratio → ratio ≤ 1
atanh-contraction-ratio≤one ratio contraction =
  isTrans≤ ratio
    (ratio Q.+ precision (contractionExponent contraction)) 1
    (≤-add-nonnegative ratio (precision (contractionExponent contraction))
      (precision-nonnegative (contractionExponent contraction)))
    (ratioSeparatedFromOne contraction)

atanh-contraction-square≤ratio :
  (ratio : Q.ℚ) → (contraction : AtanhContractionInput ratio) →
  ratio Q.· ratio ≤ ratio
atanh-contraction-square≤ratio ratio contraction =
  subst (ratio Q.· ratio ≤_) (Q.·IdL ratio)
    (≤-·o ratio 1 ratio
      (ratioNonnegative contraction)
      (atanh-contraction-ratio≤one ratio contraction))

atanh-contraction-square-separated :
  (ratio : Q.ℚ) → (contraction : AtanhContractionInput ratio) →
  (ratio Q.· ratio) Q.+ precision (contractionExponent contraction) ≤ 1
atanh-contraction-square-separated ratio contraction =
  isTrans≤
    ((ratio Q.· ratio) Q.+ precision (contractionExponent contraction))
    (ratio Q.+ precision (contractionExponent contraction)) 1
    (≤Monotone+
      (ratio Q.· ratio) ratio
      (precision (contractionExponent contraction))
      (precision (contractionExponent contraction))
      (atanh-contraction-square≤ratio ratio contraction)
      (isRefl≤ (precision (contractionExponent contraction))))
    (ratioSeparatedFromOne contraction)

positive-natural-log-atanh-contraction :
  (n : ℕ) → PositiveNaturalLogGapCertificate n →
  AtanhContractionInput (positiveNaturalLogRatio n)
positive-natural-log-atanh-contraction n gap .contractionExponent =
  gapExponent gap
positive-natural-log-atanh-contraction n gap .ratioNonnegative =
  positive-natural-log-ratio-nonnegative n
positive-natural-log-atanh-contraction n gap .ratioSeparatedFromOne =
  log-gap-certificate-gives-separated-upper-bound n gap

record PositiveNaturalLogConvergenceInput (n : ℕ) : Type where
  field
    gapCertificate : PositiveNaturalLogGapCertificate n
    ratioNonnegative : 0 ≤ positiveNaturalLogRatio n
open PositiveNaturalLogConvergenceInput public

canonical-log-ratio-nonnegative : (n : ℕ) →
  0 ≤ positiveNaturalLogRatio n
canonical-log-ratio-nonnegative = positive-natural-log-ratio-nonnegative

log-gap-is-bounded : (n : ℕ) →
  0 ≤ positiveNaturalLogRatioGapCandidate n
log-gap-is-bounded = positive-natural-log-ratio-gap-nonnegative
