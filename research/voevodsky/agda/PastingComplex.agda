{-# OPTIONS --safe --cubical --no-import-sorts --guardedness #-}
module PastingComplex where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Int
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver

record ℤ³ : Type where
  constructor triple
  field
    x y z : ℤ
open ℤ³

∂₁ : ℤ³ → ℤ³
∂₁ v = triple ((- x v) + y v) ((- y v) + z v) ((- z v) + x v)

∂₂ : ℤ³ → ℤ
∂₂ v = (x v + y v) + z v

chain : (v : ℤ³) → ∂₂ (∂₁ v) ≡ 0
chain v = solve! ℤCommRing

-- Normal coordinates for ker ∂₂.
cycle : ℤ → ℤ → ℤ³
cycle p q = triple p q (- (p + q))

cycle-closed : (p q : ℤ) → ∂₂ (cycle p q) ≡ 0
cycle-closed p q = solve! ℤCommRing

∂₂-preimage : ℤ → ℤ³
∂₂-preimage n = triple n 0 0

∂₂-surjective : (n : ℤ) → ∂₂ (∂₂-preimage n) ≡ n
∂₂-surjective n = solve! ℤCommRing

-- A vertex adjustment whose boundary is the normalized cycle.
preimage : ℤ → ℤ → ℤ³
preimage p q = triple 0 p (p + q)

exact-x : (p q : ℤ) → (- 0) + p ≡ p
exact-x p q = solve! ℤCommRing

exact-y : (p q : ℤ) → (- p) + (p + q) ≡ q
exact-y p q = solve! ℤCommRing

exact-z : (p q : ℤ) → (- (p + q)) + 0 ≡ - (p + q)
exact-z p q = solve! ℤCommRing

exact-middle : (p q : ℤ) → ∂₁ (preimage p q) ≡ cycle p q
exact-middle p q i = triple
  (exact-x p q i)
  (exact-y p q i)
  (exact-z p q i)

closed-third : (v : ℤ³) → ∂₂ v ≡ 0 → z v ≡ - (x v + y v)
closed-third v h =
  sym (solve! ℤCommRing)
  ∙ cong (λ t → t + (- (x v + y v))) h
  ∙ solve! ℤCommRing

closed-normal-form : (v : ℤ³) → ∂₂ v ≡ 0 → v ≡ cycle (x v) (y v)
closed-normal-form v h i = triple (x v) (y v) (closed-third v h i)

middle-exact : (v : ℤ³) → ∂₂ v ≡ 0 → Σ[ u ∈ ℤ³ ] ∂₁ u ≡ v
middle-exact v h =
  preimage (x v) (y v) ,
  exact-middle (x v) (y v) ∙ sym (closed-normal-form v h)

_+³_ : ℤ³ → ℤ³ → ℤ³
u +³ v = triple (x u + x v) (y u + y v) (z u + z v)

difference : ℤ³ → ℤ³ → ℤ³
difference u v = triple (x u + (- x v)) (y u + (- y v)) (z u + (- z v))

difference-closed : (f g : ℤ³) → ∂₂ f ≡ ∂₂ g → ∂₂ (difference f g) ≡ 0
difference-closed f g h =
  (solve! ℤCommRing)
  ∙ cong (λ t → t + (- ∂₂ g)) h
  ∙ solve! ℤCommRing

restore-x : (f g u : ℤ³) → ∂₁ u ≡ difference f g → x f ≡ x (∂₁ u +³ g)
restore-x f g u p = sym (cong (λ t → t + x g) (cong x p) ∙ solve! ℤCommRing)

restore-y : (f g u : ℤ³) → ∂₁ u ≡ difference f g → y f ≡ y (∂₁ u +³ g)
restore-y f g u p = sym (cong (λ t → t + y g) (cong y p) ∙ solve! ℤCommRing)

restore-z : (f g u : ℤ³) → ∂₁ u ≡ difference f g → z f ≡ z (∂₁ u +³ g)
restore-z f g u p = sym (cong (λ t → t + z g) (cong z p) ∙ solve! ℤCommRing)

unique-mod-adjustment :
  (f g : ℤ³) → ∂₂ f ≡ ∂₂ g → Σ[ u ∈ ℤ³ ] f ≡ ∂₁ u +³ g
unique-mod-adjustment f g h =
  u , λ i → triple (restore-x f g u p i)
                 (restore-y f g u p i)
                 (restore-z f g u p i)
  where
  witness : Σ[ u ∈ ℤ³ ] ∂₁ u ≡ difference f g
  witness = middle-exact (difference f g) (difference-closed f g h)

  u : ℤ³
  u = witness .fst

  p : ∂₁ u ≡ difference f g
  p = witness .snd
