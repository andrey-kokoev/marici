{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module AtanhPowerDecayContract where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Nat.Properties as ℕProperties
import Cubical.Data.Nat.Order as ℕOrder
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import TaylorTermBounds
open import DyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import RationalLogTaylorApproximants
open import RationalLogConvergenceContract
open import AtanhTermBounds

record AtanhPowerDecay
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) : Type where
  field
    decayCutoff : ℕ → ℕ
    decayCutoffMonotone : (m n : ℕ) → ℕOrder._≤_ m n →
      ℕOrder._≤_ (decayCutoff m) (decayCutoff n)
    decayCutoffCofinal : (termIndex : ℕ) →
      Σ[ stage ∈ ℕ ] ℕOrder._≤_ termIndex (decayCutoff stage)
    powerDecay : (stage : ℕ) →
      atanhRationalPower (ratio Q.· ratio) (decayCutoff stage) ≤
      precision stage
open AtanhPowerDecay public

separated-ratio-times-one-plus-gap≤one :
  (ratio gap : Q.ℚ) → 0 ≤ ratio → 0 ≤ gap →
  ratio Q.+ gap ≤ 1 → ratio Q.· (1 Q.+ gap) ≤ 1
separated-ratio-times-one-plus-gap≤one ratio gap 0≤ratio 0≤gap separated =
  let ratio≤one = isTrans≤ ratio (ratio Q.+ gap) 1
        (≤-add-nonnegative ratio gap 0≤gap) separated
      scaledGap≤gapRaw = left-multiply-monotone gap ratio 1 0≤gap ratio≤one
      scaledGap≤gap = subst2 _≤_
        (Q.·Comm gap ratio) (Q.·IdR gap) scaledGap≤gapRaw
      sumBound = isTrans≤
        (ratio Q.+ ratio Q.· gap) (ratio Q.+ gap) 1
        (≤-o+ (ratio Q.· gap) gap ratio scaledGap≤gap) separated
  in subst (_≤ 1)
    (sym (Q.·DistL+ ratio 1 gap ∙
      cong₂ Q._+_ (Q.·IdR ratio) refl)) sumBound

separated-ratio-power-product≤one :
  (ratio gap : Q.ℚ) → 0 ≤ ratio → 0 ≤ gap →
  ratio Q.+ gap ≤ 1 → (block : ℕ) →
  atanhRationalPower ratio block Q.·
    atanhRationalPower (1 Q.+ gap) block ≤ 1
separated-ratio-power-product≤one ratio gap 0≤ratio 0≤gap separated block =
  let 0≤onePlusGap = isTrans≤ 0 1 (1 Q.+ gap)
        ℤOrder.zero-≤pos
        (≤-add-nonnegative 1 gap 0≤gap)
      product≤one = separated-ratio-times-one-plus-gap≤one
        ratio gap 0≤ratio 0≤gap separated
      productPower≤one = rational-power-below-one
        (ratio Q.· (1 Q.+ gap))
        (nonnegative-bound-product ratio (1 Q.+ gap)
          0≤ratio 0≤onePlusGap)
        product≤one block
  in subst (_≤ 1)
    (atanh-rational-power-product ratio (1 Q.+ gap) block)
    productPower≤one

module DyadicGrowthPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  half-square-growth : (h : fst R) →
    (1r +S (h +S h)) +S (h ·S h) ≡
    (1r +S h) ·S (1r +S h)
  half-square-growth h = solve! R

one-plus-half-square-growth : (p : Q.ℚ) → 0 ≤ p →
  1 Q.+ p ≤ (1 Q.+ halfℚ p) Q.· (1 Q.+ halfℚ p)
one-plus-half-square-growth p 0≤p =
  let h = halfℚ p
      0≤h = half-nonnegative p 0≤p
      0≤h² = nonnegative-bound-product h h 0≤h 0≤h
      withSquare = ≤-add-nonnegative (1 Q.+ p) (h Q.· h) 0≤h²
      normalized : (1 Q.+ p) Q.+ (h Q.· h) ≡
        (1 Q.+ h) Q.· (1 Q.+ h)
      normalized =
        cong (λ z → (1 Q.+ z) Q.+ (h Q.· h)) (sym (half-double p)) ∙
        DyadicGrowthPaths.half-square-growth PreferredℚCommRing h
  in subst ((1 Q.+ p) ≤_) normalized withSquare

