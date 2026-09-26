# Two readouts select an observation-relative completion interface

## Result and operator-directed pivot

The operator chose structural synthesis rather than further local radar
arithmetic. Fresh resume still selected `radar-rational-normalization-refinement:v1`;
that work is deferred, NOT claimed complete. This turn completes the newly
authorized two-readout synthesis and records the reprioritization atomically.

The result is a reusable **observed-carrier comparison and extension criterion**,
with actual Newtonian-jet and radar instances. A common carrier comparison does
not determine a unique completion: observation and calibration supply additional
requirements. An exact vacuum family refutes the stronger claim that the weak
completion already adequate for radar must preserve pointwise tides.

This is a shared structural interface, not an equivalence between Newtonian and
relativistic physical sources.

## 1. The interface, with its obligations separated

For a declared source policy and fixed observation context, retain:

1. **Source admission:** an actual source/preparation witness, not a label.
2. **Carrier comparison:** enc:X->Y and dec:Y->X with both inverse laws.
3. **Independent readings:** r:X->O and s:Y->O, with a proved comparison

       s(enc(x))=r(x).

   Defining s as r after dec is not the required independent implementation.
4. **Observation profile:** coefficient interpretation, units, calibration,
   numeric distances and a readout modulus on the admitted domain.
5. **Completion certificate:** uniform bounds sufficient to preserve Cauchy
   data, and a complete separated output space.

The numeric distances below concern fixed payload strata. They do NOT assign
a global metric to every constructor Code, source certificate or higher witness.
Retained source/evidence/history data stay retained; numeric completion is not
permission to quotient those witnesses by equality of output values.

## 2. Reusable comparison/extension theorem

Let A and B be corresponding admitted numeric payload domains. Suppose enc and
dec are inverse and uniformly continuous for INDEPENDENTLY declared distances.
Let r and s be independently specified readings with s enc=r. Let O be complete,
and suppose r has a uniform modulus on A.

Then:

- enc/dec induce inverse comparisons of the metric completions of A and B;
- r and s extend uniquely to those completions;
- the completed square commutes;
- every existing unequal pair of reading values remains unequal in O.

For Lipschitz data, if enc and dec have constants C_enc,C_dec and r has constant L,
then s has constant at most L*C_dec. Isometric carrier comparisons do not enlarge
that constant.

**Proof.** Uniform maps carry Cauchy sequences to Cauchy sequences and preserve
the relation that pairwise distance tends to zero. Completeness of O supplies
the readout limit, independently of representative. Finite-stage comparison
holds termwise, hence passes to the limit. Inverse laws pass to completions by
density and continuity. No injectivity of the reading is needed or asserted.

This theorem concerns numeric completion views. If whole completed packages are
constructed, their provenance must be retained separately, for example as actual
Cauchy histories with their source certificates and comparison witnesses. The
statement does not identify different derivations merely because they have the
same numeric limit, nor does it establish a new completed admission policy.

The extension theorem is a written metric argument. The finite carrier/readout
comparison interface and its two instances are compiler-checked below; we do not
claim an Agda formalization of metric completion in this turn.

## 3. Genuine instance: Newtonian exact jet rows

The source payload is the actual `NewtonianTidalKernel.Jet`: one scalar, three
gradient entries and nine Hessian entries. The target is the owner's
`NativeTidalTableReadout.JetTable`, with its thirteen typed ports. Encoding sends
each field to its corresponding row; decoding reconstructs the jet. Both inverse
laws are checked.

The readings are independently present in existing code:

    source: NewtonianTidalKernel.hessian,
    native: NativeTidalTableReadout.read-tensor.

Their comparison holds for every jet. The synthesis additionally imports the
owner's actual nontrivial native-jet reading, its comparison with `geometric8`,
the actual package comparison and retained-history recovery. The instance is
therefore linked to the supplied physical calculation, not just an invented
zero example.

Independently define the source norm as the maximum of its thirteen field
magnitudes and the native norm as the maximum of its thirteen labelled rows.
The explicit index bijection proves enc/dec are isometries. Hessian projection
is 1-Lipschitz in maximum-entry norms. The selected physical tensor uses the
owner's retained common denominator 8*1728; at that fixed calibration the
normalized output bound acquires the corresponding reciprocal factor.

**Important coefficient boundary:** these native rows are INTEGERS. With a fixed
denominator they form a discrete complete lattice. Their completion is NOT all
real jets: Cauchy sequences are eventually constant. A rational/real coefficient
lift is extra declared structure, not something supplied by the carrier theorem.
The scalar/gradient entries are the supplied algebraic jet data; this note does
not silently identify every normalized polynomial entry with an uncalibrated
physical potential derivative.

The owner's first-jet-only no-factor theorem is a structural obstruction on the
full jet carrier. It does not assert that every arbitrary jet row assignment is
an admitted physical source.

## 4. Genuine instance: finite causal radar records

The source payload is the existing nine-clock-pair function indexed by time and
direction. The target is a selected-row section over the paired port domain.
Both inverse laws are checked. The native reading builds an actual finite table
and directly reads its clock-pair labels, rather than calling a decoder.

