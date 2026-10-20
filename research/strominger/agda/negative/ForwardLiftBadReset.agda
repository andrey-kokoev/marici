{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardLiftBadReset where
open import Cubical.Foundations.Prelude
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using (A; B; Seeds; pointQ; root)
import RetainedFeedbackCovariance as R
open Resolution.Generators ℓ-zero
bad : (d : Resolve Seeds (pointQ A)) → R.moveInitial A d ≡ root B
bad d = refl
