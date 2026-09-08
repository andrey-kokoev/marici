{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidQSupport where

open import Cubical.Foundations.Prelude hiding (J)
open import Cubical.Data.Empty using (⊥)
open import DGPyramidBoundary
open import DGPyramidAdapter

-- Compact proof boundary for the full finite Q-support calculation. The large
-- matrices stay in the external checker; an importer must supply these maps
-- and equations, not merely the matrix dimensions.
record QSupportCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Vhat Bhat Mhat RV RB RM Qhat : Type ℓ
    includeVB : Vhat → Bhat
    includeBM : Bhat → Mhat
    includeRVRB : RV → RB
    includeRBRM : RB → RM
    forgetRelative : RM → Mhat
    quotientM : Mhat → Qhat
    quotientR : RM → Qhat
    relativeQuotientCommutes : (x : RM) →
      quotientR x ≡ quotientM (forgetRelative x)

    -- Degrees needed by the corrected Morse disk and its selected Q primitive.
    Mtwo Mone Mzero Qtwo Qone Qzero : Type ℓ
    dM21 : Mtwo → Mone
    dM10 : Mone → Mzero
    dQ21 : Qtwo → Qone
    dQ10 : Qone → Qzero
    zeroM : Mzero
    zeroQ : Qzero
    dM² : (x : Mtwo) → dM10 (dM21 x) ≡ zeroM
    dQ² : (x : Qtwo) → dQ10 (dQ21 x) ≡ zeroQ
    projectM2Q2 : Mtwo → Qtwo
    projectM1Q1 : Mone → Qone
    projectM0Q0 : Mzero → Qzero
    projectChain21 : (x : Mtwo) →
      projectM1Q1 (dM21 x) ≡ dQ21 (projectM2Q2 x)
    projectChain10 : (x : Mone) →
      projectM0Q0 (dM10 x) ≡ dQ10 (projectM1Q1 x)

    correctedHM : Mtwo
    correctedQ : Mone
    correctedMorseFace : dM21 correctedHM ≡ correctedQ
    correctedQClosed : dM10 correctedQ ≡ zeroM

    selectedQPrimitive : Qtwo
    selectedQBoundary : dQ21 selectedQPrimitive ≡ projectM1Q1 correctedQ
    selectedPrimitiveIsProjectedMorse :
      selectedQPrimitive ≡ projectM2Q2 correctedHM

    -- The selected primitive is the actual seven-triangle chain, not an
    -- unnamed existence witness. Signs and occurrence coefficients belong in
    -- the seven terms supplied by a concrete packet.
    triangle0 triangle1 triangle2 triangle3 : Qtwo
    triangle4 triangle5 triangle6 : Qtwo
    assembleSevenTriangles :
      Qtwo → Qtwo → Qtwo → Qtwo → Qtwo → Qtwo → Qtwo → Qtwo
    selectedPrimitiveHasSevenTerms : selectedQPrimitive ≡
      assembleSevenTriangles triangle0 triangle1 triangle2 triangle3
        triangle4 triangle5 triangle6

    -- Full selected deformation retract in the three bounded Q degrees.
    ReducedQtwo ReducedQone ReducedQzero : Type ℓ
    dReduced21 : ReducedQtwo → ReducedQone
    dReduced10 : ReducedQone → ReducedQzero
    projectQ2 : Qtwo → ReducedQtwo
    projectQ1 : Qone → ReducedQone
    projectQ0 : Qzero → ReducedQzero
    includeQ2 : ReducedQtwo → Qtwo
    includeQ1 : ReducedQone → Qone
    includeQ0 : ReducedQzero → Qzero
    projectReduced21 : (x : Qtwo) →
      projectQ1 (dQ21 x) ≡ dReduced21 (projectQ2 x)
    projectReduced10 : (x : Qone) →
      projectQ0 (dQ10 x) ≡ dReduced10 (projectQ1 x)
    includeReduced21 : (x : ReducedQtwo) →
      dQ21 (includeQ2 x) ≡ includeQ1 (dReduced21 x)
    includeReduced10 : (x : ReducedQone) →
      dQ10 (includeQ1 x) ≡ includeQ0 (dReduced10 x)
    projectInclude2 : (x : ReducedQtwo) → projectQ2 (includeQ2 x) ≡ x
    projectInclude1 : (x : ReducedQone) → projectQ1 (includeQ1 x) ≡ x
    projectInclude0 : (x : ReducedQzero) → projectQ0 (includeQ0 x) ≡ x

    -- Addition is included only where needed to state dh+hd=1-ip.
    addQtwo : Qtwo → Qtwo → Qtwo
    addQone : Qone → Qone → Qone
    addQzero : Qzero → Qzero → Qzero
    homotopy12 : Qone → Qtwo
    homotopy01 : Qzero → Qone
    contraction2 : (x : Qtwo) →
      addQtwo (homotopy12 (dQ21 x)) (includeQ2 (projectQ2 x)) ≡ x
    contraction1 : (x : Qone) →
      addQone (dQ21 (homotopy12 x))
        (addQone (homotopy01 (dQ10 x)) (includeQ1 (projectQ1 x))) ≡ x
    contraction0 : (x : Qzero) →
      addQzero (dQ10 (homotopy01 x)) (includeQ0 (projectQ0 x)) ≡ x

    -- A unit coordinate and exactness are intentionally simultaneous data.
    Coeff : Type ℓ
    qReadout : Qone → Coeff
    one : Coeff
    correctedRoofHasUnitCoordinate :
      qReadout (projectM1Q1 correctedQ) ≡ one

open QSupportCertificate public

-- The unit coordinate does not obstruct the exhibited primitive.
unitCoordinateWithPrimitive : {ℓ : Level} (C : QSupportCertificate {ℓ}) →
  Σ (Qtwo C) λ K →
    Σ (dQ21 C K ≡ projectM1Q1 C (correctedQ C)) λ _ →
      qReadout C (projectM1Q1 C (correctedQ C)) ≡ one C
unitCoordinateWithPrimitive C =
  selectedQPrimitive C , selectedQBoundary C , correctedRoofHasUnitCoordinate C

-- Certificate for the concrete mixed-triangle defect of a truncated pure-flag
-- projection. No global inequality of functions is needed.
record TruncatedProjectionDefect {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    FullTwo FullOne PureTwo PureOne : Type ℓ
    dFull : FullTwo → FullOne
    dPure : PureTwo → PureOne
    projectTwo : FullTwo → PureTwo
    projectOne : FullOne → PureOne
    zeroPureTwo : PureTwo
    zeroPureOne : PureOne
    dZero : dPure zeroPureTwo ≡ zeroPureOne
    triangle : FullTwo
    d03Edge : PureOne
    triangleDeleted : projectTwo triangle ≡ zeroPureTwo
    boundaryRetainsEdge : projectOne (dFull triangle) ≡ d03Edge
    edgeNonzero : d03Edge ≡ zeroPureOne → ⊥

open TruncatedProjectionDefect public

truncatedProjectionCannotBeChainMap : {ℓ : Level}
  (D : TruncatedProjectionDefect {ℓ}) →
  ((x : FullTwo D) →
    projectOne D (dFull D x) ≡ dPure D (projectTwo D x)) → ⊥
truncatedProjectionCannotBeChainMap D chainMap =
  edgeNonzero D
    (sym (boundaryRetainsEdge D)
    ∙ chainMap (triangle D)
    ∙ cong (dPure D) (triangleDeleted D)
    ∙ dZero D)

-- Relativization supplies an underlying endpoint homotopy. Whether it is
-- allowed by a physical frame is a separate type with no automatic promotion.
record EndpointRelativization {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    EndpointMap EndpointHomotopy : Type ℓ
    UnderlyingNullhomotopy : EndpointMap → EndpointHomotopy → Type ℓ
    FramedNullhomotopy : EndpointMap → EndpointHomotopy → Type ℓ
    pulledBackEndpointMap : EndpointMap
    endpointPrimitive : EndpointHomotopy
    underlyingEquation :
      UnderlyingNullhomotopy pulledBackEndpointMap endpointPrimitive

open EndpointRelativization public

-- Explicit bridge from homological source degrees (2,1) to the bounded Hom
-- degrees (-1,0). This is required before calling source chains h_M and q.
record MorseDegreeAdapter {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    SourceDegree2 SourceDegree1 : Type ℓ
    sourceDifferential : SourceDegree2 → SourceDegree1
    realizeDegree2 : SourceDegree2 → JQminus1 P
    realizeDegree1 : SourceDegree1 → JQzero P
    differentialCompatibility : (x : SourceDegree2) →
      deltaJQ P (realizeDegree2 x) ≡
      realizeDegree1 (sourceDifferential x)
    sourceHM : SourceDegree2
    sourceQ : SourceDegree1
    sourceMorseFace : sourceDifferential sourceHM ≡ sourceQ
    identifiesHM : realizeDegree2 sourceHM ≡ h_M P
    identifiesQ : realizeDegree1 sourceQ ≡ q P

open MorseDegreeAdapter public

-- Connect a Q-support certificate to the generic-Q cell selected by an
-- existing adapter specification. This does not provide e, H_C, or a filler.
record QSupportAdapterBridge {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  (Spec : AdapterSpecification P) (C : QSupportCertificate {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    genericQCell : GenericQComparisonCell Spec
    genericQCellWitness : genericQCellValid Spec genericQCell
    -- Packet-specific relation: usually the quotient/contraction certificate.
    CellRepresentsQSupport : GenericQComparisonCell Spec →
      QSupportCertificate {ℓ} → Type ℓ
    representationWitness : CellRepresentsQSupport genericQCell C

-- Deliberately absent: physical e, H_C, discrepancy, framed endpoint
-- nullhomotopy, DGPyramidAdapter, or AdmissibleFiller constructors.
