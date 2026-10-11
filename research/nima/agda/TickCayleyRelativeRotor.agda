{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyRelativeRotor where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Relation.Nullary using (yes; no)
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-bound-product)
open import RegularCauchyStructure using (≤-add-nonnegative)
open import TickCayleyGridIncrement using
  (gridValue; gridProductInverse; grid-product-inverse-law; grid-product-inverse-nonnegative)
open import TickAtanCayleyIncrement using (relativeParameter)

square-nonnegative : (q : Q.ℚ) → 0 ≤ q Q.· q
square-nonnegative q with <Dec q 0
... | no h = nonnegative-bound-product q q (≮→≥ q 0 h) (≮→≥ q 0 h)
... | yes h = subst (0 ≤_) (sym (ProductSignPaths.double-negative-product PreferredℚCommRing q q))
  (nonnegative-bound-product (Q.- q) (Q.- q)
    (nonpositive→negative-nonnegative q (<Weaken≤ q 0 h))
    (nonpositive→negative-nonnegative q (<Weaken≤ q 0 h)))

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  expand : (x y p r s : fst R) →
    (1r +S ((y +S (-S x)) ·S p) ·S ((y +S (-S x)) ·S p)) ·S
      (((1r +S x ·S y) ·S (1r +S x ·S y)) ·S (r ·S s)) ≡
    (((1r +S x ·S y) ·S (1r +S x ·S y)) +S
      (((y +S (-S x)) ·S (y +S (-S x))) ·S
        (((1r +S x ·S y) ·S p) ·S ((1r +S x ·S y) ·S p)))) ·S (r ·S s)
  expand x y p r s = solve! R
  finish : (x y r s : fst R) →
    (((1r +S x ·S y) ·S (1r +S x ·S y)) +S
      (((y +S (-S x)) ·S (y +S (-S x))) ·S (1r ·S 1r))) ·S (r ·S s) ≡
    ((1r +S x ·S x) ·S r) ·S ((1r +S y ·S y) ·S s)
  finish x y r s = solve! R
module R = Paths PreferredℚCommRing

abstract
  relative-inverse-from-grid-laws : (x y p r s : Q.ℚ) →
    (1 Q.+ x Q.· y) Q.· p ≡ 1 → (1 Q.+ x Q.· x) Q.· r ≡ 1 → (1 Q.+ y Q.· y) Q.· s ≡ 1 →
    (1 Q.+ ((y Q.+ (Q.- x)) Q.· p) Q.· ((y Q.+ (Q.- x)) Q.· p)) Q.·
      (((1 Q.+ x Q.· y) Q.· (1 Q.+ x Q.· y)) Q.· (r Q.· s)) ≡ 1
  relative-inverse-from-grid-laws x y p r s xy xx yy = R.expand x y p r s
    ∙ cong (λ v → (((1 Q.+ x Q.· y) Q.· (1 Q.+ x Q.· y)) Q.+
      (((y Q.+ (Q.- x)) Q.· (y Q.+ (Q.- x))) Q.· v)) Q.· (r Q.· s)) (cong₂ Q._·_ xy xy)
    ∙ R.finish x y r s ∙ cong₂ Q._·_ xx yy ∙ Q.·IdR 1

relativeInverse : ℕ → ℕ → ℕ → Q.ℚ
relativeInverse n m d =
  ((1 Q.+ gridValue n d Q.· gridValue m d) Q.· (1 Q.+ gridValue n d Q.· gridValue m d)) Q.·
  (gridProductInverse n n d Q.· gridProductInverse m m d)

abstract
  relative-inverse-law : (n m d : ℕ) → (1 Q.+ relativeParameter n m d Q.· relativeParameter n m d) Q.· relativeInverse n m d ≡ 1
  relative-inverse-law n m d = relative-inverse-from-grid-laws (gridValue n d) (gridValue m d)
    (gridProductInverse n m d) (gridProductInverse n n d) (gridProductInverse m m d)
    (grid-product-inverse-law n m d) (grid-product-inverse-law n n d) (grid-product-inverse-law m m d)

  relative-inverse-nonnegative : (n m d : ℕ) → 0 ≤ relativeInverse n m d
  relative-inverse-nonnegative n m d = nonnegative-bound-product
    ((1 Q.+ gridValue n d Q.· gridValue m d) Q.· (1 Q.+ gridValue n d Q.· gridValue m d))
    (gridProductInverse n n d Q.· gridProductInverse m m d)
    (square-nonnegative (1 Q.+ gridValue n d Q.· gridValue m d))
    (nonnegative-bound-product (gridProductInverse n n d) (gridProductInverse m m d)
      (grid-product-inverse-nonnegative n n d) (grid-product-inverse-nonnegative m m d))

  relative-inverse≤one : (n m d : ℕ) → relativeInverse n m d ≤ 1
  relative-inverse≤one n m d = subst2 _≤_ (Q.·IdR (relativeInverse n m d))
    (Q.·Comm (relativeInverse n m d) (1 Q.+ relativeParameter n m d Q.· relativeParameter n m d) ∙ relative-inverse-law n m d)
    (left-multiply-monotone (relativeInverse n m d) 1 (1 Q.+ relativeParameter n m d Q.· relativeParameter n m d)
      (relative-inverse-nonnegative n m d)
      (≤-add-nonnegative 1 (relativeParameter n m d Q.· relativeParameter n m d) (square-nonnegative (relativeParameter n m d))))

relativeCosine relativeSine : ℕ → ℕ → ℕ → Q.ℚ
relativeCosine n m d = (1 Q.+ (Q.- (relativeParameter n m d Q.· relativeParameter n m d))) Q.· relativeInverse n m d
relativeSine n m d = (relativeParameter n m d Q.+ relativeParameter n m d) Q.· relativeInverse n m d
