{-# OPTIONS --safe --cubical --guardedness #-}
module DGPyramidReesResonance where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Empty using (⊥)

-- Branch-A Rees-weighted filling variation and its next coherence obstruction.
record ReesResonanceCertificate {ℓ : Level} : Type (ℓ-suc ℓ) where
  field
    FineWeight Coeff ChainOne ChainTwo ChainThree ChainFour QTwo Endpoint : Type ℓ
    resonanceWeight compatibilityWeight : FineWeight
    zeroOne : ChainOne
    zeroTwo : ChainTwo
    zeroThree : ChainThree
    zeroEndpoint : Endpoint
    d21 : ChainTwo → ChainOne
    d32 : ChainThree → ChainTwo
    d43 : ChainFour → ChainThree
    scaleTwo : Coeff → ChainTwo → ChainTwo
    scaleThree : Coeff → ChainThree → ChainThree
    differenceThree : ChainThree → ChainThree → ChainThree

    omega03 : ChainTwo
    omega03Closed : d21 omega03 ≡ zeroOne
    omega03Nonzero : omega03 ≡ zeroTwo → ⊥
    projectQ : ChainTwo → QTwo
    expectedQVariation : QTwo
    omega03QImage : projectQ omega03 ≡ expectedQVariation
    endpointOfTwo : ChainTwo → Endpoint
    omega03EndpointZero : endpointOfTwo omega03 ≡ zeroEndpoint

    u03 mu : Coeff
    Wu Wmu : ChainThree
    WuBoundary : d32 Wu ≡ scaleTwo u03 omega03
    WmuBoundary : d32 Wmu ≡ scaleTwo mu omega03

    theta03 : ChainThree
    thetaDefinition : theta03 ≡
      differenceThree (scaleThree u03 Wmu) (scaleThree mu Wu)
    theta03Closed : d32 theta03 ≡ zeroTwo
    theta03Nonzero : theta03 ≡ zeroThree → ⊥

    -- Exact annihilator classification over the stated normal/Rees subring.
    InAnnihilatorIdeal : Coeff → Type ℓ
    KillsOmega03 : Coeff → Type ℓ
    annihilatorNecessary : (c : Coeff) →
      KillsOmega03 c → InAnnihilatorIdeal c
    annihilatorSufficient : (c : Coeff) →
      InAnnihilatorIdeal c → KillsOmega03 c

    endpointOfThree : ChainThree → Endpoint
    WuEndpointZero : endpointOfThree Wu ≡ zeroEndpoint
    -- Wmu and theta endpoint values are retained rather than required zero.
    WmuEndpoint ThetaEndpoint : Endpoint
    WmuEndpointEquation : endpointOfThree Wmu ≡ WmuEndpoint
    thetaEndpointEquation : endpointOfThree theta03 ≡ ThetaEndpoint

    -- The secondary compatibility is not the boundary of a next filler.
    thetaNotBoundary : (K : ChainFour) → d43 K ≡ theta03 → ⊥

open ReesResonanceCertificate public

noFourthCoherence : {ℓ : Level} (C : ReesResonanceCertificate {ℓ}) →
  (Σ (ChainFour C) λ K → d43 C K ≡ theta03 C) → ⊥
noFourthCoherence C (K , boundary) = thetaNotBoundary C K boundary

-- A bottom endpoint-zero statement does not erase endpoint data at the two
-- higher coherence levels; those values remain explicit fields.
