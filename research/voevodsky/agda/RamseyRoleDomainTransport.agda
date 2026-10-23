{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyRoleDomainTransport where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Nat.Base using (ℕ)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Relation.Nullary using (¬_)
open import RamseyUniformRelative using (first; next)
open import RamseySingleFrameFaces

-- Geometry-only chart transition: world vertices are fixed.
change : Iso Vertex Vertex → Iso Vertex Vertex → Vertex → Vertex
change f g v = Iso.inv g (Iso.fun f v)
geometry-cell : (f g : Iso Vertex Vertex) (v : Vertex) → Iso.fun g (change f g v) ≡ Iso.fun f v
geometry-cell f g v = Iso.rightInv g (Iso.fun f v)
identity-cell : (f : Iso Vertex Vertex) (v : Vertex) → change f f v ≡ v
identity-cell f v = Iso.leftInv f v
cocycle-cell : (f g h : Iso Vertex Vertex) (v : Vertex)
  → change g h (change f g v) ≡ change f h v
cocycle-cell f g h v = cong (Iso.inv h) (Iso.rightInv g (Iso.fun f v))
data FullVertex : Type where
  body-vertex : Vertex → FullVertex
  outside-c2 : FullVertex
full-change : Iso Vertex Vertex → Iso Vertex Vertex → FullVertex → FullVertex
full-change f g (body-vertex v) = body-vertex (change f g v)
full-change f g outside-c2 = outside-c2
full-cocycle : (f g h : Iso Vertex Vertex) (v : FullVertex)
  → full-change g h (full-change f g v) ≡ full-change f h v
full-cocycle f g h (body-vertex v) = cong body-vertex (cocycle-cell f g h v)
full-cocycle f g h outside-c2 = refl

swap-role : Vertex → Vertex
swap-role c0 = c0
swap-role m0 = c1
swap-role c1 = m0
swap-role m1 = m1
swap-square : (v : Vertex) → swap-role (swap-role v) ≡ v
swap-square c0 = refl
swap-square m0 = refl
swap-square c1 = refl
swap-square m1 = refl
role-chart : Iso Vertex Vertex
Iso.fun role-chart = swap-role
Iso.inv role-chart = swap-role
Iso.rightInv role-chart = swap-square
Iso.leftInv role-chart = swap-square
-- The target M-indicator on the SAME geometric vertex set.
target-role : Vertex → ℕ
target-role v = M-role (swap-role v)
target-count : Vertex → ℕ
target-count v = count (λ i → target-role (face v i))
TargetEligible : Vertex → Type
TargetEligible v = target-count v ≡ 2
shared-PN-face : Σ (Eligible c0) (λ _ → TargetEligible c0)
shared-PN-face = refl , refl
source-lost-face : Eligible c1
source-lost-face = refl
target-lost-face : ¬ TargetEligible c1
target-lost-face = one-not-two
SourceDomain TargetDomain : Type
SourceDomain = Σ Vertex Eligible
TargetDomain = Σ Vertex TargetEligible
OverGeometry : (SourceDomain → TargetDomain) → Type
OverGeometry transition = (p : SourceDomain) → fst (transition p) ≡ fst p
no-total-fixed-face-map : (transition : SourceDomain → TargetDomain) → ¬ OverGeometry transition
no-total-fixed-face-map transition over = target-lost-face
  (subst TargetEligible (over (c1 , source-lost-face)) (snd (transition (c1 , source-lost-face))))
-- A partial adapter on the shared law domain is NOT refuted.
IntersectionDomain : Type
IntersectionDomain = Σ Vertex (λ v → Σ (Eligible v) (λ _ → TargetEligible v))
source-port : IntersectionDomain → SourceDomain
source-port (v , (p , q)) = v , p
target-port : IntersectionDomain → TargetDomain
target-port (v , (p , q)) = v , q
partial-geometry : (x : IntersectionDomain) → fst (source-port x) ≡ fst (target-port x)
partial-geometry x = refl
