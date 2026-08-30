# Positive canonical generators cannot retain the real reciprocal eigenpair

## Spectral no-go theorem

The empty two-dimensional symplectic cone has a stronger invariant form.

Let \(\Omega\) be nondegenerate and skew-Hermitian, and suppose

\[
H=\Omega A_1=H^{*}\ge0.
\]

Then

\[
A_1=\Omega^{-1}H.
\]

On the positive support of \(H\), the nonzero spectral part of \(A_1\) is equivalent to the skew-Hermitian operator

\[
H^{1/2}\Omega^{-1}H^{1/2}.
\]

Indeed, the usual \(AB\)-\(BA\) correspondence identifies their nonzero spectra. Therefore every nonzero eigenvalue of a positive canonical spectral generator lies on the imaginary axis, with the expected qualifications at the radical.

The reciprocal tail symbol

\[
A_1^{\mathrm{tail}}
=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}
\]

has the real nonzero eigenpair \(\{-1,+1\}\). Hence it cannot be a reducing block of any positive canonical generator.

## Stronger consequence for augmentation

A direct-sum extension by spectrally inert wall or archimedean coordinates leaves the real eigenpair in the spectrum:

\[
\mathcal A_1
=
A_1^{\mathrm{tail}}\oplus A_1^{\mathrm{aux}}.
\]

No nondegenerate skew form can then make

\[
\Omega\mathcal A_1\ge0
\]

on the full reachable support while the real tail modes remain reducing and nonradical.

Thus successful completion must alter the spectral dynamics, not merely add positive energy. At least one added source channel must couple to the tail modes in \(\mathcal A_1\), so that the real hyperbolic pair is converted into imaginary canonical motion or routed into an authorized radical.

## Three possible mechanisms

1. Spectral coupling: off-diagonal \(z\)-dependent incidence changes the eigenstructure of the enlarged \(\mathcal A_1\).
2. Constraint reduction: the real tail eigenvectors are removed by a source constraint before the positive canonical quotient is formed.
3. Krein retention: the real pair remains, and the programme must use indefinite-system machinery rather than de Branges positivity.

Only the first two can support the proposed positive Hermite–Biehler route.

## Source inventory refinement

For every wall, square, or archimedean channel, it is no longer enough to ask whether it carries positive Green energy. One must determine whether it carries spectral incidence:

\[
\partial_z\mathcal A(z)\big|_{z=0}.
\]

The decisive entries are the off-diagonal tail-to-auxiliary and auxiliary-to-tail blocks of \(\mathcal A_1\). If both vanish, that channel cannot repair the hyperbolic spectral pair through positive canonical geometry.

## Completion test

At cutoff \(X\), let \(\mathcal A_{1,X}\) be the enlarged spectral symbol. A necessary finite test is

\[
\sigma(\mathcal A_{1,X}|_{\mathrm{reachable}/\mathrm{radical}})
\subset i\mathbb R.
\]

But cutoffwise imaginary spectrum is not sufficient. The source-selected symplectic forms and positive supports must remain uniformly nondegenerate, and nonnormal pseudospectral growth must be controlled.

This produces a cheap next falsifier: compute the complete source \(z\)-coefficient before any Green estimate. If the reciprocal \(\pm1\) pair survives as a reducing block, the positive canonical-system route is already impossible.
