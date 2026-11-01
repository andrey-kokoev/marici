{-# OPTIONS --safe --cubical --guardedness #-}
module TwistedRouteReturn where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; false; true; not)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import CoherentFourReturn using (Four; q0; q1; q2; q3)

four : ∀ {ℓ} {S : Type ℓ} → (S → S) → S → S
four G a = G (G (G (G a)))

-- Reference-level theorem only: the original twisted witness is an input.
module Twisted {ℓ : Level} {S : Type ℓ} (G R : S → S)
  (commute : (a : S) → G (R a) ≡ R (G a))
  (involution : (a : S) → R (R a) ≡ a) where

  commute-four : (a : S) → four G (R a) ≡ R (four G a)
  commute-four a =
    cong (λ x → G (G (G x))) (commute a)
    ∙ cong (λ x → G (G x)) (commute (G a))
    ∙ cong G (commute (G (G a)))
    ∙ commute (G (G (G a)))

  eight-return : (a : S) → four G a ≡ R a → four G (four G a) ≡ a
  eight-return a p = cong (four G) p ∙ commute-four a ∙ cong R p ∙ involution a

module Program where
  -- The Bool is retained orientation-chart data, not a physical charge.
  Frame : Type
  Frame = Σ Bool (λ _ → Four)

  dual : Frame → Frame
  dual (b , k) = not b , k

  step : Frame → Frame
  step (b , q0) = b , q1
  step (b , q1) = b , q2
  step (b , q2) = b , q3
  step (b , q3) = not b , q0

  dual-involution : (s : Frame) → dual (dual s) ≡ s
  dual-involution (false , k) = refl
  dual-involution (true , k) = refl

  step-commutes : (s : Frame) → step (dual s) ≡ dual (step s)
  step-commutes (b , q0) = refl
  step-commutes (b , q1) = refl
  step-commutes (b , q2) = refl
  step-commutes (b , q3) = refl

  four-is-dual : (s : Frame) → four step s ≡ dual s
  four-is-dual (b , q0) = refl
  four-is-dual (b , q1) = refl
  four-is-dual (b , q2) = refl
  four-is-dual (b , q3) = refl

  not-fixed : (b : Bool) → not b ≡ b → ⊥
  not-fixed false p = true≢false p
  not-fixed true p = true≢false (sym p)

  no-ordinary-four-return : (s : Frame) → four step s ≡ s → ⊥
  no-ordinary-four-return s p =
    not-fixed (s .fst) (cong fst (sym (four-is-dual s) ∙ p))

  no-Per4 : Σ Frame (λ s → four step s ≡ s) → ⊥
  no-Per4 (s , p) = no-ordinary-four-return s p

  eight-is-return : (s : Frame) → four step (four step s) ≡ s
  eight-is-return s = Twisted.eight-return step dual step-commutes dual-involution s (four-is-dual s)

  -- Forgetting orientation produces a four-cycle, but is non-injective.
  phase : Frame → Four
  phase = snd

  same-phase : (k : Four) → phase (false , k) ≡ phase (true , k)
  same-phase k = refl

  distinct-frames : (k : Four) → Path Frame (false , k) (true , k) → ⊥
  distinct-frames k p = true≢false (sym (cong fst p))
