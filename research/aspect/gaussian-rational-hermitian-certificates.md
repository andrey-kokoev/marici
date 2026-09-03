# Gaussian-rational Hermitian certificates

## Question

Can the exact tomography certificate boundary support complex path-phase and circular-polarization effects without floating-point tolerances?

## Claim boundary

This packet extends the verifier to four-dimensional Hermitian matrices over Gaussian rationals \(\mathbb Q(i)\). It verifies exact certificates whose entries lie in this field. Algebraic phases outside \(\mathbb Q(i)\) still require a larger exact number field or interval enclosure.

## Exact scalar and matrix type

Represent every scalar as

\[
a+ib,
\qquad a,b\in\mathbb Q.
\]

Conjugation sends \((a,b)\) to \((a,-b)\). A matrix \(H\) is admitted as Hermitian only when

\[
H_{jk}=\overline{H_{kj}}
\]

for every entry. This check precedes positivity.

The Pauli matrix

\[
Y=
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix}
\]

and all two-qubit Pauli products then have exact Gaussian-rational entries. Path-phase and circular-polarization settings are therefore represented without decimal approximations.

## Exact positivity

For a Hermitian \(4\times4\) matrix, positive semidefiniteness is equivalent to nonnegativity of every principal minor. The verifier:

1. enumerates all fifteen nonempty principal submatrices;
2. computes each determinant exactly in \(\mathbb Q(i)\);
3. requires the imaginary part to vanish;
4. requires the rational real part to be nonnegative.

This handles semidefinite matrices, unlike a leading-principal-minor positive-definite test.

## Complex dual certificate

The rational dual construction is unchanged. For Hermitian \(W,A_i\), rational slab multipliers, and

\[
Z=W-yI-\sum_i\alpha_iA_i+
\sum_i\beta_iA_i,
\]

the exact Hermitian and principal-minor checks on \(Z\) certify the same lower bound.

As a phase-sensitive fixture, minimize

\[
\langle Y\otimes I\rangle
\]

subject to

\[
\langle Y\otimes I\rangle\ge1/2.
\]

The dual multiplier one gives zero slack and lower bound \(1/2\). The state

\[
\rho=\frac14
\left(I+\frac12Y\otimes I\right)
\]

is Hermitian, positive, trace one, and attains the bound. Its off-diagonal entries are nonzero imaginary Gaussian rationals, so the test exercises genuinely complex support.

## Corruption gates

Changing one off-diagonal entry without conjugating its transpose partner is rejected before positivity. Raising the dual scalar above the optimum makes the slack indefinite and is rejected by a negative principal minor.

A numerical candidate may be rationally reconstructed only provisionally. The reconstructed matrices and multipliers receive authority solely after all exact identities, inequalities, and margins pass this verifier. Closeness to solver output is not a certificate.

## Remaining boundary

Wave-plate angles may introduce algebraic values such as \(1/\sqrt2\), and continuous-mode operators may require interval-valued transcendental entries. Those cases need exact algebraic-number arithmetic or outward-rounded interval certificates. They must not be coerced into Gaussian rationals by decimal truncation.

## Disposition

Exact Gaussian-rational arithmetic suffices for all Pauli path–polarization settings, including phase-sensitive \(Y\) channels. Hermitian symmetry and all principal minors are verified exactly. The complex fixture proves a matching primal–dual optimum of \(1/2\) and rejects both conjugation and slack corruption.
