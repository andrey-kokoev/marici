{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module SineSeedNegation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ)
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyNegation
open import DyadicallyBoundedCauchy
open import RationalSineTaylorApproximants
open import RationalSineSymmetry
open import SineTailSchedule

negateSineTailSeed : {q : Q.ℚ} → SineTailSeed q → SineTailSeed (Q.- q)
negateSineTailSeed seed .inputExponent = inputExponent seed
negateSineTailSeed seed .inputBound =
  negate-magnitude-bound _ _ (inputBound seed)
negateSineTailSeed {q} seed .seedExponent = seedExponent seed
negateSineTailSeed {q} seed .seedBound =
  subst
    (λ value → MagnitudeBound value (dyadicRadius (seedExponent seed)))
    (sym (sineTerm-odd q
      (dyadicNat (ℕ.suc (inputExponent seed)))))
    (negate-magnitude-bound _ _ (seedBound seed))

negated-seed-base-cutoff : {q : Q.ℚ} → (seed : SineTailSeed q) →
  baseSineCutoff (negateSineTailSeed seed) ≡ baseSineCutoff seed
negated-seed-base-cutoff seed = refl

negated-seed-absorbed-cutoff : {q : Q.ℚ} →
  (seed : SineTailSeed q) (n : ℕ) →
  absorbedSineCutoff (negateSineTailSeed seed) n ≡
  absorbedSineCutoff seed n
negated-seed-absorbed-cutoff seed n = refl

negated-seed-partial-sum : {q : Q.ℚ} →
  (seed : SineTailSeed q) (n : ℕ) →
  absorbedSinePartialSum (negateSineTailSeed seed) n ≡
  Q.- absorbedSinePartialSum seed n
negated-seed-partial-sum {q} seed n =
  sinePartialSum-odd q (absorbedSineCutoff seed n)

negated-seed-regular : {q : Q.ℚ} → (seed : SineTailSeed q) →
  absorbedSineRegular (negateSineTailSeed seed) ≡
  negateRegular (absorbedSineRegular seed)
negated-seed-regular seed =
  regularCauchy-ext _ _ (funExt (negated-seed-partial-sum seed))
