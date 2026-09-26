{-# OPTIONS --safe --cubical --guardedness #-}
module ObserverOrientationPolicy where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Sigma.Base using (Σ; _,_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Bool.Properties using (true≢false)
open import Cubical.Data.Empty.Base using (⊥)
import ResolutionNetDependentMachine as M
import ObserverExecutionBridge as Bridge
import ObserverDirectionRecords as Records

-- Polarity is additional data. Neither constructor is called time.
data Policy : Type where
  forward backward : Policy

Admissible : Policy → Bridge.Closed → Bridge.Closed → Type
Admissible forward c d = Bridge.Run c d
Admissible backward c d = Bridge.Run d c

connection : (policy : Policy) {c d : Bridge.Closed}
  → Admissible policy c d → Bridge.at c ≡ Bridge.at d
connection forward run = Bridge.realize run
connection backward run = sym (Bridge.realize run)

sound : (policy : Policy) {c d : Bridge.Closed} (run : Admissible policy c d)
  → Bridge.value (Bridge.at c) ≡ Bridge.value (Bridge.at d)
sound policy run = cong Bridge.value (connection policy run)

-- Value observation is the SAME map for both admissibility policies.
value-observer : Policy → Bridge.Support → Bridge.Meaning
value-observer _ = Bridge.value

same-observer : value-observer forward ≡ value-observer backward
same-observer = refl

policy-bit : Policy → Bool
policy-bit forward = true
policy-bit backward = false

-- A convention may choose a policy; the common value map cannot
-- reconstruct BOTH possible supplied policies correctly.
no-policy-recovery : (recover : (Bridge.Support → Bridge.Meaning) → Policy)
  → ((policy : Policy) → recover (value-observer policy) ≡ policy) → ⊥
no-policy-recovery recover exact = true≢false
  (cong policy-bit (sym (exact forward) ∙ exact backward))

forward-example : Admissible forward M.supplied Bridge.finished
forward-example = Bridge.execution

backward-example : Admissible backward Bridge.finished M.supplied
backward-example = Bridge.execution

not-backward-at-forward-endpoints : Admissible backward M.supplied Bridge.finished → ⊥
not-backward-at-forward-endpoints = Bridge.no-reverse-execution

not-forward-at-backward-endpoints : Admissible forward Bridge.finished M.supplied → ⊥
not-forward-at-backward-endpoints = Bridge.no-reverse-execution

-- Recording the policy-admissible history and its actual comparison
-- preserves full operational evidence. This uses the previous general
-- lossless-record construction, not a new inverse to arbitrary paths.
module Retained (policy : Policy) (c d : Bridge.Closed) where
  module R = Records.Records (connection policy {c} {d})
  View = R.Recorded

  equivalence : Admissible policy c d ≃ View
  equivalence = R.lossless

  remember : Admissible policy c d → View
  remember = R.retain

  recover : View → Admissible policy c d
  recover = R.recover

  history-roundtrip : (run : Admissible policy c d) → recover (remember run) ≡ run
  history-roundtrip = R.source-roundtrip

  view-roundtrip : (view : View) → remember (recover view) ≡ view
  view-roundtrip = R.record-roundtrip
