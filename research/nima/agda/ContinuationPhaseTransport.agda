{-# OPTIONS --safe --cubical --guardedness #-}
module ContinuationPhaseTransport where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Equiv.Properties
import WholePackageSigmaPi as Whole

-- Function types already occur as maps in the retained universe. Equivalences
-- on states and answers are supplied; this does not derive a U(1) field.
module Transport {ℓ : Level} (V R : Type ℓ) (e : V ≃ V) (h : R ≃ R) where
  Effect = V → R
  Future = Effect → R

  effect : Effect → Effect
  effect f y = equivFun h (f (invEq e y))

  evaluation-covariant : (f : Effect) (x : V)
    → effect f (equivFun e x) ≡ equivFun h (f x)
  evaluation-covariant f x = cong (λ y → equivFun h (f y)) (retEq e x)

  -- Requiring evaluation covariance at every input uniquely determines the
  -- transformed effect. Inverse input transport is not an assigned sign.
  effect-unique : (f k : Effect)
    → ((x : V) → k (equivFun e x) ≡ equivFun h (f x))
    → k ≡ effect f
  effect-unique f k law = funExt λ y →
    cong k (sym (secEq e y)) ∙ law (invEq e y)

  back-effect : Effect → Effect
  back-effect f x = invEq h (f (equivFun e x))

  future : Future → Future
  future c f = equivFun h (c (back-effect f))

  present : V → Future
  present x f = f x

  -- Promoting a value into continuation form preserves its original action;
  -- the second contravariance does not make it oppositely charged.
  present-natural : (x : V) → future (present x) ≡ present (equivFun e x)
  present-natural x = funExt λ f → secEq h (f (equivFun e x))

  module W = Whole.Universe ℓ
  state-code : W.Code
  state-code = W.atom V
  answer-code : W.Code
  answer-code = W.atom R
  effect-code : W.Code
  effect-code = W.maps state-code answer-code
  future-code : W.Code
  future-code = W.maps effect-code answer-code

  -- Retain the original input beside its continuation presentation.
  retained-future : V → W.Complete
  retained-future x = W.pack (W.retain state-code x future-code) (present x)
  retained-value : (x : V) → W.value (retained-future x) ≡ present x
  retained-value x = refl
