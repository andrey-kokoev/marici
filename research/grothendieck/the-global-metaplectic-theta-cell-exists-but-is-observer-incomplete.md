# The global metaplectic theta cell exists but is observer-incomplete

## Question

Finite Euler cutoffs do not support Fourier–Poisson sewing.  Does the full
restricted theta source carry the missing two-carrier coherence cell, and if
so, does that cell act on the complete primitive, square, seam, connected,
and archimedean observer family?

## The global source cell

Use the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx.
\]

Let

\[
g(x)=e^{-\pi x^2}
\]

and let the unitary dilation group be

\[
(U_qf)(x)=e^{q/2}f(e^qx).
\]

The normalized Gaussian orbit is

\[
g_q(x)=U_qg(x)
=e^{q/2}e^{-\pi e^{2q}x^2}.
\]

Fourier transport reverses the scale exactly:

\[
\mathcal Fg_q=g_{-q},
\qquad
\mathcal FU_q=U_{-q}\mathcal F.
\]

Let

\[
\Delta_{\mathbb Z}=\sum_{n\in\mathbb Z}\delta_n
\]

be the arithmetic comb in the tempered-distribution boundary.  Poisson
summation is the distributional identity

\[
\mathcal F\Delta_{\mathbb Z}=\Delta_{\mathbb Z}.
\]

Hence Fourier acts on both legs of the prepared source–observer pair:

\[
(\Delta_{\mathbb Z},g_q)
\longmapsto
(\Delta_{\mathbb Z},g_{-q}).
\]

This is the first genuine global two-cell.  It lives in the rigging

\[
\mathcal S(\mathbb R)
\subset L^2(\mathbb R)
\subset\mathcal S'(\mathbb R),
\]

uses the full comb, and has no finite-cutoff antecedent.  Fourier unitarity
supplies its dagger.

## Scalar shadow

Pairing the two legs gives

\[
A(q)=\langle\Delta_{\mathbb Z},g_q\rangle.
\]

The global cell implies

\[
A(q)=A(-q).
\]

Thus the ordinary theta modular identity is the scalar matrix coefficient of
the stronger source-level correspondence.  The construction direction is
correct: the two Fourier identities precede the scalar equality.

## Why this is not yet the required cell

The cell is defined on the prepared Gaussian orbit and the comb observer.  It
does not yet act on the full observer family

\[
O=(O_{k=1},O_{k=2},O_{\ge3},O_{\mathrm{seam}},O_\infty).
\]

The primitive and square ports arise after multiplicative Tate/Euler
factorization and occupy different completion grades.  No source-derived
functor has yet been constructed from the additive Gaussian–comb
correspondence to those labelled ports.  The connected port is
absolute-summable rather than one Hilbert Gramian, and the archimedean line is
a determinant tensor extension.

Therefore only the comb component of the observer naturality diagram is
currently defined.  On that component, the global cell compresses to the
known scalar modular equality.  It has not recovered the labelled
off-diagonal information whose loss was identified earlier.

## Hostile universality test

The metaplectic relation itself is too universal to orient zeros.  Any
Fourier-fixed Schwartz source paired with a Fourier-fixed distribution obeys
the same reflection coherence.  The previously constructed degree-twelve
self-Fourier hostile source retains positive integer samples while its Mellin
window has off-critical zeros.

Thus global metaplectic coherence does not imply critical-line zero
confinement.

The missing information is not another proof of Fourier reciprocity.  It is
an observer lift that remembers the actual theta/Tate constructor grammar and
rejects the hostile source before scalar compression.

## The next exact square

Let (J) denote the still-unconstructed source trace from the additive
Schwartz carrier to the multiplicative boundary vessel.  The next square is

\[
J\mathcal F
\mathrel{?=}
\mathcal F_{\mathrm{Tate}}J.
\]

It must be interpreted as equality of maps into the Fourier-saturated
pro-Gram boundary family, including primitive, square, seam, connected, and
archimedean coordinates.  Agreement after applying only the scalar Tate
functional is insufficient.

The falsifier is a nonzero typed residual

\[
\mathfrak R(\phi)
=J(\mathcal F\phi)-\mathcal F_{\mathrm{Tate}}J(\phi)
\]

whose scalar comb pairing vanishes.  Such a residual would prove that the
functional equation hides an observer-level anomaly.

## Scope

The Gaussian dilation, Fourier reversal, comb invariance, and prepared-orbit
two-cell are exact.  Their lift to the complete theta/Tate observer family is
not constructed.  No zero-confinement statement follows.

## Result

The global metaplectic theta cell exists before scalarization, but only on the
Gaussian–comb prepared orbit.  It explains the modular reflection and
survives the rigged additive completion.  It remains observer-incomplete: the
arithmetic boundary ports have not been functorially lifted into the cell.
The RH-bearing target is now the full trace-naturality square, not Fourier
reciprocity itself.
