{-# OPTIONS --safe --cubical --guardedness #-}
module WolframBooleanAlgebra where
open import Cubical.Foundations.Prelude renaming (_∙_ to trans)
open import WolframConverse

module Reconstruction {ℓ : Level} (A : Type ℓ) (_∣_ : A → A → A)
  (W : (a b c : A) → ((a ∣ b) ∣ c) ∣ (a ∣ ((a ∣ c) ∣ a)) ≡ c) where
  open Converse A _∣_ W public

  meet-comm : (x y : A) → meet x y ≡ meet y x
  meet-comm x y = cong neg (t93 x y)
  join-comm : (x y : A) → join x y ≡ join y x
  join-comm x y = t93 (neg x) (neg y)
  meet-idem : (x : A) → meet x x ≡ x
  meet-idem = double-negation
  join-idem : (x : A) → join x x ≡ x
  join-idem = double-negation

  meet-absorb : (x y : A) → meet x (join x y) ≡ x
  meet-absorb x y = trans (cong neg
    (trans (cong (λ v → x * v) (t93 (neg x) (neg y)))
      (t83 x (neg y)))) (double-negation x)
  join-absorb : (x y : A) → join x (meet x y) ≡ x
  join-absorb x y = trans
    (cong (λ v → neg x * v) (double-negation (x * y)))
    (trans (cong (λ v → neg x * v) (t93 x y)) (t80 x y))

  distrib-core : (x y z : A)
    → meet (neg y * x) (neg z * x) ≡ x * (y * z)
  distrib-core x y z = trans (cong neg (sheffer-3 x y z))
    (double-negation (x * (y * z)))
  join-distrib : (x y z : A)
    → join x (meet y z) ≡ meet (join x y) (join x z)
  join-distrib x y z = trans
    (cong (λ v → neg x * v) (double-negation (y * z)))
    (trans (sym (distrib-core (neg x) y z))
      (cong₂ meet (t93 (neg y) (neg x)) (t93 (neg z) (neg x))))

  meet-distrib : (x y z : A)
    → meet x (join y z) ≡ join (meet x y) (meet x z)
  meet-distrib x y z = trans
    (sym (cong neg (cong₂ _*_ (double-negation x)
      (double-negation (neg y * neg z)))))
    (trans (cong neg (join-distrib (neg x) (neg y) (neg z)))
      (trans (double-negation (join (neg x) (neg y) * join (neg x) (neg z)))
        (trans (cong₂ _*_
          (cong₂ _*_ (double-negation x) (double-negation y))
          (cong₂ _*_ (double-negation x) (double-negation z)))
          (sym (cong₂ _*_ (double-negation (x * y)) (double-negation (x * z)))))))

  meet-nest : (x y : A) → meet x (meet x y) ≡ meet x y
  meet-nest x y = cong neg (trans (t130 x (x * y))
    (trans (cong (λ v → x * (x * v)) (t93 x y))
      (trans (cong (λ v → x * v) (t93 x (y * x))) (t91 x y))))

  infix 4 _≤_
  _≤_ : A → A → Type ℓ
  x ≤ y = meet x y ≡ x
  lower-left : (x y : A) → meet x y ≤ x
  lower-left x y = trans (meet-comm (meet x y) x) (meet-nest x y)
  lower-right : (x y : A) → meet x y ≤ y
  lower-right x y = trans (cong (λ v → meet v y) (meet-comm x y))
    (trans (lower-left y x) (meet-comm y x))
  le-to-join : {x y : A} → x ≤ y → join x y ≡ y
  le-to-join {x} {y} p = trans (join-comm x y)
    (trans (cong (join y) (sym p))
      (trans (cong (join y) (meet-comm x y)) (join-absorb y x)))
  join-to-le : {x y : A} → join x y ≡ y → x ≤ y
  join-to-le {x} {y} p = trans (cong (meet x) (sym p)) (meet-absorb x y)
  le-trans : {x y z : A} → x ≤ y → y ≤ z → x ≤ z
  le-trans {x} {y} {z} p q = trans
    (cong (meet x) (sym (le-to-join q)))
    (trans (meet-distrib x y z)
      (trans (cong (λ v → join v (meet x z)) p) (join-absorb x z)))
  meet-monotone : (c : A) {a b : A} → a ≤ b → meet c a ≤ meet c b
  meet-monotone c {a} {b} p = join-to-le
    (trans (sym (meet-distrib c a b)) (cong (meet c) (le-to-join p)))
  greatest : {a b c : A} → c ≤ a → c ≤ b → c ≤ meet a b
  greatest {a} {b} {c} p q = trans
    (cong₂ meet (sym (trans (meet-comm b c) q)) (meet-comm a b))
    (trans (meet-monotone b p) (trans (meet-comm b c) q))
  antisym : {x y : A} → x ≤ y → y ≤ x → x ≡ y
  antisym {x} {y} p q = trans (sym p) (trans (meet-comm x y) q)

  meet-assoc : (x y z : A) → meet (meet x y) z ≡ meet x (meet y z)
  meet-assoc x y z = antisym
    (greatest
      (le-trans (lower-left (meet x y) z) (lower-left x y))
      (greatest
        (le-trans (lower-left (meet x y) z) (lower-right x y))
        (lower-right (meet x y) z)))
    (greatest
      (greatest (lower-left x (meet y z))
        (le-trans (lower-right x (meet y z)) (lower-left y z)))
      (le-trans (lower-right x (meet y z)) (lower-right y z)))

  join-dual : (x y : A) → join x y ≡ neg (meet (neg x) (neg y))
  join-dual x y = sym (double-negation (join x y))
  join-assoc : (x y z : A) → join (join x y) z ≡ join x (join y z)
  join-assoc x y z = trans (join-dual (join x y) z)
    (trans (cong neg (meet-assoc (neg x) (neg y) (neg z)))
      (sym (join-dual x (join y z))))

  -- Constants require an inhabitant, not two distinct truth values.
  -- The resulting Boolean algebra is allowed to be trivial.
  module Constants (e : A) where
    top bottom : A
    top = e * neg e
    bottom = neg top

    top-independent : (x y : A) → x * neg x ≡ y * neg y
    top-independent x y = trans (sym (double-negation (x * neg x)))
      (trans (cong neg (trans (sym (sheffer-2 (x * neg x) y))
        (trans (t93 (x * neg x) (y * neg y)) (sheffer-2 (y * neg y) x))))
        (double-negation (y * neg y)))
    meet-top : (x : A) → meet x top ≡ x
    meet-top x = trans (cong neg (sheffer-2 x e)) (double-negation x)
    join-bottom : (x : A) → join x bottom ≡ x
    join-bottom x = trans (cong (λ v → neg x * v) (double-negation top))
      (trans (sheffer-2 (neg x) e) (double-negation x))
    meet-complement : (x : A) → meet x (neg x) ≡ bottom
    meet-complement x = cong neg (top-independent x e)
    join-complement : (x : A) → join x (neg x) ≡ top
    join-complement x = trans (cong (λ v → neg x * v) (double-negation x))
      (trans (t93 (neg x) x) (top-independent x e))
