# Fourier-square Green naturality forces wall-tail orthogonality

## Symmetry reduction

The wall and tail planes have different characters under the square of Fourier transport.

On

\[
W_{\mathrm{wall}}
=
\operatorname{span}\{1,\delta_0\},
\]

Fourier satisfies

\[
F^2=+I.
\]

On

\[
W_{\mathrm{tail}}
=
\operatorname{span}\{K,V\},
\]

the quarter-turn law gives

\[
F^2=-I.
\]

This distinction can force the unresolved cross polarization to vanish.

## Orthogonality theorem

Let \(g_s\) be the source Green form on the boundary fiber at parameter \(s\). Reciprocal Fourier–Tate transport sends the \(s\)-fiber to the \(1-s\)-fiber. Applying it twice returns to the \(s\)-fiber.

Assume the twice-transported Green form is natural:

\[
g_s(F^2x,F^2y)=g_s(x,y).
\]

For \(x\in W_{\mathrm{wall}}\) and \(y\in W_{\mathrm{tail}}\),

\[
g_s(x,y)
=
g_s(F^2x,F^2y)
=
g_s(x,-y)
=
-g_s(x,y).
\]

Therefore

\[
g_s(x,y)=0.
\]

Hence the wall-tail cross block vanishes exactly:

\[
C_{\mathrm{wt}}=0.
\]

The normalized Schur margin is then maximal, and the joint boundary Green form is the orthogonal sum of its two already-controlled incidence planes.

## Why one Fourier step is not needed

Off the seam, one Fourier–Tate step changes \(s\) to \(1-s\), so fixed-fiber Fourier invariance is the wrong statement. The square returns to the original fiber and is sufficient.

The exact source identity required is

\[
(F_{1-s}F_s)^{*}
G_s
(F_{1-s}F_s)
=
G_s,
\]

with the frozen phase convention. If the square is a central phase, the phase cancels in the Hermitian form. If it contains a noncentral comparison cell, that cell must be included explicitly.

## Consequence for the five margins

If Fourier-square Green naturality holds, no independent wall-tail loading estimate remains. The local Green form decomposes as

\[
G_{\partial,s}
=
G_{\mathrm{wall},s}
\oplus
G_{\mathrm{tail},s}.
\]

Mixed cancellation can still occur downstream when the scalar Riemann matrix coefficient combines observer outputs. That is the existing terminal \(\delta_{\mathrm{mix}}\) gate. It is distinct from Green-form cross polarization, which symmetry kills.

## Completion

Exact orthogonality is stable under completion provided:

1. \(F_s\) and \(F_{1-s}\) extend to the completed rigged fibers;
2. their composite preserves the closed Green form;
3. the wall and tail spectral projectors remain continuous;
4. no boundary anomaly is introduced by closure.

Approximate naturality is weaker. If

\[
\|(F^2)^{*}G_sF^2-G_s\|\le\varepsilon,
\]

one obtains only an \(O(\varepsilon)\) cross block, which still needs a Schur estimate.

## Hostiles

A scalar Fourier functional equation may hold while the operator Green form fails square naturality. Scalar agreement cannot force \(C_{\mathrm{wt}}=0\).

A projective Fourier square with a scalar unit phase is harmless. A state-dependent phase or nonunitary comparison cell can generate a nonzero cross block despite correct scalar reciprocity.

A finite naturality identity may fail after closure through a boundary anomaly concentrated on the wall.

## Frontier

The global wall-tail calculation has reduced to one symmetry theorem:

> Prove Fourier-square naturality of the closed source Green form on the complete boundary fiber.

If proved, wall-tail orthogonality is automatic and the next unresolved gate is the terminal scalar mixed-cancellation margin rather than another Green assembly estimate.
