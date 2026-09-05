{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CosineSeedCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyShift
open import RationalTaylorApproximants
open import CosineTailSchedule

cosineSeedOffset : {q : Q.ℚ} → CosineTailSeed q → ℕ
cosineSeedOffset seed = baseCosineCutoff seed ℕ.+ seedExponent seed

absorbed-cosine-cutoff-as-offset : {q : Q.ℚ} →
  (seed : CosineTailSeed q) (n : ℕ) →
  absorbedCosineCutoff seed n ≡ cosineSeedOffset seed ℕ.+ n
absorbed-cosine-cutoff-as-offset seed n =
  ℕ.+-assoc (baseCosineCutoff seed) (seedExponent seed) n

later-cosine-partial-sum-alignment : {q : Q.ℚ} →
  (first second : CosineTailSeed q) →
  ℕOrder._≤_ (cosineSeedOffset first) (cosineSeedOffset second) →
  Σ[ delta ∈ ℕ ] ((n : ℕ) →
    absorbedCosinePartialSum first (n ℕ.+ delta) ≡
    absorbedCosinePartialSum second n)
later-cosine-partial-sum-alignment {q} first second
  (delta , delta+first≡second) =
  delta , λ n → cong (cosinePartialSum q)
    (absorbed-cosine-cutoff-as-offset first (n ℕ.+ delta) ∙
     cong (λ z → cosineSeedOffset first ℕ.+ z) (ℕ.+-comm n delta) ∙
     ℕ.+-assoc (cosineSeedOffset first) delta n ∙
     cong (λ z → z ℕ.+ n)
       (ℕ.+-comm (cosineSeedOffset first) delta ∙
        delta+first≡second) ∙
     sym (absorbed-cosine-cutoff-as-offset second n))

ordered-cosine-seed-shift-path : {q : Q.ℚ} →
  (first second : CosineTailSeed q) →
  (offsetOrder : ℕOrder._≤_
    (cosineSeedOffset first) (cosineSeedOffset second)) →
  let delta = fst (later-cosine-partial-sum-alignment
                    first second offsetOrder)
  in
  iterateShift delta (absorbedCosineRegular first) ≡
  absorbedCosineRegular second
ordered-cosine-seed-shift-path first second offsetOrder =
  let alignment = later-cosine-partial-sum-alignment
                    first second offsetOrder
      delta = fst alignment
      valuesAlign = snd alignment
  in
  regularCauchy-ext
    (iterateShift delta (absorbedCosineRegular first))
    (absorbedCosineRegular second)
    (funExt λ n →
      iterateShift-approximation delta n (absorbedCosineRegular first) ∙
      cong (absorbedCosinePartialSum first) (ℕ.+-comm delta n) ∙
      valuesAlign n)

ordered-cosine-seeds-metric-equivalent : {q : Q.ℚ} →
  (first second : CosineTailSeed q) →
  ℕOrder._≤_ (cosineSeedOffset first) (cosineSeedOffset second) →
  absorbedCosineRegular first ≈metric absorbedCosineRegular second
ordered-cosine-seeds-metric-equivalent first second offsetOrder =
  let alignment = later-cosine-partial-sum-alignment
                    first second offsetOrder
      delta = fst alignment
      shiftPath = ordered-cosine-seed-shift-path first second offsetOrder
  in
  subst (absorbedCosineRegular first ≈metric_)
    shiftPath
    (≈metric-sym
      (iterateShift delta (absorbedCosineRegular first))
      (absorbedCosineRegular first)
      (iterateShift-equivalent delta (absorbedCosineRegular first)))

cosine-seeds-metric-equivalent : {q : Q.ℚ} →
  (first second : CosineTailSeed q) →
  absorbedCosineRegular first ≈metric absorbedCosineRegular second
cosine-seeds-metric-equivalent first second =
  ℕOrder.≤CaseInduction
    {P = λ _ _ → absorbedCosineRegular first ≈metric
      absorbedCosineRegular second}
    {n = cosineSeedOffset first} {m = cosineSeedOffset second}
    (ordered-cosine-seeds-metric-equivalent first second)
    (λ second≤first → ≈metric-sym
      (absorbedCosineRegular second) (absorbedCosineRegular first)
      (ordered-cosine-seeds-metric-equivalent second first second≤first))
