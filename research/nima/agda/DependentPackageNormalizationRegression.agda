{-# OPTIONS --safe --cubical --guardedness #-}
module DependentPackageNormalizationRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.FinData.Base using (Fin) renaming (zero to fzero)
open import Cubical.Data.Unit.Base using (Unit; tt*)
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Bool.Properties using (true≢false; false≢true)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import DependentPackageNormalization as Normal
import DependentNormalizationCoherence as Coherence
import DependentArbitraryIndexRoutes
import IndexIdentityCoherence as Indexed
import IndexIdentityCoherenceRegression as Loop

open Whole.Universe ℓ-zero
module N = Normal.Normalization ℓ-zero
module IX = Indexed.Indexed ℓ-zero

-- Infinitely many indices, with genuinely varying finite index fibres.
infinite-dependent : Code
infinite-dependent = Pi ℕ (λ n → E (Fin (suc n)) (λ j → atom (j ≡ j)))

infinite-value : El infinite-dependent
infinite-value n = fzero , refl

infinite-roundtrip : N.reconstruct infinite-dependent
  (N.normalize infinite-dependent infinite-value) ≡ infinite-value
infinite-roundtrip = N.source-roundtrip infinite-dependent infinite-value

infinite-second-roundtrip :
  N.reconstruct (N.reexpress (N.normal infinite-dependent))
    (N.normalize-again infinite-dependent (N.normalize infinite-dependent infinite-value))
  ≡ N.normalize infinite-dependent infinite-value
infinite-second-roundtrip = N.second-roundtrip infinite-dependent _

empty-sum empty-product : Code
empty-sum = E ⊥ (λ _ → atom Unit)
empty-product = Pi ⊥ (λ _ → atom ⊥)

normal-empty-sum : N.Value (N.normal empty-sum) → ⊥
normal-empty-sum v = fst (N.reconstruct empty-sum v)

normal-empty-product : N.Value (N.normal empty-product)
normal-empty-product = N.normalize empty-product (λ ())

-- Normalization is faithful on nontrivial index paths, not just on values.
index-path-equiv = N.path-equiv Loop.index-code Loop.base-index Loop.base-index

normal-loop-nontrivial :
  cong (N.normalize Loop.index-code) Loop.index-loop ≡ refl → ⊥
normal-loop-nontrivial p = Loop.loop-is-not-reflexive
  (sym (retEq index-path-equiv Loop.index-loop)
   ∙ cong (invEq index-path-equiv) p ∙ retEq index-path-equiv refl)

cover-sections : Code
cover-sections = Pi (IX.Index Loop.F) (IX.fibre Loop.F)

normalization-does-not-invent-section : N.Value (N.normal cover-sections) → ⊥
normalization-does-not-invent-section v = Loop.no-section (N.reconstruct cover-sections v)

module H = Coherence.Coherence ℓ-zero infinite-dependent

short-route long-route : H.Route H.original H.normal
short-route = H.next {R = H.normal} H.normalize-map H.stop
long-route = H.next {R = H.normal} H.normalize-map
  (H.next {R = H.original} H.reconstruct-map
    (H.next {R = H.normal} H.normalize-map H.stop))

order-comparison : H.evaluate short-route ≡ H.evaluate long-route
order-comparison = H.route-comparison short-route long-route

one-step : {P R : H.Presentation} → H.Route P R → Bool
one-step (H.next _ H.stop) = true
one-step _ = false

raw-routes-retained : short-route ≡ long-route → ⊥
raw-routes-retained p = true≢false (cong one-step p)

next-Q : Whole.Universe.Complete (ℓ-suc ℓ-zero)
next-Q = H.reify-certificate (H.certify short-route long-route)

-- The shared-coordinate hypothesis has content: negation is an equivalence
-- of Bool but cannot be a map over identity normalization coordinates.
BoolCode : Code
BoolCode = atom Bool

negation-does-not-preserve-coordinates :
  ((b : Bool) → N.normalize BoolCode (not b) ≡ N.normalize BoolCode b) → ⊥
negation-does-not-preserve-coordinates preserves =
  false≢true (cong (λ v → snd v tt*) (preserves true))
