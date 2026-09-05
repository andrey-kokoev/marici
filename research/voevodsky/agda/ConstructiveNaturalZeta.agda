{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ConstructiveNaturalZeta where

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

record NaturalZetaExponent : Type where
  field
    exponent : ℕ
    exponentAtLeastTwo : ℕOrder._≤_ 2 exponent
open NaturalZetaExponent public

naturalZetaApproximation : NaturalZetaExponent → ℕ → Q.ℚ
naturalZetaApproximation input stage =
  rationalZetaPartialSum (exponent input) (dyadicReciprocalIndex stage)

module NaturalZetaPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  extension-difference : (a tail : fst R) →
    (a +S tail) +S (-S a) ≡ tail
  extension-difference a tail = solve! R

natural-zeta-ordered-difference : (input : NaturalZetaExponent) →
  (m n : ℕ) → ℕOrder._≤_ m n →
  MagnitudeBound
    (naturalZetaApproximation input n Q.+
      (Q.- naturalZetaApproximation input m))
    (precision m)
natural-zeta-ordered-difference input m n m≤n =
  let p = exponent input
      cutoffM = dyadicReciprocalIndex m
      cutoffN = dyadicReciprocalIndex n
      cutoff≤ = dyadic-reciprocal-index-monotone m n m≤n
      extra = fst cutoff≤
      cutoffPath : cutoffM ℕ.+ extra ≡ cutoffN
      cutoffPath = ℕ.+-comm cutoffM extra ∙ snd cutoff≤
      extension : naturalZetaApproximation input n ≡
        naturalZetaApproximation input m Q.+
          rationalDirichletTail p cutoffM extra
      extension = cong (rationalZetaPartialSum p) (sym cutoffPath) ∙
        rational-zeta-partial-sum-extension p cutoffM extra
      differencePath :
        naturalZetaApproximation input n Q.+
          (Q.- naturalZetaApproximation input m) ≡
        rationalDirichletTail p cutoffM extra
      differencePath =
        cong (Q._+ (Q.- naturalZetaApproximation input m)) extension ∙
        NaturalZetaPaths.extension-difference PreferredℚCommRing
          (naturalZetaApproximation input m)
          (rationalDirichletTail p cutoffM extra)
      tailMagnitude : MagnitudeBound
        (rationalDirichletTail p cutoffM extra) (precision m)
      tailMagnitude = nonnegative-value-magnitude
        (rationalDirichletTail p cutoffM extra) (precision m)
        (rational-dirichlet-tail-nonnegative p cutoffM extra)
        (rational-higher-dyadic-tail-bound p m extra
          (exponentAtLeastTwo input))
        (precision-nonnegative m)
  in subst (λ value → MagnitudeBound value (precision m))
    (sym differencePath) tailMagnitude

naturalZetaRegular : NaturalZetaExponent → RegularCauchy
naturalZetaRegular input =
  regular-from-ordered-differences (naturalZetaApproximation input)
    (natural-zeta-ordered-difference input)
