{-# OPTIONS --safe --cubical --guardedness #-}
module TickTrigCoefficientCancellation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
import Cubical.Data.Empty as Empty
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

-- Exponential-generating-series coefficients are represented by their
-- unnormalized derivatives at zero. This avoids factorial division here.
module Cancellation {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  Jet = ℕ → fst R

  shift : Jet → Jet
  shift a n = a (suc n)
  negative : Jet → Jet
  negative a n = - a n

  -- Iterated Leibniz rule, equivalently binomial convolution. The connection
  -- to the operational factorial-normalized partial sums is a separate task.
  productDerivative : Jet → Jet → ℕ → fst R
  productDerivative a b zero = a zero · b zero
  productDerivative a b (suc n) =
    productDerivative (shift a) b n + productDerivative a (shift b) n

  product-prefix-cong : (a a′ b b′ : Jet) (n : ℕ)
    → ((k : ℕ) → NO._≤_ k n → a k ≡ a′ k)
    → ((k : ℕ) → NO._≤_ k n → b k ≡ b′ k)
    → productDerivative a b n ≡ productDerivative a′ b′ n
  product-prefix-cong a a′ b b′ zero pa pb = cong₂ _·_ (pa zero NO.≤-refl) (pb zero NO.≤-refl)
  product-prefix-cong a a′ b b′ (suc n) pa pb = cong₂ _+_
    (product-prefix-cong (shift a) (shift a′) b b′ n
      (λ k h → pa (suc k) (NO.suc-≤-suc h))
      (λ k h → pb k (NO.≤-trans {m = n} h NO.≤-sucℕ)))
    (product-prefix-cong a a′ (shift b) (shift b′) n
      (λ k h → pa k (NO.≤-trans {m = n} h NO.≤-sucℕ))
      (λ k h → pb (suc k) (NO.suc-≤-suc h)))

  truncate : ℕ → Jet → Jet
  truncate zero a zero = a zero
  truncate zero a (suc k) = 0r
  truncate (suc n) a zero = a zero
  truncate (suc n) a (suc k) = truncate n (shift a) k

  truncation-prefix : (n : ℕ) (a : Jet) (k : ℕ)
    → NO._≤_ k n → truncate n a k ≡ a k
  truncation-prefix zero a zero h = refl
  truncation-prefix zero a (suc k) h = Empty.rec (NO.¬-<-zero h)
  truncation-prefix (suc n) a zero h = refl
  truncation-prefix (suc n) a (suc k) h = truncation-prefix n (shift a) k (NO.pred-≤-pred h)

  negative-left-product : (a b : fst R) → (- a) · b ≡ - (a · b)
  negative-left-product a b = solve! R
  negative-right-product : (a b : fst R) → a · (- b) ≡ - (a · b)
  negative-right-product a b = solve! R
  negative-add : (a b : fst R) → (- a) + (- b) ≡ - (a + b)
  negative-add a b = solve! R

  product-negative-left : (a b : Jet) (n : ℕ)
    → productDerivative (negative a) b n ≡ - productDerivative a b n
  product-negative-left a b zero = negative-left-product (a zero) (b zero)
  product-negative-left a b (suc n) =
    cong₂ _+_ (product-negative-left (shift a) b n)
      (product-negative-left a (shift b) n)
    ∙ negative-add (productDerivative (shift a) b n) (productDerivative a (shift b) n)

  product-negative-right : (a b : Jet) (n : ℕ)
    → productDerivative a (negative b) n ≡ - productDerivative a b n
  product-negative-right a b zero = negative-right-product (a zero) (b zero)
  product-negative-right a b (suc n) =
    cong₂ _+_ (product-negative-right (shift a) b n)
      (product-negative-right a (shift b) n)
    ∙ negative-add (productDerivative (shift a) b n) (productDerivative a (shift b) n)

  mutual
    cosineDerivative : Jet
    cosineDerivative zero = 1r
    cosineDerivative (suc n) = - sineDerivative n
    sineDerivative : Jet
    sineDerivative zero = 0r
    sineDerivative (suc n) = cosineDerivative n

  normDerivative : ℕ → fst R
  normDerivative n = productDerivative cosineDerivative cosineDerivative n
    + productDerivative sineDerivative sineDerivative n

  constant-coefficient : normDerivative zero ≡ 1r
  constant-coefficient = solve! R

  cancel-cross-terms : (a b : fst R) → ((- a) + (- b)) + (b + a) ≡ 0r
  cancel-cross-terms a b = solve! R

  positive-coefficient : (n : ℕ) → normDerivative (suc n) ≡ 0r
  positive-coefficient n =
    cong (_+ (productDerivative cosineDerivative sineDerivative n
      + productDerivative sineDerivative cosineDerivative n))
      (cong₂ _+_ (product-negative-left sineDerivative cosineDerivative n)
        (product-negative-right cosineDerivative sineDerivative n))
    ∙ cancel-cross-terms (productDerivative sineDerivative cosineDerivative n)
        (productDerivative cosineDerivative sineDerivative n)

  truncatedNorm : ℕ → ℕ → ℕ → fst R
  truncatedNorm c s k =
    productDerivative (truncate c cosineDerivative) (truncate c cosineDerivative) k
    + productDerivative (truncate s sineDerivative) (truncate s sineDerivative) k

  truncated-norm-prefix : (c s k : ℕ) → NO._≤_ k c → NO._≤_ k s
    → truncatedNorm c s k ≡ normDerivative k
  truncated-norm-prefix c s k kc ks = cong₂ _+_
    (product-prefix-cong _ _ _ _ k
      (λ j h → truncation-prefix c cosineDerivative j (NO.≤-trans h kc))
      (λ j h → truncation-prefix c cosineDerivative j (NO.≤-trans h kc)))
    (product-prefix-cong _ _ _ _ k
      (λ j h → truncation-prefix s sineDerivative j (NO.≤-trans h ks))
      (λ j h → truncation-prefix s sineDerivative j (NO.≤-trans h ks)))

  truncated-positive-coefficient : (c s n : ℕ)
    → NO._≤_ (suc n) c → NO._≤_ (suc n) s
    → truncatedNorm c s (suc n) ≡ 0r
  truncated-positive-coefficient c s n nc ns =
    truncated-norm-prefix c s (suc n) nc ns ∙ positive-coefficient n
