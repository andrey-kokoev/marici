# Memory-one magnetic determinants have scalar factored transfers

Companion to checkers/magnetic_memory_one_checks.py (8/8, exit 0) and
results/magnetic_memory_one.json.

For reflection distances \(q=2,3\), the support memory is one pole pair.
Nevertheless, the exact determinant evolution of the nested Hall minor
collapses to a scalar ratio.

Set \(a=2k\). The observed closed laws are

\[
\frac{D_{g,2,k}}{D_{g,2,k-1}}
=2g(g+3)\,
a^{\overline g}a^{\overline{g-1}}(a+g+1)
\]

and

\[
\frac{D_{g,3,k}}{D_{g,3,k-1}}
=-\left(a^{\overline g}\right)^2(a+g-4)(a+g+2).
\]

They reproduce all 180 exact ratios over

\[
2\le g\le10,\qquad q\in\{2,3\},\qquad3\le k\le12
\]

with zero residual.

## Schur-complement proof

In the recursively ordered extension, the new rows touch only the preceding
pole pair. For \(q=2\), support forces the Schur complement to have shape

\[
S_{g,2,k}=\begin{pmatrix}*&u\\v&0\end{pmatrix}.
\]

The correction containing the entire older boundary state changes only the
starred entry. The direct endpoint entries are, including their parity signs,
proportional to

\[
u=2g(g+3)a^{\overline{g-1}},\qquad
v=(a+g+1)a^{\overline g}.
\]

Thus \(\det S=-uv\), with the endpoint parity producing the positive displayed
\(q=2\) multiplier.

For \(q=3\),

\[
S_{g,3,k}=\begin{pmatrix}u&0\\ *&v\end{pmatrix}.
\]

Again the state-dependent correction occupies only the starred entry, while

\[
u=(a+g+2)a^{\overline g},\qquad
v=(a+g-4)a^{\overline g}
\]

with net negative endpoint parity. Hence the determinant is the displayed
\(q=3\) factor.

Every stable \(q=2\) multiplier is positive. Every stable \(q=3\) multiplier
is negative and nonzero; its only potentially relevant zero is
\(a+g-4=0\), outside \(k\ge3,g\ge2\). Thus neither memory-one family exhibits
a late actual-weight singularity in the tested range.

A deliberate replacement of the \(q=2\) endpoint factor \(a+g+1\) by
\(a+g\) produces residual 508032 at \((g,k)=(3,3)\), so the factor law is
sharp rather than an underconstrained fit.

Therefore the two formulas hold for arbitrary \(g\ge2\) and every stable
\(k\ge3\). The 180 exact matrices are independent cross-checks of the symbolic
Schur theorem. Initial cutoffs remain a finite boundary problem.