dyadic-one-plus-precision-power≥two : (n : ℕ) →
  2 ≤ atanhRationalPower (1 Q.+ precision n) (dyadicNat n)
dyadic-one-plus-precision-power≥two zero =
  subst (2 ≤_)
    (sym (Q.·IdL (1 Q.+ 1)))
    (isRefl≤ 2)
dyadic-one-plus-precision-power≥two (suc n) =
  let base = 1 Q.+ precision n
      nextBase = 1 Q.+ precision (suc n)
      0≤nextBase = isTrans≤ 0 1 nextBase ℤOrder.zero-≤pos
        (≤-add-nonnegative 1 (precision (suc n))
          (precision-nonnegative (suc n)))
      base≤nextSquare = subst
        ((1 Q.+ precision n) ≤_)
        refl
        (one-plus-half-square-growth (precision n)
          (precision-nonnegative n))
      powered = atanh-rational-power-monotone
        base (nextBase Q.· nextBase)
        (isTrans≤ 0 1 base ℤOrder.zero-≤pos
          (≤-add-nonnegative 1 (precision n) (precision-nonnegative n)))
        (nonnegative-bound-product nextBase nextBase 0≤nextBase 0≤nextBase)
        base≤nextSquare (dyadicNat n)
      regroup :
        atanhRationalPower (nextBase Q.· nextBase) (dyadicNat n) ≡
        atanhRationalPower nextBase (dyadicNat (suc n))
      regroup = atanh-rational-power-product nextBase nextBase (dyadicNat n) ∙
        sym (atanh-rational-power-add nextBase (dyadicNat n) (dyadicNat n))
  in isTrans≤ 2
    (atanhRationalPower base (dyadicNat n))
    (atanhRationalPower nextBase (dyadicNat (suc n)))
    (dyadic-one-plus-precision-power≥two n)
    (subst (atanhRationalPower base (dyadicNat n) ≤_) regroup powered)

module HalfCancellationPaths where
  open CommRingStr (snd PreferredℚCommRing)
    renaming (_·_ to _·S_; _+_ to _+S_)

  cancel-two-and-half : (x : Q.ℚ) →
    (x ·S (1r +S 1r)) ·S halfℚ 1 ≡ x
  cancel-two-and-half x =
    sym (Q.·Assoc x (1 Q.+ 1) (halfℚ 1)) ∙
    cong (x Q.·_)
      (Q.·DistR+ 1 1 (halfℚ 1) ∙
       cong₂ Q._+_ (Q.·IdL (halfℚ 1)) (Q.·IdL (halfℚ 1)) ∙
       half-double 1) ∙
    Q.·IdR x

  one-times-half : 1r ·S halfℚ 1 ≡ halfℚ 1
  one-times-half = Q.·IdL (halfℚ 1)

product-with-factor≥two-gives-half : (x factor : Q.ℚ) →
  0 ≤ x → 2 ≤ factor → x Q.· factor ≤ 1 → x ≤ one-half
product-with-factor≥two-gives-half x factor 0≤x 2≤factor product≤one =
  let twice≤product = left-multiply-monotone x 2 factor 0≤x 2≤factor
      twice≤one = isTrans≤ (x Q.· 2) (x Q.· factor) 1
        twice≤product product≤one
      halved = ≤-·o (x Q.· 2) 1 one-half
        one-half-nonnegative twice≤one
  in subst2 _≤_
    (HalfCancellationPaths.cancel-two-and-half x)
    (HalfCancellationPaths.one-times-half)
    halved

module DyadicGapPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  cancel-gap-left : (ratio gap : fst R) →
    (ratio +S gap) +S (-S gap) ≡ ratio
  cancel-gap-left ratio gap = solve! R

