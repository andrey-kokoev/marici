{-# OPTIONS --safe --cubical --guardedness #-}
module RadarClockBadCalibration where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Int.Base using (pos)
open import RadarClockAdmission
import NativeRadarReadout as Radar
bad : ClockCertificate 31 flat-rows
bad = record flat-certificate
  { calibration = Radar.calibration 16 4 (pos 1) Radar.probe-vectors
      Radar.central-proper-time-c1 Radar.instantaneous-return
  ; calibration-fixed = refl
  }
