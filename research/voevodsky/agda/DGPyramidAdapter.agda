{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidAdapter where

open import Cubical.Foundations.Prelude
open import DGPyramidBoundary
open import DGPyramidFiller

-- A future packet first declares the concrete types and the exact obligations
-- its maps/cells must satisfy. This layer permits strict maps, roofs, or richer
-- records as ConcreteSourceMap etc.; their validity predicates decide what is
-- accepted. Merely choosing Unit for everything gives no physical provenance.
record AdapterSpecification {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  : Type (ℓ-suc ℓ) where
  field
    ConcreteSource ConcreteGeneric ConcreteSupported : Type ℓ

    ConcreteSourceMap ConcreteGenericMap ConcreteSupportedMap : Type ℓ
    -- Every comparison object has an actual action on its declared concrete
    -- object. Extra roof/homotopy data may live in the map type itself.
    sourceMapAction : ConcreteSourceMap → ConcreteSource → SourceObj P
    genericMapAction : ConcreteGenericMap → ConcreteGeneric → GenericObj P
    supportedMapAction : ConcreteSupportedMap → ConcreteSupported → SupportedObj P
    sourceMapValid : ConcreteSourceMap → Type ℓ
    genericMapValid : ConcreteGenericMap → Type ℓ
    supportedMapValid : ConcreteSupportedMap → Type ℓ

    -- Concrete Hom cells computed by the packet before comparison with P.
    ConcreteQ ConcreteE ConcreteHM ConcreteHC : Type ℓ
    realizeQ : ConcreteQ → JQzero P
    realizeE : ConcreteE → QFtwo P
    realizeHM : ConcreteHM → JQminus1 P
    realizeHC : ConcreteHC → JFone P

    -- Both endpoint connector cells remain first-class data.
    PlusConnector MinusConnector : Type ℓ
    plusConnectorValid : PlusConnector → Type ℓ
    minusConnectorValid : MinusConnector → Type ℓ

    -- Compatibility cells are separate: endpoint validity cannot imply Q or
    -- Rees/Cartier compatibility.
    GenericQComparisonCell ReesCartierComparisonCell : Type ℓ
    genericQCellValid : GenericQComparisonCell → Type ℓ
    reesCartierCellValid : ReesCartierComparisonCell → Type ℓ

open AdapterSpecification public

record DGPyramidAdapter {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  (Spec : AdapterSpecification P) : Type (ℓ-suc ℓ) where
  field
    sourceMap : ConcreteSourceMap Spec
    genericMap : ConcreteGenericMap Spec
    supportedMap : ConcreteSupportedMap Spec
    sourceWitness : sourceMapValid Spec sourceMap
    genericWitness : genericMapValid Spec genericMap
    supportedWitness : supportedMapValid Spec supportedMap

    concreteQ : ConcreteQ Spec
    concreteE : ConcreteE Spec
    concreteHM : ConcreteHM Spec
    concreteHC : ConcreteHC Spec

    -- These paths force the packet's cells to instantiate THIS boundary,
    -- rather than merely having matching scalar readouts.
    identifiesQ : realizeQ Spec concreteQ ≡ q P
    identifiesE : realizeE Spec concreteE ≡ e P
    identifiesHM : realizeHM Spec concreteHM ≡ hM P
    identifiesHC : realizeHC Spec concreteHC ≡ HC P

    plusConnector : PlusConnector Spec
    minusConnector : MinusConnector Spec
    plusWitness : plusConnectorValid Spec plusConnector
    minusWitness : minusConnectorValid Spec minusConnector

    genericQComparison : GenericQComparisonCell Spec
    reesCartierComparison : ReesCartierComparisonCell Spec
    genericQWitness : genericQCellValid Spec genericQComparison
    reesCartierWitness : reesCartierCellValid Spec reesCartierComparison

open DGPyramidAdapter public

-- Applied comparison maps exposed with source/target terminology. Thus an
-- adapter inhabitant provides functions, not merely names for map records.
concreteSourceComparison : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Spec : AdapterSpecification P} → DGPyramidAdapter Spec →
  ConcreteSource Spec → SourceObj P
concreteSourceComparison {Spec = Spec} adapter =
  sourceMapAction Spec (sourceMap adapter)

concreteGenericComparison : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Spec : AdapterSpecification P} → DGPyramidAdapter Spec →
  ConcreteGeneric Spec → GenericObj P
concreteGenericComparison {Spec = Spec} adapter =
  genericMapAction Spec (genericMap adapter)

concreteTargetComparison : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Spec : AdapterSpecification P} → DGPyramidAdapter Spec →
  ConcreteSupported Spec → SupportedObj P
concreteTargetComparison {Spec = Spec} adapter =
  supportedMapAction Spec (supportedMap adapter)

-- A packet accepted by the adapter inherits closure from the boundary laws;
-- closure is never supplied independently by the packet.
adaptedDiscrepancyClosed : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Spec : AdapterSpecification P} → DGPyramidAdapter Spec →
  deltaJF P (pyramidDiscrepancy P) ≡ zeroJFtwo P
adaptedDiscrepancyClosed {P = P} adapter = pyramidDiscrepancyClosed P

-- Adapter data alone do not manufacture a filler. A packet that also proposes
-- one must pass the existing four-condition framed fibre unchanged.
record AdaptedFiller {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  (Spec : AdapterSpecification P) (Frame : PyramidFrame P)
  : Type (ℓ-suc ℓ) where
  field
    adapter : DGPyramidAdapter Spec
    filler : AdmissibleFiller P Frame

-- Endpoint cells can be retrieved independently; neither can be reconstructed
-- from the other or from the generic-Q comparison.
adaptedPlusConnector : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Spec : AdapterSpecification P} → DGPyramidAdapter Spec → PlusConnector Spec
adaptedPlusConnector = plusConnector

adaptedMinusConnector : {ℓ : Level} {P : DGPyramidBoundary {ℓ}}
  {Spec : AdapterSpecification P} → DGPyramidAdapter Spec → MinusConnector Spec
adaptedMinusConnector = minusConnector

-- No constructor from artifact paths, scalar values, target-derived triangle
-- data, or literal endpoint readout is exported.
