# Hadamard four blocks reconstruct the full ordered polarization

Date: 2026-09-08

## Exact reconstruction

Let the resolved tail/output-wall Gram be

\[
K=\begin{pmatrix}T&C\\C^*&O\end{pmatrix}.
\]

After the canonical Hadamard change of ports, write its four ordered blocks as

\[
HKH=\begin{pmatrix}P&Q\\R&N\end{pmatrix}.
\]

Direct expansion gives

\[
P-N=C+C^*,\qquad Q-R=C^*-C,
\]

and, crucially,

\[
C=\frac{P-N-Q+R}{2}.
\]

The diagonal source forms are also recovered:

\[
T=\frac{P+N+Q+R}{2},\qquad
O=\frac{P+N-Q-R}{2}.
\]

Thus all four Hadamard blocks reconstruct the entire ordered resolved Gram.
The diagonal energies `P,N` recover only the Hermitian cross term.  The
ordered off-diagonal blocks `Q,R` are exactly what retains the skew-Hermitian
reciprocal orientation.

## Reduction of the next comparison

The target of the Pauli/Adams comparison is now explicit on both sides:

1. form the four theta-history Hadamard blocks `P,Q,R,N` before any output
   summation;
2. compare them to the faithful four Pauli linking blocks;
3. use `C=(P-N-Q+R)/2` to descend the ordered wall-tail polarization.

This is compatible with the existing Pauli module reduction: one base channel
and its phase intertwiner generate the remaining blocks.  It also gives a
finite falsifier: any proposed comparison that supplies only `P+N` or `P-N`
cannot recover the skew cross term and is not faithful.

## Boundary

This algebraic reconstruction does not construct the theta source intertwiner
or establish common-domain closure.  It removes ambiguity about which finite
blocks must be compared and proves their sufficiency.

## Evidence

- `check_marici_rh_hadamard_four_block_reconstruction_20260908.py`
- `marici_rh_hadamard_four_block_reconstruction_certificate_20260908.json`
