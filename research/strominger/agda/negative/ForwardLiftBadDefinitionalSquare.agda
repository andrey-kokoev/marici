{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardLiftBadDefinitionalSquare where
open import Cubical.Foundations.Prelude
import WholePackageResolution as Resolution
open import NativeExtensionFamilyAudit using (A; B; Seeds; pointQ)
import RetainedFeedbackCovariance as R
open Resolution.Generators ℓ-zero
bad : (d : Resolve Seeds (pointQ A)) → R.moveInitial B (R.moveInitial A d) ≡ d
bad d = refl
