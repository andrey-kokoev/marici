{-# OPTIONS --safe --cubical --guardedness #-}
module PhaseAlgebraSelectionBoundary where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; _⊕_)
open import Cubical.Data.Bool.Properties using (false≢true; ⊕-comm; ⊕-assoc)
open import Cubical.Data.Empty.Base using (⊥)
import RetainedCliffordProfiles as C
import ComponentArithmetic as Coeff
import PhaseLiftCocycle as Phase

-- Existing coefficient multiplication really is constructed, not missing.
component-commutativity : (a b : Coeff.Word) → Coeff.multiply a b ≡ Coeff.multiply b a
component-commutativity = Coeff.multiply-comm

-- Same source actions, two declared phase products. This is not two products
-- inside an already fixed Clifford algebra: the algebra policy differs.
data Model : Type where trivial clifford : Model
product : Model → C.Signed → C.Signed → C.Signed
product trivial (e , a , b) (d , c , f) = e ⊕ d , a ⊕ c , b ⊕ f
product clifford = C.multiply
reverse : Model → C.Signed → C.Signed
reverse trivial x = x
reverse clifford = C.reverse-lift
projection-law : (m : Model) (x y : C.Signed)
  → C.forget-sign (product m x y) ≡ C.compose-action (C.forget-sign x) (C.forget-sign y)
projection-law trivial (e , a , b) (d , c , f) = refl
projection-law clifford = C.action-composition
reverse-projection : (m : Model) (x : C.Signed) → C.forget-sign (reverse m x) ≡ C.forget-sign x
reverse-projection trivial x = refl
reverse-projection clifford (e , a , b) = refl
trivial-commutes : (x y : C.Signed) → product trivial x y ≡ product trivial y x
trivial-commutes (e , a , b) (d , c , f) i = ⊕-comm e d i , ⊕-comm a c i , ⊕-comm b f i
trivial-associative : (x y z : C.Signed)
  → product trivial (product trivial x y) z ≡ product trivial x (product trivial y z)
trivial-associative (e , a , b) (d , c , f) (k , g , h) i =
  sym (⊕-assoc e d k) i , sym (⊕-assoc a c g) i , sym (⊕-assoc b f h) i
interpret : Model → C.History → C.Signed
interpret m C.unit = false , false , false
interpret m C.e1 = false , true , false
interpret m C.e2 = false , false , true
interpret m (C.times h k) = product m (interpret m h) (interpret m k)
interpret m (C.reversal h) = reverse m (interpret m h)
all-histories-same-action : (h : C.History)
  → C.forget-sign (interpret trivial h) ≡ C.forget-sign (interpret clifford h)
all-histories-same-action C.unit = refl
all-histories-same-action C.e1 = refl
all-histories-same-action C.e2 = refl
all-histories-same-action (C.times h k) =
  projection-law trivial (interpret trivial h) (interpret trivial k)
  ∙ cong₂ C.compose-action (all-histories-same-action h) (all-histories-same-action k)
  ∙ sym (projection-law clifford (interpret clifford h) (interpret clifford k))
all-histories-same-action (C.reversal h) =
  reverse-projection trivial (interpret trivial h) ∙ all-histories-same-action h
  ∙ sym (reverse-projection clifford (interpret clifford h))
products-not-selected : product trivial ≡ product clifford → ⊥
products-not-selected p = false≢true (cong (λ mu → fst (mu (false , false , true) (false , true , false))) p)

module N = C.N
module G = C.G
-- Keep only the common actual source certificate here, not the fixed-Clifford
-- scope tag of the previous example. Each candidate records its own model tag.
common-source : G.Node C.History
common-source = G.retain-node (N.N.expression C.source-packet) (N.N.value C.source-packet)
  (G.atom-node C.History)
module Profiles = N.Two common-source C.unit (interpret trivial) (interpret clifford)
candidate : Model → G.Package
candidate m = N.N.pack
  (G.retain-node (N.N.expression C.source-packet) (N.N.value C.source-packet)
    (G.retain-node (G.atom-node Model) m
      (G.maps-node (G.atom-node C.Signed) (G.maps-node (G.atom-node C.Signed) (G.atom-node C.Signed)))))
  (product m)
-- Native representability is not a claim of admission by every source policy.

-- Composition of maps supplies a monoid without selecting a Clifford product.
module Endomorphisms {ℓ} (A : Type ℓ) (a0 : A) where
  End = A → A
  compose : End → End → End
  compose f g x = f (g x)
  associative : (f g h : End) → compose (compose f g) h ≡ compose f (compose g h)
  associative f g h = refl
  constant : A → End
  constant a _ = a
  constant-faithful : {a b : A} → constant a ≡ constant b → a ≡ b
  constant-faithful p = cong (λ f → f a0) p

-- An independent extra condition: nontrivial conjugation cannot be inner in
-- any commutative unital associative algebra (indeed, monoid).
module CommutativeInner {ℓ} (A : Type ℓ) (mul : A → A → A) (one : A)
  (assoc : (x y z : A) → mul (mul x y) z ≡ mul x (mul y z))
  (comm : (x y : A) → mul x y ≡ mul y x)
  (right-unit : (x : A) → mul x one ≡ x) where
  inner-identity : (u v : A) → mul u v ≡ one → (x : A) → mul (mul u x) v ≡ x
  inner-identity u v inverse x = cong (λ z → mul z v) (comm u x)
    ∙ assoc x u v ∙ cong (mul x) inverse ∙ right-unit x
  nontrivial-not-inner : (u v : A) → mul u v ≡ one → (f : A → A)
    → (x : A) → (f x ≡ x → ⊥)
    → ((y : A) → f y ≡ mul (mul u y) v) → ⊥
  nontrivial-not-inner u v inverse f x nontrivial implements =
    nontrivial (implements x ∙ inner-identity u v inverse x)
