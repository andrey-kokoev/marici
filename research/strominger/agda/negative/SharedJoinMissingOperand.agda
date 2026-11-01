{-# OPTIONS --safe --cubical --guardedness #-}
module SharedJoinMissingOperand where
open import Cubical.Data.Bool.Base using (false)
open import NativeSharedReaderJoin
module P = Prepared (λ _ → false)
bad : P.R.Resolve P.J.result
bad = P.J.derive (P.channel-derivation false)
