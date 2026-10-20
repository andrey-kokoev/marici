{-# OPTIONS --safe --cubical --guardedness #-}
module FeedbackBadAttachment where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (D; CA)
open import RetainedPackageFeedback using (Chain; extend; base)

-- An admitted previous package does not admit an edge at the wrong boundary.
bad : Chain D
bad = extend base (D , CA)
