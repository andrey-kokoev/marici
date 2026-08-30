# Minimal mixed-boundary logical probes require arc ports

Owner: `marici.Kitaev`

## Bounded question

What is the smallest legal probe family that separates logical Pauli classes
modulo stabilizers on a mixed-boundary surface code, and can those probes be
measured sharply in one setting?

## Logical quotient dimensions

For genus \(g\) with \(b=r+s\) boundary components and \(r,s>0\), each CSS
logical sector has dimension

\[
k=2g+b-2.
\]

A family of binary linear probes separating one sector is an injective map

\[
\mathbf F_2^k\longrightarrow\mathbf F_2^m.
\]

Therefore \(m\ge k\). A dual basis of relative intersection probes achieves
equality.

The full logical Pauli quotient modulo phase and stabilizers is

\[
\mathbf F_2^k\oplus\mathbf F_2^k,
\]

so any binary linear probe map faithful on all Pauli classes needs at least
\(2k\) rows. A symplectic dual basis supplies exactly \(2k\).

## Minimal geometric inventory

To separate primal logical strings, the minimal dual probe basis contains:

- \(2g\) dual handle probes;
- \(r-1\) rough-boundary loop probes;
- \(s-1\) smooth-to-smooth arc probes.

To separate dual logical strings, the primal probe basis contains:

- \(2g\) primal handle probes;
- \(s-1\) smooth-boundary loop probes;
- \(r-1\) rough-to-rough arc probes.

Each list has \(k\) entries. Omitting any basis probe leaves a nonzero logical
class in the common kernel. In particular, closed-loop ports alone are blind
to the relative arc coordinates created by disconnected condensing boundary.

## Algebraic faithfulness is not simultaneous measurement

The \(2k\) probe functionals are jointly faithful as an algebraic coordinate
map on Pauli classes. Their corresponding quantum observables are not one
commuting sharp measurement family. In a symplectic basis,

\[
Z_iX_j=(-1)^{\delta_{ij}}X_jZ_i.
\]

All \(Z\)-type logical probes form one commuting setting and all \(X\)-type
probes form another. When \(k>0\), at least two incompatible sharp settings are
required to access both sectors without replacing the measurement model. The
rank-zero mixed annulus requires no logical setting. Measuring one
setting on a single unknown logical state generally disturbs information in
the other.

Thus three claims must remain separate:

1. \(k\) probes separate one CSS quotient;
2. \(2k\) algebraic bits label a logical Pauli coset;
3. full logical-state tomography requires expectation data beyond one sharp
   joint measurement and is not supplied by the \(2k\)-bit label map.

## Pair-of-pants witness

For \(g=0,b=3,r=2,s=1\), \(k=1\). The primal logical is a rough-to-rough arc
and its minimal dual probe is a rough boundary loop. The dual logical is a
rough boundary loop and its minimal primal probe is a rough-to-rough arc. The
two probes anticommute. Algebraically two bits identify the four Pauli cosets,
but no single sharp two-bit PVM measures both.

## Detection, separation, and reconstruction

Local syndrome detects endpoints but is constant on the logical quotient.
The minimal relative probes separate Pauli cosets modulo stabilizers. They do
not select a decoder, reconstruct an arbitrary density matrix, or supply a
joint physical instrument for incompatible observables.

## Falsifiers

- fewer than \(k\) binary rows claimed injective on one CSS sector;
- fewer than \(2k\) rows claimed faithful on the full Pauli quotient;
- omission of an arc row with no resulting kernel;
- a claimed simultaneous sharp measurement whose logical probes anticommute;
- promotion of Pauli-coset labels to full state tomography.

## Disposition

The minimal algebraic probe count is topologically exact: \(k\) per CSS
sector and \(2k\) for the full Pauli quotient. Mixed boundaries force arc
ports into every minimal family. Quantum coefficients impose a separate
instrument obstruction: the two minimal CSS families are incompatible sharp
settings.

## Claim strength

Exact finite quotient-readout and incompatibility theorem.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_mixed_boundary_minimal_probes.py`.
The result is written to
`research/kitaev/results/mixed-boundary-minimal-probes.json`.
