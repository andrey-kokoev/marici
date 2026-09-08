{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module SynchronizedExponentialApproximation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ; suc; max)
import Cubical.Data.Nat.Order as O
open import Cubical.Data.Rationals as Q
open import RegularCauchyStructure
open import CauchyAddition
open import CauchyMetricEquivalence
open import CanonicalExponentialRegularity
open import ExponentialRationalApproximation

module Synchronized (x y : RegularCauchy) (kx ky ks : ℕ) where
  leftCutoff = exponentialApproximationCutoff x kx
  rightCutoff = exponentialApproximationCutoff y ky
  sumCutoff = exponentialApproximationCutoff (addRegular x y) ks
  commonCutoff = Nat.max leftCutoff (Nat.max rightCutoff sumCutoff)

  left≤common : O._≤_ leftCutoff commonCutoff
  left≤common = O.left-≤-max {m = leftCutoff} {n = Nat.max rightCutoff sumCutoff}
  right≤common : O._≤_ rightCutoff commonCutoff
  right≤common = O.≤-trans
    (O.left-≤-max {m = rightCutoff} {n = sumCutoff})
    (O.right-≤-max {n = Nat.max rightCutoff sumCutoff} {m = leftCutoff})
  sum≤common : O._≤_ sumCutoff commonCutoff
  sum≤common = O.≤-trans
    (O.right-≤-max {n = sumCutoff} {m = rightCutoff})
    (O.right-≤-max {n = Nat.max rightCutoff sumCutoff} {m = leftCutoff})

  leftApproximation : (N : ℕ) → O._≤_ commonCutoff N →
    EventuallyWithin
      (canonicalExponentialRegular (constantCauchy (approximation x (suc N))))
      (canonicalExponentialRegular x) kx
  leftApproximation N common≤N = exponentialRationalApproximation x kx (suc N)
    (O.≤-trans left≤common (O.≤-trans common≤N O.≤-sucℕ))

  rightApproximation : (N : ℕ) → O._≤_ commonCutoff N →
    EventuallyWithin
      (canonicalExponentialRegular (constantCauchy (approximation y (suc N))))
      (canonicalExponentialRegular y) ky
  rightApproximation N common≤N = exponentialRationalApproximation y ky (suc N)
    (O.≤-trans right≤common (O.≤-trans common≤N O.≤-sucℕ))

  sumApproximation : (N : ℕ) → O._≤_ commonCutoff N →
    EventuallyWithin
      (canonicalExponentialRegular (constantCauchy
        (approximation x (suc N) Q.+ approximation y (suc N))))
      (canonicalExponentialRegular (addRegular x y)) ks
  sumApproximation N common≤N =
    exponentialRationalApproximation (addRegular x y) ks N
      (O.≤-trans sum≤common common≤N)
