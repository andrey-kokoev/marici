{-# OPTIONS --safe --cubical --guardedness #-}
module TickCayleyRotorComposition where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.Data.Rationals as Q
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import RationalAnalyticSubstrate using (PreferredℚCommRing)
open import CauchyMetricEquivalence
open import CauchyCompletionCommRing
open import TickRotationDefectTransport using (Rotor; _⊗_)
open import TickCayleyGridIncrement using (gridValue; gridProductInverse; grid-product-inverse-law)
open import TickCayleyOuterRotor using (cayleyReal; cayleyImaginary; cayleyRotor; inverseCayleyRotor; embedded-product; cayley-inverse-law)
open import TickCayleyRelativeRotor using (relativeCosine; relativeSine)

module Algebra {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R) renaming (_+_ to _+S_; _·_ to _·S_; -_ to -S_)
  real-clear : (v D p r s : fst R) →
    (1r +S (-S ((v ·S p) ·S (v ·S p)))) ·S ((D ·S D) ·S (r ·S s)) ≡
    ((D ·S D) +S (-S ((v ·S v) ·S ((D ·S p) ·S (D ·S p))))) ·S (r ·S s)
  real-clear v D p r s = solve! R
  imaginary-clear : (v D p r s : fst R) →
    ((v ·S p) +S (v ·S p)) ·S ((D ·S D) ·S (r ·S s)) ≡
    ((v +S v) ·S D ·S (D ·S p)) ·S (r ·S s)
  imaginary-clear v D p r s = solve! R
  real-finish : (x y r s : fst R) →
    (((1r +S x ·S y) ·S (1r +S x ·S y)) +S (-S (((y +S (-S x)) ·S (y +S (-S x))) ·S (1r ·S 1r)))) ·S (r ·S s) ≡
    (((1r +S (-S (x ·S x))) ·S r) ·S ((1r +S (-S (y ·S y))) ·S s)) +S
      (-S ((-S ((x +S x) ·S r)) ·S ((y +S y) ·S s)))
  real-finish x y r s = solve! R
  imaginary-finish : (x y r s : fst R) →
    (((y +S (-S x)) +S (y +S (-S x))) ·S (1r +S x ·S y) ·S 1r) ·S (r ·S s) ≡
    (((1r +S (-S (x ·S x))) ·S r) ·S ((y +S y) ·S s)) +S
      ((-S ((x +S x) ·S r)) ·S ((1r +S (-S (y ·S y))) ·S s))
  imaginary-finish x y r s = solve! R
  assoc-real : (a b c d e f : fst R) →
    (a ·S c +S (-S (b ·S d))) ·S e +S (-S ((a ·S d +S b ·S c) ·S f)) ≡
    a ·S (c ·S e +S (-S (d ·S f))) +S (-S (b ·S (c ·S f +S d ·S e)))
  assoc-real a b c d e f = solve! R
  assoc-imaginary : (a b c d e f : fst R) →
    (a ·S c +S (-S (b ·S d))) ·S f +S ((a ·S d +S b ·S c) ·S e) ≡
    a ·S (c ·S f +S d ·S e) +S b ·S (c ·S e +S (-S (d ·S f)))
  assoc-imaginary a b c d e f = solve! R
  unit-real : (a b : fst R) → a ·S 1r +S (-S (b ·S 0r)) ≡ a
  unit-real a b = solve! R
  unit-imaginary : (a b : fst R) → a ·S 0r +S b ·S 1r ≡ b
  unit-imaginary a b = solve! R
module R = Algebra PreferredℚCommRing
module C = Algebra CompletionCommRing

abstract
  relative-real-composition : (x y p r s : Q.ℚ) → (1 Q.+ x Q.· y) Q.· p ≡ 1 →
    (1 Q.+ (Q.- (((y Q.+ (Q.- x)) Q.· p) Q.· ((y Q.+ (Q.- x)) Q.· p)))) Q.·
      (((1 Q.+ x Q.· y) Q.· (1 Q.+ x Q.· y)) Q.· (r Q.· s)) ≡
    (((1 Q.+ (Q.- (x Q.· x))) Q.· r) Q.· ((1 Q.+ (Q.- (y Q.· y))) Q.· s)) Q.+
      (Q.- ((Q.- ((x Q.+ x) Q.· r)) Q.· ((y Q.+ y) Q.· s)))
  relative-real-composition x y p r s law = R.real-clear (y Q.+ (Q.- x)) (1 Q.+ x Q.· y) p r s
    ∙ cong (λ z → (((1 Q.+ x Q.· y) Q.· (1 Q.+ x Q.· y)) Q.+
      (Q.- (((y Q.+ (Q.- x)) Q.· (y Q.+ (Q.- x))) Q.· z))) Q.· (r Q.· s)) (cong₂ Q._·_ law law)
    ∙ R.real-finish x y r s

  relative-imaginary-composition : (x y p r s : Q.ℚ) → (1 Q.+ x Q.· y) Q.· p ≡ 1 →
    (((y Q.+ (Q.- x)) Q.· p) Q.+ ((y Q.+ (Q.- x)) Q.· p)) Q.·
      (((1 Q.+ x Q.· y) Q.· (1 Q.+ x Q.· y)) Q.· (r Q.· s)) ≡
    (((1 Q.+ (Q.- (x Q.· x))) Q.· r) Q.· ((y Q.+ y) Q.· s)) Q.+
      ((Q.- ((x Q.+ x) Q.· r)) Q.· ((1 Q.+ (Q.- (y Q.· y))) Q.· s))
  relative-imaginary-composition x y p r s law = R.imaginary-clear (y Q.+ (Q.- x)) (1 Q.+ x Q.· y) p r s
    ∙ cong (λ z → (((y Q.+ (Q.- x)) Q.+ (y Q.+ (Q.- x))) Q.· (1 Q.+ x Q.· y) Q.· z) Q.· (r Q.· s)) law
    ∙ R.imaginary-finish x y r s

  rotor-assoc : (a b c : Rotor) → (a ⊗ b) ⊗ c ≡ a ⊗ (b ⊗ c)
  rotor-assoc (a , b) (c , d) (e , f) = cong₂ _,_ (C.assoc-real a b c d e f) (C.assoc-imaginary a b c d e f)
  rotor-right-unit : (a : Rotor) → a ⊗ (embedMetricℚ 1 , embedMetricℚ 0) ≡ a
  rotor-right-unit (a , b) = cong₂ _,_ (C.unit-real a b) (C.unit-imaginary a b)

relativeRotor : ℕ → ℕ → ℕ → Rotor
relativeRotor n m d = embedMetricℚ (relativeCosine n m d) , embedMetricℚ (relativeSine n m d)

abstract
  relative-rotor-composition : (n m d : ℕ) → relativeRotor n m d ≡ inverseCayleyRotor n d ⊗ cayleyRotor m d
  relative-rotor-composition n m d = cong₂ _,_
    (cong embedMetricℚ (relative-real-composition (gridValue n d) (gridValue m d)
      (gridProductInverse n m d) (gridProductInverse n n d) (gridProductInverse m m d) (grid-product-inverse-law n m d)))
    (cong embedMetricℚ (relative-imaginary-composition (gridValue n d) (gridValue m d)
      (gridProductInverse n m d) (gridProductInverse n n d) (gridProductInverse m m d) (grid-product-inverse-law n m d)))
    ∙ sym (embedded-product (cayleyReal n d) (Q.- cayleyImaginary n d) (cayleyReal m d) (cayleyImaginary m d))

  relative-inverse-cancellation : (n m d : ℕ) → relativeRotor n m d ⊗ inverseCayleyRotor m d ≡ inverseCayleyRotor n d
  relative-inverse-cancellation n m d = cong (_⊗ inverseCayleyRotor m d) (relative-rotor-composition n m d)
    ∙ rotor-assoc (inverseCayleyRotor n d) (cayleyRotor m d) (inverseCayleyRotor m d)
    ∙ cong (inverseCayleyRotor n d ⊗_) (cayley-inverse-law m d) ∙ rotor-right-unit (inverseCayleyRotor n d)
