# A finite radar contract retaining clocks, labels and a direct section readout

## Result and frozen protocol

Fresh resume selected `finite-resolution-radar-contract:v1`.
A nine-record protocol is now implemented in `finite_radar_protocol.py`.
Its processed reading is a **finite radar-shape second difference**, not an
unconditional instantaneous-curvature estimate. It is continuous on the actual
finite record completion at fixed resolution. Its error amplification is explicit.

The protocol is fixed before the controls:

- central proper-clock emission times tau_j=1+j/4, j=-1,0,1;
- epsilon=1/32 and labelled transverse vectors epsilon*(3,0), epsilon*(0,4),
  epsilon*(3,4), called x3,y4,xy5;
- the same Rosen emitter/reflector congruence and instantaneous null-return
  convention as the source-backed radar note;
- c=1, retained frame and proper-clock labels, no reflection dwell time;
- all nine emission/reception clock pairs retained, with source provenance.

The 3-4-5 geometry makes the flat control's clock values rational while still
providing three independent quadratic-form probes. It is not a physical law
or a geometry chosen to fit a measured curvature. All baselines are <=5/32,
inside the earlier 1/4 source bound. Emission u=tau/sqrt(2) lies in [0,1].

Validation rejects duplicate/missing slots, clock-grid mismatches, nonfuture
receptions, erased provenance, and wrong section membership. It does not
verify a supplied metric or certify that an arbitrary accepted packet is a
physically realizable observation. Provenance text alone is not a proof.

## Declared processing

For each labelled slot (j,d), retain the clocks and compute

    R_jd=(tau_reception-tau_emission)/2,
    q_jd=(R_jd/epsilon)^2.

The inferred shape matrix G_j is a declared finite-baseline processing output:

    G_11=q_x3/9, G_22=q_y4/16,
    G_12=(q_xy5-q_x3-q_y4)/24.

These coefficients invert the three calibrated quadratic probes in the
small-baseline limit. At finite epsilon, G is NOT asserted to equal gamma,
to be positive definite, or to be the metric of any actual spacetime.

The readout is

    Y=-(G_+ -2G_0 +G_-)/(2h^2), h=1/4,

stored as the symmetric components (11,12,22). Here h is a PROPER-TIME step,
not the u-step used in the preceding inverse note. The factor -1/2 corresponds
to the second-derivative term in the proper-time expression for E, but omits
its connection-quadratic term and transported frame. No renaming makes Y=E.

The output record retains the protocol and all raw clocks alongside Y.
A consumer requesting only Y explicitly forgets information; the package
itself does not discard the raw evidence.

## Completion and error theorem

Use maximum absolute component norm on the three output entries. The linear
polarization map q->G has infinity-operator norm

    max(1/9,1/16,3/24)=1/8.

The weighted temporal reduction has norm 2/h^2. If true distances are at most M
and each distance error is at most sigma, then

    |delta q| <= (2M sigma+sigma^2)/epsilon^2,
    ||delta Y||_max <= (2M sigma+sigma^2)/(4 epsilon^2 h^2).  (*)

This needs no curvature-derivative prior or bandwidth assumption. It only
bounds the declared finite processing of records. For two distance records
both bounded by M, a simpler Lipschitz constant is

    ||Y(R)-Y(R')||_max <= M/(2 epsilon^2 h^2) ||R-R'||_infinity.

For a fixed protocol, the finite-coordinate real closure of an admitted record
set therefore has a unique continuous extension of Y. More generally Y is a
polynomial in those distance coordinates with fixed coefficients. This does
not make every point of the ambient coordinate space physically realizable.
Discrete labels and protocol metadata remain fixed/retained during completion.
Allowing epsilon or h to vanish has no uniform bound from this theorem.

The flat control has M=5/32. With sigma=1/4096, (*) gives 1281/4096, illustrating
that small raw timing errors can still have substantial processed amplification.
Clock-origin shifts leave Y unchanged. Joint changes of time and length unit
by scale s send Y to Y/s^2, as verified. Time-grid jitter, baseline uncertainty,
frame recalibration and reflection delay require separate error terms; they
are not covertly included in the distance-error hypothesis.

## A direct finite section reading, not readout after decode

Freshly read `research/nima/fibration-constructor-equivalence.md` distinguishes
full annotated constructor equivalence from bare regrouping, and a generic
readout-after-decode theorem from an independently proposed reading.

Our finite interface is consequently stated narrowly. Set

    I={-1,0,1} x {x3,y4,xy5}.

Over each slot i, the fiber consists of clock-pair rows compatible with that
slot and the frozen protocol. A complete packet selects one row in every fiber.
The display map is the projection from labelled rows to I. The implementation
`NativeSection` retains the selected rows and their membership indices.

`on_native_section` reads these selected rows DIRECTLY, squares their calibrated
clock differences, accumulates weighted sums within each direction, and applies
the displayed polarization coefficients. It never reconstructs a Packet or
calls a decode operation. The source-side `by_time` first forms each time's
shape and then applies the temporal reduction. `by_direction` gives another
explicit finite table reading.

For every valid packet, each route uses the same q_jd. The polarization and
temporal maps are linear on distinct indices, so finite distributivity proves

    on_native_section(encode_section(packet)) = by_time(packet).

This is a new direct comparison for this finite observation interface, not
an invocation of the owner's generic decode theorem. The nonlinear squaring
must stay at each individual row before the linear reductions. A control shows
that moving it after temporal summation changes the result.

This does NOT establish equivalence with all of the owner's recursive Code,
resolution rules or physical source types, nor does it identify Pi with grouping
at the other endpoint. It is an explicit finite display-map section interface
suitable for owner review. No owner artifact was edited or adoption inferred.
The prior independent Newtonian/fibration readout request remains separate.

## What is retained and what is lost

The full packet retains the finite causal records, labels and protocol.
Y alone annihilates temporally constant and affine inferred shape components.
Two different static candidate records therefore have equal Y=0. The test of
this loss is algebraic; it is not passed off as two distinct source solutions
with the same fixed initial preparation.

The implementation is nonconstant on admissible-format candidate records.
The only fully supplied physical fixture in this turn is Minkowski space with
static reflectors: exact round trips give R=(3,4,5)*epsilon at each time, G=I,
and Y=0. The 512 perturbed fixtures are error/algebra controls, not claimed
vacuum spacetimes. In particular, successful validation is not a physical
realization theorem.

## Verification and successor

Run:

    python research/voevodsky/check_finite_radar_protocol.py

All 21 checks passed, including exhaustive 512 binary distance-noise patterns,
direct section/source comparisons, the quantitative error envelope, unit and
clock-origin controls, missing/duplicate/member hostiles and nonlinear-order
failure. Receipt: `research/voevodsky/finite-radar-protocol.json`.

Universal completion/commutation/error statements are written mathematical
proofs, not inferred from the finite cases or certified in Agda.

The finite-contract leaf is resolved. The next substantive gate is physical
noncollapse: produce a nonzero packet from an admitted source solution, not a
synthetic perturbation, and compare it with a curvature-free kinematic control.
That will distinguish an actual nontrivial observation from code nonconstancy
and prevent a finite shape acceleration from being mistaken for curvature.
