{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidReverseEndpointGysin where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

record ReverseEndpointGysinCertificate {ℓ : Level}
  : Type (ℓ-suc ℓ) where
  field
    ReverseTwelve ReverseFourteen EndpointDual ConnectingMorphism : Type ℓ
    reverseTwelve : ReverseTwelve
    reverseFourteen : ReverseFourteen
    endpointDual : EndpointDual
    connectingMorphism : ConnectingMorphism
    ReverseEndpointTriangle : Type ℓ
    reverseEndpointTriangleWitness : ReverseEndpointTriangle
    zeroConnectingMorphism : ConnectingMorphism
    connectingGloballyNonzero : connectingMorphism ≡ zeroConnectingMorphism → ⊥

    CohomologyDegree CohomologySheafMap : Type ℓ
    inducedCohomologyMap : CohomologyDegree → ConnectingMorphism → CohomologySheafMap
    zeroCohomologyMap : CohomologyDegree → CohomologySheafMap
    connectingInvisibleOnCohomologySheaves : (j : CohomologyDegree) →
      inducedCohomologyMap j connectingMorphism ≡ zeroCohomologyMap j
    exactAnnihilatorUnchanged : Type ℓ

    EndpointAttachmentColumn : Type ℓ
    SixteenEndpointColumns : Type ℓ
    sixteenColumnsWitness : SixteenEndpointColumns
    positiveEndpointColumns negativeEndpointColumns : EndpointAttachmentColumn
    CommonChartPrimitive : Type ℓ
    commonChartPrimitive : CommonChartPrimitive
    primitiveEquation : Type ℓ
    localPrimitivesFailToDescend : Type ℓ

    PositiveSupport NegativeSupport SupportedEndpointLine : Type ℓ
    positiveSupport : PositiveSupport
    negativeSupport : NegativeSupport
    supportsDisjointFromOccurrenceConductor : Type ℓ
    ExtraordinaryRestriction : Type ℓ
    positiveExtraordinaryRestriction negativeExtraordinaryRestriction :
      ExtraordinaryRestriction
    restrictedConnectingVanishes : Type ℓ

    SupportedGysinLift SupportedCounit : Type ℓ
    positiveSupportedLift negativeSupportedLift : SupportedGysinLift
    positiveSupportedCounit negativeSupportedCounit : SupportedCounit
    positiveLiftCounitEquation negativeLiftCounitEquation : Type ℓ
    supportedLiftsNonzero : Type ℓ
    supportedLiftsDoNotSplitUnrestrictedEndpoint : Type ℓ

    PositiveLiftTorsor NegativeLiftTorsor : Type ℓ
    positiveLiftTorsor : PositiveLiftTorsor
    negativeLiftTorsor : NegativeLiftTorsor
    SevenPositiveFamilies SevenNegativeFamilies : Type ℓ
    sevenPositiveWitness : SevenPositiveFamilies
    sevenNegativeWitness : SevenNegativeFamilies
    liftingSpacesDiscrete : Type ℓ
    noPositiveHigherHomotopy noNegativeHigherHomotopy : Type ℓ
    FourteenSimultaneousAmbiguityFamilies : Type ℓ
    fourteenAmbiguityWitness : FourteenSimultaneousAmbiguityFamilies

    PhysicalSupportedLiftSelection : Type ℓ
