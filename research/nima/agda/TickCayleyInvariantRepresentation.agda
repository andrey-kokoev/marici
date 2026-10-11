{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyInvariantRepresentation where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing; one-half)
open import CauchyMetricEquivalence
open import CauchyProductBounds
open import CauchyAdditionCongruence using (_+completion_)
open import TickAtanCompletionFirstOrder using (atanCompletion)
open import TickOperationalRotorIncrement using (rotation)
open import TickRotationDefectTransport using (_⊗_)
open import TickCayleyGridIncrement using (gridValue; gridProductInverse; grid-product-inverse-law)
open import TickCayleyConcreteTransport using (gridInvariant)

magnitude-isProp : (q B : Q.ℚ) → isProp (MagnitudeBound q B)
magnitude-isProp q B h k i .positive-upper = isProp≤ q B (positive-upper h) (positive-upper k) i
magnitude-isProp q B h k i .negative-upper = isProp≤ (Q.- q) B (negative-upper h) (negative-upper k) i

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_·_ to _·S_)
  reorder : (d u v : fst R) → u ·S (d ·S v) ≡ (d ·S u) ·S v
  reorder d u v = solve! R
  inverse-unique : (d u v : fst R) → d ·S u ≡ 1r → d ·S v ≡ 1r → u ≡ v
  inverse-unique d u v hu hv = sym (CommRingStr.·IdR (snd R) u) ∙ cong (u ·S_) (sym hv) ∙ reorder d u v
    ∙ cong (_·S v) hu ∙ CommRingStr.·IdL (snd R) v

abstract
  grid-inverse-representation : (n d m e : ℕ) → gridValue n d ≡ gridValue m e → gridProductInverse n n d ≡ gridProductInverse m m e
  grid-inverse-representation n d m e p = Algebra.inverse-unique PreferredℚCommRing
    (1 Q.+ gridValue n d Q.· gridValue n d) (gridProductInverse n n d) (gridProductInverse m m e)
    (grid-product-inverse-law n n d)
    (cong (λ q → (1 Q.+ q Q.· q) Q.· gridProductInverse m m e) p ∙ grid-product-inverse-law m m e)

  invariant-representation : (n d m e : ℕ)
    (h : MagnitudeBound (gridValue n d) one-half) (k : MagnitudeBound (gridValue m e) one-half) →
    gridValue n d ≡ gridValue m e → gridInvariant n d h ≡ gridInvariant m e k
  invariant-representation n d m e h k p i =
    rotation (atanCompletion (p i) (hp i) +completion atanCompletion (p i) (hp i)) ⊗
      (embedMetricℚ ((1 Q.+ (Q.- (p i Q.· p i))) Q.· ip i) ,
       embedMetricℚ (Q.- ((p i Q.+ p i) Q.· ip i)))
    where
    hp : PathP (λ i → MagnitudeBound (p i) one-half) h k
    hp = isProp→PathP (λ i → magnitude-isProp (p i) one-half) h k
    ip : gridProductInverse n n d ≡ gridProductInverse m m e
    ip = grid-inverse-representation n d m e p
