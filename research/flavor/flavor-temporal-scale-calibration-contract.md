# Temporal scale-calibration contract

## Question

What must it mean operationally for a \(P_{\mathrm{scale}}\) calibration to
establish the interface row required by WP548?

## State-establishing event

A successful calibration is both an observation and a state transition. It
reveals that the named transfer chain produced a reference readback and
establishes a shared flavor/comb frame for a bounded validity interval.

WP549 uses the finite state space

\[
\{U,V_3,V_2,V_1,E\},
\]

where \(U\) is unlinked, \(V_j\) has \(j\) remaining validity units, and \(E\)
is expired. The illustrative budget is three physics trials. It is a contract
parameter, not a calibrated physical timescale.

A successful calibration sends every state to \(V_3\). Each accepted physics
trial or wait step ages \(V_3\) to \(V_2\), \(V_2\) to \(V_1\), and \(V_1\)
to \(E\). Physics trials in \(U\) or \(E\) are invalid.

## Typed null and fitted outcomes

A completed calibration trial with no reference readback produces the typed
null outcome "calibration_null". It does not establish the interface.

A numerical row supplied without a named calibration chain produces
"compiler_reject". Algebraic rank three is therefore insufficient for
instrument authority.

## Temporal support law

Every accepted physics readout must have a preceding successful calibration
whose validity budget has not expired. The following histories are forbidden:

- accepted physics readout before successful calibration;
- accepted physics readout after expiry;
- null calibration followed by accepted physics readout;
- fitted interface row followed by accepted physics readout.

This is a qualitative support contract, not merely a probability assignment.

## Rank is state-relative

In \(U\) and \(E\), the \(P_{\mathrm{scale}}\) row is absent. The detector
Jacobian has rank two and kernel

\[
(1,1,0)^T.
\]

In a valid state, the interface row is present and the Jacobian has rank three
with zero kernel. Hence detector faithfulness is indexed by the calibration
state and authorized event history.

## Deletion replay

Deleting the successful calibration event from a history invalidates every
dependent physics readout. Algebraically it removes the interface row, returns
the Jacobian to rank two, and restores the exact scale kernel.

This is the smallest compiler test against fitting a projector from the
desired answer. If a rank-three state survives deletion of its source
calibration event, the interface has been granted authority by presentation.

## Authority boundary

WP549 specifies an executable temporal contract but does not realize the
physical transfer chain. Its three-step validity budget is illustrative.
Physical admission still requires measured drift, disturbance, resource cost,
readback distribution, and covariance.

The contract affects detector identification only. It neither changes the
flavor source rank nor supplies the independent selector condition

\[
2\ell_a-\ell_w\ne0.
\]

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp549_temporal_scale_calibration_contract.py

The generated result is
research/flavor/results/wp549_temporal_scale_calibration_contract.json.

The reviewed graph admission is
ev-000000004988-f44374fd-20e8-42fe-8bf6-c92871840fd9.
