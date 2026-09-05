{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module SineSeedCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyShift
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
open import SineTailSchedule

sineSeedOffset : {q : Q.ℚ} → SineTailSeed q → ℕ
sineSeedOffset seed = baseSineCutoff seed ℕ.+ seedExponent seed

absorbed-sine-cutoff-as-offset : {q : Q.ℚ} →
  (seed : SineTailSeed q) (n : ℕ) →
  absorbedSineCutoff seed n ≡ sineSeedOffset seed ℕ.+ n
absorbed-sine-cutoff-as-offset seed n =
  ℕ.+-assoc (baseSineCutoff seed) (seedExponent seed) n

later-sine-partial-sum-alignment : {q : Q.ℚ} →
  (first second : SineTailSeed q) →
  ℕOrder._≤_ (sineSeedOffset first) (sineSeedOffset second) →
  Σ[ delta ∈ ℕ ] ((n : ℕ) →
    absorbedSinePartialSum first (n ℕ.+ delta) ≡
    absorbedSinePartialSum second n)
later-sine-partial-sum-alignment {q} first second
  (delta , delta+first≡second) =
  delta , λ n → cong (sinePartialSum q)
    (absorbed-sine-cutoff-as-offset first (n ℕ.+ delta) ∙
     cong (λ z → sineSeedOffset first ℕ.+ z) (ℕ.+-comm n delta) ∙
     ℕ.+-assoc (sineSeedOffset first) delta n ∙
     cong (λ z → z ℕ.+ n)
       (ℕ.+-comm (sineSeedOffset first) delta ∙
        delta+first≡second) ∙
     sym (absorbed-sine-cutoff-as-offset second n))

ordered-sine-seed-shift-path : {q : Q.ℚ} →
  (first second : SineTailSeed q) →
  (offsetOrder : ℕOrder._≤_
    (sineSeedOffset first) (sineSeedOffset second)) →
  let delta = fst (later-sine-partial-sum-alignment
                    first second offsetOrder)
  in
  iterateShift delta (absorbedSineRegular first) ≡
  absorbedSineRegular second
ordered-sine-seed-shift-path first second offsetOrder =
  let alignment = later-sine-partial-sum-alignment
                    first second offsetOrder
      delta = fst alignment
      valuesAlign = snd alignment
  in
  regularCauchy-ext
    (iterateShift delta (absorbedSineRegular first))
    (absorbedSineRegular second)
    (funExt λ n →
      iterateShift-approximation delta n (absorbedSineRegular first) ∙
      cong (absorbedSinePartialSum first) (ℕ.+-comm delta n) ∙
      valuesAlign n)

ordered-sine-seeds-metric-equivalent : {q : Q.ℚ} →
  (first second : SineTailSeed q) →
  ℕOrder._≤_ (sineSeedOffset first) (sineSeedOffset second) →
  absorbedSineRegular first ≈metric absorbedSineRegular second
ordered-sine-seeds-metric-equivalent first second offsetOrder =
  let alignment = later-sine-partial-sum-alignment
                    first second offsetOrder
      delta = fst alignment
      shiftPath = ordered-sine-seed-shift-path first second offsetOrder
  in
  subst (absorbedSineRegular first ≈metric_)
    shiftPath
    (≈metric-sym
      (iterateShift delta (absorbedSineRegular first))
      (absorbedSineRegular first)
      (iterateShift-equivalent delta (absorbedSineRegular first)))

sine-seeds-metric-equivalent : {q : Q.ℚ} →
  (first second : SineTailSeed q) →
  absorbedSineRegular first ≈metric absorbedSineRegular second
sine-seeds-metric-equivalent first second =
  ℕOrder.≤CaseInduction
    {P = λ _ _ → absorbedSineRegular first ≈metric
      absorbedSineRegular second}
    {n = sineSeedOffset first} {m = sineSeedOffset second}
    (ordered-sine-seeds-metric-equivalent first second)
    (λ second≤first → ≈metric-sym
      (absorbedSineRegular second) (absorbedSineRegular first)
      (ordered-sine-seeds-metric-equivalent second first second≤first))
