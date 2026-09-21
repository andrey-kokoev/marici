{-# OPTIONS --safe --cubical --guardedness #-}
module GeneratorMateExtension where

open import Cubical.Foundations.Prelude
import EndpointDecoratedHistory as H

-- The pointwise proof uses no metric axioms: those are needed to construct
-- the generator mates and beta, not to propagate an admitted naturality square.
module Extension {ℓ : Level} (V : Type ℓ) (E : V → V → Type ℓ)
  (X Y : V → Type ℓ)
  (f : {x y : V} → E x y → X y → X x)
  (g : {x y : V} → E x y → Y y → Y x)
  (beta : (x : V) → X x → Y x)
  (local : {x y : V} (e : E x y) (z : X y) →
    beta x (f e z) ≡ g e (beta y z)) where

  open H.Typed V E

  fold-X : {x y : V} → Route x y → X y → X x
  fold-X nil z = z
  fold-X (step e p) z = f e (fold-X p z)

  fold-Y : {x y : V} → Route x y → Y y → Y x
  fold-Y nil z = z
  fold-Y (step e p) z = g e (fold-Y p z)

  path-square : {x y : V} (p : Route x y) (z : X y) →
    beta x (fold-X p z) ≡ fold-Y p (beta y z)
  path-square nil z = refl
  path-square (step e p) z =
    local e (fold-X p z) ∙ cong (g e) (path-square p z)

  fold-composition : {x y z : V} (p : Route x y) (q : Route y z) (v : X z) →
    fold-X (append p q) v ≡ fold-X p (fold-X q v)
  fold-composition nil q v = refl
  fold-composition (step e p) q v = cong (f e) (fold-composition p q v)

  -- Any extension with the unit and generator-composition laws is this fold.
  module Uniqueness
    (R : {x y : V} → Route x y → X y → X x)
    (unit : {x : V} (v : X x) → R nil v ≡ v)
    (extend : {x y z : V} (e : E x y) (p : Route y z) (v : X z) →
      R (step e p) v ≡ f e (R p v)) where

    unique : {x y : V} (p : Route x y) (v : X y) → R p v ≡ fold-X p v
    unique nil v = unit v
    unique (step e p) v = extend e p v ∙ cong (f e) (unique p v)

  -- The middle vertex stays in the type, even for the contravariant cut.
  cut-square : {x y : V} {p : Route x y} (c : Cut p) (v : X y) →
    beta x (fold-X (prefix c) (fold-X (suffix c) v)) ≡ fold-Y p (beta y v)
  cut-square {x = x} {p = p} c v =
    cong (beta x) (sym (fold-composition (prefix c) (suffix c) v))
    ∙ cong (λ q → beta x (fold-X q v)) (rejoin c)
    ∙ path-square p v
