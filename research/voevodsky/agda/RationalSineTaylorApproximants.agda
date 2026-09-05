{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalSineTaylorApproximants where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RationalTaylorApproximants

firstSineDenominator : ℕ → ℕ
firstSineDenominator n = suc (n ℕ.+ n)

secondSineDenominator : ℕ → ℕ
secondSineDenominator n = suc (firstSineDenominator n)

sineTerm : Q.ℚ → ℕ → Q.ℚ
sineTerm q zero = q
sineTerm q (suc n) =
  Q.- ((((sineTerm q n Q.· q) Q.· q) Q.·
    reciprocalSuccessor (firstSineDenominator n)) Q.·
    reciprocalSuccessor (secondSineDenominator n))

sinePartialSum : Q.ℚ → ℕ → Q.ℚ
sinePartialSum q = finiteSum (sineTerm q)

module SineZeroPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_·_ to _·S_; -_ to -S_)

  sine-zero-step : (a firstInverse secondInverse : fst R) →
    -S ((((a ·S 0r) ·S 0r) ·S firstInverse) ·S secondInverse) ≡ 0r
  sine-zero-step a firstInverse secondInverse = solve! R

sineTerm-at-zero : (n : ℕ) → sineTerm 0 n ≡ 0
sineTerm-at-zero zero = refl
sineTerm-at-zero (suc n) =
  SineZeroPaths.sine-zero-step PreferredℚCommRing
    (sineTerm 0 n)
    (reciprocalSuccessor (firstSineDenominator n))
    (reciprocalSuccessor (secondSineDenominator n))

finiteSum-all-zero : (term : ℕ → Q.ℚ) →
  ((n : ℕ) → term n ≡ 0) →
  (n : ℕ) → finiteSum term n ≡ 0
finiteSum-all-zero term allZero zero = allZero zero
finiteSum-all-zero term allZero (suc n) =
  cong₂ Q._+_ (finiteSum-all-zero term allZero n) (allZero (suc n)) ∙
  Q.+IdR 0

sinePartialSum-at-zero : (n : ℕ) → sinePartialSum 0 n ≡ 0
sinePartialSum-at-zero = finiteSum-all-zero (sineTerm 0) sineTerm-at-zero
