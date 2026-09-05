{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyProductDepthIndependence where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Sigma
open import Cubical.HITs.SetQuotients as SQ using ([_])
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyShift
open import DyadicallyBoundedCauchy
open import CauchyProductRegularity
open import CauchyProductAlgebra

shuffle-four-summands : (a b c d : ℕ) →
  (a ℕ.+ b) ℕ.+ (c ℕ.+ d) ≡ (c ℕ.+ a) ℕ.+ (d ℕ.+ b)
shuffle-four-summands a b c d =
  sym (ℕ.+-assoc a b (c ℕ.+ d)) ∙
  cong (λ z → a ℕ.+ z) (ℕ.+-assoc b c d) ∙
  cong (λ z → a ℕ.+ (z ℕ.+ d)) (ℕ.+-comm b c) ∙
  cong (λ z → a ℕ.+ z) (sym (ℕ.+-assoc c b d)) ∙
  ℕ.+-assoc a c (b ℕ.+ d) ∙
  cong (λ z → z ℕ.+ (b ℕ.+ d)) (ℕ.+-comm a c) ∙
  cong (λ z → (c ℕ.+ a) ℕ.+ z) (ℕ.+-comm b d)

widening-product-depth :
  (dx dy ex ey : ℕ) →
  ℕOrder._≤_ dx ex → ℕOrder._≤_ dy ey →
  Σ[ extra ∈ ℕ ]
    suc (dx ℕ.+ dy) ℕ.+ extra ≡ suc (ex ℕ.+ ey)
widening-product-depth dx dy ex ey (kx , kx+dx≡ex) (ky , ky+dy≡ey) =
  (kx ℕ.+ ky) ,
  cong suc
    (shuffle-four-summands dx dy kx ky ∙
     cong₂ ℕ._+_ kx+dx≡ex ky+dy≡ey)

deeperProductRegular :
  ℕ → DyadicallyBoundedRegularCauchy →
  DyadicallyBoundedRegularCauchy → RegularCauchy
deeperProductRegular extra x y =
  iterateShift extra (boundedProductRegular x y)

deeperProduct-approximation :
  (extra n : ℕ) (x y : DyadicallyBoundedRegularCauchy) →
  let canonical = suc (radius-exponent x ℕ.+ radius-exponent y)
  in
  approximation (deeperProductRegular extra x y) n ≡
  refinedProductApproximation (canonical ℕ.+ extra) (regular x) (regular y) n
deeperProduct-approximation extra n x y =
  let canonical = suc (radius-exponent x ℕ.+ radius-exponent y)
  in
  iterateShift-approximation extra n (boundedProductRegular x y) ∙
  cong₂ Q._·_
    (cong (approximation (regular x))
      (ℕ.+-assoc canonical extra n))
    (cong (approximation (regular y))
      (ℕ.+-assoc canonical extra n))

deepened-product-path-at-equal-depth :
  (extra : ℕ) (x y x′ y′ : DyadicallyBoundedRegularCauchy) →
  regular x ≡ regular x′ → regular y ≡ regular y′ →
  suc (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ extra ≡
    suc (radius-exponent x′ ℕ.+ radius-exponent y′) →
  deeperProductRegular extra x y ≡ boundedProductRegular x′ y′
deepened-product-path-at-equal-depth extra x y x′ y′ regularX regularY depthPath =
  regularCauchy-ext _ _ (funExt λ n →
    deeperProduct-approximation extra n x y ∙
    cong (λ { (xRegular , yRegular , depth) →
      refinedProductApproximation depth xRegular yRegular n })
      (λ i → regularX i , regularY i , depthPath i))

deeper-product-equivalent-to-canonical :
  (extra : ℕ) (x y : DyadicallyBoundedRegularCauchy) →
  deeperProductRegular extra x y ≈metric boundedProductRegular x y
deeper-product-equivalent-to-canonical extra x y =
  iterateShift-equivalent extra (boundedProductRegular x y)

widened-product-equivalent :
  (x y : DyadicallyBoundedRegularCauchy) (ex ey : ℕ) →
  (x≤ex : ℕOrder._≤_ (radius-exponent x) ex) →
  (y≤ey : ℕOrder._≤_ (radius-exponent y) ey) →
  boundedProductRegular
    (widenDyadicBound x ex x≤ex) (widenDyadicBound y ey y≤ey) ≈metric
  boundedProductRegular x y
widened-product-equivalent x y ex ey x≤ex y≤ey =
  let depthWitness = widening-product-depth
        (radius-exponent x) (radius-exponent y) ex ey x≤ex y≤ey
      extra = fst depthWitness
      depthPath = snd depthWitness
      productPath = deepened-product-path-at-equal-depth
        extra x y
        (widenDyadicBound x ex x≤ex) (widenDyadicBound y ey y≤ey)
        refl refl depthPath
  in
  subst (λ z → z ≈metric boundedProductRegular x y) productPath
    (deeper-product-equivalent-to-canonical extra x y)

extra-refinement-choice-independent :
  (extra₁ extra₂ : ℕ) (x y : DyadicallyBoundedRegularCauchy) →
  deeperProductRegular extra₁ x y ≈metric
  deeperProductRegular extra₂ x y
extra-refinement-choice-independent extra₁ extra₂ x y =
  iterateShift-choice-independent extra₁ extra₂
    (boundedProductRegular x y)

metricClass : RegularCauchy → MetricCompletionCandidate
metricClass z = SQ.[ z ]

extra-refinement-quotient-independent :
  (extra₁ extra₂ : ℕ) (x y : DyadicallyBoundedRegularCauchy) →
  metricClass (deeperProductRegular extra₁ x y) ≡
  metricClass (deeperProductRegular extra₂ x y)
extra-refinement-quotient-independent extra₁ extra₂ x y =
  SQ.eq/ _ _ (extra-refinement-choice-independent extra₁ extra₂ x y)
