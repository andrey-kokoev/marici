# Joint phase action and spatial-moment balance on the same retained interaction

## Reuse, not a new mechanical model

The earlier `phase-memory-first-moment.md` already demonstrated why carrier
and record intensities can miss a conserved coherent first moment. This test
applies that idea to the ACTUAL bound six-port exchange, the same 68 full-turn
branches, the same AB preparation, and the same complex pulse realization
used to obtain nonreal retained-history overlaps. No new masses, forces or
initial amplitudes are introduced.

## Phase weights are constrained by the coupling

Give the whole carrier one phase weight q_c and each persistent record its
own q_i. Hold the actual six labelled pulse operators fixed. Commutation with
every pulse forces

    q_c=q_AB=q_BC=q_CA=q_BA=q_AD=q_DB.

The exact linear constraint matrix has rank six on these seven variables.
Thus there is one free COMMON phase weight in this declared class. Assigning
neutral or opposite charge weights to the records while retaining the same
fixed coupling fails that invariance test.

The existing complex/canonical realization supplies the conserved phase
quantity

    Q=z^dagger metric z.

Every full exchange and every intermediate pulse preserves Q. It generates
the common phase action up to the established symplectic orientation and
normalization convention. The numeric charge weight, coupling to an external
field, and electric-charge interpretation are not selected by the commutant.

This does not contradict the prior neutral-record endpoint-frame adapter:
that adapter also transforms the feature/metric data. Nor does it contradict
the negative phase character of a linear dual effect. Those are different
typed actions, not opposite-charge records under the same fixed pulse.

## Relational phase is neutral under that common action

Multiplying EVERY retained alternative by the common phase preserves its
Gram and therefore all of the newly calculated cyclic overlap phases.
Hence a nonzero relational cycle phase is not the common phase charge value.
Both structures coexist on the SAME state without being identical.

A naive linear spatial amplitude Lz instead transforms by the common phase.
It cannot simultaneously be treated as a phase-neutral classical spatial
quantity under that internal symmetry. This is why the joint test must
retain the pairing, rather than naming a linear amplitude momentum.

## Whole-state first moment with the existing target geometry

The conserved whole anchor is a=y+F r. For each existing tetrahedral target
coordinate, let X be the corresponding real diagonal matrix on the raw
16 tensor-coordinate chart. Define the unnormalized intensity diagnostic

    M_X=a^dagger X a
       =y^dagger X y
        +r^dagger F^dagger X F r
        +2 Re(y^dagger X F r).

The complete quantity and each displayed term are neutral under common
phase. The full M_X is conserved by ALL six pulses, including their continuous
intermediate evolution. X is the prior endpoint-coordinate chart, not a new
fitted spatial direction. This raw-coordinate diagnostic is not silently
identified with the exchange's energy metric.

Carrier and mapped-record contributions do not generally balance without
the cross term. On the actual full-turn family:

| Test | Result |
|---|---:|
| Complete branches |68|
| Separate carrier+record first moment fails to balance |60|
| Retained cross term compensates that failure exactly |60|

The same nonreal-overlap examples also satisfy unit Q and phase neutrality
of the full first moment. Thus charge-symmetry compatibility and the
collective spatial balance have been checked jointly, not on unrelated
preparations or independently fitted bodies.

## What the joint test establishes

There is a working common phase symmetry and a phase-neutral collective
spatial-moment balance for the existing source-labelled interaction. The
missing balance in separate-sector readings is stored in the retained
relation between carrier and record. Assigning independent bodies and
discarding that relation loses actual dynamical information.

This is NOT yet mechanical momentum conservation: M_X is a first moment
on a declared endpoint chart. No inertial masses, position-to-momentum law
or force law were derived by renaming it. Likewise, the fixed exchange does
not supply an opposite-charge carrier/record pair; its admissible common
phase action says the opposite within the tested weight class.

The narrower remaining identification is now explicit: relate the common
phase quantity and the complete coherent spatial balance to physical charge
and mechanics, retaining the cross term. Another clock or independently
assigned curvature variable would not resolve that identification.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_joint_phase_and_retained_moment_balance.py

142 exact checks pass, rerunning the retained-history phase census and
original source/exchange checks. Conservation is checked as full operator
and generator identities; the 68-branch census supplies the actual orbit
controls. Receipt: `results/joint-phase-retained-moment-balance.json`.
