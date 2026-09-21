{-# OPTIONS --safe --cubical --guardedness #-}
module ClosureContextualPortCoherence where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (lUnit; assoc; cong-∙)

-- Transport a port square through an inclusion and flattening map.
-- Both the leading composition unit and the prescribed nested port
-- witnesses are retained; they are not treated as judgmental identities.
postPort : {Y Z W : Type} (include : Y → Z) (flatten : Z → W)
  {x₀ x₁ m z : Y} {target : W}
  (h : x₀ ≡ x₁) (p : x₀ ≡ m) (q : m ≡ z) (v : x₁ ≡ z)
  (t : flatten (include z) ≡ target)
  (coherence : PathP (λ i → h i ≡ z) (p ∙ q) v) →
  PathP (λ i → cong flatten (refl ∙ cong include h) i ≡ target)
    (cong (λ x → flatten (include x)) p ∙ (cong (λ x → flatten (include x)) q ∙ t))
    (cong (λ x → flatten (include x)) v ∙ t)
postPort include flatten {target = target} h p q v t coherence =
  subst (λ k → PathP (λ i → k i ≡ target) start finish)
    (sym (cong (cong flatten) (sym (lUnit (cong include h)))))
    (subst (λ s → PathP (λ i → image (h i) ≡ target) s finish)
      (sym adjustStart) (λ i → cong image (coherence i) ∙ t))
  where
  image = λ x → flatten (include x)
  start = cong image p ∙ (cong image q ∙ t)
  finish = cong image v ∙ t
  adjustStart : start ≡ cong image (p ∙ q) ∙ t
  adjustStart = assoc (cong image p) (cong image q) t
    ∙ cong (λ r → r ∙ t) (sym (cong-∙ image p q))
