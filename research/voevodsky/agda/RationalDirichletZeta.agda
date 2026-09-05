{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module RationalDirichletZeta where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat as ℕ using (ℕ; zero; suc)
import Cubical.Data.Nat.Order as ℕOrder
open import Cubical.Data.Int as ℤ using (pos)
open import Cubical.Data.Int.Properties as ℤProperties
open import Cubical.Data.NatPlusOne as ℕ₊₁ using (1+_)
open import Cubical.Data.NatPlusOne.Properties as ℕ₊₁Properties using (_·₊₁_; ·₊₁-identityˡ)
open import Cubical.Data.Rationals as Q
open import Cubical.Data.Rationals.Order
open import Cubical.Algebra.CommRing
open import Cubical.Algebra.CommRing.Instances.Int
open import Cubical.Tactics.CommRingSolver
import Cubical.Data.Int.Order as ℤOrder
open import Cubical.Relation.Nullary
open import RationalAnalyticSubstrate
open import RegularCauchyStructure
open import DyadicallyBoundedCauchy
open import RationalLogConvergenceContract
open import CauchyProductBounds
open import CauchyProductErrorBounds
open import TaylorTermBounds using (nonnegative-bound-product)
open import RationalTaylorApproximants using
  (reciprocalSuccessor; reciprocalSuccessor-nonnegative;
   reciprocalSuccessor-antitone; reciprocalSuccessor≤one; finiteSum)

rationalPower : Q.ℚ → ℕ → Q.ℚ
rationalPower q zero = 1
rationalPower q (suc exponent) = rationalPower q exponent Q.· q

rational-power-nonnegative : (q : Q.ℚ) (exponent : ℕ) →
  0 ≤ q → 0 ≤ rationalPower q exponent
rational-power-nonnegative q zero 0≤q = ℤOrder.zero-≤pos
rational-power-nonnegative q (suc exponent) 0≤q =
  nonnegative-bound-product (rationalPower q exponent) q
    (rational-power-nonnegative q exponent 0≤q) 0≤q

rationalDirichletTerm : ℕ → ℕ → Q.ℚ
rationalDirichletTerm exponent denominatorIndex =
  rationalPower (reciprocalSuccessor denominatorIndex) exponent

rational-power-add : (q : Q.ℚ) (m n : ℕ) →
  rationalPower q (m ℕ.+ n) ≡ rationalPower q m Q.· rationalPower q n
rational-power-add q m zero =
  cong (rationalPower q) (ℕ.+-zero m) ∙ sym (Q.·IdR (rationalPower q m))
rational-power-add q m (suc n) =
  cong (rationalPower q) (ℕ.+-suc m n) ∙
  cong (Q._· q) (rational-power-add q m n) ∙
  sym (Q.·Assoc (rationalPower q m) (rationalPower q n) q)

dirichlet-rational-power-below-one : (q : Q.ℚ) → 0 ≤ q → q ≤ 1 →
  (n : ℕ) → rationalPower q n ≤ 1
dirichlet-rational-power-below-one q 0≤q q≤one zero = isRefl≤ 1
dirichlet-rational-power-below-one q 0≤q q≤one (suc n) =
  let previous = dirichlet-rational-power-below-one q 0≤q q≤one n
      multiplied = left-multiply-monotone q
        (rationalPower q n) 1 0≤q previous
      reduced = subst2 _≤_
        (Q.·Comm q (rationalPower q n)) (Q.·IdR q) multiplied
  in isTrans≤ (rationalPower q n Q.· q) q 1 reduced q≤one

rational-power-exponent-antitone : (q : Q.ℚ) → 0 ≤ q → q ≤ 1 →
  (m n : ℕ) → ℕOrder._≤_ m n → rationalPower q n ≤ rationalPower q m
rational-power-exponent-antitone q 0≤q q≤one m n (extra , path) =
  let exponentPath : m ℕ.+ extra ≡ n
      exponentPath = ℕ.+-comm m extra ∙ path
      factor≤one = dirichlet-rational-power-below-one q 0≤q q≤one extra
      product≤ = left-multiply-monotone (rationalPower q m)
        (rationalPower q extra) 1
        (rational-power-nonnegative q m 0≤q) factor≤one
      reduced = subst (rationalPower q m Q.· rationalPower q extra ≤_)
        (Q.·IdR (rationalPower q m)) product≤
  in subst (_≤ rationalPower q m)
    (sym (rational-power-add q m extra) ∙
      cong (rationalPower q) exponentPath)
    reduced

rational-dirichlet-term-nonnegative : (exponent denominatorIndex : ℕ) →
  0 ≤ rationalDirichletTerm exponent denominatorIndex
rational-dirichlet-term-nonnegative exponent denominatorIndex =
  rational-power-nonnegative (reciprocalSuccessor denominatorIndex) exponent
    (reciprocalSuccessor-nonnegative denominatorIndex)

module IntegerTelescopingPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
    renaming (_+_ to _+I_; _·_ to _·I_; -_ to -I_)

  successive-difference : (x : fst R) →
    ((x +I 1r) +I 1r) +I (-I (x +I 1r)) ≡ 1r
  successive-difference x = solve! R

  reciprocal-numerator : (d : fst R) →
    (1r ·I (1r ·I (d +I 1r))) +I ((-I 1r) ·I d) ≡ 1r
  reciprocal-numerator d = solve! R

  reciprocal-cross : (d : fst R) →
    1r ·I (d ·I (1r ·I (d +I 1r))) ≡
    ((1r ·I (1r ·I (d +I 1r))) +I ((-I 1r) ·I d)) ·I
      (d ·I (d +I 1r))
  reciprocal-cross d = solve! R

successive-positive-integer-difference : (n : ℕ) →
  pos (suc (suc n)) ℤ.+ (ℤ.- pos (suc n)) ≡ pos 1
successive-positive-integer-difference n =
  IntegerTelescopingPaths.successive-difference ℤCommRing (pos n)

unit-times-successor-denominator : (n : ℕ) →
  Q.ℕ₊₁→ℤ ((1+ 0) ℕ₊₁Properties.·₊₁ (1+ n)) ≡
  Q.ℕ₊₁→ℤ (1+ n)
unit-times-successor-denominator n =
  cong Q.ℕ₊₁→ℤ (ℕ₊₁Properties.·₊₁-identityˡ (1+ n))

successor-denominator-product : (m n : ℕ) →
  Q.ℕ₊₁→ℤ ((1+ m) ℕ₊₁Properties.·₊₁ (1+ n)) ≡
  Q.ℕ₊₁→ℤ (1+ m) ℤ.· Q.ℕ₊₁→ℤ (1+ n)
successor-denominator-product m n =
  ℤProperties.pos·pos (suc m) (suc n)

reciprocal-successor-left-normalizes : (n : ℕ) →
  reciprocalSuccessor n Q.· reciprocalSuccessor (suc n) ≡
  Q.[ pos 1 / (1+ n) ℕ₊₁Properties.·₊₁ (1+ suc n) ]
reciprocal-successor-left-normalizes n =
  cong (λ z → Q.[ z / (1+ n) ℕ₊₁Properties.·₊₁ (1+ suc n) ])
    (ℤProperties.·IdL (pos 1))

reciprocal-successor-right-normalizes : (n : ℕ) →
  reciprocalSuccessor n Q.+ (Q.- reciprocalSuccessor (suc n)) ≡
  Q.[ pos 1 / (1+ n) ℕ₊₁Properties.·₊₁ (1+ suc n) ]
reciprocal-successor-right-normalizes n =
  cong₂ Q.[_/_]
    numeratorPath denominatorPath
  where
  d = 1+ n
  e = 1+ suc n
  denominatorPath :
    d ℕ₊₁Properties.·₊₁ ((1+ 0) ℕ₊₁Properties.·₊₁ e) ≡
    d ℕ₊₁Properties.·₊₁ e
  denominatorPath = cong (d ℕ₊₁Properties.·₊₁_)
    (ℕ₊₁Properties.·₊₁-identityˡ e)
  numeratorPath :
    (pos 1 ℤ.· Q.ℕ₊₁→ℤ ((1+ 0) ℕ₊₁Properties.·₊₁ e)) ℤ.+
      ((ℤ.- pos 1) ℤ.· Q.ℕ₊₁→ℤ d) ≡ pos 1
  numeratorPath =
    cong (λ z → (pos 1 ℤ.· z) ℤ.+ ((ℤ.- pos 1) ℤ.· Q.ℕ₊₁→ℤ d))
      (unit-times-successor-denominator (suc n)) ∙
    IntegerTelescopingPaths.reciprocal-numerator ℤCommRing (pos (suc n))

reciprocal-successor-telescopes : (n : ℕ) →
  reciprocalSuccessor n Q.· reciprocalSuccessor (suc n) ≡
  reciprocalSuccessor n Q.+ (Q.- reciprocalSuccessor (suc n))
reciprocal-successor-telescopes n =
  reciprocal-successor-left-normalizes n ∙
  sym (reciprocal-successor-right-normalizes n)

rational-dirichlet-higher-term≤square : (exponent denominatorIndex : ℕ) →
  ℕOrder._≤_ 2 exponent →
  rationalDirichletTerm exponent denominatorIndex ≤
    rationalDirichletTerm 2 denominatorIndex
rational-dirichlet-higher-term≤square exponent denominatorIndex 2≤exponent =
  rational-power-exponent-antitone
    (reciprocalSuccessor denominatorIndex)
    (reciprocalSuccessor-nonnegative denominatorIndex)
    (reciprocalSuccessor≤one denominatorIndex)
    2 exponent 2≤exponent

rational-square-dirichlet-tail-term-upper : (n : ℕ) →
  rationalDirichletTerm 2 (suc n) ≤
  reciprocalSuccessor n Q.· reciprocalSuccessor (suc n)
rational-square-dirichlet-tail-term-upper n =
  let smaller = reciprocalSuccessor (suc n)
      larger = reciprocalSuccessor n
      smaller≤larger = reciprocalSuccessor-antitone n (suc n)
        ℕOrder.≤-sucℕ
      multiplied = left-multiply-monotone smaller smaller larger
        (reciprocalSuccessor-nonnegative (suc n)) smaller≤larger
  in subst2 _≤_
    (sym (cong (Q._· smaller) (Q.·IdL smaller)))
    (Q.·Comm smaller larger)
    multiplied

rationalDirichletTail : ℕ → ℕ → ℕ → Q.ℚ
rationalDirichletTail exponent boundary zero = 0
rationalDirichletTail exponent boundary (suc count) =
  rationalDirichletTerm exponent (suc boundary) Q.+
  rationalDirichletTail exponent (suc boundary) count

rational-dirichlet-tail-nonnegative : (exponent boundary count : ℕ) →
  0 ≤ rationalDirichletTail exponent boundary count
rational-dirichlet-tail-nonnegative exponent boundary zero = ℤOrder.zero-≤pos
rational-dirichlet-tail-nonnegative exponent boundary (suc count) =
  let termNonnegative = rational-dirichlet-term-nonnegative
        exponent (suc boundary)
      tailNonnegative = rational-dirichlet-tail-nonnegative
        exponent (suc boundary) count
  in isTrans≤ 0 (rationalDirichletTerm exponent (suc boundary))
    (rationalDirichletTail exponent boundary (suc count))
    termNonnegative
    (≤-add-nonnegative (rationalDirichletTerm exponent (suc boundary))
      (rationalDirichletTail exponent (suc boundary) count) tailNonnegative)

rational-dirichlet-tail-append : (exponent boundary count : ℕ) →
  rationalDirichletTail exponent boundary (suc count) ≡
  rationalDirichletTail exponent boundary count Q.+
    rationalDirichletTerm exponent (suc (boundary ℕ.+ count))
rational-dirichlet-tail-append exponent boundary zero =
  Q.+Comm (rationalDirichletTerm exponent (suc boundary)) 0 ∙
  cong (λ endpoint → 0 Q.+ rationalDirichletTerm exponent (suc endpoint))
    (sym (ℕ.+-zero boundary))
rational-dirichlet-tail-append exponent boundary (suc count) =
  cong (rationalDirichletTerm exponent (suc boundary) Q.+_)
    (rational-dirichlet-tail-append exponent (suc boundary) count) ∙
  Q.+Assoc
    (rationalDirichletTerm exponent (suc boundary))
    (rationalDirichletTail exponent (suc boundary) count)
    (rationalDirichletTerm exponent (suc (suc boundary ℕ.+ count))) ∙
  cong (λ endpoint →
      rationalDirichletTail exponent boundary (suc count) Q.+
        rationalDirichletTerm exponent (suc endpoint))
    (sym (ℕ.+-suc boundary count))

rationalSquareTail : ℕ → ℕ → Q.ℚ
rationalSquareTail boundary zero = 0
rationalSquareTail boundary (suc count) =
  rationalDirichletTerm 2 (suc boundary) Q.+
  rationalSquareTail (suc boundary) count

module RationalTailPaths {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; -_ to -S_)

  zero-as-self-difference : (a : fst R) → 0r ≡ a +S (-S a)
  zero-as-self-difference a = solve! R

  collapse-adjacent-differences : (a b c : fst R) →
    (a +S (-S b)) +S (b +S (-S c)) ≡ a +S (-S c)
  collapse-adjacent-differences a b c = solve! R

  add-zero-rotate : (a : fst R) → a +S 0r ≡ 0r +S a
  add-zero-rotate a = solve! R

rational-square-tail-append : (boundary count : ℕ) →
  rationalSquareTail boundary (suc count) ≡
  rationalSquareTail boundary count Q.+
    rationalDirichletTerm 2 (suc (boundary ℕ.+ count))
rational-square-tail-append boundary zero =
  RationalTailPaths.add-zero-rotate PreferredℚCommRing
    (rationalDirichletTerm 2 (suc boundary)) ∙
  cong (λ endpoint → 0 Q.+ rationalDirichletTerm 2 (suc endpoint))
    (sym (ℕ.+-zero boundary))
rational-square-tail-append boundary (suc count) =
  cong (rationalDirichletTerm 2 (suc boundary) Q.+_)
    (rational-square-tail-append (suc boundary) count) ∙
  Q.+Assoc
    (rationalDirichletTerm 2 (suc boundary))
    (rationalSquareTail (suc boundary) count)
    (rationalDirichletTerm 2 (suc (suc boundary ℕ.+ count))) ∙
  cong (λ endpoint →
      rationalSquareTail boundary (suc count) Q.+
        rationalDirichletTerm 2 (suc endpoint))
    (sym (ℕ.+-suc boundary count))

rational-square-tail-telescoping-bound : (boundary count : ℕ) →
  rationalSquareTail boundary count ≤
  reciprocalSuccessor boundary Q.+
    (Q.- reciprocalSuccessor (boundary ℕ.+ count))
rational-square-tail-telescoping-bound boundary zero =
  subst (0 ≤_)
    (RationalTailPaths.zero-as-self-difference PreferredℚCommRing
      (reciprocalSuccessor boundary) ∙
     cong (λ endpoint → reciprocalSuccessor boundary Q.+
       (Q.- reciprocalSuccessor endpoint))
       (sym (ℕ.+-zero boundary)))
    ℤOrder.zero-≤pos
rational-square-tail-telescoping-bound boundary (suc count) =
  let termBound = subst
        (rationalDirichletTerm 2 (suc boundary) ≤_)
        (reciprocal-successor-telescopes boundary)
        (rational-square-dirichlet-tail-term-upper boundary)
      tailBound = rational-square-tail-telescoping-bound (suc boundary) count
      combined = ≤Monotone+
        (rationalDirichletTerm 2 (suc boundary))
        (reciprocalSuccessor boundary Q.+
          (Q.- reciprocalSuccessor (suc boundary)))
        (rationalSquareTail (suc boundary) count)
        (reciprocalSuccessor (suc boundary) Q.+
          (Q.- reciprocalSuccessor (suc boundary ℕ.+ count)))
        termBound tailBound
      collapsed = RationalTailPaths.collapse-adjacent-differences
        PreferredℚCommRing
        (reciprocalSuccessor boundary)
        (reciprocalSuccessor (suc boundary))
        (reciprocalSuccessor (suc boundary ℕ.+ count))
      endpointPath : suc boundary ℕ.+ count ≡ boundary ℕ.+ suc count
      endpointPath = sym (ℕ.+-suc boundary count)
  in subst (rationalSquareTail boundary (suc count) ≤_)
    (collapsed ∙ cong
      (λ endpoint → reciprocalSuccessor boundary Q.+
        (Q.- reciprocalSuccessor endpoint)) endpointPath)
    combined

rational-higher-tail≤square-tail : (exponent boundary count : ℕ) →
  ℕOrder._≤_ 2 exponent →
  rationalDirichletTail exponent boundary count ≤
    rationalSquareTail boundary count
rational-higher-tail≤square-tail exponent boundary zero 2≤exponent = isRefl≤ 0
rational-higher-tail≤square-tail exponent boundary (suc count) 2≤exponent =
  ≤Monotone+
    (rationalDirichletTerm exponent (suc boundary))
    (rationalDirichletTerm 2 (suc boundary))
    (rationalDirichletTail exponent (suc boundary) count)
    (rationalSquareTail (suc boundary) count)
    (rational-dirichlet-higher-term≤square exponent (suc boundary) 2≤exponent)
    (rational-higher-tail≤square-tail exponent (suc boundary) count 2≤exponent)

rational-square-tail-nonnegative : (boundary count : ℕ) →
  0 ≤ rationalSquareTail boundary count
rational-square-tail-nonnegative boundary zero = ℤOrder.zero-≤pos
rational-square-tail-nonnegative boundary (suc count) =
  let termNonnegative = rational-dirichlet-term-nonnegative 2 (suc boundary)
      tailNonnegative = rational-square-tail-nonnegative (suc boundary) count
  in isTrans≤ 0 (rationalDirichletTerm 2 (suc boundary))
    (rationalDirichletTerm 2 (suc boundary) Q.+
      rationalSquareTail (suc boundary) count)
    termNonnegative
    (≤-add-nonnegative (rationalDirichletTerm 2 (suc boundary))
      (rationalSquareTail (suc boundary) count) tailNonnegative)

rational-square-tail-below-boundary-reciprocal : (boundary count : ℕ) →
  rationalSquareTail boundary count ≤ reciprocalSuccessor boundary
rational-square-tail-below-boundary-reciprocal boundary count =
  isTrans≤
    (rationalSquareTail boundary count)
    (reciprocalSuccessor boundary Q.+
      (Q.- reciprocalSuccessor (boundary ℕ.+ count)))
    (reciprocalSuccessor boundary)
    (rational-square-tail-telescoping-bound boundary count)
    (subst2 _≤_
      (Q.+Comm (Q.- reciprocalSuccessor (boundary ℕ.+ count))
        (reciprocalSuccessor boundary))
      (Q.+IdL (reciprocalSuccessor boundary))
      (≤-+o
        (Q.- reciprocalSuccessor (boundary ℕ.+ count)) 0
        (reciprocalSuccessor boundary)
        (negative-nonpositive
          (reciprocalSuccessor (boundary ℕ.+ count))
          (reciprocalSuccessor-nonnegative (boundary ℕ.+ count)))))

rational-square-dyadic-tail-bound : (stage count : ℕ) →
  rationalSquareTail (dyadicReciprocalIndex stage) count ≤ precision stage
rational-square-dyadic-tail-bound stage count =
  subst (rationalSquareTail (dyadicReciprocalIndex stage) count ≤_)
    (sym (precision-as-dyadic-reciprocal stage))
    (rational-square-tail-below-boundary-reciprocal
      (dyadicReciprocalIndex stage) count)

rational-higher-dyadic-tail-bound : (exponent stage count : ℕ) →
  ℕOrder._≤_ 2 exponent →
  rationalDirichletTail exponent (dyadicReciprocalIndex stage) count ≤
    precision stage
rational-higher-dyadic-tail-bound exponent stage count 2≤exponent =
  isTrans≤
    (rationalDirichletTail exponent (dyadicReciprocalIndex stage) count)
    (rationalSquareTail (dyadicReciprocalIndex stage) count)
    (precision stage)
    (rational-higher-tail≤square-tail exponent
      (dyadicReciprocalIndex stage) count 2≤exponent)
    (rational-square-dyadic-tail-bound stage count)

rationalZetaPartialSum : ℕ → ℕ → Q.ℚ
rationalZetaPartialSum exponent cutoff =
  finiteSum (rationalDirichletTerm exponent) cutoff

rational-dirichlet-first-term : (exponent : ℕ) →
  rationalDirichletTerm exponent zero ≡ 1
rational-dirichlet-first-term zero = refl
rational-dirichlet-first-term (suc exponent) =
  cong (Q._· 1) (rational-dirichlet-first-term exponent) ∙ Q.·IdR 1

rational-zeta-partial-sum-extension : (exponent boundary count : ℕ) →
  rationalZetaPartialSum exponent (boundary ℕ.+ count) ≡
  rationalZetaPartialSum exponent boundary Q.+
    rationalDirichletTail exponent boundary count
rational-zeta-partial-sum-extension exponent boundary zero =
  cong (rationalZetaPartialSum exponent) (ℕ.+-zero boundary) ∙
  sym (Q.+IdR (rationalZetaPartialSum exponent boundary))
rational-zeta-partial-sum-extension exponent boundary (suc count) =
  cong (rationalZetaPartialSum exponent) (ℕ.+-suc boundary count) ∙
  cong (λ x → x Q.+ rationalDirichletTerm exponent
      (suc (boundary ℕ.+ count)))
    (rational-zeta-partial-sum-extension exponent boundary count) ∙
  sym (Q.+Assoc
    (rationalZetaPartialSum exponent boundary)
    (rationalDirichletTail exponent boundary count)
    (rationalDirichletTerm exponent (suc (boundary ℕ.+ count)))) ∙
  cong (rationalZetaPartialSum exponent boundary Q.+_)
    (sym (rational-dirichlet-tail-append exponent boundary count))

rational-zeta-square-partial-sum-extension : (boundary count : ℕ) →
  rationalZetaPartialSum 2 (boundary ℕ.+ count) ≡
  rationalZetaPartialSum 2 boundary Q.+ rationalSquareTail boundary count
rational-zeta-square-partial-sum-extension boundary zero =
  cong (rationalZetaPartialSum 2) (ℕ.+-zero boundary) ∙
  sym (Q.+IdR (rationalZetaPartialSum 2 boundary))
rational-zeta-square-partial-sum-extension boundary (suc count) =
  cong (rationalZetaPartialSum 2) (ℕ.+-suc boundary count) ∙
  cong (λ x → x Q.+ rationalDirichletTerm 2 (suc (boundary ℕ.+ count)))
    (rational-zeta-square-partial-sum-extension boundary count) ∙
  sym (Q.+Assoc
    (rationalZetaPartialSum 2 boundary)
    (rationalSquareTail boundary count)
    (rationalDirichletTerm 2 (suc (boundary ℕ.+ count)))) ∙
  cong (rationalZetaPartialSum 2 boundary Q.+_)
    (sym (rational-square-tail-append boundary count))

rational-zeta-partial-sum-at-least-one : (exponent cutoff : ℕ) →
  1 ≤ rationalZetaPartialSum exponent cutoff
rational-zeta-partial-sum-at-least-one exponent zero =
  subst (1 ≤_) (sym (rational-dirichlet-first-term exponent)) (isRefl≤ 1)
rational-zeta-partial-sum-at-least-one exponent (suc cutoff) =
  isTrans≤ 1 (rationalZetaPartialSum exponent cutoff)
    (rationalZetaPartialSum exponent cutoff Q.+
      rationalDirichletTerm exponent (suc cutoff))
    (rational-zeta-partial-sum-at-least-one exponent cutoff)
    (≤-add-nonnegative (rationalZetaPartialSum exponent cutoff)
      (rationalDirichletTerm exponent (suc cutoff))
      (rational-dirichlet-term-nonnegative exponent (suc cutoff)))

rational-zeta-partial-sum-positive : (exponent cutoff : ℕ) →
  0 < rationalZetaPartialSum exponent cutoff
rational-zeta-partial-sum-positive exponent cutoff =
  isTrans<≤ 0 1 (rationalZetaPartialSum exponent cutoff)
    ℤOrder.isRefl≤
    (rational-zeta-partial-sum-at-least-one exponent cutoff)

rational-zeta-partial-sum-nonzero : (exponent cutoff : ℕ) →
  ¬ (rationalZetaPartialSum exponent cutoff ≡ 0)
rational-zeta-partial-sum-nonzero exponent cutoff path =
  isIrrefl< 0
    (subst (0 <_) path
      (rational-zeta-partial-sum-positive exponent cutoff))
