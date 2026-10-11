{-# OPTIONS --safe --cubical --guardedness #-}
module TickDenseTrigCutoffs where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import RationalTaylorApproximants using (exponentialTerm; finiteSum; cosinePartialSum)
open import RationalSineTaylorApproximants using (sinePartialSum)
import TickTrigCoefficientCancellation as C
import TickTrigTaylorNormalization as T
module D = C.Cancellation PreferredℚCommRing

-- Definitionally the dense sequences used in TickNormalizedTrigConvolution,
-- without importing the entire product/residual development just for parity.
denseCosine denseSine : Q.ℚ → ℕ → Q.ℚ
denseCosine q k = D.cosineDerivative k Q.· exponentialTerm q k
denseSine q k = D.sineDerivative k Q.· exponentialTerm q k

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  negative-zero : -S 0r ≡ 0r
  negative-zero = solve! R
  zero-times : (z : fst R) → 0r ·S z ≡ 0r
  zero-times z = solve! R

sine-even-zero : (n : ℕ) → D.sineDerivative (n N.+ n) ≡ 0
sine-even-zero zero = refl
sine-even-zero (suc n) = cong D.sineDerivative (T.double-step n)
  ∙ cong Q.-_ (sine-even-zero n)
  ∙ Paths.negative-zero PreferredℚCommRing

cosine-odd-zero : (n : ℕ) → D.cosineDerivative (suc (n N.+ n)) ≡ 0
cosine-odd-zero n = cong Q.-_ (sine-even-zero n)
  ∙ Paths.negative-zero PreferredℚCommRing

dense-sine-even-zero : (q : Q.ℚ) (n : ℕ) → denseSine q (n N.+ n) ≡ 0
dense-sine-even-zero q n = cong (Q._· exponentialTerm q (n N.+ n)) (sine-even-zero n)
  ∙ Paths.zero-times PreferredℚCommRing (exponentialTerm q (n N.+ n))

dense-cosine-odd-zero : (q : Q.ℚ) (n : ℕ) → denseCosine q (suc (n N.+ n)) ≡ 0
dense-cosine-odd-zero q n = cong (Q._· exponentialTerm q (suc (n N.+ n))) (cosine-odd-zero n)
  ∙ Paths.zero-times PreferredℚCommRing (exponentialTerm q (suc (n N.+ n)))

-- Both series use the common dense cutoff 2n+1, with no erased endpoint term.
cosine-dense-cutoff : (q : Q.ℚ) (n : ℕ)
  → finiteSum (denseCosine q) (suc (n N.+ n)) ≡ cosinePartialSum q n
cosine-dense-cutoff q zero = cong₂ Q._+_
  (sym (T.cosine-term-normalized q zero)) (dense-cosine-odd-zero q zero)
  ∙ Q.+IdR 1
cosine-dense-cutoff q (suc n) =
  cong₂ Q._+_
    (cong (finiteSum (denseCosine q)) (T.double-step n)
      ∙ cong₂ Q._+_ (cosine-dense-cutoff q n)
          (sym (cong (denseCosine q) (T.double-step n)) ∙ sym (T.cosine-term-normalized q (suc n))))
    (dense-cosine-odd-zero q (suc n))
  ∙ Q.+IdR (cosinePartialSum q (suc n))

sine-dense-cutoff : (q : Q.ℚ) (n : ℕ)
  → finiteSum (denseSine q) (suc (n N.+ n)) ≡ sinePartialSum q n
sine-dense-cutoff q zero = cong₂ Q._+_
  (dense-sine-even-zero q zero) (sym (T.sine-term-normalized q zero))
  ∙ Q.+IdL q
sine-dense-cutoff q (suc n) = cong₂ Q._+_
  (cong (finiteSum (denseSine q)) (T.double-step n)
    ∙ cong₂ Q._+_ (sine-dense-cutoff q n)
        (sym (cong (denseSine q) (T.double-step n)) ∙ dense-sine-even-zero q (suc n))
    ∙ Q.+IdR (sinePartialSum q n))
  (sym (T.sine-term-normalized q (suc n)))
