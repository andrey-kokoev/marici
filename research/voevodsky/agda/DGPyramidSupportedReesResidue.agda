{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidSupportedReesResidue where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- The supported residue is intentionally distinct from an ordinary return
-- D_x -> D_u. The latter is universally determinant-divisible and vanishes on
-- the central Rees fibre; the former survives as a shifted Gysin extension.
record SupportedReesResidueTraceCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    RawSource SelectedSource RawExcess SelectedExcess : Type ℓ
    Coeff CentralExcess : Type ℓ
    tau zeroCentral : Coeff
    etaRaw : RawExcess
    etaSelected : SelectedExcess

    OrdinaryDerivedReturn : Type ℓ
    returnOnExcess : OrdinaryDerivedReturn → SelectedExcess → RawExcess
    TauDivisible : RawExcess → Type ℓ
    everyReturnTauDivisible : (f : OrdinaryDerivedReturn) →
      TauDivisible (returnOnExcess f etaSelected)
    specializeRawExcess : RawExcess → CentralExcess
    zeroCentralExcess : CentralExcess
    tauDivisibleDiesCentral : (z : RawExcess) →
      TauDivisible z → specializeRawExcess z ≡ zeroCentralExcess
    selectedCentralExcess : CentralExcess
    selectedCentralExcessNonzero : selectedCentralExcess ≡ zeroCentralExcess → ⊥

    KoszulDual CechSupport : Type ℓ
    differentialKoszul : KoszulDual → KoszulDual
    differentialCech : CechSupport → CechSupport
    supportedResidue : KoszulDual → CechSupport
    residueChainMap : (z : KoszulDual) →
      supportedResidue (differentialKoszul z) ≡
      differentialCech (supportedResidue z)

    Face : Type ℓ
    centralFace : Face
    specializeResidue : Face → KoszulDual → CechSupport
    FaceEdge : Face → Face → Type ℓ
    faceNaturality : {P Q : Face} → FaceEdge P Q → (z : KoszulDual) →
      specializeResidue Q z ≡ specializeResidue P z
    FaceSquare : Type ℓ
    allPartialFaceSquaresCommute : FaceSquare

    GysinExtension DualDeterminant Shift : Type ℓ
    centralGysin : GysinExtension
    zeroGysin : GysinExtension
    branchDualDeterminant : DualDeterminant
    codimensionThreeShift : Shift
    centralResidueRepresentsGysin : Type ℓ
    centralResidueWitness : centralResidueRepresentsGysin
    centralGysinPrimitive : centralGysin ≡ zeroGysin → ⊥

    ExcessGysinChannel : Type ℓ
    excessGysin : SelectedExcess → GysinExtension → ExcessGysinChannel
    zeroExcessGysin : ExcessGysinChannel
    shiftedExcessSurvives :
      excessGysin etaSelected centralGysin ≡ zeroExcessGysin → ⊥
    bareCentralDegreeOneImage : CentralExcess
    bareDegreeOneImageIsZero : bareCentralDegreeOneImage ≡ zeroCentralExcess

    SupportObstruction GenericObstruction : Type ℓ
    DualSupportFunctional DualGenericFunctional GysinValue : Type ℓ
    beta : SupportObstruction
    generic : GenericObstruction
    betaDual : DualSupportFunctional
    genericDual : DualGenericFunctional
    gysinValue : GysinValue
    zeroGysinValue : GysinValue
    reverseConnecting : DualSupportFunctional → DualGenericFunctional
    reverseConnectingEquation : reverseConnecting betaDual ≡ genericDual
    pairSupport : DualSupportFunctional → SupportObstruction → GysinValue
    pairGeneric : DualGenericFunctional → GenericObstruction → GysinValue
    supportPairingIsGysin : pairSupport betaDual beta ≡ gysinValue
    genericPairingIsGysin : pairGeneric genericDual generic ≡ gysinValue
    gysinValueNonzero : gysinValue ≡ zeroGysinValue → ⊥

ordinaryReturnKillsCentralExcess : {ℓ : Level}
  (C : SupportedReesResidueTraceCertificate {ℓ})
  (f : SupportedReesResidueTraceCertificate.OrdinaryDerivedReturn C) →
  SupportedReesResidueTraceCertificate.specializeRawExcess C
    (SupportedReesResidueTraceCertificate.returnOnExcess C f
      (SupportedReesResidueTraceCertificate.etaSelected C)) ≡
  SupportedReesResidueTraceCertificate.zeroCentralExcess C
ordinaryReturnKillsCentralExcess C f =
  SupportedReesResidueTraceCertificate.tauDivisibleDiesCentral C _
    (SupportedReesResidueTraceCertificate.everyReturnTauDivisible C f)

-- A primitive shifted residue must not be reinterpreted as the bare degree-one
-- image, which is explicitly zero on the central face.
shiftedResidueIsNotBareExcessImage : {ℓ : Level}
  (C : SupportedReesResidueTraceCertificate {ℓ}) →
  SupportedReesResidueTraceCertificate.excessGysin C
    (SupportedReesResidueTraceCertificate.etaSelected C)
    (SupportedReesResidueTraceCertificate.centralGysin C) ≡
  SupportedReesResidueTraceCertificate.zeroExcessGysin C → ⊥
shiftedResidueIsNotBareExcessImage C =
  SupportedReesResidueTraceCertificate.shiftedExcessSurvives C
