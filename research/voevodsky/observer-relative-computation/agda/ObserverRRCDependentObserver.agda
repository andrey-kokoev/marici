{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverRRCDependentObserver where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_,_; fst; snd)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Maybe.Base using (just)
import WholePackageSigmaPi as W
import ResolutionNetDependentSubstitution as DSC
import ObserverInternalComparison as O
import IndexIdentityCoherenceRegression as Cover
import IndexIdentityCoherence as Indexed

module U = W.Universe ℓ-zero
module D = DSC.Dependent {ℓ-zero}
module Ix = Indexed.Indexed ℓ-zero

-- A transparent retained path/fibre expression, not atom of an entire
-- observer plus an arbitrary callback. Evaluation uses fixed transport.
emit : O.Total → U.Complete
emit (y , p) = U.pack
  (U.retain (U.paths Cover.index-code O.base y) p (Ix.fibre Cover.F y))
  (subst (Ix.Fibre Cover.F) p true)

path-retained : (q : O.Total) → U.recover (U.expression (emit q))
  ≡ just (U.path-package Cover.index-code O.base (fst q) (snd q))
path-retained q = refl

reading-retained : (q : O.Total) → U.value (emit q) ≡ O.dependent-read q
reading-retained q = refl

-- Actual dependent DSC execution: the output type varies with the reply.
execute : {Γ : Type} (reply : Γ → O.Reply)
  → ((γ : Γ) → O.base ≡ reply γ) → (γ : Γ) → Ix.Fibre Cover.F (reply γ)
execute = D.execute (λ q → Ix.Fibre Cover.F (fst q)) O.dependent-read

execution-agrees : {Γ : Type} (reply : Γ → O.Reply)
  (comparison : (γ : Γ) → O.base ≡ reply γ) (γ : Γ)
  → execute reply comparison γ ≡ U.value (emit (reply γ , comparison γ))
execution-agrees reply comparison γ = refl

execution-substitution : {Γ Δ : Type} (reply : Γ → O.Reply)
  (comparison : (γ : Γ) → O.base ≡ reply γ) (σ : Δ → Γ)
  → execute (D.compose reply σ) (λ δ → comparison (σ δ))
    ≡ (λ δ → execute reply comparison (σ δ))
execution-substitution reply comparison σ = refl

stationary-reading : U.value (emit (O.forget-fixed O.stationary)) ≡ true
stationary-reading = O.stationary-read

turn-reading : U.value (emit (O.forget-fixed O.turn)) ≡ false
turn-reading = O.turn-read

fixed-paths-distinct : O.interpret O.turn ≡ O.interpret O.stationary → ⊥
fixed-paths-distinct = O.fixed-witnesses-distinct

-- Allowing the reply to move also transports the fibre and retained code.
-- This equality is compatible with the FIXED-boundary distinction above.
moving-packages-equal : emit (O.forget-fixed O.stationary) ≡ emit (O.forget-fixed O.turn)
moving-packages-equal = cong emit O.same-total-certificate

moving-reading : PathP
  (λ i → U.El (U.expression (moving-packages-equal i)))
  (U.value (emit (O.forget-fixed O.stationary)))
  (U.value (emit (O.forget-fixed O.turn)))
moving-reading i = U.value (moving-packages-equal i)

no-constant-package-reader : (read : U.Complete → Bool)
  → read (emit (O.forget-fixed O.stationary)) ≡ true
  → read (emit (O.forget-fixed O.turn)) ≡ false → ⊥
no-constant-package-reader read stationary turn = true≢false
  (sym stationary ∙ cong read moving-packages-equal ∙ turn)

-- This module proves a retained package/DSC interface, not a new native
-- RRC Resolve transport rule or synthesis of arbitrary index paths.
