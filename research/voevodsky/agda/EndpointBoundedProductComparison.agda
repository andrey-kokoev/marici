{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module EndpointBoundedProductComparison where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ; suc; _+_)
import Cubical.Data.Nat.Order as O
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import CauchyProductCongruence

module Restore {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)
  restore : (b d : fst R) → d ≡ b +S (-S (b +S (-S d)))
  restore b d = solve! R

nearbyValueBound : (b d : Q.ℚ) (dy depth : ℕ) →
  MagnitudeBound b (dyadicRadius dy) →
  MagnitudeBound (b Q.+ (Q.- d)) (precision depth) →
  MagnitudeBound d (dyadicRadius (suc dy))
nearbyValueBound b d dy depth bBound differenceBound =
  weaken-magnitude-bound d (dyadicRadius dy Q.+ precision depth)
    (dyadicRadius (suc dy))
    (≤Monotone+ (dyadicRadius dy) (dyadicRadius dy)
      (precision depth) (dyadicRadius dy) (isRefl≤ (dyadicRadius dy))
      (isTrans≤ (precision depth) 1 (dyadicRadius dy)
        (precision-antitone 0 depth O.zero-≤) (dyadicRadius-at-least-one dy)))
    (transport-magnitude d _ _ (Restore.restore PreferredℚCommRing b d)
      (add-magnitude-bounds b (dyadicRadius dy)
        (Q.- (b Q.+ (Q.- d))) (precision depth) bBound
        (negate-magnitude-bound (b Q.+ (Q.- d)) (precision depth) differenceBound)))

endpointProductDepth : ℕ → ℕ → ℕ → ℕ
endpointProductDepth dx dy k = suc (dx Nat.+ suc dy) Nat.+ k

endpointProductComparison : (a b c d : Q.ℚ) (dx dy k : ℕ) →
  MagnitudeBound a (dyadicRadius dx) →
  MagnitudeBound b (dyadicRadius dy) →
  MagnitudeBound (a Q.+ (Q.- c)) (precision (endpointProductDepth dx dy k)) →
  MagnitudeBound (b Q.+ (Q.- d)) (precision (endpointProductDepth dx dy k)) →
  MagnitudeBound ((a Q.· b) Q.+ (Q.- (c Q.· d))) (precision k)
endpointProductComparison a b c d dx dy k aBound bBound ac bd =
  pointwise-refined-product-congruence-bound a b c d dx (suc dy) k
    aBound (nearbyValueBound b d dy (endpointProductDepth dx dy k) bBound bd)
    bd ac
