{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidPurityDualTransgression where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Principal occurrence-line factorization must precede branch restriction.
record PrincipalLineDualityCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Ring Line DualLine BranchRing Source EndpointTarget : Type ℓ
    lineFrame : Line
    dualFrame : DualLine
    includeLine : Line → Ring
    evaluateLine : DualLine → Line → Ring
    baseChangeLine : Line → BranchRing
    baseChangeRing : Ring → BranchRing
    zeroBranch : BranchRing
    multiplicationDiesOnBranch :
      baseChangeRing (includeLine lineFrame) ≡ zeroBranch

    oldEndpointMap : Source → EndpointTarget
    normalizedEndpointMap : Source → EndpointTarget
    FactorizesThroughLine :
      (Source → EndpointTarget) → Line → (Source → EndpointTarget) → Type ℓ
    endpointFactorization :
      FactorizesThroughLine oldEndpointMap lineFrame normalizedEndpointMap
    factorizationUnique : (candidate : Source → EndpointTarget) →
      FactorizesThroughLine oldEndpointMap lineFrame candidate →
      candidate ≡ normalizedEndpointMap

    BranchEndpointClass : Type ℓ
    zeroEndpointClass : BranchEndpointClass
    restrictNormalizedEndpoint :
      (Source → EndpointTarget) → BranchEndpointClass
    normalizedEndpointSurvives :
      restrictNormalizedEndpoint normalizedEndpointMap ≡ zeroEndpointClass → ⊥

open PrincipalLineDualityCertificate public

-- Ordered regular-immersion purity with its determinant and codimension shift.
record RegularImmersionPurityCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    AmbientObject RestrictedObject ExactSupportRHom : Type ℓ
    DeterminantLine DualDeterminantLine Shift : Type ℓ
    orderedDeterminant : DeterminantLine
    dualDeterminant : DualDeterminantLine
    codimensionShift : Shift
    derivedRestriction : AmbientObject → RestrictedObject
    purityTarget : RestrictedObject → DualDeterminantLine → Shift → ExactSupportRHom
    purityMap : AmbientObject → ExactSupportRHom
    purityInverse : ExactSupportRHom → AmbientObject
    puritySection : (x : AmbientObject) → purityInverse (purityMap x) ≡ x
    purityRetraction : (x : ExactSupportRHom) → purityMap (purityInverse x) ≡ x

    ExcessSource ExcessTarget : Type ℓ
    excessGenerator : ExcessSource
    zeroExcessTarget : ExcessTarget
    purityOnExcess : ExcessSource → ExcessTarget
    purityPreservesExcess :
      purityOnExcess excessGenerator ≡ zeroExcessTarget → ⊥

open RegularImmersionPurityCertificate public

-- Finite homogeneous duality reverses the support transgression and pairs both
-- sides primitively; it does not turn the obstruction into a boundary.
record DualTransgressionCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    GenericClass SupportClass DualGeneric DualSupport Scalar : Type ℓ
    genericClass : GenericClass
    supportObstruction : SupportClass
    dualGeneric : DualGeneric
    dualSupport : DualSupport
    one : Scalar
    zeroScalar : Scalar
    pairGeneric : DualGeneric → GenericClass → Scalar
    pairSupport : DualSupport → SupportClass → Scalar
    reverseConnecting : DualSupport → DualGeneric
    reverseConnectingEquation : reverseConnecting dualSupport ≡ dualGeneric
    genericPairingPrimitive : pairGeneric dualGeneric genericClass ≡ one
    supportPairingPrimitive : pairSupport dualSupport supportObstruction ≡ one
    oneNonzero : one ≡ zeroScalar → ⊥

open DualTransgressionCertificate public

dualityDoesNotKillSupportObstruction : {ℓ : Level}
  (C : DualTransgressionCertificate {ℓ}) →
  pairSupport C (dualSupport C) (supportObstruction C) ≡ zeroScalar C → ⊥
dualityDoesNotKillSupportObstruction C zeroPairing =
  oneNonzero C (sym (supportPairingPrimitive C) ∙ zeroPairing)

-- Product-Rees branch selection preserves excess forward, while the adjugate
-- return multiplies it by the Rees determinant and kills it centrally.
record ReesSelectorExcessCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SourceNormal SourceSelected Coeff CentralExcess : Type ℓ
    forward : SourceNormal → SourceSelected
    adjugateReturn : SourceSelected → SourceNormal
    scaleNormal : Coeff → SourceNormal → SourceNormal
    scaleSelected : Coeff → SourceSelected → SourceSelected
    branchReesDeterminant : Coeff
    forwardReturn : (x : SourceNormal) →
      adjugateReturn (forward x) ≡ scaleNormal branchReesDeterminant x
    returnForward : (x : SourceSelected) →
      forward (adjugateReturn x) ≡ scaleSelected branchReesDeterminant x

    normalExcess : SourceNormal
    selectedExcess : SourceSelected
    forwardPreservesExcess : forward normalExcess ≡ selectedExcess
    returnScalesExcess :
      adjugateReturn selectedExcess ≡
      scaleNormal branchReesDeterminant normalExcess

    specializeSelected : SourceSelected → CentralExcess
    specializeReturned : SourceNormal → CentralExcess
    zeroCentral : CentralExcess
    selectedExcessSurvivesCentral :
      specializeSelected selectedExcess ≡ zeroCentral → ⊥
    returnedExcessDiesCentral :
      specializeReturned (adjugateReturn selectedExcess) ≡ zeroCentral

open ReesSelectorExcessCertificate public

adjugateReturnDoesNotPreservePrimitiveCentralExcess : {ℓ : Level}
  (C : ReesSelectorExcessCertificate {ℓ}) →
  specializeReturned C (adjugateReturn C (selectedExcess C)) ≡
    specializeSelected C (selectedExcess C) → ⊥
adjugateReturnDoesNotPreservePrimitiveCentralExcess C identifies =
  selectedExcessSurvivesCentral C
    (sym identifies ∙ returnedExcessDiesCentral C)

-- No certificate above identifies its finite dual with spatial Verdier duality
-- or supplies the two physical connector 2-cells.
