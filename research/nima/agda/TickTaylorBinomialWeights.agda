{-# OPTIONS --safe --cubical --guardedness #-}
module TickTaylorBinomialWeights where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as NO
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using (exponentialTerm)
import AbsoluteTaylorSeriesMultiplication as A
import TickTaylorProductExpansion as T
import TickTrigCoefficientCancellation as C
module D = C.Cancellation PreferredℚCommRing
import TickTaylorDegreeRegrouping as G
module F = T.FiniteProducts PreferredℚCommRing
module Degrees = G.Degrees PreferredℚCommRing

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_)
  reassociate : (x y z : fst R) → x ·S (y ·S z) ≡ (x ·S y) ·S z
  reassociate x y z = solve! R
  collect : (choose x y inverse : fst R)
    → ((choose ·S x) ·S y) ·S inverse ≡ choose ·S ((x ·S y) ·S inverse)
  collect choose x y inverse = solve! R
  weights : (a b x y : fst R) → (a ·S x) ·S (b ·S y) ≡ (a ·S b) ·S (x ·S y)
  weights a b x y = solve! R
  binomial : (a b choose z : fst R) → (a ·S b) ·S (choose ·S z) ≡ ((choose ·S a) ·S b) ·S z
  binomial a b choose z = solve! R

power-add : (q : Q.ℚ) (i j : ℕ)
  → A.taylorMonomialPower q i Q.· A.taylorMonomialPower q j ≡ A.taylorMonomialPower q (i N.+ j)
power-add q i zero = Q.·IdR _ ∙ sym (cong (A.taylorMonomialPower q) (N.+-zero i))
power-add q i (suc j) = Paths.reassociate PreferredℚCommRing (A.taylorMonomialPower q i) (A.taylorMonomialPower q j) q
  ∙ cong (Q._· q) (power-add q i j)
  ∙ sym (cong (A.taylorMonomialPower q) (N.+-suc i j))

exponential-binomial-split : (q : Q.ℚ) (degree left : ℕ) → NO._≤_ left degree
  → exponentialTerm q left Q.· exponentialTerm q (degree N.∸ left)
    ≡ A.RationalBinomial._choose_ degree left Q.· exponentialTerm q degree
exponential-binomial-split q degree left h =
  A.exponential-convolution-summand-from-factorial-split q q degree left
    (A.reciprocal-factorial-split degree left h)
  ∙ Paths.collect PreferredℚCommRing (A.RationalBinomial._choose_ degree left)
      (A.taylorMonomialPower q left) (A.taylorMonomialPower q (degree N.∸ left)) (A.reciprocalFactorial degree)
  ∙ cong (λ p → A.RationalBinomial._choose_ degree left Q.· (p Q.· A.reciprocalFactorial degree))
      (power-add q left (degree N.∸ left)
        ∙ cong (A.taylorMonomialPower q)
            (N.+-comm left (degree N.∸ left) ∙ NO.≤-∸-+-cancel h))
  ∙ cong (A.RationalBinomial._choose_ degree left Q.·_) (sym (A.exponential-term-factorization q degree))

exponential-product-weight : (q : Q.ℚ) (i j : ℕ)
  → exponentialTerm q i Q.· exponentialTerm q j
    ≡ A.RationalBinomial._choose_ (i N.+ j) i Q.· exponentialTerm q (i N.+ j)
exponential-product-weight q i j =
  cong (exponentialTerm q i Q.·_) (sym (cong (exponentialTerm q) (N.∸+ j i)))
  ∙ exponential-binomial-split q (i N.+ j) i NO.≤SumLeft

normalized-product-weight : (q a b : Q.ℚ) (i j : ℕ)
  → (a Q.· exponentialTerm q i) Q.· (b Q.· exponentialTerm q j)
    ≡ ((A.RationalBinomial._choose_ (i N.+ j) i Q.· a) Q.· b) Q.· exponentialTerm q (i N.+ j)
normalized-product-weight q a b i j =
  Paths.weights PreferredℚCommRing a b (exponentialTerm q i) (exponentialTerm q j)
  ∙ cong ((a Q.· b) Q.·_) (exponential-product-weight q i j)
  ∙ Paths.binomial PreferredℚCommRing a b (A.RationalBinomial._choose_ (i N.+ j) i) (exponentialTerm q (i N.+ j))

cosine-product-weight : (q : Q.ℚ) (i j : ℕ)
  → T.normalizedCosine q i Q.· T.normalizedCosine q j ≡
    ((A.RationalBinomial._choose_ ((i N.+ i) N.+ (j N.+ j)) (i N.+ i) Q.· D.cosineDerivative (i N.+ i)) Q.·
      D.cosineDerivative (j N.+ j)) Q.· exponentialTerm q ((i N.+ i) N.+ (j N.+ j))
cosine-product-weight q i j = normalized-product-weight q _ _ (i N.+ i) (j N.+ j)

sine-product-weight : (q : Q.ℚ) (i j : ℕ)
  → T.normalizedSine q i Q.· T.normalizedSine q j ≡
    ((A.RationalBinomial._choose_ (suc (i N.+ i) N.+ suc (j N.+ j)) (suc (i N.+ i)) Q.· D.sineDerivative (suc (i N.+ i))) Q.·
      D.sineDerivative (suc (j N.+ j))) Q.· exponentialTerm q (suc (i N.+ i) N.+ suc (j N.+ j))
sine-product-weight q i j = normalized-product-weight q _ _ (suc (i N.+ i)) (suc (j N.+ j))

cosBinomial sinBinomial : ℕ → ℕ → Q.ℚ
cosBinomial i j = (A.RationalBinomial._choose_ (G.cosDegree i j) (i N.+ i) Q.· D.cosineDerivative (i N.+ i)) Q.· D.cosineDerivative (j N.+ j)
sinBinomial i j = (A.RationalBinomial._choose_ (G.sinDegree i j) (suc (i N.+ i)) Q.· D.sineDerivative (suc (i N.+ i))) Q.· D.sineDerivative (suc (j N.+ j))

weightedDegreeContribution : Q.ℚ → ℕ → ℕ → Q.ℚ
weightedDegreeContribution q n k =
  F.sum (λ i → F.sum (λ j → Degrees.mass (G.cosDegree i j)
    (cosBinomial i j Q.· exponentialTerm q (G.cosDegree i j)) k) n) n Q.+
  F.sum (λ i → F.sum (λ j → Degrees.mass (G.sinDegree i j)
    (sinBinomial i j Q.· exponentialTerm q (G.sinDegree i j)) k) n) n

degree-contributions-weighted : (q : Q.ℚ) (n k : ℕ)
  → G.degreeContribution q n k ≡ weightedDegreeContribution q n k
degree-contributions-weighted q n k = cong₂ Q._+_
  (F.sum-cong _ _ (λ i → F.sum-cong _ _
    (λ j → cong (λ a → Degrees.mass (G.cosDegree i j) a k) (cosine-product-weight q i j)) n) n)
  (F.sum-cong _ _ (λ i → F.sum-cong _ _
    (λ j → cong (λ a → Degrees.mass (G.sinDegree i j) a k) (sine-product-weight q i j)) n) n)
