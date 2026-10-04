{-# OPTIONS --safe --cubical --guardedness #-}
module ApplicationExtensionBadArgument where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (false; true)
open import Cubical.Data.Sum.Base using (inr)
open import ApplicationExtensionRegression
import NativeApplicationGate as Gate
-- Both premise ports are mandatory and typed. A second function certificate
-- cannot replace the argument certificate.
bad : R.New.Resolve Gate.retained-answer
bad = R.New.apply (inr application)
  (λ { (lift false) → R.New.seed Gate.function-seed
     ; (lift true) → R.New.seed Gate.function-seed })
