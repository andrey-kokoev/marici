{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module AtanhTailBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
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
open import DyadicallyBoundedCauchy
open import TaylorTermBounds
open import RationalTaylorApproximants
open import RationalLogTaylorApproximants
open import RationalLogConvergenceContract
open import AtanhPowerDecayContract
open import TaylorGeometricTail
open import OrderedDifferenceRegularity
open import CauchyAddition

module AtanhTailPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  successor-scale : (T countScale : fst R) →
    T +S (countScale ·S T) ≡ (1r +S countScale) ·S T
  successor-scale T countScale = solve! R

atanhTermBlock : Q.ℚ → ℕ → ℕ → Q.ℚ
atanhTermBlock ratio start zero = 0
atanhTermBlock ratio start (suc count) =
  atanhTerm ratio start Q.+ atanhTermBlock ratio (suc start) count

naturalScale : ℕ → Q.ℚ
naturalScale zero = 0
naturalScale (suc count) = 1 Q.+ naturalScale count

natural-scale-is-natℚ : (count : ℕ) → naturalScale count ≡ natℚ count
natural-scale-is-natℚ zero = refl
natural-scale-is-natℚ (suc count) =
  cong (1 Q.+_) (natural-scale-is-natℚ count) ∙
  Q.+Comm 1 (natℚ count)

natural-scale≤dyadic-radius : (count : ℕ) →
  naturalScale count ≤ dyadicRadius count
natural-scale≤dyadic-radius count =
  subst (_≤ dyadicRadius count) (sym (natural-scale-is-natℚ count))
    (natℚ≤dyadicRadius count)

natural-scale-nonnegative : (count : ℕ) → 0 ≤ naturalScale count
natural-scale-nonnegative zero = isRefl≤ 0
natural-scale-nonnegative (suc count) =
  ≤Monotone+ 0 1 0 (naturalScale count)
    Cubical.Data.Int.Order.zero-≤pos (natural-scale-nonnegative count)

atanh-term-block-at-zero-ratio : (start count : ℕ) →
  atanhTermBlock 0 start count ≡ 0
atanh-term-block-at-zero-ratio start zero = refl
atanh-term-block-at-zero-ratio start (suc count) =
  cong₂ Q._+_ (atanhTerm-at-zero start)
    (atanh-term-block-at-zero-ratio (suc start) count) ∙
  Q.+IdL 0

atanh-term-block-zero-right : (ratio : Q.ℚ) (start : ℕ) →
  atanhTermBlock ratio start zero ≡ 0
atanh-term-block-zero-right ratio start = refl

atanh-term-block-append :
  (ratio : Q.ℚ) (start left right : ℕ) →
  atanhTermBlock ratio start (left ℕ.+ right) ≡
  atanhTermBlock ratio start left Q.+
    atanhTermBlock ratio (start ℕ.+ left) right
atanh-term-block-append ratio start zero right =
  sym (Q.+IdL (atanhTermBlock ratio start right)) ∙
  cong (0 Q.+_)
    (cong (λ index → atanhTermBlock ratio index right)
      (sym (ℕ.+-zero start)))
atanh-term-block-append ratio start (suc left) right =
  cong (atanhTerm ratio start Q.+_)
    (atanh-term-block-append ratio (suc start) left right) ∙
  Q.+Assoc (atanhTerm ratio start)
    (atanhTermBlock ratio (suc start) left)
    (atanhTermBlock ratio (suc start ℕ.+ left) right) ∙
  cong (λ tail →
      atanhTermBlock ratio start (suc left) Q.+ tail)
    (cong (λ index → atanhTermBlock ratio index right)
      (sym (ℕ.+-suc start left)))

atanh-term-block-uniform-magnitude :
  (ratio T : Q.ℚ) (start count : ℕ) → 0 ≤ T →
  ((offset : ℕ) → MagnitudeBound (atanhTerm ratio (start ℕ.+ offset)) T) →
  MagnitudeBound (atanhTermBlock ratio start count)
    (naturalScale count Q.· T)
atanh-term-block-uniform-magnitude ratio T start zero 0≤T bound =
  nonnegative-value-magnitude 0 (0 Q.· T)
    (isRefl≤ 0)
    (nonnegative-bound-product 0 T (isRefl≤ 0) 0≤T)
    (nonnegative-bound-product 0 T (isRefl≤ 0) 0≤T)
atanh-term-block-uniform-magnitude ratio T start (suc count) 0≤T bound =
  subst (MagnitudeBound (atanhTermBlock ratio start (suc count)))
    (AtanhTailPaths.successor-scale PreferredℚCommRing T (naturalScale count))
    (add-magnitude-bounds (atanhTerm ratio start) T
      (atanhTermBlock ratio (suc start) count) (naturalScale count Q.· T)
      (transport-magnitude _ _ T
        (cong (atanhTerm ratio) (sym (ℕ.+-zero start))) (bound zero))
      (atanh-term-block-uniform-magnitude ratio T (suc start) count 0≤T
        (λ offset → transport-magnitude _ _ T
          (cong (atanhTerm ratio) (sym (ℕ.+-suc start offset)))
          (bound (suc offset)))))

atanh-seed-post-cutoff-block-bound :
  {ratio : Q.ℚ} (seed : AtanhTailSeed ratio) (stage count : ℕ) →
  MagnitudeBound
    (atanhTermBlock ratio
      (startIndex seed ℕ.+ decayCutoff (decay seed) stage) count)
    (naturalScale count Q.·
      (dyadicRadius (termExponent seed) Q.· precision stage))
atanh-seed-post-cutoff-block-bound seed stage count =
  atanh-term-block-uniform-magnitude _ _
    (startIndex seed ℕ.+ decayCutoff (decay seed) stage) count
    (nonnegative-bound-product
      (dyadicRadius (termExponent seed)) (precision stage)
      (dyadicRadius-nonnegative (termExponent seed))
      (precision-nonnegative stage))
    (atanh-seed-post-cutoff-term-bound seed stage)

positive-natural-log-scheduled-block-bound :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in (block : AtanhHalfContractingBlock
        (positiveNaturalLogRatio n) contraction) →
     (stage : ℕ) →
     MagnitudeBound
       (atanhTermBlock (positiveNaturalLogRatio n)
         (blockSize block ℕ.· stage) (blockSize block))
       (naturalScale (blockSize block) Q.· precision stage)
positive-natural-log-scheduled-block-bound n gap block stage =
  subst
    (MagnitudeBound
      (atanhTermBlock (positiveNaturalLogRatio n)
        (blockSize block ℕ.· stage) (blockSize block)))
    (cong (naturalScale (blockSize block) Q.·_)
      (Q.·IdL (precision stage)))
    (atanh-seed-post-cutoff-block-bound
      (positive-natural-log-tail-seed n gap block) stage (blockSize block))

positiveNaturalLogScheduledBlock :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  AtanhHalfContractingBlock (positiveNaturalLogRatio n)
    (positive-natural-log-atanh-contraction n gap) →
  ℕ → Q.ℚ
positiveNaturalLogScheduledBlock n gap block stage =
  atanhTermBlock (positiveNaturalLogRatio n)
    (blockSize block ℕ.· stage) (blockSize block)

flattenedBlockLength : ℕ → ℕ → ℕ
flattenedBlockLength block count = block ℕ.· suc count

flattened-block-length-step : (block count : ℕ) →
  flattenedBlockLength block (suc count) ≡
  flattenedBlockLength block count ℕ.+ block
flattened-block-length-step block count =
  ℕ.·-suc block (suc count) ∙
  ℕ.+-comm block (block ℕ.· suc count)

scheduled-block-prefix-is-contiguous :
  (ratio : Q.ℚ) (block count : ℕ) →
  finiteSum
    (λ stage → atanhTermBlock ratio (block ℕ.· stage) block) count ≡
  atanhTermBlock ratio zero (flattenedBlockLength block count)
scheduled-block-prefix-is-contiguous ratio block zero =
  cong (λ start → atanhTermBlock ratio start block)
    (sym (ℕProperties.0≡m·0 block)) ∙
  cong (atanhTermBlock ratio zero)
    (sym (ℕ.·-suc block zero ∙
      cong (block ℕ.+_) (sym (ℕProperties.0≡m·0 block)) ∙
      ℕ.+-zero block))
scheduled-block-prefix-is-contiguous ratio block (suc count) =
  cong (Q._+ atanhTermBlock ratio (block ℕ.· suc count) block)
    (scheduled-block-prefix-is-contiguous ratio block count) ∙
  sym (atanh-term-block-append ratio zero
    (flattenedBlockLength block count) block) ∙
  cong (atanhTermBlock ratio zero)
    (sym (flattened-block-length-step block count))

positive-natural-log-scheduled-block-tail-bound :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in (block : AtanhHalfContractingBlock
        (positiveNaturalLogRatio n) contraction) →
     (start count : ℕ) →
     MagnitudeBound
       (termBlock (positiveNaturalLogScheduledBlock n gap block) start count)
       (naturalScale (blockSize block) Q.· geometricBlock start count)
positive-natural-log-scheduled-block-tail-bound n gap block start count =
  termBlock-magnitude
    (positiveNaturalLogScheduledBlock n gap block)
    (naturalScale (blockSize block)) start count
    (natural-scale-nonnegative (blockSize block))
    (λ j → positive-natural-log-scheduled-block-bound n gap block (suc j))

positive-natural-log-scheduled-block-tail≤precision :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in (block : AtanhHalfContractingBlock
        (positiveNaturalLogRatio n) contraction) →
     (start count : ℕ) →
     MagnitudeBound
       (termBlock (positiveNaturalLogScheduledBlock n gap block) start count)
       (naturalScale (blockSize block) Q.· precision start)
positive-natural-log-scheduled-block-tail≤precision n gap block start count =
  termBlock≤scaledPrecision
    (positiveNaturalLogScheduledBlock n gap block)
    (naturalScale (blockSize block)) start count
    (natural-scale-nonnegative (blockSize block))
    (λ j → positive-natural-log-scheduled-block-bound n gap block (suc j))

positive-natural-log-block-partial-sum-difference :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in (block : AtanhHalfContractingBlock
        (positiveNaturalLogRatio n) contraction) →
     (start count : ℕ) →
     MagnitudeBound
       (finiteSum (positiveNaturalLogScheduledBlock n gap block)
          (start ℕ.+ count) Q.+
        (Q.- finiteSum (positiveNaturalLogScheduledBlock n gap block) start))
       (naturalScale (blockSize block) Q.· precision start)
positive-natural-log-block-partial-sum-difference n gap block start count =
  finiteSum-segment-difference-magnitude
    (positiveNaturalLogScheduledBlock n gap block)
    (naturalScale (blockSize block)) start count
    (natural-scale-nonnegative (blockSize block))
    (λ j → positive-natural-log-scheduled-block-bound n gap block (suc j))

positive-natural-log-shifted-block-partial-sum-difference :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in (block : AtanhHalfContractingBlock
        (positiveNaturalLogRatio n) contraction) →
     (stage count : ℕ) →
     MagnitudeBound
       (finiteSum (positiveNaturalLogScheduledBlock n gap block)
          ((blockSize block ℕ.+ stage) ℕ.+ count) Q.+
        (Q.- finiteSum (positiveNaturalLogScheduledBlock n gap block)
          (blockSize block ℕ.+ stage)))
       (precision stage)
positive-natural-log-shifted-block-partial-sum-difference
  n gap block stage count =
  let raw = positive-natural-log-block-partial-sum-difference
        n gap block (blockSize block ℕ.+ stage) count
      multiplied = ≤-·o
        (naturalScale (blockSize block)) (dyadicRadius (blockSize block))
        (precision (blockSize block ℕ.+ stage))
        (precision-nonnegative (blockSize block ℕ.+ stage))
        (natural-scale≤dyadic-radius (blockSize block))
      absorbed = subst
        (naturalScale (blockSize block) Q.·
          precision (blockSize block ℕ.+ stage) ≤_)
        (radius-cancels-precision-shift (blockSize block) stage)
        multiplied
  in weaken-magnitude-bound _ _ (precision stage) absorbed raw

block-shift-index : (block m n d : ℕ) → d ℕ.+ m ≡ n →
  (block ℕ.+ m) ℕ.+ d ≡ block ℕ.+ n
block-shift-index block m n d d+m≡n =
  sym (ℕ.+-assoc block m d) ∙
  cong (block ℕ.+_) (ℕ.+-comm m d ∙ d+m≡n)

positiveNaturalLogBlockCauchy :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in AtanhHalfContractingBlock
       (positiveNaturalLogRatio n) contraction → RegularCauchy
positiveNaturalLogBlockCauchy n gap block =
  regular-from-ordered-differences approximationSequence orderedDifference
  where
  blockTerm = positiveNaturalLogScheduledBlock n gap block
  approximationSequence : ℕ → Q.ℚ
  approximationSequence stage =
    finiteSum blockTerm (blockSize block ℕ.+ stage)
  orderedDifference : (m k : ℕ) → ℕOrder._≤_ m k →
    MagnitudeBound
      (approximationSequence k Q.+ (Q.- approximationSequence m))
      (precision m)
  orderedDifference m k (d , d+m≡k) =
    transport-magnitude _ _ (precision m)
      (sym (cong (λ index → finiteSum blockTerm index Q.+
          (Q.- finiteSum blockTerm (blockSize block ℕ.+ m)))
        (block-shift-index (blockSize block) m k d d+m≡k)))
      (positive-natural-log-shifted-block-partial-sum-difference
        n gap block m d)

positive-natural-log-block-approximation-contiguous :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in (block : AtanhHalfContractingBlock
        (positiveNaturalLogRatio n) contraction) →
     (stage : ℕ) →
     approximation (positiveNaturalLogBlockCauchy n gap block) stage ≡
     atanhTermBlock (positiveNaturalLogRatio n) zero
       (flattenedBlockLength (blockSize block)
         (blockSize block ℕ.+ stage))
positive-natural-log-block-approximation-contiguous n gap block stage =
  scheduled-block-prefix-is-contiguous
    (positiveNaturalLogRatio n) (blockSize block)
    (blockSize block ℕ.+ stage)

record PositiveNaturalLogEvaluationInput (n : ℕ) : Type where
  field
    gap : PositiveNaturalLogGapCertificate n
    halfBlock : AtanhHalfContractingBlock (positiveNaturalLogRatio n)
      (positive-natural-log-atanh-contraction n gap)
open PositiveNaturalLogEvaluationInput public

positiveNaturalLogOneInput : PositiveNaturalLogEvaluationInput ℕ.zero
positiveNaturalLogOneInput .gap = positive-natural-log-gap-certificate-at-one
positiveNaturalLogOneInput .halfBlock = positive-natural-log-one-half-block

positiveNaturalLogTwoInput : PositiveNaturalLogEvaluationInput (suc ℕ.zero)
positiveNaturalLogTwoInput .gap = positive-natural-log-two-gap-certificate
positiveNaturalLogTwoInput .halfBlock = positive-natural-log-two-half-block

positiveNaturalLogAtanhRegularFromInput :
  (n : ℕ) → PositiveNaturalLogEvaluationInput n → RegularCauchy
positiveNaturalLogAtanhRegularFromInput n input =
  positiveNaturalLogBlockCauchy n (gap input) (halfBlock input)

positive-natural-log-input-approximation-contiguous :
  (n : ℕ) (input : PositiveNaturalLogEvaluationInput n) (stage : ℕ) →
  approximation (positiveNaturalLogAtanhRegularFromInput n input) stage ≡
  atanhTermBlock (positiveNaturalLogRatio n) zero
    (flattenedBlockLength (blockSize (halfBlock input))
      (blockSize (halfBlock input) ℕ.+ stage))
positive-natural-log-input-approximation-contiguous n input =
  positive-natural-log-block-approximation-contiguous
    n (gap input) (halfBlock input)

positiveNaturalLogRegular :
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) →
  let contraction = positive-natural-log-atanh-contraction n gap
  in AtanhHalfContractingBlock
       (positiveNaturalLogRatio n) contraction → RegularCauchy
