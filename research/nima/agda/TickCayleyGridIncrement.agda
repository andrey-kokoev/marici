{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyGridIncrement where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as N using (ℕ; zero; suc)
open import Cubical.Data.NatPlusOne as P using (ℕ₊₁; 1+_; ℕ₊₁→ℕ)
import Cubical.Data.NatPlusOne.Properties as PP
import Cubical.Data.Int as Z
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Tactics.NatSolver using (solveℕ!)
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import CauchyProductBounds
open import TaylorTermBounds using (nonnegative-bound-product)
open import RegularCauchyStructure using (≤-add-nonnegative; precision-nonnegative)
open import TickAtanDerivativeAlgebra using (positive-product; positive-fractions-equal)
import Cubical.Data.Int.Order as ZO

positive-addition : (a b : ℕ) (d e : ℕ₊₁) →
  Q.[ Z.pos a / d ] Q.+ Q.[ Z.pos b / e ] ≡
  Q.[ Z.pos (a N.· ℕ₊₁→ℕ e N.+ b N.· ℕ₊₁→ℕ d) / d PP.·₊₁ e ]
positive-addition a b d e = cong (λ z → Q.[ z / d PP.·₊₁ e ])
  (cong₂ Z._+_ (sym (Z.pos·pos a (ℕ₊₁→ℕ e))) (sym (Z.pos·pos b (ℕ₊₁→ℕ d)))
    ∙ sym (Z.pos+ (a N.· ℕ₊₁→ℕ e) (b N.· ℕ₊₁→ℕ d)))

gridValue : ℕ → ℕ → Q.ℚ
gridValue n d = Q.[ Z.pos n / 1+ d ]

grid-value-nonnegative : (n d : ℕ) → 0 ≤ gridValue n d
grid-value-nonnegative n d = subst (Z.pos zero ZO.≤_) (sym (Z.·IdR (Z.pos n))) ZO.zero-≤pos

-- For x=n/D and y=m/D, 1+xy=(D²+nm)/D². Its reciprocal is
-- constructed as a positive raw fraction, not postulated as a field inverse.
inverseIndex : ℕ → ℕ → ℕ → ℕ
inverseIndex n m d = (d N.+ d N.· suc d) N.+ n N.· m

gridProductInverse : ℕ → ℕ → ℕ → Q.ℚ
gridProductInverse n m d = Q.[ Z.pos (suc d N.· suc d) / 1+ inverseIndex n m d ]

module Paths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  expand : (x y p : fst R) → (1r +S x ·S y) ·S p ≡ p +S (x ·S y) ·S p
  expand x y p = solve! R
  insert : (x y p r : fst R) →
    ((y +S (-S x)) ·S p) +S (-S ((y +S (-S x)) ·S r)) ≡
    (((y +S (-S x)) ·S p) ·S 1r) +S (-S (((y +S (-S x)) ·S r) ·S 1r))
  insert x y p r = solve! R
  cancellation : (x y p r : fst R) →
    (((y +S (-S x)) ·S p) ·S ((1r +S x ·S x) ·S r)) +S
    (-S (((y +S (-S x)) ·S r) ·S ((1r +S x ·S y) ·S p))) ≡
    -S ((((x ·S ((y +S (-S x)) ·S (y +S (-S x)))) ·S p) ·S r))
  cancellation x y p r = solve! R
module R = Paths PreferredℚCommRing

abstract
  grid-product-inverse-law : (n m d : ℕ) →
    (1 Q.+ gridValue n d Q.· gridValue m d) Q.· gridProductInverse n m d ≡ 1
  grid-product-inverse-law n m d = R.expand (gridValue n d) (gridValue m d) (gridProductInverse n m d)
    ∙ cong (gridProductInverse n m d Q.+_)
      (cong (Q._· gridProductInverse n m d) (positive-product n m (1+ d) (1+ d))
        ∙ positive-product (n N.· m) (suc d N.· suc d) ((1+ d) PP.·₊₁ (1+ d)) (1+ inverseIndex n m d)
        ∙ positive-fractions-equal ((n N.· m) N.· (suc d N.· suc d)) (n N.· m)
          (((1+ d) PP.·₊₁ (1+ d)) PP.·₊₁ (1+ inverseIndex n m d)) (1+ inverseIndex n m d) (solveℕ!))
    ∙ positive-addition (suc d N.· suc d) (n N.· m) (1+ inverseIndex n m d) (1+ inverseIndex n m d)
    ∙ positive-fractions-equal ((suc d N.· suc d) N.· suc (inverseIndex n m d) N.+ (n N.· m) N.· suc (inverseIndex n m d)) (suc zero)
      ((1+ inverseIndex n m d) PP.·₊₁ (1+ inverseIndex n m d)) (1+ zero) (solveℕ!)

  grid-product-inverse-nonnegative : (n m d : ℕ) → 0 ≤ gridProductInverse n m d
  grid-product-inverse-nonnegative n m d =
    grid-value-nonnegative (suc d N.· suc d) (inverseIndex n m d)

  grid-product-inverse≤one : (n m d : ℕ) → gridProductInverse n m d ≤ 1
  grid-product-inverse≤one n m d =
    subst2 _≤_ (Q.·IdR p) (Q.·Comm p (1 Q.+ x Q.· y) ∙ grid-product-inverse-law n m d)
      (left-multiply-monotone p 1 (1 Q.+ x Q.· y) (grid-product-inverse-nonnegative n m d)
        (≤-add-nonnegative 1 (x Q.· y) (nonnegative-bound-product x y (grid-value-nonnegative n d) (grid-value-nonnegative m d))))
    where
    x y p : Q.ℚ
    x = gridValue n d
    y = gridValue m d
    p = gridProductInverse n m d

  rational-increment-cancellation : (x y p r : Q.ℚ) →
    (1 Q.+ x Q.· y) Q.· p ≡ 1 → (1 Q.+ x Q.· x) Q.· r ≡ 1 →
    ((y Q.+ (Q.- x)) Q.· p) Q.+ (Q.- ((y Q.+ (Q.- x)) Q.· r)) ≡
    Q.- ((((x Q.· ((y Q.+ (Q.- x)) Q.· (y Q.+ (Q.- x)))) Q.· p) Q.· r))
  rational-increment-cancellation x y p r xy xx = R.insert x y p r
    ∙ cong₂ Q._+_
      (cong (((y Q.+ (Q.- x)) Q.· p) Q.·_) (sym xx))
      (cong Q.-_ (cong (((y Q.+ (Q.- x)) Q.· r) Q.·_) (sym xy)))
    ∙ R.cancellation x y p r

  grid-increment-cancellation : (n m d : ℕ) →
    ((gridValue m d Q.+ (Q.- gridValue n d)) Q.· gridProductInverse n m d) Q.+
    (Q.- ((gridValue m d Q.+ (Q.- gridValue n d)) Q.· gridProductInverse n n d)) ≡
    Q.- ((((gridValue n d Q.· ((gridValue m d Q.+ (Q.- gridValue n d)) Q.·
      (gridValue m d Q.+ (Q.- gridValue n d)))) Q.· gridProductInverse n m d) Q.· gridProductInverse n n d))
  grid-increment-cancellation n m d = rational-increment-cancellation
    (gridValue n d) (gridValue m d) (gridProductInverse n m d) (gridProductInverse n n d)
    (grid-product-inverse-law n m d) (grid-product-inverse-law n n d)

  grid-increment-quadratic-bound : (n m d : ℕ) (X e : Q.ℚ) →
    0 ≤ X → 0 ≤ e → MagnitudeBound (gridValue n d) X →
    MagnitudeBound (gridValue m d Q.+ (Q.- gridValue n d)) e →
    MagnitudeBound
      (((gridValue m d Q.+ (Q.- gridValue n d)) Q.· gridProductInverse n m d) Q.+
        (Q.- ((gridValue m d Q.+ (Q.- gridValue n d)) Q.· gridProductInverse n n d)))
      (X Q.· (e Q.· e))
  grid-increment-quadratic-bound n m d X e Xh eh hx hd = transport-magnitude
    ((delta Q.· p) Q.+ (Q.- (delta Q.· r))) (Q.- (((x Q.· (delta Q.· delta)) Q.· p) Q.· r))
    (X Q.· (e Q.· e)) (grid-increment-cancellation n m d)
    (negate-magnitude-bound (((x Q.· (delta Q.· delta)) Q.· p) Q.· r) (X Q.· (e Q.· e))
      (subst (MagnitudeBound (((x Q.· (delta Q.· delta)) Q.· p) Q.· r)) (Q.·IdR (X Q.· (e Q.· e)))
        (nonnegative-multiplier-bound ((x Q.· (delta Q.· delta)) Q.· p) (X Q.· (e Q.· e)) r 1 Xeeh
          (subst (MagnitudeBound ((x Q.· (delta Q.· delta)) Q.· p)) (Q.·IdR (X Q.· (e Q.· e)))
            (nonnegative-multiplier-bound (x Q.· (delta Q.· delta)) (X Q.· (e Q.· e)) p 1 Xeeh
              (arbitrary-multiplier-bound x X (delta Q.· delta) (e Q.· e) Xh eeh hx
                (arbitrary-multiplier-bound delta e delta e eh eh hd hd))
              (grid-product-inverse-nonnegative n m d) (grid-product-inverse≤one n m d)))
          (grid-product-inverse-nonnegative n n d) (grid-product-inverse≤one n n d))))
    where
    x delta p r : Q.ℚ
    x = gridValue n d
    delta = gridValue m d Q.+ (Q.- gridValue n d)
    p = gridProductInverse n m d
    r = gridProductInverse n n d
    eeh : 0 ≤ e Q.· e
    eeh = nonnegative-bound-product e e eh eh
    Xeeh : 0 ≤ X Q.· (e Q.· e)
    Xeeh = nonnegative-bound-product X (e Q.· e) Xh eeh
