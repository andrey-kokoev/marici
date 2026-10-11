{-# OPTIONS --safe --cubical --guardedness #-}
module TickTrigTaylorNormalization where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RationalTaylorApproximants
open import RationalSineTaylorApproximants
import TickTrigCoefficientCancellation as C
module D = C.Cancellation PreferredℚCommRing

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_; -_ to -S_)
  step : (d e q a b : fst R)
    → -S (((((d ·S e) ·S q) ·S q) ·S a) ·S b)
      ≡ (-S d) ·S ((((e ·S q) ·S a) ·S q) ·S b)
  step d e q a b = solve! R

  cosine-start : 1r ≡ 1r ·S 1r
  cosine-start = solve! R
  sine-start : (q : fst R) → q ≡ 1r ·S ((1r ·S q) ·S 1r)
  sine-start q = solve! R

double-step : (n : ℕ) → suc n N.+ suc n ≡ suc (suc (n N.+ n))
double-step n = cong suc (N.+-suc n n)

cosine-term-normalized : (q : Q.ℚ) (n : ℕ)
  → cosineTerm q n ≡ D.cosineDerivative (n N.+ n) Q.· exponentialTerm q (n N.+ n)
cosine-term-normalized q zero = Paths.cosine-start PreferredℚCommRing
cosine-term-normalized q (suc n) =
  cong (λ a → Q.- ((((a Q.· q) Q.· q) Q.· reciprocalSuccessor (n N.+ n)) Q.· reciprocalSuccessor (suc (n N.+ n))))
    (cosine-term-normalized q n)
  ∙ Paths.step PreferredℚCommRing (D.cosineDerivative (n N.+ n)) (exponentialTerm q (n N.+ n)) q
      (reciprocalSuccessor (n N.+ n)) (reciprocalSuccessor (suc (n N.+ n)))
  ∙ sym (cong (λ k → D.cosineDerivative k Q.· exponentialTerm q k) (double-step n))

sine-term-normalized : (q : Q.ℚ) (n : ℕ)
  → sineTerm q n ≡ D.sineDerivative (suc (n N.+ n)) Q.· exponentialTerm q (suc (n N.+ n))
sine-term-normalized q zero = Paths.sine-start PreferredℚCommRing q
sine-term-normalized q (suc n) =
  cong (λ a → Q.- ((((a Q.· q) Q.· q) Q.· reciprocalSuccessor (suc (n N.+ n))) Q.· reciprocalSuccessor (suc (suc (n N.+ n)))))
    (sine-term-normalized q n)
  ∙ Paths.step PreferredℚCommRing (D.sineDerivative (suc (n N.+ n))) (exponentialTerm q (suc (n N.+ n))) q
      (reciprocalSuccessor (suc (n N.+ n))) (reciprocalSuccessor (suc (suc (n N.+ n))))
  ∙ sym (cong (λ k → D.sineDerivative k Q.· exponentialTerm q k) (cong suc (double-step n)))

finiteSum-cong : (a b : ℕ → Q.ℚ) → ((k : ℕ) → a k ≡ b k)
  → (n : ℕ) → finiteSum a n ≡ finiteSum b n
finiteSum-cong a b p zero = p zero
finiteSum-cong a b p (suc n) = cong₂ Q._+_ (finiteSum-cong a b p n) (p (suc n))

cosine-sum-normalized : (q : Q.ℚ) (n : ℕ)
  → cosinePartialSum q n ≡ finiteSum (λ k → D.cosineDerivative (k N.+ k) Q.· exponentialTerm q (k N.+ k)) n
cosine-sum-normalized q = finiteSum-cong _ _ (cosine-term-normalized q)

sine-sum-normalized : (q : Q.ℚ) (n : ℕ)
  → sinePartialSum q n ≡ finiteSum (λ k → D.sineDerivative (suc (k N.+ k)) Q.· exponentialTerm q (suc (k N.+ k))) n
sine-sum-normalized q = finiteSum-cong _ _ (sine-term-normalized q)
