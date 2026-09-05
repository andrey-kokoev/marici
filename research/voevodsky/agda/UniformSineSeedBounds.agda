{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformSineSeedBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import DyadicallyBoundedCauchy
open import RationalSineTaylorApproximants
open import SineTermBounds
open import SineTailSchedule

sineTermGrowthExponent : ℕ → ℕ → ℕ
sineTermGrowthExponent d zero = d
sineTermGrowthExponent d (suc n) =
  (sineTermGrowthExponent d n ℕ.+ d) ℕ.+ d

sine-term-uniform-growth-bound :
  (q : Q.ℚ) (d n : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound (sineTerm q n)
    (dyadicRadius (sineTermGrowthExponent d n))
sine-term-uniform-growth-bound q d zero qBound = qBound
sine-term-uniform-growth-bound q d (suc n) qBound =
  let previousExponent = sineTermGrowthExponent d n
      raw = sine-term-step-bound q
        (dyadicRadius previousExponent) (dyadicRadius d) n
        (dyadicRadius-nonnegative previousExponent)
        (dyadicRadius-nonnegative d)
        (sine-term-uniform-growth-bound q d n qBound) qBound
      firstProduct = dyadicRadius-add previousExponent d
      secondProduct = dyadicRadius-add (previousExponent ℕ.+ d) d
      scalePath = cong (Q._· dyadicRadius d) (sym firstProduct) ∙
        sym secondProduct
  in
  subst (MagnitudeBound (sineTerm q (suc n))) scalePath raw

uniformSineSeedExponent : ℕ → ℕ
uniformSineSeedExponent d =
  sineTermGrowthExponent d (dyadicNat (suc d))

uniform-sine-seed-bound :
  (q : Q.ℚ) (d : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound (sineTerm q (dyadicNat (suc d)))
    (dyadicRadius (uniformSineSeedExponent d))
uniform-sine-seed-bound q d =
  sine-term-uniform-growth-bound q d (dyadicNat (suc d))

uniformSineTailSeed :
  (q : Q.ℚ) (d : ℕ) →
  MagnitudeBound q (dyadicRadius d) → SineTailSeed q
uniformSineTailSeed q d qBound = record
  { inputExponent = d
  ; inputBound = qBound
  ; seedExponent = uniformSineSeedExponent d
  ; seedBound = uniform-sine-seed-bound q d qBound
  }

uniformSineCutoff : ℕ → ℕ → ℕ
uniformSineCutoff d n =
  dyadicNat (suc d) ℕ.+ (uniformSineSeedExponent d ℕ.+ n)

uniform-sine-cutoff-seed-path :
  (q : Q.ℚ) (d n : ℕ) →
  (qBound : MagnitudeBound q (dyadicRadius d)) →
  uniformSineCutoff d n ≡
  absorbedSineCutoff (uniformSineTailSeed q d qBound) n
uniform-sine-cutoff-seed-path q d n qBound = refl
