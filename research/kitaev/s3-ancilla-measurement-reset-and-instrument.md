# Ancilla, measurement, reset, and instrument typing

Owner: `marici.Kitaev`

Status: exact finite dilation target and resource inventory; controlled central
powers are not yet source-derived.

## Bounded question

Which ancillas and records are required for the center channel, and which
construction actually produces a sector readout?

## Three distinct resources

The local port compilers use one six-level coherent holonomy ancilla prepared
in `|e>`.  It is not a measurement record.  It may be reused only after an
ideal clean return has been verified or after reset.

The nonselective random-unitary center channel uses private classical draws:
three unbiased bits for sector dephasing, eight unbiased bits across the four
two-dimensional block stages, and four uniform trits across the two
three-dimensional stages.  The ideal entropy is

\[
11+4\log_2 3\ \text{bits}.
\]

Those branch records must be discarded or kept inaccessible.  Retaining them
defines a refined control-branch instrument, not a center measurement.

## Exact sector record

To produce an eight-valued sector record, use a three-qubit phase-estimation
register.  Prepare `|000>`, create the uniform `Z8` superposition, apply the
controlled central powers `U1,U2,U4`, perform the inverse eight-point Fourier
transform, and measure computationally.  The exact residue map is

\[
0:A,\ 1:B,\ 2:C,\ 3:D,\ 6:E,\ 7:F,\ 4:G,\ 5:H.
\]

Three qubits are sufficient and necessary for eight orthogonal records.

The unresolved source gate is controlization: reachability of an uncontrolled
`U_j` does not by itself provide a controlled-`U_j`.  A conditional coupling
from each phase-estimation qubit to the central pulse compiler must be added.

## Instrument hierarchy

Retaining the sector record immediately after phase estimation gives the
projective sector instrument.  Following it by within-block depolarization
gives

\[
\rho\longmapsto
\frac{\operatorname{Tr}(P_a\rho)}{d_a}P_a\otimes|a\rangle\langle a|.
\]

This record-producing center measure--prepare instrument has 36 Kraus
operators.  Discarding `a` recovers the nonselective center conditional
expectation.  Thus a channel implementation and a readout instrument are not
the same apparatus claim.

## Verification and falsifiers

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_s3_ancilla_measurement_instrument.py
```

The checker exactly decodes every residue, verifies the dimension and
matrix-unit census, and types every record/reset rule.  Eight aggregate gates
are declared.  Saved result:
`research/kitaev/results/s3-ancilla-measurement-instrument.json`.

Falsifiers include a wrong residue record, fewer than eight orthogonal record
states, Kraus count other than 36, failure of nonselective recovery, or absence
of a physical controlled-power interface.
