{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverMachineTransportRegression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.HITs.PropositionalTruncation.Base using (∣_∣₁)
import ObserverExecutionBridge as B
import ObserverPolicyReconstruction as R

length : {c d : B.Closed} → B.Run c d → ℕ
length B.stop = zero
length (B.next step rest) = suc (length rest)

moved : R.Fixture.History
moved = transport (λ _ → R.Fixture.History) B.execution

-- Definitional tests: no transportRefl rewrite is used.
transported-length : length moved ≡ suc (suc zero)
transported-length = refl

recovered-length : length (R.Fixture.recover ∣ moved ∣₁) ≡ suc (suc zero)
recovered-length = refl

-- The original indexed Run and endpoint uniqueness statement survive.
transported-unique : moved ≡ B.execution
transported-unique = R.Fixture.history-unique moved
