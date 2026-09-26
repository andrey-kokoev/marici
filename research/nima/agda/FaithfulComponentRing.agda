{-# OPTIONS --safe --cubical --guardedness #-}
module FaithfulComponentRing where
open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing.Base

-- Transfer laws, not operations: source operations and their preservation
-- proofs must already have been constructed, including quotient descent.
module Transfer (A : Type) (setA : isSet A) (R : CommRing ℓ-zero)
  (f : A → fst R) (injective : {x y : A} → f x ≡ f y → x ≡ y)
  (zero one : A) (add multiply : A → A → A) (negate : A → A)
  (pzero : f zero ≡ CommRingStr.0r (snd R))
  (pone : f one ≡ CommRingStr.1r (snd R))
  (padd : (x y : A) → f (add x y) ≡ CommRingStr._+_ (snd R) (f x) (f y))
  (pmul : (x y : A) → f (multiply x y) ≡ CommRingStr._·_ (snd R) (f x) (f y))
  (pneg : (x : A) → f (negate x) ≡ CommRingStr.-_ (snd R) (f x)) where
  open CommRingStr (snd R)
  associative : (op : A → A → A) (target : fst R → fst R → fst R)
    → ((x y : A) → f (op x y) ≡ target (f x) (f y))
    → ((x y z : fst R) → target x (target y z) ≡ target (target x y) z)
    → (x y z : A) → op x (op y z) ≡ op (op x y) z
  associative op target p law x y z = injective
    (p x (op y z) ∙ cong (target (f x)) (p y z) ∙ law (f x) (f y) (f z)
      ∙ cong (λ t → target t (f z)) (sym (p x y)) ∙ sym (p (op x y) z))
  commutative : (op : A → A → A) (target : fst R → fst R → fst R)
    → ((x y : A) → f (op x y) ≡ target (f x) (f y))
    → ((x y : fst R) → target x y ≡ target y x)
    → (x y : A) → op x y ≡ op y x
  commutative op target p law x y = injective (p x y ∙ law (f x) (f y) ∙ sym (p y x))
  add-unit : (x : A) → add x zero ≡ x
  add-unit x = injective (padd x zero ∙ cong (f x +_) pzero ∙ +IdR (f x))
  mul-unit : (x : A) → multiply x one ≡ x
  mul-unit x = injective (pmul x one ∙ cong (f x ·_) pone ∙ ·IdR (f x))
  add-inverse : (x : A) → add x (negate x) ≡ zero
  add-inverse x = injective (padd x (negate x) ∙ cong (f x +_) (pneg x) ∙ +InvR (f x) ∙ sym pzero)
  distribute : (x y z : A) → multiply x (add y z) ≡ add (multiply x y) (multiply x z)
  distribute x y z = injective (pmul x (add y z) ∙ cong (f x ·_) (padd y z)
    ∙ ·DistR+ (f x) (f y) (f z) ∙ cong₂ _+_ (sym (pmul x y)) (sym (pmul x z))
    ∙ sym (padd (multiply x y) (multiply x z)))
  ring : CommRing ℓ-zero
  ring = makeCommRing zero one add multiply negate setA
    (associative add _+_ padd +Assoc) add-unit add-inverse
    (commutative add _+_ padd +Comm)
    (associative multiply _·_ pmul ·Assoc) mul-unit distribute
    (commutative multiply _·_ pmul ·Comm)
