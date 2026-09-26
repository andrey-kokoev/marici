{-# OPTIONS --safe --cubical --guardedness #-}
module RadarClockBadBudget where
open import Cubical.Foundations.Prelude
open import RadarClockAdmission
open import RadarClockPhysicalCertificates
open import NativeRadarReadout using (before; center; after; x3; y4; xy5)
bad : ClockCertificate 1208925819614629174706175 wave-rows
bad = record wave-certificate
  { error-budget = 0
  ; within-budget = λ { before x3 → refl ; before y4 → refl ; before xy5 → refl
                     ; center x3 → refl ; center y4 → refl ; center xy5 → refl
                     ; after x3 → refl ; after y4 → refl ; after xy5 → refl }
  }
