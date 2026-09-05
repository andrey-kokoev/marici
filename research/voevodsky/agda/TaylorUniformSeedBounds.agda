{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TaylorUniformSeedBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import RationalTaylorApproximants
open import TaylorTermBounds
open import ExponentialTailSchedule

termPowerExponent : ℕ → ℕ → ℕ
termPowerExponent d zero = zero
termPowerExponent d (suc n) = termPowerExponent d n ℕ.+ d

exponential-term-dyadic-power-bound :
  (q : Q.ℚ) (d n : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound (exponentialTerm q n)
    (dyadicRadius (termPowerExponent d n))
exponential-term-dyadic-power-bound q d zero qBound =
  bounded-value boundedOne zero
exponential-term-dyadic-power-bound q d (suc n) qBound =
  let previous = exponential-term-dyadic-power-bound q d n qBound
      step = exponential-term-step-bound
        q (dyadicRadius (termPowerExponent d n)) (dyadicRadius d) n
        (dyadicRadius-nonnegative (termPowerExponent d n))
        (dyadicRadius-nonnegative d) previous qBound
  in
  subst (MagnitudeBound (exponentialTerm q (suc n)))
    (Q.·IdR
      (dyadicRadius (termPowerExponent d n) Q.· dyadicRadius d) ∙
     sym (dyadicRadius-add (termPowerExponent d n) d))
    step

termDifferenceExponent : ℕ → ℕ → ℕ
termDifferenceExponent d zero = zero
termDifferenceExponent d (suc n) =
  suc ((termDifferenceExponent d n ℕ.+ d) ℕ.+ termPowerExponent d n)

term-difference-scale-step : (d n : ℕ) →
  (dyadicRadius (termDifferenceExponent d n) Q.· dyadicRadius d) Q.+
  dyadicRadius (termPowerExponent d n) ≤
  dyadicRadius (termDifferenceExponent d (suc n))
term-difference-scale-step d n =
  let differenceScale = termDifferenceExponent d n
      termScale = termPowerExponent d n
      target = dyadicRadius (termDifferenceExponent d (suc n))
      radiusSum = radius-sum≤successor-combined
        (differenceScale ℕ.+ d) termScale
  in
  subst (_≤ target)
    (cong (Q._+ dyadicRadius termScale)
      (dyadicRadius-add differenceScale d))
    radiusSum

uniformExponentialSeedExponent : ℕ → ℕ
uniformExponentialSeedExponent d =
  termPowerExponent d (dyadicNat (suc d))

uniform-exponential-seed-bound :
  (q : Q.ℚ) (d : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound
    (exponentialTerm q (dyadicNat (suc d)))
    (dyadicRadius (uniformExponentialSeedExponent d))
uniform-exponential-seed-bound q d =
  exponential-term-dyadic-power-bound q d (dyadicNat (suc d))

uniformExponentialTailSeed :
  (q : Q.ℚ) (d : ℕ) →
  MagnitudeBound q (dyadicRadius d) → ExponentialTailSeed q
uniformExponentialTailSeed q d qBound = record
  { inputExponent = d
  ; inputBound = qBound
  ; seedExponent = uniformExponentialSeedExponent d
  ; seedBound = uniform-exponential-seed-bound q d qBound
  }

uniformExponentialCutoff : ℕ → ℕ → ℕ
uniformExponentialCutoff d n =
  absorbedTaylorCutoff
    (uniformExponentialTailSeed 0 d
      (weaken-magnitude-bound 0 0 (dyadicRadius d)
        (dyadicRadius-nonnegative d)
        record
          { negative-upper = isRefl≤ 0
          ; positive-upper = isRefl≤ 0
          })) n

uniformExponentialCutoff-formula : (d n : ℕ) →
  uniformExponentialCutoff d n ≡
  dyadicNat (suc d) ℕ.+ (uniformExponentialSeedExponent d ℕ.+ n)
uniformExponentialCutoff-formula d n = refl
