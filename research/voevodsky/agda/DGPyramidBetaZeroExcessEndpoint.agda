{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidBetaZeroExcessEndpoint where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import Cubical.Data.Sigma using (_×_)

record BetaZeroExcessEndpointCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Coeff Chain HomologyClass MapClass Endpoint QPacket : Type ℓ
    beta x35 : Coeff
    zeroCoeff : Coeff
    multiply : Coeff → Chain → Chain
    differential : Chain → Chain
    zeroChain : Chain

    -- Only genuine v-units are used in this family; beta is not inverted.
    BetaInverse : Type ℓ
    betaInverseUnavailable : BetaInverse → ⊥
    unitNormalFrameComparison : Type ℓ
    unitNormalFrameWitness : unitNormalFrameComparison

    dividedPrimary primaryPrimitive secondaryDifference : Chain
    firstPrimitive secondPrimitive : Chain
    dividedPrimaryClosed : differential dividedPrimary ≡ zeroChain
    firstPrimitiveEquation :
      differential firstPrimitive ≡ multiply beta dividedPrimary
    secondPrimitiveEquation :
      differential secondPrimitive ≡ multiply beta dividedPrimary
    difference : Chain → Chain → Chain
    secondaryDifferenceEquation :
      secondaryDifference ≡ difference secondPrimitive firstPrimitive
    secondaryClosed : differential secondaryDifference ≡ zeroChain

    classOf : Chain → HomologyClass
    zeroHomology : HomologyClass
    primaryClass : HomologyClass
    secondaryClass : HomologyClass
    primaryClassDefinition : classOf dividedPrimary ≡ primaryClass
    secondaryClassDefinition : classOf secondaryDifference ≡ secondaryClass
    primaryPrimitiveNonzero : primaryClass ≡ zeroHomology → ⊥
    betaKillsPrimary : classOf (multiply beta dividedPrimary) ≡ zeroHomology
    secondaryNonzero : secondaryClass ≡ zeroHomology → ⊥
    x35KillsSecondary : classOf (multiply x35 secondaryDifference) ≡ zeroHomology
    BetaTorsion : HomologyClass → Type ℓ
    secondaryHasNoBetaTorsion : BetaTorsion secondaryClass → ⊥
    AnnihilatesHomology : Coeff → HomologyClass → Type ℓ
    X35Multiple : Coeff → Type ℓ
    secondaryExactAnnihilator : (a : Coeff) →
      (AnnihilatesHomology a secondaryClass → X35Multiple a) ×
      (X35Multiple a → AnnihilatesHomology a secondaryClass)

    SingleNormalSource SupportedMap : Type ℓ
    map03 mapMu : SupportedMap
    mapDifference : MapClass
    zeroMapClass : MapClass
    mapDifferenceDefinition : Type ℓ
    mapDifferenceWitness : mapDifferenceDefinition
    mapDifferenceNonzero : mapDifference ≡ zeroMapClass → ⊥
    betaKillsMapDifference : Type ℓ
    betaKillsMapDifferenceWitness : betaKillsMapDifference
    x35KillsMapDifference : Type ℓ
    x35KillsMapDifferenceWitness : x35KillsMapDifference
    AnnihilatesMap : Coeff → MapClass → Type ℓ
    BetaX35Ideal : Coeff → Type ℓ
    mapDifferenceExactAnnihilator : (a : Coeff) →
      (AnnihilatesMap a mapDifference → BetaX35Ideal a) ×
      (BetaX35Ideal a → AnnihilatesMap a mapDifference)

    endpointProjection : Chain → Endpoint
    zeroEndpoint : Endpoint
    negativeEndpoint : Endpoint
    secondaryEndpointEquation :
      endpointProjection secondaryDifference ≡ negativeEndpoint
    negativeEndpointNonzero : negativeEndpoint ≡ zeroEndpoint → ⊥

    qProjection : Chain → QPacket
    zeroQ : QPacket
    BetaOrder : QPacket → Type ℓ
    secondaryQOrderTwo : BetaOrder (qProjection secondaryDifference)
    endpointOrderZero : Type ℓ
    endpointOrderZeroWitness : endpointOrderZero
    topQOrderThree : Type ℓ
    topQOrderThreeWitness : topQOrderThree

    DegeneratePair ExcessLine : Type ℓ
    betaPair : DegeneratePair
    excessGenerator : ExcessLine
    zeroExcess : ExcessLine
    excessSurvivesAtBetaZero : excessGenerator ≡ zeroExcess → ⊥
    PairRegular : DegeneratePair → Type ℓ
    betaPairIsNotRegular : PairRegular betaPair → ⊥

    ProposedTwoPrimitiveLift FirstInfinitesimalLift : Type ℓ
    proposedAssignment : ProposedTwoPrimitiveLift
    liftToFirstInfinitesimal :
      ProposedTwoPrimitiveLift → FirstInfinitesimalLift → Type ℓ
    firstInfinitesimalObstructed : (L : FirstInfinitesimalLift) →
      liftToFirstInfinitesimal proposedAssignment L → ⊥

primaryAndSecondaryHaveDifferentSupport : {ℓ : Level}
  (C : BetaZeroExcessEndpointCertificate {ℓ}) →
  BetaZeroExcessEndpointCertificate.BetaTorsion C
    (BetaZeroExcessEndpointCertificate.secondaryClass C) → ⊥
primaryAndSecondaryHaveDifferentSupport C =
  BetaZeroExcessEndpointCertificate.secondaryHasNoBetaTorsion C

endpointFrameDetectsSecondaryDifference : {ℓ : Level}
  (C : BetaZeroExcessEndpointCertificate {ℓ}) →
  BetaZeroExcessEndpointCertificate.endpointProjection C
    (BetaZeroExcessEndpointCertificate.secondaryDifference C) ≡
  BetaZeroExcessEndpointCertificate.zeroEndpoint C → ⊥
endpointFrameDetectsSecondaryDifference C endpointZero =
  BetaZeroExcessEndpointCertificate.negativeEndpointNonzero C
    (sym (BetaZeroExcessEndpointCertificate.secondaryEndpointEquation C)
    ∙ endpointZero)
