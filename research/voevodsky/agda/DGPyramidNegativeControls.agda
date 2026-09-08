{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidNegativeControls where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)
open import PyramidNormalizationObstruction
open import DGPyramidBoundary
open import DGPyramidFiller

-- Control 1: the checked normalization obstruction is retained verbatim.
-- A frame cannot create an underlying nullhomotopy that is already impossible.
normalizedSourceCannotBeBoundary : Nullhomotopy → ⊥
normalizedSourceCannotBeBoundary = augmentationNotNullhomotopic

-- Control 2: abstract exactly the established support statement for Xi_jet.
-- It says the CURRENT readout kills literal endpoint inclusion pointwise. It
-- does not say endpoint cochains vanish, nor constrain an extraordinary map.
record EndpointJetControl {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SourceInput EndpointCochain AmbientCochain JetValue : Type ℓ
    endpointValue : SourceInput → EndpointCochain
    literalEndpointInclusion : EndpointCochain → AmbientCochain
    jetReadout : AmbientCochain → JetValue
    zeroJet : JetValue
    annihilatesLiteralEndpoint : (v : EndpointCochain) →
      jetReadout (literalEndpointInclusion v) ≡ zeroJet

open EndpointJetControl public

literalEndpointRouteIsZero : {ℓ : Level} (C : EndpointJetControl {ℓ})
  (input : SourceInput C) →
  jetReadout C (literalEndpointInclusion C (endpointValue C input)) ≡ zeroJet C
literalEndpointRouteIsZero C input =
  annihilatesLiteralEndpoint C (endpointValue C input)

-- Factoring through endpoint support remains invisible after any precomposition.
precomposedEndpointRouteIsZero : {ℓ : Level} (C : EndpointJetControl {ℓ})
  {A : Type ℓ} (precompose : A → SourceInput C) (x : A) →
  jetReadout C
    (literalEndpointInclusion C (endpointValue C (precompose x))) ≡ zeroJet C
precomposedEndpointRouteIsZero C precompose x =
  literalEndpointRouteIsZero C (precompose x)

-- The theorem has no converse. A zero jet value is not an equality of ambient
-- or endpoint cochains, and no such constructor is exported.

-- Control 3: provenance and normalization are independent obligations.
data PresentationOrigin : Type where
  targetDerived physicalSource : PresentationOrigin

OriginEvidence : PresentationOrigin → Type
OriginEvidence targetDerived = PrimitiveCycle
OriginEvidence physicalSource = ⊥

targetDerivedIsNotPhysical : targetDerived ≡ physicalSource → ⊥
targetDerivedIsNotPhysical path =
  transport (cong OriginEvidence path) z

-- A target-derived obstruction presentation may be a valid test object, but
-- masquerading as the physical source would require both a false provenance
-- identification and the already refuted normalized-to-exact comparison.
record TargetTriangleMasquerade : Type where
  field
    identifiesOrigin : targetDerived ≡ physicalSource
    identifiesNormalization : NormalizedComparison

masqueradeImpossibleByOrigin : TargetTriangleMasquerade → ⊥
masqueradeImpossibleByOrigin candidate =
  targetDerivedIsNotPhysical
    (TargetTriangleMasquerade.identifiesOrigin candidate)

masqueradeImpossibleByNormalization : TargetTriangleMasquerade → ⊥
masqueradeImpossibleByNormalization candidate =
  normalizedComparisonImpossible
    (TargetTriangleMasquerade.identifiesNormalization candidate)

-- Negative framing control: an unframed boundary filler cannot populate a
-- frame whose support condition is empty.
record EmptySupportFrame {ℓ : Level} (P : DGPyramidBoundary {ℓ})
  (Base : PyramidFrame P) : Type (ℓ-suc ℓ) where
  field
    supportAlwaysImpossible : (K : JFzero Base) → PreservesSupport Base K → ⊥

emptySupportHasNoAdmissibleFiller : {ℓ : Level}
  {P : DGPyramidBoundary {ℓ}} {Frame : PyramidFrame P}
  → EmptySupportFrame P Frame → AdmissibleFiller P Frame → ⊥
emptySupportHasNoAdmissibleFiller {P = P} {Frame = Frame} control filler =
  EmptySupportFrame.supportAlwaysImpossible control
    (fillerCandidate {P = P} {Frame = Frame} filler)
    (fillerSupport {P = P} {Frame = Frame} filler)

-- Scope: these controls reject three specific invalid promotions. They do not
-- prove the physical filler type empty for every future extraordinary adapter.
