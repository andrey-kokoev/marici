{-# OPTIONS --safe --cubical --guardedness #-}
module ForgottenDiamondBoundary where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver
open import Cubical.Data.Empty using (⊥)

-- Coordinate identities over any commutative ring. Degrees of the primal
-- complexes are -1,0; degrees of the transposed duals are 0,1.
module Comparison {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  Scalar = fst R

  record V₂ : Type ℓ where
    constructor v₂
    field first₂ second₂ : Scalar
  open V₂

  record V₄ : Type ℓ where
    constructor v₄
    field first₄ second₄ third₄ fourth₄ : Scalar
  open V₄

  eq₂ : {a b c d : Scalar} → a ≡ c → b ≡ d → v₂ a b ≡ v₂ c d
  eq₂ p q i = v₂ (p i) (q i)

  eq₄ : {a b c d e f g h : Scalar} →
    a ≡ e → b ≡ f → c ≡ g → d ≡ h → v₄ a b c d ≡ v₄ e f g h
  eq₄ p q r s i = v₄ (p i) (q i) (r i) (s i)

  zero₂ : V₂
  zero₂ = v₂ 0r 0r
  zero₄ : V₄
  zero₄ = v₄ 0r 0r 0r 0r

  sub₂ : V₂ → V₂ → V₂
  sub₂ (v₂ a b) (v₂ c d) = v₂ (a + (- c)) (b + (- d))
  sub₄ : V₄ → V₄ → V₄
  sub₄ (v₄ a b c d) (v₄ e f g h) =
    v₄ (a + (- e)) (b + (- f)) (c + (- g)) (d + (- h))

  -- Vertices: 2,4,6,12. Edges: 24,26,4-12,6-12.
  incidence : V₄ → V₄
  incidence (v₄ a b c d) = v₄ ((- a) + (- b)) (a + (- c)) (b + (- d)) (c + d)

  -- Both endpoint attachments are retained: (fold,-fold).
  boundary : V₂ → V₂
  boundary (v₂ a b) = v₂ (a + b) ((- a) + (- b))

  project₀ project₁ : V₄ → V₂
  project₀ (v₄ a b c d) = v₂ ((a + b) + d) c
  project₁ (v₄ a b c d) = v₂ (- b) d

  include₀ include₁ : V₂ → V₄
  include₀ (v₂ a b) = v₄ 0r a b 0r
  include₁ (v₂ a b) = v₄ a (- a) (- b) b

  homotopy : V₄ → V₄
  homotopy (v₄ a b c d) = v₄ (- a) 0r d 0r

  project-chain : (x : V₄) → project₀ (incidence x) ≡ boundary (project₁ x)
  project-chain (v₄ a b c d) = eq₂ (solve! R) (solve! R)

  include-chain : (x : V₂) → incidence (include₁ x) ≡ include₀ (boundary x)
  include-chain (v₂ a b) = eq₄ (solve! R) (solve! R) (solve! R) (solve! R)

  retract₀ : (x : V₂) → project₀ (include₀ x) ≡ x
  retract₀ (v₂ a b) = eq₂ (solve! R) (solve! R)
  retract₁ : (x : V₂) → project₁ (include₁ x) ≡ x
  retract₁ (v₂ a b) = eq₂ (solve! R) (solve! R)

  homotopy₀ : (x : V₄) → incidence (homotopy x) ≡ sub₄ x (include₀ (project₀ x))
  homotopy₀ (v₄ a b c d) = eq₄ (solve! R) (solve! R) (solve! R) (solve! R)
  homotopy₁ : (x : V₄) → homotopy (incidence x) ≡ sub₄ x (include₁ (project₁ x))
  homotopy₁ (v₄ a b c d) = eq₄ (solve! R) (solve! R) (solve! R) (solve! R)

  cycle : Scalar → V₄
  cycle t = v₄ t (- t) t (- t)
  endpointDifference : Scalar → V₂
  endpointDifference t = v₂ t (- t)

  cycle-closed : (t : Scalar) → incidence (cycle t) ≡ zero₄
  cycle-closed t = eq₄ (solve! R) (solve! R) (solve! R) (solve! R)
  cycle-image : (t : Scalar) → project₁ (cycle t) ≡ endpointDifference t
  cycle-image t = eq₂ (solve! R) (solve! R)
  endpoint-closed : (t : Scalar) → boundary (endpointDifference t) ≡ zero₂
  endpoint-closed t = eq₂ (solve! R) (solve! R)

  cycle-nonzero : ((1r ≡ 0r) → ⊥) → (cycle 1r ≡ zero₄) → ⊥
  cycle-nonzero nontrivial p = nontrivial (cong first₄ p)
  endpoint-nonzero : ((1r ≡ 0r) → ⊥) → (endpointDifference 1r ≡ zero₂) → ⊥
  endpoint-nonzero nontrivial p = nontrivial (cong first₂ p)

  -- A second explicit retract: the boundary complex to one scalar in each
  -- of degrees -1 and 0 with zero differential. No quotient construction.
  scalarProject₀ scalarProject₁ : V₂ → Scalar
  scalarProject₀ (v₂ a b) = a + b
  scalarProject₁ (v₂ a b) = a
  scalarInclude₀ scalarInclude₁ : Scalar → V₂
  scalarInclude₀ a = v₂ a 0r
  scalarInclude₁ = endpointDifference
  scalarHomotopy : V₂ → V₂
  scalarHomotopy (v₂ a b) = v₂ 0r (- b)

  scalar-project-chain : (x : V₂) → scalarProject₀ (boundary x) ≡ 0r
  scalar-project-chain (v₂ a b) = solve! R
  scalar-retract₀ : (a : Scalar) → scalarProject₀ (scalarInclude₀ a) ≡ a
  scalar-retract₀ a = solve! R
  scalar-retract₁ : (a : Scalar) → scalarProject₁ (scalarInclude₁ a) ≡ a
  scalar-retract₁ a = refl
  scalar-homotopy₀ : (x : V₂) → boundary (scalarHomotopy x) ≡
    sub₂ x (scalarInclude₀ (scalarProject₀ x))
  scalar-homotopy₀ (v₂ a b) = eq₂ (solve! R) (solve! R)
  scalar-homotopy₁ : (x : V₂) → scalarHomotopy (boundary x) ≡
    sub₂ x (scalarInclude₁ (scalarProject₁ x))
  scalar-homotopy₁ (v₂ a b) = eq₂ (solve! R) (solve! R)

  -- Transposed coefficient dual: differential is MINUS the transpose.
  dualIncidence : V₄ → V₄
  dualIncidence (v₄ a b c d) = v₄ (a + (- b)) (a + (- c)) (b + (- d)) (c + (- d))
  dualBoundary : V₂ → V₂
  dualBoundary (v₂ a b) = v₂ ((- a) + b) ((- a) + b)

  dualInclude₀ dualInclude₁ : V₂ → V₄
  dualInclude₀ (v₂ a b) = v₄ a a b a
  dualInclude₁ (v₂ a b) = v₄ 0r (- a) 0r b
  dualProject₀ dualProject₁ : V₄ → V₂
  dualProject₀ (v₄ a b c d) = v₂ b c
  dualProject₁ (v₄ a b c d) = v₂ (a + (- b)) ((- c) + d)

  -- Minus the transpose of the primal homotopy in these cochain degrees.
  dualHomotopy : V₄ → V₄
  dualHomotopy (v₄ a b c d) = v₄ a 0r 0r (- c)

  dual-include-chain : (x : V₂) → dualIncidence (dualInclude₀ x) ≡ dualInclude₁ (dualBoundary x)
  dual-include-chain (v₂ a b) = eq₄ (solve! R) (solve! R) (solve! R) (solve! R)
  dual-project-chain : (x : V₄) → dualProject₁ (dualIncidence x) ≡ dualBoundary (dualProject₀ x)
  dual-project-chain (v₄ a b c d) = eq₂ (solve! R) (solve! R)
  dual-retract₀ : (x : V₂) → dualProject₀ (dualInclude₀ x) ≡ x
  dual-retract₀ (v₂ a b) = refl
  dual-retract₁ : (x : V₂) → dualProject₁ (dualInclude₁ x) ≡ x
  dual-retract₁ (v₂ a b) = eq₂ (solve! R) (solve! R)
  dual-homotopy₀ : (x : V₄) → dualHomotopy (dualIncidence x) ≡
    sub₄ x (dualInclude₀ (dualProject₀ x))
  dual-homotopy₀ (v₄ a b c d) = eq₄ (solve! R) (solve! R) (solve! R) (solve! R)
  dual-homotopy₁ : (x : V₄) → dualIncidence (dualHomotopy x) ≡
    sub₄ x (dualInclude₁ (dualProject₁ x))
  dual-homotopy₁ (v₄ a b c d) = eq₄ (solve! R) (solve! R) (solve! R) (solve! R)

  -- Verify the transpose assertions themselves via evaluation pairings.
  dot₂ : V₂ → V₂ → Scalar
  dot₂ (v₂ a b) (v₂ c d) = a · c + b · d
  dot₄ : V₄ → V₄ → Scalar
  dot₄ (v₄ a b c d) (v₄ e f g h) = ((a · e + b · f) + c · g) + d · h

  incidence-dual-sign : (x y : V₄) → dot₄ (incidence x) y ≡ - (dot₄ x (dualIncidence y))
  incidence-dual-sign (v₄ a b c d) (v₄ e f g h) = solve! R
  boundary-dual-sign : (x y : V₂) → dot₂ (boundary x) y ≡ - (dot₂ x (dualBoundary y))
  boundary-dual-sign (v₂ a b) (v₂ c d) = solve! R
  project₀-transpose : (x : V₄) (y : V₂) → dot₂ (project₀ x) y ≡ dot₄ x (dualInclude₀ y)
  project₀-transpose (v₄ a b c d) (v₂ e f) = solve! R
  project₁-transpose : (x : V₄) (y : V₂) → dot₂ (project₁ x) y ≡ dot₄ x (dualInclude₁ y)
  project₁-transpose (v₄ a b c d) (v₂ e f) = solve! R
  include₀-transpose : (x : V₂) (y : V₄) → dot₄ (include₀ x) y ≡ dot₂ x (dualProject₀ y)
  include₀-transpose (v₂ a b) (v₄ c d e f) = solve! R
  include₁-transpose : (x : V₂) (y : V₄) → dot₄ (include₁ x) y ≡ dot₂ x (dualProject₁ y)
  include₁-transpose (v₂ a b) (v₄ c d e f) = solve! R
  homotopy-dual-sign : (x y : V₄) → dot₄ (homotopy x) y ≡ - (dot₄ x (dualHomotopy y))
  homotopy-dual-sign (v₄ a b c d) (v₄ e f g h) = solve! R

  -- The cycle has an explicit dual class, not just a dimension count.
  observer : V₂
  observer = v₂ 1r 0r
  difference : V₂ → Scalar
  difference (v₂ a b) = a + (- b)
  observer-difference : difference observer ≡ 1r
  observer-difference = solve! R
  difference-boundary : (x : V₂) → difference (dualBoundary x) ≡ 0r
  difference-boundary (v₂ a b) = solve! R
  observer-not-boundary : ((1r ≡ 0r) → ⊥) →
    (x : V₂) → (dualBoundary x ≡ observer) → ⊥
  observer-not-boundary nontrivial x p = nontrivial
    (sym observer-difference ∙ sym (cong difference p) ∙ difference-boundary x)
  detects-cycle : dot₂ (endpointDifference 1r) observer ≡ 1r
  detects-cycle = solve! R

  -- Replacing the two-endpoint boundary by one line removes its kernel.
  one-endpoint-no-cycle : (t : Scalar) → endpointDifference t ≡ zero₂ → t ≡ 0r
  one-endpoint-no-cycle t p = cong first₂ p
