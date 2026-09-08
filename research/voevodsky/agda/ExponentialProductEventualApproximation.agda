{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ExponentialProductEventualApproximation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; suc)
import Cubical.Data.Nat.Order as O
open import Cubical.Data.Sigma
open import Cubical.Data.Rationals as Q
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CanonicalDyadicallyBoundedCauchy
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import CauchyProductCongruence
open import CauchyProductRegularity
open import CauchyQuantitativeContinuity
open import CanonicalExponentialRegularity
open import SynchronizedExponentialApproximation
open import EndpointBoundedProductComparison

RawProductEventuallyClose : (x y c d : RegularCauchy) → ℕ → Type
RawProductEventuallyClose x y c d k =
  ∥ Σ[ M ∈ ℕ ] ((n : ℕ) → O._≤_ M n →
    MagnitudeBound
      ((approximation x n Q.· approximation y n) Q.+
        (Q.- (approximation c n Q.· approximation d n))) (precision k)) ∥₁

endpointProductEventuallyClose : (x y c d : RegularCauchy) (k : ℕ) →
  let depth = endpointProductDepth (canonicalDyadicExponent x) (canonicalDyadicExponent y) k in
  EventuallyWithin x c depth → EventuallyWithin y d depth →
  RawProductEventuallyClose x y c d k
endpointProductEventuallyClose x y c d k xc yd =
  PT.map (λ { (M , bounds) → M , λ n M≤n →
    endpointProductComparison (approximation x n) (approximation y n)
      (approximation c n) (approximation d n)
      (canonicalDyadicExponent x) (canonicalDyadicExponent y) k
      (bounded-value (canonicalDyadicallyBounded x) n)
      (bounded-value (canonicalDyadicallyBounded y) n)
      (difference-magnitude-bound (approximation x n) (approximation c n)
        (precision depth) (fst (fst (bounds n M≤n))) (snd (fst (bounds n M≤n))))
      (difference-magnitude-bound (approximation y n) (approximation d n)
        (precision depth) (fst (snd (bounds n M≤n))) (snd (snd (bounds n M≤n)))) })
    (combine-eventual-thresholds x c y d depth xc yd)
  where
  depth = endpointProductDepth (canonicalDyadicExponent x) (canonicalDyadicExponent y) k

module ExponentialProduct (x y : RegularCauchy) (k ks : ℕ) where
  ex = canonicalExponentialRegular x
  ey = canonicalExponentialRegular y
  depth = endpointProductDepth (canonicalDyadicExponent ex) (canonicalDyadicExponent ey) k
  module Sync = Synchronized x y depth depth ks

  productApproximation : (N : ℕ) → O._≤_ Sync.commonCutoff N →
    RawProductEventuallyClose ex ey
      (canonicalExponentialRegular (constantCauchy (approximation x (suc N))))
      (canonicalExponentialRegular (constantCauchy (approximation y (suc N)))) k
  productApproximation N cutoff≤N =
    endpointProductEventuallyClose ex ey
      (canonicalExponentialRegular (constantCauchy (approximation x (suc N))))
      (canonicalExponentialRegular (constantCauchy (approximation y (suc N)))) k
      (eventuallyWithin-sym
        (canonicalExponentialRegular (constantCauchy (approximation x (suc N))))
        ex depth (Sync.leftApproximation N cutoff≤N))
      (eventuallyWithin-sym
        (canonicalExponentialRegular (constantCauchy (approximation y (suc N))))
        ey depth (Sync.rightApproximation N cutoff≤N))
