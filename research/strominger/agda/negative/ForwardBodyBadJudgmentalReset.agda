{-# OPTIONS --safe --cubical --guardedness #-}
module ForwardBodyBadJudgmentalReset where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; Seeds; pointQ)
open import GeneratedReaderClassification using (start)
import ForwardForwardBodyBinding as Binding
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero
module Test (d : Resolve Seeds (pointQ A)) where
  module T = Binding.Diagram d
  bad : T.a2 ≡ start A d
  bad = refl
