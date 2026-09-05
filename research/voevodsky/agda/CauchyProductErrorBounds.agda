{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyProductErrorBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; suc; _+_)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Data.Rationals.Order
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import CauchyProductBounds
import CauchyNegation

module ProductScalePaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_)

  factor-right : (a b e : fst R) →
    (a ·S e) +S (b ·S e) ≡ (a +S b) ·S e
  factor-right a b e = solve! R

  distribute-left : (r p q : fst R) →
    r ·S (p +S q) ≡ (r ·S p) +S (r ·S q)
  distribute-left r p q = solve! R

weaken-magnitude-bound : (a A B : Q.ℚ) →
  A ≤ B → MagnitudeBound a A → MagnitudeBound a B
weaken-magnitude-bound a A B A≤B bound .positive-upper =
  isTrans≤ a A B (positive-upper bound) A≤B
weaken-magnitude-bound a A B A≤B bound .negative-upper =
  isTrans≤ (Q.- a) A B (negative-upper bound) A≤B

precision-sum-nonnegative : (m n : ℕ) →
  0 ≤ precision m Q.+ precision n
precision-sum-nonnegative m n =
  ≤Monotone+ 0 (precision m) 0 (precision n)
    (precision-nonnegative m) (precision-nonnegative n)

cauchy-difference-bound : (x : RegularCauchy) (m n : ℕ) →
  MagnitudeBound
    (approximation x m Q.+ (Q.- approximation x n))
    (precision m Q.+ precision n)
cauchy-difference-bound x m n =
  difference-magnitude-bound
    (approximation x m) (approximation x n)
    (precision m Q.+ precision n)
    (subst (approximation x m ≤_)
      (sym (Q.+Assoc (approximation x n) (precision m) (precision n)))
      (close-forward x m n))
    (subst (approximation x n ≤_)
      (sym (Q.+Assoc (approximation x m) (precision m) (precision n)))
      (close-backward x m n))

bounded-value : (x : DyadicallyBoundedRegularCauchy) (n : ℕ) →
  MagnitudeBound (approximation (regular x) n)
    (dyadicRadius (radius-exponent x))
bounded-value x n .positive-upper = upper-bound x n
bounded-value x n .negative-upper =
  subst (Q.- approximation (regular x) n ≤_)
    (Q.+IdR (Q.- Q.- dyadicRadius (radius-exponent x)) ∙
     Q.-Invol (dyadicRadius (radius-exponent x)))
    (CauchyNegation.negate-one-error-bound
      (Q.- dyadicRadius (radius-exponent x))
      (approximation (regular x) n) 0
      (subst (Q.- dyadicRadius (radius-exponent x) ≤_)
        (sym (Q.+IdR (approximation (regular x) n)))
        (lower-bound x n)))

first-product-error-bound :
  (x y : DyadicallyBoundedRegularCauchy) (m n : ℕ) →
  MagnitudeBound
    (approximation (regular x) m Q.·
      (approximation (regular y) m Q.+
       (Q.- approximation (regular y) n)))
    (dyadicRadius (radius-exponent x) Q.·
      (precision m Q.+ precision n))
first-product-error-bound x y m n =
  arbitrary-multiplier-bound
    (approximation (regular x) m)
    (dyadicRadius (radius-exponent x))
    (approximation (regular y) m Q.+
      (Q.- approximation (regular y) n))
    (precision m Q.+ precision n)
    (dyadicRadius-nonnegative (radius-exponent x))
    (precision-sum-nonnegative m n)
    (bounded-value x m)
    (cauchy-difference-bound (regular y) m n)

second-product-error-bound :
  (x y : DyadicallyBoundedRegularCauchy) (m n : ℕ) →
  MagnitudeBound
    (approximation (regular y) n Q.·
      (approximation (regular x) m Q.+
       (Q.- approximation (regular x) n)))
    (dyadicRadius (radius-exponent y) Q.·
      (precision m Q.+ precision n))
