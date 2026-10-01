{-# OPTIONS --safe --cubical --guardedness #-}
module SeedTriangleRouteBinding where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.List.Base using (List; []; _∷_)
open import Cubical.Data.Sum.Base using (inl; inr)
import WholePackageSigmaPi as Whole
import NativeNormalizationRouteCompiler as Native

-- An interface, not an instance identifying the actual six-arrow seed.
-- Occurrence identities are supplied; this module does not allocate events.
module Contract (ℓ : Level) (Q : Whole.Universe.Code ℓ) (Occurrence : Type ℓ) where
  module N = Native.Compiler ℓ Q
  module H = N.H
  open Whole.Universe ℓ using (El)

  record Binding : Type (ℓ-suc ℓ) where
    field
      A B C : H.Presentation
      AB : H.CoherentMap A B
      BC : H.CoherentMap B C
      CA : H.CoherentMap C A
      occurrence-AB occurrence-BC occurrence-CA : Occurrence
      AB≠BC : occurrence-AB ≡ occurrence-BC → ⊥
      BC≠CA : occurrence-BC ≡ occurrence-CA → ⊥
      CA≠AB : occurrence-CA ≡ occurrence-AB → ⊥

  loop : (b : Binding) → H.Route (Binding.A b) (Binding.A b)
  loop b = H.next {P = Binding.A b} {R = Binding.B b} {T = Binding.A b}
    (Binding.AB b)
    (H.next {P = Binding.B b} {R = Binding.C b} {T = Binding.A b}
      (Binding.BC b)
      (H.next {P = Binding.C b} {R = Binding.A b} {T = Binding.A b}
        (Binding.CA b) (H.stop {P = Binding.A b})))

  steps : {P R : H.Presentation} → H.Route P R → ℕ
  steps H.stop = 0
  steps (H.next f rest) = suc (steps rest)

  three-steps : (b : Binding) → steps (loop b) ≡ 3
  three-steps b = refl

  occurrences : Binding → List Occurrence
  occurrences b = Binding.occurrence-AB b ∷ Binding.occurrence-BC b
    ∷ Binding.occurrence-CA b ∷ []

  -- Bind each native compilation slot to its supplied occurrence identity.
  occurrence-at : (b : Binding) → N.Slots (loop b) → Occurrence
  occurrence-at b (inl _) = Binding.occurrence-AB b
  occurrence-at b (inr (inl _)) = Binding.occurrence-BC b
  occurrence-at b (inr (inr (inl _))) = Binding.occurrence-CA b
  occurrence-at b (inr (inr (inr ())))

  -- This wrapper retains the supplied binding as well as the compiled route.
  record BoundRun : Type (ℓ-suc ℓ) where
    constructor bound-run
    field
      binding : Binding
      input : El (H.Presentation.expression (Binding.A binding))

    compilation : N.Retained
    compilation = N.retain-compilation (loop binding) input

    occurrence-history : List Occurrence
    occurrence-history = occurrences binding

  run : (b : Binding) → El (H.Presentation.expression (Binding.A b)) → BoundRun
  run = bound-run

  retains-binding : (b : Binding) (x : El (H.Presentation.expression (Binding.A b)))
    → BoundRun.binding (run b x) ≡ b
  retains-binding b x = refl

  retains-route : (b : Binding) (x : El (H.Presentation.expression (Binding.A b)))
    → N.Retained.route (BoundRun.compilation (run b x)) ≡ loop b
  retains-route b x = refl

  retains-occurrences : (b : Binding) (x : El (H.Presentation.expression (Binding.A b)))
    → BoundRun.occurrence-history (run b x) ≡ occurrences b
  retains-occurrences b x = refl

  -- Coordinate coherence already forces the closed route to have identity
  -- effect. This is not a theorem about arbitrary edge transport or holonomy.
  closed-effect : (b : Binding) (x : El (H.Presentation.expression (Binding.A b)))
    → N.execute (loop b) x ≡ x
  closed-effect b x = N.effects-agree (loop b) H.stop x