positiveNaturalLogRegular n gap block =
  addRegular atanhValue atanhValue
  where
  atanhValue = positiveNaturalLogBlockCauchy n gap block

positiveNaturalLogOneRegular : RegularCauchy
positiveNaturalLogOneRegular =
  positiveNaturalLogRegular ℕ.zero
    positive-natural-log-gap-certificate-at-one
    positive-natural-log-one-half-block

positive-natural-log-one-approximation-zero : (stage : ℕ) →
  approximation positiveNaturalLogOneRegular stage ≡ 0
positive-natural-log-one-approximation-zero stage =
  let blockApproximationZero :
        approximation
          (positiveNaturalLogBlockCauchy ℕ.zero
            positive-natural-log-gap-certificate-at-one
            positive-natural-log-one-half-block)
          (suc stage) ≡ 0
      blockApproximationZero =
        positive-natural-log-block-approximation-contiguous ℕ.zero
          positive-natural-log-gap-certificate-at-one
          positive-natural-log-one-half-block (suc stage) ∙
        cong (λ ratio → atanhTermBlock ratio zero
          (flattenedBlockLength 1 (1 ℕ.+ suc stage)))
          positive-natural-log-ratio-at-one ∙
        atanh-term-block-at-zero-ratio zero
          (flattenedBlockLength 1 (1 ℕ.+ suc stage))
  in cong₂ Q._+_ blockApproximationZero blockApproximationZero ∙ Q.+IdL 0