dyadic-gap-complement-upper :
  (ratio : Q.ℚ) (exponent : ℕ) →
  ratio Q.+ precision exponent ≤ 1 →
  ratio ≤ 1 Q.- precision exponent
dyadic-gap-complement-upper ratio exponent separated =
  subst2 _≤_
    (DyadicGapPaths.cancel-gap-left PreferredℚCommRing
      ratio (precision exponent))
    refl
    (≤-+o (ratio Q.+ precision exponent) 1
      (Q.- precision exponent) separated)

record DyadicGapHalfPowerPrinciple : Type where
  field
    halfPowerFromDyadicGap :
      (ratio : Q.ℚ) (exponent : ℕ) → 0 ≤ ratio →
      ratio Q.+ precision exponent ≤ 1 →
      Σ[ block ∈ ℕ ]
        Σ[ positive ∈ ℕOrder._≤_ 1 block ]
        atanhRationalPower (ratio Q.· ratio) block ≤ one-half
open DyadicGapHalfPowerPrinciple public

record AtanhHalfContractingBlock
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) : Type where
  field
    blockSize : ℕ
    blockPositive : ℕOrder._≤_ 1 blockSize
    blockContracts :
      atanhRationalPower (ratio Q.· ratio) blockSize ≤ one-half
open AtanhHalfContractingBlock public

record AtanhLinearHalfContractingBlock
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) : Type where
  field
    linearBlockSize : ℕ
    linearBlockPositive : ℕOrder._≤_ 1 linearBlockSize
    linearBlockContracts :
      atanhRationalPower ratio linearBlockSize ≤ one-half
open AtanhLinearHalfContractingBlock public

linear-half-block-gives-square-half-block :
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) →
  AtanhLinearHalfContractingBlock ratio contraction →
  AtanhHalfContractingBlock ratio contraction
linear-half-block-gives-square-half-block ratio contraction linear .blockSize =
  linearBlockSize linear
linear-half-block-gives-square-half-block ratio contraction linear .blockPositive =
  linearBlockPositive linear
linear-half-block-gives-square-half-block ratio contraction linear .blockContracts =
  isTrans≤
    (atanhRationalPower (ratio Q.· ratio) (linearBlockSize linear))
    (atanhRationalPower ratio (linearBlockSize linear)) one-half
    (square-power-below-power ratio
      (ratioNonnegative contraction)
      (atanh-contraction-ratio≤one ratio contraction)
      (linearBlockSize linear))
    (linearBlockContracts linear)

contraction-gives-linear-half-block :
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) →
  AtanhLinearHalfContractingBlock ratio contraction
contraction-gives-linear-half-block ratio contraction .linearBlockSize =
  dyadicNat (contractionExponent contraction)
contraction-gives-linear-half-block ratio contraction .linearBlockPositive =
  dyadicNat-at-least-one (contractionExponent contraction)
contraction-gives-linear-half-block ratio contraction .linearBlockContracts =
  let exponent = contractionExponent contraction
      gap = precision exponent
      powerNonnegative = atanh-rational-power-nonnegative ratio
        (ratioNonnegative contraction) (dyadicNat exponent)
      productBound = separated-ratio-power-product≤one ratio gap
        (ratioNonnegative contraction) (precision-nonnegative exponent)
        (ratioSeparatedFromOne contraction) (dyadicNat exponent)
  in product-with-factor≥two-gives-half
    (atanhRationalPower ratio (dyadicNat exponent))
    (atanhRationalPower (1 Q.+ gap) (dyadicNat exponent))
    powerNonnegative (dyadic-one-plus-precision-power≥two exponent)
    productBound

contraction-gives-half-block :
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) →
  AtanhHalfContractingBlock ratio contraction
contraction-gives-half-block ratio contraction =
  linear-half-block-gives-square-half-block ratio contraction
    (contraction-gives-linear-half-block ratio contraction)

zero-ratio-half-block :
  (contraction : AtanhContractionInput 0) →
  AtanhHalfContractingBlock 0 contraction
