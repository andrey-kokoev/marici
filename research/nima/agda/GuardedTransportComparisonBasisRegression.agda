{-# OPTIONS --safe --cubical --guardedness #-}
module GuardedTransportComparisonBasisRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not)
open import Cubical.Data.Bool.Properties using (false≢true)
open import Cubical.Data.Unit.Base using (tt*)
open import Cubical.Data.Empty.Base using (⊥)
import WholePackageSigmaPi as Whole
import GuardedTransportComparisonBasis as Basis

-- Symbolic retention checks apply to arbitrary dependent source types and
-- routes, without eagerly expanding their concrete normalization proofs.
module Retention (ℓ : Level) (Q : Whole.Universe.Code ℓ) where
  module G = Basis.Basis ℓ Q
  open Whole.Universe ℓ
  open G.H.Presentation

  module Given (P R : G.H.Presentation) (a b : G.H.Route P R)
    (x : El (expression P)) (p : G.Semantic a b) where

    result : Whole.Universe.Complete (ℓ-suc ℓ)
    result = G.next-Q (G.realize a b x p)

    input-retained : G.Requested.input-value (Whole.Universe.value result) ≡ x
    input-retained = refl
    witness-retained : G.Requested.witness (Whole.Universe.value result) ≡ p
    witness-retained = refl
    first-native-retained : G.Requested.first-native (Whole.Universe.value result)
      ≡ G.C.source-compile a x
    first-native-retained = refl
    second-native-retained : G.Requested.second-native (Whole.Universe.value result)
      ≡ G.C.source-compile b x
    second-native-retained = refl

open Whole.Universe ℓ-zero
module G = Basis.Basis ℓ-zero (atom Bool)
P = G.H.original

empty-route one two : G.H.Route P P
empty-route = G.H.stop
one = G.H.next {P} {P} {P} (G.H.identity P) G.H.stop
two = G.H.next {P} {P} {P} (G.H.identity P) one

abstract
  requested-witness : G.Semantic empty-route two
  requested-witness = G.H.compare-maps {P} {P} (G.observe empty-route) (G.observe two)

reconstructed : Σ[ c ∈ G.Generated empty-route two ] (G.sound c ≡ requested-witness)
reconstructed = G.completeness empty-route two requested-witness

-- Different retained packets, not an assumed common native endpoint.
remembered-code : Code → Bool
remembered-code (retain _ _ _) = true
remembered-code _ = false

initial = G.C.start P true
empty-packet = G.C.packet (G.C.run empty-route initial)
one-packet = G.C.packet (G.C.run one initial)

packets-distinct : empty-packet ≡ one-packet → ⊥
packets-distinct p = false≢true (cong (λ q → remembered-code (expression q)) p)

empty-one-comparison : G.Generated empty-route one
empty-one-comparison = G.compare empty-route one

-- An unrestricted negating transport cannot acquire the shared-coordinate
-- guard required by the compiled-route comparison calculus.
negation-guard-impossible : (f : G.H.CoherentMap P P)
  → ((b : Bool) → fst (f b) ≡ not b) → ⊥
negation-guard-impossible f changes = false≢true
  (sym (changes true) ∙ cong (λ v → snd v tt*) (snd (f true)))
