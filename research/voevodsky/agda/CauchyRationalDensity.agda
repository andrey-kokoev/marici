{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyRationalDensity where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; max)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyMetricEquivalence
open import CauchyShift
open import DyadicallyBoundedCauchy

eventuallyWithin-weaken :
  (x y : RegularCauchy) (loose tight : ℕ) →
  ℕOrder._≤_ loose tight →
  EventuallyWithin x y tight → EventuallyWithin x y loose
eventuallyWithin-weaken x y loose tight loose≤tight =
  PT.map λ { (N , bounds) →
    N , λ n N≤n →
      let old = bounds n N≤n
          error≤ = precision-antitone loose tight loose≤tight
      in
      isTrans≤
        (approximation x n)
        (approximation y n Q.+ precision tight)
        (approximation y n Q.+ precision loose)
        (fst old)
        (≤Monotone+
          (approximation y n) (approximation y n)
          (precision tight) (precision loose)
          (isRefl≤ (approximation y n)) error≤) ,
      isTrans≤
        (approximation y n)
        (approximation x n Q.+ precision tight)
        (approximation x n Q.+ precision loose)
        (snd old)
        (≤Monotone+
          (approximation x n) (approximation x n)
          (precision tight) (precision loose)
          (isRefl≤ (approximation x n)) error≤) }

rational-approximation-eventually-within :
  (x : RegularCauchy) (k N : ℕ) →
  ℕOrder._≤_ (suc k) N →
  EventuallyWithin (constantCauchy (approximation x N)) x k
rational-approximation-eventually-within x k N sk≤N =
  ∣ (suc N , λ n sucN≤n →
    let error≤ = isTrans≤
          (precision N Q.+ precision n)
          (precision N Q.+ precision (suc N))
          (precision k)
          (≤Monotone+
            (precision N) (precision N)
            (precision n) (precision (suc N))
            (isRefl≤ (precision N))
            (precision-antitone (suc N) n sucN≤n))
          (shift-error≤ k N sk≤N)
    in
    tighten-two-errors
      (approximation x N) (approximation x n)
      (precision N) (precision n) (precision k)
      error≤ (close-forward x N n) ,
    tighten-two-errors
      (approximation x n) (approximation x N)
      (precision N) (precision n) (precision k)
      error≤ (close-backward x N n)) ∣₁

rational-approximation-dense :
  (x : RegularCauchy) (k : ℕ) →
  EventuallyWithin
    (constantCauchy (approximation x (suc k))) x k
rational-approximation-dense x k =
  rational-approximation-eventually-within x k (suc k)
    ℕOrder.≤-refl

rational-approximation-class-close :
  (x : RegularCauchy) (k : ℕ) →
  EventuallyWithin
    (constantCauchy (approximation x (suc k))) x k
rational-approximation-class-close = rational-approximation-dense

bounded-rational-approximation-eventually-within :
  (x : DyadicallyBoundedRegularCauchy) (k N : ℕ) →
  ℕOrder._≤_ (suc k) N →
  EventuallyWithin
    (regular (rationalApproximationDyadicallyBounded x N))
    (regular x) k
bounded-rational-approximation-eventually-within x k N sk≤N =
  rational-approximation-eventually-within (regular x) k N sk≤N

bounded-rational-approximation-dense :
  (x : DyadicallyBoundedRegularCauchy) (k : ℕ) →
  EventuallyWithin
    (regular (rationalApproximationDyadicallyBounded x (suc k)))
    (regular x) k
bounded-rational-approximation-dense x k =
  rational-approximation-dense (regular x) k

shared-bounded-rational-centers :
  (x y z : DyadicallyBoundedRegularCauchy) (kx ky kz : ℕ) →
  let common = ℕ.max kx (ℕ.max ky kz)
      N = suc common
      qx = rationalApproximationDyadicallyBounded x N
      qy = rationalApproximationDyadicallyBounded y N
      qz = rationalApproximationDyadicallyBounded z N
  in
  Σ[ xClose ∈ EventuallyWithin (regular qx) (regular x) kx ]
  Σ[ yClose ∈ EventuallyWithin (regular qy) (regular y) ky ]
  EventuallyWithin (regular qz) (regular z) kz
shared-bounded-rational-centers x y z kx ky kz =
  let common = ℕ.max kx (ℕ.max ky kz)
      N = suc common
      kx≤common : ℕOrder._≤_ kx common
      kx≤common = ℕOrder.left-≤-max
      ky≤inner : ℕOrder._≤_ ky (ℕ.max ky kz)
      ky≤inner = ℕOrder.left-≤-max
      kz≤inner : ℕOrder._≤_ kz (ℕ.max ky kz)
      kz≤inner = ℕOrder.right-≤-max
      inner≤common :
        ℕOrder._≤_ (ℕ.max ky kz) (ℕ.max kx (ℕ.max ky kz))
      inner≤common = ℕOrder.right-≤-max {m = kx}
      ky≤common : ℕOrder._≤_ ky common
      ky≤common = ℕOrder.≤-trans ky≤inner inner≤common
      kz≤common : ℕOrder._≤_ kz common
      kz≤common = ℕOrder.≤-trans kz≤inner inner≤common
  in
  bounded-rational-approximation-eventually-within x kx N
    (ℕOrder.suc-≤-suc kx≤common) ,
  bounded-rational-approximation-eventually-within y ky N
    (ℕOrder.suc-≤-suc ky≤common) ,
  bounded-rational-approximation-eventually-within z kz N
    (ℕOrder.suc-≤-suc kz≤common)
