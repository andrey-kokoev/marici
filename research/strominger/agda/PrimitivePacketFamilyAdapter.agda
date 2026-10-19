{-# OPTIONS --safe --cubical --guardedness #-}
module PrimitivePacketFamilyAdapter where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Maybe.Base using (just)
import WholePackageSigmaPi as W

-- An adapter for SUPPLIED families and witnessed comparisons. No enumeration
-- of continuations, phase selection, quotient or leaf-count law is assumed.
module Adapter (ℓ : Level) (I : Type ℓ)
  (F G : I → W.Universe.Complete ℓ)
  (e : (i : I) → W.Universe.El ℓ (W.Universe.expression (F i))
                   ≃ W.Universe.El ℓ (W.Universe.expression (G i)))
  (p : (i : I) → equivFun (e i) (W.Universe.value (F i))
                   ≡ W.Universe.value (G i)) where

  module U = W.Universe ℓ
  module C = U.Congruence I F G e p

  source : U.Complete
  source = U.Pi-package I F

  target : U.Complete
  target = U.Pi-package I G

  -- The unary comparison is reflexive on this supplied source; it is not a
  -- proof of stability against an independently supplied previous phase.
  stable : U.Complete
  stable = U.identity-comparison source

  source-family-retained : U.input-family (U.expression source)
    ≡ just (I , (λ i → just (F i)))
  source-family-retained = U.Pi-retains-family I F

  target-family-retained : U.input-family (U.expression target)
    ≡ just (I , (λ i → just (G i)))
  target-family-retained = U.Pi-retains-family I G

  -- This is an actual family payload action, not an inference from a bare edge.
  move : ((i : I) → U.El (U.expression (F i)))
       → ((i : I) → U.El (U.expression (G i)))
  move x i = equivFun (e i) (x i)

  -- The diagonal comparison: assemble then move, or move each component
  -- then read the supplied target assembly. The actual path p is preserved.
  square : move (U.value source) ≡ U.value target
  square = funExt p

  square-at : (i : I) → (λ j → square j i) ≡ p i
  square-at i = refl

  reconciled : U.Complete
  reconciled = C.Pi-comparison

  joint-comparisons-retained : U.recover (U.expression reconciled)
    ≡ just C.all-comparisons
  joint-comparisons-retained = refl

  witness-retained : (i : I)
    → snd (snd (U.value C.all-comparisons i)) ≡ p i
  witness-retained i = refl

  -- Keep the unary-stage evidence as well, without replacing the comparison.
  terminal : U.Complete
  terminal = U.remember stable reconciled

  stable-retained : U.recover (U.expression terminal) ≡ just stable
  stable-retained = refl

  -- Explicit universe increase; no universe contains itself.
  next-input : W.Universe.Complete (ℓ-suc ℓ)
  next-input = W.reify terminal

  next-input-recovers-terminal : W.Universe.value next-input ≡ terminal
  next-input-recovers-terminal = W.reify-retains-all terminal

  -- The exact terminal packet can be consumed by the existing whole-family
  -- constructor, retaining one copy at each supplied port. This is reuse,
  -- not a claim that those ports constitute newly generated continuations.
  reused : W.Universe.Complete (ℓ-suc ℓ)
  reused = W.Pi-whole I (λ _ → terminal)

  reused-entry : (i : I) → W.Universe.value reused (lift i) ≡ terminal
  reused-entry i = W.Pi-whole-entry I (λ _ → terminal) i
