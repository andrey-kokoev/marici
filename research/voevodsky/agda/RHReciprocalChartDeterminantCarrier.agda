{-# OPTIONS --safe --cubical --guardedness #-}
module RHReciprocalChartDeterminantCarrier where

open import Cubical.Foundations.Prelude
open import RHThetaTailEndpointMateSquare using (Tail)
open import RHThirdOrderRelativeEndpointPacket

-- Primitive and square currents are not required to continue as independent
-- global characters.  Scalarization is chartwise on the complete packet.
record ReciprocalChartCarrier {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ}) : Type (ℓ-suc ℓ) where
  field
    plusChart minusChart overlapDomain : Type ℓ
    restrictPlus : plusChart → overlapDomain
    restrictMinus : minusChart → overlapDomain

    plusScalarization minusScalarization : PacketScalarization R
    commonLine : Type ℓ
    plusToCommon : PacketScalarization.Line plusScalarization → commonLine
    minusToCommon : PacketScalarization.Line minusScalarization → commonLine

    connectedTransition connectedTransitionInverse :
      overlapDomain → commonLine → commonLine
    transitionUnit : overlapDomain → commonLine
    transitionRoundTrip : (z : overlapDomain) (x : commonLine) →
      connectedTransitionInverse z (connectedTransition z x) ≡ x

    -- The whole packets glue after the determinant-three transition.  No
    -- separate continuation of primitive or square coordinates is assumed.
    packetGluing : (p : EndpointPacketValue (Value R))
      (u : plusChart) (v : minusChart) →
      restrictPlus u ≡ restrictMinus v →
      connectedTransition (restrictPlus u)
        (minusToCommon
          (PacketScalarization.scalarize minusScalarization p))
      ≡ plusToCommon
          (PacketScalarization.scalarize plusScalarization p)

open ReciprocalChartCarrier public

-- A distinguished theta section is extra data over the nowhere-zero carrier.
-- Carrier invertibility alone provides no inhabitant or nonvanishing theorem
-- for this section.
record DistinguishedThetaSection {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R) : Type (ℓ-suc ℓ) where
  field
    Parameter : Type ℓ
    section : Parameter → commonLine C
    reciprocal : Parameter → Parameter
    reciprocalLaw : (s : Parameter) → section (reciprocal s) ≡ section s

open DistinguishedThetaSection public

-- Local determinant concatenation remains available on either complete chart.
plusConcatenation : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}}
  (C : ReciprocalChartCarrier R)
  (G : Tail (thetaTail R)) (a b : Scale R) →
  PacketScalarization.tensor (plusScalarization C)
    (PacketScalarization.scalarize (plusScalarization C)
      (endpointPacket R G a))
    (PacketScalarization.scalarize (plusScalarization C)
      (endpointPacket R (translate R a G) b))
  ≡ PacketScalarization.scalarize (plusScalarization C)
      (endpointPacket R G (_⊕_ R a b))
plusConcatenation C =
  determinantConcatenation _
    (scalarizationGivesDeterminantLift _ (plusScalarization C))