The source reading is the existing time-first radar numerator calculation. The
target independently performs direction-first temporal sums and polarization.
Its comparison is connected to the previously checked `NativeRadarReadout`
arithmetic theorem. The concrete clock-admitted native package and retained
history are referenced as the marked package-level instance.

Define the source distance as the maximum change of all emission/reception
coordinates. Define the target distance directly as the maximum rowwise clock-
pair change. Their isometry follows from the explicit index bijection.

For the frozen physical normalization, bounded radar distances R<=M and the
fixed probe design give

    ||delta Y||_max <= M/(2*epsilon^2*h^2) delta_clock.

Here epsilon=1/32 and h=1/4, so M=1 gives L=8192. This follows from the earlier
finite-readout bound and |delta R|<=delta_clock. It is a bound on the finite Y,
not on instantaneous curvature. With varying apparatus the already proved
inverse-design, range and resolution certificates must also be retained.

Again, fixed-denominator integer ticks alone are discrete. The real-clock
completion statement uses the separately declared calibrated clock-coordinate
space (or a specified rational-clock domain with its closure). It is not an
inference that the formal integer atom automatically became the reals. Formal
rational normalization/refinement remains deferred; the analytic theorem and
exact Fraction controls are already available with their stated boundaries.

The physical noncollapse witnesses remain the exact vacuum wave and static-flat
reference with the same initial rest preparation. The moving-flat control shows
why finite Y is not curvature alone. These are retained physical witnesses,
not the synthetic norm-test packets.

## 5. Observation families and forgetting

`agda/ObservedCarrierSynthesis.agda` checks a product construction: two readings
on the SAME compared carrier form a joint reading with a commuting comparison.
With output maximum metric, moduli combine by maximum. On a common source with
two control pseudometrics, their maximum is a sufficient joint control.

The qualification SAME is essential. Nothing here supplies a shared source
state or cross-regime equivalence between the Newtonian fixture and Rosen radar.
An independently constructed overlap map and compatible admission witnesses
would be needed for that further claim.

The module also proves two generic consequences:

- compared readings preserve any witnessed distinction;
- if a proposed forgetting identifies two inputs whose readings differ, no
  reader on the forgotten data can reproduce the original reading everywhere.

The actual owner first-jet obstruction supplies the tidal example. A new radar
instance has the same calibrated emission schedule but one altered reception:
the xx integer numerator changes from 0 to -416. Hence emission data alone
cannot carry this reading. The altered packet is explicitly an algebraic
candidate, not a newly claimed vacuum solution.

These are tests of indispensable observation data, not assertions that every
carrier distinction must remain observable.

## 6. Physical counterexample to a universal completion claim

On ONE actual Einstein source family, both the causal radar observation and
pointwise E(0) are defined. The earlier exact vacuum hostile satisfies

    gamma_n -> I in C1,
    sup |R_n(t,b)/|b| - 1| <= 8/n^2,
    ||E_n(0)-E_flat(0)|| = 1/2.

Thus the metric completion already sufficient for the radar reading cannot
also support a continuous pointwise tidal reading. Reversible carrier encoding
does not repair this failure: it supplies neither the missing regularity nor
a stronger norm.

Controlled C2 source convergence with uniform inverse/frame bounds does support
the pointwise tidal readout, by the earlier quantitative theorem. That is a
sufficient joint refinement for these declared source readings, not the unique
possible weak theory or a topology on every constructor package.

This is a physical hostile, unlike the arbitrary-jet or perturbed-clock algebra
controls. It refutes the stronger completion claim without requiring an assumed
Newtonian/Rosen identification.

## 7. Verification and authority boundaries

Run:

    python research/voevodsky/check_native_radar_formal.py --structural --fresh
    python research/voevodsky/check_observed_carrier_synthesis.py

Fresh safe/cubical compilation passes for `ObservedCarrierSynthesis`, including
the actual owner Newtonian native reading/package/history dependencies and our
radar integration. Two existing readout/provenance rejection controls fail as
intended. All work occurs in private snapshots; no owner artifact is modified.
The exact control audit passes 114 checks for independently defined norms,
projection bounds, clock-readout bounds and the retained hostile envelopes.
The all-n and completion statements are written proofs, not finite-sampling claims.

Receipts:

- `observed-carrier-synthesis-formal.json`;
- `observed-carrier-synthesis.json`.

This establishes a common **observation-relative interface and criterion**,
instantiated by two actual constructions. It does not derive their physical laws,
identify their source policies, imply owner adoption of the synthesis, or select
one universal completion from the bare carrier.

## Next structural experiment

Test a source-anchored local overlap rather than adding another abstract wrapper:
can a controlled local tidal jet from the exact Rosen observer be compared with
an admitted Newtonian Hessian calculation, and with the appropriate radar limit,
while preserving units, frame and preparation?

The deliverable must identify the actual common datum or prove why the proposed
identification fails. Equality of matrix-shaped outputs is not enough. Any local
jet approximation, new harmonic-potential admission or resolution limit must
be stated explicitly; no global Newtonian/relativistic equivalence is licensed.
The unfinished rational-normalization proof remains a separate verification
backlog rather than being marked resolved by this synthesis.
