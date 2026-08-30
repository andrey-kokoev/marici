# Objective records as a metastable dynamical sector

## Question

Can the fault-qualified objective-record quotient be derived as a metastable
sector of a specified reversible dynamics rather than postulated from a static
family of agreeing readouts?

## Claim boundary

Let (U_t) be the source-specified reversible dynamics on a global carrier
(S\otimes E). Let (r_i) be physically derived fragment readouts. A static
record quotient at time (t) does not establish a durable objective record.
The dynamical constructor additionally requires:

1. a declared interaction generating the record channels;
2. a record-formation rate (alpha);
3. a record-loss rate (eta);
4. an information-return rate (gamma);
5. an observer-readout rate (omega);
6. a fault-qualified independence test;
7. a completion-stable lower observability bound.

Define the dimensionless dynamical margin

\[
\mathcal R=\frac{\alpha}{\beta+\gamma}.
\]

For this DPC, a candidate metastable record regime requires

\[
\mathcal R>1,
\qquad
\beta+\gamma<\omega<\alpha.
\]

These inequalities are gates chosen for the finite rate model below. They are
not asserted as universal laws of natural decoherence.

## Exact reversible witness

A controlled-NOT fanout sends

\[
(a|0\rangle+b|1\rangle)|00\rangle
\longmapsto
a|000\rangle+b|111\rangle.
\]

Each environment qubit then carries the pointer value, while the relative
phase remains global. Applying the same two controlled-NOT gates again returns
the initial state. Static redundancy therefore coexists with exact global
reversibility.

This witness separates three notions:

- formation of readable records;
- persistence of those records under uncontrolled dynamics;
- fundamental destruction of the hidden relation.

Only the first follows from the fanout snapshot.

## Coarse rate model

Let (x(t)) be the expected fraction of usable records. The finite model is

\[
\dot x=\alpha(1-x)-(\beta+\gamma)x.
\]

Its equilibrium is

\[
x_*=\frac{\alpha}{\alpha+\beta+\gamma},
\]

and its relaxation gap is

\[
\Delta=\alpha+\beta+\gamma.
\]

The quotient is dynamically useful only relative to a declared observation
window. Neither (x_*>1/2) nor a large gap alone proves witness independence,
nondisturbance, or global separatedness.

## Hostile fixtures

1. Snapshot-only fanout: all records agree, but a source-authorized inverse
   erases them exactly.
2. Return-dominated dynamics: (gamma\geq\alpha) prevents the declared
   metastable margin even when instantaneous redundancy is high.
3. Slow observer: (omega\leq\beta+\gamma) means records decay or return before
   they can be read reliably.
4. Premature observer: (omega\geq\alpha) probes faster than the declared
   formation process completes.
5. Completion collapse: finite readout maps may remain injective while their
   minimum gain tends to zero.

## Decisive problem contract

The programme passes only if one source-derived model supplies the interaction,
rates, fragment cover, fault domains, and completion topology and then passes
all corresponding gates. Fitting rates after observing a stable plateau is not
a source derivation.

The finite checker establishes only the logical independence of static
redundancy, reversible recovery, rate separation, and completion stability.

## Disposition

The finite DPC is closed. It refines objective-record formation from a static
quotient into a candidate metastable dynamical constructor. Its unresolved
physical task is to derive the rates and observer cover from an actual
Hamiltonian and environment rather than assigning them phenomenologically.

Verification is provided by
`research/nima/checkers/check_sommerfeld_dynamical_objective_record_dpc.py` and
`research/nima/results/sommerfeld-dynamical-objective-record-dpc.json`.
