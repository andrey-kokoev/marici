{-# OPTIONS --safe --cubical --guardedness #-}
module TickTaylorProductExpansion where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

-- Finite algebra only: no rearrangement of an infinite sum is assumed.
module FiniteProducts {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  sum : (ℕ → fst R) → ℕ → fst R
  sum a zero = a zero
  sum a (suc n) = sum a n + a (suc n)

  sum-cong : (a b : ℕ → fst R) → ((k : ℕ) → a k ≡ b k)
    → (n : ℕ) → sum a n ≡ sum b n
  sum-cong a b p zero = p zero
  sum-cong a b p (suc n) = cong₂ _+_ (sum-cong a b p n) (p (suc n))

  regroup : (a b c d : fst R) → (a + b) + (c + d) ≡ (a + c) + (b + d)
  regroup a b c d = solve! R

  sum-add : (a b : ℕ → fst R) (n : ℕ)
    → sum (λ k → a k + b k) n ≡ sum a n + sum b n
  sum-add a b zero = refl
  sum-add a b (suc n) = cong (_+ (a (suc n) + b (suc n))) (sum-add a b n)
    ∙ regroup (sum a n) (sum b n) (a (suc n)) (b (suc n))

  sum-left-multiply : (x : fst R) (a : ℕ → fst R) (n : ℕ)
    → x · sum a n ≡ sum (λ k → x · a k) n
  sum-left-multiply x a zero = refl
  sum-left-multiply x a (suc n) = ·DistR+ x (sum a n) (a (suc n))
    ∙ cong (_+ (x · a (suc n))) (sum-left-multiply x a n)

  sum-right-multiply : (a : ℕ → fst R) (n : ℕ) (x : fst R)
    → sum a n · x ≡ sum (λ k → a k · x) n
  sum-right-multiply a zero x = refl
  sum-right-multiply a (suc n) x = ·DistL+ (sum a n) (a (suc n)) x
    ∙ cong (_+ (a (suc n) · x)) (sum-right-multiply a n x)

  product-expansion : (a b : ℕ → fst R) (m n : ℕ)
    → sum a m · sum b n ≡ sum (λ i → sum (λ j → a i · b j) n) m
  product-expansion a b m n = sum-right-multiply a m (sum b n)
    ∙ sum-cong _ _ (λ i → sum-left-multiply (a i) b n) m

  interchange : (a : ℕ → ℕ → fst R) (m n : ℕ)
    → sum (λ i → sum (a i) n) m ≡ sum (λ j → sum (λ i → a i j) m) n
  interchange a zero n = refl
  interchange a (suc m) n =
    cong (_+ sum (a (suc m)) n) (interchange a m n)
    ∙ sym (sum-add (λ j → sum (λ i → a i j) m) (a (suc m)) n)

  norm-expansion : (c s : ℕ → fst R) (n : ℕ)
    → (sum c n · sum c n) + (sum s n · sum s n)
      ≡ sum (λ i → sum (λ j → (c i · c j) + (s i · s j)) n) n
  norm-expansion c s n = cong₂ _+_ (product-expansion c c n n) (product-expansion s s n n)
    ∙ sym (sum-add (λ i → sum (λ j → c i · c j) n) (λ i → sum (λ j → s i · s j) n) n)
    ∙ sum-cong _ _ (λ i → sym (sum-add (λ j → c i · c j) (λ j → s i · s j) n)) n

import Cubical.Data.Rationals as Q
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using (finiteSum; exponentialTerm; cosinePartialSum)
open import RationalSineTaylorApproximants using (sinePartialSum)
import TickTrigTaylorNormalization as T
module F = FiniteProducts PreferredℚCommRing

finite-sum-agrees : (a : ℕ → Q.ℚ) (n : ℕ) → finiteSum a n ≡ F.sum a n
finite-sum-agrees a zero = refl
finite-sum-agrees a (suc n) = cong (Q._+ a (suc n)) (finite-sum-agrees a n)

normalizedCosine normalizedSine : Q.ℚ → ℕ → Q.ℚ
normalizedCosine q n = T.D.cosineDerivative (n N.+ n) Q.· exponentialTerm q (n N.+ n)
normalizedSine q n = T.D.sineDerivative (suc (n N.+ n)) Q.· exponentialTerm q (suc (n N.+ n))

cosine-sum-as-normalized : (q : Q.ℚ) (n : ℕ) → cosinePartialSum q n ≡ F.sum (normalizedCosine q) n
cosine-sum-as-normalized q n = T.cosine-sum-normalized q n ∙ finite-sum-agrees (normalizedCosine q) n
sine-sum-as-normalized : (q : Q.ℚ) (n : ℕ) → sinePartialSum q n ≡ F.sum (normalizedSine q) n
sine-sum-as-normalized q n = T.sine-sum-normalized q n ∙ finite-sum-agrees (normalizedSine q) n

operational-norm-expansion : (q : Q.ℚ) (n : ℕ)
  → (cosinePartialSum q n Q.· cosinePartialSum q n) Q.+ (sinePartialSum q n Q.· sinePartialSum q n)
    ≡ F.sum (λ i → F.sum (λ j →
        (normalizedCosine q i Q.· normalizedCosine q j) Q.+
        (normalizedSine q i Q.· normalizedSine q j)) n) n
operational-norm-expansion q n = cong₂ Q._+_
  (cong₂ Q._·_ (cosine-sum-as-normalized q n) (cosine-sum-as-normalized q n))
  (cong₂ Q._·_ (sine-sum-as-normalized q n) (sine-sum-as-normalized q n))
  ∙ F.norm-expansion (normalizedCosine q) (normalizedSine q) n