positive-natural-log-one-any-block-is-zero :
  (gap : PositiveNaturalLogGapCertificate ℕ.zero) →
  (block : AtanhHalfContractingBlock (positiveNaturalLogRatio ℕ.zero)
    (positive-natural-log-atanh-contraction ℕ.zero gap)) →
  positiveNaturalLogRegular ℕ.zero gap block ≡ constantCauchy 0
positive-natural-log-one-any-block-is-zero gap block =
  regularCauchy-ext _ _ (funExt approximationZero)
  where
  approximationZero : (stage : ℕ) →
    approximation (positiveNaturalLogRegular ℕ.zero gap block) stage ≡ 0
  approximationZero stage =
    let blockApproximationZero :
          approximation (positiveNaturalLogBlockCauchy ℕ.zero gap block)
            (suc stage) ≡ 0
        blockApproximationZero =
          positive-natural-log-block-approximation-contiguous
            ℕ.zero gap block (suc stage) ∙
          cong (λ ratio → atanhTermBlock ratio zero
            (flattenedBlockLength (blockSize block)
              (blockSize block ℕ.+ suc stage)))
            positive-natural-log-ratio-at-one ∙
          atanh-term-block-at-zero-ratio zero
            (flattenedBlockLength (blockSize block)
              (blockSize block ℕ.+ suc stage))
    in cong₂ Q._+_ blockApproximationZero blockApproximationZero ∙ Q.+IdL 0

