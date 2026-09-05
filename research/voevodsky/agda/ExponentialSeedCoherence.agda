{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ExponentialSeedCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyShift
open import CauchyMetricEquivalence
open import RationalTaylorApproximants
open import ExponentialTailSchedule

seedOffset : {q : Q.ℚ} → ExponentialTailSeed q → ℕ
seedOffset seed = baseTaylorCutoff seed ℕ.+ seedExponent seed

absorbed-cutoff-as-offset : {q : Q.ℚ} →
  (seed : ExponentialTailSeed q) (n : ℕ) →
  absorbedTaylorCutoff seed n ≡ seedOffset seed ℕ.+ n
absorbed-cutoff-as-offset seed n =
  ℕ.+-assoc (baseTaylorCutoff seed) (seedExponent seed) n

later-seed-cutoff-alignment : {q : Q.ℚ} →
  (first second : ExponentialTailSeed q) →
  ℕOrder._≤_ (seedOffset first) (seedOffset second) →
  Σ[ delta ∈ ℕ ] ((n : ℕ) →
    absorbedTaylorCutoff first (n ℕ.+ delta) ≡
    absorbedTaylorCutoff second n)
later-seed-cutoff-alignment first second (delta , delta+first≡second) =
  delta , λ n →
    absorbed-cutoff-as-offset first (n ℕ.+ delta) ∙
    cong (λ z → seedOffset first ℕ.+ z) (ℕ.+-comm n delta) ∙
    ℕ.+-assoc (seedOffset first) delta n ∙
    cong (λ z → z ℕ.+ n)
      (ℕ.+-comm (seedOffset first) delta ∙ delta+first≡second) ∙
    sym (absorbed-cutoff-as-offset second n)

later-seed-partial-sum-alignment : {q : Q.ℚ} →
  (first second : ExponentialTailSeed q) →
  ℕOrder._≤_ (seedOffset first) (seedOffset second) →
  Σ[ delta ∈ ℕ ] ((n : ℕ) →
    absorbedExponentialPartialSum first (n ℕ.+ delta) ≡
    absorbedExponentialPartialSum second n)
later-seed-partial-sum-alignment {q} first second offsetOrder =
  let alignment = later-seed-cutoff-alignment first second offsetOrder
  in
  fst alignment , λ n →
    cong (exponentialPartialSum q) (snd alignment n)

suc-index≤positive-shift : (n delta : ℕ) →
  ℕOrder._≤_ (ℕ.suc n) (n ℕ.+ ℕ.suc delta)
suc-index≤positive-shift n delta =
  delta ,
  ℕ.+-suc delta n ∙
  cong ℕ.suc (ℕ.+-comm delta n) ∙
  sym (ℕ.+-suc n delta)

positive-shift-error≤ : (k n delta : ℕ) →
  ℕOrder._≤_ (ℕ.suc k) n →
  precision n Q.+ precision (n ℕ.+ ℕ.suc delta) ≤ precision k
positive-shift-error≤ k n delta sk≤n =
  isTrans≤
    (precision n Q.+ precision (n ℕ.+ ℕ.suc delta))
    (precision n Q.+ precision (ℕ.suc n))
    (precision k)
    (≤Monotone+
      (precision n) (precision n)
      (precision (n ℕ.+ ℕ.suc delta)) (precision (ℕ.suc n))
      (isRefl≤ (precision n))
      (precision-antitone (ℕ.suc n) (n ℕ.+ ℕ.suc delta)
        (suc-index≤positive-shift n delta)))
    (shift-error≤ k n sk≤n)

ordered-seed-shift-path : {q : Q.ℚ} →
  (first second : ExponentialTailSeed q) →
  (offsetOrder : ℕOrder._≤_ (seedOffset first) (seedOffset second)) →
  let delta = fst (later-seed-partial-sum-alignment
                    first second offsetOrder)
  in
  iterateShift delta (absorbedExponentialRegular first) ≡
  absorbedExponentialRegular second
ordered-seed-shift-path first second offsetOrder =
  let alignment = later-seed-partial-sum-alignment
                    first second offsetOrder
      delta = fst alignment
      valuesAlign = snd alignment
  in
  regularCauchy-ext
    (iterateShift delta (absorbedExponentialRegular first))
    (absorbedExponentialRegular second)
    (funExt λ n →
      iterateShift-approximation delta n
        (absorbedExponentialRegular first) ∙
      cong (absorbedExponentialPartialSum first)
        (ℕ.+-comm delta n) ∙
      valuesAlign n)

ordered-seeds-metric-equivalent : {q : Q.ℚ} →
  (first second : ExponentialTailSeed q) →
  ℕOrder._≤_ (seedOffset first) (seedOffset second) →
  absorbedExponentialRegular first ≈metric
  absorbedExponentialRegular second
ordered-seeds-metric-equivalent first second offsetOrder =
  let alignment = later-seed-partial-sum-alignment
                    first second offsetOrder
      delta = fst alignment
      shiftPath = ordered-seed-shift-path first second offsetOrder
  in
  subst (absorbedExponentialRegular first ≈metric_)
    shiftPath
    (≈metric-sym
      (iterateShift delta (absorbedExponentialRegular first))
      (absorbedExponentialRegular first)
      (iterateShift-equivalent delta
        (absorbedExponentialRegular first)))

exponential-seeds-metric-equivalent : {q : Q.ℚ} →
  (first second : ExponentialTailSeed q) →
  absorbedExponentialRegular first ≈metric
  absorbedExponentialRegular second
exponential-seeds-metric-equivalent first second =
  ℕOrder.≤CaseInduction
    {P = λ _ _ → absorbedExponentialRegular first ≈metric
      absorbedExponentialRegular second}
    {n = seedOffset first} {m = seedOffset second}
    (ordered-seeds-metric-equivalent first second)
    (λ second≤first →
      ≈metric-sym
        (absorbedExponentialRegular second)
        (absorbedExponentialRegular first)
        (ordered-seeds-metric-equivalent second first second≤first))
