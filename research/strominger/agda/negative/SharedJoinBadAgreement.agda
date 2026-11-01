{-# OPTIONS --safe --cubical --guardedness #-}
module SharedJoinBadAgreement where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import NativeSharedReaderJoin
module P = Prepared (λ _ → false)
bad : P.readShared false (N.value (P.channel false)) ≡ record-at true
bad = refl
