{-# OPTIONS --safe --cubical --guardedness #-}
module ModeBadExchangeIdentity where
open import Cubical.Foundations.Prelude
open import RetainedPackageFeedback using (Total)
import ForwardSourceLiftComposition as F
import RetainedFeedbackCovariance as R
bad : (c : Total) → R.move c ≡ c
bad c = F.forward-square c
