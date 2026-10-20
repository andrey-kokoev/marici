{-# OPTIONS --safe --cubical --guardedness #-}
module FeedbackBadEdgeTransport where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; B; AB)
open import RetainedPackageFeedback using (base; Total; step)
open import RetainedFeedbackCovariance using (move)

-- Moving the whole package while leaving its extension edge unmoved breaks
-- the typed boundary: AB is not outgoing from the transported B endpoint.
bad : Total
bad = step (move (A , base)) (B , AB)
