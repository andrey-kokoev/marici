{-# OPTIONS --safe --cubical --guardedness #-}
module RadarClockBadEnclosure where
open import Cubical.Foundations.Prelude
open import RadarClockAdmission
open import NativeRadarReadout using (before; center; after; x3; y4; xy5)
bad : ClockCertificate 31 flat-rows
bad = record flat-certificate
  { below = λ _ _ → 1
  ; inside-lower = λ { before x3 → refl ; before y4 → refl ; before xy5 → refl
                    ; center x3 → refl ; center y4 → refl ; center xy5 → refl
                    ; after x3 → refl ; after y4 → refl ; after xy5 → refl }
  }
