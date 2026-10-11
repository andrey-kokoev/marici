{-# OPTIONS --safe --cubical --guardedness #-}
module TickTrigAdditionCoefficients where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using (finiteSum; exponentialTerm)
import AbsoluteTaylorSeriesMultiplication as A
import TickTrigCoefficientCancellation as J
import TickNormalizedTrigConvolution as D
module W = J.Cancellation PreferredℚCommRing

module Rotation {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  module Jets = J.Cancellation R
  c = Jets.cosineDerivative
  s = Jets.sineDerivative

  c-base : (a b : fst R) → a ≡ 1r · a + (- (0r · b))
  c-base a b = solve! R
  s-base : (a b : fst R) → b ≡ 0r · a + 1r · b
  s-base a b = solve! R
  c-step : (a b u v : fst R) → - (b · u + a · v) ≡ (- b) · u + (- (a · v))
  c-step a b u v = solve! R
  s-step : (a b u v : fst R) → a · u + (- (b · v)) ≡ a · u + (- b) · v
  s-step a b u v = solve! R

  mutual
    cosine-add-index : (m n : ℕ) → c (m N.+ n) ≡ c m · c n + (- (s m · s n))
    cosine-add-index zero n = c-base (c n) (s n)
    cosine-add-index (suc m) n = cong -_ (sine-add-index m n) ∙ c-step (c m) (s m) (c n) (s n)

    sine-add-index : (m n : ℕ) → s (m N.+ n) ≡ s m · c n + c m · s n
    sine-add-index zero n = s-base (c n) (s n)
    sine-add-index (suc m) n = cosine-add-index m n ∙ s-step (c m) (s m) (c n) (s n)

  collect-minus : (a b c d x y : fst R) →
    (a · x) · (b · y) + (- ((c · x) · (d · y))) ≡ (a · b + (- (c · d))) · (x · y)
  collect-minus a b c d x y = solve! R
  collect-plus : (a b c d x y : fst R) →
    (a · x) · (b · y) + ((c · x) · (d · y)) ≡ (a · b + c · d) · (x · y)
  collect-plus a b c d x y = solve! R
  negative-sum : (a b : fst R) → - (a + b) ≡ (- a) + (- b)
  negative-sum a b = solve! R
  distribute : (a b d : fst R) → d · (a + b) ≡ d · a + d · b
  distribute a b d = solve! R

module R = Rotation PreferredℚCommRing

finiteSum-negate : (f : ℕ → Q.ℚ) (n : ℕ) → finiteSum (λ k → Q.- f k) n ≡ Q.- finiteSum f n
finiteSum-negate f zero = refl
finiteSum-negate f (suc n) = cong (Q._+ (Q.- f (suc n))) (finiteSum-negate f n)
  ∙ sym (R.negative-sum (finiteSum f n) (f (suc n)))

finiteSum-scale : (d : Q.ℚ) (f : ℕ → Q.ℚ) (n : ℕ) →
  finiteSum (λ k → d Q.· f k) n ≡ d Q.· finiteSum f n
finiteSum-scale d f zero = refl
finiteSum-scale d f (suc n) = cong (Q._+ (d Q.· f (suc n))) (finiteSum-scale d f n)
  ∙ sym (R.distribute (finiteSum f n) (f (suc n)) d)

finiteSum-cong-prefix : (f g : ℕ → Q.ℚ) (n : ℕ) →
  ((k : ℕ) → NO._≤_ k n → f k ≡ g k) → finiteSum f n ≡ finiteSum g n
finiteSum-cong-prefix f g zero h = h zero NO.≤-refl
finiteSum-cong-prefix f g (suc n) h = cong₂ Q._+_
  (finiteSum-cong-prefix f g n (λ k hk → h k (NO.≤-trans hk NO.≤-sucℕ))) (h (suc n) NO.≤-refl)

cos-summand : (x y : Q.ℚ) (n k : ℕ) → NO._≤_ k n →
  (D.denseCosine x k Q.· D.denseCosine y (n N.∸ k)) Q.+
    (Q.- (D.denseSine x k Q.· D.denseSine y (n N.∸ k))) ≡
  W.cosineDerivative n Q.· (exponentialTerm x k Q.· exponentialTerm y (n N.∸ k))
cos-summand x y n k kn =
  R.collect-minus (W.cosineDerivative k) (W.cosineDerivative (n N.∸ k))
    (W.sineDerivative k) (W.sineDerivative (n N.∸ k)) (exponentialTerm x k) (exponentialTerm y (n N.∸ k))
  ∙ cong (Q._· (exponentialTerm x k Q.· exponentialTerm y (n N.∸ k)))
    (sym (R.cosine-add-index k (n N.∸ k))
      ∙ cong W.cosineDerivative (N.+-comm k (n N.∸ k) ∙ NO.≤-∸-+-cancel kn))

sin-summand : (x y : Q.ℚ) (n k : ℕ) → NO._≤_ k n →
  (D.denseSine x k Q.· D.denseCosine y (n N.∸ k)) Q.+
    (D.denseCosine x k Q.· D.denseSine y (n N.∸ k)) ≡
  W.sineDerivative n Q.· (exponentialTerm x k Q.· exponentialTerm y (n N.∸ k))
sin-summand x y n k kn =
  R.collect-plus (W.sineDerivative k) (W.cosineDerivative (n N.∸ k))
    (W.cosineDerivative k) (W.sineDerivative (n N.∸ k)) (exponentialTerm x k) (exponentialTerm y (n N.∸ k))
  ∙ cong (Q._· (exponentialTerm x k Q.· exponentialTerm y (n N.∸ k)))
    (sym (R.sine-add-index k (n N.∸ k))
      ∙ cong W.sineDerivative (N.+-comm k (n N.∸ k) ∙ NO.≤-∸-+-cancel kn))

abstract
  cosine-addition-coefficient : (x y : Q.ℚ) (n : ℕ) →
    A.cauchyProductCoefficient (D.denseCosine x) (D.denseCosine y) n Q.+
      (Q.- A.cauchyProductCoefficient (D.denseSine x) (D.denseSine y) n) ≡ D.denseCosine (x Q.+ y) n
  cosine-addition-coefficient x y n =
    cong (A.cauchyProductCoefficient (D.denseCosine x) (D.denseCosine y) n Q.+_)
      (sym (finiteSum-negate (λ k → D.denseSine x k Q.· D.denseSine y (n N.∸ k)) n))
    ∙ sym (A.finiteSumAdd _ _ n)
    ∙ finiteSum-cong-prefix _ _ n (cos-summand x y n)
    ∙ finiteSum-scale (W.cosineDerivative n) _ n
    ∙ cong (W.cosineDerivative n Q.·_) (A.exponential-coefficient-convolution x y n)

  sine-addition-coefficient : (x y : Q.ℚ) (n : ℕ) →
    A.cauchyProductCoefficient (D.denseSine x) (D.denseCosine y) n Q.+
      A.cauchyProductCoefficient (D.denseCosine x) (D.denseSine y) n ≡ D.denseSine (x Q.+ y) n
  sine-addition-coefficient x y n = sym (A.finiteSumAdd _ _ n)
    ∙ finiteSum-cong-prefix _ _ n (sin-summand x y n)
    ∙ finiteSum-scale (W.sineDerivative n) _ n
    ∙ cong (W.sineDerivative n Q.·_) (A.exponential-coefficient-convolution x y n)
