{-# OPTIONS --safe --cubical --guardedness #-}
module WitnessGeneratorExamples where
open import Cubical.Foundations.Prelude
open import NativeExtensionFamilyAudit using (Vertex; A; Seeds)
open import InternalSourceComparisons using (package; act; exchange)
open import WitnessContinuationHistories
open import WitnessHigherControls
open import WitnessHigherAdmissionObstruction
import WitnessNativeEnvelope
import WholePackageResolution as R
open R.Generators ℓ-zero
-- Quantified checks, not a finite list of instances.
allHistories : {v : Vertex} (h : History A v)
  → Resolve Seeds (package (witness (squareState h chosen)))
allHistories = chosen-universal
reuse : {v t : Vertex} (h : History A v) (k : History (act exchange v) t)
  → Resolve Seeds (package (witness (squareState k (squareState h chosen))))
reuse h k = recursively-reusable h chosen k
higher = chosen-direct-staged
nativeHigherPath = chosen-direct-staged-native
obstruction = no-higher-package-admission
