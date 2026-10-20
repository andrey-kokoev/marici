{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardLiftBadReadyIdentity where
open import Cubical.Foundations.Prelude
open import RetainedPackageFeedback using (Ready)
import RetainedFeedbackCovariance as R
import ForwardSourceLiftComposition as F
bad : (r : Ready) → R.moveReady (R.moveReady r) ≡ r
bad = F.ready-forward-square