second-product-error-bound x y m n =
  arbitrary-multiplier-bound
    (approximation (regular y) n)
    (dyadicRadius (radius-exponent y))
    (approximation (regular x) m Q.+
      (Q.- approximation (regular x) n))
    (precision m Q.+ precision n)
    (dyadicRadius-nonnegative (radius-exponent y))
    (precision-sum-nonnegative m n)
    (bounded-value y n)
    (cauchy-difference-bound (regular x) m n)

decomposed-product-error-bound :
  (x y : DyadicallyBoundedRegularCauchy) (m n : ℕ) →
  MagnitudeBound
    ((approximation (regular x) m Q.·
       (approximation (regular y) m Q.+
        (Q.- approximation (regular y) n))) Q.+
     (approximation (regular y) n Q.·
       (approximation (regular x) m Q.+
        (Q.- approximation (regular x) n))))
    ((dyadicRadius (radius-exponent x) Q.·
       (precision m Q.+ precision n)) Q.+
     (dyadicRadius (radius-exponent y) Q.·
       (precision m Q.+ precision n)))
decomposed-product-error-bound x y m n =
  add-magnitude-bounds _ _ _ _
    (first-product-error-bound x y m n)
    (second-product-error-bound x y m n)

scale-cancels-refined-error : (d m n : ℕ) →
  dyadicRadius d Q.·
    (precision (d ℕ.+ m) Q.+ precision (d ℕ.+ n)) ≡
  precision m Q.+ precision n
scale-cancels-refined-error d m n =
  ProductScalePaths.distribute-left PreferredℚCommRing
    (dyadicRadius d) (precision (d ℕ.+ m)) (precision (d ℕ.+ n)) ∙
  cong₂ Q._+_
    (radius-cancels-precision-shift d m)
    (radius-cancels-precision-shift d n)

refined-error-scale-bound : (dx dy m n : ℕ) →
  let d = suc (dx ℕ.+ dy)
      e = precision (d ℕ.+ m) Q.+ precision (d ℕ.+ n)
  in
  (dyadicRadius dx Q.· e) Q.+ (dyadicRadius dy Q.· e) ≤
  precision m Q.+ precision n
refined-error-scale-bound dx dy m n =
  let d = suc (dx ℕ.+ dy)
      e = precision (d ℕ.+ m) Q.+ precision (d ℕ.+ n)
  in
  subst2 _≤_
    (sym (ProductScalePaths.factor-right PreferredℚCommRing
      (dyadicRadius dx) (dyadicRadius dy) e))
    (scale-cancels-refined-error d m n)
    (≤-·o
      (dyadicRadius dx Q.+ dyadicRadius dy)
      (dyadicRadius d) e
      (precision-sum-nonnegative (d ℕ.+ m) (d ℕ.+ n))
      (radius-sum≤successor-combined dx dy))

refined-decomposed-product-error-bound :
  (x y : DyadicallyBoundedRegularCauchy) (m n : ℕ) →
  let d = suc (radius-exponent x ℕ.+ radius-exponent y)
  in
  MagnitudeBound
    ((approximation (regular x) (d ℕ.+ m) Q.·
       (approximation (regular y) (d ℕ.+ m) Q.+
        (Q.- approximation (regular y) (d ℕ.+ n)))) Q.+
     (approximation (regular y) (d ℕ.+ n) Q.·
       (approximation (regular x) (d ℕ.+ m) Q.+
        (Q.- approximation (regular x) (d ℕ.+ n)))))
    (precision m Q.+ precision n)
refined-decomposed-product-error-bound x y m n =
  let d = suc (radius-exponent x ℕ.+ radius-exponent y)
      e = precision (d ℕ.+ m) Q.+ precision (d ℕ.+ n)
      original = decomposed-product-error-bound x y (d ℕ.+ m) (d ℕ.+ n)
  in
  weaken-magnitude-bound _
    ((dyadicRadius (radius-exponent x) Q.· e) Q.+
     (dyadicRadius (radius-exponent y) Q.· e))
    (precision m Q.+ precision n)
    (refined-error-scale-bound
      (radius-exponent x) (radius-exponent y) m n)
    original
