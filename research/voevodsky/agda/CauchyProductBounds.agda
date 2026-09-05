{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module CauchyProductBounds where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Relation.Nullary
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate
import CauchyNegation

record MagnitudeBound (a A : Q.ℚ) : Type where
  field
    positive-upper : a ≤ A
    negative-upper : Q.- a ≤ A
open MagnitudeBound public

left-multiply-monotone : (a b c : Q.ℚ) →
  0 ≤ a → b ≤ c → a Q.· b ≤ a Q.· c
left-multiply-monotone a b c 0≤a b≤c =
  subst2 _≤_ (Q.·Comm b a) (Q.·Comm c a)
    (≤-·o b c a 0≤a b≤c)

module ProductSignPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)

  negative-product : (a b : fst R) →
    -S (a ·S b) ≡ (-S a) ·S b
  negative-product a b = solve! R

  double-negative-product : (a b : fst R) →
    a ·S b ≡ (-S a) ·S (-S b)
  double-negative-product a b = solve! R

  negative-zero : -S 0r ≡ 0r
  negative-zero = solve! R

  cancel-translated : (b e : fst R) →
    (b +S e) +S (-S b) ≡ e
  cancel-translated b e = solve! R

  negative-difference : (a b : fst R) →
    -S (a +S (-S b)) ≡ b +S (-S a)
  negative-difference a b = solve! R

  negative-sum : (a b : fst R) →
    -S (a +S b) ≡ (-S a) +S (-S b)
  negative-sum a b = solve! R

add-magnitude-bounds : (a A b B : Q.ℚ) →
  MagnitudeBound a A → MagnitudeBound b B →
  MagnitudeBound (a Q.+ b) (A Q.+ B)
add-magnitude-bounds a A b B aBound bBound .positive-upper =
  ≤Monotone+ a A b B (positive-upper aBound) (positive-upper bBound)
add-magnitude-bounds a A b B aBound bBound .negative-upper =
  subst (_≤ A Q.+ B)
    (sym (ProductSignPaths.negative-sum PreferredℚCommRing a b))
    (≤Monotone+ (Q.- a) A (Q.- b) B
      (negative-upper aBound) (negative-upper bBound))

one-sided-difference-bound : (a b e : Q.ℚ) →
  a ≤ b Q.+ e → a Q.+ (Q.- b) ≤ e
one-sided-difference-bound a b e a≤b+e =
  subst (a Q.+ (Q.- b) ≤_)
    (ProductSignPaths.cancel-translated PreferredℚCommRing b e)
    (≤-+o a (b Q.+ e) (Q.- b) a≤b+e)

difference-magnitude-bound : (a b e : Q.ℚ) →
  a ≤ b Q.+ e → b ≤ a Q.+ e →
  MagnitudeBound (a Q.+ (Q.- b)) e
difference-magnitude-bound a b e a≤b+e b≤a+e .positive-upper =
  one-sided-difference-bound a b e a≤b+e
difference-magnitude-bound a b e a≤b+e b≤a+e .negative-upper =
  subst (_≤ e)
    (sym (ProductSignPaths.negative-difference PreferredℚCommRing a b))
    (one-sided-difference-bound b a e b≤a+e)

nonpositive→negative-nonnegative : (b : Q.ℚ) → b ≤ 0 → 0 ≤ Q.- b
nonpositive→negative-nonnegative b b≤0 =
  subst2 _≤_
    (ProductSignPaths.negative-zero PreferredℚCommRing)
    (Q.+IdR (Q.- b))
    (CauchyNegation.negate-one-error-bound b 0 0
      (subst (b ≤_) (sym (Q.+IdR 0)) b≤0))

negate-magnitude-bound : (a A : Q.ℚ) →
  MagnitudeBound a A → MagnitudeBound (Q.- a) A
negate-magnitude-bound a A bound .positive-upper = negative-upper bound
negate-magnitude-bound a A bound .negative-upper =
  subst (_≤ A) (sym (Q.-Invol a)) (positive-upper bound)

transport-magnitude : (a a′ A : Q.ℚ) →
  a ≡ a′ → MagnitudeBound a′ A → MagnitudeBound a A
transport-magnitude a a′ A p bound .positive-upper =
  subst (_≤ A) (sym p) (positive-upper bound)
transport-magnitude a a′ A p bound .negative-upper =
  subst (λ z → Q.- z ≤ A) (sym p) (negative-upper bound)

nonnegative-multiplier-bound :
  (a A b B : Q.ℚ) →
  0 ≤ A → MagnitudeBound a A →
  0 ≤ b → b ≤ B →
  MagnitudeBound (a Q.· b) (A Q.· B)
nonnegative-multiplier-bound a A b B 0≤A bound 0≤b b≤B
  .positive-upper =
    isTrans≤ (a Q.· b) (A Q.· b) (A Q.· B)
      (≤-·o a A b 0≤b (positive-upper bound))
      (left-multiply-monotone A b B 0≤A b≤B)
nonnegative-multiplier-bound a A b B 0≤A bound 0≤b b≤B
  .negative-upper =
    subst (_≤ A Q.· B)
      (sym (ProductSignPaths.negative-product PreferredℚCommRing a b))
      (isTrans≤ ((Q.- a) Q.· b) (A Q.· b) (A Q.· B)
        (≤-·o (Q.- a) A b 0≤b (negative-upper bound))
        (left-multiply-monotone A b B 0≤A b≤B))

arbitrary-multiplier-bound :
  (a A b B : Q.ℚ) →
  0 ≤ A → 0 ≤ B →
  MagnitudeBound a A → MagnitudeBound b B →
  MagnitudeBound (a Q.· b) (A Q.· B)
arbitrary-multiplier-bound a A b B 0≤A 0≤B aBound bBound
  with <Dec b 0
... | no b≮0 =
  nonnegative-multiplier-bound a A b B 0≤A aBound
    (≮→≥ b 0 b≮0) (positive-upper bBound)
... | yes b<0 =
  transport-magnitude (a Q.· b) ((Q.- a) Q.· (Q.- b)) (A Q.· B)
    (ProductSignPaths.double-negative-product PreferredℚCommRing a b)
    (nonnegative-multiplier-bound (Q.- a) A (Q.- b) B
      0≤A (negate-magnitude-bound a A aBound)
      (nonpositive→negative-nonnegative b (<Weaken≤ b 0 b<0))
      (negative-upper bBound))

-- Sequence bounds can be projected pointwise into the value-level interface.
pointwise-magnitude :
  {x : Type} → (value : x → Q.ℚ) → (A : Q.ℚ) →
  ((i : x) → value i ≤ A) →
  ((i : x) → Q.- value i ≤ A) →
  (i : x) → MagnitudeBound (value i) A
pointwise-magnitude value A upper lower i .positive-upper = upper i
pointwise-magnitude value A upper lower i .negative-upper = lower i
