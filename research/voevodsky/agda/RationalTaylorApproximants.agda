{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalTaylorApproximants where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.NatPlusOne using (ℕ₊₁; 1+_)
open import Cubical.Data.Int as ℤ using (pos)
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RationalArchimedean
open import DyadicallyBoundedCauchy
open import CauchyProductBounds

reciprocalSuccessor : ℕ → Q.ℚ
reciprocalSuccessor n = Q.[ pos 1 / 1+ n ]

reciprocalSuccessor-nonnegative : (n : ℕ) →
  0 ≤ reciprocalSuccessor n
reciprocalSuccessor-nonnegative n = ℤOrder.zero-≤pos

reciprocalSuccessor≤one : (n : ℕ) →
  reciprocalSuccessor n ≤ 1
reciprocalSuccessor≤one n =
  positive-raw-rational≤numerator 1 (1+ n)

reciprocalSuccessor-after-zero≤half : (n : ℕ) →
  reciprocalSuccessor (suc n) ≤ one-half
reciprocalSuccessor-after-zero≤half n =
  ℤOrder.suc-≤-suc
    (ℤOrder.suc-≤-suc (ℤOrder.zero-≤pos {l = n}))

dyadicRadius-representative : (d : ℕ) →
  dyadicRadius d ≡ Q.[ pos (dyadicNat d) / 1 ]
dyadicRadius-representative d =
  sym (natℚ-dyadicNat d) ∙ natℚ-representative (dyadicNat d)

nat≤→positive-integer≤ : (m n : ℕ) →
  ℕOrder._≤_ m n → ℤOrder._≤_ (pos m) (pos n)
nat≤→positive-integer≤ m n (k , k+m≡n) =
  k , sym (ℤ.pos+ m k) ∙
    cong pos (ℕ.+-comm m k ∙ k+m≡n)

raw-late-reciprocal-contraction : (D : ℕ) →
  Q.[ pos D / 1 ] Q.· reciprocalSuccessor (D ℕ.+ D) ≤ one-half
raw-late-reciprocal-contraction D =
  let doubled = D ℕ.+ D
      left-normalizes :
        (pos D ℤ.· pos 1) ℤ.· pos 2 ≡ pos doubled
      left-normalizes =
        cong (ℤ._· pos 2) (ℤ.·IdR (pos D)) ∙
        cong (pos D ℤ.·_) (ℤ.pos+ 1 1) ∙
        ℤ.·DistR+ (pos D) (pos 1) (pos 1) ∙
        cong₂ ℤ._+_ (ℤ.·IdR (pos D)) (ℤ.·IdR (pos D)) ∙
        sym (ℤ.pos+ D D)
      right-normalizes :
        pos 1 ℤ.· pos (suc (doubled ℕ.+ zero)) ≡
        pos (suc doubled)
      right-normalizes =
        ℤ.·IdL (pos (suc (doubled ℕ.+ zero))) ∙
        cong pos (cong suc (ℕ.+-zero doubled))
  in
  subst (((pos D ℤ.· pos 1) ℤ.· pos 2) ℤOrder.≤_)
    (cong ℤ.sucℤ left-normalizes ∙ sym right-normalizes)
    ℤOrder.≤-sucℤ

dyadic-late-reciprocal-contraction : (d : ℕ) →
  dyadicRadius d Q.· reciprocalSuccessor (dyadicNat (suc d)) ≤ one-half
dyadic-late-reciprocal-contraction d =
  subst (_≤ one-half)
    (sym (cong (Q._· reciprocalSuccessor (dyadicNat (suc d)))
      (dyadicRadius-representative d)))
    (raw-late-reciprocal-contraction (dyadicNat d))

reciprocalSuccessor-antitone : (m n : ℕ) →
  ℕOrder._≤_ m n → reciprocalSuccessor n ≤ reciprocalSuccessor m
reciprocalSuccessor-antitone m n m≤n =
  subst2 ℤOrder._≤_
    (sym (ℤ.·IdL (pos (suc m))))
    (sym (ℤ.·IdL (pos (suc n))))
    (nat≤→positive-integer≤ (suc m) (suc n)
      (ℕOrder.suc-≤-suc m≤n))

reciprocalSuccessor-antitone-add : (d extra : ℕ) →
  reciprocalSuccessor (d ℕ.+ extra) ≤ reciprocalSuccessor d
reciprocalSuccessor-antitone-add d extra =
  reciprocalSuccessor-antitone d (d ℕ.+ extra) ℕOrder.≤SumLeft

dyadic-later-reciprocal-contraction : (d extra : ℕ) →
  dyadicRadius d Q.·
    reciprocalSuccessor (dyadicNat (suc d) ℕ.+ extra) ≤ one-half
dyadic-later-reciprocal-contraction d extra =
  isTrans≤
    (dyadicRadius d Q.·
      reciprocalSuccessor (dyadicNat (suc d) ℕ.+ extra))
    (dyadicRadius d Q.· reciprocalSuccessor (dyadicNat (suc d)))
    one-half
    (left-multiply-monotone
      (dyadicRadius d)
      (reciprocalSuccessor (dyadicNat (suc d) ℕ.+ extra))
      (reciprocalSuccessor (dyadicNat (suc d)))
      (dyadicRadius-nonnegative d)
      (reciprocalSuccessor-antitone-add (dyadicNat (suc d)) extra))
    (dyadic-late-reciprocal-contraction d)

finiteSum : (ℕ → Q.ℚ) → ℕ → Q.ℚ
finiteSum term zero = term zero
finiteSum term (suc n) = finiteSum term n Q.+ term (suc n)

exponentialTerm : Q.ℚ → ℕ → Q.ℚ
exponentialTerm q zero = 1
exponentialTerm q (suc n) =
  (exponentialTerm q n Q.· q) Q.· reciprocalSuccessor n

exponentialPartialSum : Q.ℚ → ℕ → Q.ℚ
exponentialPartialSum q = finiteSum (exponentialTerm q)

firstCosineDenominator : ℕ → ℕ
firstCosineDenominator n = n ℕ.+ n

secondCosineDenominator : ℕ → ℕ
secondCosineDenominator n = suc (n ℕ.+ n)

cosineTerm : Q.ℚ → ℕ → Q.ℚ
cosineTerm q zero = 1
cosineTerm q (suc n) =
  Q.- ((((cosineTerm q n Q.· q) Q.· q) Q.·
    reciprocalSuccessor (firstCosineDenominator n)) Q.·
    reciprocalSuccessor (secondCosineDenominator n))

cosinePartialSum : Q.ℚ → ℕ → Q.ℚ
cosinePartialSum q = finiteSum (cosineTerm q)

module TaylorZeroPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  exponential-zero-step : (a inverse : fst R) →
    (a ·S 0r) ·S inverse ≡ 0r
  exponential-zero-step a inverse = solve! R

  cosine-zero-step : (a firstInverse secondInverse : fst R) →
    -S ((((a ·S 0r) ·S 0r) ·S firstInverse) ·S secondInverse) ≡ 0r
  cosine-zero-step a firstInverse secondInverse = solve! R

exponentialTerm-at-zero : (n : ℕ) →
  exponentialTerm 0 (suc n) ≡ 0
exponentialTerm-at-zero n =
  TaylorZeroPaths.exponential-zero-step PreferredℚCommRing
    (exponentialTerm 0 n) (reciprocalSuccessor n)

cosineTerm-at-zero : (n : ℕ) →
  cosineTerm 0 (suc n) ≡ 0
cosineTerm-at-zero n =
  TaylorZeroPaths.cosine-zero-step PreferredℚCommRing
    (cosineTerm 0 n)
    (reciprocalSuccessor (firstCosineDenominator n))
    (reciprocalSuccessor (secondCosineDenominator n))

finiteSum-with-zero-tail : (term : ℕ → Q.ℚ) →
  term zero ≡ 1 → ((n : ℕ) → term (suc n) ≡ 0) →
  (n : ℕ) → finiteSum term n ≡ 1
finiteSum-with-zero-tail term atZero tail zero = atZero
finiteSum-with-zero-tail term atZero tail (suc n) =
  cong₂ Q._+_ (finiteSum-with-zero-tail term atZero tail n) (tail n) ∙
  Q.+IdR 1

exponentialPartialSum-at-zero : (n : ℕ) →
  exponentialPartialSum 0 n ≡ 1
exponentialPartialSum-at-zero =
  finiteSum-with-zero-tail (exponentialTerm 0) refl exponentialTerm-at-zero

cosinePartialSum-at-zero : (n : ℕ) →
  cosinePartialSum 0 n ≡ 1
cosinePartialSum-at-zero =
  finiteSum-with-zero-tail (cosineTerm 0) refl cosineTerm-at-zero

record TaylorCutoffSchedule : Type where
  field
    input-depth : ℕ → ℕ
    series-depth : ℕ → ℕ
open TaylorCutoffSchedule public

scheduledExponentialApproximation :
  TaylorCutoffSchedule → (ℕ → Q.ℚ) → ℕ → Q.ℚ
scheduledExponentialApproximation schedule input n =
  exponentialPartialSum
    (input (input-depth schedule n))
    (series-depth schedule n)

scheduledCosineApproximation :
  TaylorCutoffSchedule → (ℕ → Q.ℚ) → ℕ → Q.ℚ
scheduledCosineApproximation schedule input n =
  cosinePartialSum
    (input (input-depth schedule n))
    (series-depth schedule n)

scheduledExponential-at-zero : (schedule : TaylorCutoffSchedule) (n : ℕ) →
  scheduledExponentialApproximation schedule (λ _ → 0) n ≡ 1
scheduledExponential-at-zero schedule n =
  exponentialPartialSum-at-zero (series-depth schedule n)

scheduledCosine-at-zero : (schedule : TaylorCutoffSchedule) (n : ℕ) →
  scheduledCosineApproximation schedule (λ _ → 0) n ≡ 1
scheduledCosine-at-zero schedule n =
  cosinePartialSum-at-zero (series-depth schedule n)