zero-ratio-half-block contraction .blockSize = 1
zero-ratio-half-block contraction .blockPositive = ℕOrder.≤-refl
zero-ratio-half-block contraction .blockContracts =
  subst (_≤ one-half)
    (Q.·AnnihilL 0 ∙ Q.·AnnihilL 1)
    one-half-nonnegative

positive-natural-log-one-half-block :
  AtanhHalfContractingBlock (positiveNaturalLogRatio ℕ.zero)
    (positive-natural-log-atanh-contraction ℕ.zero
      positive-natural-log-gap-certificate-at-one)
positive-natural-log-one-half-block .blockSize = 1
positive-natural-log-one-half-block .blockPositive = ℕOrder.≤-refl
positive-natural-log-one-half-block .blockContracts =
  transport (λ i → contractionPath (~ i) ≤ one-half) one-half-nonnegative
  where
  contractionPath :
    atanhRationalPower
      (positiveNaturalLogRatio ℕ.zero Q.· positiveNaturalLogRatio ℕ.zero) 1
      ≡ 0
  contractionPath =
    cong (λ ratio → atanhRationalPower (ratio Q.· ratio) 1)
      positive-natural-log-ratio-at-one ∙
    Q.·AnnihilL 0 ∙ Q.·AnnihilR 1

positive-natural-log-two-gap-certificate :
  PositiveNaturalLogGapCertificate (suc ℕ.zero)
positive-natural-log-two-gap-certificate .gapExponent = suc (suc ℕ.zero)
positive-natural-log-two-gap-certificate .precisionFitsGap =
  nat≤→positive-integer≤ 3 8 (5 , refl)

positive-natural-log-two-half-block :
  AtanhHalfContractingBlock (positiveNaturalLogRatio (suc ℕ.zero))
    (positive-natural-log-atanh-contraction (suc ℕ.zero)
      positive-natural-log-two-gap-certificate)
positive-natural-log-two-half-block .blockSize = 1
positive-natural-log-two-half-block .blockPositive = ℕOrder.≤-refl
positive-natural-log-two-half-block .blockContracts =
  nat≤→positive-integer≤ 2 9 (7 , refl)

positive-natural-log-three-gap-certificate :
  PositiveNaturalLogGapCertificate (suc (suc ℕ.zero))
positive-natural-log-three-gap-certificate .gapExponent = suc ℕ.zero
positive-natural-log-three-gap-certificate .precisionFitsGap =
  nat≤→positive-integer≤ 4 4 (0 , refl)

positive-natural-log-three-half-block :
  AtanhHalfContractingBlock
    (positiveNaturalLogRatio (suc (suc ℕ.zero)))
    (positive-natural-log-atanh-contraction (suc (suc ℕ.zero))
      positive-natural-log-three-gap-certificate)
positive-natural-log-three-half-block .blockSize = 1
positive-natural-log-three-half-block .blockPositive = ℕOrder.≤-refl
positive-natural-log-three-half-block .blockContracts =
  nat≤→positive-integer≤ 8 16 (8 , refl)

positive-natural-log-four-gap-certificate :
  PositiveNaturalLogGapCertificate (suc (suc (suc ℕ.zero)))
positive-natural-log-four-gap-certificate .gapExponent = suc (suc ℕ.zero)
positive-natural-log-four-gap-certificate .precisionFitsGap =
  nat≤→positive-integer≤ 5 8 (3 , refl)

positive-natural-log-four-half-block :
  AtanhHalfContractingBlock
    (positiveNaturalLogRatio (suc (suc (suc ℕ.zero))))
    (positive-natural-log-atanh-contraction (suc (suc (suc ℕ.zero)))
      positive-natural-log-four-gap-certificate)
positive-natural-log-four-half-block .blockSize = 1
positive-natural-log-four-half-block .blockPositive = ℕOrder.≤-refl
positive-natural-log-four-half-block .blockContracts =
  nat≤→positive-integer≤ 18 25 (7 , refl)

positive-natural-log-five-gap-certificate :
  PositiveNaturalLogGapCertificate (suc (suc (suc (suc ℕ.zero))))
