# Exceptional magnetic classes are failed local transport

Companion to checkers/magnetic_kernel_birth_checks.py (7/7, exit 0) and
results/magnetic_kernel_birth.json.

## Kernel-birth map

For a block extension

\[
M'=\begin{pmatrix}A&B\\C&E\end{pmatrix},
\qquad \det A\ne0,
\]

let \(S=E-CA^{-1}B\). Projection to the new coordinates identifies

\[
\ker M'\cong\ker S,
\]

with inverse

\[
y\longmapsto\begin{pmatrix}-A^{-1}By\\y\end{pmatrix}.
\]

Thus a new kernel direction is born exactly when the local Schur transport is
singular. Its global coefficients are the canonical lift of the local failed
direction.

## The q=7 birth

At \(g=2,q=7\), the cutoff-two prefix is invertible, with determinant

\[
265420800000.
\]

At cutoff three, append the two source columns and target rows \(-8,-7\).
The Schur block is

\[
S=\begin{pmatrix}-588&0\\-984&0\end{pmatrix},
\qquad
\ker S=\langle(0,1)\rangle.
\]

The lift is

\[
\begin{pmatrix}-A^{-1}B(0,1)\\0\\1\end{pmatrix}
=
\left(\frac12,0,0,0,0,-\frac32,0,1\right).
\]

After clearing denominators, its active coordinates are

\[
\boxed{(1,-3,2)}
\]

on the source points

\[
(0,-8),\qquad(4,2),\qquad(6,0).
\]

Hence the exceptional datum

\[
\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}
\]

is the transported image of one local null direction. Its integers are forced
by lifting through the invertible prefix.

The class persists with nullity one through every tested later cutoff
\(3\le k\le10\); no second class is born.

## The q=1 birth

At \(g=2,q=1\), there is no invertible prefix. The initial block is simply

\[
\begin{pmatrix}-40&-40\end{pmatrix},
\]

with primitive kernel \((1,-1)\). Thus \(1-\bar z^{-2}\) is a singular initial
condition, while the \(q=7\) circuit is a singular interior extension.

## Explanatory content and boundary

The two exceptions are now typed:

- \(q=1\): failed initialization;
- \(q=7\): failed continuation through one Schur step.

This exactly realizes the principle that exceptional kernel classes are
residues of singular finite transport. The checker proves the mechanism for
the two known exceptions. A global theorem still requires showing that every
other admissible transfer is nonsingular.

