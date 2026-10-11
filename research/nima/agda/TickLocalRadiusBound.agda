{-# OPTIONS --safe --cubical --guardedness #-}
module TickLocalRadiusBound where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as Nat using (ℕ; zero; suc; max; _+_)
import Cubical.Data.Nat.Order as N
import Cubical.Data.Empty as Empty
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Sigma using (_×_)
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyNegation
open import CauchyShift using (tighten-two-errors)
import RationallyBoundedCauchy as RB
open import RationalArchimedean using (least-dominates; least-minimal)
open import DyadicallyBoundedCauchy using (dyadicRadius; dyadicRadius-at-least-one; dyadicRadius-monotone)
open import CanonicalDyadicallyBoundedCauchy

max-bounded : (a b d : ℕ) → N._≤_ a d → N._≤_ b d → N._≤_ (Nat.max a b) d
max-bounded zero b d ad bd = bd
max-bounded (suc a) zero d ad bd = ad
max-bounded (suc a) (suc b) zero ad bd = Empty.rec (N.¬-<-zero ad)
max-bounded (suc a) (suc b) (suc d) ad bd =
  N.suc-≤-suc (max-bounded a b d (N.pred-≤-pred ad) (N.pred-≤-pred bd))

-- A finite envelope avoids assuming monotonicity of the library's very
-- large Taylor schedule functions.
envelope : (ℕ → ℕ) → ℕ → ℕ
envelope f zero = f zero
envelope f (suc d) = Nat.max (envelope f d) (f (suc d))

envelope-self : (f : ℕ → ℕ) (d : ℕ) → N._≤_ (f d) (envelope f d)
envelope-self f zero = N.≤-refl
envelope-self f (suc d) = N.right-≤-max

envelope-monotone : (f : ℕ → ℕ) (a b : ℕ) → N._≤_ a b →
  N._≤_ (envelope f a) (envelope f b)
envelope-monotone f a b (extra , path) = subst (λ n → N._≤_ (envelope f a) (envelope f n)) path (go extra)
  where
  go : (e : ℕ) → N._≤_ (envelope f a) (envelope f (e Nat.+ a))
  go zero = N.≤-refl
  go (suc e) = N.≤-trans (go e) N.left-≤-max

envelope-covers : (f : ℕ → ℕ) (a b : ℕ) → N._≤_ a b → N._≤_ (f a) (envelope f b)
envelope-covers f a b h = N.≤-trans (envelope-self f a) (envelope-monotone f a b h)

nearbyExponent : RegularCauchy → ℕ
nearbyExponent x = suc (suc (suc (canonicalDyadicExponent x)))

center-exponent≤nearby : (x : RegularCauchy) → N._≤_ (canonicalDyadicExponent x) (nearbyExponent x)
center-exponent≤nearby x = N.≤-trans N.≤-sucℕ (N.≤-trans N.≤-sucℕ N.≤-sucℕ)

-- Crucial quantifier order: this bound depends only on the CENTER x.
-- Eventual closeness and Cauchy regularity bound even the early samples of y.
nearby-exponent-bound : (x y : RegularCauchy) → EventuallyWithin x y 0 →
  N._≤_ (canonicalDyadicExponent y) (nearbyExponent x)
nearby-exponent-bound x y = PT.rec N.isProp≤ λ { (n , bounds) →
  least-minimal (canonicalLeastDyadicExponent y) (nearbyExponent x) (radiusBound n (bounds n N.≤-refl)) }
  where
  d = canonicalDyadicExponent x
  R = dyadicRadius d
  two = RB.rationalTwo
  xb = RB.regular-is-rationally-bounded x
  radiusX≤R = least-dominates (canonicalLeastDyadicExponent x)
  one≤R = dyadicRadius-at-least-one d
  two≤2R : two ≤ dyadicRadius (suc d)
  two≤2R = ≤Monotone+ 1 R 1 R one≤R one≤R
  two≤4R : two ≤ dyadicRadius (suc (suc d))
  two≤4R = isTrans≤ two (dyadicRadius (suc d)) (dyadicRadius (suc (suc d)))
    two≤2R (dyadicRadius-monotone (suc d) (suc (suc d)) N.≤-sucℕ)

  sampleBound : (a b c : Q.ℚ) → a ≤ b Q.+ two → b ≤ c Q.+ 1 → c ≤ R →
    a ≤ dyadicRadius (suc (suc d))
  sampleBound a b c ab bc cr = isTrans≤ a ((R Q.+ 1) Q.+ two) (dyadicRadius (suc (suc d)))
    (isTrans≤ a (b Q.+ two) ((R Q.+ 1) Q.+ two) ab
      (≤-+o b (R Q.+ 1) two
        (isTrans≤ b (c Q.+ 1) (R Q.+ 1) bc (≤-+o c R 1 cr))))
    (≤Monotone+ (R Q.+ 1) (R Q.+ R) two (R Q.+ R)
      (≤Monotone+ R R 1 R (isRefl≤ R) one≤R) two≤2R)

  radiusBound : (n : ℕ) →
    (approximation x n ≤ approximation y n Q.+ precision 0) ×
    (approximation y n ≤ approximation x n Q.+ precision 0) →
    RB.canonicalRadius y ≤ dyadicRadius (nearbyExponent x)
  radiusBound n h =
    let xN = approximation x n
        yN = approximation y n
        y0 = approximation y 0
        positive = sampleBound y0 yN xN
          (tighten-two-errors y0 yN (precision n) (precision 0) two
            (RB.precision-pair≤two n) (close-backward y n 0))
          (snd h) (isTrans≤ xN (RB.canonicalRadius x) R (RB.positive-upper xb n) radiusX≤R)
        negative = sampleBound (Q.- y0) (Q.- yN) (Q.- xN)
          (tighten-two-errors (Q.- y0) (Q.- yN) (precision n) (precision 0) two
            (RB.precision-pair≤two n)
            (negate-two-error-bound yN y0 (precision n) (precision 0) (close-forward y n 0)))
          (negate-one-error-bound xN yN 1 (fst h))
          (isTrans≤ (Q.- xN) (RB.canonicalRadius x) R (RB.negative-upper xb n) radiusX≤R)
        R4 = dyadicRadius (suc (suc d))
        maxBound = subst (Q.max y0 (Q.- y0) ≤_) (≤→max R4 R4 (isRefl≤ R4))
          (≤MonotoneMax y0 R4 (Q.- y0) R4 positive negative)
    in ≤Monotone+ (Q.max y0 (Q.- y0)) R4 two R4 maxBound two≤4R
