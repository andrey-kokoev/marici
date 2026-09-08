{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidPhysicalReesGysin where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- The fixed-beta graph is a chain-level specialization.  In particular, none
-- of these fields asserts flat transport of the old homology presentation.
record PhysicalReesGysinTripleCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    SourceCoeff PhysicalCoeff Chain SupportedClass FirstSymbol : Type ℓ
    Endpoint QPacket : Type ℓ

    graph : SourceCoeff → PhysicalCoeff
    beta lambda x03 mu : PhysicalCoeff
    zeroCoeff : PhysicalCoeff
    multiply : PhysicalCoeff → Chain → Chain
    differential : Chain → Chain
    zeroChain : Chain

    omega wu wmu theta fillingPrimitive residual : Chain
    omegaCycle : differential omega ≡ zeroChain
    primitiveFillsOmega : differential fillingPrimitive ≡ omega
    wuNormalForm : wu ≡ multiply lambda (multiply x03 fillingPrimitive)
    addResidual : Chain → Chain → Chain
    wmuWithResidual : wmu ≡ addResidual (multiply mu fillingPrimitive) residual
    residualCycle : differential residual ≡ zeroChain
    thetaNormalForm : theta ≡ multiply lambda (multiply x03 residual)

    supportedPrimary supportedCompatibility zeroSupported : SupportedClass
    primaryOrdinaryGysinVanishes : supportedPrimary ≡ zeroSupported
    compatibilityOrdinaryGysinVanishes :
      supportedCompatibility ≡ zeroSupported

    firstNormalSymbol : Chain → FirstSymbol
    zeroFirstSymbol : FirstSymbol
    fixedCompatibilitySymbolSurvives :
      firstNormalSymbol theta ≡ zeroFirstSymbol → ⊥

    endpointProjection : Chain → Endpoint
    qProjection : Chain → QPacket
    zeroEndpoint : Endpoint
    endpointOfPrimitiveIsZero : endpointProjection fillingPrimitive ≡ zeroEndpoint
    residualEndpointSurvives : endpointProjection residual ≡ zeroEndpoint → ⊥

    -- A coherent replacement may erase compatibility, but is not definitionally
    -- the fixed comparison supplied by the source packet.
    replacementWmu : Chain
    replacementCompatibility : Chain
    replacementCompatibilityZero : replacementCompatibility ≡ zeroChain
    fixedWmuIsNotReplacement : wmu ≡ replacementWmu → ⊥

open PhysicalReesGysinTripleCertificate public

ordinaryGysinVanishingDoesNotKillFixedSymbol : {ℓ : Level}
  (C : PhysicalReesGysinTripleCertificate {ℓ}) →
  firstNormalSymbol C (theta C) ≡ zeroFirstSymbol C → ⊥
ordinaryGysinVanishingDoesNotKillFixedSymbol C =
  fixedCompatibilitySymbolSurvives C

-- The native and occurrence 35 directions remain different factors.  The
-- strict two-term summand retains both its lower class and its upper kernel.
record Occurrence35SummandCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Chain Native35 Occurrence35 Coeff LowerHomology UpperHomology : Type ℓ
    native35 : Native35
    occurrence35 : Occurrence35
    NativeOccurrenceIdentification : Native35 → Occurrence35 → Type ℓ
    factorsAreNotIdentified : NativeOccurrenceIdentification native35 occurrence35 → ⊥

    differential35 : Chain → Chain
    zeroChain35 : Chain
    allMarkedTop differenceCycle : Chain
    replaceNativeByOccurrence : Chain → Chain
    topCycleClosed : differential35 allMarkedTop ≡ zeroChain35
    differenceFormula :
      differenceCycle ≡ replaceNativeByOccurrence allMarkedTop
    differenceClosed : differential35 differenceCycle ≡ zeroChain35

    x35 : Coeff
    scale35 : Coeff → Chain → Chain
    occurrenceHomotopy : Chain → Chain
    homotopySum : Chain → Chain → Chain
    occurrenceHomotopyEquation : (c : Chain) →
      homotopySum (differential35 (occurrenceHomotopy c))
                  (occurrenceHomotopy (differential35 c)) ≡ scale35 x35 c

    upperGenerator lowerGenerator : Chain
    strictSummandDifferential :
      differential35 upperGenerator ≡ scale35 x35 lowerGenerator
    lowerSection : lowerGenerator ≡ differenceCycle
    projectLower : Chain → LowerHomology
    lowerClass : LowerHomology
    zeroLower : LowerHomology
    lowerDetected : projectLower differenceCycle ≡ lowerClass
    lowerNonzero : lowerClass ≡ zeroLower → ⊥

    upperClass : UpperHomology
    zeroUpper : UpperHomology
    upperAnnihilatorSurvives : upperClass ≡ zeroUpper → ⊥

    -- A truncation retaining only the lower quotient is not an equivalence of
    -- the strict summand, since it kills this upper class.
    LowerOnlyModel : Type ℓ
    truncateUpper : UpperHomology → LowerOnlyModel
    zeroLowerOnly : LowerOnlyModel
    truncationKillsUpper : truncateUpper upperClass ≡ zeroLowerOnly

open Occurrence35SummandCertificate public

lowerOnlyTruncationLosesInformation : {ℓ : Level}
  (C : Occurrence35SummandCertificate {ℓ}) →
  truncateUpper C (upperClass C) ≡ zeroLowerOnly C
lowerOnlyTruncationLosesInformation C = truncationKillsUpper C

-- These certificates do not identify the residual first symbol with the
-- independently required conductor--Morse class or construct a spatial mate.
