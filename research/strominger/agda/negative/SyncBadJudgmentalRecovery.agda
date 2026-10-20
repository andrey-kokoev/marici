{-# OPTIONS --safe --cubical --guardedness #-}
module SyncBadJudgmentalRecovery where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import SynchronizedContinuationAdapter
bad : (r : Example.Request) → invEq (Example.S.P.synchronized-source Example.S.z) (fst r) ≡ r
bad r = refl
