{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TaylorTermBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import RationalTaylorApproximants

module TaylorTermPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_)

  reassociate-term : (term q reciprocal : fst R) →
    (term ·S q) ·S reciprocal ≡ term ·S (q ·S reciprocal)
  reassociate-term term q reciprocal = solve! R

nonnegative-value-magnitude : (a A : Q.ℚ) →
  0 ≤ a → a ≤ A → 0 ≤ A → MagnitudeBound a A
nonnegative-value-magnitude a A 0≤a a≤A 0≤A .positive-upper = a≤A
nonnegative-value-magnitude a A 0≤a a≤A 0≤A .negative-upper =
  isTrans≤ (Q.- a) 0 A (negative-nonpositive a 0≤a) 0≤A

nonnegative-bound-product : (A B : Q.ℚ) →
  0 ≤ A → 0 ≤ B → 0 ≤ A Q.· B
nonnegative-bound-product A B 0≤A 0≤B =
  subst (_≤ A Q.· B) (Q.·AnnihilR A)
    (left-multiply-monotone A 0 B 0≤A 0≤B)

reciprocal-magnitude≤one : (n : ℕ) →
  MagnitudeBound (reciprocalSuccessor n) 1
reciprocal-magnitude≤one n =
  nonnegative-value-magnitude (reciprocalSuccessor n) 1
    (reciprocalSuccessor-nonnegative n)
    (reciprocalSuccessor≤one n)
    (dyadicRadius-nonnegative 0)

reciprocal-after-zero-magnitude≤half : (n : ℕ) →
  MagnitudeBound (reciprocalSuccessor (suc n)) one-half
reciprocal-after-zero-magnitude≤half n =
  nonnegative-value-magnitude (reciprocalSuccessor (suc n)) one-half
    (reciprocalSuccessor-nonnegative (suc n))
    (reciprocalSuccessor-after-zero≤half n)
    one-half-nonnegative

