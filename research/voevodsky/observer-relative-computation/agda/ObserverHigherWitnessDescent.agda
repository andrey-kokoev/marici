{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverHigherWitnessDescent where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.GroupoidLaws using (lUnit; lCancel)
open import Cubical.Data.Sigma.Base using (_,_; fst)
open import Cubical.Data.Sigma.Properties using (Σ≡Prop)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (squash₁)
open import ObserverAdmissibleImages
import ObserverSetImageDescent as SetDescent
import IndexIdentityCoherenceRegression as Cover
import IndexIdentityCoherence as Indexed
module Ix = Indexed.Indexed ℓ-zero

-- A single source. The target retains genuine higher index paths.
f : Unit → Unit
f _ = tt
g : Unit → Ix.Index Cover.F
g _ = Cover.base-index
module C = SetDescent.Criterion f g

-- Ordinary image factorization does exist.
factor : ImageFactors f g
factor = (λ _ → arrive g tt) , (λ { tt → refl })

-- Every requested endpoint equality has this inhabitant. But the
-- chosen action sends even an identity collision to a nontrivial loop.
chosen : C.Preserves
chosen _ _ _ = Cover.index-loop

image-prop : isProp (Image f)
image-prop u v = Σ≡Prop (λ _ → squash₁) refl

image-self : arrive f tt ≡ arrive f tt
image-self = Σ≡Prop (λ _ → squash₁) refl

image-self-trivial : image-self ≡ refl
image-self-trivial = isProp→isSet image-prop _ _ image-self refl

-- Any actual factor induces the identity comparison on this identity
-- collision, even if its source-arrival witness is itself nontrivial.
induced-identity : (w : ImageFactors f g) → C.necessary w tt tt refl ≡ refl
induced-identity (post , exact) =
  cong (λ e → cong fst (sym (exact tt) ∙ cong post e ∙ exact tt)) image-self-trivial
  ∙ cong (λ tail → cong fst (sym (exact tt) ∙ tail)) (sym (lUnit (exact tt)))
  ∙ cong (cong fst) (lCancel (exact tt))

-- No factor retains this particular family of comparison witnesses.
-- This is NOT nonexistence of all factors: factor above is explicit.
no-faithful-factor : (w : ImageFactors f g)
  → ((x y : Unit) (e : f x ≡ f y) → C.necessary w x y e ≡ chosen x y e)
  → ⊥
no-faithful-factor w retains = Cover.loop-is-not-reflexive
  (sym (retains tt tt refl) ∙ induced-identity w)

-- The obstruction is already a unit-coherence failure, before any
-- general multi-dimensional descent theorem is attempted.
chosen-breaks-unit : chosen tt tt refl ≡ refl → ⊥
chosen-breaks-unit = Cover.loop-is-not-reflexive
