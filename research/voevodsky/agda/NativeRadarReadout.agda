{-# OPTIONS --safe --cubical --guardedness #-}
module NativeRadarReadout where
open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Data.Nat.Base using (ℕ; suc)
open import Cubical.Data.Int.Base using (ℤ; pos; _+_; _-_; _·_)
open import Cubical.Data.Bool.Base using (Bool; true; false)
open import Cubical.Data.Sigma.Base using (_×_)
open import Cubical.Algebra.CommRing.Instances.Int using (ℤCommRing)
open import Cubical.Tactics.CommRingSolver
import WholePackageSigmaPi as Whole
import WholePackageResolution as Legacy
import IndexedConstructorTables as Tables
import NativeTableRules as Rules
import NativeTableResolution as Resolution
import TableFibrationCycle as Kernel
module O = Whole.Universe ℓ-zero
module R = Legacy.Generators ℓ-zero
module G = Tables.Core ℓ-zero
module N = Rules.Native ℓ-zero

data Time : Type where before center after : Time
data Direction : Type where x3 y4 xy5 : Direction
data Component : Type where xx xy yy : Component
record ClockPair : Type where
  constructor clocks
  field emission reception : ℤ
open ClockPair
Rows : Type
Rows = Time → Direction → ClockPair
Tensor : Type
Tensor = Component → ℤ
data ClockConvention : Type where central-proper-time-c1 : ClockConvention
data ReflectionConvention : Type where instantaneous-return : ReflectionConvention
record Calibration : Type where
  constructor calibration
  field
    baseline-denominator proper-step-denominator : ℕ
    proper-center : ℤ
    probes : Direction → ℤ × ℤ
    clock-convention : ClockConvention
    reflection-convention : ReflectionConvention
probe-vectors : Direction → ℤ × ℤ
probe-vectors x3 = pos 3 , pos 0
probe-vectors y4 = pos 0 , pos 4
probe-vectors xy5 = pos 3 , pos 4
frozen-calibration : Calibration
frozen-calibration = calibration 32 4 (pos 1) probe-vectors
  central-proper-time-c1 instantaneous-return
-- If ticks have denominator D>0, actual Y = -2048*numerator/(144*D^2).
-- These are exact numerator comparisons, not an integer scaling equivalence.
square : ℤ → ℤ
square x = x · x
source-q : Rows → Time → Direction → ℤ
source-q r t d = square (reception (r t d) - emission (r t d))
shape : (Direction → ℤ) → Tensor
shape q xx = pos 16 · q x3
shape q xy = pos 6 · (q xy5 - q x3 - q y4)
shape q yy = pos 9 · q y4
temporal : (Time → ℤ) → ℤ
temporal f = f after - pos 2 · f center + f before
source-read : Rows → Tensor
source-read r c = temporal (λ t → shape (source-q r t) c)

-- Native rows expose the actual clock pair at its marked finite port.
Port : Type
Port = Time × Direction
clock-table : Rows → Kernel.Table ClockPair Time Port
clock-table r = Kernel.table Port (λ p → r (fst p) (snd p)) fst (λ p → p)
clock-unique : (r : Rows) → Kernel.UniqueEndpoints (clock-table r)
clock-unique r p q from-eq to-eq = to-eq
native-q : Rows → Time → Direction → ℤ
native-q r t d = let row = Kernel.Table.label (clock-table r) (t , d)
                in (reception row - emission row) · (reception row - emission row)
native-read : Rows → Tensor
native-read r xx = pos 16 · temporal (λ t → native-q r t x3)
native-read r xy = pos 6 · (temporal (λ t → native-q r t xy5)
                        - temporal (λ t → native-q r t x3)
                        - temporal (λ t → native-q r t y4))
native-read r yy = pos 9 · temporal (λ t → native-q r t y4)

-- Arithmetic proof for arbitrary rows, not refl on a zero physical fixture.
linear-xx : (a b c : ℤ) → pos 16 · (a - pos 2 · b + c)
  ≡ pos 16 · a - pos 2 · (pos 16 · b) + pos 16 · c
linear-xx a b c = solve! ℤCommRing
linear-yy : (a b c : ℤ) → pos 9 · (a - pos 2 · b + c)
  ≡ pos 9 · a - pos 2 · (pos 9 · b) + pos 9 · c
linear-yy a b c = solve! ℤCommRing
linear-xy : (a b c d e f g h k : ℤ)
  → pos 6 · ((a - pos 2 · b + c) - (d - pos 2 · e + f) - (g - pos 2 · h + k))
  ≡ pos 6 · (a - d - g) - pos 2 · (pos 6 · (b - e - h)) + pos 6 · (c - f - k)
linear-xy a b c d e f g h k = solve! ℤCommRing
component-agrees : (r : Rows) (c : Component) → native-read r c ≡ source-read r c
component-agrees r xx = linear-xx (source-q r after x3) (source-q r center x3) (source-q r before x3)
component-agrees r yy = linear-yy (source-q r after y4) (source-q r center y4) (source-q r before y4)
component-agrees r xy = linear-xy
  (source-q r after xy5) (source-q r center xy5) (source-q r before xy5)
  (source-q r after x3) (source-q r center x3) (source-q r before x3)
  (source-q r after y4) (source-q r center y4) (source-q r before y4)
readout-agrees : (r : Rows) → native-read r ≡ source-read r
readout-agrees r = funExt (component-agrees r)

-- Genuine Pi/P nodes, not an old-Code annotation or an untyped list of rows.
rows-code : O.Code
rows-code = O.Pi Time (λ _ → O.Pi Direction (λ _ → O.atom ClockPair))
rows-node : G.Node Rows
rows-node = G.P-node Time (λ _ → G.P-node Direction (λ _ → G.atom-node ClockPair))

-- Admission is supplied, not fabricated by successful format validation.
-- The index k represents the positive tick denominator D=suc k.
module Admitted (Admission : ℕ → Rows → Type)
  (k : ℕ) (r : Rows) (witness : Admission k r) where
  data Route : Type where time-first direction-first : Route
  route-code : Route → O.Code
  route-code route = O.retain (O.atom Route) route
    (O.retain (O.atom Calibration) frozen-calibration
      (O.retain (O.atom ℕ) (suc k)
        (O.retain rows-code r
          (O.retain (O.atom (Admission k r)) witness (O.atom Tensor)))))
  route-node : Route → G.Node Tensor
  route-node route = G.retain-node (G.atom-node Route) route
    (G.retain-node (G.atom-node Calibration) frozen-calibration
      (G.retain-node (G.atom-node ℕ) (suc k)
        (G.retain-node rows-node r
          (G.retain-node (G.atom-node (Admission k r)) witness (G.atom-node Tensor)))))
  old-source old-direct : O.Complete
  old-source = O.pack (route-code time-first) (source-read r)
  old-direct = O.pack (route-code direction-first) (native-read r)
  native-source native-direct : G.Package
  native-source = N.pack (route-node time-first) (native-read r)
  native-direct = N.pack (route-node direction-first) (native-read r)
  source-package-agrees : G.encode-package old-source ≡ native-source
  source-package-agrees = cong (N.pack (route-node time-first)) (sym (readout-agrees r))
  direct-package-agrees : G.encode-package old-direct ≡ native-direct
  direct-package-agrees = refl

  evidence-package : O.Complete
  evidence-package = O.pack (O.atom (Admission k r)) witness
  data Seeds : O.Complete → Type₁ where
    source-seed : Seeds old-source
    direct-seed : Seeds old-direct
    evidence-seed : Seeds evidence-package
  comparison-rule : R.Rule
  comparison-rule = R.compare-rule old-source old-direct (idEquiv Tensor) (sym (readout-agrees r))
  comparison-history : R.Resolve Seeds (R.output comparison-rule)
  comparison-history = R.apply comparison-rule
    λ { (lift true) → R.seed source-seed ; (lift false) → R.seed direct-seed }
  family : Bool → O.Complete
  family true = R.output comparison-rule
  family false = evidence-package
  history : R.Resolve Seeds (O.Pi-package Bool family)
  history = R.apply (R.Pi-rule Bool family)
    λ { (lift true) → comparison-history ; (lift false) → R.seed evidence-seed }
  actual-native-rule : G.encode-package (R.output comparison-rule)
    ≡ N.output (N.encode-rule comparison-rule)
  actual-native-rule = N.output-commutes comparison-rule
  module H = Resolution.ForOldSeeds ℓ-zero Seeds
  old-run : R.Closure Seeds
  old-run = O.Pi-package Bool family , history
  native-run : H.F.Closed
  native-run = equivFun H.closure-equivalence old-run
  endpoint-agrees : fst native-run ≡ G.encode-package (fst old-run)
  endpoint-agrees = H.endpoint-commutes old-run
  history-recovered : invEq H.closure-equivalence native-run ≡ old-run
  history-recovered = retEq H.closure-equivalence old-run

  -- Global typed-value observation, then its actual radar marked endpoint.
  old-value : O.Complete → G.TypedValue
  old-value q = O.El (O.expression q) , O.value q
  native-value : G.Package → G.TypedValue
  native-value q = G.Value (fst q) , snd q
  value-comparison : (q : O.Complete) → native-value (G.encode-package q) ≡ old-value q
  value-comparison q = refl
  retained-readout-commutes : native-value (fst native-run) ≡ old-value (fst old-run)
  retained-readout-commutes = H.readout-commutes old-value native-value value-comparison old-run
  marked-radar-reading : native-value native-source ≡ (Tensor , source-read r)
  marked-radar-reading = cong (λ t → Tensor , t) (readout-agrees r)
