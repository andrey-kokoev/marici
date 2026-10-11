{-# OPTIONS --safe --cubical --guardedness #-}
module TickAtanDerivativeAlgebra where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Data.NatPlusOne as P using (ℕ₊₁; 1+_; ℕ₊₁→ℕ)
import Cubical.Data.NatPlusOne.Properties as PP
import Cubical.Data.Int as Z
import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Tactics.NatSolver using (solveℕ!)
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import DyadicallyBoundedCauchy using (natℚ; natℚ-representative)
open import RationalTaylorApproximants using (reciprocalSuccessor; finiteSum)
open import RationalLogTaylorApproximants using (atanhStepRatio; positiveNaturalLogRatio)
open import TickSmallArctangent using (atanTerm; atanPartialSum)

-- Positive rational normalization is reduced to symbolic natural-number
-- identities, rather than expanding large closed denominators.
positive-product : (a b : ℕ) (d e : ℕ₊₁) →
  Q.[ Z.pos a / d ] Q.· Q.[ Z.pos b / e ] ≡ Q.[ Z.pos (a N.· b) / d PP.·₊₁ e ]
positive-product a b d e = cong (λ z → Q.[ z / d PP.·₊₁ e ]) (sym (Z.pos·pos a b))

positive-fractions-equal : (a b : ℕ) (d e : ℕ₊₁) →
  a N.· ℕ₊₁→ℕ e ≡ b N.· ℕ₊₁→ℕ d → Q.[ Z.pos a / d ] ≡ Q.[ Z.pos b / e ]
positive-fractions-equal a b d e h = Q.eq/ _ _
  (sym (Z.pos·pos a (ℕ₊₁→ℕ e)) ∙ cong Z.pos h ∙ Z.pos·pos b (ℕ₊₁→ℕ d))

abstract
  reciprocal-ratio-step : (n : ℕ) →
    reciprocalSuccessor n Q.· positiveNaturalLogRatio (suc n) ≡ reciprocalSuccessor (suc (suc n))
  reciprocal-ratio-step n = positive-product 1 (suc n) (1+ n) (1+ suc (suc n))
    ∙ positive-fractions-equal (1 N.· suc n) 1 ((1+ n) PP.·₊₁ (1+ suc (suc n))) (1+ suc (suc n)) (solveℕ!)

  ratio-as-scaled-reciprocal : (n : ℕ) →
    positiveNaturalLogRatio (suc n) ≡ natℚ (suc n) Q.· reciprocalSuccessor (suc (suc n))
  ratio-as-scaled-reciprocal n = sym
    (cong (Q._· reciprocalSuccessor (suc (suc n))) (natℚ-representative (suc n))
      ∙ positive-product (suc n) 1 (1+ zero) (1+ suc (suc n))
      ∙ positive-fractions-equal (suc n N.· 1) (suc n) ((1+ zero) PP.·₊₁ (1+ suc (suc n))) (1+ suc (suc n)) (solveℕ!))

  successor-reciprocal-cancels : (n : ℕ) → natℚ (suc n) Q.· reciprocalSuccessor n ≡ Q.[ Z.pos 1 / 1+ zero ]
  successor-reciprocal-cancels n = cong (Q._· reciprocalSuccessor n) (natℚ-representative (suc n))
    ∙ positive-product (suc n) 1 (1+ zero) (1+ n)
    ∙ positive-fractions-equal (suc n N.· 1) 1 ((1+ zero) PP.·₊₁ (1+ n)) (1+ zero) (solveℕ!)

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  ratio-expand : (r a : fst R) → r · (1r + (a + a)) ≡ r + ((a · r) + (a · r))
  ratio-expand r a = solve! R
  ratio-collect : (m a : fst R) → m · a + (a + a) ≡ ((m + 1r) + 1r) · a
  ratio-collect m a = solve! R
  factor-step : (q g a r : fst R) → - ((((q · g) · a) · q) · q · r) ≡ (q · (- ((g · q) · q))) · (a · r)
  factor-step q g a r = solve! R
  factor-base : (q : fst R) → q ≡ (q · 1r) · 1r
  factor-base q = solve! R
  derivative-factor : (q g a r : fst R) → ((q · q) · g + ((q + q) · ((q · g) · a))) · r ≡
    ((q · q) · g) · (r · (1r + (a + a)))
  derivative-factor q g a r = solve! R
  geometric-base : (q : fst R) → (1r + q · q) · 1r ≡ 1r + (- (- ((1r · q) · q)))
  geometric-base q = solve! R
  geometric-step : (q s g : fst R) →
    (1r + q · q) · (s + g) ≡ ((1r + q · q) · s) + (g + (- (- ((g · q) · q))))
  geometric-step q s g = solve! R
  geometric-cancel : (g h : fst R) → (1r + (- g)) + (g + (- h)) ≡ 1r + (- h)
  geometric-cancel g h = solve! R
  term-remainder-step : (x y a b d r : fst R) →
    ((- (((b · y) · y) · r)) + (- (- (((a · x) · x) · r)))) +
      (- ((y + (- x)) · (- ((x · x · d + ((x + x) · a)) · r)))) ≡
    - (((y · y) · ((b + (- a)) + (- ((y + (- x)) · d))) +
      ((y + (- x)) · (y + (- x))) · (((x + y) · d) + a)) · r)
  term-remainder-step x y a b d r = solve! R
  zero-remainder : (x y : fst R) → (y + (- x)) + (- ((y + (- x)) · 1r)) ≡ 0r
  zero-remainder x y = solve! R

module R = Paths PreferredℚCommRing

geometricTerm : Q.ℚ → ℕ → Q.ℚ
geometricTerm q zero = Q.[ Z.pos 1 / 1+ zero ]
geometricTerm q (suc n) = Q.- ((geometricTerm q n Q.· q) Q.· q)
geometricSum : Q.ℚ → ℕ → Q.ℚ
geometricSum q = finiteSum (geometricTerm q)

abstract
  ratio-derivative-cancels : (n : ℕ) →
    atanhStepRatio n Q.· (Q.[ Z.pos 1 / 1+ zero ] Q.+ (reciprocalSuccessor (n N.+ n) Q.+ reciprocalSuccessor (n N.+ n))) ≡
    Q.[ Z.pos 1 / 1+ zero ]
  ratio-derivative-cancels n = R.ratio-expand (atanhStepRatio n) (reciprocalSuccessor (n N.+ n))
    ∙ cong₂ Q._+_ (ratio-as-scaled-reciprocal (n N.+ n))
      (cong₂ Q._+_ (reciprocal-ratio-step (n N.+ n)) (reciprocal-ratio-step (n N.+ n)))
    ∙ R.ratio-collect (natℚ (suc (n N.+ n))) (reciprocalSuccessor (suc (suc (n N.+ n))))
    ∙ successor-reciprocal-cancels (suc (suc (n N.+ n)))

  atan-term-factorization : (q : Q.ℚ) (n : ℕ) →
    atanTerm q n ≡ (q Q.· geometricTerm q n) Q.· reciprocalSuccessor (n N.+ n)
  atan-term-factorization q zero = R.factor-base q
  atan-term-factorization q (suc n) =
    cong (λ a → Q.- (((a Q.· q) Q.· q) Q.· atanhStepRatio n)) (atan-term-factorization q n)
    ∙ R.factor-step q (geometricTerm q n) (reciprocalSuccessor (n N.+ n)) (atanhStepRatio n)
    ∙ cong ((q Q.· geometricTerm q (suc n)) Q.·_) (reciprocal-ratio-step (n N.+ n))
    ∙ cong (λ k → (q Q.· geometricTerm q (suc n)) Q.· reciprocalSuccessor k) (sym (cong suc (N.+-suc n n)))

  atan-term-derivative-step : (q : Q.ℚ) (n : ℕ) →
    geometricTerm q (suc n) ≡
    Q.- (((q Q.· q) Q.· geometricTerm q n Q.+ ((q Q.+ q) Q.· atanTerm q n)) Q.· atanhStepRatio n)
  atan-term-derivative-step q n = sym
    (cong (λ a → Q.- (((q Q.· q) Q.· geometricTerm q n Q.+ ((q Q.+ q) Q.· a)) Q.· atanhStepRatio n))
      (atan-term-factorization q n)
      ∙ cong Q.-_ (R.derivative-factor q (geometricTerm q n) (reciprocalSuccessor (n N.+ n)) (atanhStepRatio n)
        ∙ cong (((q Q.· q) Q.· geometricTerm q n) Q.·_) (ratio-derivative-cancels n)
        ∙ Q.·IdR ((q Q.· q) Q.· geometricTerm q n)
        ∙ Q.·Comm (q Q.· q) (geometricTerm q n) ∙ Q.·Assoc (geometricTerm q n) q q))

  geometric-denominator-identity : (q : Q.ℚ) (n : ℕ) →
    (Q.[ Z.pos 1 / 1+ zero ] Q.+ q Q.· q) Q.· geometricSum q n ≡
    Q.[ Z.pos 1 / 1+ zero ] Q.+ (Q.- geometricTerm q (suc n))
  geometric-denominator-identity q zero = R.geometric-base q
  geometric-denominator-identity q (suc n) = R.geometric-step q (geometricSum q n) (geometricTerm q (suc n))
    ∙ cong (Q._+ (geometricTerm q (suc n) Q.+ (Q.- geometricTerm q (suc (suc n))))) (geometric-denominator-identity q n)
    ∙ R.geometric-cancel (geometricTerm q (suc n)) (geometricTerm q (suc (suc n)))

termRemainder : Q.ℚ → Q.ℚ → ℕ → Q.ℚ
termRemainder x y n = (atanTerm y n Q.+ (Q.- atanTerm x n)) Q.+ (Q.- ((y Q.+ (Q.- x)) Q.· geometricTerm x n))

abstract
  term-remainder-recurrence : (x y : Q.ℚ) (n : ℕ) → termRemainder x y (suc n) ≡
    Q.- (((y Q.· y) Q.· termRemainder x y n Q.+
      ((y Q.+ (Q.- x)) Q.· (y Q.+ (Q.- x))) Q.· (((x Q.+ y) Q.· geometricTerm x n) Q.+ atanTerm x n)) Q.· atanhStepRatio n)
  term-remainder-recurrence x y n =
    cong (λ d → (atanTerm y (suc n) Q.+ (Q.- atanTerm x (suc n))) Q.+ (Q.- ((y Q.+ (Q.- x)) Q.· d))) (atan-term-derivative-step x n)
    ∙ R.term-remainder-step x y (atanTerm x n) (atanTerm y n) (geometricTerm x n) (atanhStepRatio n)
