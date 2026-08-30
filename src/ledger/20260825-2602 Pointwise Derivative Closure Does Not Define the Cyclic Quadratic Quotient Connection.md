# 2602 — Pointwise Derivative Closure Does Not Define the Cyclic Quadratic Quotient Connection

## Corrected claim

Entry 2593 proves pointwise derivative closure of the cyclic quadratic class
after adjoining the three first-normal classes. It does not prove a horizontal
quotient line because preservation of the first-normal denominator was never
established.

## Reconstruction

The pointwise scalar coefficients reconstruct uniquely as

\[
\omega_i=\frac{N_i}{s_1s_2s_3\Lambda_P},
\]

with homogeneous degree-four numerators. The reconstruction uses fifteen
independent degree-four evaluation points and passes five unused points at two
independent primes.

## Decisive falsifier

Exact characteristic-zero differentiation gives nonzero curvature. At
\((s_1,s_2,s_3)=(5,7,11)\),

\[
(F_{12},F_{13},F_{23})
=
\left(
\frac{8}{40425},
-\frac{8}{63525},
\frac{8}{88935}
\right).
\]

The nonvanishing replicates at \((7,11,13)\).

A scalar connection induced on a line quotient of a flat bundle must be flat.
Hence these coefficients are not a descended quotient connection.

## Consequences

The “horizontal quotient line” conclusion of Entry 2593 is retracted. Entry
2597 remains a correct falsification of a two-parameter algebraic ansatz, but
not an intrinsic pole classification.

No new support divisor is indicated. Indeed, the reconstructed candidate's
denominator factors only through the existing soft and momentum-triangle
supports. The defect is categorical: pointwise closure was mistaken for
descent through an unverified denominator subconnection.

## Next falsifier

Compute the Gauss--Manin derivatives of the three labelled first-normal
classes and test preservation of their span. Do not form another quotient
connection unless that test passes.

## Artifacts

- `research/benincasa/cm-cyclic-pointwise-closure-curvature.md`
- `research/benincasa/checkers/probe_cm_cyclic_connection_slice_degrees.py`
- `research/benincasa/checkers/check_cm_cyclic_connection_reconstruction.py`
- `research/benincasa/results/cm-cyclic-connection-reconstruction.json`
- `research/benincasa/checkers/check_cm_cyclic_connection_curvature.py`
- `research/benincasa/results/cm-cyclic-connection-curvature.json`

Ledger sequence claim: `seqclaim-92e4f8f8676570f02ad93d69`.

Epistemic event: `ev-000000003806-fa0f61a8-7b14-4c62-95d7-9588e05d1152`.
