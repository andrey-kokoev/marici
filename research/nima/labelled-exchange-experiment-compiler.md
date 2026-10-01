# Iteration 6: executable source-labelled experiment adapter

## Implemented contract

`checkers/labelled_exchange_experiment.py` now implements the weaker contract
selected by the preceding composition audit. It connects actual native witness
boundaries to addressed exchange experiments with explicitly attached memory.
It does not claim that exchange operators factor through native primitive legs.

Compilation takes a comparison label, a retained witness chain, a source ID and
a trusted native differential evaluator. The evaluator must return exactly the
labelled composite-minus-direct-reference boundary. A wrong witness boundary,
an excluded reference leg or a request for native-path composition is rejected.
The checker obtains these witnesses and the differential from the freshly rerun
shared-leg DG source and compiles all137 actual comparison boundaries.

The compiler is a research API, not an authorization/security boundary: the
caller supplies the trusted source evaluator. A source ID alone is not evidence
of a valid witness. The native selection of this attached instrument remains
an assumption, even when its source boundary is correctly validated.

## Retained state and preparation

Preparation supplies q, w and their full153-by153 covariance, plus a preparation
identifier. It does not infer amplitudes from labels or traces. Invalid dimensions,
nonfinite inputs and non-positive-semidefinite covariance are rejected, with
explicit numerical tolerance1e-10 for covariance checks.

The stored packet contains:

- the16 conserved anchors a=q+U^T w;
- the137 mismatches delta=w-Uq;
- covariance in the full carrier/record coordinates;
- the current instrument reference frame;
- preparation identity and chronological compiled events.

Current q,w are reconstructed from a,delta, not stored as an inconsistent second
copy. Arrays returned in packets are read-only. This implementation concerns
real exchange endpoints; the intermediate complex oscillator pulse needs both
quadrature copies, as stated in iteration2.

## Composition and provenance

Each event retains its original source label, source reference and exact witness
chain separately from its current instrument address and reference. Execution
uses the addressed reflection H, updates covariance by H Sigma H^T, and appends
the event without quotienting history.

Running two event lists successively agrees with running their concatenation.
Two native witnesses for the same comparison compile to the same physical event
but remain distinct in provenance. A rectangle followed by its actual reverse
returns the state while retaining all eight events; it is not replaced by the
empty history.

Reference relabelling transports the packet, covariance and instrument addresses.
Original witness chains remain in their original source frame with that frame
recorded. They are not silently rewritten as witnesses in a new source chart.
A stale-frame event is rejected. Tests include a reference-moving permutation
and both isotropic and nonisotropic covariance.

This is a compiler for labelled experiments, not a representation of all native
path equalities or arbitrary rung reference changes. In particular the failed
shared-leg rectangle is still a nonidentity experiment.

## Current target status

A bounded checked chain now exists:

    validated native comparison witness
      -> declared feature and attached record port
      -> faithful exchange packet and ordered experiment
      -> conditional oscillator preparation/readout contract.

Its meaningful limits remain visible. The native source has not selected the
independent memory, carrier amplitudes, pulse Hamiltonian or detector. The
oscillator and homodyne identification is conditional, not a derived field law.
No absolute coupling follows from the normalized1/137 mismatch share.

Next run a complete calibrated measurement calculation through this adapter,
including detector loss, gain and phase-reference uncertainty. The signed echo
and rectangle controls provide falsifiers; calibration freedom must not be
mistaken for a prediction of interaction strength.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_labelled_exchange_experiment.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-labelled-exchange-experiment

Native witness boundaries are checked exactly by the supplied DG evaluator;
exchange, covariance and transport checks use tolerance1e-10. The report is
`results/labelled-exchange-experiment.json`. No physical measurements are supplied.
