{-# OPTIONS --safe --cubical --guardedness #-}
module ResolutionNetObservationGluing where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (false≢true; true≢false; notEquiv)
open import Cubical.Foundations.Univalence using (uaβ)
open import Cubical.Data.Empty.Base using (⊥)
import IndexIdentityCoherence as Indexed
import IndexIdentityCoherenceRegression as Cover
module Ix = Indexed.Indexed ℓ-zero

-- Joint support is constructed with its actual overlap witnesses.
-- This is a homotopy pushout, not a claim that arbitrary ambient
-- subsets satisfy descent without further assumptions.
module Gluing {ℓ : Level} (X : Type ℓ) (F : X → Type ℓ)
  (L R K : Type ℓ) (toL : K → L) (toR : K → R)
  (p : L → X) (q : R → X)
  (h : (k : K) → p (toL k) ≡ q (toR k)) where

  data Joint : Type ℓ where
    left : L → Joint
    right : R → Joint
    seam : (k : K) → left (toL k) ≡ right (toR k)

  probe : Joint → X
  probe (left l) = p l
  probe (right r) = q r
  probe (seam k i) = h k i

  Compatible : ((l : L) → F (p l)) → ((r : R) → F (q r)) → Type ℓ
  Compatible a b = (k : K) → PathP (λ i → F (h k i)) (a (toL k)) (b (toR k))

  -- Compatibility is supplied evidence, never inferred from endpoints.
  glue : (a : (l : L) → F (p l)) (b : (r : R) → F (q r))
    → Compatible a b → (z : Joint) → F (probe z)
  glue a b c (left l) = a l
  glue a b c (right r) = b r
  glue a b c (seam k i) = c k i

  left-retained : (a : (l : L) → F (p l)) (b : (r : R) → F (q r))
    (c : Compatible a b) → (λ l → glue a b c (left l)) ≡ a
  left-retained a b c = refl

  right-retained : (a : (l : L) → F (p l)) (b : (r : R) → F (q r))
    (c : Compatible a b) → (λ r → glue a b c (right r)) ≡ b
  right-retained a b c = refl

  overlap-retained : (a : (l : L) → F (p l)) (b : (r : R) → F (q r))
    (c : Compatible a b) (k : K)
    → (λ i → glue a b c (seam k i)) ≡ c k
  overlap-retained a b c k = refl

  -- Any joint observation reconstructs from its two restrictions AND
  -- its overlap action. This does not discard higher witness data.
  reconstruct : (s : (z : Joint) → F (probe z))
    → glue (λ l → s (left l)) (λ r → s (right r))
        (λ k i → s (seam k i)) ≡ s
  reconstruct s i (left l) = s (left l)
  reconstruct s i (right r) = s (right r)
  reconstruct s i (seam k j) = s (seam k j)

-- Two point supports, with two overlap comparisons: identity and loop.
-- Both points have local observations; together these comparisons
-- obstruct a joint coherent observation of the double cover.
module Obstruction where
  endpoint : Unit → Ix.Index Cover.F
  endpoint _ = Cover.base-index

  comparison : (k : Bool) → endpoint tt ≡ endpoint tt
  comparison true = refl
  comparison false = Cover.index-loop

  module G = Gluing (Ix.Index Cover.F) (Ix.Fibre Cover.F)
    Unit Unit Bool (λ _ → tt) (λ _ → tt) endpoint endpoint comparison

  local : (u : Unit) → Ix.Fibre Cover.F (endpoint u)
  local _ = true

  incompatible : G.Compatible local local → ⊥
  incompatible c = false≢true (sym flip-proof ∙ fromPathP (c false))
    where
    open import Cubical.Foundations.Univalence using (uaβ)
    open import Cubical.Data.Bool.Properties using (notEquiv)
    flip-proof = uaβ notEquiv true

  -- Stronger: no choice of local Bool values satisfies both overlaps.
  no-joint : ((z : G.Joint) → Ix.Fibre Cover.F (G.probe z)) → ⊥
  no-joint s = no-fixed (s (G.left tt))
    (fromPathP (λ i → s (G.seam false i))
      ∙ sym (λ i → s (G.seam true i)))
    where
    no-fixed : (b : Bool) → subst (Ix.Fibre Cover.F) Cover.index-loop b ≡ b → ⊥
    no-fixed true e = false≢true (sym (uaβ notEquiv true) ∙ e)
    no-fixed false e = true≢false (sym (uaβ notEquiv false) ∙ e)
