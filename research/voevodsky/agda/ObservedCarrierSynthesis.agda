{-# OPTIONS --safe --cubical --guardedness #-}
module ObservedCarrierSynthesis where
open import Cubical.Foundations.Prelude
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Data.Empty.Base using (⊥)
open import Cubical.Data.Int.Base using (ℤ; pos; _-_; _+_; _·_)
open import Cubical.Data.Int.Properties using (posNotnegsuc)
import NewtonianTidalKernel as J
import NativeTidalTableReadout as NT
import NewtonianTidalRoutes as OldTidal
import NativeRadarReadout as Radar
import RadarClockAdmission as Clocks
import TableFibrationCycle as Table

-- This interface compares fixed numeric payload strata. It does not assign
-- a topology to all Code, erase admission witnesses or identify source laws.
record Carrier (X Y : Type) : Type where
  field
    encode : X → Y
    decode : Y → X
    source-roundtrip : (x : X) → decode (encode x) ≡ x
    native-roundtrip : (y : Y) → encode (decode y) ≡ y
record Observed {X Y : Type} (E : Carrier X Y) (O : Type) : Type where
  field
    source : X → O
    native : Y → O
    compares : (x : X) → native (Carrier.encode E x) ≡ source x

joint : {X Y U V : Type} {E : Carrier X Y}
  → Observed E U → Observed E V → Observed E (U × V)
Observed.source (joint a b) x = Observed.source a x , Observed.source b x
Observed.native (joint a b) y = Observed.native a y , Observed.native b y
Observed.compares (joint a b) x i = Observed.compares a x i , Observed.compares b x i

preserves-distinction : {X Y O : Type} {E : Carrier X Y} (a : Observed E O)
  → (x y : X) → (Observed.source a x ≡ Observed.source a y → ⊥)
  → Observed.native a (Carrier.encode E x) ≡ Observed.native a (Carrier.encode E y) → ⊥
preserves-distinction a x y different same = different
  (sym (Observed.compares a x) ∙ same ∙ Observed.compares a y)

no-forgetting : {X Y O W : Type} {E : Carrier X Y} (a : Observed E O)
  → (forget : X → W) (x y : X) → forget x ≡ forget y
  → (Observed.source a x ≡ Observed.source a y → ⊥)
  → (f : W → O) → ((z : X) → f (forget z) ≡ Observed.source a z) → ⊥
no-forgetting a forget x y forgotten different f law =
  different (sym (law x) ∙ cong f forgotten ∙ law y)

-- Instance 1: the actual Newtonian jet and the owner's thirteen native rows.
jet-encode : J.Jet → NT.JetTable
jet-encode j NT.scalar = J.potential j
jet-encode j (NT.first i) = J.gradient j i
jet-encode j (NT.second i k) = J.hessian j i k
jet-decode : NT.JetTable → J.Jet
jet-decode f = J.jet (f NT.scalar) (λ i → f (NT.first i)) (λ i k → f (NT.second i k))
jet-carrier : Carrier J.Jet NT.JetTable
Carrier.encode jet-carrier = jet-encode
Carrier.decode jet-carrier = jet-decode
Carrier.source-roundtrip jet-carrier j = refl
Carrier.native-roundtrip jet-carrier f = funExt λ { NT.scalar → refl ; (NT.first i) → refl ; (NT.second i k) → refl }
jet-reading : Observed jet-carrier J.Tensor
Observed.source jet-reading = J.hessian
Observed.native jet-reading = NT.read-tensor
Observed.compares jet-reading j = refl

-- Link the instance to the owner's nontrivial supplied physical fixture and
-- actual package/history comparison, not just an invented zero payload.
actual-tidal-reading : Observed.native jet-reading NT.native-jet ≡ OldTidal.geometric8
actual-tidal-reading = NT.to-geometric
actual-tidal-package = NT.ad-package-commutes
actual-tidal-history = NT.actual-history-recovered
first-jet-loss = NT.no-first-jet-factor

-- Instance 2: the actual radar rows and an independently read selected-row table.
RadarSection : Type
RadarSection = Radar.Port → Radar.ClockPair
radar-carrier : Carrier Radar.Rows RadarSection
Carrier.encode radar-carrier r p = r (fst p) (snd p)
Carrier.decode radar-carrier f t d = f (t , d)
Carrier.source-roundtrip radar-carrier r = refl
Carrier.native-roundtrip radar-carrier f = refl
native-radar-table : RadarSection → Table.Table Radar.ClockPair Radar.Time Radar.Port
native-radar-table f = Table.table Radar.Port f fst (λ p → p)
row-square : RadarSection → Radar.Time → Radar.Direction → ℤ
row-square f t d = let row = Table.Table.label (native-radar-table f) (t , d)
                  in (Radar.ClockPair.reception row - Radar.ClockPair.emission row) ·
                     (Radar.ClockPair.reception row - Radar.ClockPair.emission row)
column : RadarSection → Radar.Direction → ℤ
column f d = row-square f Radar.after d - pos 2 · row-square f Radar.center d + row-square f Radar.before d
section-reading : RadarSection → Radar.Tensor
section-reading f Radar.xx = pos 16 · column f Radar.x3
section-reading f Radar.xy = pos 6 · (column f Radar.xy5 - column f Radar.x3 - column f Radar.y4)
section-reading f Radar.yy = pos 9 · column f Radar.y4
section-is-native : (r : Radar.Rows) (c : Radar.Component)
  → section-reading (Carrier.encode radar-carrier r) c ≡ Radar.native-read r c
section-is-native r Radar.xx = refl
section-is-native r Radar.xy = refl
section-is-native r Radar.yy = refl
radar-reading : Observed radar-carrier Radar.Tensor
Observed.source radar-reading = Radar.source-read
Observed.native radar-reading = section-reading
Observed.compares radar-reading r = funExt (section-is-native r) ∙ Radar.readout-agrees r

-- The existing concrete clock-admitted native package/run is the marked
-- package-level instantiation behind this fixed-payload comparison.
actual-radar-package = Clocks.Flat.Native.source-package-agrees
actual-radar-history = Clocks.Flat.history-recovered

-- An explicit forgetting hostile: same calibrated emission schedule, changed
-- reception. The changed packet is an algebraic candidate, NOT a new vacuum.
changed : Radar.Rows
changed Radar.center Radar.x3 = Radar.clocks (pos 32) (pos 39)
changed t d = Clocks.flat-rows t d
emissions : Radar.Rows → Radar.Time → Radar.Direction → ℤ
emissions r t d = Radar.ClockPair.emission (r t d)
same-emission : (t : Radar.Time) (d : Radar.Direction)
  → emissions Clocks.flat-rows t d ≡ emissions changed t d
same-emission Radar.before d = refl
same-emission Radar.after d = refl
same-emission Radar.center Radar.x3 = refl
same-emission Radar.center Radar.y4 = refl
same-emission Radar.center Radar.xy5 = refl
same-emissions : emissions Clocks.flat-rows ≡ emissions changed
same-emissions = funExt (λ t → funExt (same-emission t))
radar-gap : Radar.source-read Clocks.flat-rows ≡ Radar.source-read changed → ⊥
radar-gap p = posNotnegsuc 0 415 (cong (λ f → f Radar.xx) p)
no-emission-only-readout : (f : (Radar.Time → Radar.Direction → ℤ) → Radar.Tensor)
  → ((r : Radar.Rows) → f (emissions r) ≡ Radar.source-read r) → ⊥
no-emission-only-readout = no-forgetting radar-reading emissions Clocks.flat-rows changed same-emissions radar-gap
