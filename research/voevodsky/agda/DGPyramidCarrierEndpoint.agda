{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidCarrierEndpoint where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Proof boundary for the completed occurrence-weighted carrier endpoint square.
-- Its connectors are intentionally not called physical connectors.
record CarrierEndpointCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    ChainOne ChainZero Coeff : Type ℓ
    boundary : ChainOne → ChainZero
    scaleZero : Coeff → ChainZero → ChainZero
    differenceZero : ChainZero → ChainZero → ChainZero

    midpoint positiveEndpoint negativeEndpoint : ChainZero
    midpointWeight positiveWeight negativeWeight : Coeff
    positiveHomotopy negativeHomotopy : ChainOne
    positiveEndpointEquation : boundary positiveHomotopy ≡
      differenceZero (scaleZero midpointWeight midpoint)
        (scaleZero positiveWeight positiveEndpoint)
    negativeEndpointEquation : boundary negativeHomotopy ≡
      differenceZero (scaleZero midpointWeight midpoint)
        (scaleZero negativeWeight negativeEndpoint)

    RelativeGenerator RelativeImage : Type ℓ
    exceptionalGenerator : RelativeGenerator
    carrierImage : RelativeGenerator → RelativeImage
    zeroRelativeImage : RelativeImage
    exceptionalImageNonzero :
      carrierImage exceptionalGenerator ≡ zeroRelativeImage → ⊥

    -- Exhaustive coefficient classification L = (mu). Divisibility and
    -- admissibility are packet-defined polynomial notions, not scalar fitting.
    Divides : Coeff → Coeff → Type ℓ
    AdmissibleEndpointSquare : Coeff → Type ℓ
    admissibleImpliesMidpointDivides : (k : Coeff) →
      AdmissibleEndpointSquare k → Divides midpointWeight k
    midpointDividesImpliesAdmissible : (k : Coeff) →
      Divides midpointWeight k → AdmissibleEndpointSquare k
    one : Coeff
    midpointDoesNotDivideOne : Divides midpointWeight one → ⊥

open CarrierEndpointCertificate public

unitCollapsedSquareImpossible : {ℓ : Level}
  (C : CarrierEndpointCertificate {ℓ}) →
  AdmissibleEndpointSquare C (one C) → ⊥
unitCollapsedSquareImpossible C square =
  midpointDoesNotDivideOne C
    (admissibleImpliesMidpointDivides C (one C) square)

-- Carrier and physical connector types remain nominally separated. A future
-- mixed-variance mate may provide this bridge; none is derivable here.
record PhysicalConnectorBridge {ℓ : Level}
  (C : CarrierEndpointCertificate {ℓ}) : Type (ℓ-suc ℓ) where
  field
    PhysicalPlusConnector PhysicalMinusConnector : Type ℓ
    carrierPlusToPhysical : ChainOne C → PhysicalPlusConnector
    carrierMinusToPhysical : ChainOne C → PhysicalMinusConnector
    plusCompatibility : PhysicalPlusConnector → Type ℓ
    minusCompatibility : PhysicalMinusConnector → Type ℓ
    plusWitness : plusCompatibility
      (carrierPlusToPhysical (positiveHomotopy C))
    minusWitness : minusCompatibility
      (carrierMinusToPhysical (negativeHomotopy C))

-- No PhysicalConnectorBridge constructor is exported.
