# Algebraic wave-plate and interferometer certificates

## Question

How can balanced interferometers and quarter-phase polarization analyzers be certified exactly when their matrices contain \(1/\sqrt2\) and \(i\)?

## Claim boundary

This packet implements the exact number field \(\mathbb Q(\sqrt2,i)\) for two-mode analyzers. It certifies unitary transformations and rank-one effects. It does not yet cover arbitrary wave-plate angles or transcendental dispersive phases.

## Exact field

Represent each scalar as

\[
(a+b\sqrt2)+i(c+d\sqrt2),
\qquad a,b,c,d\in\mathbb Q.
\]

Multiplication reduces \((\sqrt2)^2\) to two and \(i^2\) to minus one. Conjugation negates the imaginary coefficients. This gives exact arithmetic in the compositum

\[
K=\mathbb Q(\sqrt2,i).
\]

The balanced amplitude is represented exactly as

\[
\frac1{\sqrt2}=\frac{\sqrt2}{2}.
\]

## Analyzer generators

The balanced path interferometer is

\[
H=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
\]

The quarter-phase element is

\[
S=
\begin{pmatrix}
1&0\\
0&i
\end{pmatrix}.
\]

Exact field arithmetic proves

\[
H^\dagger H=I,
\qquad
S^\dagger S=I.
\]

It also verifies the analyzer identities

\[
HZH=X
\]

and

\[
SXS^\dagger=Y.
\]

These connect which-path analysis to interference and linear polarization analysis to circular-phase analysis without decimal approximations.

## Exact detector effect

For output projector

\[
P_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]

the pulled analyzer effect

\[
E=U^\dagger P_0U
\]

for \(U=SH\) is Hermitian, idempotent, trace one, and positive semidefinite. Principal minors lie in the real subfield \(\mathbb Q(\sqrt2)\); their signs are decided exactly by comparing rational squares rather than decimal embeddings.

## Positivity ordering

For \(x=a+b\sqrt2\), its sign is exact:

- equal signs of \(a\) and \(b\) are immediate;
- for opposite signs, compare \(a^2\) with \(2b^2\), retaining the sign of the dominant term.

A Hermitian matrix over \(K\) is positive semidefinite when all principal determinants are real and nonnegative under this ordering.

## Decimal-coercion falsifier

Replacing \(1/\sqrt2\) by \(707/1000\) gives

\[
H_{\rm dec}^\dagger H_{\rm dec}
=rac{999698}{1000000}I
\ne I.
\]

The decimal matrix is close to unitary but is not exactly unitary. An exact certificate must therefore retain the algebraic generator or use an outward interval with a residual bound; decimal closeness cannot be promoted to an identity.

## Disposition

The field \(\mathbb Q(\sqrt2,i)\) exactly supports balanced splitters, quarter-phase elements, and their analyzer effects. Unitarity, Hermiticity, projector structure, and positivity become checkable identities. Arbitrary source angles require adjoining their algebraic values or using interval-certified transcendental functions.
