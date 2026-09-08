{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidOrbitSupportedQ where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record OrbitSupportedQCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Coeff AbsoluteTarget PCTarget GenericQ BoundaryPC : Type ℓ
    zeroAbsolute : AbsoluteTarget
    pcZero : PCTarget
    qZero : GenericQ

    OldDefect NewDefect PCLinearityExtension : Type ℓ
    oldDefect : OldDefect
    transformedOldDefect : OldDefect → PCTarget
    transformedOldDefectPrimitive : OldDefect → PCTarget
    differentialPC : PCTarget → PCTarget
    oldDefectBecomesBoundary : (d : OldDefect) →
      differentialPC (transformedOldDefectPrimitive d) ≡
      transformedOldDefect d

    newDefect : NewDefect
    newExtension : PCLinearityExtension
    zeroExtension : PCLinearityExtension
    recomputedExtensionNonzero : newExtension ≡ zeroExtension → ⊥

    AbsoluteLiftCoefficient PCLiftCoefficient : Type ℓ
    zeroAbsoluteLift : AbsoluteLiftCoefficient
    zeroPCLift : PCLiftCoefficient
    absoluteGenericImageIsZero : (k : AbsoluteLiftCoefficient) →
      k ≡ zeroAbsoluteLift
    pcLiftingIdeal : PCLiftCoefficient → Type ℓ
    pcUnit : PCLiftCoefficient
    pcUnitDoesNotLiftAfterOnePair : pcLiftingIdeal pcUnit → ⊥

    PairLabel OrderedPair : Type ℓ
    pair03 pair25 pair14 : OrderedPair
    pairsAreDisjoint : Type ℓ
    disjointWitness : pairsAreDisjoint
    PairPurityOperation : OrderedPair → Type ℓ
    pairOperation : (p : OrderedPair) → PairPurityOperation p

    OrbitTarget OrbitLine Shift : Type ℓ
    orbitTarget : OrbitTarget
    orbitLine : OrbitLine
    codimensionSixShift : Shift
    compositeSupportedDual :
      PairPurityOperation pair03 →
      PairPurityOperation pair25 →
      PairPurityOperation pair14 → OrbitTarget
    compositeDefinition :
      compositeSupportedDual (pairOperation pair03)
        (pairOperation pair25) (pairOperation pair14) ≡ orbitTarget

    orbitDifferential : OrbitTarget → OrbitTarget
    qDifferential : GenericQ → GenericQ
    includeQ : GenericQ → OrbitTarget
    projectQ : OrbitTarget → GenericQ
    qSection : (q : GenericQ) → projectQ (includeQ q) ≡ q
    qInclusionChainMap : (q : GenericQ) →
      orbitDifferential (includeQ q) ≡ includeQ (qDifferential q)

    genericTheta : GenericQ
    thetaClosed : qDifferential genericTheta ≡ qZero
    liftedThetaClosed : orbitDifferential (includeQ genericTheta) ≡ includeQ qZero
    liftedThetaProjects : projectQ (includeQ genericTheta) ≡ genericTheta

    splitBoundaryInclusion : BoundaryPC → OrbitTarget
    OrbitSplitting : Type ℓ
    orbitSplitting : OrbitSplitting
    codimensionSixPlacementRetained : Type ℓ
    codimensionSixPlacementWitness : codimensionSixPlacementRetained

    -- Permission for the native source to enter the composite target is not
    -- part of the target-side construction. A future mate must supply it.
    NativeSource : Type ℓ
    NativeOrbitAuthorization : NativeSource → OrbitTarget → Type ℓ

strictOrbitQLift : {ℓ : Level} (C : OrbitSupportedQCertificate {ℓ}) →
  OrbitSupportedQCertificate.projectQ C
    (OrbitSupportedQCertificate.includeQ C
      (OrbitSupportedQCertificate.genericTheta C)) ≡
  OrbitSupportedQCertificate.genericTheta C
strictOrbitQLift C = OrbitSupportedQCertificate.liftedThetaProjects C

-- Deliberately no inhabitant of NativeOrbitAuthorization is constructed here.
