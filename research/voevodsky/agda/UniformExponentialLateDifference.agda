{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformExponentialLateDifference where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_; _∸_; +-zero; +-comm)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Sum
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import DyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import TaylorTermBounds
open import TaylorUniformSeedBounds
open import ExponentialTailSchedule
open import TaylorInputDifference
open import TaylorPartialSumInputDifference
open import TaylorScheduleMonotonicity
open import UniformTaylorInputStabilityContract
open import UniformExponentialStabilityScale
open import UniformExponentialDifferenceWeights

initial-late-term-difference-bound :
  (q r error : Q.ℚ) (d : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (exponentialTerm q (dyadicNat (suc d)) Q.+
     (Q.- exponentialTerm r (dyadicNat (suc d))))
    (dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.· error)
initial-late-term-difference-bound q r error d errorNonnegative
  qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      raw = exponential-term-input-difference-bound
        q r error d cutoff errorNonnegative qBound rBound differenceBound
      scale≤ = ≤-·o
        (dyadicRadius (termDifferenceExponent d cutoff))
        (dyadicRadius (uniformExponentialStabilityCoreExponent d))
        error errorNonnegative
        (initial-term-difference-scale≤stability-core d)
  in
  weaken-magnitude-bound _ _
    (dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.· error)
    scale≤ raw

module LateDifferencePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  fresh-reassociate : (term difference reciprocal : fst R) →
    (term ·S difference) ·S reciprocal ≡
    (term ·S reciprocal) ·S difference
  fresh-reassociate term difference reciprocal = solve! R

  propagated-reassociate : (difference q reciprocal : fst R) →
    difference ·S (q ·S reciprocal) ≡
    (difference ·S q) ·S reciprocal
  propagated-reassociate difference q reciprocal = solve! R

  propagated-scale : (core weight error half : fst R) →
    ((core ·S weight) ·S error) ·S half ≡
    (core ·S (weight ·S half)) ·S error
  propagated-scale core weight error half = solve! R

  combine-recurrence-scale : (core weight half precision error : fst R) →
    ((core ·S (weight ·S half)) ·S error) +S
      ((core ·S precision) ·S error) ≡
    (core ·S ((weight ·S half) +S precision)) ·S error
  combine-recurrence-scale core weight half precision error = solve! R

  combine-recurrence-value : (difference q term fresh reciprocal : fst R) →
    ((difference ·S q) +S (term ·S fresh)) ·S reciprocal ≡
    ((difference ·S q) ·S reciprocal) +S
      ((term ·S fresh) ·S reciprocal)
  combine-recurrence-value difference q term fresh reciprocal = solve! R

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

late-fresh-difference-bound :
  (q r error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    ((exponentialTerm r index Q.· (q Q.+ (Q.- r))) Q.·
      reciprocalSuccessor index)
    ((dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
      precision extra) Q.· error)
late-fresh-difference-bound q r error d extra errorNonnegative
  rBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      seed = uniformExponentialTailSeed r d rBound
      termBound = exponential-tail-bound-before-absorption seed extra
      seed≤core = dyadicRadius-monotone
        (uniformExponentialSeedExponent d)
        (uniformExponentialStabilityCoreExponent d)
        ℕOrder.right-≤-max
      scaled≤ = ≤-·o
        (dyadicRadius (uniformExponentialSeedExponent d))
        (dyadicRadius (uniformExponentialStabilityCoreExponent d))
        (precision extra) (precision-nonnegative extra) seed≤core
      coreTermBound = weaken-magnitude-bound _ _
        (dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
          precision extra) scaled≤ termBound
      reciprocalBound = reciprocal-magnitude≤one index
      contractedRaw = arbitrary-multiplier-bound
        (exponentialTerm r index)
        (dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
          precision extra)
        (reciprocalSuccessor index) 1
        (nonnegative-bound-product
          (dyadicRadius (uniformExponentialStabilityCoreExponent d))
          (precision extra)
          (dyadicRadius-nonnegative
            (uniformExponentialStabilityCoreExponent d))
          (precision-nonnegative extra))
        (dyadicRadius-nonnegative 0) coreTermBound reciprocalBound
      contracted = subst
        (MagnitudeBound
          (exponentialTerm r index Q.· reciprocalSuccessor index))
        (Q.·IdR
          (dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
            precision extra))
        contractedRaw
      multiplied = arbitrary-multiplier-bound
        (exponentialTerm r index Q.· reciprocalSuccessor index)
        (dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
          precision extra)
        (q Q.+ (Q.- r)) error
        (nonnegative-bound-product
          (dyadicRadius (uniformExponentialStabilityCoreExponent d))
          (precision extra)
          (dyadicRadius-nonnegative
            (uniformExponentialStabilityCoreExponent d))
          (precision-nonnegative extra))
        errorNonnegative contracted differenceBound
  in
  transport-magnitude _ _ _
    (LateDifferencePaths.fresh-reassociate PreferredℚCommRing
      (exponentialTerm r index) (q Q.+ (Q.- r))
      (reciprocalSuccessor index))
    multiplied

late-propagated-difference-bound :
  (q difference error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound difference
    ((dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
      lateDifferenceWeight extra) Q.· error) →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    ((difference Q.· q) Q.· reciprocalSuccessor index)
    ((dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
      (lateDifferenceWeight extra Q.· one-half)) Q.· error)
late-propagated-difference-bound q difference error d extra errorNonnegative
  qBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
      weight = lateDifferenceWeight extra
      differenceScale = (core Q.· weight) Q.· error
      scaleNonnegative = nonnegative-bound-product
        (core Q.· weight) error
        (nonnegative-bound-product core weight
          (dyadicRadius-nonnegative
            (uniformExponentialStabilityCoreExponent d))
          (late-difference-weight-nonnegative extra))
        errorNonnegative
      multiplierBound = later-scaled-input-magnitude≤half
        q d extra qBound
      raw = arbitrary-multiplier-bound
        difference differenceScale
        (q Q.· reciprocalSuccessor index) one-half
        scaleNonnegative one-half-nonnegative
        differenceBound multiplierBound
      valuePath = LateDifferencePaths.propagated-reassociate
        PreferredℚCommRing difference q (reciprocalSuccessor index)
      scalePath = LateDifferencePaths.propagated-scale
        PreferredℚCommRing core weight error one-half
  in
  subst (MagnitudeBound ((difference Q.· q) Q.· reciprocalSuccessor index))
    scalePath
    (transport-magnitude _ _ _ (sym valuePath) raw)

late-term-difference-bound :
  (q r error : Q.ℚ) (d extra : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  let index = dyadicNat (suc d) ℕ.+ extra
  in
  MagnitudeBound
    (exponentialTerm q index Q.+ (Q.- exponentialTerm r index))
    ((dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
      lateDifferenceWeight extra) Q.· error)
late-term-difference-bound q r error d zero errorNonnegative
  qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
      targetValue = exponentialTerm q (cutoff ℕ.+ zero) Q.+
        (Q.- exponentialTerm r (cutoff ℕ.+ zero))
      raw = initial-late-term-difference-bound q r error d errorNonnegative
        qBound rBound differenceBound
      moved = transport-magnitude _ _ _
        (cong (λ j → exponentialTerm q j Q.+ (Q.- exponentialTerm r j))
          (+-zero cutoff)) raw
      scalePath = cong (Q._· error) (Q.·IdR core)
  in
  subst (MagnitudeBound targetValue) (sym scalePath) moved
late-term-difference-bound q r error d (suc extra) errorNonnegative
  qBound rBound differenceBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      currentDifference = exponentialTerm q index Q.+
        (Q.- exponentialTerm r index)
      propagatedValue = (currentDifference Q.· q) Q.· reciprocalSuccessor index
      freshValue = (exponentialTerm r index Q.· (q Q.+ (Q.- r))) Q.·
        reciprocalSuccessor index
      propagated = late-propagated-difference-bound
        q currentDifference error d extra errorNonnegative qBound
        (late-term-difference-bound q r error d extra errorNonnegative
          qBound rBound differenceBound)
      fresh = late-fresh-difference-bound q r error d extra
        errorNonnegative rBound differenceBound
      combined = add-magnitude-bounds _ _ _ _ propagated fresh
      combinedAligned = transport-magnitude _ _ _
        (LateDifferencePaths.combine-recurrence-value PreferredℚCommRing
          currentDifference q (exponentialTerm r index)
          (q Q.+ (Q.- r)) (reciprocalSuccessor index))
        combined
      scalePath = LateDifferencePaths.combine-recurrence-scale
        PreferredℚCommRing
        (dyadicRadius (uniformExponentialStabilityCoreExponent d))
        (lateDifferenceWeight extra) one-half (precision extra) error
      valuePath =
        cong (λ j → exponentialTerm q j Q.+ (Q.- exponentialTerm r j))
          (ℕ.+-suc (dyadicNat (suc d)) extra) ∙
        exponential-term-difference-step q r index
  in
  subst
    (MagnitudeBound
      (exponentialTerm q (dyadicNat (suc d) ℕ.+ suc extra) Q.+
       (Q.- exponentialTerm r (dyadicNat (suc d) ℕ.+ suc extra))))
    scalePath
    (transport-magnitude _ _ _ valuePath combinedAligned)

lateDifferenceBlock : (q r : Q.ℚ) (d : ℕ) → ℕ → Q.ℚ
lateDifferenceBlock q r d zero = 0
lateDifferenceBlock q r d (suc n) =
  lateDifferenceBlock q r d n Q.+
  (exponentialTerm q (dyadicNat (suc d) ℕ.+ n) Q.+
   (Q.- exponentialTerm r (dyadicNat (suc d) ℕ.+ n)))

late-difference-block-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound (lateDifferenceBlock q r d count)
    ((dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
      lateDifferenceWeightSum count) Q.· error)
late-difference-block-bound q r error d zero errorNonnegative
  qBound rBound differenceBound =
  let core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
      zeroBound : MagnitudeBound 0 0
      zeroBound = record { positive-upper = isRefl≤ 0 ; negative-upper = isRefl≤ 0 }
      scaleZero : (core Q.· 0) Q.· error ≡ 0
      scaleZero = cong (Q._· error) (Q.·AnnihilR core) ∙
        Q.·AnnihilL error
  in subst (MagnitudeBound 0) (sym scaleZero) zeroBound
late-difference-block-bound q r error d (suc count) errorNonnegative
  qBound rBound differenceBound =
  let core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
      block = lateDifferenceBlock q r d count
      term = exponentialTerm q (dyadicNat (suc d) ℕ.+ count) Q.+
        (Q.- exponentialTerm r (dyadicNat (suc d) ℕ.+ count))
      blockBound = late-difference-block-bound q r error d count
        errorNonnegative qBound rBound differenceBound
      termBound = late-term-difference-bound q r error d count
        errorNonnegative qBound rBound differenceBound
      combined = add-magnitude-bounds _ _ _ _ blockBound termBound
      scalePath = LateDifferencePaths.combine-block-scale PreferredℚCommRing
        core (lateDifferenceWeightSum count)
        (lateDifferenceWeight count) error
  in
  subst (MagnitudeBound (block Q.+ term)) scalePath combined

latePartialDifferenceExtension : (q r : Q.ℚ) (d : ℕ) → ℕ → Q.ℚ
latePartialDifferenceExtension q r d zero = 0
latePartialDifferenceExtension q r d (suc n) =
  latePartialDifferenceExtension q r d n Q.+
  (exponentialTerm q (suc (dyadicNat (suc d) ℕ.+ n)) Q.+
   (Q.- exponentialTerm r (suc (dyadicNat (suc d) ℕ.+ n))))

late-partial-difference-extension-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound (latePartialDifferenceExtension q r d count)
    ((dyadicRadius (uniformExponentialStabilityCoreExponent d) Q.·
      lateExtensionWeightSum count) Q.· error)
late-partial-difference-extension-bound q r error d zero errorNonnegative
  qBound rBound differenceBound =
  let core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
      zeroBound : MagnitudeBound 0 0
      zeroBound = record { positive-upper = isRefl≤ 0 ; negative-upper = isRefl≤ 0 }
      scaleZero = cong (Q._· error) (Q.·AnnihilR core) ∙ Q.·AnnihilL error
  in subst (MagnitudeBound 0) (sym scaleZero) zeroBound
late-partial-difference-extension-bound q r error d (suc count)
  errorNonnegative qBound rBound differenceBound =
  let core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
      block = latePartialDifferenceExtension q r d count
      term = exponentialTerm q (suc (dyadicNat (suc d) ℕ.+ count)) Q.+
        (Q.- exponentialTerm r (suc (dyadicNat (suc d) ℕ.+ count)))
      blockBound = late-partial-difference-extension-bound
        q r error d count errorNonnegative qBound rBound differenceBound
      termBoundRaw = late-term-difference-bound q r error d (suc count)
        errorNonnegative qBound rBound differenceBound
      termBound = transport-magnitude _ _ _
        (cong₂ (λ qTerm rTerm → qTerm Q.+ (Q.- rTerm))
          (cong (exponentialTerm q)
            (sym (ℕ.+-suc (dyadicNat (suc d)) count)))
          (cong (exponentialTerm r)
            (sym (ℕ.+-suc (dyadicNat (suc d)) count))))
        termBoundRaw
      combined = add-magnitude-bounds _ _ _ _ blockBound termBound
      scalePath = LateDifferencePaths.combine-block-scale PreferredℚCommRing
        core (lateExtensionWeightSum count)
        (lateDifferenceWeight (suc count)) error
  in subst (MagnitudeBound (block Q.+ term)) scalePath combined

uniform-late-partial-difference-extension-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound (latePartialDifferenceExtension q r d count)
    (dyadicRadius (uniformExponentialStabilityExponent d) Q.· error)
uniform-late-partial-difference-extension-bound q r error d count
  errorNonnegative qBound rBound differenceBound =
  let coreScale = dyadicRadius
        (uniformExponentialStabilityCoreExponent d) Q.·
        lateExtensionWeightSum count
      stabilityScale = dyadicRadius (uniformExponentialStabilityExponent d)
      raw = late-partial-difference-extension-bound q r error d count
        errorNonnegative qBound rBound differenceBound
      scaled≤ = ≤-·o coreScale stabilityScale error errorNonnegative
        (stability-extension-weight-sum-scale≤radius d count)
  in weaken-magnitude-bound _ _ (stabilityScale Q.· error) scaled≤ raw

lateAdvanceIndex : ℕ → ℕ → ℕ
lateAdvanceIndex cutoff zero = cutoff
lateAdvanceIndex cutoff (suc count) = suc (lateAdvanceIndex cutoff count)

lateAdvanceIndex-add : (cutoff count : ℕ) →
  lateAdvanceIndex cutoff count ≡ cutoff ℕ.+ count
lateAdvanceIndex-add cutoff zero = sym (+-zero cutoff)
lateAdvanceIndex-add cutoff (suc count) =
  cong suc (lateAdvanceIndex-add cutoff count) ∙
  sym (ℕ.+-suc cutoff count)

late-advance-term-path : (q r : Q.ℚ) (cutoff count : ℕ) →
  let index = lateAdvanceIndex cutoff count
  in
  (exponentialTerm q (suc index) Q.+
   (Q.- exponentialTerm r (suc index))) ≡
  (exponentialTerm q (suc (cutoff ℕ.+ count)) Q.+
   (Q.- exponentialTerm r (suc (cutoff ℕ.+ count))))
late-advance-term-path q r cutoff count =
  cong (λ index → exponentialTerm q index Q.+
    (Q.- exponentialTerm r index))
    (cong suc (lateAdvanceIndex-add cutoff count))

late-advance-difference-decomposition :
  (q r : Q.ℚ) (d count : ℕ) →
  (exponentialPartialSum q
      (lateAdvanceIndex (dyadicNat (suc d)) count) Q.+
   (Q.- exponentialPartialSum r
      (lateAdvanceIndex (dyadicNat (suc d)) count))) ≡
  ((exponentialPartialSum q (dyadicNat (suc d)) Q.+
    (Q.- exponentialPartialSum r (dyadicNat (suc d)))) Q.+
   latePartialDifferenceExtension q r d count)
late-advance-difference-decomposition q r d zero =
  sym (Q.+IdR
    (exponentialPartialSum q (dyadicNat (suc d)) Q.+
     (Q.- exponentialPartialSum r (dyadicNat (suc d)))))
late-advance-difference-decomposition q r d (suc count) =
  let cutoff = dyadicNat (suc d)
      index = lateAdvanceIndex cutoff count
      cutoffDifference = exponentialPartialSum q cutoff Q.+
        (Q.- exponentialPartialSum r cutoff)
      extension = latePartialDifferenceExtension q r d count
      term = exponentialTerm q (suc index) Q.+
        (Q.- exponentialTerm r (suc index))
  in
  exponential-partial-sum-difference-step q r index ∙
  cong (λ z → z Q.+ term)
    (late-advance-difference-decomposition q r d count) ∙
  LateDifferencePaths.extend-reassociate PreferredℚCommRing
    cutoffDifference extension term ∙
  cong (λ z → cutoffDifference Q.+ (extension Q.+ z))
    (late-advance-term-path q r cutoff count)

uniform-late-advance-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (exponentialPartialSum q
       (lateAdvanceIndex (dyadicNat (suc d)) count) Q.+
     (Q.- exponentialPartialSum r
       (lateAdvanceIndex (dyadicNat (suc d)) count)))
    (dyadicRadius (uniformExponentialStabilityExponent d) Q.· error)
uniform-late-advance-partial-sum-difference-bound q r error d count
  errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      core = dyadicRadius (uniformExponentialStabilityCoreExponent d)
      extensionWeight = lateExtensionWeightSum count
      cutoffDifference = exponentialPartialSum q cutoff Q.+
        (Q.- exponentialPartialSum r cutoff)
      extension = latePartialDifferenceExtension q r d count
      cutoffRaw = exponential-partial-sum-input-difference-bound
        q r error d cutoff errorNonnegative qBound rBound differenceBound
      cutoffScale≤core = dyadicRadius-monotone
        (partialSumDifferenceExponent d cutoff)
        (uniformExponentialStabilityCoreExponent d)
        ℕOrder.left-≤-max
      cutoffScale≤coreTimesError = ≤-·o
        (dyadicRadius (partialSumDifferenceExponent d cutoff)) core
        error errorNonnegative cutoffScale≤core
      cutoffBound = weaken-magnitude-bound cutoffDifference
        (dyadicRadius (partialSumDifferenceExponent d cutoff) Q.· error)
        (core Q.· error) cutoffScale≤coreTimesError cutoffRaw
      extensionBound = late-partial-difference-extension-bound
        q r error d count errorNonnegative qBound rBound differenceBound
      combined = add-magnitude-bounds cutoffDifference (core Q.· error)
        extension ((core Q.· extensionWeight) Q.· error)
        cutoffBound extensionBound
      scalePath = LateDifferencePaths.combine-initial-extension-scale
        PreferredℚCommRing core extensionWeight error
      factored = subst (MagnitudeBound (cutoffDifference Q.+ extension))
        scalePath combined
      combinedScale≤ = ≤-·o
        (core Q.+ (core Q.· extensionWeight))
        (dyadicRadius (uniformExponentialStabilityExponent d))
        error errorNonnegative
        (uniform-stability-dominates-initial-plus-extension d count)
      weakened = weaken-magnitude-bound (cutoffDifference Q.+ extension)
        ((core Q.+ (core Q.· extensionWeight)) Q.· error)
        (dyadicRadius (uniformExponentialStabilityExponent d) Q.· error)
        combinedScale≤ factored
  in
  transport-magnitude _ _ _
    (late-advance-difference-decomposition q r d count) weakened

lateAdvanceIndex-to-later : (cutoff truncation : ℕ) →
  ℕOrder._≤_ cutoff truncation →
  lateAdvanceIndex cutoff (truncation ∸ cutoff) ≡ truncation
lateAdvanceIndex-to-later cutoff truncation cutoff≤truncation =
  lateAdvanceIndex-add cutoff (truncation ∸ cutoff) ∙
  +-comm cutoff (truncation ∸ cutoff) ∙
  ℕOrder.≤-∸-+-cancel cutoff≤truncation

uniform-later-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  ℕOrder._≤_ (dyadicNat (suc d)) truncation →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (exponentialPartialSum q truncation Q.+
     (Q.- exponentialPartialSum r truncation))
    (dyadicRadius (uniformExponentialStabilityExponent d) Q.· error)
uniform-later-partial-sum-difference-bound q r error d truncation
  cutoff≤truncation errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      count = truncation ∸ cutoff
      indexPath = lateAdvanceIndex-to-later cutoff truncation cutoff≤truncation
      raw = uniform-late-advance-partial-sum-difference-bound
        q r error d count errorNonnegative qBound rBound differenceBound
  in
  transport-magnitude _ _ _
    (cong (λ index → exponentialPartialSum q index Q.+
      (Q.- exponentialPartialSum r index)) (sym indexPath))
    raw

uniform-early-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  ℕOrder._≤_ truncation (dyadicNat (suc d)) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (exponentialPartialSum q truncation Q.+
     (Q.- exponentialPartialSum r truncation))
    (dyadicRadius (uniformExponentialStabilityExponent d) Q.· error)
uniform-early-partial-sum-difference-bound q r error d truncation
  truncation≤cutoff errorNonnegative qBound rBound differenceBound =
  let cutoff = dyadicNat (suc d)
      truncationExponent = partialSumDifferenceExponent d truncation
      stabilityExponent = uniformExponentialStabilityExponent d
      raw = exponential-partial-sum-input-difference-bound
        q r error d truncation errorNonnegative qBound rBound differenceBound
      exponent≤base = partialSumDifferenceExponent-monotone d
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

uniform-exponential-partial-sum-difference-bound :
  (q r error : Q.ℚ) (d truncation : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound
    (exponentialPartialSum q truncation Q.+
     (Q.- exponentialPartialSum r truncation))
    (dyadicRadius (uniformExponentialStabilityExponent d) Q.· error)
uniform-exponential-partial-sum-difference-bound q r error d truncation
  errorNonnegative qBound rBound differenceBound
  with ℕOrder.splitℕ-≤ (dyadicNat (suc d)) truncation
... | inl cutoff≤truncation =
  uniform-later-partial-sum-difference-bound q r error d truncation
    cutoff≤truncation errorNonnegative qBound rBound differenceBound
... | inr truncation<cutoff =
  uniform-early-partial-sum-difference-bound q r error d truncation
    (ℕOrder.<-weaken truncation<cutoff)
    errorNonnegative qBound rBound differenceBound

operationalUniformExponentialPartialSumInputStability :
  UniformExponentialPartialSumInputStability
operationalUniformExponentialPartialSumInputStability = record
  { uniformExponentialDifferenceExponent =
      uniformExponentialStabilityExponent
  ; uniformExponentialPartialSumDifference =
      uniform-exponential-partial-sum-difference-bound
  }

uniform-late-difference-block-bound :
  (q r error : Q.ℚ) (d count : ℕ) →
  0 ≤ error →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound r (dyadicRadius d) →
  MagnitudeBound (q Q.+ (Q.- r)) error →
  MagnitudeBound (lateDifferenceBlock q r d count)
    (dyadicRadius (uniformExponentialStabilityExponent d) Q.· error)
uniform-late-difference-block-bound q r error d count errorNonnegative
  qBound rBound differenceBound =
  let coreScale = dyadicRadius
        (uniformExponentialStabilityCoreExponent d) Q.·
        lateDifferenceWeightSum count
      stabilityScale = dyadicRadius (uniformExponentialStabilityExponent d)
      raw = late-difference-block-bound q r error d count
        errorNonnegative qBound rBound differenceBound
      scaled≤ = ≤-·o coreScale stabilityScale error errorNonnegative
        (stability-weight-sum-scale≤radius d count)
  in
  weaken-magnitude-bound _ _ (stabilityScale Q.· error) scaled≤ raw
