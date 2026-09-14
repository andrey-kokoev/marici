# Prior-research audit of the additive--multiplicative crossing

Date: 2026-09-08

## Global comparison exists

Mellin transport is already a source-derived additive-to-multiplicative comparison:

\[
\int_0^\infty e^{-\pi n^2t}t^{s/2-1}\,dt
=
\pi^{-s/2}\Gamma(s/2)n^{-s}.
\]

In the Euler chamber, absolute convergence permits sum/integral interchange; Poisson reflection and retained polar currents complete the square.  This explains why the additive theta and multiplicative Euler constructions have the same completed scalar section.

It does not construct the shell-to-cyclic-square map needed by the Green residual.  Point evaluation after Mellin transport is not faithful to the labelled source, and the comparison is compatible with scalar off-seam cancellation.

## Scalar Adams-two target is insufficient

A single cyclic-square coordinate `p^-2/4` cannot reproduce the finite-shell density

\[
\rho_{a,b}(t)=\int_a^b\Phi(x)\Phi(x+t)\,dx.
\]

Laplace-transform injectivity shows that equality for all `z` requires equality of the complete densities, including every separation moment.  Matching one Watson coefficient or asymptotic prime order supplies only one scalar.

Therefore the proposed map

\[
T_{\theta\to\mathrm{cyc}2,p}
\]

cannot land in the bare one-dimensional Adams-two coordinate.  Any viable target must retain a separation-history module or an infinite even-grade response.

## Available replacement structures

Prior research supplies two partial structures:

1. the global Mellin cell, which is source-authorized but divisor-neutral;
2. the relative Haar comparison
   \[
   J:L^2(dx)\supset\operatorname{Dom}J\to L^2(dx/x),
   \]
   whose positive energy has exact cocycle
   \[
   \mathcal E(V_s(p)f)
   =p^{1-2\operatorname{Re}s}\mathcal E(f).
   \]

The second identifies the critical seam as the unit-energy locus, but its domain excludes uncancelled endpoint constants.  The completed boundary-renormalization/domain theorem and zero-to-state bridge remain open.

## Disposition

The repository contains a global additive--multiplicative comparison but no faithful finite-shell crossing into the conservative response carrier.  Adams two is only a leading arithmetic coordinate.  The remaining candidate must preserve the full separation density, for example by tensoring the cyclic-square carrier with the ratio/history graph, and must prove that the completed boundary-corrected Evans state lies in the relative Haar form domain.

## Evidence

- `research/grothendieck/mellin-transport-is-the-additive-to-multiplicative-comparison-cell.md`
- `research/nima/a-single-adams-two-cyclic-square-coordinate-cannot-reproduce-the-finite-shell-autocorrelation-density.md`
- `research/nima/theta-relative-haar-operator-has-the-exact-critical-energy-cocycle.md`
