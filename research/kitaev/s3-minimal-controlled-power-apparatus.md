# Minimal apparatus for the three controlled sector powers

Owner: `marici.Kitaev`

Status: exact conditional compiler and interaction-family minimum; the added
five-body coupling is an apparatus postulate, not derived from the native
Hamiltonian.

## Frozen coherent surface `S0`

The previously admitted source has:

- record-qubit preparation and record-only gates;
- the four-edge `D(S3)` site controls;
- the clean six-level holonomy ancilla and its edge couplings;
- no interaction between any record qubit and either the data or holonomy
  ancilla.

Every circuit on `S0` therefore factorizes across
`record | (data,holonomy)`.  Its operator Schmidt rank across that cut is one.
For non-scalar `U`,

\[
C(U)=P_0\otimes I+P_1\otimes U
\]

has operator Schmidt rank two.  Hence `S0` cannot implement any of the three
controlled powers, regardless of circuit length.  This is stronger than a
failed compiler search.

## Minimal enlarged surface `S1`

Add one tunable record--data interaction family

\[
H_{\rm cond}=P_1\otimes Z,
\qquad
Z_A,\ldots,Z_H=(-8,1,2,3,6,7,20,5).
\]

Then

\[
e^{-i(\pi j/4)H_{\rm cond}}
=P_0\otimes I+P_1\otimes U^j,
\qquad j=1,2,4.
\]

Thus `controlled-U1`, `controlled-U2`, and `controlled-U4` each require one
conditional pulse: three pulses total.  There is no workspace ancilla, so
workspace cleanup is vacuous and exact.  The three control qubits are retained
because they are the intended sector record.

Minimality is stated only in the honest discrete sense: zero new
record--data interaction families cannot cross the tensor cut, while one
tunable family suffices.  It is not a minimum over hardware energy, geometric
range, or analog precision.

## Locality and single faults

The endpoint site is supported on the four frozen boundary edges.  Therefore
`P1 tensor Z` has data support four and total arity five including its record
qubit.  In this primitive-five-body model:

- a control-Z fault commutes and has data weight zero;
- a control-X fault may acquire all four data edges;
- an arbitrary fault in the five-body pulse may have data weight four.

Correcting every arbitrary weight-four data fault requires code distance at
least nine.  No preferred decoder is selected.  A lower-arity gadget could
improve this bound, but would need its own clean-ancilla compiler and
gate-by-gate census; none is derived here.

## Source boundary

`S1` closes the controlled-power typing gap conditionally and exactly.  It
does not derive the new coupling from the native commuting-projector
Hamiltonian, nor from the nine-dimensional direct primitive span.  The prior
packet proves that `Z` is not already a simultaneous source Hamiltonian.
Calibration, timing noise, preparation, inverse `F8`, measurement, and a
fault-tolerant lower-arity realization remain separate apparatus obligations.

## Verification and falsifiers

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_s3_minimal_controlled_power_enlargement.py
```

The checker verifies the tensor-cut rank obstruction, all three exponential
identities, the one-family minimum, pulse inventory, cleanup, locality, and
fault bound.  Saved output:
`research/kitaev/results/s3-minimal-controlled-power-enlargement.json`.

Falsifiers are a rank-two joint unitary constructed on `S0`, failure of any
controlled-power identity, a nontrivial workspace residue, or a verified
lower-support realization under the same frozen gate contract.

