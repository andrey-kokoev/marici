{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverGroupoidImageDescent where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Function using (3-Constant)
open import Cubical.Foundations.HLevels using (isGroupoidΣ; isSet→isGroupoid)
open import Cubical.Data.Sigma.Base using (_,_; fst; snd)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.HITs.PropositionalTruncation.Base using (∣_∣₁; squash₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
open import ObserverAdmissibleImages

module Criterion {X Y Z : Type} (f : X → Y) (g : X → Z) where
  origin-output : (y : Y) → Fibre f y → Image g
  origin-output y origin = arrive g (fst origin)

  -- This is a dependent family over y, not unrelated choices of data.
  -- Each 3-Constant record supplies links and their triangle squares.
  CoherentFibres = (y : Y) → 3-Constant (origin-output y)

  module Sufficient (Zgroupoid : isGroupoid Z) (coherence : CoherentFibres) where
    image-groupoid : isGroupoid (Image g)
    image-groupoid = isGroupoidΣ Zgroupoid
      (λ _ → isSet→isGroupoid (isProp→isSet squash₁))

    descend : Image f → Image g
    descend (y , possible) = Trunc.rec→Gpd image-groupoid
      (origin-output y) (coherence y) possible

    arrival : (x : X) → descend (arrive f x) ≡ arrive g x
    arrival x = refl

    factor : ImageFactors f g
    factor = descend , arrival

    -- Retain the SPECIFIED links, not just their endpoint equalities.
    link-retained : (y : Y) (u v : Fibre f y)
      → (λ i → descend (y , squash₁ ∣ u ∣₁ ∣ v ∣₁ i))
        ≡ 3-Constant.link (coherence y) u v
    link-retained y u v = refl

    -- The supplied triangle witness is also recovered by computation.
    triangle-retained : (y : Y) (u v w : Fibre f y)
      → (λ i j → descend (y , squash₁ ∣ u ∣₁ (squash₁ ∣ v ∣₁ ∣ w ∣₁ i) j))
        ≡ 3-Constant.coh₁ (coherence y) u v w
    triangle-retained y u v w = refl

  -- Existing factors supply coherent fibre data even without Zgroupoid.
  -- Endpoint changes are retained by transporting the whole record.
  necessary : ImageFactors f g → CoherentFibres
  necessary (post , exact) y = subst 3-Constant (funExt agrees) raw-coherence
    where
    raw : Fibre f y → Image g
    raw origin = post (y , ∣ origin ∣₁)

    agrees : (origin : Fibre f y) → raw origin ≡ origin-output y origin
    agrees (x , e) = sym (cong post
      (Σ≡Prop (λ _ → squash₁) {u = arrive f x} {v = y , ∣ x , e ∣₁} e)) ∙ exact x

    raw-coherence : 3-Constant raw
    3-Constant.link raw-coherence u v i = post (y , squash₁ ∣ u ∣₁ ∣ v ∣₁ i)
    3-Constant.coh₁ raw-coherence u v w i j =
      post (y , squash₁ ∣ u ∣₁ (squash₁ ∣ v ∣₁ ∣ w ∣₁ i) j)
