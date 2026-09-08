{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalApproximantCanonicalBound where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
import Cubical.Data.Nat.Order as NatOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import RegularCauchyStructure
open import RationallyBoundedCauchy
open import RationalArchimedean
open import DyadicallyBoundedCauchy using (dyadicRadius)
open import CanonicalDyadicallyBoundedCauchy
open import LeastDyadicExponentSearch

approximantCanonicalRadiusBound : (x : RegularCauchy) (N : ℕ) →
  canonicalRadius (constantCauchy (approximation x N)) ≤
    canonicalRadius x Q.+ rationalTwo
approximantCanonicalRadiusBound x N =
  ≤-+o (Q.max q (Q.- q)) (canonicalRadius x) rationalTwo
    (subst (Q.max q (Q.- q) ≤_)
      (≤→max (canonicalRadius x) (canonicalRadius x) (isRefl≤ (canonicalRadius x)))
      (≤MonotoneMax q (canonicalRadius x) (Q.- q) (canonicalRadius x)
        (RationallyBoundedRegularCauchy.positive-upper
          (regular-is-rationally-bounded x) N)
        (RationallyBoundedRegularCauchy.negative-upper
          (regular-is-rationally-bounded x) N)))
  where
  q = approximation x N

approximantRadiusWitness : (x : RegularCauchy) →
  ArchimedeanExponent (canonicalRadius x Q.+ rationalTwo)
approximantRadiusWitness x = least-dyadic-gives-exponent _
  (select-least-dyadic preferred-least-dyadic-exponent-principle
    (canonicalRadius x Q.+ rationalTwo))

approximantCanonicalExponentBound : (x : RegularCauchy) (N : ℕ) →
  NatOrder._≤_ (canonicalDyadicExponent (constantCauchy (approximation x N)))
    (exponent (approximantRadiusWitness x))
approximantCanonicalExponentBound x N =
  least-minimal (canonicalLeastDyadicExponent (constantCauchy (approximation x N)))
    (exponent (approximantRadiusWitness x))
    (isTrans≤ (canonicalRadius (constantCauchy (approximation x N)))
      (canonicalRadius x Q.+ rationalTwo)
      (dyadicRadius (exponent (approximantRadiusWitness x)))
      (approximantCanonicalRadiusBound x N)
      (dominates (approximantRadiusWitness x)))
