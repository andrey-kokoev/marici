{-# OPTIONS --safe --cubical --guardedness #-}
module BoundaryPfaffianFluxMomentQuotient where

open import Cubical.Foundations.Prelude
open import Cubical.Algebra.CommRing
open import Cubical.Tactics.CommRingSolver

module FluxMoments {ℓ} (R : CommRing ℓ) where
  open CommRingStr (snd R)
  Carrier = fst R

  -- Each labelled flux stores its reciprocal and direct position weights.
  -- No division or positivity is required by the algebraic quotient.
  data FluxFamily : Type ℓ where
    noFlux : FluxFamily
    seam : Carrier → Carrier → Carrier → FluxFamily → FluxFamily

  minusMoment : FluxFamily → Carrier
  minusMoment noFlux = 0r
  minusMoment (seam yInv y flux X) = flux · yInv + minusMoment X

  plusMoment : FluxFamily → Carrier
  plusMoment noFlux = 0r
  plusMoment (seam yInv y flux X) = flux · y + plusMoment X

  record EndpointDouble : Type ℓ where
    field
      minus plus : Carrier

  open EndpointDouble public

  observeEndpoints : FluxFamily → EndpointDouble
  observeEndpoints X = record
    { minus = minusMoment X
    ; plus = plusMoment X
    }

  swapEndpoints : EndpointDouble → EndpointDouble
  swapEndpoints q = record { minus = plus q ; plus = minus q }

  reflectFluxes : FluxFamily → FluxFamily
  reflectFluxes noFlux = noFlux
  reflectFluxes (seam yInv y flux X) =
    seam y yInv flux (reflectFluxes X)

  reflectionInvolutive : (X : FluxFamily) →
    reflectFluxes (reflectFluxes X) ≡ X
  reflectionInvolutive noFlux = refl
  reflectionInvolutive (seam yInv y flux X) =
    cong (seam yInv y flux) (reflectionInvolutive X)

  minusAfterReflection : (X : FluxFamily) →
    minusMoment (reflectFluxes X) ≡ plusMoment X
  minusAfterReflection noFlux = refl
  minusAfterReflection (seam yInv y flux X) =
    cong (flux · y +_) (minusAfterReflection X)

  plusAfterReflection : (X : FluxFamily) →
    plusMoment (reflectFluxes X) ≡ minusMoment X
  plusAfterReflection noFlux = refl
  plusAfterReflection (seam yInv y flux X) =
    cong (flux · yInv +_) (plusAfterReflection X)

  observationReflectsBySwap : (X : FluxFamily) →
    observeEndpoints (reflectFluxes X) ≡
    swapEndpoints (observeEndpoints X)
  observationReflectsBySwap X i = record
    { minus = minusAfterReflection X i
    ; plus = plusAfterReflection X i
    }

  rescaleFluxes : Carrier → Carrier → FluxFamily → FluxFamily
  rescaleFluxes zInv z noFlux = noFlux
  rescaleFluxes zInv z (seam yInv y flux X) =
    seam (zInv · yInv) (z · y) flux (rescaleFluxes zInv z X)

  minusAfterRescale : (zInv z : Carrier) (X : FluxFamily) →
    minusMoment (rescaleFluxes zInv z X) ≡ zInv · minusMoment X
  minusAfterRescale zInv z noFlux = solve! R
  minusAfterRescale zInv z (seam yInv y flux X) =
    cong (flux · (zInv · yInv) +_) (minusAfterRescale zInv z X) ∙
    solve! R

  plusAfterRescale : (zInv z : Carrier) (X : FluxFamily) →
    plusMoment (rescaleFluxes zInv z X) ≡ z · plusMoment X
  plusAfterRescale zInv z noFlux = solve! R
  plusAfterRescale zInv z (seam yInv y flux X) =
    cong (flux · (z · y) +_) (plusAfterRescale zInv z X) ∙
    solve! R

  record MomentKernel (X : FluxFamily) : Type ℓ where
    field
      minusVanishes : minusMoment X ≡ 0r
      plusVanishes : plusMoment X ≡ 0r

  -- The kernel predicate is stable under translation and reflection.
  kernelReflects : (X : FluxFamily) →
    MomentKernel X → MomentKernel (reflectFluxes X)
  kernelReflects X k = record
    { minusVanishes = minusAfterReflection X ∙ MomentKernel.plusVanishes k
    ; plusVanishes = plusAfterReflection X ∙ MomentKernel.minusVanishes k
    }

  kernelRescales : (zInv z : Carrier) (X : FluxFamily) →
    MomentKernel X → MomentKernel (rescaleFluxes zInv z X)
  kernelRescales zInv z X k = record
    { minusVanishes = minusAfterRescale zInv z X ∙
        cong (zInv ·_) (MomentKernel.minusVanishes k) ∙ solve! R
    ; plusVanishes = plusAfterRescale zInv z X ∙
        cong (z ·_) (MomentKernel.plusVanishes k) ∙ solve! R
    }
