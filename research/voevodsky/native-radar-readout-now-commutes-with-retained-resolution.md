# Native radar reading now commutes with the actual retained-resolution interface

## Result and fresh leaf

Fresh resume selected `native-radar-package-readout-comparison:v1`.
The missing formal finite integration is now implemented in
`agda/NativeRadarReadout.agda` and passes a fresh safe/cubical closure check.

This is no longer only a Python section-regrouping example. It imports the
actual `WholePackageSigmaPi`, `WholePackageResolution`,
`IndexedConstructorTables`, `NativeTableRules` and `NativeTableResolution`
interfaces. The source/native arithmetic comparison is proved for arbitrary
integer clock rows. Actual packages, a comparison rule, retained evidence and
its derivation are connected through the owner's closure equivalence.

The theorem remains conditional on a supplied physical admission predicate.
It does not turn a source label into a proof of a vacuum realization or formally
verify the continuum/error analysis from the earlier notes.

## Exact clock representation and physical normalization

The frozen protocol uses epsilon=1/32, proper-time step h=1/4, center 1, and
probe vectors (3,0),(0,4),(3,4). Each row retains BOTH emission and reception
integer ticks. A common positive denominator D converts a tick count into
proper time; the formal module represents D as suc k.

For each time/direction slot let n_jd be reception ticks minus emission ticks.
Then

    R_jd=n_jd/(2D), q_jd=256*n_jd^2/D^2.

Let T denote the temporal weights (1,-2,1). The integer numerator is

    N_11=16*T(n_x3^2),
    N_12=6*[T(n_xy5^2)-T(n_x3^2)-T(n_y4^2)],
    N_22=9*T(n_y4^2).

The physical finite reading is

    Y=(-2048/(144*D^2)) N.

This is an exact normalization of the existing protocol, not a new readout.
Integer multiplication by a denominator is not asserted to be an equivalence
on arbitrary integer tensors.

`check_native_radar_tick_bridge.py` takes both previously certified rounded
physical clock packets, finds their exact common denominator and verifies:
all clock roundtrips, positive denominator and future reception, integer
numerator equality, and exact equality of the normalized result with the old
Fraction protocol implementation. Both examples remain nonzero. All 16 controls
pass. Ideal irrational clocks retain their earlier enclosure/rounding bounds;
they are not silently identified with the rational rounded clocks.

## Independently defined native reading

`source-read` is the time-first calculation: square each clock difference,
form each time's three fitted numerator components, then take temporal weights.

The native construction creates an actual `TableFibrationCycle.Table` with
clock-pair labels and typed time/direction ports. `native-q` reads its row label
directly. `native-read` independently performs direction-first temporal sums
and the polarization coefficients. Neither calls a legacy decoder, the source
reader, or an old evaluator.

Three ring identities establish the comparison for arbitrary row values:

    component-agrees : (r : Rows) (c : Component)
                    -> native-read r c = source-read r c,
    readout-agrees : (r : Rows) -> native-read r = source-read r.

These are compiler-checked algebraic proofs using the integer commutative-ring
solver, not `refl` on a zero or selected numerical fixture. Squaring still occurs
at the individual row before the two linear reductions.

## Actual packages and retained history

The raw nine-row carrier is represented by actual legacy Pi constructors and
native P nodes over Time and Direction, not a required old-Code annotation.
Each route package retains:

- its route label;
- the frozen calibration, including explicit probe vectors, clock and reflection
  conventions, baseline/time denominators and proper-time center;
- positive tick denominator D;
- all nine clock pairs;
- an actual value of the supplied admission type;
- the selected three-component numerator reading.

The `Admitted` module takes

    Admission : Nat -> Rows -> Type,
    k, r, witness : Admission k r.

It supplies `source-package-agrees` and `direct-package-agrees` against actual
`G.encode-package` endpoints. The native source package's selected reading is
computed independently by `native-read`, so its equality is obtained from the
new arithmetic proof rather than assumed by the generic encoder.

A genuine legacy `compare-rule` connects the two routes. Its history uses the
actual seed and application constructors. An actual Pi rule retains that
comparison alongside a separate evidence package. The implementation checks:

- `actual-native-rule`, using the actual native rule output comparison;
- `endpoint-agrees`, for translation of the retained run;
- `history-recovered`, recovering the full legacy run by the inverse equivalence;
- `retained-readout-commutes`, instantiating the owner's `readout-commutes` API;
- `marked-radar-reading`, identifying the independently computed native marked
  endpoint with the source radar numerator.

The global observation passed to `readout-commutes` is the typed selected value
of a package; it is defined directly on each package representation. Its
preservation is generic. The NON-generic radar content comes from the independent
row arithmetic and marked-package comparison just described. The generic closure
theorem alone is not advertised as proving the radar calculation.

## Fresh verification without owner mutation

Run:

    python research/voevodsky/check_native_radar_formal.py --fresh
    python research/voevodsky/check_native_radar_tick_bridge.py

The formal checker copies source files into private snapshots under
`temp/native-radar-formal`, then compiles with Agda 2.8.0 and Cubical 0.9 using
`--safe --cubical --guardedness --ignore-interfaces`. All imported interfaces
in that closure are rechecked. Owner and library source hashes are checked
unchanged; interfaces and build output are written only in the snapshots.
No owner file or receipt was modified.

The fresh positive root passes. Two own negative roots reject with the expected
`UnequalTerms` diagnostics:

- `NativeRadarBadPort`: erasing the distinction between xx and yy fails, 16 != 0;
- `NativeRadarBadEvidence`: erasing distinct retained admission values fails,
  true != false.

These are synthetic algebra/provenance hostiles, not physical observations.
The initial development runs exposed a layout error and a diagnostic-output
encoding issue; both were fixed before the successful final fresh run.

Receipts:

- `native-radar-formal.json`: fresh formal closure, intended rejections and
  source snapshots;
- `native-radar-tick-bridge.json`: exact normalization of both physical packets,
  with formal and physical receipt hashes.

This is formal verification of the finite arithmetic/package/retained-history
comparison. It is not a formal proof of the vacuum equations, analytic ray
bounds, real-number completion or a laboratory instrument's accuracy.

## Disposition and next gate

The selected native-package comparison leaf is resolved in this explicit scope.
It fills the formal integration gap identified by the preceding synthesis and
does not presume owner adoption of the new artifact.

The remaining boundary is now sharper: `Admission` is a supplied predicate.
The next leaf should construct an explicit finite clock-admission certificate
retaining grid consistency, causal ordering, calibration and rounding/enclosure
bounds, and distinguish its mechanically checked content from the external
analytic witness of physical realization. A hash or source-name string must
not be used as the inhabitant of a stronger physical proposition.
