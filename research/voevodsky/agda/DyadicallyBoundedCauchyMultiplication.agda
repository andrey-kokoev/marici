{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module DyadicallyBoundedCauchyMultiplication where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.HITs.PropositionalTruncation as PT
open import RegularCauchyStructure
open import CauchyNegation
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import CauchyBoundPromotion
open import DyadicallyBoundedCauchy
open import CauchyProductRegularity

boundedProductValue :
  (x y : DyadicallyBoundedRegularCauchy) (n : ℕ) →
  MagnitudeBound
    (approximation (boundedProductRegular x y) n)
    (dyadicRadius (radius-exponent x ℕ.+ radius-exponent y))
boundedProductValue x y n =
  let depth = suc
        (radius-exponent x ℕ.+ radius-exponent y) ℕ.+ n
      rx = dyadicRadius (radius-exponent x)
      ry = dyadicRadius (radius-exponent y)
      productBound = arbitrary-multiplier-bound
        (approximation (regular x) depth) rx
        (approximation (regular y) depth) ry
        (dyadicRadius-nonnegative (radius-exponent x))
        (dyadicRadius-nonnegative (radius-exponent y))
        (bounded-value x depth) (bounded-value y depth)
  in
  subst (MagnitudeBound (approximation (boundedProductRegular x y) n))
    (sym (dyadicRadius-add (radius-exponent x) (radius-exponent y)))
    productBound

multiplyDyadicallyBounded :
  DyadicallyBoundedRegularCauchy → DyadicallyBoundedRegularCauchy →
  DyadicallyBoundedRegularCauchy
multiplyDyadicallyBounded x y .regular = boundedProductRegular x y
multiplyDyadicallyBounded x y .radius-exponent =
  radius-exponent x ℕ.+ radius-exponent y
multiplyDyadicallyBounded x y .lower-bound n =
  let value = approximation (boundedProductRegular x y) n
      radius = dyadicRadius (radius-exponent x ℕ.+ radius-exponent y)
      bound = boundedProductValue x y n
  in
  subst (Q.- radius ≤_)
    (Q.+IdR (Q.- Q.- value) ∙ Q.-Invol value)
    (negate-one-error-bound (Q.- value) radius 0
      (subst ((Q.- value) ≤_) (sym (Q.+IdR radius))
        (negative-upper bound)))
multiplyDyadicallyBounded x y .upper-bound n =
  positive-upper (boundedProductValue x y n)

multiplyDyadicallyBounded-regular :
  (x y : DyadicallyBoundedRegularCauchy) →
  regular (multiplyDyadicallyBounded x y) ≡ boundedProductRegular x y
multiplyDyadicallyBounded-regular x y = refl

boundedProductPresentation :
  (x y : DyadicallyBoundedRegularCauchy) →
  BoundedPresentation (boundedProductRegular x y)
boundedProductPresentation x y = multiplyDyadicallyBounded x y , refl

multiplyBoundedPresentations : {x y : RegularCauchy} →
  (px : BoundedPresentation x) → (py : BoundedPresentation y) →
  BoundedPresentation (boundedProductRegular (fst px) (fst py))
multiplyBoundedPresentations px py =
  boundedProductPresentation (fst px) (fst py)

multiplyTruncatedBoundedPresentations : {x y : RegularCauchy} →
  (px : BoundedPresentation x) → (py : BoundedPresentation y) →
  ∥ BoundedPresentation (boundedProductRegular (fst px) (fst py)) ∥₁
multiplyTruncatedBoundedPresentations px py =
  ∣ multiplyBoundedPresentations px py ∣₁

multiplyDyadicallyBounded-exponent-commutative :
  (x y : DyadicallyBoundedRegularCauchy) →
  radius-exponent (multiplyDyadicallyBounded x y) ≡
  radius-exponent (multiplyDyadicallyBounded y x)
multiplyDyadicallyBounded-exponent-commutative x y =
  ℕ.+-comm (radius-exponent x) (radius-exponent y)

multiplyDyadicallyBounded-exponent-associative :
  (x y z : DyadicallyBoundedRegularCauchy) →
  radius-exponent (multiplyDyadicallyBounded
    (multiplyDyadicallyBounded x y) z) ≡
  radius-exponent (multiplyDyadicallyBounded
    x (multiplyDyadicallyBounded y z))
multiplyDyadicallyBounded-exponent-associative x y z =
  sym (ℕ.+-assoc
    (radius-exponent x) (radius-exponent y) (radius-exponent z))