positive-natural-log-five-gap-certificate .gapExponent = suc (suc ℕ.zero)
positive-natural-log-five-gap-certificate .precisionFitsGap =
  nat≤→positive-integer≤ 6 8 (2 , refl)

positive-natural-log-five-half-block :
  AtanhHalfContractingBlock
    (positiveNaturalLogRatio (suc (suc (suc (suc ℕ.zero)))))
    (positive-natural-log-atanh-contraction
      (suc (suc (suc (suc ℕ.zero))))
      positive-natural-log-five-gap-certificate)
positive-natural-log-five-half-block .blockSize = 1
positive-natural-log-five-half-block .blockPositive = ℕOrder.≤-refl
positive-natural-log-five-half-block .blockContracts =
  nat≤→positive-integer≤ 32 36 (4 , refl)

positive-natural-log-six-gap-certificate :
  PositiveNaturalLogGapCertificate
    (suc (suc (suc (suc (suc ℕ.zero)))))
positive-natural-log-six-gap-certificate .gapExponent = suc (suc ℕ.zero)
positive-natural-log-six-gap-certificate .precisionFitsGap =
  nat≤→positive-integer≤ 7 8 (1 , refl)

positive-natural-log-six-half-block :
  AtanhHalfContractingBlock
    (positiveNaturalLogRatio (suc (suc (suc (suc (suc ℕ.zero))))))
    (positive-natural-log-atanh-contraction
      (suc (suc (suc (suc (suc ℕ.zero)))))
      positive-natural-log-six-gap-certificate)
positive-natural-log-six-half-block .blockSize = 2
positive-natural-log-six-half-block .blockPositive = 1 , refl
positive-natural-log-six-half-block .blockContracts =
  nat≤→positive-integer≤ 1250 2401 (1151 , refl)

power-principle-gives-half-block :
  (principle : DyadicGapHalfPowerPrinciple) →
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) →
  AtanhHalfContractingBlock ratio contraction
power-principle-gives-half-block principle ratio contraction .blockSize =
  fst witness
  where witness = halfPowerFromDyadicGap principle ratio
          (contractionExponent contraction) (ratioNonnegative contraction)
          (ratioSeparatedFromOne contraction)
power-principle-gives-half-block principle ratio contraction .blockPositive =
  fst (snd witness)
  where witness = halfPowerFromDyadicGap principle ratio
          (contractionExponent contraction) (ratioNonnegative contraction)
          (ratioSeparatedFromOne contraction)
power-principle-gives-half-block principle ratio contraction .blockContracts =
  snd (snd witness)
  where witness = halfPowerFromDyadicGap principle ratio
          (contractionExponent contraction) (ratioNonnegative contraction)
          (ratioSeparatedFromOne contraction)

half-block-gives-power-decay :
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) →
  AtanhHalfContractingBlock ratio contraction →
  AtanhPowerDecay ratio contraction
half-block-gives-power-decay ratio contraction block .decayCutoff stage =
  blockSize block ℕ.· stage
half-block-gives-power-decay ratio contraction block .decayCutoffMonotone
  m n m≤n =
  subst2 ℕOrder._≤_
    (ℕ.·-comm m (blockSize block))
    (ℕ.·-comm n (blockSize block))
    (ℕOrder.≤-·k m≤n)
half-block-gives-power-decay ratio contraction block .decayCutoffCofinal
  termIndex =
  termIndex , subst2 ℕOrder._≤_
    (ℕ.+-zero termIndex) refl
    (ℕOrder.≤-·k {k = termIndex} (blockPositive block))
half-block-gives-power-decay ratio contraction block .powerDecay stage =
  subst2 _≤_
    (sym (atanh-rational-power-multiply
      (ratio Q.· ratio) (blockSize block) stage)) refl
    (rational-power≤precision
      (atanhRationalPower (ratio Q.· ratio) (blockSize block))
      (atanh-rational-power-nonnegative (ratio Q.· ratio)
        (nonnegative-bound-product ratio ratio
          (ratioNonnegative contraction) (ratioNonnegative contraction))
        (blockSize block))
      (blockContracts block) stage)

