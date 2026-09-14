{-# OPTIONS --safe --cubical --guardedness #-}
module RHThirdOrderRelativeEndpointPacket where

open import Cubical.Foundations.Prelude
open import RHThetaTailEndpointMateSquare

-- The five components required before a relative determinant can be formed.
record EndpointPacketValue {ℓ : Level} (Value : Type ℓ) : Type ℓ where
  constructor packet
  field
    primitiveGrade squareGrade connectedGrade seamGrade archimedeanGrade : Value

open EndpointPacketValue public

record ThirdOrderRelativeEndpoint {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    thetaTail : ThetaTailCorrespondence {ℓ}
    Scale Value : Type ℓ
    _⊕_ : Scale → Scale → Scale
    scaleCommutes : (a b : Scale) → a ⊕ b ≡ b ⊕ a
    translate : Scale → Tail thetaTail → Tail thetaTail
    combine : Value → Value → Value

    primitiveCurrent squareCurrent connectedTail seamInterval
      archimedeanCountercurrent : Tail thetaTail → Scale → Value

    primitiveCocycle : (G : Tail thetaTail) (a b : Scale) →
      combine (primitiveCurrent G a) (primitiveCurrent (translate a G) b)
        ≡ primitiveCurrent G (a ⊕ b)
    squareCocycle : (G : Tail thetaTail) (a b : Scale) →
      combine (squareCurrent G a) (squareCurrent (translate a G) b)
        ≡ squareCurrent G (a ⊕ b)
    connectedCocycle : (G : Tail thetaTail) (a b : Scale) →
      combine (connectedTail G a) (connectedTail (translate a G) b)
        ≡ connectedTail G (a ⊕ b)
    seamCocycle : (G : Tail thetaTail) (a b : Scale) →
      combine (seamInterval G a) (seamInterval (translate a G) b)
        ≡ seamInterval G (a ⊕ b)
    archimedeanCocycle : (G : Tail thetaTail) (a b : Scale) →
      combine (archimedeanCountercurrent G a)
        (archimedeanCountercurrent (translate a G) b)
        ≡ archimedeanCountercurrent G (a ⊕ b)

open ThirdOrderRelativeEndpoint public

endpointPacket : {ℓ : Level} (R : ThirdOrderRelativeEndpoint {ℓ}) →
  Tail (thetaTail R) → Scale R → EndpointPacketValue (Value R)
endpointPacket R G a = packet
  (primitiveCurrent R G a)
  (squareCurrent R G a)
  (connectedTail R G a)
  (seamInterval R G a)
  (archimedeanCountercurrent R G a)

combinePacket : {ℓ : Level} (R : ThirdOrderRelativeEndpoint {ℓ}) →
  EndpointPacketValue (Value R) → EndpointPacketValue (Value R) →
  EndpointPacketValue (Value R)
combinePacket R x y = packet
  (combine R (primitiveGrade x) (primitiveGrade y))
  (combine R (squareGrade x) (squareGrade y))
  (combine R (connectedGrade x) (connectedGrade y))
  (combine R (seamGrade x) (seamGrade y))
  (combine R (archimedeanGrade x) (archimedeanGrade y))

-- All five source components compose before determinant scalarization.
packetCocycle : {ℓ : Level} (R : ThirdOrderRelativeEndpoint {ℓ}) →
  (G : Tail (thetaTail R)) (a b : Scale R) →
  combinePacket R (endpointPacket R G a)
    (endpointPacket R (translate R a G) b)
  ≡ endpointPacket R G (_⊕_ R a b)
packetCocycle R G a b i = packet
  (primitiveCocycle R G a b i)
  (squareCocycle R G a b i)
  (connectedCocycle R G a b i)
  (seamCocycle R G a b i)
  (archimedeanCocycle R G a b i)

-- The determinant-line lift is deliberately separate: packet coherence alone
-- does not manufacture multiplicativity or completion control.
record RelativeDeterminantLift {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ}) : Type (ℓ-suc ℓ) where
  field
    Line : Type ℓ
    tensor : Line → Line → Line
    determinant : EndpointPacketValue (Value R) → Line
    determinantMultiplicative :
      (x y : EndpointPacketValue (Value R)) →
      determinant (combinePacket R x y) ≡
      tensor (determinant x) (determinant y)

open RelativeDeterminantLift public

-- The packet itself is the universal multiplicative target.  This is not a
-- scalar determinant line; it records that no information need be discarded
-- before regularized scalarization.
packetIdentityLift : {ℓ : Level} (R : ThirdOrderRelativeEndpoint {ℓ}) →
  RelativeDeterminantLift R
packetIdentityLift R = record
  { Line = EndpointPacketValue (Value R)
  ; tensor = combinePacket R
  ; determinant = λ x → x
  ; determinantMultiplicative = λ x y → refl
  }

-- A genuine line-valued construction is exactly a multiplicative
-- scalarization of the universal packet target.
record PacketScalarization {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ}) : Type (ℓ-suc ℓ) where
  field
    Line : Type ℓ
    tensor : Line → Line → Line
    scalarize : EndpointPacketValue (Value R) → Line
    preservesCombination :
      (x y : EndpointPacketValue (Value R)) →
      scalarize (combinePacket R x y) ≡ tensor (scalarize x) (scalarize y)

open PacketScalarization public

scalarizationGivesDeterminantLift : {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ}) →
  PacketScalarization R → RelativeDeterminantLift R
scalarizationGivesDeterminantLift R S = record
  { Line = PacketScalarization.Line S
  ; tensor = PacketScalarization.tensor S
  ; determinant = scalarize S
  ; determinantMultiplicative = preservesCombination S
  }

-- A lawful lift turns the packet cocycle into determinant concatenation.
determinantConcatenation : {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ})
  (D : RelativeDeterminantLift R)
  (G : Tail (thetaTail R)) (a b : Scale R) →
  tensor D
    (determinant D (endpointPacket R G a))
    (determinant D (endpointPacket R (translate R a G) b))
  ≡ determinant D (endpointPacket R G (_⊕_ R a b))
determinantConcatenation R D G a b =
  sym (determinantMultiplicative D _ _) ∙
  cong (determinant D) (packetCocycle R G a b)
