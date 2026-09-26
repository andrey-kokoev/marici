{-# OPTIONS --safe --cubical --guardedness #-}
module BooleanNandEquivalence where
open import Cubical.Foundations.Prelude renaming (_∙_ to trans)
open import WolframBooleanAlgebra

record BooleanStructure {ℓ : Level} (A : Type ℓ) : Type ℓ where
  field
    carrier-is-set : isSet A
    bottom top : A
    neg : A → A
    meet join : A → A → A
    meet-comm : (x y : A) → meet x y ≡ meet y x
    join-comm : (x y : A) → join x y ≡ join y x
    meet-assoc : (x y z : A) → meet (meet x y) z ≡ meet x (meet y z)
    join-assoc : (x y z : A) → join (join x y) z ≡ join x (join y z)
    meet-idem : (x : A) → meet x x ≡ x
    join-idem : (x : A) → join x x ≡ x
    meet-absorb : (x y : A) → meet x (join x y) ≡ x
    join-absorb : (x y : A) → join x (meet x y) ≡ x
    meet-distrib : (x y z : A) → meet x (join y z) ≡ join (meet x y) (meet x z)
    join-distrib : (x y z : A) → join x (meet y z) ≡ meet (join x y) (join x z)
    meet-top : (x : A) → meet x top ≡ x
    join-bottom : (x : A) → join x bottom ≡ x
    meet-complement : (x : A) → meet x (neg x) ≡ bottom
    join-complement : (x : A) → join x (neg x) ≡ top

-- Reconstruction from W uses no Boolean laws as assumptions.
module FromWolfram {ℓ : Level} (A : Type ℓ) (setA : isSet A) (e : A)
  (_∣_ : A → A → A)
  (W : (a b c : A) → ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) ≡ c) where
  open Reconstruction A _∣_ W
  open Constants e
  boolean : BooleanStructure A
  boolean = record
    { carrier-is-set = setA ; bottom = bottom ; top = top
    ; neg = neg ; meet = meet ; join = join
    ; meet-comm = meet-comm ; join-comm = join-comm
    ; meet-assoc = meet-assoc ; join-assoc = join-assoc
    ; meet-idem = meet-idem ; join-idem = join-idem
    ; meet-absorb = meet-absorb ; join-absorb = join-absorb
    ; meet-distrib = meet-distrib ; join-distrib = join-distrib
    ; meet-top = meet-top ; join-bottom = join-bottom
    ; meet-complement = meet-complement ; join-complement = join-complement }
  recovered-operation : (x y : A) → (x ∣ y) ≡ neg (meet x y)
  recovered-operation = original-is-nand

