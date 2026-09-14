{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidThreeByFourTotalization where

open import Cubical.Foundations.Prelude

-- One carrier equipped with the four transverse comparison directions.  The
-- compatibility field represents the signed pairwise anticommutation laws;
-- it is not inferred merely from four square-zero endomorphisms.
record FourModeComplex {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Carrier : Type ℓ
    zero : Carrier
    realizationD underdeterminationD overpresentationD coherenceD :
      Carrier → Carrier

    realizationSquared : (x : Carrier) →
      realizationD (realizationD x) ≡ zero
    underdeterminationSquared : (x : Carrier) →
      underdeterminationD (underdeterminationD x) ≡ zero
    overpresentationSquared : (x : Carrier) →
      overpresentationD (overpresentationD x) ≡ zero
    coherenceSquared : (x : Carrier) →
      coherenceD (coherenceD x) ≡ zero

    SignedPairwiseCompatibility : Type ℓ
    allSixSignedMixedSquaresClose : SignedPairwiseCompatibility

open FourModeComplex public

-- A map between categorical levels must intertwine all four directions.  This
-- prevents a scalar comparison from being promoted merely because it commutes
-- with one constituent differential.
record FourModeMap {ℓ : Level}
  (Source Target : FourModeComplex {ℓ}) : Type (ℓ-suc ℓ) where
  field
    map : Carrier Source → Carrier Target
    preservesZero : map (zero Source) ≡ zero Target
    preservesRealization : (x : Carrier Source) →
      map (realizationD Source x) ≡ realizationD Target (map x)
    preservesUnderdetermination : (x : Carrier Source) →
      map (underdeterminationD Source x) ≡
      underdeterminationD Target (map x)
    preservesOverpresentation : (x : Carrier Source) →
      map (overpresentationD Source x) ≡ overpresentationD Target (map x)
    preservesCoherence : (x : Carrier Source) →
      map (coherenceD Source x) ≡ coherenceD Target (map x)

-- Three categorical levels crossed with four transverse modes: twelve sectors.
-- The first map is physical realization to its relative control object; the
-- second is evaluation in cyclic cochains.
record ThreeByFourCollar {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    PhysicalHom ControlHom CyclicCochains : FourModeComplex {ℓ}
    physicalToControl : FourModeMap PhysicalHom ControlHom
    controlToCyclic : FourModeMap ControlHom CyclicCochains

    PhysicalEndpointClass ControlResidue CyclicDeformationClass : Type ℓ
    physicalEndpointClass : PhysicalEndpointClass
    controlResidue : ControlResidue
    cyclicDeformationClass : CyclicDeformationClass

    endpointClassMapsToResidue : Type ℓ
    residueMapsToCyclicDeformationClass : Type ℓ
    productCartierAndDeterminantFramesPersistAcrossRows : Type ℓ

-- Exact audit against current results.  Two rows are partially constructed;
-- the cyclic row and the cross-row physical maps await the Branch A/C arrows.
record CurrentThreeByFourAudit {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    coefficientPhysicalHomDirectionsArePartiallyConstructed : Type ℓ
    relativeControlDifferentialFormulaIsConstructed : Type ℓ
    overpresentationBarDirectionIsExplicit : Type ℓ
    comparisonCoherenceDirectionIsExplicitInCandidateModel : Type ℓ
    physicalToControlMapAwaitsChiAndTau : Type ℓ
    cyclicCochainRowAwaitsPhysicalQStructure : Type ℓ
    noStructuralThreeByFourInhabitantClaimedYet : Type ℓ

-- A successful structural test must instantiate this record from actual maps,
-- rather than matching the number twelve in independent computations.
record ThreeByFourStructuralTest {ℓ : Level}
  (C : ThreeByFourCollar {ℓ}) : Type (ℓ-suc ℓ) where
  field
    allTwelveSectorsHaveDeclaredFrames : Type ℓ
    bothCrossLevelMapsAreTheActualDerivedMaps : Type ℓ
    everyKnownClassHasOneDeclaredSector : Type ℓ
    noSectorIsDuplicatedToFitTheCount : Type ℓ
    totalizationRecoversPhysicalComparisonDifferential : Type ℓ
    oneOneIsBoundaryOfTheDeclaredControlResidue : Type ℓ
