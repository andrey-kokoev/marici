{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformCosineLateDifference where

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
open import CosineTermBounds
open import CosineTailSchedule
open import CosineInputDifference
open import CosinePartialSumInputDifference
open import UniformCosineSeedBounds
open import UniformCosineStabilityScale
open import UniformCosineInputStabilityContract
open import UniformExponentialDifferenceWeights

module CosineLateDifferencePaths {ℓ} (R : CommRing ℓ) where
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

late-cosine-propagated-difference-bound :
  (q difference error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound difference
    ((dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
      lateDifferenceWeight extra) Q.· error) →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (Q.- (((((difference Q.· q) Q.· q) Q.·
      reciprocalSuccessor (firstCosineDenominator index)) Q.·
      reciprocalSuccessor (secondCosineDenominator index))))
    ((dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
      (lateDifferenceWeight extra Q.· one-half)) Q.· error)
late-cosine-propagated-difference-bound q difference error d extra
  errorNonnegative qBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      core = dyadicRadius (uniformCosineStabilityCoreExponent d)
      weight = lateDifferenceWeight extra
      scale = (core Q.· weight) Q.· error
      scaleNonnegative = nonnegative-bound-product (core Q.· weight) error
        (nonnegative-bound-product core weight
          (dyadicRadius-nonnegative (uniformCosineStabilityCoreExponent d))
          (late-difference-weight-nonnegative extra)) errorNonnegative
      firstFactor = q Q.· reciprocalSuccessor (firstCosineDenominator index)
      secondFactor = q Q.· reciprocalSuccessor (secondCosineDenominator index)
      firstBound = late-cosine-first-factor-magnitude≤half q d extra qBound
      secondHalf = late-cosine-second-factor-magnitude≤half q d extra qBound
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
      valuePath = CosineLateDifferencePaths.propagated-regroup
        PreferredℚCommRing difference q
        (reciprocalSuccessor (firstCosineDenominator index))
        (reciprocalSuccessor (secondCosineDenominator index))
      scalePath = CosineLateDifferencePaths.propagated-bound-scale
        PreferredℚCommRing core weight error one-half
  in
  subst (MagnitudeBound
    (Q.- (((((difference Q.· q) Q.· q) Q.·
      reciprocalSuccessor (firstCosineDenominator index)) Q.·
      reciprocalSuccessor (secondCosineDenominator index)))))
    scalePath
    (transport-magnitude _ _ _ valuePath negated)

late-cosine-fresh-left-difference-bound :
  (q r error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (Q.- (((((cosineTerm r index Q.· (q Q.+ (Q.- r))) Q.· q) Q.·
      reciprocalSuccessor (firstCosineDenominator index)) Q.·
      reciprocalSuccessor (secondCosineDenominator index))))
    ((dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
      (precision extra Q.· one-half)) Q.· error)
late-cosine-fresh-left-difference-bound q r error d extra
  errorNonnegative qBound rBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      seedExponent = uniformCosineSeedExponent d
      coreExponent = uniformCosineStabilityCoreExponent d
      seedScale = dyadicRadius seedExponent Q.· precision extra
      coreScale = dyadicRadius coreExponent Q.· precision extra
      seed = uniformCosineTailSeed r d rBound
      termRaw = shifted-cosine-term-geometric-decay seed extra
      seed≤core = dyadicRadius-monotone seedExponent coreExponent
        ℕOrder.right-≤-max
      seedScale≤coreScale = ≤-·o (dyadicRadius seedExponent)
        (dyadicRadius coreExponent) (precision extra)
        (precision-nonnegative extra) seed≤core
      termBound = weaken-magnitude-bound (cosineTerm r index)
        seedScale coreScale seedScale≤coreScale termRaw
      contractedFactor = q Q.· reciprocalSuccessor
        (secondCosineDenominator index)
      contractedFactorBound =
        late-cosine-second-factor-magnitude≤half q d extra qBound
      firstProduct = arbitrary-multiplier-bound
        (cosineTerm r index) coreScale contractedFactor one-half
        (nonnegative-bound-product (dyadicRadius coreExponent)
          (precision extra) (dyadicRadius-nonnegative coreExponent)
          (precision-nonnegative extra))
        one-half-nonnegative termBound contractedFactorBound
      firstScaleNonnegative = nonnegative-bound-product coreScale one-half
        (nonnegative-bound-product (dyadicRadius coreExponent)
          (precision extra) (dyadicRadius-nonnegative coreExponent)
          (precision-nonnegative extra)) one-half-nonnegative
      withDifference = arbitrary-multiplier-bound
        (cosineTerm r index Q.· contractedFactor)
        (coreScale Q.· one-half) (q Q.+ (Q.- r)) error
        firstScaleNonnegative errorNonnegative firstProduct differenceBound
      differenceScaleNonnegative = nonnegative-bound-product
        (coreScale Q.· one-half) error firstScaleNonnegative errorNonnegative
      withReciprocal = arbitrary-multiplier-bound
        ((cosineTerm r index Q.· contractedFactor) Q.· (q Q.+ (Q.- r)))
        ((coreScale Q.· one-half) Q.· error)
        (reciprocalSuccessor (firstCosineDenominator index)) 1
        differenceScaleNonnegative (dyadicRadius-nonnegative 0)
        withDifference (reciprocal-magnitude≤one (firstCosineDenominator index))
      negated = negate-magnitude-bound _ _ withReciprocal
      valuePath = CosineLateDifferencePaths.fresh-left-regroup
        PreferredℚCommRing (cosineTerm r index) (q Q.+ (Q.- r)) q
        (reciprocalSuccessor (firstCosineDenominator index))
        (reciprocalSuccessor (secondCosineDenominator index))
      scalePath = CosineLateDifferencePaths.fresh-scale PreferredℚCommRing
        (dyadicRadius coreExponent) (precision extra) one-half error
  in
  subst (MagnitudeBound
    (Q.- (((((cosineTerm r index Q.· (q Q.+ (Q.- r))) Q.· q) Q.·
      reciprocalSuccessor (firstCosineDenominator index)) Q.·
      reciprocalSuccessor (secondCosineDenominator index)))))
    scalePath (transport-magnitude _ _ _ valuePath negated)

late-cosine-fresh-right-difference-bound :
  (q r error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (Q.- (((((cosineTerm r index Q.· r) Q.· (q Q.+ (Q.- r))) Q.·
      reciprocalSuccessor (firstCosineDenominator index)) Q.·
      reciprocalSuccessor (secondCosineDenominator index))))
    ((dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
      (precision extra Q.· one-half)) Q.· error)
late-cosine-fresh-right-difference-bound q r error d extra
  errorNonnegative qBound rBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      seedExponent = uniformCosineSeedExponent d
      coreExponent = uniformCosineStabilityCoreExponent d
      seedScale = dyadicRadius seedExponent Q.· precision extra
      coreScale = dyadicRadius coreExponent Q.· precision extra
      seed = uniformCosineTailSeed r d rBound
      termRaw = shifted-cosine-term-geometric-decay seed extra
      seed≤core = dyadicRadius-monotone seedExponent coreExponent
        ℕOrder.right-≤-max
      seedScale≤coreScale = ≤-·o (dyadicRadius seedExponent)
        (dyadicRadius coreExponent) (precision extra)
        (precision-nonnegative extra) seed≤core
      termBound = weaken-magnitude-bound (cosineTerm r index)
        seedScale coreScale seedScale≤coreScale termRaw
      contractedFactor = r Q.· reciprocalSuccessor
        (firstCosineDenominator index)
      contractedFactorBound =
        late-cosine-first-factor-magnitude≤half r d extra rBound
      firstProduct = arbitrary-multiplier-bound
        (cosineTerm r index) coreScale contractedFactor one-half
        (nonnegative-bound-product (dyadicRadius coreExponent)
          (precision extra) (dyadicRadius-nonnegative coreExponent)
          (precision-nonnegative extra))
        one-half-nonnegative termBound contractedFactorBound
      firstScaleNonnegative = nonnegative-bound-product coreScale one-half
        (nonnegative-bound-product (dyadicRadius coreExponent)
          (precision extra) (dyadicRadius-nonnegative coreExponent)
          (precision-nonnegative extra)) one-half-nonnegative
      withDifference = arbitrary-multiplier-bound
        (cosineTerm r index Q.· contractedFactor)
        (coreScale Q.· one-half) (q Q.+ (Q.- r)) error
        firstScaleNonnegative errorNonnegative firstProduct differenceBound
      differenceScaleNonnegative = nonnegative-bound-product
        (coreScale Q.· one-half) error firstScaleNonnegative errorNonnegative
      withReciprocal = arbitrary-multiplier-bound
        ((cosineTerm r index Q.· contractedFactor) Q.· (q Q.+ (Q.- r)))
        ((coreScale Q.· one-half) Q.· error)
        (reciprocalSuccessor (secondCosineDenominator index)) 1
        differenceScaleNonnegative (dyadicRadius-nonnegative 0)
        withDifference (reciprocal-magnitude≤one (secondCosineDenominator index))
      negated = negate-magnitude-bound _ _ withReciprocal
      valuePath = CosineLateDifferencePaths.fresh-right-regroup
        PreferredℚCommRing (cosineTerm r index) r (q Q.+ (Q.- r))
        (reciprocalSuccessor (firstCosineDenominator index))
        (reciprocalSuccessor (secondCosineDenominator index))
      scalePath = CosineLateDifferencePaths.fresh-scale PreferredℚCommRing
        (dyadicRadius coreExponent) (precision extra) one-half error
  in
  subst (MagnitudeBound
    (Q.- (((((cosineTerm r index Q.· r) Q.· (q Q.+ (Q.- r))) Q.·
      reciprocalSuccessor (firstCosineDenominator index)) Q.·
      reciprocalSuccessor (secondCosineDenominator index)))))
    scalePath (transport-magnitude _ _ _ valuePath negated)

late-cosine-term-difference-bound :
  (q r error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (cosineTerm q index Q.+ (Q.- cosineTerm r index))
    ((dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
      lateDifferenceWeight extra) Q.· error)
late-cosine-term-difference-bound q r error d zero errorNonnegative
  qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      raw = cosine-term-input-difference-bound q r error d cutoff
        errorNonnegative qBound rBound differenceBound
      exponent≤core : ℕOrder._≤_
        (cosineTermDifferenceExponent d cutoff)
        (uniformCosineStabilityCoreExponent d)
      exponent≤core = ℕOrder.≤-trans
        (term-difference-exponent≤cosine-partial-sum d cutoff)
        ℕOrder.left-≤-max
      scale≤ = ≤-·o
        (dyadicRadius (cosineTermDifferenceExponent d cutoff))
        (dyadicRadius (uniformCosineStabilityCoreExponent d))
        error errorNonnegative
        (dyadicRadius-monotone _ _ exponent≤core)
      weakened = weaken-magnitude-bound _ _ _ scale≤ raw
      reindexed = transport-magnitude _ _ _
        (cong (λ index → cosineTerm q index Q.+ (Q.- cosineTerm r index))
          (ℕ.+-zero cutoff)) weakened
      scalePath = cong (Q._· error)
        (Q.·IdR (dyadicRadius (uniformCosineStabilityCoreExponent d)))
  in subst (MagnitudeBound _) (sym scalePath) reindexed
late-cosine-term-difference-bound q r error d (suc extra)
  errorNonnegative qBound rBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      core = dyadicRadius (uniformCosineStabilityCoreExponent d)
      weight = lateDifferenceWeight extra
      p = precision extra
      previousDifference = cosineTerm q index Q.+ (Q.- cosineTerm r index)
      previous = late-cosine-term-difference-bound q r error d extra
        errorNonnegative qBound rBound differenceBound
      propagated = late-cosine-propagated-difference-bound
        q previousDifference error d extra errorNonnegative qBound previous
      freshLeft = late-cosine-fresh-left-difference-bound
        q r error d extra errorNonnegative qBound rBound differenceBound
      freshRight = late-cosine-fresh-right-difference-bound
        q r error d extra errorNonnegative qBound rBound differenceBound
      firstCombined = add-magnitude-bounds _ _ _ _ propagated freshLeft
      combined = add-magnitude-bounds _ _ _ _ firstCombined freshRight
      halfScalePath = CosineLateDifferencePaths.combine-three-half-scales
        PreferredℚCommRing core weight p one-half error
      collapseFreshHalves = cong
        (λ z → (core Q.· ((weight Q.· one-half) Q.+ z)) Q.· error)
        (half-double p)
      scaled = subst (MagnitudeBound _) (halfScalePath ∙ collapseFreshHalves)
        combined
      valuePath =
        cong (λ j → cosineTerm q j Q.+ (Q.- cosineTerm r j))
          (ℕ.+-suc (dyadicNat (suc d)) extra) ∙
        cosine-term-difference-step q r index
  in transport-magnitude _ _ _ valuePath scaled

lateCosinePartialDifferenceExtension :
  (q r : Q.ℚ) (d : ℕ) → ℕ → Q.ℚ
lateCosinePartialDifferenceExtension q r d zero = 0
lateCosinePartialDifferenceExtension q r d (suc n) =
  lateCosinePartialDifferenceExtension q r d n Q.+
  (cosineTerm q (suc (dyadicNat (suc d) ℕ.+ n)) Q.+
   (Q.- cosineTerm r (suc (dyadicNat (suc d) ℕ.+ n))))

late-cosine-partial-difference-extension-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound (lateCosinePartialDifferenceExtension q r d count)
    ((dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
      lateExtensionWeightSum count) Q.· error)
late-cosine-partial-difference-extension-bound q r error d zero
  errorNonnegative qBound rBound differenceBound =
  let core = dyadicRadius (uniformCosineStabilityCoreExponent d)
      zeroBound : MagnitudeBound 0 0
      zeroBound = record
        { positive-upper = isRefl≤ 0 ; negative-upper = isRefl≤ 0 }
      scaleZero = cong (Q._· error) (Q.·AnnihilR core) ∙
        Q.·AnnihilL error
  in subst (MagnitudeBound 0) (sym scaleZero) zeroBound
late-cosine-partial-difference-extension-bound q r error d (suc count)
  errorNonnegative qBound rBound differenceBound =
  let core = dyadicRadius (uniformCosineStabilityCoreExponent d)
      block = lateCosinePartialDifferenceExtension q r d count
      term = cosineTerm q (suc (dyadicNat (suc d) ℕ.+ count)) Q.+
        (Q.- cosineTerm r (suc (dyadicNat (suc d) ℕ.+ count)))
      blockBound = late-cosine-partial-difference-extension-bound
        q r error d count errorNonnegative qBound rBound differenceBound
      termRaw = late-cosine-term-difference-bound
        q r error d (suc count) errorNonnegative qBound rBound differenceBound
      termBound = transport-magnitude _ _ _
        (cong (λ index → cosineTerm q index Q.+ (Q.- cosineTerm r index))
          (sym (ℕ.+-suc (dyadicNat (suc d)) count))) termRaw
      combined = add-magnitude-bounds _ _ _ _ blockBound termBound
      scalePath = CosineLateDifferencePaths.combine-block-scale
        PreferredℚCommRing core (lateExtensionWeightSum count)
        (lateDifferenceWeight (suc count)) error
  in subst (MagnitudeBound (block Q.+ term)) scalePath combined

uniform-late-cosine-partial-difference-extension-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound (lateCosinePartialDifferenceExtension q r d count)
    (dyadicRadius (uniformCosineStabilityExponent d) Q.· error)
uniform-late-cosine-partial-difference-extension-bound q r error d count
  errorNonnegative qBound rBound differenceBound =
  let coreScale = dyadicRadius (uniformCosineStabilityCoreExponent d) Q.·
        lateExtensionWeightSum count
      stabilityScale = dyadicRadius (uniformCosineStabilityExponent d)
      raw = late-cosine-partial-difference-extension-bound
        q r error d count errorNonnegative qBound rBound differenceBound
      scale≤ = ≤-·o coreScale stabilityScale error errorNonnegative
        (cosine-stability-extension-weight-sum-scale≤radius d count)
  in weaken-magnitude-bound _ _ (stabilityScale Q.· error) scale≤ raw

lateCosineAdvanceIndex : ℕ → ℕ → ℕ
lateCosineAdvanceIndex cutoff zero = cutoff
lateCosineAdvanceIndex cutoff (suc count) =
  suc (lateCosineAdvanceIndex cutoff count)

lateCosineAdvanceIndex-add : (cutoff count : ℕ) →
  lateCosineAdvanceIndex cutoff count ≡ cutoff ℕ.+ count
lateCosineAdvanceIndex-add cutoff zero = sym (ℕ.+-zero cutoff)
lateCosineAdvanceIndex-add cutoff (suc count) =
  cong suc (lateCosineAdvanceIndex-add cutoff count) ∙
  sym (ℕ.+-suc cutoff count)

late-cosine-advance-term-path : (q r : Q.ℚ) (cutoff count : ℕ) →
  let index = lateCosineAdvanceIndex cutoff count
  in
  (cosineTerm q (suc index) Q.+ (Q.- cosineTerm r (suc index))) ≡
  (cosineTerm q (suc (cutoff ℕ.+ count)) Q.+
   (Q.- cosineTerm r (suc (cutoff ℕ.+ count))))
late-cosine-advance-term-path q r cutoff count =
  cong (λ index → cosineTerm q index Q.+ (Q.- cosineTerm r index))
    (cong suc (lateCosineAdvanceIndex-add cutoff count))

late-cosine-advance-difference-decomposition :
  (q r : Q.ℚ) (d count : ℕ) →
  (cosinePartialSum q
      (lateCosineAdvanceIndex (dyadicNat (suc d)) count) Q.+
   (Q.- cosinePartialSum r
      (lateCosineAdvanceIndex (dyadicNat (suc d)) count))) ≡
  ((cosinePartialSum q (dyadicNat (suc d)) Q.+
    (Q.- cosinePartialSum r (dyadicNat (suc d)))) Q.+
   lateCosinePartialDifferenceExtension q r d count)
late-cosine-advance-difference-decomposition q r d zero =
  sym (Q.+IdR
    (cosinePartialSum q (dyadicNat (suc d)) Q.+
     (Q.- cosinePartialSum r (dyadicNat (suc d)))))
late-cosine-advance-difference-decomposition q r d (suc count) =
  let cutoff = dyadicNat (suc d)
      index = lateCosineAdvanceIndex cutoff count
      cutoffDifference = cosinePartialSum q cutoff Q.+
        (Q.- cosinePartialSum r cutoff)
      extension = lateCosinePartialDifferenceExtension q r d count
      term = cosineTerm q (suc index) Q.+ (Q.- cosineTerm r (suc index))
  in
  cosine-partial-sum-difference-step q r index ∙
  cong (λ z → z Q.+ term)
    (late-cosine-advance-difference-decomposition q r d count) ∙
  CosineLateDifferencePaths.extend-reassociate PreferredℚCommRing
    cutoffDifference extension term ∙
  cong (λ z → cutoffDifference Q.+ (extension Q.+ z))
    (late-cosine-advance-term-path q r cutoff count)

uniform-late-cosine-advance-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (cosinePartialSum q
       (lateCosineAdvanceIndex (dyadicNat (suc d)) count) Q.+
     (Q.- cosinePartialSum r
       (lateCosineAdvanceIndex (dyadicNat (suc d)) count)))
    (dyadicRadius (uniformCosineStabilityExponent d) Q.· error)
uniform-late-cosine-advance-partial-sum-difference-bound
  q r error d count errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      core = dyadicRadius (uniformCosineStabilityCoreExponent d)
      extensionWeight = lateExtensionWeightSum count
      cutoffDifference = cosinePartialSum q cutoff Q.+
        (Q.- cosinePartialSum r cutoff)
      extension = lateCosinePartialDifferenceExtension q r d count
      cutoffRaw = cosine-partial-sum-input-difference-bound
        q r error d cutoff errorNonnegative qBound rBound differenceBound
      cutoffScale≤core = dyadicRadius-monotone
        (cosinePartialSumDifferenceExponent d cutoff)
        (uniformCosineStabilityCoreExponent d) ℕOrder.left-≤-max
      cutoffScale≤coreTimesError = ≤-·o
        (dyadicRadius (cosinePartialSumDifferenceExponent d cutoff)) core
        error errorNonnegative cutoffScale≤core
      cutoffBound = weaken-magnitude-bound cutoffDifference
        (dyadicRadius (cosinePartialSumDifferenceExponent d cutoff) Q.· error)
        (core Q.· error) cutoffScale≤coreTimesError cutoffRaw
      extensionBound = late-cosine-partial-difference-extension-bound
        q r error d count errorNonnegative qBound rBound differenceBound
      combined = add-magnitude-bounds cutoffDifference (core Q.· error)
        extension ((core Q.· extensionWeight) Q.· error)
        cutoffBound extensionBound
      scalePath = CosineLateDifferencePaths.combine-initial-extension-scale
        PreferredℚCommRing core extensionWeight error
      factored = subst (MagnitudeBound (cutoffDifference Q.+ extension))
        scalePath combined
      combinedScale≤ = ≤-·o
        (core Q.+ (core Q.· extensionWeight))
        (dyadicRadius (uniformCosineStabilityExponent d))
        error errorNonnegative
        (cosine-stability-dominates-initial-plus-extension d count)
      weakened = weaken-magnitude-bound (cutoffDifference Q.+ extension)
        ((core Q.+ (core Q.· extensionWeight)) Q.· error)
        (dyadicRadius (uniformCosineStabilityExponent d) Q.· error)
        combinedScale≤ factored
  in
  transport-magnitude _ _ _
    (late-cosine-advance-difference-decomposition q r d count) weakened

lateCosineAdvanceIndex-to-later : (cutoff truncation : ℕ) →
  ℕOrder._≤_ cutoff truncation →
  lateCosineAdvanceIndex cutoff (truncation ∸ cutoff) ≡ truncation
lateCosineAdvanceIndex-to-later cutoff truncation cutoff≤truncation =
  lateCosineAdvanceIndex-add cutoff (truncation ∸ cutoff) ∙
  +-comm cutoff (truncation ∸ cutoff) ∙
  ℕOrder.≤-∸-+-cancel cutoff≤truncation

uniform-later-cosine-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  ℕOrder._≤_ (dyadicNat (suc d)) truncation →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (cosinePartialSum q truncation Q.+
     (Q.- cosinePartialSum r truncation))
    (dyadicRadius (uniformCosineStabilityExponent d) Q.· error)
uniform-later-cosine-partial-sum-difference-bound
  q r error d truncation cutoff≤truncation
  errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      count = truncation ∸ cutoff
      indexPath = lateCosineAdvanceIndex-to-later
        cutoff truncation cutoff≤truncation
      raw = uniform-late-cosine-advance-partial-sum-difference-bound
        q r error d count errorNonnegative qBound rBound differenceBound
  in
  transport-magnitude _ _ _
    (cong (λ index → cosinePartialSum q index Q.+
      (Q.- cosinePartialSum r index)) (sym indexPath)) raw

uniform-early-cosine-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  ℕOrder._≤_ truncation (dyadicNat (suc d)) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (cosinePartialSum q truncation Q.+
     (Q.- cosinePartialSum r truncation))
    (dyadicRadius (uniformCosineStabilityExponent d) Q.· error)
uniform-early-cosine-partial-sum-difference-bound
  q r error d truncation truncation≤cutoff
  errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      truncationExponent = cosinePartialSumDifferenceExponent d truncation
      stabilityExponent = uniformCosineStabilityExponent d
      raw = cosine-partial-sum-input-difference-bound
        q r error d truncation errorNonnegative qBound rBound differenceBound
      exponent≤base = cosinePartialSumDifferenceExponent-monotone d
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

uniform-cosine-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (cosinePartialSum q truncation Q.+
     (Q.- cosinePartialSum r truncation))
    (dyadicRadius (uniformCosineStabilityExponent d) Q.· error)
uniform-cosine-partial-sum-difference-bound q r error d truncation
  errorNonnegative qBound rBound differenceBound
  with ℕOrder.splitℕ-≤ (dyadicNat (suc d)) truncation
... | inl cutoff≤truncation =
  uniform-later-cosine-partial-sum-difference-bound
    q r error d truncation cutoff≤truncation
    errorNonnegative qBound rBound differenceBound
... | inr truncation<cutoff =
  uniform-early-cosine-partial-sum-difference-bound
    q r error d truncation (ℕOrder.<-weaken truncation<cutoff)
    errorNonnegative qBound rBound differenceBound

operationalUniformCosinePartialSumInputStability :
  UniformCosinePartialSumInputStability
operationalUniformCosinePartialSumInputStability = record
  { uniformCosineDifferenceExponent = uniformCosineStabilityExponent
  ; uniformCosinePartialSumDifference =
      uniform-cosine-partial-sum-difference-bound
  }

late-cosine-propagated-regroup :
  (q difference : Q.ℚ) (n : ℕ) →
  let firstInverse = reciprocalSuccessor (firstCosineDenominator n)
      secondInverse = reciprocalSuccessor (secondCosineDenominator n)
  in
  Q.- (((((difference Q.· q) Q.· q) Q.· firstInverse) Q.· secondInverse)) ≡
  Q.- ((difference Q.· (q Q.· firstInverse)) Q.·
    (q Q.· secondInverse))
late-cosine-propagated-regroup q difference n =
  CosineLateDifferencePaths.propagated-regroup PreferredℚCommRing
    difference q (reciprocalSuccessor (firstCosineDenominator n))
    (reciprocalSuccessor (secondCosineDenominator n))

late-cosine-fresh-left-regroup :
  (q term difference : Q.ℚ) (n : ℕ) →
  Q.- (((((term Q.· difference) Q.· q) Q.·
    reciprocalSuccessor (firstCosineDenominator n)) Q.·
    reciprocalSuccessor (secondCosineDenominator n))) ≡
  Q.- ((((term Q.· (q Q.· reciprocalSuccessor
    (secondCosineDenominator n))) Q.· difference) Q.·
    reciprocalSuccessor (firstCosineDenominator n)))
late-cosine-fresh-left-regroup q term difference n =
  CosineLateDifferencePaths.fresh-left-regroup PreferredℚCommRing
    term difference q (reciprocalSuccessor (firstCosineDenominator n))
    (reciprocalSuccessor (secondCosineDenominator n))

late-cosine-fresh-right-regroup :
  (r term difference : Q.ℚ) (n : ℕ) →
  Q.- (((((term Q.· r) Q.· difference) Q.·
    reciprocalSuccessor (firstCosineDenominator n)) Q.·
    reciprocalSuccessor (secondCosineDenominator n))) ≡
  Q.- ((((term Q.· (r Q.· reciprocalSuccessor
    (firstCosineDenominator n))) Q.· difference) Q.·
    reciprocalSuccessor (secondCosineDenominator n)))
late-cosine-fresh-right-regroup r term difference n =
  CosineLateDifferencePaths.fresh-right-regroup PreferredℚCommRing
    term r difference (reciprocalSuccessor (firstCosineDenominator n))
    (reciprocalSuccessor (secondCosineDenominator n))