module ToWolfram {ℓ : Level} {A : Type ℓ} (B : BooleanStructure A) where
  open BooleanStructure B

  -- Complement uniqueness supplies involution and De Morgan, rather than
  -- adding those as assumptions to the Boolean lattice signature.
  complement-unique : (x y z : A)
    → meet x y ≡ bottom → join x y ≡ top
    → meet x z ≡ bottom → join x z ≡ top → y ≡ z
  complement-unique x y z xy jy xz jz = trans
    (sym (meet-top y))
    (trans (cong (meet y) (sym jz))
      (trans (meet-distrib y x z)
        (trans (cong (λ v → join v (meet y z)) (trans (meet-comm y x) xy))
          (trans (join-comm bottom (meet y z))
            (trans (join-bottom (meet y z))
              (trans (meet-comm y z)
                (trans (sym (join-bottom (meet z y)))
                  (trans (join-comm (meet z y) bottom)
                    (trans (cong (λ v → join v (meet z y)) (sym (trans (meet-comm z x) xz)))
                      (trans (sym (meet-distrib z x y))
                        (trans (cong (meet z) jy) (meet-top z))))))))))))

  double-negation : (x : A) → neg (neg x) ≡ x
  double-negation x = complement-unique (neg x) (neg (neg x)) x
    (meet-complement (neg x)) (join-complement (neg x))
    (trans (meet-comm (neg x) x) (meet-complement x))
    (trans (join-comm (neg x) x) (join-complement x))

  meet-bottom : (x : A) → meet x bottom ≡ bottom
  meet-bottom x = trans (meet-comm x bottom)
    (trans (cong (meet bottom) (sym (join-bottom x)))
      (trans (cong (meet bottom) (join-comm x bottom)) (meet-absorb bottom x)))
  join-top : (x : A) → join top x ≡ top
  join-top x = trans (cong (join top) (sym (trans (meet-comm top x) (meet-top x))))
    (join-absorb top x)

  deMorgan : (x y : A) → neg (meet x y) ≡ join (neg x) (neg y)
  deMorgan x y = complement-unique (meet x y) (neg (meet x y)) (join (neg x) (neg y))
    (meet-complement (meet x y)) (join-complement (meet x y))
    (trans (meet-distrib (meet x y) (neg x) (neg y))
      (trans (cong₂ join
        (trans (cong (λ v → meet v (neg x)) (meet-comm x y))
          (trans (meet-assoc y x (neg x))
            (trans (cong (meet y) (meet-complement x)) (meet-bottom y))))
        (trans (meet-assoc x y (neg y))
          (trans (cong (meet x) (meet-complement y)) (meet-bottom x))))
        (join-bottom bottom)))
    (trans (join-comm (meet x y) (join (neg x) (neg y)))
      (trans (join-distrib (join (neg x) (neg y)) x y)
        (trans (cong₂ meet
          (trans (join-comm (join (neg x) (neg y)) x)
            (trans (sym (join-assoc x (neg x) (neg y)))
              (trans (cong (λ v → join v (neg y)) (join-complement x)) (join-top (neg y)))))
          (trans (join-assoc (neg x) (neg y) y)
            (trans (cong (join (neg x))
              (trans (join-comm (neg y) y) (join-complement y)))
              (trans (join-comm (neg x) top) (join-top (neg x))))))
          (meet-top top))))

  nand : A → A → A
  nand x y = neg (meet x y)

  right-reduce : (a c : A) → nand a (nand (nand a c) a) ≡ nand a c
  right-reduce a c = cong neg
    (trans (cong (meet a)
      (trans (deMorgan (nand a c) a)
        (cong (λ v → join v (neg a)) (double-negation (meet a c)))))
      (trans (meet-distrib a (meet a c) (neg a))
        (trans (cong₂ join
          (trans (sym (meet-assoc a a c)) (cong (λ v → meet v c) (meet-idem a)))
          (meet-complement a)) (join-bottom (meet a c)))))

  cover : (a b : A) → join (nand a b) a ≡ top
  cover a b = trans (cong (λ v → join v a) (deMorgan a b))
    (trans (join-comm (join (neg a) (neg b)) a)
      (trans (sym (join-assoc a (neg a) (neg b)))
        (trans (cong (λ v → join v (neg b)) (join-complement a)) (join-top (neg b)))))

  wolfram : (a b c : A)
    → nand (nand (nand a b) c) (nand a (nand (nand a c) a)) ≡ c
  wolfram a b c = trans
    (cong (nand (nand (nand a b) c)) (right-reduce a c))
    (trans (deMorgan (nand (nand a b) c) (nand a c))
      (trans (cong₂ join (double-negation (meet (nand a b) c)) (double-negation (meet a c)))
        (trans (cong₂ join (meet-comm (nand a b) c) (meet-comm a c))
          (trans (sym (meet-distrib c (nand a b) a))
            (trans (cong (meet c) (cover a b)) (meet-top c))))))

  module Roundtrip (e : A) where
    module R = Reconstruction A nand wolfram
    module C = R.Constants e
    recovered-neg : (x : A) → R.neg x ≡ neg x
    recovered-neg x = cong neg (meet-idem x)
    recovered-meet : (x y : A) → R.meet x y ≡ meet x y
    recovered-meet x y = trans (recovered-neg (nand y x))
      (trans (double-negation (meet y x)) (meet-comm y x))
    recovered-join : (x y : A) → R.join x y ≡ join x y
    recovered-join x y = trans
      (cong neg (cong₂ meet (recovered-neg y) (recovered-neg x)))
      (trans (deMorgan (neg y) (neg x))
        (trans (cong₂ join (double-negation y) (double-negation x)) (join-comm y x)))
    neg-bottom : neg bottom ≡ top
    neg-bottom = trans (sym (join-bottom (neg bottom)))
      (trans (join-comm (neg bottom) bottom) (join-complement bottom))
    neg-top : neg top ≡ bottom
    neg-top = trans (cong neg (sym neg-bottom)) (double-negation bottom)
    recovered-top : C.top ≡ top
    recovered-top = trans (cong neg (cong (λ v → meet v e) (recovered-neg e)))
      (trans (cong neg (meet-comm (neg e) e))
        (trans (cong neg (meet-complement e)) neg-bottom))
    recovered-bottom : C.bottom ≡ bottom
    recovered-bottom = trans (recovered-neg C.top)
      (trans (cong neg recovered-top) neg-top)

