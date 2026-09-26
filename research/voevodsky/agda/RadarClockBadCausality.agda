{-# OPTIONS --safe --cubical --guardedness #-}
module RadarClockBadCausality where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (_·_)
open import Cubical.Data.Int.Base using (pos)
open import RadarClockAdmission
open import NativeRadarReadout using (Rows; clocks; before; center; after; x3; y4; xy5; frozen-calibration)
bad-arrival : Grid
bad-arrival before x3 = 23 -- emission is 24: genuinely past reception
bad-arrival t d = flat-arrival t d
bad-rows : Rows
bad-rows t d = clocks (pos (slot t · 8)) (pos (bad-arrival t d))
bad : ClockCertificate 31 bad-rows
bad = record
  { calibration = frozen-calibration ; calibration-fixed = refl
  ; quarter-ticks = 8 ; denominator-grid = refl
  ; arrival = bad-arrival ; row-grid = λ t d → refl
  ; delay-minus-one = λ _ _ → 0
  ; causal = λ { before x3 → refl ; before y4 → refl ; before xy5 → refl
               ; center x3 → refl ; center y4 → refl ; center xy5 → refl
               ; after x3 → refl ; after y4 → refl ; after xy5 → refl }
  ; refinement = 0 ; lower = flat-arrival ; upper = flat-arrival
  ; below = λ _ _ → 0 ; above = λ _ _ → 0 ; width = λ _ _ → 0
  ; inside-lower = inside-lower flat-certificate
  ; inside-upper = inside-upper flat-certificate
  ; width-exact = width-exact flat-certificate
  ; error-budget = 0 ; slack = λ _ _ → 0
  ; within-budget = λ _ _ → refl
  }
