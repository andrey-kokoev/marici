{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidFixture where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Unit
open import DGPyramidBoundary
open import DGPyramidFiller
open import DGPyramidAdapter

-- A deliberately nonphysical fixture. Every Hom group is terminal, but map
-- and connector token types remain nominally distinct to test adapter wiring.
toyBoundary : DGPyramidBoundary
DGPyramidBoundary.SourceObj toyBoundary = Unit
DGPyramidBoundary.GenericObj toyBoundary = Unit
DGPyramidBoundary.SupportedObj toyBoundary = Unit
DGPyramidBoundary.JQminus1 toyBoundary = Unit
DGPyramidBoundary.JQzero toyBoundary = Unit
DGPyramidBoundary.QFtwo toyBoundary = Unit
DGPyramidBoundary.QFthree toyBoundary = Unit
DGPyramidBoundary.JFone toyBoundary = Unit
DGPyramidBoundary.JFtwo toyBoundary = Unit
DGPyramidBoundary.zeroQFthree toyBoundary = tt
DGPyramidBoundary.zeroJFtwo toyBoundary = tt
DGPyramidBoundary.addJFone toyBoundary _ _ = tt
DGPyramidBoundary.negJFone toyBoundary _ = tt
DGPyramidBoundary.addJFtwo toyBoundary _ _ = tt
DGPyramidBoundary.negJFtwo toyBoundary _ = tt
DGPyramidBoundary.deltaJQ toyBoundary _ = tt
DGPyramidBoundary.deltaQF toyBoundary _ = tt
DGPyramidBoundary.deltaJF toyBoundary _ = tt
DGPyramidBoundary.compose20 toyBoundary _ _ = tt
DGPyramidBoundary.compose2minus1 toyBoundary _ _ = tt
DGPyramidBoundary.compose3minus1 toyBoundary _ _ = tt
DGPyramidBoundary.q toyBoundary = tt
DGPyramidBoundary.e toyBoundary = tt
DGPyramidBoundary.hM toyBoundary = tt
DGPyramidBoundary.HC toyBoundary = tt
DGPyramidBoundary.morseFace toyBoundary = refl
DGPyramidBoundary.eClosed toyBoundary = refl
DGPyramidBoundary.conductorFace toyBoundary = refl
DGPyramidBoundary.compositionBoundary toyBoundary = refl
DGPyramidBoundary.deltaDifference toyBoundary _ _ = refl
DGPyramidBoundary.composeZero toyBoundary = refl
DGPyramidBoundary.zeroPlus toyBoundary _ = refl
DGPyramidBoundary.differenceSelf toyBoundary _ = refl

toyClosure : deltaJF toyBoundary (pyramidDiscrepancy toyBoundary)
  ≡ zeroJFtwo toyBoundary
toyClosure = pyramidDiscrepancyClosed toyBoundary

toyFrame : PyramidFrame toyBoundary
PyramidFrame.JFzero toyFrame = Unit
PyramidFrame.deltaFiller toyFrame _ = tt
PyramidFrame.PreservesSupport toyFrame _ = Unit
PyramidFrame.PreservesEndpoints toyFrame _ = Unit
PyramidFrame.PreservesGenericQ toyFrame _ = Unit
PyramidFrame.PreservesReesCartier toyFrame _ = Unit

toyFiller : AdmissibleFiller toyBoundary toyFrame
toyFiller = tt , refl , tt , tt , tt , tt

data SourceMapToken : Type where sourceMapToken : SourceMapToken
data GenericMapToken : Type where genericMapToken : GenericMapToken
data SupportedMapToken : Type where supportedMapToken : SupportedMapToken
data PlusConnectorToken : Type where plusConnectorToken : PlusConnectorToken
data MinusConnectorToken : Type where minusConnectorToken : MinusConnectorToken
data GenericQToken : Type where genericQToken : GenericQToken
data ReesCartierToken : Type where reesCartierToken : ReesCartierToken

toySpecification : AdapterSpecification toyBoundary
AdapterSpecification.ConcreteSource toySpecification = Unit
AdapterSpecification.ConcreteGeneric toySpecification = Unit
AdapterSpecification.ConcreteSupported toySpecification = Unit
AdapterSpecification.ConcreteSourceMap toySpecification = SourceMapToken
AdapterSpecification.ConcreteGenericMap toySpecification = GenericMapToken
AdapterSpecification.ConcreteSupportedMap toySpecification = SupportedMapToken
AdapterSpecification.sourceMapAction toySpecification _ _ = tt
AdapterSpecification.genericMapAction toySpecification _ _ = tt
AdapterSpecification.supportedMapAction toySpecification _ _ = tt
AdapterSpecification.sourceMapValid toySpecification _ = Unit
AdapterSpecification.genericMapValid toySpecification _ = Unit
AdapterSpecification.supportedMapValid toySpecification _ = Unit
AdapterSpecification.ConcreteQ toySpecification = Unit
AdapterSpecification.ConcreteE toySpecification = Unit
AdapterSpecification.ConcreteHM toySpecification = Unit
AdapterSpecification.ConcreteHC toySpecification = Unit
AdapterSpecification.realizeQ toySpecification _ = tt
AdapterSpecification.realizeE toySpecification _ = tt
AdapterSpecification.realizeHM toySpecification _ = tt
AdapterSpecification.realizeHC toySpecification _ = tt
AdapterSpecification.PlusConnector toySpecification = PlusConnectorToken
AdapterSpecification.MinusConnector toySpecification = MinusConnectorToken
AdapterSpecification.plusConnectorValid toySpecification _ = Unit
AdapterSpecification.minusConnectorValid toySpecification _ = Unit
AdapterSpecification.GenericQComparisonCell toySpecification = GenericQToken
AdapterSpecification.ReesCartierComparisonCell toySpecification = ReesCartierToken
AdapterSpecification.genericQCellValid toySpecification _ = Unit
AdapterSpecification.reesCartierCellValid toySpecification _ = Unit

toyAdapter : DGPyramidAdapter toySpecification
DGPyramidAdapter.sourceMap toyAdapter = sourceMapToken
DGPyramidAdapter.genericMap toyAdapter = genericMapToken
DGPyramidAdapter.supportedMap toyAdapter = supportedMapToken
DGPyramidAdapter.sourceWitness toyAdapter = tt
DGPyramidAdapter.genericWitness toyAdapter = tt
DGPyramidAdapter.supportedWitness toyAdapter = tt
DGPyramidAdapter.concreteQ toyAdapter = tt
DGPyramidAdapter.concreteE toyAdapter = tt
DGPyramidAdapter.concreteHM toyAdapter = tt
DGPyramidAdapter.concreteHC toyAdapter = tt
DGPyramidAdapter.identifiesQ toyAdapter = refl
DGPyramidAdapter.identifiesE toyAdapter = refl
DGPyramidAdapter.identifiesHM toyAdapter = refl
DGPyramidAdapter.identifiesHC toyAdapter = refl
DGPyramidAdapter.plusConnector toyAdapter = plusConnectorToken
DGPyramidAdapter.minusConnector toyAdapter = minusConnectorToken
DGPyramidAdapter.plusWitness toyAdapter = tt
DGPyramidAdapter.minusWitness toyAdapter = tt
DGPyramidAdapter.genericQComparison toyAdapter = genericQToken
DGPyramidAdapter.reesCartierComparison toyAdapter = reesCartierToken
DGPyramidAdapter.genericQWitness toyAdapter = tt
DGPyramidAdapter.reesCartierWitness toyAdapter = tt

toyAdaptedFiller : AdaptedFiller toySpecification toyFrame
AdaptedFiller.adapter toyAdaptedFiller = toyAdapter
AdaptedFiller.filler toyAdaptedFiller = toyFiller

toyNamedObjects : Σ (DGPyramidBoundary.J toyBoundary) λ _ →
  Σ (DGPyramidBoundary.Q toyBoundary) λ _ →
    DGPyramidBoundary.F toyBoundary
toyNamedObjects = tt , tt , tt

toyNamedCells : Σ (JQminus1 toyBoundary) λ _ → JFone toyBoundary
toyNamedCells = h_M toyBoundary , H_C toyBoundary

toySourceComparisonApplied : SourceObj toyBoundary
toySourceComparisonApplied = concreteSourceComparison toyAdapter tt

toyTargetComparisonApplied : SupportedObj toyBoundary
toyTargetComparisonApplied = concreteTargetComparison toyAdapter tt

-- Distinct endpoint connector types prevent swapping by definitional equality.
toyPlus : PlusConnector toySpecification
toyPlus = adaptedPlusConnector toyAdapter

toyMinus : MinusConnector toySpecification
toyMinus = adaptedMinusConnector toyAdapter

-- This fixture validates architecture only. Terminal validity predicates are
-- not evidence for any source packet and are never exported as physical data.
