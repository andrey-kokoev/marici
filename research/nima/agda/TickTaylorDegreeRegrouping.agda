{-# OPTIONS --safe --cubical --guardedness #-}
module TickTaylorDegreeRegrouping where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
import Cubical.Data.Empty as Empty
open import Cubical.Algebra.CommRing
import TickTaylorProductExpansion as P

module Degrees {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  module F = P.FiniteProducts R
  open F using (sum; sum-cong; sum-add; interchange)

  -- Put a weight at its actual monomial degree, zero at other degrees.
  mass : ℕ → fst R → ℕ → fst R
  mass zero a zero = a
  mass zero a (suc k) = 0r
  mass (suc d) a zero = 0r
  mass (suc d) a (suc k) = mass d a k

  sum-head : (a : ℕ → fst R) (n : ℕ)
    → sum a (suc n) ≡ a zero + sum (λ k → a (suc k)) n
  sum-head a zero = refl
  sum-head a (suc n) = cong (_+ a (suc (suc n))) (sum-head a n)
    ∙ sym (+Assoc (a zero) (sum (λ k → a (suc k)) n) (a (suc (suc n))))

  zero-mass-total : (a : fst R) (n : ℕ) → sum (mass zero a) n ≡ a
  zero-mass-total a zero = refl
  zero-mass-total a (suc n) = cong (_+ 0r) (zero-mass-total a n) ∙ +IdR a

  mass-total : (d n : ℕ) (a : fst R) → NO._≤_ d n → sum (mass d a) n ≡ a
  mass-total zero n a h = zero-mass-total a n
  mass-total (suc d) zero a h = Empty.rec (NO.¬-<-zero h)
  mass-total (suc d) (suc n) a h = sum-head (mass (suc d) a) n
    ∙ cong (0r +_) (mass-total d n a (NO.pred-≤-pred h)) ∙ +IdL a

  bounded-sum-cong : (a b : ℕ → fst R) (n : ℕ)
    → ((k : ℕ) → NO._≤_ k n → a k ≡ b k) → sum a n ≡ sum b n
  bounded-sum-cong a b zero p = p zero NO.≤-refl
  bounded-sum-cong a b (suc n) p = cong₂ _+_
    (bounded-sum-cong a b n (λ k h → p k (NO.≤-trans {m = n} h NO.≤-sucℕ)))
    (p (suc n) NO.≤-refl)

  -- All weights, including factorial-normalization factors, are unchanged.
  regroup-grid : (weight : ℕ → ℕ → fst R) (degree : ℕ → ℕ → ℕ) (m n D : ℕ)
    → ((i j : ℕ) → NO._≤_ i m → NO._≤_ j n → NO._≤_ (degree i j) D)
    → sum (λ i → sum (weight i) n) m
      ≡ sum (λ k → sum (λ i → sum (λ j → mass (degree i j) (weight i j) k) n) m) D
  regroup-grid weight degree m n D bounded =
    bounded-sum-cong _ _ m (λ i hi → bounded-sum-cong _ _ n (λ j hj →
      sym (mass-total (degree i j) D (weight i j) (bounded i j hi hj))))
    ∙ sum-cong _ _ (λ i → interchange (λ j k → mass (degree i j) (weight i j) k) n D) m
    ∙ interchange (λ i k → sum (λ j → mass (degree i j) (weight i j) k) n) m D

import Cubical.Data.Rationals as Q
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using (cosinePartialSum)
open import RationalSineTaylorApproximants using (sinePartialSum)
module G = Degrees PreferredℚCommRing
module F = P.FiniteProducts PreferredℚCommRing

cosDegree sinDegree : ℕ → ℕ → ℕ
cosDegree i j = (i N.+ i) N.+ (j N.+ j)
sinDegree i j = suc (i N.+ i) N.+ suc (j N.+ j)
maxDegree : ℕ → ℕ
maxDegree n = suc (n N.+ n) N.+ suc (n N.+ n)

cos-degree-bound : (n i j : ℕ) → NO._≤_ i n → NO._≤_ j n → NO._≤_ (cosDegree i j) (maxDegree n)
cos-degree-bound n i j hi hj = NO.≤-+-≤
  (NO.≤-trans {m = n N.+ n} (NO.≤-+-≤ hi hi) NO.≤-sucℕ)
  (NO.≤-trans {m = n N.+ n} (NO.≤-+-≤ hj hj) NO.≤-sucℕ)
sin-degree-bound : (n i j : ℕ) → NO._≤_ i n → NO._≤_ j n → NO._≤_ (sinDegree i j) (maxDegree n)
sin-degree-bound n i j hi hj = NO.≤-+-≤ (NO.suc-≤-suc (NO.≤-+-≤ hi hi)) (NO.suc-≤-suc (NO.≤-+-≤ hj hj))

cosWeight sinWeight : Q.ℚ → ℕ → ℕ → Q.ℚ
cosWeight q i j = P.normalizedCosine q i Q.· P.normalizedCosine q j
sinWeight q i j = P.normalizedSine q i Q.· P.normalizedSine q j

degreeContribution : Q.ℚ → ℕ → ℕ → Q.ℚ
degreeContribution q n k =
  F.sum (λ i → F.sum (λ j → G.mass (cosDegree i j) (cosWeight q i j) k) n) n Q.+
  F.sum (λ i → F.sum (λ j → G.mass (sinDegree i j) (sinWeight q i j) k) n) n

operational-norm-by-degree : (q : Q.ℚ) (n : ℕ)
  → (cosinePartialSum q n Q.· cosinePartialSum q n) Q.+ (sinePartialSum q n Q.· sinePartialSum q n)
    ≡ F.sum (degreeContribution q n) (maxDegree n)
operational-norm-by-degree q n =
  cong₂ Q._+_
    (cong₂ Q._·_ (P.cosine-sum-as-normalized q n) (P.cosine-sum-as-normalized q n)
      ∙ F.product-expansion (P.normalizedCosine q) (P.normalizedCosine q) n n
      ∙ G.regroup-grid (cosWeight q) cosDegree n n (maxDegree n) (cos-degree-bound n))
    (cong₂ Q._·_ (P.sine-sum-as-normalized q n) (P.sine-sum-as-normalized q n)
      ∙ F.product-expansion (P.normalizedSine q) (P.normalizedSine q) n n
      ∙ G.regroup-grid (sinWeight q) sinDegree n n (maxDegree n) (sin-degree-bound n))
  ∙ sym (F.sum-add _ _ (maxDegree n))
