{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverPolicyReconstruction where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Isomorphism
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.HITs.PropositionalTruncation.Base using (∥_∥₁; ∣_∣₁; squash₁)
import Cubical.HITs.PropositionalTruncation.Properties as Trunc
import ResolutionNetDependentMachine as M
import ObserverExecutionBridge as B
import ObserverMachineElimination as Elimination

import ObserverFaithfulRecovery as Recovery
module Faithful = Recovery.Faithful

-- A scoped actual-machine proof, not an assumption of determinism.
module Fixture where
  History = B.Run M.supplied B.finished

  finished-unique : (r : B.Run B.finished B.finished) → r ≡ B.stop
  finished-unique = Elimination.terminal-unique Elimination.no-finished-step

  middle-unique : (r : B.Run B.middle B.finished)
    → r ≡ B.next M.second-step B.stop
  middle-unique = Elimination.peel M.second-step B.stop finished-unique Elimination.middle-not-finished

  history-unique : (r : History) → r ≡ B.execution
  history-unique = Elimination.peel M.first-step (B.next M.second-step B.stop)
    middle-unique Elimination.supplied-not-finished

  history-prop : isProp History
  history-prop a b = history-unique a ∙ sym (history-unique b)

  recover : ∥ History ∥₁ → History
  recover = Faithful.reconstruct history-prop

  faithful : (run : History) → recover ∣ run ∣₁ ≡ run
  faithful run = refl

  admissibility-equiv-history : ∥ History ∥₁ ≃ History
  admissibility-equiv-history = Faithful.equivalence history-prop

-- Mere inhabitation can permit choosing SOME witness without permitting
-- a faithful inverse to forgetting which witness was actually supplied.
module Nonunique where
  choose-some : ∥ Bool ∥₁ → Bool
  choose-some _ = true

  no-faithful-recovery : (recover : ∥ Bool ∥₁ → Bool)
    → ((b : Bool) → recover ∣ b ∣₁ ≡ b) → ⊥
  no-faithful-recovery recover exact = true≢false (Faithful.necessary recover exact true false)
