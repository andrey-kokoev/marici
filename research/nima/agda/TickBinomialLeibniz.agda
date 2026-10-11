{-# OPTIONS --safe --cubical --guardedness #-}
module TickBinomialLeibniz where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function
open import Cubical.Data.Nat using (ℕ; zero; suc; _∸_)
open import Cubical.Data.Nat.Order
open import Cubical.Data.FinData
open import Cubical.Algebra.CommRing
open import Cubical.Algebra.CommRing.BinomialThm
open import Cubical.Algebra.Ring.BigOps
open import Cubical.Tactics.CommRingSolver
import TickTrigCoefficientCancellation as C

-- The missing finite-sum interpretation of the recursively defined Leibniz jet.
-- The shape of the sum rearrangement follows the library's BinomialThm proof.
module Leibniz {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  open Sum (CommRing→Ring R)
  module B = BinomialThm R
  module D = C.Cancellation R

  terms : (n : ℕ) → D.Jet → D.Jet → FinVec (fst R) (suc n)
  terms n a b i = (B._choose_ n (toℕ i) · a (toℕ i)) · b (n ∸ toℕ i)

  convolution : D.Jet → D.Jet → ℕ → fst R
  convolution a b n = ∑ (terms n a b)

  rearrange : (x y z w : fst R) → (x + z) + (w + y) ≡ (w + (x + y)) + z
  rearrange x y z w = solve! R

  pascal-product : (x y a b : fst R) → (y · a) · b + (x · a) · b ≡ ((x + y) · a) · b
  pascal-product x y a b = solve! R

  recurrence : (n : ℕ) (a b : D.Jet)
    → convolution (D.shift a) b n + convolution a (D.shift b) n
      ≡ convolution a b (suc n)
  recurrence n a b =
    cong (_+ ∑ yVec) (∑Last xVec)
    ∙ rearrange (∑ (xVec ∘ weakenFin)) (∑ (yVec ∘ suc)) (xVec (fromℕ n)) (yVec zero)
    ∙ cong (λ z → (yVec zero + z) + xVec (fromℕ n)) (sym (∑Split (xVec ∘ weakenFin) (yVec ∘ suc)))
    ∙ cong (λ z → (yVec zero + z) + xVec (fromℕ n)) (∑Ext middlePath)
    ∙ cong (∑ (terms (suc n) a b ∘ weakenFin) +_) lastPath
    ∙ sym (∑Last (terms (suc n) a b))
    where
    xVec : FinVec (fst R) (suc n)
    xVec = terms n (D.shift a) b
    yVec : FinVec (fst R) (suc n)
    yVec = terms n a (D.shift b)

    middlePath : (i : Fin n)
      → xVec (weakenFin i) + yVec (suc i)
        ≡ terms (suc n) a b (weakenFin (suc i))
    middlePath i =
      cong₂ _+_
        (cong (λ k → (B._choose_ n k · a (suc k)) · b (n ∸ k)) (weakenRespToℕ i))
        (cong (λ k → (B._choose_ n (suc (toℕ i)) · a (suc (toℕ i))) · b k)
          (≤-∸-suc (toℕ<n i)))
      ∙ pascal-product (B._choose_ n (suc (toℕ i))) (B._choose_ n (toℕ i))
          (a (suc (toℕ i))) (b (n ∸ toℕ i))
      ∙ sym (cong (λ k → (B._choose_ (suc n) k · a k) · b (suc n ∸ k))
          (weakenRespToℕ (suc i)))

    lastPath : xVec (fromℕ n) ≡ terms (suc n) a b (fromℕ (suc n))
    lastPath =
      cong (λ k → (B._choose_ n k · a (suc k)) · b (n ∸ k)) (toFromId n)
      ∙ cong (λ c → (c · a (suc n)) · b (n ∸ n))
          (sym (+IdL _) ∙ cong (_+ B._choose_ n n) (sym (B.nChooseN+1 n)))
      ∙ sym (cong (λ k → (B._choose_ (suc n) k · a k) · b (suc n ∸ k)) (toFromId (suc n)))

  binomial-is-leibniz : (a b : D.Jet) (n : ℕ)
    → convolution a b n ≡ D.productDerivative a b n
  binomial-is-leibniz a b zero = solve! R
  binomial-is-leibniz a b (suc n) = sym (recurrence n a b)
    ∙ cong₂ _+_ (binomial-is-leibniz (D.shift a) b n)
        (binomial-is-leibniz a (D.shift b) n)

  norm-binomial-constant :
    convolution D.cosineDerivative D.cosineDerivative zero
      + convolution D.sineDerivative D.sineDerivative zero ≡ 1r
  norm-binomial-constant = cong₂ _+_
    (binomial-is-leibniz D.cosineDerivative D.cosineDerivative zero)
    (binomial-is-leibniz D.sineDerivative D.sineDerivative zero)
    ∙ D.constant-coefficient

  norm-binomial-positive : (n : ℕ)
    → convolution D.cosineDerivative D.cosineDerivative (suc n)
      + convolution D.sineDerivative D.sineDerivative (suc n) ≡ 0r
  norm-binomial-positive n = cong₂ _+_
    (binomial-is-leibniz D.cosineDerivative D.cosineDerivative (suc n))
    (binomial-is-leibniz D.sineDerivative D.sineDerivative (suc n))
    ∙ D.positive-coefficient n
