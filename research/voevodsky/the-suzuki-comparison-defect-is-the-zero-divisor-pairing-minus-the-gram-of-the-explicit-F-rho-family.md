# Coordinate restatement of the Suzuki comparison defect

## Status correction

The essential off-axis signature obstruction and the impossibility of a second positive Suzuki factorization were already proved in `suzuki-squared-factorization-meets-an-off-axis-two-by-two-signature-obstruction.md`. This note only rewrites that established obstruction in finite divisor-Gram coordinates. It is not a new route to positivity, and the divisor-pairing matrix notation requires the same normalization and interpolation hypotheses as the prior localized-zero argument.

## Source-explicit Suzuki expansion

Suzuki's source-explicit screw line admits the expansion

\[
S_t(z)
=
\sum_{\rho}
c_\rho(t)F_\rho(z),
\]

where

\[
F_\rho(z)
=
\frac{
m_\rho i(1+
\Theta(z))
}
{2(z-\rho)}
\]

and \(c_\rho(t)\) is the explicit exponential increment coefficient appearing in the screw-line formula. For the standard convention it is proportional to

\[
e^{-i\rho t}-1.
\]

The expansion and the fact that \(S_t\in L^2(\mathbb R)\) are unconditional. Orthogonality of the \(F_\rho\) family is not unconditional.

## Finite divisor packet

Let \(Z\) be a finite zero packet closed under the functional-equation and conjugation symmetries. Define the synthesis map

\[
\mathcal F_Z:
\mathbb C^Z
\to
L^2(\mathbb R)
\]

by

\[
\mathcal F_Za
=
\sum_{\rho\in Z}
a_\rho F_\rho.
\]

Its positive Gram matrix is

\[
G_{F,Z}
=
\mathcal F_Z^*
\mathcal F_Z.
\]

For the coefficient vector

\[
c_Z(t)
=
(c_\rho(t))_{\rho\in Z},
\]

the truncated Suzuki kernel is

\[
G_{Suz,Z}(t,u)
=
\frac12
c_Z(u)^*
G_{F,Z}
c_Z(t).
\]

This kernel is positive for every finite packet because \(G_{F,Z}\succeq0\).

## Arithmetic divisor pairing

The zero side of the polarized explicit formula defines a Hermitian divisor-pairing matrix

\[
J_{\Xi,Z}.
\]

It includes multiplicities and pairs each zero coordinate according to the completed functional-equation involution. The corresponding arithmetic screw kernel is

\[
G_{arith,Z}(t,u)
=
\frac12
c_Z(u)^*
J_{\Xi,Z}
c_Z(t).
\]

When every zero lies on the fixed line, the involution fixes each spectral coordinate and the normalized divisor pairing becomes the identity:

\[
J_{\Xi,Z}=I.
\]

For an off-axis orbit, \(J_{\Xi,Z}\) contains a hyperbolic block and is indefinite.

## Exact comparison defect

Subtracting the two independently defined kernels gives

\[
\Delta_{Suz,Z}(t,u)
=
G_{arith,Z}(t,u)
-
G_{Suz,Z}(t,u)
\]

with the exact factorization

\[
\Delta_{Suz,Z}(t,u)
=
\frac12
c_Z(u)^*
(
J_{\Xi,Z}-G_{F,Z}
)
c_Z(t).
\]

Thus the Suzuki comparison defect is the mismatch between:

1. the arithmetic Hermitian metric on divisor coefficients;
2. the ordinary positive \(L^2\) Gram metric of the explicit \(F_\rho\) family.

No endpoint, gamma, or prime term is missing from this formula: they are already incorporated in \(S_t\), \(\Theta\), and the completed divisor pairing.

## Critical-line specialization

Under the critical-line condition, Suzuki proves that the normalized \(F_\rho\) form an orthonormal basis of the model space. Hence

\[
G_{F,Z}=I
\]

on every finite packet. Since also

\[
J_{\Xi,Z}=I,
\]

one gets

\[
\Delta_{Suz,Z}=0.
\]

This recovers the screw-kernel identity without hiding its two ingredients: fixed-line divisor metric and orthonormality of the model-space family.

## Off-axis orbit

For an off-axis functional-equation orbit, the arithmetic metric has a negative direction. The \(L^2\) Gram remains positive semidefinite.

Therefore

\[
J_{\Xi,Z}-G_{F,Z}
\]

cannot vanish on the full coefficient space. Suzuki's converse constructs coefficient vectors, realized by compactly supported tests, that expose this mismatch as a negative arithmetic value against a nonnegative \(L^2\) norm.

Thus the comparison defect detects exactly the hostile divisor geometry.

## Infinite packet

Let \(Z_N\) be symmetry-closed finite divisor packets exhausting the zero multiset. On source tests for which the explicit formula and Suzuki expansion converge, the coefficient vectors and pairings have compatible limits.

The infinite comparison defect is the form limit

\[
\Delta_{Suz}
=
\lim_N
\frac12
c_{Z_N}^*
(
J_{\Xi,Z_N}-G_{F,Z_N}
)
c_{Z_N}.
\]

A publication-level statement requires the convergence estimates from Suzuki's \(L^2\) expansion and the completed explicit formula. The finite-packet identity itself is algebraic.

## Relation to Krein--Langer

The negative index of the completed divisor pairing is the same forbidden-divisor phenomenon recorded analytically by the Krein--Langer model space \(K_B\).

The matrix

\[
J_{\Xi,Z}-G_{F,Z}
\]

is therefore the zero-coordinate presentation of the same comparison obstruction whose strip-kernel presentation is

\[
K_S-K_B.
\]

An explicit unitary identification between its negative range and the corresponding finite section of \(K_B\) still requires the model-space interpolation map. That identification is classification, not a positivity proof.

## Consequence for the larger-positive-bulk search

Suzuki's kernel supplies a genuine unconditional positive bulk, but the arithmetic readout is not obtained from it by deleting only an endpoint line. The comparison metric already changes on off-axis divisor coordinates.

Hence the hoped-for identity

\[
\Delta_{Suz}
=
-
b^*b
\]

cannot hold in the presence of an interior defect. The correct defect must include the full divisor/Krein--Langer sector.

Structurally,

\[
\Delta_{Suz}
=
-
A_B^*A_B
-
b^*b
+
R_{metric},
\]

where \(R_{metric}\) records any remaining mismatch between the normalized divisor metric and the \(L^2\) Gram of the \(F_\rho\) synthesis family. Under the critical-line orthonormal-basis theorem, every term vanishes in the required normalization.

## What is gained

The comparison defect is no longer an unspecified endpoint--gamma--prime remainder. It has an exact finite-packet coordinate:

\[
J_{\Xi,Z}-G_{F,Z}.
\]

This gives a concrete target for symbolic and certified numerical work:

1. compute finite \(F_\rho\) Gram matrices;
2. compare them with the functional-equation divisor metric;
3. identify their negative mismatch with finite model-space sections;
4. track convergence over symmetry-closed exhaustions.

## What remains irreducible

Proving the arithmetic kernel positive would require showing that the source never detects a negative divisor direction. The translated-Gaussian source is divisor-faithful, so this is equivalent to absence of that direction.

Therefore the Suzuki comparison does not bypass the final arithmetic gate. It supplies the clearest explicit coordinate system for it.

## Disposition

Prior research does contain the desired larger unconditional positive kernel. Its exact arithmetic comparison defect is the divisor-pairing metric minus the positive Gram metric of Suzuki's explicit \(F_\rho\) family.

The remaining obstruction is not an unknown mixed local term; it is the failure of those two completed metrics to coincide off the critical-line geometry.
