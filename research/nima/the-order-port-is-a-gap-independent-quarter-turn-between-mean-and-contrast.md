# The order port is a gap-independent quarter-turn between mean and contrast

## Two instruments

On two ordered arithmetic labels, a positive Mellin window has Gram matrix

\[
P_\rho=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix},
\qquad
0<\rho<1.
\]

For adjacent logarithmic labels, \(\rho\to1\). In the mean and contrast
basis

\[
u=\frac1{\sqrt2}(1,1)^T,
\qquad
v=\frac1{\sqrt2}(-1,1)^T,
\]

the eigenvalues are \(1+\rho\) and \(1-\rho\). The positive instrument is
faithful at every finite separation, but its contrast sensitivity collapses.

The source order operator is

\[
S=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]

It satisfies

\[
Su=v,
\qquad
Sv=-u,
\qquad
S^2=-I.
\]

Thus source order is a gap-independent quarter-turn between the stable mean
channel and the escaping contrast channel.

## Consequence

The order port does not repair the positive Gram matrix by rescaling its small
eigenvalue. It supplies a distinct instrument that transports the well-observed
mean direction into the poorly observed contrast direction.

This separates three operations:

1. positive window: measures magnitude;
2. scale jet: measures infinitesimal logarithmic separation;
3. order port: remembers which label lies on which side, independently of gap.

The third operation is the discrete valuation port demanded by the completion
obstruction. It is not generated continuously from the positive window.

## Clifford form

The pair \((u,v)\) carries a real two-dimensional Clifford module with complex
structure \(S\). Reversing source order sends \(S\) to \(-S\), so the
orientation sign is explicit rather than hidden in a scalar phase.

The positive form and the order operator together retain both magnitude and
orientation. Neither alone does:

- \(P_\rho\) loses uniform contrast sensitivity;
- \(S\) is skew and has no positive energy interpretation.

## Remaining theta/Tate gate

This finite model becomes relevant to RH only if the theta/Tate source derives
the same order operator and its boundary coupling. The decisive calculation is
the old/new conductor block of \(S\) on the Mellin-jet tower.

The proposed coupling passes only if:

- its finite matrix entries are source-derived;
- its off-diagonal block remains bounded in the admitted completion;
- its boundary residual is exactly the typed primitive, square, seam, and
  archimedean packet;
- no additional bulk term remains;
- scalar projection occurs only after the positive and oriented instruments
  have been coupled.

The smallest falsifier is already two-dimensional: if the source order block
does not send mean to contrast with the declared sign, the quarter-turn model
does not instantiate.

