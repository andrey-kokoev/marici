{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidMarkedNormalQ where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Unit using (Unit; tt)

-- Fine Q sectors are nominally separated so the marked top class cannot be
-- installed as the exact unit-degree roof by an implicit coercion.
data QFineSector : Type where
  unitDegree allLongNormals : QFineSector

SectorEvidence : QFineSector → Type
SectorEvidence unitDegree = Unit
SectorEvidence allLongNormals = ⊥

markedSectorIsNotUnitSector : allLongNormals ≡ unitDegree → ⊥
markedSectorIsNotUnitSector path =
  transport (cong SectorEvidence (sym path)) tt

record MarkedNormalQCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    UnitRoof MarkedTop MarkedDegree2 SupportDegree2 : Type ℓ
    unitRoof : UnitRoof
    markedBoundary : MarkedTop → MarkedDegree2
    zeroMarked : MarkedDegree2

    -- The corrected all-long-normal top cycle omega.
    omega : MarkedTop
    omegaClosed : markedBoundary omega ≡ zeroMarked

    -- Its actual short-support transgression b (the concrete packet records
    -- the eighteen terms and their coefficients inside SupportDegree2).
    supportConnectingBoundary : MarkedTop → SupportDegree2
    b : SupportDegree2
    zeroSupport : SupportDegree2
    omegaConnectsToB : supportConnectingBoundary omega ≡ b
    bNonzero : b ≡ zeroSupport → ⊥

    -- Equivariant sign-line behavior.
    rotate reflect negateTop : MarkedTop → MarkedTop
    rotationFixesOmega : rotate omega ≡ omega
    reflectionNegatesOmega : reflect omega ≡ negateTop omega

    -- Independently framed marked comparison admits an order-two loop. This
    -- does not choose a physical parity or identify an external Tor state.
    ComparisonLoop LoopCoboundary : Type ℓ
    markedLoop : ComparisonLoop
    doubleLoopBoundary : ComparisonLoop → LoopCoboundary → Type ℓ
    loopNontrivial : ComparisonLoop → Type ℓ
    doubledLoopPrimitive : LoopCoboundary
    doubledLoopIsBoundary :
      doubleLoopBoundary markedLoop doubledLoopPrimitive
    markedLoopIsNontrivial : loopNontrivial markedLoop

    -- A specified normal-multiplication comparison is stricter than an
    -- independently framed marked comparison.
    UnitComparison IndependentMarkedComparison : Type ℓ
    multiplyAllLongNormals : UnitComparison → IndependentMarkedComparison

open MarkedNormalQCertificate public

-- No map from IndependentMarkedComparison back to UnitComparison, no physical
-- parity selector, and no promotion to a pyramid filler are exported.
