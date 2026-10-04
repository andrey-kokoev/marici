{-# OPTIONS --safe --cubical --guardedness #-}
module FourChannelBadRecovery where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (true; _or_)
import RetainedComparisonStructure as R
open import FourChannelBridge
-- Same channels do not make their two source compositions equal.
bad : R.xor true true ≡ true or true
bad = refl
