{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ConstructiveZetaTwo where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-value-magnitude)
open import OrderedDifferenceRegularity
open import RationalLogConvergenceContract
open import RationalDirichletZeta

zetaTwoApproximation : ℕ → Q.ℚ
zetaTwoApproximation stage =
  rationalZetaPartialSum 2 (dyadicReciprocalIndex stage)

module ZetaTwoPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  extension-difference : (a tail : fst R) →
    (a +S tail) +S (-S a) ≡ tail
  extension-difference a tail = solve! R

zeta-two-ordered-difference : (m n : ℕ) → ℕOrder._≤_ m n →
  MagnitudeBound
    (zetaTwoApproximation n Q.+ (Q.- zetaTwoApproximation m))
    (precision m)
zeta-two-ordered-difference m n m≤n =
  let cutoffM = dyadicReciprocalIndex m
      cutoffN = dyadicReciprocalIndex n
      cutoff≤ = dyadic-reciprocal-index-monotone m n m≤n
      extra = fst cutoff≤
      cutoffPath : cutoffM ℕ.+ extra ≡ cutoffN
      cutoffPath = ℕ.+-comm cutoffM extra ∙ snd cutoff≤
      extension : zetaTwoApproximation n ≡
        zetaTwoApproximation m Q.+ rationalSquareTail cutoffM extra
      extension = cong (rationalZetaPartialSum 2) (sym cutoffPath) ∙
        rational-zeta-square-partial-sum-extension cutoffM extra
      differencePath :
        zetaTwoApproximation n Q.+ (Q.- zetaTwoApproximation m) ≡
        rationalSquareTail cutoffM extra
      differencePath = cong (Q._+ (Q.- zetaTwoApproximation m)) extension ∙
        ZetaTwoPaths.extension-difference PreferredℚCommRing
          (zetaTwoApproximation m) (rationalSquareTail cutoffM extra)
      tailMagnitude : MagnitudeBound
        (rationalSquareTail cutoffM extra) (precision m)
      tailMagnitude = nonnegative-value-magnitude
        (rationalSquareTail cutoffM extra) (precision m)
        (rational-square-tail-nonnegative cutoffM extra)
        (rational-square-dyadic-tail-bound m extra)
        (precision-nonnegative m)
  in subst (λ value → MagnitudeBound value (precision m))
    (sym differencePath) tailMagnitude

zetaTwoRegular : RegularCauchy
zetaTwoRegular =
  regular-from-ordered-differences zetaTwoApproximation
    zeta-two-ordered-difference
