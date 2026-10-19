{-# OPTIONS --safe --cubical --guardedness #-}
module TickCompletionPositivePart where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels
open import Cubical.Data.Nat using (ℕ; zero)
open import Cubical.HITs.PropositionalTruncation as PT
import Cubical.HITs.SetQuotients as SQ
open import Cubical.HITs.SetQuotients.Properties using (setQuotUnaryOp)
open import Cubical.Data.Rationals as Q hiding (_+_; _·_; -_)
open import Cubical.Data.Rationals.Order
open import Cubical.Relation.Nullary using (yes; no)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyNegation using (-completion_; negateRegular)
open import CauchyCompletionAbGroup using (zeroCompletion)
open import TickCompletionMetric
open import TickCompletionDerivative using (CompletionNonnegative)
open import TickCompletionLimits
open import TickCompletionPositiveProduct using
  (positivePart; positivePart-nonnegative; positive-approximant; positive-approximants-converge; nonnegative-representative)

module Algebra (R : CommRing ℓ-zero) where
  open CommRingStr (snd R)
  abstract
    shift-left : (q e : fst R) → (- e) + (q + e) ≡ q
    shift-left q e = solve! R
    shift-right : (q e : fst R) → (- q) + (q + e) ≡ e
    shift-right q e = solve! R
module QR = Algebra PreferredℚCommRing

rational-below-positivePart : (q : Q.ℚ) → q ≤ positivePart q
rational-below-positivePart q with <Dec q 0
... | yes negative = <Weaken≤ q 0 negative
... | no _ = isRefl≤ q

positivePart-upper : (q b : Q.ℚ) → q ≤ b → 0 ≤ b → positivePart q ≤ b
positivePart-upper q b bound positive with <Dec q 0
... | yes _ = positive
... | no _ = bound

positivePart-directed : (q r e : Q.ℚ) → 0 ≤ e → q ≤ r Q.+ e → positivePart q ≤ positivePart r Q.+ e
positivePart-directed q r e positive bound = positivePart-upper q (positivePart r Q.+ e)
  (isTrans≤ q (r Q.+ e) (positivePart r Q.+ e) bound
    (≤-+o r (positivePart r) e (rational-below-positivePart r)))
  (isTrans≤ 0 (positivePart r) (positivePart r Q.+ e) (positivePart-nonnegative r)
    (≤-add-nonnegative (positivePart r) e positive))

positiveRegular : RegularCauchy → RegularCauchy
positiveRegular x .approximation n = positivePart (approximation x n)
positiveRegular x .close-forward m n = subst (positivePart (approximation x m) ≤_)
  (Q.+Assoc (positivePart (approximation x n)) (precision m) (precision n))
  (positivePart-directed (approximation x m) (approximation x n) (precision m Q.+ precision n)
    (≤Monotone+ 0 (precision m) 0 (precision n) (precision-nonnegative m) (precision-nonnegative n))
    (subst (approximation x m ≤_) (sym (Q.+Assoc (approximation x n) (precision m) (precision n))) (close-forward x m n)))
positiveRegular x .close-backward m n = subst (positivePart (approximation x n) ≤_)
  (Q.+Assoc (positivePart (approximation x m)) (precision m) (precision n))
  (positivePart-directed (approximation x n) (approximation x m) (precision m Q.+ precision n)
    (≤Monotone+ 0 (precision m) 0 (precision n) (precision-nonnegative m) (precision-nonnegative n))
    (subst (approximation x n ≤_) (sym (Q.+Assoc (approximation x m) (precision m) (precision n))) (close-backward x m n)))

positiveRegular-eventual : (x y : RegularCauchy) (k : ℕ) → EventuallyWithin x y k → EventuallyWithin (positiveRegular x) (positiveRegular y) k
positiveRegular-eventual x y k = PT.map λ { (threshold , bounds) → threshold , λ n hn →
  positivePart-directed (approximation x n) (approximation y n) (precision k) (precision-nonnegative k) (fst (bounds n hn)) ,
  positivePart-directed (approximation y n) (approximation x n) (precision k) (precision-nonnegative k) (snd (bounds n hn)) }

positiveRegular-cong : (x y : RegularCauchy) → x ≈metric y → positiveRegular x ≈metric positiveRegular y
positiveRegular-cong x y equivalent k = positiveRegular-eventual x y k (equivalent k)

positiveCompletion : MetricCompletionCandidate → MetricCompletionCandidate
positiveCompletion = setQuotUnaryOp positiveRegular positiveRegular-cong

positive-local : LocallyContinuous positiveRegular
positive-local .localModulus x k = k
positive-local .localPreserves = positiveRegular-eventual

abstract
  positive-metric-continuous : MetricContinuous positiveCompletion
  positive-metric-continuous = lift-local-continuity positiveRegular positiveCompletion (λ x → refl) positive-local

  positive-fixes-nonnegative : (a : MetricCompletionCandidate) → CompletionNonnegative a → positiveCompletion a ≡ a
  positive-fixes-nonnegative = SQ.elimProp (λ a → isPropΠ λ _ → metric-candidate-isSet (positiveCompletion a) a)
    (λ x positive → close-limits-equal (rational-approximants (positiveRegular x)) (rational-approximants (positiveRegular x))
      SQ.[ positiveRegular x ] SQ.[ x ] (rational-approximants-converge (positiveRegular x))
      (positive-approximants-converge x positive)
      (pointwise-close (rational-approximants (positiveRegular x)) (rational-approximants (positiveRegular x)) (λ n → refl)))

  positive-vanishes-nonpositive : (a : MetricCompletionCandidate) → CompletionNonnegative (-completion a) → positiveCompletion a ≡ zeroCompletion
  positive-vanishes-nonpositive = SQ.elimProp (λ a → isPropΠ λ _ → metric-candidate-isSet (positiveCompletion a) zeroCompletion)
    (λ x negative → SQ.eq/ (positiveRegular x) (constantCauchy 0) (λ k → PT.map
      (λ { (threshold , lower) → threshold , λ n hn →
        subst (positivePart (approximation x n) ≤_) (sym (Q.+IdL (precision k)))
          (positivePart-upper (approximation x n) (precision k)
            (subst2 _≤_ (QR.shift-left (approximation x n) (precision k)) (QR.shift-right (approximation x n) (precision k))
              (≤-+o (Q.- precision k) (Q.- approximation x n) (approximation x n Q.+ precision k) (lower n hn)))
            (precision-nonnegative k)) ,
        isTrans≤ 0 (positivePart (approximation x n)) (positivePart (approximation x n) Q.+ precision k)
          (positivePart-nonnegative (approximation x n))
          (≤-add-nonnegative (positivePart (approximation x n)) (precision k) (precision-nonnegative k)) })
      (nonnegative-representative (negateRegular x) negative k)))
