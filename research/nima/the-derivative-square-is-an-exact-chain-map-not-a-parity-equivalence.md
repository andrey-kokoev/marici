# The derivative square is an exact chain map, not a parity equivalence

## Scope

Aspect's acquisition analogy demands that the corrected parity sectors retain both their source metrics and their typed comparison map. This note freezes the derivative commuting square on the common Laguerre core and separates it from any claim of bounded equivalence.

Let

\[
B_-=A+\frac12
\]

on the normalized even Laguerre carrier with parameter \(-\tfrac12\), and let

\[
B_+=A+\frac12
\]

on the normalized odd Laguerre carrier with parameter \(+\tfrac12\).

The two \(B\)-operators have the same skew-Jacobi form but different recurrence weights.

## Direct and shifted completion operators

The direct odd completion is

\[
P_+=A(A+1)=B_+^2-\frac14.
\]

The operator acting on the even potential before differentiation is

\[
Q_-=(A-1)A.
\]

In the centered even coordinate,

\[
Q_-=
\left(B_--\frac32\right)
\left(B_--\frac12\right)
=
B_-^2-2B_-+\frac34.
\]

This is not the direct even completion

\[
P_-=B_-^2-\frac14.
\]

## Derivative bridge

In normalized Laguerre coordinates, define \(\mathsf D\) on finite sequences by

\[
\mathsf D E_k
=
-\sqrt{2\pi(k+\tfrac12)}\,O_k
-\sqrt{2\pi k}\,O_{k-1}.
\]

The analytic differential identity gives the exact commuting square

\[
P_+\mathsf D
=
\mathsf D Q_-
\]

on the finite Laguerre core.

This square is the correct replacement for the false common-\(J_3\) identification.

## Why this is not a similarity

The derivative bridge is:

- densely defined;
- closed after graph completion;
- injective;
- unbounded;
- not bounded below;
- and has nonclosed range.

Therefore one may not write

\[
P_+=\mathsf DQ_-\mathsf D^{-1}
\]

as a bounded operator similarity. The inverse is not continuous on the derivative range.

The square expresses a chain map between distinct metric carriers, not equality of coordinate matrices and not unitary equivalence.

## Closure gate

The finite-core identity does not automatically determine the maximal closed-domain identity. The completed theorem must prove

\[
\mathsf D\operatorname{Dom}(Q_-)
\subseteq
\operatorname{Dom}(P_+)
\]

and

\[
P_+\mathsf Df=\mathsf DQ_-f
\]

for every \(f\) in the declared source domain.

A safe source domain is a common invariant analytic core, such as the appropriate Schwartz/Gaussian polynomial core. To pass to graph closure, one needs a core theorem for the joint graph norm

\[
\|f\|^2+
\|\mathsf Df\|^2+
\|Q_-f\|^2+
\|P_+\mathsf Df\|^2.
\]

Separate essential self-adjointness statements for the Jacobi operators do not alone prove this joint-core property.

## Metric covariance

Let \(U_-\) and \(U_+\) denote the source-normalized Laguerre synthesis maps. The analytic derivative and coefficient bridge must satisfy

\[
U_+\mathsf D_{\mathrm{coeff}}
=
\partial_x U_-
\]

on finite sequences and then on the closed graph domain.

This equation prevents reduced Laguerre coordinates from becoming independent metric authority: all coefficients, adjoints, and graph norms are pulled back from the analytic source spaces.

## Result

The corrected parity relation is the typed chain map

\[
(P_+,\mathcal H_+)
\;\xleftarrow{\ \mathsf D\ }\;
(Q_-,\mathcal H_-),
\qquad
P_+\mathsf D=\mathsf DQ_-.
\]

It is not a common matrix and not a bounded conjugacy. The next analytic gate is the joint-core/closure theorem that promotes this finite commuting square to the completed source graph.
