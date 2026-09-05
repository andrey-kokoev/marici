{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module UniformCosineSeedBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import DyadicallyBoundedCauchy
open import RationalTaylorApproximants
open import TaylorTermBounds
open import CosineTermBounds
open import CosineTailSchedule

cosineTermGrowthExponent : ℕ → ℕ → ℕ
cosineTermGrowthExponent d zero = zero
cosineTermGrowthExponent d (suc n) =
  (cosineTermGrowthExponent d n ℕ.+ d) ℕ.+ d

cosine-term-uniform-growth-bound :
  (q : Q.ℚ) (d n : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound (cosineTerm q n)
    (dyadicRadius (cosineTermGrowthExponent d n))
cosine-term-uniform-growth-bound q d zero qBound =
  nonnegative-value-magnitude 1 1
    (dyadicRadius-nonnegative 0)
    (isRefl≤ 1)
    (dyadicRadius-nonnegative 0)
cosine-term-uniform-growth-bound q d (suc n) qBound =
  let previousExponent = cosineTermGrowthExponent d n
      raw = cosine-term-step-bound q
        (dyadicRadius previousExponent) (dyadicRadius d) n
        (dyadicRadius-nonnegative previousExponent)
        (dyadicRadius-nonnegative d)
        (cosine-term-uniform-growth-bound q d n qBound) qBound
      firstProduct = dyadicRadius-add previousExponent d
      secondProduct = dyadicRadius-add (previousExponent ℕ.+ d) d
      scalePath = cong (Q._· dyadicRadius d) (sym firstProduct) ∙
        sym secondProduct
  in
  subst (MagnitudeBound (cosineTerm q (suc n))) scalePath raw

uniformCosineSeedExponent : ℕ → ℕ
uniformCosineSeedExponent d =
  cosineTermGrowthExponent d (dyadicNat (suc d))

uniform-cosine-seed-bound :
  (q : Q.ℚ) (d : ℕ) →
  MagnitudeBound q (dyadicRadius d) →
  MagnitudeBound (cosineTerm q (dyadicNat (suc d)))
    (dyadicRadius (uniformCosineSeedExponent d))
uniform-cosine-seed-bound q d =
  cosine-term-uniform-growth-bound q d (dyadicNat (suc d))

uniformCosineTailSeed :
  (q : Q.ℚ) (d : ℕ) →
  MagnitudeBound q (dyadicRadius d) → CosineTailSeed q
uniformCosineTailSeed q d qBound = record
  { inputExponent = d
  ; inputBound = qBound
  ; seedExponent = uniformCosineSeedExponent d
  ; seedBound = uniform-cosine-seed-bound q d qBound
  }

uniformCosineCutoff : ℕ → ℕ → ℕ
uniformCosineCutoff d n =
  dyadicNat (suc d) ℕ.+ (uniformCosineSeedExponent d ℕ.+ n)

uniform-cosine-cutoff-seed-path :
  (q : Q.ℚ) (d n : ℕ) →
  (qBound : MagnitudeBound q (dyadicRadius d)) →
  uniformCosineCutoff d n ≡ absorbedCosineCutoff
    (uniformCosineTailSeed q d qBound) n
uniform-cosine-cutoff-seed-path q d n qBound = refl
