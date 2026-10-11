{-# OPTIONS --safe --cubical --guardedness #-}
module WolframCommutativeBridge where

open import Cubical.Foundations.Prelude

-- A structural bridge, not a proof of commutativity from the axiom.
-- The reversed stroke matches the published Sh_2 certificate convention.
module Bridge {ℓ : Level} (A : Type ℓ) (_*_ : A → A → A)
  (sh2 : (x y z : A) → (((x * (y * x)) * x) * (y * (z * x))) ≡ y)
  (comm : (x y : A) → x * y ≡ y * x) where

  -- Commutativity alone supplies the reassociation needed here;
  -- associativity of the stroke is neither assumed nor true for NAND.
  pivot : (x u : A) → x * (u * x) ≡ (x * u) * x
  pivot x u = comm x (u * x) ∙ cong (λ v → v * x) (comm u x)

  sh1 : (x y z : A) → (x * ((y * x) * x)) * (y * (z * x)) ≡ y
  sh1 x y z = cong (λ v → v * (y * (z * x))) (pivot x (y * x)) ∙ sh2 x y z
