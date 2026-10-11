{-# OPTIONS --safe --cubical --guardedness #-}
module TickComplexNativeOperators where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true)
open import Cubical.Data.Sigma.Base using (_×_; _,_)
open import ConstructiveComplexCompletion using (ComplexCompletion; _+complex_; _·complex_)

-- Pullback by the native coordinate flips on the free four-state space.
-- The involutions equal their inverses, so this is also their pushforward.
module Native (Scalar : Type) (_+s_ _*s_ : Scalar → Scalar → Scalar) where
  Label = Bool × Bool
  Vector = Label → Scalar
  Factor = Bool → Scalar

  flip : Bool → Bool
  flip false = true
  flip true = false

  flip-involutive : (b : Bool) → flip (flip b) ≡ b
  flip-involutive false = refl
  flip-involutive true = refl

  left right exchange : Vector → Vector
  left v (a , b) = v (flip a , b)
  right v (a , b) = v (a , flip b)
  exchange v (a , b) = v (b , a)

  add : Vector → Vector → Vector
  add v w j = v j +s w j
  scale : Scalar → Vector → Vector
  scale c v j = c *s v j
  tensor : Factor → Factor → Vector
  tensor u v (a , b) = u a *s v b
  factor-flip : Factor → Factor
  factor-flip u a = u (flip a)

  left-involutive : (v : Vector) → left (left v) ≡ v
  left-involutive v = funExt λ { (a , b) → cong (λ x → v (x , b)) (flip-involutive a) }
  right-involutive : (v : Vector) → right (right v) ≡ v
  right-involutive v = funExt λ { (a , b) → cong (λ x → v (a , x)) (flip-involutive b) }
  flips-commute : (v : Vector) → left (right v) ≡ right (left v)
  flips-commute v = refl

  left-additive : (v w : Vector) → left (add v w) ≡ add (left v) (left w)
  left-additive v w = refl
  right-additive : (v w : Vector) → right (add v w) ≡ add (right v) (right w)
  right-additive v w = refl
  left-homogeneous : (c : Scalar) (v : Vector) → left (scale c v) ≡ scale c (left v)
  left-homogeneous c v = refl
  right-homogeneous : (c : Scalar) (v : Vector) → right (scale c v) ≡ scale c (right v)
  right-homogeneous c v = refl

  left-tensor : (u v : Factor) → left (tensor u v) ≡ tensor (factor-flip u) v
  left-tensor u v = refl
  right-tensor : (u v : Factor) → right (tensor u v) ≡ tensor u (factor-flip v)
  right-tensor u v = refl
  exchange-involutive : (v : Vector) → exchange (exchange v) ≡ v
  exchange-involutive v = refl
  exchange-left : (v : Vector) → exchange (left v) ≡ right (exchange v)
  exchange-left v = refl
  exchange-right : (v : Vector) → exchange (right v) ≡ left (exchange v)
  exchange-right v = refl

-- Actual operational completion amplitudes, not an assumed complex field.
module Operational = Native ComplexCompletion _+complex_ _·complex_
