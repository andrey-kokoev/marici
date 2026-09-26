{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverTriangleCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using (substComposite)
open import Cubical.Foundations.GroupoidLaws using (rUnit)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import IndexIdentityCoherenceRegression as Cover
import IndexIdentityCoherence as Indexed
module Ix = Indexed.Indexed ℓ-zero

-- A triangle is extra data, not something inferred from three edges.
module Triangle {ℓ : Level} {X : Type ℓ} (F : X → Type ℓ)
  {x y z : X} (p : x ≡ y) (q : y ≡ z) (r : x ≡ z) where

  Cell = p ∙ q ≡ r

  transport-cell : Cell → (u : F x)
    → subst F q (subst F p u) ≡ subst F r u
  transport-cell c u = sym (substComposite F p q u)
    ∙ cong (λ path → subst F path u) c

  -- Local agreement witnesses compose along the two-edge route.
  route : {u : F x} {v : F y} {w : F z}
    → subst F p u ≡ v → subst F q v ≡ w
    → subst F (p ∙ q) u ≡ w
  route {u} a b = substComposite F p q u ∙ cong (subst F q) a ∙ b

  -- A base triangle identifies the route's endpoint type with the
  -- direct route, but does NOT erase the actual agreement witnesses.
  compare-route : (c : Cell) {u : F x} {v : F y} {w : F z}
    → subst F p u ≡ v → subst F q v ≡ w → subst F r u ≡ w
  compare-route c {u} a b = sym (cong (λ path → subst F path u) c) ∙ route a b

  -- Required only when this overlap is specified to carry a 2-cell.
  -- It is an equality BETWEEN agreement witnesses, not endpoints.
  CompatibleLift : (c : Cell) {u : F x} {v : F y} {w : F z}
    (a : subst F p u ≡ v) (b : subst F q v ≡ w)
    (direct : subst F r u ≡ w) → Type ℓ
  CompatibleLift c a b direct = compare-route c a b ≡ direct

  canonical-lift : (c : Cell) {u : F x} {v : F y} {w : F z}
    (a : subst F p u ≡ v) (b : subst F q v ≡ w)
    → CompatibleLift c a b (compare-route c a b)
  canonical-lift c a b = refl

module Obstruction where
  -- All three edges exist, at the same index. No filling exists.
  p q r : Cover.base-index ≡ Cover.base-index
  p = refl
  q = refl
  r = Cover.index-loop

  no-cell : p ∙ q ≡ r → ⊥
  no-cell c = Cover.loop-is-not-reflexive (sym c ∙ sym (rUnit refl))

  -- A coarse observer cannot detect this obstruction from its values.
  -- Equality of observed route results does not imply a base 2-cell.
  coarse-routes-agree :
    subst (λ (_ : Ix.Index Cover.F) → Unit) (p ∙ q) tt
      ≡ subst (λ (_ : Ix.Index Cover.F) → Unit) r tt
  coarse-routes-agree = refl
