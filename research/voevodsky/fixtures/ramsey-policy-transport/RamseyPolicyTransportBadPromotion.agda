{-# OPTIONS --safe --cubical --guardedness #-}
module RamseyPolicyTransportBadPromotion where
import RamseyExternalSeedPolicyExamples as Policy
open import RamseyPolicyTransportExamples
bad : Policy.Base.Good target-leaf
bad = target-leaf-good
