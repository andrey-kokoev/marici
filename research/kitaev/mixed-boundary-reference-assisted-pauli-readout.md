# A logical Bell reference converts incompatible loop--arc probes into one QND setting

Owner: `marici.Kitaev`

## Bounded question

Can the full \(2k\)-bit logical Pauli label be measured in one sharp QND
setting, and what additional source resource is minimally required?

## Data-only obstruction

For each logical coordinate, primal and dual probes obey

\[
Z_iX_i=-X_iZ_i.
\]

They cannot belong to one projective measurement algebra on the data block.
The algebraic \(2k\)-bit Pauli label from milestone 2609 is therefore not a
single data-only sharp record.

## Reference-assisted commuting checks

Adjoin a reference code block with the same mixed-boundary logical quotient
and prepare the logical Bell state stabilized by

\[
Z_iZ_i^{R},
\qquad
X_iX_i^{R},
\qquad i=1,\ldots,k.
\]

The doubled checks commute. For the paired coordinate, the data intersection
contributes one mod two and the reference intersection contributes another:

\[
1+1=0\pmod2.
\]

All \(2k\) checks are independent, so their joint eigenspaces on the doubled
logical Hilbert space are one-dimensional. The resulting Bell basis has
\(4^k\) records.

If a logical Pauli \(Z^aX^b\) acts on the data half, its Bell syndrome is the
pair \((b,a)\), up to the frozen ordering convention. Hence the joint sharp
measurement reconstructs the entire logical Pauli coset in one setting.

## Minimality

There are \(4^k\) Pauli cosets modulo phase and stabilizers. Any faithful
binary record requires at least \(2k\) bits. The Bell stabilizer family has
exactly \(2k\) independent checks and attains the lower bound.

The resource improvement is not free. The reference supplies:

- a second logical code block of the same rank;
- a matched primal--dual coordinate frame, including every required arc port;
- preparation of a logical Bell state;
- joint parity couplings implementing the doubled checks.

Without the matched frame, the syndrome is defined only up to the induced
symplectic relabeling. Without Bell preparation, the same PVM is a relational
measurement but does not identify which Pauli acted on the data half.

## QND boundary

The Bell projectors form a repeatable sharp instrument for the relational
Pauli-error label: an immediate repetition returns the same record. This is
not a nondisturbing measurement of an arbitrary unknown data state. It
projects the data--reference pair into a Bell sector and generally destroys
standalone logical-state information.

Thus the construction diagnoses a Pauli channel relative to a prepared
reference; it is not full tomography and not a decoder.

## Mixed-boundary support

Every rough-to-rough or smooth-to-smooth arc probe required on the data block
must be matched by the corresponding reference arc. The doubled support is a
pair of homologous relative strings. Phase cancellation is quantum
coefficient data; the existence and typing of the relative supports belongs
to Carrier geometry.

## Pair-of-pants witness

For the one-qubit pair-of-pants code, the data rough arc and dual rough loop
anticommute. After adjoining a matched reference, the rough-arc parity and
rough-loop parity commute and their four joint records distinguish
\(I,X,Z,XZ\).

## Falsifiers

- a nonzero symplectic product between two doubled checks;
- rank below \(2k\) for the doubled stabilizer family;
- fewer than \(4^k\) joint records;
- a missing matched reference arc port;
- identifying Pauli action without Bell-reference preparation;
- promoting relational error diagnosis to arbitrary-state tomography.

## Disposition

One-setting QND readout of the full logical Pauli label is possible, but only
relationally. A matched Bell reference converts each incompatible loop--arc
pair into commuting doubled parities and exactly attains the \(2k\)-bit lower
bound.

## Claim strength

Exact finite stabilizer-instrument theorem and resource typing statement.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_mixed_boundary_bell_readout.py`.
The result is written to
`research/kitaev/results/mixed-boundary-bell-readout.json`.

