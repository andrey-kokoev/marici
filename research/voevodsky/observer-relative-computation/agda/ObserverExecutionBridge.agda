{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverExecutionBridge where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (Σ; _,_)
open import Cubical.Data.Bool.Base using (Bool; false)
open import Cubical.Data.Nat.Base using (zero; suc)
open import Cubical.Data.Unit.Base using (Unit; tt)
open import Cubical.Data.Empty.Base using (⊥)
import ResolutionNetDependentMachine as M
import ResolutionNetObservation as O

Closed = M.Config ⊥
Meaning = Σ Bool M.Family

empty-environment : ⊥ → Bool
empty-environment ()

-- Explicit directed operational histories, before taking observation.
data Run : Closed → Closed → Type where
  stop : {c : Closed} → Run c c
  next : {c d e : Closed} → M.Step c d → Run d e → Run c e

-- A static support generated FROM the operational data. Generator
-- labels retain their source steps; paths can be traversed both ways.
-- This is not a derivation of the machine rules from observer positivity.
data Support : Type where
  at : Closed → Support
  comparison : {c d : Closed} → M.Step c d → at c ≡ at d

realize : {c d : Closed} → Run c d → at c ≡ at d
realize stop = refl
realize (next step rest) = comparison step ∙ realize rest

value : Support → Meaning
value (at c) = M.observe c empty-environment
value (comparison step i) = M.step-sound step empty-environment i

run-sound : {c d : Closed} (run : Run c d)
  → M.observe c empty-environment ≡ M.observe d empty-environment
run-sound run = cong value (realize run)

-- Instantiate the earlier observer interface, not only an analogy.
module Observation = O.Observation Support (λ _ → Meaning)
global-observation : Observation.Observe (λ s → s)
global-observation = value

point-probe : Closed → Unit → Support
point-probe c _ = at c

local-readout : (c : Closed) → Observation.Observe (point-probe c)
local-readout c = Observation.restrict {p = λ s → s} (point-probe c) global-observation

positive-support : Unit
positive-support = tt

middle finished : Closed
middle = M.lit false , M.choose (M.lit false) (suc zero)
finished = M.lit false , M.number (suc zero)

execution : Run M.supplied finished
execution = next M.first-step (next M.second-step stop)

observed-connection : at M.supplied ≡ at finished
observed-connection = realize execution

same-observed-value : local-readout M.supplied tt ≡ local-readout finished tt
same-observed-value = run-sound execution

-- Reversing a comparison path is allowed; reversing the machine run
-- is not. The final number has no outgoing operational Step.
reverse-connection : at finished ≡ at M.supplied
reverse-connection = sym observed-connection

no-reverse-execution : Run finished M.supplied → ⊥
no-reverse-execution (next () rest)

-- Hence the observational path carrier does not reconstruct all
-- directed histories, even though actual histories map into it.
no-universal-run-readback :
  ((c d : Closed) → at c ≡ at d → Run c d) → ⊥
no-universal-run-readback readback =
  no-reverse-execution (readback finished M.supplied reverse-connection)