power-principle-gives-decay :
  (principle : DyadicGapHalfPowerPrinciple) →
  (ratio : Q.ℚ) (contraction : AtanhContractionInput ratio) →
  AtanhPowerDecay ratio contraction
power-principle-gives-decay principle ratio contraction =
  half-block-gives-power-decay ratio contraction
    (power-principle-gives-half-block principle ratio contraction)

atanh-term-bound-at-decay-cutoff :
  (ratio T : Q.ℚ) (start stage : ℕ) →
  (contraction : AtanhContractionInput ratio) →
  (decay : AtanhPowerDecay ratio contraction) → 0 ≤ T →
  MagnitudeBound (atanhTerm ratio start) T →
  MagnitudeBound
    (atanhTerm ratio (start ℕ.+ decayCutoff decay stage))
    (T Q.· precision stage)
atanh-term-bound-at-decay-cutoff ratio T start stage contraction decay
  0≤T initial =
  let iterated = atanh-term-iterated-square-bound
        ratio T start (decayCutoff decay stage) contraction 0≤T initial
      scale≤ = left-multiply-monotone T
        (atanhRationalPower (ratio Q.· ratio) (decayCutoff decay stage))
        (precision stage) 0≤T (powerDecay decay stage)
  in weaken-magnitude-bound _ _ (T Q.· precision stage) scale≤ iterated

record AtanhTailSeed (ratio : Q.ℚ) : Type where
  field
    contraction : AtanhContractionInput ratio
    decay : AtanhPowerDecay ratio contraction
    startIndex : ℕ
    termExponent : ℕ
    initialTermBound :
      MagnitudeBound (atanhTerm ratio startIndex)
        (dyadicRadius termExponent)
open AtanhTailSeed public

positive-natural-log-tail-seed :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in AtanhHalfContractingBlock (positiveNaturalLogRatio n) contraction →
     AtanhTailSeed (positiveNaturalLogRatio n)
positive-natural-log-tail-seed n gap block .contraction = c
  where c = positive-natural-log-atanh-contraction n gap
positive-natural-log-tail-seed n gap block .decay =
  half-block-gives-power-decay _ c block
  where c = positive-natural-log-atanh-contraction n gap
positive-natural-log-tail-seed n gap block .startIndex = ℕ.zero
positive-natural-log-tail-seed n gap block .termExponent = ℕ.zero
positive-natural-log-tail-seed n gap block .initialTermBound =
  atanh-initial-term-bound _ c
  where c = positive-natural-log-atanh-contraction n gap

atanh-seed-scheduled-term-bound :
  {ratio : Q.ℚ} (seed : AtanhTailSeed ratio) (stage : ℕ) →
  MagnitudeBound
    (atanhTerm ratio
      (startIndex seed ℕ.+ decayCutoff (decay seed) stage))
    (dyadicRadius (termExponent seed) Q.· precision stage)
atanh-seed-scheduled-term-bound seed stage =
  atanh-term-bound-at-decay-cutoff _ _ (startIndex seed) stage
    (contraction seed) (decay seed)
    (dyadicRadius-nonnegative (termExponent seed))
    (initialTermBound seed)

atanh-seed-post-cutoff-term-bound :
  {ratio : Q.ℚ} (seed : AtanhTailSeed ratio) (stage offset : ℕ) →
  MagnitudeBound
    (atanhTerm ratio
      ((startIndex seed ℕ.+ decayCutoff (decay seed) stage) ℕ.+ offset))
    (dyadicRadius (termExponent seed) Q.· precision stage)
atanh-seed-post-cutoff-term-bound seed stage offset =
  atanh-term-later-nonincreasing _ _
    (startIndex seed ℕ.+ decayCutoff (decay seed) stage) offset
    (contraction seed)
    (nonnegative-bound-product
      (dyadicRadius (termExponent seed)) (precision stage)
      (dyadicRadius-nonnegative (termExponent seed))
      (precision-nonnegative stage))
    (atanh-seed-scheduled-term-bound seed stage)
