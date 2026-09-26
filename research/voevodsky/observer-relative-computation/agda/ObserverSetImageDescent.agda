{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverSetImageDescent where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.HLevels using (isSetΣ)
open import Cubical.Data.Sigma.Base using (Σ; _,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
open import ObserverAdmissibleImages

module Criterion {X Y Z : Type} (f : X → Y) (g : X → Z) where
  Preserves = (x x' : X) → f x ≡ f x' → g x ≡ g x'

  -- Necessary without any truncation-level assumption on Z.
  necessary : ImageFactors f g → Preserves
  necessary (post , exact) x x' e = cong fst
    (sym (exact x) ∙ cong post (Σ≡Prop (λ _ → squash₁) e) ∙ exact x')

  module SetOutput (Zset : isSet Z) where
    image-set : isSet (Image g)
    image-set = isSetΣ Zset (λ _ → isProp→isSet squash₁)

    fibre-constant : (k : Preserves) (y : Y) (u v : Fibre f y)
      → arrive g (fst u) ≡ arrive g (fst v)
    fibre-constant k y (x , e) (x' , e') =
      Σ≡Prop (λ _ → squash₁) (k x x' (e ∙ sym e'))

    -- Weak constancy is enough to eliminate the truncated fibre into
    -- this SET. No arbitrary origin is selected or returned.
    descend : Preserves → Image f → Image g
    descend k (y , possible) = Trunc.rec→Set image-set
      (λ origin → arrive g (fst origin)) (fibre-constant k y) possible

    arrival-law : (k : Preserves) (x : X)
      → descend k (arrive f x) ≡ arrive g x
    arrival-law k x = refl

    sufficient : Preserves → ImageFactors f g
    sufficient k = descend k , arrival-law k

    -- Uniqueness on admissible outputs, not on unreachable elements of Y.
    unique : (k : Preserves) (post : Image f → Image g)
      (exact : (x : X) → post (arrive f x) ≡ arrive g x)
      (i : Image f) → post i ≡ descend k i
    unique k post exact (y , possible) = Trunc.elim
      (λ t → image-set (post (y , t)) (descend k (y , t)))
      (λ { (x , e) → sym (cong post
        (Σ≡Prop (λ _ → squash₁) {u = arrive f x} {v = y , ∣ x , e ∣₁} e)) ∙ exact x })
      possible
