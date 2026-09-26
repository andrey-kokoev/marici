{-# OPTIONS --safe --cubical --guardedness #-}
module RadarClockAdmission where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat.Base using (ℕ; suc; _+_; _·_)
open import Cubical.Data.Int.Base using (pos)
open import NativeRadarReadout using
  (Time; before; center; after; Direction; x3; y4; xy5;
   Rows; ClockPair; clocks; Calibration; frozen-calibration)
import NativeRadarReadout as Radar

slot : Time → ℕ
slot before = 3
slot center = 4
slot after = 5
Grid : Type
Grid = Time → Direction → ℕ

-- These are arithmetic certificates, not witnesses of any spacetime metric.
record ClockCertificate (k : ℕ) (r : Rows) : Type where
  field
    calibration : Calibration
    calibration-fixed : calibration ≡ frozen-calibration
    quarter-ticks : ℕ
    denominator-grid : suc k ≡ 4 · quarter-ticks
    arrival : Grid
    row-grid : (t : Time) (d : Direction)
      → r t d ≡ clocks (pos (slot t · quarter-ticks)) (pos (arrival t d))
    delay-minus-one : Grid
    causal : (t : Time) (d : Direction)
      → arrival t d ≡ slot t · quarter-ticks + suc (delay-minus-one t d)
    -- All enclosure integers use denominator (suc k)*(suc refinement).
    refinement : ℕ
    lower upper below above width : Grid
    inside-lower : (t : Time) (d : Direction)
      → lower t d + below t d ≡ suc refinement · arrival t d
    inside-upper : (t : Time) (d : Direction)
      → suc refinement · arrival t d + above t d ≡ upper t d
    width-exact : (t : Time) (d : Direction)
      → upper t d ≡ lower t d + width t d
    error-budget : ℕ
    slack : Grid
    within-budget : (t : Time) (d : Direction)
      → width t d + slack t d ≡ error-budget
open ClockCertificate public

module FiniteChecked (k : ℕ) (r : Rows) (certificate : ClockCertificate k r) where
  module Native = Radar.Admitted ClockCertificate k r certificate
  -- This is the actual retained-resolution interface with concrete finite admission.
  retained-readout-commutes = Native.retained-readout-commutes
  marked-radar-reading = Native.marked-radar-reading
  history-recovered = Native.history-recovered

-- Physical realization remains a SEPARATE supplied predicate on a certificate.
-- No constructor below turns a source string/hash into its inhabitant.
module WithPhysical
  (Physical : (k : ℕ) (r : Rows) → ClockCertificate k r → Type) where
  Admission : ℕ → Rows → Type
  Admission k r = Σ (ClockCertificate k r) (Physical k r)
  module Checked (k : ℕ) (r : Rows) (c : ClockCertificate k r) (p : Physical k r c) where
    module Native = Radar.Admitted Admission k r (c , p)

-- Fully checked nonempty finite admission: static flat reference, D=32.
-- Its physical identification is supplied by the existing analytic source note.
lag : Direction → ℕ
lag x3 = 6
lag y4 = 8
lag xy5 = 10
lag-minus-one : Direction → ℕ
lag-minus-one x3 = 5
lag-minus-one y4 = 7
lag-minus-one xy5 = 9
flat-arrival : Grid
flat-arrival t d = slot t · 8 + lag d
flat-rows : Rows
flat-rows t d = clocks (pos (slot t · 8)) (pos (flat-arrival t d))
flat-certificate : ClockCertificate 31 flat-rows
calibration flat-certificate = frozen-calibration
calibration-fixed flat-certificate = refl
quarter-ticks flat-certificate = 8
denominator-grid flat-certificate = refl
arrival flat-certificate = flat-arrival
row-grid flat-certificate t d = refl
delay-minus-one flat-certificate t d = lag-minus-one d
causal flat-certificate t x3 = refl
causal flat-certificate t y4 = refl
causal flat-certificate t xy5 = refl
refinement flat-certificate = 0
lower flat-certificate = flat-arrival
upper flat-certificate = flat-arrival
below flat-certificate _ _ = 0
above flat-certificate _ _ = 0
width flat-certificate _ _ = 0
inside-lower flat-certificate before x3 = refl
inside-lower flat-certificate before y4 = refl
inside-lower flat-certificate before xy5 = refl
inside-lower flat-certificate center x3 = refl
inside-lower flat-certificate center y4 = refl
inside-lower flat-certificate center xy5 = refl
inside-lower flat-certificate after x3 = refl
inside-lower flat-certificate after y4 = refl
inside-lower flat-certificate after xy5 = refl
inside-upper flat-certificate before x3 = refl
inside-upper flat-certificate before y4 = refl
inside-upper flat-certificate before xy5 = refl
inside-upper flat-certificate center x3 = refl
inside-upper flat-certificate center y4 = refl
inside-upper flat-certificate center xy5 = refl
inside-upper flat-certificate after x3 = refl
inside-upper flat-certificate after y4 = refl
inside-upper flat-certificate after xy5 = refl
width-exact flat-certificate before x3 = refl
width-exact flat-certificate before y4 = refl
width-exact flat-certificate before xy5 = refl
width-exact flat-certificate center x3 = refl
width-exact flat-certificate center y4 = refl
width-exact flat-certificate center xy5 = refl
width-exact flat-certificate after x3 = refl
width-exact flat-certificate after y4 = refl
width-exact flat-certificate after xy5 = refl
error-budget flat-certificate = 0
slack flat-certificate _ _ = 0
within-budget flat-certificate _ _ = refl
module Flat = FiniteChecked 31 flat-rows flat-certificate
