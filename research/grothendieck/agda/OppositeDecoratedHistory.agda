{-# OPTIONS --safe --cubical --guardedness #-}
module OppositeDecoratedHistory where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base
import EndpointDecoratedHistory as H
module T = H.Typed

app : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {x y z : V} →
  T.Route V E x y → T.Route V E y z → T.Route V E x z
app {V = V} {E = E} = T.append V E

app-unit : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {x y : V}
  (p : T.Route V E x y) → app p T.nil ≡ p
app-unit {V = V} {E = E} = T.append-unit V E

app-assoc : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {w x y z : V}
  (p : T.Route V E w x) (q : T.Route V E x y) (r : T.Route V E y z) →
  app (app p q) r ≡ app p (app q r)
app-assoc {V = V} {E = E} = T.append-assoc V E

leftpart : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {x y : V}
  {p : T.Route V E x y} (c : T.Cut V E p) → T.Route V E x (T.middle V E c)
leftpart {V = V} {E = E} = T.prefix V E

rightpart : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {x y : V}
  {p : T.Route V E x y} (c : T.Cut V E p) → T.Route V E (T.middle V E c) y
rightpart {V = V} {E = E} = T.suffix V E

joinparts : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {x y : V}
  {p : T.Route V E x y} (c : T.Cut V E p) → app (leftpart c) (rightpart c) ≡ p
joinparts {V = V} {E = E} = T.rejoin V E

Op : {ℓ : Level} {V : Type ℓ} → (V → V → Type ℓ) → V → V → Type ℓ
Op E x y = E y x

rev : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {x y : V} →
  T.Route V E x y → T.Route V (Op E) y x
rev T.nil = T.nil
rev (T.step e p) = app (rev p) (T.step e T.nil)

rev-append : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {x y z : V}
  (p : T.Route V E x y) (q : T.Route V E y z) →
  rev (app p q) ≡ app (rev q) (rev p)
rev-append T.nil q = sym (app-unit (rev q))
rev-append (T.step e p) q =
  cong (λ r → app r (T.step e T.nil)) (rev-append p q)
  ∙ app-assoc (rev q) (rev p) (T.step e T.nil)

rev-rev : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ} {x y : V}
  (p : T.Route V E x y) → rev (rev p) ≡ p
rev-rev T.nil = refl
rev-rev (T.step e p) =
  rev-append (rev p) (T.step e T.nil) ∙ cong (T.step e) (rev-rev p)

-- Reversal commutes with any edge relabelling, including keeping or erasing marks.
map-route : {ℓ : Level} {V : Type ℓ} {E F : V → V → Type ℓ}
  (f : {x y : V} → E x y → F x y) {x y : V} →
  T.Route V E x y → T.Route V F x y
map-route f T.nil = T.nil
map-route f (T.step e p) = T.step (f e) (map-route f p)

map-append : {ℓ : Level} {V : Type ℓ} {E F : V → V → Type ℓ}
  (f : {x y : V} → E x y → F x y) {x y z : V}
  (p : T.Route V E x y) (q : T.Route V E y z) →
  map-route f (app p q) ≡ app (map-route f p) (map-route f q)
map-append f T.nil q = refl
map-append f (T.step e p) q = cong (T.step (f e)) (map-append f p q)

rev-map : {ℓ : Level} {V : Type ℓ} {E F : V → V → Type ℓ}
  (f : {x y : V} → E x y → F x y) {x y : V} (p : T.Route V E x y) →
  rev (map-route f p) ≡ map-route (λ {x} {y} → f {y} {x}) (rev p)
rev-map f T.nil = refl
rev-map f (T.step e p) =
  cong (λ r → app r (T.step (f e) T.nil)) (rev-map f p)
  ∙ sym (map-append (λ {x} {y} → f {y} {x}) (rev p) (T.step e T.nil))

-- Every original typed cut supplies a reversed factorization through the SAME vertex.
-- This avoids identifying a reversed arrow with a new forward arithmetic event.
rev-cut-rejoin : {ℓ : Level} {V : Type ℓ} {E : V → V → Type ℓ}
  {x y : V} {p : T.Route V E x y} (c : T.Cut V E p) →
  app (rev (rightpart c)) (rev (leftpart c)) ≡ rev p
rev-cut-rejoin c = sym (rev-append (leftpart c) (rightpart c)) ∙ cong rev (joinparts c)

-- The abstract edge family can itself be Bool × E. Then the same theorems
-- reverse marked arrows without changing their marks. No inverse edges are
-- postulated in E, and no Hilbert adjoint structure occurs here.
