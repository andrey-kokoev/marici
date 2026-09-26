{-# OPTIONS --safe --cubical --guardedness #-}
module RadarOutputBadDelay where
open import Cubical.Foundations.Prelude
open import NativeRadarReadout using (before; center; after; x3; y4; xy5)
open import RadarClockPhysicalCertificates
open import RadarOutputEnclosure
open import RadarOutputPhysicalCertificates
bad : DelayCertificate wave-certificate
bad = record wave-delays
  { low-delay = λ _ _ → 0
  ; lower-shift = λ { before x3 → refl ; before y4 → refl ; before xy5 → refl
                   ; center x3 → refl ; center y4 → refl ; center xy5 → refl
                   ; after x3 → refl ; after y4 → refl ; after xy5 → refl }
  }
