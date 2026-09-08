{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidQFillingAttachment where

open import Cubical.Foundations.Prelude

-- Homotopy classes of fillings and their lower-support attachment. This record
-- isolates the computed rigidity statement from any physical framing claim.
record QFillingAttachmentCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    FineWeight : Type ℓ
    zeroWeight certificateWeight : FineWeight
    -- Rigidity below is local to certificateWeight; it is not quantified over
    -- every Rees/normal degree.
    Qone Qtwo Qthree BoundaryOne : Type ℓ
    dQ21 : Qtwo → Qone
    dQ32 : Qthree → Qtwo
    zeroQone : Qone
    fixedRoof : Qone

    Filling : Type ℓ
    fillingChain : Filling → Qtwo
    fillsFixedRoof : (h : Filling) → dQ21 (fillingChain h) ≡ fixedRoof
    morseFilling : Filling

    VariationClass AttachmentClass : Type ℓ
    zeroVariation : VariationClass
    zeroAttachment : AttachmentClass
    addVariation : VariationClass → VariationClass → VariationClass
    fillingDifference : Filling → Filling → VariationClass
    lowerAttachment : VariationClass → AttachmentClass

    zeta03 zeta14 zeta25 : Qtwo
    zeta03Class zeta14Class zeta25Class : VariationClass
    zeta03Closed : dQ21 zeta03 ≡ zeroQone
    zeta14Closed : dQ21 zeta14 ≡ zeroQone
    zeta25Closed : dQ21 zeta25 ≡ zeroQone

    -- Rank-two presentation: three generators modulo their diagonal relation.
    diagonalRelation :
      addVariation zeta03Class
        (addVariation zeta14Class zeta25Class) ≡ zeroVariation
    Coordinate : Type ℓ
    zeroCoordinate : Coordinate
    coordinates : VariationClass → Coordinate → Coordinate → Type ℓ
    zeroCoordinatesDetectZero : (v : VariationClass) →
      coordinates v zeroCoordinate zeroCoordinate → v ≡ zeroVariation

    beta03 beta14 beta25 : BoundaryOne
    attachmentRepresentative : BoundaryOne → AttachmentClass
    attachment03 : lowerAttachment zeta03Class ≡ attachmentRepresentative beta03
    attachment14 : lowerAttachment zeta14Class ≡ attachmentRepresentative beta14
    attachment25 : lowerAttachment zeta25Class ≡ attachmentRepresentative beta25

    -- Injectivity of the actual short-boundary connecting map.
    attachmentRigid : (v : VariationClass) →
      lowerAttachment v ≡ zeroAttachment → v ≡ zeroVariation

    -- Seven-triangle Morse and eight-triangle reduction fillers are compared
    -- by an actual six-tetrahedron chain in the same Q complex.
    sevenTriangleFilling eightTriangleFilling : Qtwo
    sixTetrahedronComparison : Qthree
    differenceQtwo : Qtwo → Qtwo → Qtwo
    sevenIsMorse : sevenTriangleFilling ≡ fillingChain morseFilling
    sameBoundarySeven : dQ21 sevenTriangleFilling ≡ fixedRoof
    sameBoundaryEight : dQ21 eightTriangleFilling ≡ fixedRoof
    comparisonBoundary : dQ32 sixTetrahedronComparison ≡
      differenceQtwo sevenTriangleFilling eightTriangleFilling

open QFillingAttachmentCertificate public

preservingAttachmentForcesTrivialVariation : {ℓ : Level}
  (C : QFillingAttachmentCertificate {ℓ}) (v : VariationClass C) →
  lowerAttachment C v ≡ zeroAttachment C → v ≡ zeroVariation C
preservingAttachmentForcesTrivialVariation C = attachmentRigid C

sameAttachmentForcesSameFillingClass : {ℓ : Level}
  (C : QFillingAttachmentCertificate {ℓ}) (h : Filling C) →
  lowerAttachment C (fillingDifference C h (morseFilling C))
    ≡ zeroAttachment C →
  fillingDifference C h (morseFilling C) ≡ zeroVariation C
sameAttachmentForcesSameFillingClass C h =
  attachmentRigid C (fillingDifference C h (morseFilling C))

-- No field identifies VariationClass with a conductor class or promotes an
-- ordinary same-complex comparison to a framed physical homotopy.
