{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformSineLateDifference where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using
  (ℕ; zero; suc; _+_; _∸_; +-comm)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Sum
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import Cubical.Data.Rationals.Order
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import TaylorTermBounds
open import DyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import SineTermBounds
open import SineTailSchedule
open import SineInputDifference
open import SinePartialSumInputDifference
open import UniformSineSeedBounds
open import UniformSineStabilityScale
open import UniformSineInputStabilityContract
open import UniformExponentialDifferenceWeights

module SineLateDifferencePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  propagated-regroup :
    (difference q firstInverse secondInverse : fst R) →
    -S (((((difference ·S q) ·S q) ·S firstInverse) ·S secondInverse)) ≡
    -S ((difference ·S (q ·S firstInverse)) ·S
      (q ·S secondInverse))
  propagated-regroup difference q firstInverse secondInverse = solve! R

  fresh-left-regroup :
    (term difference q firstInverse secondInverse : fst R) →
    -S (((((term ·S difference) ·S q) ·S firstInverse) ·S secondInverse)) ≡
    -S ((((term ·S (q ·S secondInverse)) ·S difference) ·S firstInverse))
  fresh-left-regroup term difference q firstInverse secondInverse = solve! R

  fresh-right-regroup :
    (term r difference firstInverse secondInverse : fst R) →
    -S (((((term ·S r) ·S difference) ·S firstInverse) ·S secondInverse)) ≡
    -S ((((term ·S (r ·S firstInverse)) ·S difference) ·S secondInverse))
  fresh-right-regroup term r difference firstInverse secondInverse = solve! R

  propagated-scale : (scale half : fst R) →
    (scale ·S half) ·S half ≡ scale ·S (half ·S half)
  propagated-scale scale half = solve! R

  fresh-scale : (seed precision half error : fst R) →
    (((seed ·S precision) ·S half) ·S error) ·S 1r ≡
      ((seed ·S (precision ·S half)) ·S error)
  fresh-scale seed precision half error = solve! R

  propagated-bound-scale : (core weight error half : fst R) →
    ((((core ·S weight) ·S error) ·S half) ·S 1r) ≡
      (core ·S (weight ·S half)) ·S error
  propagated-bound-scale core weight error half = solve! R

  combine-three-half-scales :
    (core weight precision half error : fst R) →
    (((core ·S (weight ·S half)) ·S error) +S
      ((core ·S (precision ·S half)) ·S error)) +S
      ((core ·S (precision ·S half)) ·S error) ≡
    (core ·S ((weight ·S half) +S
      ((precision ·S half) +S (precision ·S half)))) ·S error
  combine-three-half-scales core weight precision half error = solve! R

  combine-block-scale : (core sum weight error : fst R) →
    ((core ·S sum) ·S error) +S ((core ·S weight) ·S error) ≡
    (core ·S (sum +S weight)) ·S error
  combine-block-scale core sum weight error = solve! R

  extend-reassociate : (cutoff extension term : fst R) →
    (cutoff +S extension) +S term ≡ cutoff +S (extension +S term)
  extend-reassociate cutoff extension term = solve! R

  combine-initial-extension-scale :
    (core extension error : fst R) →
    (core ·S error) +S ((core ·S extension) ·S error) ≡
      (core +S (core ·S extension)) ·S error
  combine-initial-extension-scale core extension error = solve! R

late-sine-propagated-difference-bound :
  (q difference error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound difference
    ((dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
      lateDifferenceWeight extra) Q.· error) →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (Q.- (((((difference Q.· q) Q.· q) Q.·
      reciprocalSuccessor (firstSineDenominator index)) Q.·
      reciprocalSuccessor (secondSineDenominator index))))
    ((dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
      (lateDifferenceWeight extra Q.· one-half)) Q.· error)
late-sine-propagated-difference-bound q difference error d extra
  errorNonnegative qBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      core = dyadicRadius (uniformSineStabilityCoreExponent d)
      weight = lateDifferenceWeight extra
      scale = (core Q.· weight) Q.· error
      scaleNonnegative = nonnegative-bound-product (core Q.· weight) error
        (nonnegative-bound-product core weight
          (dyadicRadius-nonnegative (uniformSineStabilityCoreExponent d))
          (late-difference-weight-nonnegative extra)) errorNonnegative
      firstFactor = q Q.· reciprocalSuccessor (firstSineDenominator index)
      secondFactor = q Q.· reciprocalSuccessor (secondSineDenominator index)
      firstBound = late-sine-first-factor-magnitude≤half q d extra qBound
      secondHalf = late-sine-second-factor-magnitude≤half q d extra qBound
      secondBound = weaken-magnitude-bound secondFactor one-half 1
        (precision-step≤ zero) secondHalf
      once = arbitrary-multiplier-bound difference scale firstFactor one-half
        scaleNonnegative one-half-nonnegative differenceBound firstBound
      onceNonnegative = nonnegative-bound-product scale one-half
        scaleNonnegative one-half-nonnegative
      twice = arbitrary-multiplier-bound (difference Q.· firstFactor)
        (scale Q.· one-half) secondFactor 1
        onceNonnegative (dyadicRadius-nonnegative 0) once secondBound
      negated = negate-magnitude-bound _ _ twice
      valuePath = SineLateDifferencePaths.propagated-regroup
        PreferredℚCommRing difference q
        (reciprocalSuccessor (firstSineDenominator index))
        (reciprocalSuccessor (secondSineDenominator index))
      scalePath = SineLateDifferencePaths.propagated-bound-scale
        PreferredℚCommRing core weight error one-half
  in
  subst (MagnitudeBound
    (Q.- (((((difference Q.· q) Q.· q) Q.·
      reciprocalSuccessor (firstSineDenominator index)) Q.·
      reciprocalSuccessor (secondSineDenominator index)))))
    scalePath
    (transport-magnitude _ _ _ valuePath negated)

late-sine-fresh-left-difference-bound :
  (q r error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (Q.- (((((sineTerm r index Q.· (q Q.+ (Q.- r))) Q.· q) Q.·
      reciprocalSuccessor (firstSineDenominator index)) Q.·
      reciprocalSuccessor (secondSineDenominator index))))
    ((dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
      (precision extra Q.· one-half)) Q.· error)
late-sine-fresh-left-difference-bound q r error d extra
  errorNonnegative qBound rBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      seedExponent = uniformSineSeedExponent d
      coreExponent = uniformSineStabilityCoreExponent d
      seedScale = dyadicRadius seedExponent Q.· precision extra
      coreScale = dyadicRadius coreExponent Q.· precision extra
      seed = uniformSineTailSeed r d rBound
      termRaw = shifted-sine-term-geometric-decay seed extra
      seed≤core = dyadicRadius-monotone seedExponent coreExponent
        ℕOrder.right-≤-max
      seedScale≤coreScale = ≤-·o (dyadicRadius seedExponent)
        (dyadicRadius coreExponent) (precision extra)
        (precision-nonnegative extra) seed≤core
      termBound = weaken-magnitude-bound (sineTerm r index)
        seedScale coreScale seedScale≤coreScale termRaw
      contractedFactor = q Q.· reciprocalSuccessor
        (secondSineDenominator index)
      contractedFactorBound =
        late-sine-second-factor-magnitude≤half q d extra qBound
      firstProduct = arbitrary-multiplier-bound
        (sineTerm r index) coreScale contractedFactor one-half
        (nonnegative-bound-product (dyadicRadius coreExponent)
          (precision extra) (dyadicRadius-nonnegative coreExponent)
          (precision-nonnegative extra))
        one-half-nonnegative termBound contractedFactorBound
      firstScaleNonnegative = nonnegative-bound-product coreScale one-half
        (nonnegative-bound-product (dyadicRadius coreExponent)
          (precision extra) (dyadicRadius-nonnegative coreExponent)
          (precision-nonnegative extra)) one-half-nonnegative
      withDifference = arbitrary-multiplier-bound
        (sineTerm r index Q.· contractedFactor)
        (coreScale Q.· one-half) (q Q.+ (Q.- r)) error
        firstScaleNonnegative errorNonnegative firstProduct differenceBound
      differenceScaleNonnegative = nonnegative-bound-product
        (coreScale Q.· one-half) error firstScaleNonnegative errorNonnegative
      withReciprocal = arbitrary-multiplier-bound
        ((sineTerm r index Q.· contractedFactor) Q.· (q Q.+ (Q.- r)))
        ((coreScale Q.· one-half) Q.· error)
        (reciprocalSuccessor (firstSineDenominator index)) 1
        differenceScaleNonnegative (dyadicRadius-nonnegative 0)
        withDifference (reciprocal-magnitude≤one (firstSineDenominator index))
      negated = negate-magnitude-bound _ _ withReciprocal
      valuePath = SineLateDifferencePaths.fresh-left-regroup
        PreferredℚCommRing (sineTerm r index) (q Q.+ (Q.- r)) q
        (reciprocalSuccessor (firstSineDenominator index))
        (reciprocalSuccessor (secondSineDenominator index))
      scalePath = SineLateDifferencePaths.fresh-scale PreferredℚCommRing
        (dyadicRadius coreExponent) (precision extra) one-half error
  in
  subst (MagnitudeBound
    (Q.- (((((sineTerm r index Q.· (q Q.+ (Q.- r))) Q.· q) Q.·
      reciprocalSuccessor (firstSineDenominator index)) Q.·
      reciprocalSuccessor (secondSineDenominator index)))))
    scalePath (transport-magnitude _ _ _ valuePath negated)

late-sine-fresh-right-difference-bound :
  (q r error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (Q.- (((((sineTerm r index Q.· r) Q.· (q Q.+ (Q.- r))) Q.·
      reciprocalSuccessor (firstSineDenominator index)) Q.·
      reciprocalSuccessor (secondSineDenominator index))))
    ((dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
      (precision extra Q.· one-half)) Q.· error)
late-sine-fresh-right-difference-bound q r error d extra
  errorNonnegative qBound rBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      seedExponent = uniformSineSeedExponent d
      coreExponent = uniformSineStabilityCoreExponent d
      seedScale = dyadicRadius seedExponent Q.· precision extra
      coreScale = dyadicRadius coreExponent Q.· precision extra
      seed = uniformSineTailSeed r d rBound
      termRaw = shifted-sine-term-geometric-decay seed extra
      seed≤core = dyadicRadius-monotone seedExponent coreExponent
        ℕOrder.right-≤-max
      seedScale≤coreScale = ≤-·o (dyadicRadius seedExponent)
        (dyadicRadius coreExponent) (precision extra)
        (precision-nonnegative extra) seed≤core
      termBound = weaken-magnitude-bound (sineTerm r index)
        seedScale coreScale seedScale≤coreScale termRaw
      contractedFactor = r Q.· reciprocalSuccessor
        (firstSineDenominator index)
      contractedFactorBound =
        late-sine-first-factor-magnitude≤half r d extra rBound
      firstProduct = arbitrary-multiplier-bound
        (sineTerm r index) coreScale contractedFactor one-half
        (nonnegative-bound-product (dyadicRadius coreExponent)
          (precision extra) (dyadicRadius-nonnegative coreExponent)
          (precision-nonnegative extra))
        one-half-nonnegative termBound contractedFactorBound
      firstScaleNonnegative = nonnegative-bound-product coreScale one-half
        (nonnegative-bound-product (dyadicRadius coreExponent)
          (precision extra) (dyadicRadius-nonnegative coreExponent)
          (precision-nonnegative extra)) one-half-nonnegative
      withDifference = arbitrary-multiplier-bound
        (sineTerm r index Q.· contractedFactor)
        (coreScale Q.· one-half) (q Q.+ (Q.- r)) error
        firstScaleNonnegative errorNonnegative firstProduct differenceBound
      differenceScaleNonnegative = nonnegative-bound-product
        (coreScale Q.· one-half) error firstScaleNonnegative errorNonnegative
      withReciprocal = arbitrary-multiplier-bound
        ((sineTerm r index Q.· contractedFactor) Q.· (q Q.+ (Q.- r)))
        ((coreScale Q.· one-half) Q.· error)
        (reciprocalSuccessor (secondSineDenominator index)) 1
        differenceScaleNonnegative (dyadicRadius-nonnegative 0)
        withDifference (reciprocal-magnitude≤one (secondSineDenominator index))
      negated = negate-magnitude-bound _ _ withReciprocal
      valuePath = SineLateDifferencePaths.fresh-right-regroup
        PreferredℚCommRing (sineTerm r index) r (q Q.+ (Q.- r))
        (reciprocalSuccessor (firstSineDenominator index))
        (reciprocalSuccessor (secondSineDenominator index))
      scalePath = SineLateDifferencePaths.fresh-scale PreferredℚCommRing
        (dyadicRadius coreExponent) (precision extra) one-half error
  in
  subst (MagnitudeBound
    (Q.- (((((sineTerm r index Q.· r) Q.· (q Q.+ (Q.- r))) Q.·
      reciprocalSuccessor (firstSineDenominator index)) Q.·
      reciprocalSuccessor (secondSineDenominator index)))))
    scalePath (transport-magnitude _ _ _ valuePath negated)

late-sine-term-difference-bound :
  (q r error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (sineTerm q index Q.+ (Q.- sineTerm r index))
    ((dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
      lateDifferenceWeight extra) Q.· error)
late-sine-term-difference-bound q r error d zero errorNonnegative
  qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      raw = sine-term-input-difference-bound q r error d cutoff
        errorNonnegative qBound rBound differenceBound
      exponent≤core : ℕOrder._≤_
        (sineTermDifferenceExponent d cutoff)
        (uniformSineStabilityCoreExponent d)
      exponent≤core = ℕOrder.≤-trans
        (term-difference-exponent≤sine-partial-sum d cutoff)
        ℕOrder.left-≤-max
      scale≤ = ≤-·o
        (dyadicRadius (sineTermDifferenceExponent d cutoff))
        (dyadicRadius (uniformSineStabilityCoreExponent d))
        error errorNonnegative
        (dyadicRadius-monotone _ _ exponent≤core)
      weakened = weaken-magnitude-bound _ _ _ scale≤ raw
      reindexed = transport-magnitude _ _ _
        (cong (λ index → sineTerm q index Q.+ (Q.- sineTerm r index))
          (ℕ.+-zero cutoff)) weakened
      scalePath = cong (Q._· error)
        (Q.·IdR (dyadicRadius (uniformSineStabilityCoreExponent d)))
  in subst (MagnitudeBound _) (sym scalePath) reindexed
late-sine-term-difference-bound q r error d (suc extra)
  errorNonnegative qBound rBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      core = dyadicRadius (uniformSineStabilityCoreExponent d)
      weight = lateDifferenceWeight extra
      p = precision extra
      previousDifference = sineTerm q index Q.+ (Q.- sineTerm r index)
      previous = late-sine-term-difference-bound q r error d extra
        errorNonnegative qBound rBound differenceBound
      propagated = late-sine-propagated-difference-bound
        q previousDifference error d extra errorNonnegative qBound previous
      freshLeft = late-sine-fresh-left-difference-bound
        q r error d extra errorNonnegative qBound rBound differenceBound
      freshRight = late-sine-fresh-right-difference-bound
        q r error d extra errorNonnegative qBound rBound differenceBound
      firstCombined = add-magnitude-bounds _ _ _ _ propagated freshLeft
      combined = add-magnitude-bounds _ _ _ _ firstCombined freshRight
      halfScalePath = SineLateDifferencePaths.combine-three-half-scales
        PreferredℚCommRing core weight p one-half error
      collapseFreshHalves = cong
        (λ z → (core Q.· ((weight Q.· one-half) Q.+ z)) Q.· error)
        (half-double p)
      scaled = subst (MagnitudeBound _) (halfScalePath ∙ collapseFreshHalves)
        combined
      valuePath =
        cong (λ j → sineTerm q j Q.+ (Q.- sineTerm r j))
          (ℕ.+-suc (dyadicNat (suc d)) extra) ∙
        sine-term-difference-step q r index
  in transport-magnitude _ _ _ valuePath scaled

lateSinePartialDifferenceExtension :
  (q r : Q.ℚ) (d : ℕ) → ℕ → Q.ℚ
lateSinePartialDifferenceExtension q r d zero = 0
lateSinePartialDifferenceExtension q r d (suc n) =
  lateSinePartialDifferenceExtension q r d n Q.+
  (sineTerm q (suc (dyadicNat (suc d) ℕ.+ n)) Q.+
   (Q.- sineTerm r (suc (dyadicNat (suc d) ℕ.+ n))))

late-sine-partial-difference-extension-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound (lateSinePartialDifferenceExtension q r d count)
    ((dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
      lateExtensionWeightSum count) Q.· error)
late-sine-partial-difference-extension-bound q r error d zero
  errorNonnegative qBound rBound differenceBound =
  let core = dyadicRadius (uniformSineStabilityCoreExponent d)
      zeroBound : MagnitudeBound 0 0
      zeroBound = record
        { positive-upper = isRefl≤ 0 ; negative-upper = isRefl≤ 0 }
      scaleZero = cong (Q._· error) (Q.·AnnihilR core) ∙
        Q.·AnnihilL error
  in subst (MagnitudeBound 0) (sym scaleZero) zeroBound
late-sine-partial-difference-extension-bound q r error d (suc count)
  errorNonnegative qBound rBound differenceBound =
  let core = dyadicRadius (uniformSineStabilityCoreExponent d)
      block = lateSinePartialDifferenceExtension q r d count
      term = sineTerm q (suc (dyadicNat (suc d) ℕ.+ count)) Q.+
        (Q.- sineTerm r (suc (dyadicNat (suc d) ℕ.+ count)))
      blockBound = late-sine-partial-difference-extension-bound
        q r error d count errorNonnegative qBound rBound differenceBound
      termRaw = late-sine-term-difference-bound
        q r error d (suc count) errorNonnegative qBound rBound differenceBound
      termBound = transport-magnitude _ _ _
        (cong (λ index → sineTerm q index Q.+ (Q.- sineTerm r index))
          (sym (ℕ.+-suc (dyadicNat (suc d)) count))) termRaw
      combined = add-magnitude-bounds _ _ _ _ blockBound termBound
      scalePath = SineLateDifferencePaths.combine-block-scale
        PreferredℚCommRing core (lateExtensionWeightSum count)
        (lateDifferenceWeight (suc count)) error
  in subst (MagnitudeBound (block Q.+ term)) scalePath combined

uniform-late-sine-partial-difference-extension-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound (lateSinePartialDifferenceExtension q r d count)
    (dyadicRadius (uniformSineStabilityExponent d) Q.· error)
uniform-late-sine-partial-difference-extension-bound q r error d count
  errorNonnegative qBound rBound differenceBound =
  let coreScale = dyadicRadius (uniformSineStabilityCoreExponent d) Q.·
        lateExtensionWeightSum count
      stabilityScale = dyadicRadius (uniformSineStabilityExponent d)
      raw = late-sine-partial-difference-extension-bound
        q r error d count errorNonnegative qBound rBound differenceBound
      scale≤ = ≤-·o coreScale stabilityScale error errorNonnegative
        (sine-stability-extension-weight-sum-scale≤radius d count)
  in weaken-magnitude-bound _ _ (stabilityScale Q.· error) scale≤ raw

lateSineAdvanceIndex : ℕ → ℕ → ℕ
lateSineAdvanceIndex cutoff zero = cutoff
lateSineAdvanceIndex cutoff (suc count) =
  suc (lateSineAdvanceIndex cutoff count)

lateSineAdvanceIndex-add : (cutoff count : ℕ) →
  lateSineAdvanceIndex cutoff count ≡ cutoff ℕ.+ count
lateSineAdvanceIndex-add cutoff zero = sym (ℕ.+-zero cutoff)
lateSineAdvanceIndex-add cutoff (suc count) =
  cong suc (lateSineAdvanceIndex-add cutoff count) ∙
  sym (ℕ.+-suc cutoff count)

late-sine-advance-term-path : (q r : Q.ℚ) (cutoff count : ℕ) →
  let index = lateSineAdvanceIndex cutoff count
  in
  (sineTerm q (suc index) Q.+ (Q.- sineTerm r (suc index))) ≡
  (sineTerm q (suc (cutoff ℕ.+ count)) Q.+
   (Q.- sineTerm r (suc (cutoff ℕ.+ count))))
late-sine-advance-term-path q r cutoff count =
  cong (λ index → sineTerm q index Q.+ (Q.- sineTerm r index))
    (cong suc (lateSineAdvanceIndex-add cutoff count))

late-sine-advance-difference-decomposition :
  (q r : Q.ℚ) (d count : ℕ) →
  (sinePartialSum q
      (lateSineAdvanceIndex (dyadicNat (suc d)) count) Q.+
   (Q.- sinePartialSum r
      (lateSineAdvanceIndex (dyadicNat (suc d)) count))) ≡
  ((sinePartialSum q (dyadicNat (suc d)) Q.+
    (Q.- sinePartialSum r (dyadicNat (suc d)))) Q.+
   lateSinePartialDifferenceExtension q r d count)
late-sine-advance-difference-decomposition q r d zero =
  sym (Q.+IdR
    (sinePartialSum q (dyadicNat (suc d)) Q.+
     (Q.- sinePartialSum r (dyadicNat (suc d)))))
late-sine-advance-difference-decomposition q r d (suc count) =
  let cutoff = dyadicNat (suc d)
      index = lateSineAdvanceIndex cutoff count
      cutoffDifference = sinePartialSum q cutoff Q.+
        (Q.- sinePartialSum r cutoff)
      extension = lateSinePartialDifferenceExtension q r d count
      term = sineTerm q (suc index) Q.+ (Q.- sineTerm r (suc index))
  in
  sine-partial-sum-difference-step q r index ∙
  cong (λ z → z Q.+ term)
    (late-sine-advance-difference-decomposition q r d count) ∙
  SineLateDifferencePaths.extend-reassociate PreferredℚCommRing
    cutoffDifference extension term ∙
  cong (λ z → cutoffDifference Q.+ (extension Q.+ z))
    (late-sine-advance-term-path q r cutoff count)

uniform-late-sine-advance-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (sinePartialSum q
       (lateSineAdvanceIndex (dyadicNat (suc d)) count) Q.+
     (Q.- sinePartialSum r
       (lateSineAdvanceIndex (dyadicNat (suc d)) count)))
    (dyadicRadius (uniformSineStabilityExponent d) Q.· error)
uniform-late-sine-advance-partial-sum-difference-bound
  q r error d count errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      core = dyadicRadius (uniformSineStabilityCoreExponent d)
      extensionWeight = lateExtensionWeightSum count
      cutoffDifference = sinePartialSum q cutoff Q.+
        (Q.- sinePartialSum r cutoff)
      extension = lateSinePartialDifferenceExtension q r d count
      cutoffRaw = sine-partial-sum-input-difference-bound
        q r error d cutoff errorNonnegative qBound rBound differenceBound
      cutoffScale≤core = dyadicRadius-monotone
        (sinePartialSumDifferenceExponent d cutoff)
        (uniformSineStabilityCoreExponent d) ℕOrder.left-≤-max
      cutoffScale≤coreTimesError = ≤-·o
        (dyadicRadius (sinePartialSumDifferenceExponent d cutoff)) core
        error errorNonnegative cutoffScale≤core
      cutoffBound = weaken-magnitude-bound cutoffDifference
        (dyadicRadius (sinePartialSumDifferenceExponent d cutoff) Q.· error)
        (core Q.· error) cutoffScale≤coreTimesError cutoffRaw
      extensionBound = late-sine-partial-difference-extension-bound
        q r error d count errorNonnegative qBound rBound differenceBound
      combined = add-magnitude-bounds cutoffDifference (core Q.· error)
        extension ((core Q.· extensionWeight) Q.· error)
        cutoffBound extensionBound
      scalePath = SineLateDifferencePaths.combine-initial-extension-scale
        PreferredℚCommRing core extensionWeight error
      factored = subst (MagnitudeBound (cutoffDifference Q.+ extension))
        scalePath combined
      combinedScale≤ = ≤-·o
        (core Q.+ (core Q.· extensionWeight))
        (dyadicRadius (uniformSineStabilityExponent d))
        error errorNonnegative
        (sine-stability-dominates-initial-plus-extension d count)
      weakened = weaken-magnitude-bound (cutoffDifference Q.+ extension)
        ((core Q.+ (core Q.· extensionWeight)) Q.· error)
        (dyadicRadius (uniformSineStabilityExponent d) Q.· error)
        combinedScale≤ factored
  in
  transport-magnitude _ _ _
    (late-sine-advance-difference-decomposition q r d count) weakened

lateSineAdvanceIndex-to-later : (cutoff truncation : ℕ) →
  ℕOrder._≤_ cutoff truncation →
  lateSineAdvanceIndex cutoff (truncation ∸ cutoff) ≡ truncation
lateSineAdvanceIndex-to-later cutoff truncation cutoff≤truncation =
  lateSineAdvanceIndex-add cutoff (truncation ∸ cutoff) ∙
  +-comm cutoff (truncation ∸ cutoff) ∙
  ℕOrder.≤-∸-+-cancel cutoff≤truncation

uniform-later-sine-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  ℕOrder._≤_ (dyadicNat (suc d)) truncation →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (sinePartialSum q truncation Q.+
     (Q.- sinePartialSum r truncation))
    (dyadicRadius (uniformSineStabilityExponent d) Q.· error)
uniform-later-sine-partial-sum-difference-bound
  q r error d truncation cutoff≤truncation
  errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      count = truncation ∸ cutoff
      indexPath = lateSineAdvanceIndex-to-later
        cutoff truncation cutoff≤truncation
      raw = uniform-late-sine-advance-partial-sum-difference-bound
        q r error d count errorNonnegative qBound rBound differenceBound
  in
  transport-magnitude _ _ _
    (cong (λ index → sinePartialSum q index Q.+
      (Q.- sinePartialSum r index)) (sym indexPath)) raw

uniform-early-sine-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  ℕOrder._≤_ truncation (dyadicNat (suc d)) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (sinePartialSum q truncation Q.+
     (Q.- sinePartialSum r truncation))
    (dyadicRadius (uniformSineStabilityExponent d) Q.· error)
uniform-early-sine-partial-sum-difference-bound
  q r error d truncation truncation≤cutoff
  errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      truncationExponent = sinePartialSumDifferenceExponent d truncation
      stabilityExponent = uniformSineStabilityExponent d
      raw = sine-partial-sum-input-difference-bound
        q r error d truncation errorNonnegative qBound rBound differenceBound
      exponent≤base = sinePartialSumDifferenceExponent-monotone d
        truncation cutoff truncation≤cutoff
      exponent≤stability = ℕOrder.≤-trans exponent≤base
        (ℕOrder.≤-trans ℕOrder.left-≤-max
          (ℕOrder.≤-trans ℕOrder.≤-sucℕ
            (ℕOrder.≤-trans ℕOrder.≤-sucℕ ℕOrder.≤-sucℕ)))
      scale≤ = ≤-·o (dyadicRadius truncationExponent)
        (dyadicRadius stabilityExponent) error errorNonnegative
        (dyadicRadius-monotone truncationExponent stabilityExponent
          exponent≤stability)
  in
  weaken-magnitude-bound _ _
    (dyadicRadius stabilityExponent Q.· error) scale≤ raw

uniform-sine-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (sinePartialSum q truncation Q.+
     (Q.- sinePartialSum r truncation))
    (dyadicRadius (uniformSineStabilityExponent d) Q.· error)
uniform-sine-partial-sum-difference-bound q r error d truncation
  errorNonnegative qBound rBound differenceBound
  with ℕOrder.splitℕ-≤ (dyadicNat (suc d)) truncation
... | inl cutoff≤truncation =
  uniform-later-sine-partial-sum-difference-bound
    q r error d truncation cutoff≤truncation
    errorNonnegative qBound rBound differenceBound
... | inr truncation<cutoff =
  uniform-early-sine-partial-sum-difference-bound
    q r error d truncation (ℕOrder.<-weaken truncation<cutoff)
    errorNonnegative qBound rBound differenceBound

operationalUniformSinePartialSumInputStability :
  UniformSinePartialSumInputStability
operationalUniformSinePartialSumInputStability = record
  { uniformSineDifferenceExponent = uniformSineStabilityExponent
  ; uniformSinePartialSumDifference =
      uniform-sine-partial-sum-difference-bound
  }

late-sine-propagated-regroup :
  (q difference : Q.ℚ) (n : ℕ) →
  let firstInverse = reciprocalSuccessor (firstSineDenominator n)
      secondInverse = reciprocalSuccessor (secondSineDenominator n)
  in
  Q.- (((((difference Q.· q) Q.· q) Q.· firstInverse) Q.· secondInverse)) ≡
  Q.- ((difference Q.· (q Q.· firstInverse)) Q.·
    (q Q.· secondInverse))
late-sine-propagated-regroup q difference n =
  SineLateDifferencePaths.propagated-regroup PreferredℚCommRing
    difference q (reciprocalSuccessor (firstSineDenominator n))
    (reciprocalSuccessor (secondSineDenominator n))

late-sine-fresh-left-regroup :
  (q term difference : Q.ℚ) (n : ℕ) →
  Q.- (((((term Q.· difference) Q.· q) Q.·
    reciprocalSuccessor (firstSineDenominator n)) Q.·
    reciprocalSuccessor (secondSineDenominator n))) ≡
  Q.- ((((term Q.· (q Q.· reciprocalSuccessor
    (secondSineDenominator n))) Q.· difference) Q.·
    reciprocalSuccessor (firstSineDenominator n)))
late-sine-fresh-left-regroup q term difference n =
  SineLateDifferencePaths.fresh-left-regroup PreferredℚCommRing
    term difference q (reciprocalSuccessor (firstSineDenominator n))
    (reciprocalSuccessor (secondSineDenominator n))

late-sine-fresh-right-regroup :
  (r term difference : Q.ℚ) (n : ℕ) →
  Q.- (((((term Q.· r) Q.· difference) Q.·
    reciprocalSuccessor (firstSineDenominator n)) Q.·
    reciprocalSuccessor (secondSineDenominator n))) ≡
  Q.- ((((term Q.· (r Q.· reciprocalSuccessor
    (firstSineDenominator n))) Q.· difference) Q.·
    reciprocalSuccessor (secondSineDenominator n)))
late-sine-fresh-right-regroup r term difference n =
  SineLateDifferencePaths.fresh-right-regroup PreferredℚCommRing
    term r difference (reciprocalSuccessor (firstSineDenominator n))
    (reciprocalSuccessor (secondSineDenominator n))
