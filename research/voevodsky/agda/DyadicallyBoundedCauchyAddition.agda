{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module DyadicallyBoundedCauchyAddition where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import CauchyAddition
open import CauchyNegation
open import CauchyProductBounds
open import CauchyBoundPromotion
open import DyadicallyBoundedCauchy

addDyadicallyBounded :
  DyadicallyBoundedRegularCauchy → DyadicallyBoundedRegularCauchy →
  DyadicallyBoundedRegularCauchy
addDyadicallyBounded x y .regular = addRegular (regular x) (regular y)
addDyadicallyBounded x y .radius-exponent =
  suc (radius-exponent x ℕ.+ radius-exponent y)
addDyadicallyBounded x y .upper-bound n =
  isTrans≤
    (approximation (regular x) (suc n) Q.+
     approximation (regular y) (suc n))
    (dyadicRadius (radius-exponent x) Q.+
     dyadicRadius (radius-exponent y))
    (dyadicRadius (suc (radius-exponent x ℕ.+ radius-exponent y)))
    (≤Monotone+
      (approximation (regular x) (suc n))
      (dyadicRadius (radius-exponent x))
      (approximation (regular y) (suc n))
      (dyadicRadius (radius-exponent y))
      (upper-bound x (suc n)) (upper-bound y (suc n)))
    (radius-sum≤successor-combined
      (radius-exponent x) (radius-exponent y))
addDyadicallyBounded x y .lower-bound n =
  let rx = dyadicRadius (radius-exponent x)
      ry = dyadicRadius (radius-exponent y)
      radius = dyadicRadius (suc (radius-exponent x ℕ.+ radius-exponent y))
      sum≤radius = radius-sum≤successor-combined
        (radius-exponent x) (radius-exponent y)
      negative-radius≤negative-sum : Q.- radius ≤ Q.- (rx Q.+ ry)
      negative-radius≤negative-sum =
        subst (Q.- radius ≤_)
          (Q.+IdR (Q.- (rx Q.+ ry)))
          (negate-one-error-bound (rx Q.+ ry) radius 0
            (subst ((rx Q.+ ry) ≤_) (sym (Q.+IdR radius)) sum≤radius))
      negative-sum≤values :
        Q.- (rx Q.+ ry) ≤
        approximation (regular x) (suc n) Q.+
        approximation (regular y) (suc n)
      negative-sum≤values =
        subst (_≤ approximation (regular x) (suc n) Q.+
          approximation (regular y) (suc n))
          (sym (ProductSignPaths.negative-sum PreferredℚCommRing rx ry))
          (≤Monotone+
            (Q.- rx) (approximation (regular x) (suc n))
            (Q.- ry) (approximation (regular y) (suc n))
            (lower-bound x (suc n)) (lower-bound y (suc n)))
  in
  isTrans≤ (Q.- radius) (Q.- (rx Q.+ ry))
    (approximation (regular x) (suc n) Q.+
     approximation (regular y) (suc n))
    negative-radius≤negative-sum negative-sum≤values

addDyadicallyBounded-regular :
  (x y : DyadicallyBoundedRegularCauchy) →
  regular (addDyadicallyBounded x y) ≡ addRegular (regular x) (regular y)
addDyadicallyBounded-regular x y = refl

bounded-presented-constant-addition-regular :
  (q r : Q.ℚ) →
  (px : BoundedPresentation (constantCauchy q)) →
  (py : BoundedPresentation (constantCauchy r)) →
  regular (addDyadicallyBounded (fst px) (fst py)) ≡
  constantCauchy (q Q.+ r)
bounded-presented-constant-addition-regular q r
    (bx , bxPath) (by , byPath) =
  regularCauchy-ext _ (constantCauchy (q Q.+ r))
    (funExt λ n →
      cong₂ Q._+_
        (cong (λ z → approximation z (suc n)) bxPath)
        (cong (λ z → approximation z (suc n)) byPath))

addBoundedPresentations : {x y : RegularCauchy} →
  BoundedPresentation x → BoundedPresentation y →
  BoundedPresentation (addRegular x y)
addBoundedPresentations (bx , bxPath) (by , byPath) =
  addDyadicallyBounded bx by , cong₂ addRegular bxPath byPath

addTruncatedBoundedPresentations : {x y : RegularCauchy} →
  ∥ BoundedPresentation x ∥₁ → ∥ BoundedPresentation y ∥₁ →
  ∥ BoundedPresentation (addRegular x y) ∥₁
addTruncatedBoundedPresentations = PT.map2 addBoundedPresentations