late-scaled-input-magnitude≤half :
  (q : Q.ℚ) (d : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound
    (q Q.· reciprocalSuccessor (dyadicNat (suc d))) one-half
late-scaled-input-magnitude≤half q d qBound =
  weaken-magnitude-bound _ _ one-half
    (dyadic-late-reciprocal-contraction d)
    (arbitrary-multiplier-bound
      q (dyadicRadius d)
      (reciprocalSuccessor (dyadicNat (suc d)))
      (reciprocalSuccessor (dyadicNat (suc d)))
      (dyadicRadius-nonnegative d)
      (reciprocalSuccessor-nonnegative (dyadicNat (suc d)))
      qBound
      (nonnegative-value-magnitude _ _
        (reciprocalSuccessor-nonnegative (dyadicNat (suc d)))
        (isRefl≤ (reciprocalSuccessor (dyadicNat (suc d))))
        (reciprocalSuccessor-nonnegative (dyadicNat (suc d)))))

later-scaled-input-magnitude≤half :
  (q : Q.ℚ) (d extra : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound
    (q Q.· reciprocalSuccessor (dyadicNat (suc d) ℕ.+ extra))
    one-half
later-scaled-input-magnitude≤half q d extra qBound =
  let index = dyadicNat (suc d) ℕ.+ extra
      reciprocal = reciprocalSuccessor index
      reciprocalNonnegative = reciprocalSuccessor-nonnegative index
  in
  weaken-magnitude-bound (q Q.· reciprocal)
    (dyadicRadius d Q.· reciprocal) one-half
    (dyadic-later-reciprocal-contraction d extra)
    (arbitrary-multiplier-bound
      q (dyadicRadius d) reciprocal reciprocal
      (dyadicRadius-nonnegative d) reciprocalNonnegative qBound
      (nonnegative-value-magnitude reciprocal reciprocal
        reciprocalNonnegative (isRefl≤ reciprocal) reciprocalNonnegative))

exponential-term-step-bound :
  (q T R : Q.ℚ) (n : ℕ) →
  0 ≤ T → 0 ≤ R →
  MagnitudeBound (exponentialTerm q n) T →
  MagnitudeBound q R →
  MagnitudeBound (exponentialTerm q (suc n)) ((T Q.· R) Q.· 1)
exponential-term-step-bound q T R n 0≤T 0≤R termBound qBound =
  arbitrary-multiplier-bound
    (exponentialTerm q n Q.· q) (T Q.· R)
    (reciprocalSuccessor n) 1
    (nonnegative-bound-product T R 0≤T 0≤R)
    (dyadicRadius-nonnegative 0)
    (arbitrary-multiplier-bound
      (exponentialTerm q n) T q R
      0≤T 0≤R termBound qBound)
    (reciprocal-magnitude≤one n)

exponential-term-after-zero-step-bound :
  (q T R : Q.ℚ) (n : ℕ) →
  0 ≤ T → 0 ≤ R →
  MagnitudeBound (exponentialTerm q (suc n)) T →
  MagnitudeBound q R →
  MagnitudeBound (exponentialTerm q (suc (suc n)))
    ((T Q.· R) Q.· one-half)
exponential-term-after-zero-step-bound q T R n 0≤T 0≤R termBound qBound =
  arbitrary-multiplier-bound
    (exponentialTerm q (suc n) Q.· q) (T Q.· R)
    (reciprocalSuccessor (suc n)) one-half
    (nonnegative-bound-product T R 0≤T 0≤R)
    one-half-nonnegative
    (arbitrary-multiplier-bound
      (exponentialTerm q (suc n)) T q R
      0≤T 0≤R termBound qBound)
    (reciprocal-after-zero-magnitude≤half n)

late-exponential-term-contraction :
  (q T : Q.ℚ) (d extra : ℕ) →
  0 ≤ T →
  MagnitudeBound
    (exponentialTerm q (dyadicNat (suc d) ℕ.+ extra)) T →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound
    (exponentialTerm q (suc (dyadicNat (suc d) ℕ.+ extra)))
    (T Q.· one-half)
late-exponential-term-contraction q T d extra 0≤T termBound qBound =
  transport-magnitude _ _ (T Q.· one-half)
    (TaylorTermPaths.reassociate-term PreferredℚCommRing
      (exponentialTerm q (dyadicNat (suc d) ℕ.+ extra)) q
      (reciprocalSuccessor (dyadicNat (suc d) ℕ.+ extra)))
    (arbitrary-multiplier-bound
      (exponentialTerm q (dyadicNat (suc d) ℕ.+ extra)) T
      (q Q.· reciprocalSuccessor (dyadicNat (suc d) ℕ.+ extra)) one-half
      0≤T one-half-nonnegative termBound
      (later-scaled-input-magnitude≤half q d extra qBound))

late-exponential-term-geometric-decay :
  (q T : Q.ℚ) (d : ℕ) →
  0 ≤ T →
  MagnitudeBound (exponentialTerm q (dyadicNat (suc d))) T →
  MagnitudeBound q (dyadicRadius d) →
  (extra : ℕ) →
  MagnitudeBound
    (exponentialTerm q (dyadicNat (suc d) ℕ.+ extra))
    (T Q.· precision extra)
late-exponential-term-geometric-decay q T d 0≤T initial qBound zero =
  subst (MagnitudeBound
      (exponentialTerm q (dyadicNat (suc d) ℕ.+ zero)))
    (sym (Q.·IdR T))
    (transport-magnitude _ _ T
      (cong (exponentialTerm q) (ℕ.+-zero (dyadicNat (suc d))))
      initial)
late-exponential-term-geometric-decay q T d 0≤T initial qBound (suc extra) =
  let previous = late-exponential-term-geometric-decay
        q T d 0≤T initial qBound extra
      contracted = late-exponential-term-contraction
        q (T Q.· precision extra) d extra
        (nonnegative-bound-product T (precision extra)
          0≤T (precision-nonnegative extra))
        previous qBound
      reindexed = transport-magnitude _ _
        ((T Q.· precision extra) Q.· one-half)
        (cong (exponentialTerm q) (ℕ.+-suc (dyadicNat (suc d)) extra))
        contracted
  in
  subst (MagnitudeBound
      (exponentialTerm q (dyadicNat (suc d) ℕ.+ suc extra)))
    (sym (Q.·Assoc T (precision extra) one-half))
    reindexed

