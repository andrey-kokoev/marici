{-# OPTIONS --safe --cubical --guardedness #-}
module RHRegularizedPacketScalarization where

open import Cubical.Foundations.Prelude
open import RHThirdOrderRelativeEndpointPacket

record CommutativeLine {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    Line : Type ℓ
    _⊗_ : Line → Line → Line
    assoc : (x y z : Line) → (x ⊗ y) ⊗ z ≡ x ⊗ (y ⊗ z)
    comm : (x y : Line) → x ⊗ y ≡ y ⊗ x

open CommutativeLine public

-- The only rearrangement needed to multiply pointwise characters.
interchange : {ℓ : Level} (L : CommutativeLine {ℓ}) →
  (a b c d : Line L) →
  _⊗_ L (_⊗_ L a b) (_⊗_ L c d) ≡
  _⊗_ L (_⊗_ L a c) (_⊗_ L b d)
interchange L a b c d =
  assoc L a b (_⊗_ L c d) ∙
  cong (_⊗_ L a) (sym (assoc L b c d)) ∙
  cong (λ x → _⊗_ L a (_⊗_ L x d)) (comm L b c) ∙
  cong (_⊗_ L a) (assoc L c b d) ∙
  sym (assoc L a c (_⊗_ L b d))

record ComponentCharacter {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ})
  (L : CommutativeLine {ℓ}) : Type (ℓ-suc ℓ) where
  field
    character : Value R → Line L
    multiplicative : (x y : Value R) →
      character (combine R x y) ≡
      _⊗_ L (character x) (character y)

open ComponentCharacter public

record RegularizedFiveCharacters {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ})
  (L : CommutativeLine {ℓ}) : Type (ℓ-suc ℓ) where
  field
    primitiveCharacter squareCharacter connectedCharacter seamCharacter
      archimedeanCharacter : ComponentCharacter R L

open RegularizedFiveCharacters public

record PacketCharacter {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ})
  (L : CommutativeLine {ℓ}) : Type (ℓ-suc ℓ) where
  field
    packetCharacter : EndpointPacketValue (Value R) → Line L
    packetMultiplicative : (x y : EndpointPacketValue (Value R)) →
      packetCharacter (combinePacket R x y) ≡
      _⊗_ L (packetCharacter x) (packetCharacter y)

open PacketCharacter public

liftComponent : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}} {L : CommutativeLine {ℓ}} →
  (projection : EndpointPacketValue (Value R) → Value R) →
  ((x y : EndpointPacketValue (Value R)) →
    projection (combinePacket R x y) ≡ combine R (projection x) (projection y)) →
  ComponentCharacter R L → PacketCharacter R L
liftComponent {R = R} projection preserves F = record
  { packetCharacter = λ x → character F (projection x)
  ; packetMultiplicative = λ x y →
      cong (character F) (preserves x y) ∙ multiplicative F (projection x) (projection y)
  }

productPacketCharacter : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}} {L : CommutativeLine {ℓ}} →
  PacketCharacter R L → PacketCharacter R L → PacketCharacter R L
productPacketCharacter {L = L} F G = record
  { packetCharacter = λ x → _⊗_ L (packetCharacter F x) (packetCharacter G x)
  ; packetMultiplicative = λ x y →
      cong₂ (_⊗_ L) (packetMultiplicative F x y)
        (packetMultiplicative G x y) ∙
      interchange L (packetCharacter F x) (packetCharacter F y)
        (packetCharacter G x) (packetCharacter G y)
  }

fiveProduct : {ℓ : Level}
  {R : ThirdOrderRelativeEndpoint {ℓ}} {L : CommutativeLine {ℓ}} →
  RegularizedFiveCharacters R L → PacketCharacter R L
fiveProduct F =
  productPacketCharacter
    (productPacketCharacter
      (productPacketCharacter
        (productPacketCharacter
          (liftComponent primitiveGrade (λ _ _ → refl) (primitiveCharacter F))
          (liftComponent squareGrade (λ _ _ → refl) (squareCharacter F)))
        (liftComponent connectedGrade (λ _ _ → refl) (connectedCharacter F)))
      (liftComponent seamGrade (λ _ _ → refl) (seamCharacter F)))
    (liftComponent archimedeanGrade (λ _ _ → refl) (archimedeanCharacter F))

-- Applying the five characters to their respective packet components gives
-- the regularized scalar determinant candidate.
regularizedScalarization : {ℓ : Level}
  (R : ThirdOrderRelativeEndpoint {ℓ})
  (L : CommutativeLine {ℓ})
  (F : RegularizedFiveCharacters R L) → PacketScalarization R
regularizedScalarization R L F = record
  { Line = Line L
  ; tensor = _⊗_ L
  ; scalarize = packetCharacter (fiveProduct F)
  ; preservesCombination = packetMultiplicative (fiveProduct F)
  }
