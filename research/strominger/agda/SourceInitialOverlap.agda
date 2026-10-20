{-# OPTIONS --safe --cubical --guardedness #-}
module SourceInitialOverlap where

open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (A; B; C; D; Seeds)
import WholePackageResolution as Resolution
open Resolution.Generators ℓ-zero
import ForwardSourceLiftComposition as F
import RetainedFeedbackCovariance as R
import SourceInverseSquareCoherence as Base
import TransportCancellationCoherence as T

-- Bind the generic theorem to the OLD cancellation and inverse witnesses.
-- Abstract boundaries prevent normalization of their large implementations
-- when these theorems are subsequently used; no witness is replaced.
abstract
  initial-A : Base.InitialOverlapA
  initial-A = T.paired-with-coherence (Resolve Seeds) (R.pointPath A) (R.pointPath B)
    (F.pointed-inverse B A refl refl) (F.pointed-inverse A B refl refl)
    (Base.pointed-inverse-coherent B A refl refl)
  initial-B : Base.InitialOverlapB
  initial-B = T.paired-with-coherence (Resolve Seeds) (R.pointPath B) (R.pointPath A)
    (F.pointed-inverse A B refl refl) (F.pointed-inverse B A refl refl)
    (Base.pointed-inverse-coherent A B refl refl)
  initial-C : Base.InitialOverlapC
  initial-C = T.paired-with-coherence (Resolve Seeds) (R.pointPath C) (R.pointPath D)
    (F.pointed-inverse D C refl refl) (F.pointed-inverse C D refl refl)
    (Base.pointed-inverse-coherent D C refl refl)
  initial-D : Base.InitialOverlapD
  initial-D = T.paired-with-coherence (Resolve Seeds) (R.pointPath D) (R.pointPath C)
    (F.pointed-inverse C D refl refl) (F.pointed-inverse D C refl refl)
    (Base.pointed-inverse-coherent C D refl refl)

triangle-boundary : (ℓ : Level) → Base.TransportCancellationTriangle ℓ
triangle-boundary ℓ = T.transport-cancellation-triangle
