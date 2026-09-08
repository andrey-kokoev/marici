{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module ExponentialRationalApproximation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ; zero; suc; max)
import Cubical.Data.Nat.Order as NatOrder
import Cubical.Data.Empty as Empty
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyRationalDensity
open import CauchyQuantitativeContinuity using (eventuallyWithin-sym)
open import CanonicalDyadicallyBoundedCauchy
open import CanonicalExponentialRegularity
open import RationalArchimedean
open import RationalApproximantCanonicalBound
open import BoundedExponentialModulus

maxRightMonotone : (a b c : ℕ) → NatOrder._≤_ b c →
  NatOrder._≤_ (Nat.max a b) (Nat.max a c)
maxRightMonotone zero b c b≤c = b≤c
maxRightMonotone (suc a) zero c b≤c = NatOrder.left-≤-max {m = suc a} {n = c}
maxRightMonotone (suc a) (suc b) zero b≤c = Empty.rec (NatOrder.¬-<-zero b≤c)
maxRightMonotone (suc a) (suc b) (suc c) b≤c =
  NatOrder.suc-≤-suc (maxRightMonotone a b c (NatOrder.pred-≤-pred b≤c))

exponentialApproximationExponent : RegularCauchy → ℕ
exponentialApproximationExponent x =
  Nat.max (canonicalDyadicExponent x) (exponent (approximantRadiusWitness x))

exponentialApproximationCutoff : RegularCauchy → ℕ → ℕ
exponentialApproximationCutoff x k =
  suc (boundedExponentialDepth (exponentialApproximationExponent x) k)

exponentialRationalApproximation : (x : RegularCauchy) (k N : ℕ) →
  NatOrder._≤_ (exponentialApproximationCutoff x k) N →
  EventuallyWithin
    (canonicalExponentialRegular (constantCauchy (approximation x N)))
    (canonicalExponentialRegular x) k
exponentialRationalApproximation x k N cutoff≤N =
  eventuallyWithin-sym (canonicalExponentialRegular x)
    (canonicalExponentialRegular (constantCauchy (approximation x N))) k
    (boundedExponentialEventuallyWithin x
      (constantCauchy (approximation x N)) (exponentialApproximationExponent x) k
      (maxRightMonotone (canonicalDyadicExponent x)
        (canonicalDyadicExponent (constantCauchy (approximation x N)))
        (exponent (approximantRadiusWitness x))
        (approximantCanonicalExponentBound x N))
      (eventuallyWithin-sym (constantCauchy (approximation x N)) x
        (boundedExponentialDepth (exponentialApproximationExponent x) k)
        (rational-approximation-eventually-within x
          (boundedExponentialDepth (exponentialApproximationExponent x) k) N cutoff≤N)))
