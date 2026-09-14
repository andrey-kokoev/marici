{-# OPTIONS --safe --cubical --guardedness #-}
module RHFormalization where

-- Audited RH dependency surface.  Importing this module checks the complete
-- current formal chain, including the explicit physical-promotion boundary.
open import RHThetaTailEndpointMateSquare public
open import RHThetaSixNormalIncidenceAudit public
open import RHThetaTailSixNormalInterface public
open import RHThirdOrderRelativeEndpointPacket public
open import RHReciprocalChartDeterminantCarrier public
open import RHRegularizedPacketScalarization public
open import RHThetaBoundaryConservation public
open import RHBoundaryConservationIndependence public
open import RHSectionBoundaryReadout public
open import RHPhysicalRecollementRealization public
open import RHCR1PromotionBoundary public
open import RHCR1WitnessAssembly public
open import RHCR1GalleryQNoGo public
open import RHCR1KatoSupportBridge public
open import RHThreeStratumWeylResponse public
open import RHPrimeShellResidualBoundary public

-- Status encoded by the imported types:
--
--   ThirdOrderRelativeEndpoint
--     -> ReciprocalChartCarrier
--     -> DistinguishedThetaSection
--     -> PhysicalRecollementRealization
--     -> ThetaBoundaryConservation
--     -> theta-zero implies transverse-zero.
--
-- The first three layers are structural inputs.  The physical realization is
-- not synthesized by the formal chain: CR1ProperBaseChangePromotion carries
-- a separate Authority type, and closedCR1Promotion instantiates the current
-- repository gate with Lift bottom.  RHCR1GalleryQNoGo additionally proves
-- that the certified F1-supported marked gallery cannot supply the required
-- nonzero costalk unit through ordinary relative-Q projection.  A successful
-- support witness must therefore use a genuinely extraordinary specialization.
-- Consequently importing this umbrella cannot manufacture the missing
-- physical theorem.
