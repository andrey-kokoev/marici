# Dilation-residue sum rule

## Bounded theorem

WP473 asks whether WP472's rate failure can be repaired merely by retuning
radial curvature coefficients while preserving the WP469 common-dilation lift.

For general positive `y` and `a`, the canonical vacuum dilation vector in the
ordered radial channels `(flavor, Higgs, singlet)` is

\[
d=(\sqrt3y,\sqrt{2a},1)^T,
\qquad d^Td=3y^2+2a+1.
\]

The source lift isolates the normalized projector

\[
P_D={dd^T\over d^Td}.
\]

It permanently consumes the Higgs-channel residue

\[
Z_D^{(H)}={2a\over3y^2+2a+1}.
\]

Spectral-projector completeness and positivity then bound every other single
radial pole by

\[
Z_r^{(H)}\leq1-Z_D^{(H)}
={3y^2+1\over3y^2+2a+1}.
\]

This statement is independent of `lambda`, `rho`, `eta`, `kappa`, and all
mass eigenvalues. Curvature retuning cannot evade it.

## Unit-geometry no-go

At `a=y=1`, every pole orthogonal to the lifted mode has

\[
Z_r^{(H)}\leq{2\over3}.
\]

The PDG rate gate used in WP472 requires at least `0.9516` on its frozen
95-percent working interval. Therefore no radial retuning within the unit
geometry can repair the Higgs rate. WP471 nearly saturates the exact `2/3`
ceiling, so its failure is structural rather than a poor choice of `eta`.

## Escape inequality and flavor-clock consequence

On the same mixing-only response domain, compatibility requires

\[
{3y^2+1\over3y^2+2a+1}\geq L,
\qquad L={2379\over2500}.
\]

Equivalently,

\[
a\leq{121(3y^2+1)\over4758}.
\]

Because the selector predicts `g_F f/v=g_F y sqrt(3/a)`, the rate instrument
implies the conditional lower bound

\[
{g_Ff\over v}\geq
g_Fy\sqrt{{14274\over121(3y^2+1)}}.
\]

At `y=1`, this is

\[
{g_Ff\over v}\geq g_F\sqrt{{7137\over242}}
\simeq5.43g_F.
\]

This is a physical constraint on the selector family, not numerical source
selection: `y` and `g_F` remain unfixed.

## Scope and falsifiers

The theorem assumes the lifted pole is spectrally isolated and that no new
production amplitude changes the mixing-only relation between residue and
signal strength. Its smallest falsifier is a source-derived production channel
that raises the rate without being represented by the Higgs projector.

Within the admitted domain, the unit geometry closes negative. Reopening must
change `(a,y)` within the exact inequality or add a separately derived
production operation; either route requires fresh masses, residues, widths,
and likelihoods.

