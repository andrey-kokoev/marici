{-# OPTIONS --safe --cubical --guardedness #-}
module TickNormalizedTrigConvolution where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.FinData using (Fin; toℕ; toℕ<n)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using (exponentialTerm)
import AbsoluteTaylorSeriesMultiplication as A
import TickTaylorBinomialWeights as W
import TickBinomialLeibniz as L
import TickTrigCoefficientCancellation as C
module B = L.Leibniz PreferredℚCommRing
module D = C.Cancellation PreferredℚCommRing

normalized : Q.ℚ → D.Jet → ℕ → Q.ℚ
normalized q a k = a k Q.· exponentialTerm q k

normalized-summand : (q : Q.ℚ) (a b : D.Jet) (n : ℕ) (i : Fin (suc n))
  → normalized q a (toℕ i) Q.· normalized q b (n N.∸ toℕ i)
    ≡ B.terms n a b i Q.· exponentialTerm q n
normalized-summand q a b n i =
  W.Paths.weights PreferredℚCommRing (a (toℕ i)) (b (n N.∸ toℕ i))
    (exponentialTerm q (toℕ i)) (exponentialTerm q (n N.∸ toℕ i))
  ∙ cong ((a (toℕ i) Q.· b (n N.∸ toℕ i)) Q.·_)
      (W.exponential-binomial-split q n (toℕ i) (NO.pred-≤-pred (toℕ<n i)))
  ∙ W.Paths.binomial PreferredℚCommRing (a (toℕ i)) (b (n N.∸ toℕ i))
      (A.RationalBinomial._choose_ n (toℕ i)) (exponentialTerm q n)

normalized-convolution : (q : Q.ℚ) (a b : D.Jet) (n : ℕ)
  → A.cauchyProductCoefficient (normalized q a) (normalized q b) n
    ≡ B.convolution a b n Q.· exponentialTerm q n
normalized-convolution q a b n =
  A.finiteSumAsBigOp (λ k → normalized q a k Q.· normalized q b (n N.∸ k)) n
  ∙ A.RationalSum.∑Ext (normalized-summand q a b n)
  ∙ sym (A.RationalSum.∑Mulldist (exponentialTerm q n) (B.terms n a b))

denseCosine denseSine : Q.ℚ → ℕ → Q.ℚ
denseCosine q = normalized q D.cosineDerivative
denseSine q = normalized q D.sineDerivative

denseNormCoefficient : Q.ℚ → ℕ → Q.ℚ
denseNormCoefficient q n =
  A.cauchyProductCoefficient (denseCosine q) (denseCosine q) n Q.+
  A.cauchyProductCoefficient (denseSine q) (denseSine q) n

module RingPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)
  collect : (a b z : fst R) → (a ·S z) +S (b ·S z) ≡ (a +S b) ·S z
  collect a b z = solve! R
  zero-times : (z : fst R) → 0r ·S z ≡ 0r
  zero-times z = solve! R

norm-coefficient-factorization : (q : Q.ℚ) (n : ℕ)
  → denseNormCoefficient q n ≡
    (B.convolution D.cosineDerivative D.cosineDerivative n Q.+
     B.convolution D.sineDerivative D.sineDerivative n) Q.· exponentialTerm q n
norm-coefficient-factorization q n = cong₂ Q._+_
  (normalized-convolution q D.cosineDerivative D.cosineDerivative n)
  (normalized-convolution q D.sineDerivative D.sineDerivative n)
  ∙ RingPaths.collect PreferredℚCommRing
      (B.convolution D.cosineDerivative D.cosineDerivative n)
      (B.convolution D.sineDerivative D.sineDerivative n) (exponentialTerm q n)

norm-coefficient-zero : (q : Q.ℚ) → denseNormCoefficient q zero ≡ 1
norm-coefficient-zero q = norm-coefficient-factorization q zero
  ∙ cong (Q._· exponentialTerm q zero) B.norm-binomial-constant
  ∙ Q.·IdL 1

norm-coefficient-positive : (q : Q.ℚ) (n : ℕ) → denseNormCoefficient q (suc n) ≡ 0
norm-coefficient-positive q n = norm-coefficient-factorization q (suc n)
  ∙ cong (Q._· exponentialTerm q (suc n)) (B.norm-binomial-positive n)
  ∙ RingPaths.zero-times PreferredℚCommRing (exponentialTerm q (suc n))
