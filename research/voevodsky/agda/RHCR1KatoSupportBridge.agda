{-# OPTIONS --safe --cubical --guardedness #-}
module RHCR1KatoSupportBridge where

open import Cubical.Foundations.Prelude
open import RHThirdOrderRelativeEndpointPacket
open import RHReciprocalChartDeterminantCarrier
open import RHCR1PromotionBoundary
open import RHCR1WitnessAssembly

-- Exact interpretation boundary for the completed fs/Kato connector.  The
-- executable Kato calculation supplies the primitive class and its local
-- signatures; these fields state what must be proved when interpreting that
-- class in the abstract CR1 carrier and determinant line.
record KatoCR1SupportBridge {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) : Type (ℓ-suc ℓ) where
  field
    katoDistinguishedClass : DistinguishedThetaSection.Parameter S → Carrier F
    katoZeroClass : Carrier F
    katoOpenImage katoClosedImage : Carrier F → commonLine C

    katoProperBaseChange :
      (x : Carrier F) → katoOpenImage x ≡ katoClosedImage x

    katoZeroLine : commonLine C
    katoClosedZero : katoClosedImage katoZeroClass ≡ katoZeroLine

    katoThetaComparison :
      (s : DistinguishedThetaSection.Parameter S) →
      DistinguishedThetaSection.section S s ≡
      katoOpenImage (katoDistinguishedClass s)

open KatoCR1SupportBridge public

-- Once the Kato descent has produced one global connector type, its finite
-- carrier interpretation is diagonal: open, closed, and overlap charts are
-- the same descended object.  This construction carries no physical-line
-- comparison; that remains a separate bridge field below.
diagonalKatoFiniteCarrier : {ℓ : Level} → Type ℓ → FiniteCR1Carrier {ℓ}
diagonalKatoFiniteCarrier K = record
  { Carrier = K
  ; OpenFace = K
  ; ClosedFace = K
  ; Overlap = K
  ; openRestriction = λ x → x
  ; closedRestriction = λ x → x
  ; openToOverlap = λ x → x
  ; closedToOverlap = λ x → x
  ; finiteBeckChevalley = λ x → refl
  ; rotate = λ x → x
  ; reflect = λ x → x
  ; reflectOverlap = λ x → x
  ; rotate³ = λ x → refl
  ; reflect² = λ x → refl
  ; reflectionOpen = λ x → refl
  ; reflectionClosed = λ x → refl
  }

-- Sign-refined determinant-of-cohomology output of the based physical
-- complex.  The distinction between physicalPrimitive and
-- determinantGenerator records the canonical Det(C) ≃ Det(H(C)) step rather
-- than silently treating a homology class as an element of a determinant line.
record KatoDeterminantGenerator {ℓ : Level}
  (KatoLine : Type ℓ) : Type (ℓ-suc ℓ) where
  field
    determinantLine : Type ℓ
    physicalPrimitive : KatoLine
    determinantGenerator : determinantLine
    physicalToDeterminant : KatoLine → determinantLine
    primitiveDeterminantLaw :
      physicalToDeterminant physicalPrimitive ≡ determinantGenerator

open KatoDeterminantGenerator public

-- Interpretation of the primitive Kato line in the determinant line used by
-- the RH chart carrier.  Keeping this map explicit prevents the numerical
-- residue +1 from being silently identified with an abstract commonLine.
record KatoDeterminantLineInterpretation {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (KatoLine : Type ℓ) : Type (ℓ-suc ℓ) where
  field
    toCommonLine : KatoLine → commonLine C
    zeroKatoLine : KatoLine
    interpretedZeroLine : commonLine C
    toCommonLineZero :
      toCommonLine zeroKatoLine ≡ interpretedZeroLine

open KatoDeterminantLineInterpretation public

-- The only project-specific map after determinant-of-cohomology is the
-- normalization from its determinant line to the reciprocal-chart common
-- line.  The physical-to-common map then factors canonically through it.
determinantGeneratorInterpretation : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (K : Type ℓ)
  (G : KatoDeterminantGenerator K)
  (detToCommon : determinantLine G → commonLine C)
  (zeroK : K)
  (zeroCommon : commonLine C)
  (zeroLaw :
    detToCommon (physicalToDeterminant G zeroK) ≡ zeroCommon) →
  KatoDeterminantLineInterpretation C K
determinantGeneratorInterpretation C K G detToCommon zeroK zeroCommon zeroLaw = record
  { toCommonLine = λ x → detToCommon (physicalToDeterminant G x)
  ; zeroKatoLine = zeroK
  ; interpretedZeroLine = zeroCommon
  ; toCommonLineZero = zeroLaw
  }

-- Typed form of the source-bordered Xi comparison.  Its determinant law is
-- the Agda boundary corresponding to det(M_s)=2xi(s); normalization by the
-- chosen common-line frame is included in detToCommon rather than erased.
record XiBorderedEndpointComparison {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (S : DistinguishedThetaSection C)
  (K : Type ℓ)
  (G : KatoDeterminantGenerator K) : Type (ℓ-suc ℓ) where
  field
    distinguishedKatoClass : DistinguishedThetaSection.Parameter S → K
    detToCommon : determinantLine G → commonLine C
    zeroKatoClass : K
    zeroCommonLine : commonLine C
    borderedZeroLaw :
      detToCommon (physicalToDeterminant G zeroKatoClass) ≡ zeroCommonLine
    borderedThetaLaw :
      (s : DistinguishedThetaSection.Parameter S) →
      DistinguishedThetaSection.section S s ≡
      detToCommon
        (physicalToDeterminant G (distinguishedKatoClass s))

open XiBorderedEndpointComparison public

-- For the diagonal descended carrier, one determinant-line interpretation
-- and the theta comparison generate every field of KatoCR1SupportBridge.
diagonalKatoSupportBridge : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (S : DistinguishedThetaSection C)
  (K : Type ℓ)
  (D : KatoDeterminantLineInterpretation C K)
  (distinguished : DistinguishedThetaSection.Parameter S → K)
  (thetaComparison :
    (s : DistinguishedThetaSection.Parameter S) →
    DistinguishedThetaSection.section S s ≡
    toCommonLine D (distinguished s)) →
  KatoCR1SupportBridge C S (diagonalKatoFiniteCarrier K)
diagonalKatoSupportBridge C S K D distinguished thetaComparison = record
  { katoDistinguishedClass = distinguished
  ; katoZeroClass = zeroKatoLine D
  ; katoOpenImage = toCommonLine D
  ; katoClosedImage = toCommonLine D
  ; katoProperBaseChange = λ x → refl
  ; katoZeroLine = interpretedZeroLine D
  ; katoClosedZero = toCommonLineZero D
  ; katoThetaComparison = thetaComparison
  }

katoBridgeGivesCR1SupportWitness : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (S : DistinguishedThetaSection C)
  (F : FiniteCR1Carrier {ℓ}) →
  KatoCR1SupportBridge C S F →
  CR1SupportWitness C S F
katoBridgeGivesCR1SupportWitness C S F K = record
  { distinguishedCarrier = katoDistinguishedClass K
  ; zeroCarrier = katoZeroClass K
  ; openPhysical = katoOpenImage K
  ; closedPhysical = katoClosedImage K
  ; properBaseChange = katoProperBaseChange K
  ; physicalZeroLine = katoZeroLine K
  ; closedZero = katoClosedZero K
  ; sectionComparison = katoThetaComparison K
  }

xiBorderedComparisonGivesSupport : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (S : DistinguishedThetaSection C)
  (K : Type ℓ)
  (G : KatoDeterminantGenerator K) →
  XiBorderedEndpointComparison C S K G →
  CR1SupportWitness C S (diagonalKatoFiniteCarrier K)
xiBorderedComparisonGivesSupport C S K G X =
  katoBridgeGivesCR1SupportWitness C S (diagonalKatoFiniteCarrier K)
    (diagonalKatoSupportBridge C S K D
      (distinguishedKatoClass X) (borderedThetaLaw X))
  where
  D : KatoDeterminantLineInterpretation C K
  D = determinantGeneratorInterpretation C K G
    (detToCommon X) (zeroKatoClass X) (zeroCommonLine X)
    (borderedZeroLaw X)
