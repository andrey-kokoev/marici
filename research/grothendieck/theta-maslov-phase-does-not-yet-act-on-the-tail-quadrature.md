# The Maslov phase does not yet act on the theta-tail quadrature

## Source-identity audit

Packet 149 observes that opposite phases `+pi/4` and `-pi/4` would select
complementary quadratures. The required gate is whether those phases act on
the same amplitude frame as the doubled theta-tail energy.

The existing source constructions answer this negatively at their current
typing level.

## Theta matrix-coefficient frame

The adelic Fourier transform is the metaplectic quarter-turn and satisfies

\[
 \mathcal F R_u\mathcal F^{-1}=R_{-u}.
\]

With self-dual Haar normalization, the arithmetic comb is fixed:

\[
 \mathcal F\Delta_{\mathbb Q}=\Delta_{\mathbb Q}.
\]

The completed Gaussian-derived source is also Fourier-fixed in the chosen
theta convention. Therefore the matrix coefficient

\[
 \mathcal A(u)=\langle\Delta_{\mathbb Q},R_uf\rangle
\]

transforms by reversal of the dilation parameter,

\[
 \mathcal A(u)=\mathcal A(-u),
\]

without acquiring an amplitude-frame phase `exp(+/- i pi/4)`.

At the two-copy level, tensoring two Fourier-fixed endpoints still produces
a fixed frame. The quarter-turn acts on phase-space polarization and source
transport, but no relative `pi/2` rotation of the real/imaginary scalar
quadratures has yet been derived.

## Oscillator determinant frame

The archimedean gamma factor has a different construction:

\[
 \Gamma(1/4+z)
 =\frac{\sqrt{2\pi}}{\det_\zeta(A+z)},
\]

where `A` is the scaled even harmonic oscillator. Its eighth phase arises
from zero-point/parity data and the asymptotics of a regularized determinant,
or equivalently from an oriented Gaussian/Fresnel half-form.

This is determinant-line phase data. It is not presently an eigenphase of the
theta source or comb in the matrix-coefficient carrier.

Thus the two appearances of the metaplectic group occupy different levels:

\[
 \begin{array}{c|c}
 \text{theta overlap}&\text{Fourier-fixed state/boundary matrix coefficient}\\
 \text{gamma sector}&\text{oscillator determinant/half-form phase}.
 \end{array}
\]

Equal numerical angles do not provide a comparison map between these levels.

## Disposition of the complementary-phase shortcut

The implication

\[
 \text{opposite gamma Maslov phases}
 \Longrightarrow
 \text{complementary doubled-tail quadratures}
\]

is currently unsupported. In the normalized theta matrix coefficient, the
visible Fourier eigenphases cancel to one. Packet 149 remains an exact
conditional algebra theorem, but its proposed source identification is not
established by the existing metaplectic constructions.

## Remaining admissible bridge

A comparison could still arise at the determinant-line level if the doubled
tail boundary problem has a canonical determinant/Pfaffian functor and its
Fourier transport carries the oscillator half-form. That would require a
commuting diagram

\[
 \begin{array}{ccc}
 \text{theta boundary system}&\longrightarrow&\text{determinant line}\\
 \downarrow\mathcal F&&\downarrow\text{Maslov lift}\\
 \text{reciprocal boundary system}&\longrightarrow&\text{determinant line}.
 \end{array}
\]

No such functor has yet been constructed. It is the same determinant bridge
already identified as missing in the puncture programme.

## Revised finite test

Do not insert `+/- pi/4` into the tail matrices. First derive `Q_X^+` and
`Q_X^-` directly in the Fourier-fixed theta frame. If they are complementary,
the mechanism is intrinsic to the two-sector Green system. Only afterward
test whether their determinant-line lift reproduces the oscillator Maslov
phase.

The smallest falsifier is equality of the two rank-one projectors in the
theta frame rather than complementarity. That would show that the missing
quadrature is not restored by sheet exchange at the matrix-coefficient level.

## Present boundary

This is a source-typing no-go for an immediate phase transfer, not a no-go for
a future determinant-line comparison. The complementary-sheet matrix
certificate remains live and must be calculated without importing the gamma
phase.

