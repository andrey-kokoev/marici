{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidDihedralAttachment where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Fine-degree-zero, linear homology-class attachment certificate. It is
-- deliberately not reusable for Rees-resonance or nonlinear geometric lanes.
record DihedralAttachmentCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    FineWeight : Type ℓ
    zeroWeight certificateWeight : FineWeight
    isFineDegreeZero : certificateWeight ≡ zeroWeight

    Group Stabilizer U V W : Type ℓ
    zeroU : U
    addV : V → V → V
    attachment : U → V
    fullProjection : V → W
    attachmentRetraction : V → U
    projectionSection : W → V

    -- Split exactness LA=1, PX=1, AL+XP=1.
    retractsAttachment : (u : U) →
      attachmentRetraction (attachment u) ≡ u
    sectionsProjection : (w : W) →
      fullProjection (projectionSection w) ≡ w
    splitIdentity : (v : V) →
      addV (attachment (attachmentRetraction v))
        (projectionSection (fullProjection v)) ≡ v

    actU : Stabilizer → U → U
    actV : Stabilizer → V → V
    actW : Stabilizer → W → W
    attachmentEquivariant : (g : Stabilizer) (u : U) →
      actV g (attachment u) ≡ attachment (actU g u)
    projectionEquivariant : (g : Stabilizer) (v : V) →
      actW g (fullProjection v) ≡ fullProjection (actV g v)
    retractionEquivariant : (g : Stabilizer) (v : V) →
      attachmentRetraction (actV g v) ≡ actU g (attachmentRetraction v)
    sectionEquivariant : (g : Stabilizer) (w : W) →
      actV g (projectionSection w) ≡ projectionSection (actW g w)

    -- The full symmetry acts on the transported three-label orbit, not on one
    -- occurrence-labelled packet with a falsely fixed rotation.
    OccurrenceLabel OrbitU OrbitV OrbitW : Type ℓ
    distinguishedLabel : OccurrenceLabel
    transportLabel : Group → OccurrenceLabel → OccurrenceLabel
    induceU : OccurrenceLabel → U → OrbitU
    induceV : OccurrenceLabel → V → OrbitV
    induceW : OccurrenceLabel → W → OrbitW
    OrbitIsRegularModule : OrbitU → Type ℓ
    regularOrbitWitness : (label : OccurrenceLabel) (u : U) →
      OrbitIsRegularModule (induceU label u)

    -- Group-cohomology obstruction type for each positive degree. The external
    -- certificate proves it empty for the regular filling orbit.
    PositiveDegree : Type ℓ
    FillingObstruction : PositiveDegree → Type ℓ
    noPositiveFillingObstruction : (n : PositiveDegree) →
      FillingObstruction n → ⊥

open DihedralAttachmentCertificate public

attachmentRigidByEquivariantSplitting : {ℓ : Level}
  (C : DihedralAttachmentCertificate {ℓ}) (u : U C) →
  attachment C u ≡ attachment C (zeroU C) → u ≡ zeroU C
attachmentRigidByEquivariantSplitting C u same =
  sym
    (sym (retractsAttachment C (zeroU C))
    ∙ cong (attachmentRetraction C) (sym same)
    ∙ retractsAttachment C u)

positiveDegreeFillingObstructionImpossible : {ℓ : Level}
  (C : DihedralAttachmentCertificate {ℓ}) (n : PositiveDegree C) →
  FillingObstruction C n → ⊥
positiveDegreeFillingObstructionImpossible C =
  noPositiveFillingObstruction C

-- Scope exclusions: no action on a single packet by the full group, no claim
-- about nonzero Rees weights, and no chain-level or geometric lift constructor.
