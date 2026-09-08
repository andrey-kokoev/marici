{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RawProductRefinementTransport where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ; suc; _+_)
import Cubical.Data.Nat.Order as O
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyMetricEquivalence
open import CauchyQuantitativeContinuity
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import CauchyProductRegularity
open import CauchyProductCongruence
open import DyadicallyBoundedCauchyMultiplication
open import DyadicallyBoundedCauchyAddition
open import DyadicBoundNormalization
open import CauchyAdditionCongruence
open import CauchyProductAlgebra
open import CauchyProductDepthIndependence
open import ExponentialProductEventualApproximation

module Transport (x y c d : DyadicallyBoundedRegularCauchy) where
  p = suc (radius-exponent x Nat.+ radius-exponent y)
  q = suc (radius-exponent c Nat.+ radius-exponent d)
  left = boundedProductRegular x y
  right = boundedProductRegular c d
  deepLeft = deeperProductRegular q x y
  deepRight = deeperProductRegular p c d

  alignedEventually : (k : ℕ) →
    RawProductEventuallyClose (regular x) (regular y) (regular c) (regular d) k →
    EventuallyWithin deepLeft deepRight k
  alignedEventually k = PT.map λ { (M , bounds) → M , λ n M≤n →
    let index = (p Nat.+ q) Nat.+ n
        tail = bounds index (O.≤-trans M≤n (O.≤SumRight {n = n} {k = p Nat.+ q}))
        lp = deeperProduct-approximation q n x y
        rp = deeperProduct-approximation p n c d ∙
          cong (λ depth → refinedProductApproximation depth (regular c) (regular d) n)
            (Nat.+-comm q p)
        bound = subst2 (λ a b → MagnitudeBound (a Q.+ (Q.- b)) (precision k))
          (sym lp) (sym rp) tail
    in
    single-difference-bound→directed (approximation deepLeft n)
      (approximation deepRight n) (precision k) (positive-upper bound) ,
    single-difference-bound→directed (approximation deepRight n)
      (approximation deepLeft n) (precision k)
      (subst (λ z → z ≤ precision k)
        (ProductSignPaths.negative-difference PreferredℚCommRing
          (approximation deepLeft n) (approximation deepRight n))
        (negative-upper bound)) }

  rawToBoundedProducts : (k : ℕ) →
    RawProductEventuallyClose (regular x) (regular y) (regular c) (regular d)
      (suc (suc k)) → EventuallyWithin left right k
  rawToBoundedProducts k raw =
    composeEventuallyWithin left deepLeft right k
      (eventuallyWithin-sym deepLeft left (suc k)
        (deeper-product-equivalent-to-canonical q x y (suc k)))
      (composeEventuallyWithin deepLeft deepRight right (suc k)
        (alignedEventually (suc (suc k)) raw)
        (deeper-product-equivalent-to-canonical p c d (suc (suc k))))
