{-# OPTIONS --safe --cubical --guardedness #-}
module RadarClockBadGrid where
open import Cubical.Foundations.Prelude
open import RadarClockAdmission
bad : ClockCertificate 31 flat-rows
bad = record flat-certificate { quarter-ticks = 7 ; denominator-grid = refl }
