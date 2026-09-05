{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalSineSymmetry where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants

module SineOddRingPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  term-step-odd : (a q firstInverse secondInverse : fst R) →
    -S (((((-S a) ·S (-S q)) ·S (-S q)) ·S firstInverse) ·S
      secondInverse) ≡
    -S (-S ((((a ·S q) ·S q) ·S firstInverse) ·S secondInverse))
  term-step-odd a q firstInverse secondInverse = solve! R

  sum-step-odd : (sum term : fst R) →
    (-S sum) +S (-S term) ≡ -S (sum +S term)
  sum-step-odd sum term = solve! R

sineTerm-odd : (q : Q.ℚ) (n : ℕ) →
  sineTerm (Q.- q) n ≡ Q.- sineTerm q n
sineTerm-odd q zero = refl
sineTerm-odd q (suc n) =
  cong
    (λ previous →
      Q.- ((((previous Q.· (Q.- q)) Q.· (Q.- q)) Q.·
        reciprocalSuccessor (firstSineDenominator n)) Q.·
        reciprocalSuccessor (secondSineDenominator n)))
    (sineTerm-odd q n) ∙
  SineOddRingPaths.term-step-odd PreferredℚCommRing
    (sineTerm q n) q
    (reciprocalSuccessor (firstSineDenominator n))
    (reciprocalSuccessor (secondSineDenominator n))

sinePartialSum-odd : (q : Q.ℚ) (n : ℕ) →
  sinePartialSum (Q.- q) n ≡ Q.- sinePartialSum q n
sinePartialSum-odd q zero = sineTerm-odd q zero
sinePartialSum-odd q (suc n) =
  cong₂ Q._+_
    (sinePartialSum-odd q n)
    (sineTerm-odd q (suc n)) ∙
  SineOddRingPaths.sum-step-odd PreferredℚCommRing
    (sinePartialSum q n) (sineTerm q (suc n))
