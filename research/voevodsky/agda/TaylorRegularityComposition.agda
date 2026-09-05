{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module TaylorRegularityComposition where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ; suc)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyMetricEquivalence using (compose-bound)
open import CauchyProductBounds
open import CauchyProductCongruence using (single-difference-bound→directed)
open import CauchyProductRegularity using (difference-upper→directed)

module HalfErrorPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  reverse-difference : (a b : fst R) →
    -S (a +S (-S b)) ≡ b +S (-S a)
  reverse-difference a b = solve! R

  collect-halves : (c halfM halfN : fst R) →
    (c +S (halfM +S halfN)) +S (halfM +S halfN) ≡
    (c +S (halfM +S halfM)) +S (halfN +S halfN)
  collect-halves c halfM halfN = solve! R

magnitude-bound-forward : (a b error : Q.ℚ) →
  MagnitudeBound (a Q.+ (Q.- b)) error → a ≤ b Q.+ error
magnitude-bound-forward a b error bound =
  single-difference-bound→directed a b error (positive-upper bound)

magnitude-bound-backward : (a b error : Q.ℚ) →
  MagnitudeBound (a Q.+ (Q.- b)) error → b ≤ a Q.+ error
magnitude-bound-backward a b error bound =
  single-difference-bound→directed b a error
    (subst (_≤ error)
      (HalfErrorPaths.reverse-difference PreferredℚCommRing a b)
      (negative-upper bound))

compose-half-precision-pairs : (a b c : Q.ℚ) (m n : ℕ) →
  a ≤ b Q.+ (precision (suc m) Q.+ precision (suc n)) →
  b ≤ (c Q.+ precision (suc m)) Q.+ precision (suc n) →
  a ≤ (c Q.+ precision m) Q.+ precision n
compose-half-precision-pairs a b c m n a≤b+halves b≤c+halves =
  let halfM = precision (suc m)
      halfN = precision (suc n)
      first = isTrans≤ a
        (b Q.+ (halfM Q.+ halfN))
        (((c Q.+ halfM) Q.+ halfN) Q.+ (halfM Q.+ halfN))
        a≤b+halves
        (≤-+o b ((c Q.+ halfM) Q.+ halfN)
          (halfM Q.+ halfN) b≤c+halves)
      normalizeTail : (c Q.+ halfM) Q.+ halfN ≡
        c Q.+ (halfM Q.+ halfN)
      normalizeTail = sym (Q.+Assoc c halfM halfN)
      collected :
        (((c Q.+ halfM) Q.+ halfN) Q.+ (halfM Q.+ halfN)) ≡
        (c Q.+ (halfM Q.+ halfM)) Q.+ (halfN Q.+ halfN)
      collected =
        cong (Q._+ (halfM Q.+ halfN)) normalizeTail ∙
        HalfErrorPaths.collect-halves PreferredℚCommRing c halfM halfN
      collapsed :
        (c Q.+ (halfM Q.+ halfM)) Q.+ (halfN Q.+ halfN) ≡
        (c Q.+ precision m) Q.+ precision n
      collapsed = cong₂ (λ u v → (c Q.+ u) Q.+ v)
        (precision-refines-double m) (precision-refines-double n)
  in
  subst (a ≤_) (collected ∙ collapsed) first

compose-five-third-refinement : (a b c d e f : Q.ℚ) (k : ℕ) →
  a ≤ b Q.+ precision (suc (suc (suc k))) →
  b ≤ c Q.+ precision (suc (suc (suc k))) →
  c ≤ d Q.+ precision (suc (suc (suc k))) →
  d ≤ e Q.+ precision (suc (suc (suc k))) →
  e ≤ f Q.+ precision (suc (suc (suc k))) →
  a ≤ f Q.+ precision k
compose-five-third-refinement a b c d e f k ab bc cd de ef =
  let k1 = suc k
      k2 = suc k1
      k3 = suc k2
      ac = compose-bound a b c k2 ab bc
      ce = compose-bound c d e k2 cd de
      ae = compose-bound a c e k1 ac ce
      p3≤p1 = isTrans≤ (precision k3) (precision k2) (precision k1)
        (precision-step≤ k2) (precision-step≤ k1)
      efWidened = isTrans≤ e (f Q.+ precision k3)
        (f Q.+ precision k1) ef
        (≤Monotone+ f f (precision k3) (precision k1)
          (isRefl≤ f) p3≤p1)
  in
  compose-bound a e f k ae efWidened