positive-natural-log-one-is-zero :
  positiveNaturalLogOneRegular ≡ constantCauchy 0
positive-natural-log-one-is-zero =
  regularCauchy-ext positiveNaturalLogOneRegular (constantCauchy 0)
    (funExt positive-natural-log-one-approximation-zero)

positiveNaturalLogTwoRegular : RegularCauchy
positiveNaturalLogTwoRegular =
  positiveNaturalLogRegular (suc ℕ.zero)
    positive-natural-log-two-gap-certificate
    positive-natural-log-two-half-block

positiveNaturalLogThreeRegular : RegularCauchy
positiveNaturalLogThreeRegular =
  positiveNaturalLogRegular (suc (suc ℕ.zero))
    positive-natural-log-three-gap-certificate
    positive-natural-log-three-half-block

positiveNaturalLogFourRegular : RegularCauchy
positiveNaturalLogFourRegular =
  positiveNaturalLogRegular (suc (suc (suc ℕ.zero)))
    positive-natural-log-four-gap-certificate
    positive-natural-log-four-half-block

positiveNaturalLogFiveRegular : RegularCauchy
positiveNaturalLogFiveRegular =
  positiveNaturalLogRegular (suc (suc (suc (suc ℕ.zero))))
    positive-natural-log-five-gap-certificate
    positive-natural-log-five-half-block

positiveNaturalLogSixRegular : RegularCauchy
positiveNaturalLogSixRegular =
  positiveNaturalLogRegular
    (suc (suc (suc (suc (suc ℕ.zero)))))
    positive-natural-log-six-gap-certificate
    positive-natural-log-six-half-block

positiveNaturalLogRegularFromPowerPrinciple :
  DyadicGapHalfPowerPrinciple →
  (n : ℕ) (gap : PositiveNaturalLogGapCertificate n) → RegularCauchy
positiveNaturalLogRegularFromInput :
  (n : ℕ) → PositiveNaturalLogEvaluationInput n → RegularCauchy
positiveNaturalLogRegularFromInput n input =
  positiveNaturalLogRegular n (gap input) (halfBlock input)

positiveNaturalLogRegularFromPowerPrinciple principle n gap =
  positiveNaturalLogRegular n gap
    (power-principle-gives-half-block principle
      (positiveNaturalLogRatio n)
      (positive-natural-log-atanh-contraction n gap))
