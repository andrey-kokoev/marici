# Curvature--flux balance fixes the clock and magnitude but not the sign: WP790

## Question

Can one physical compactification generate the two radius homogeneities
required by WP789?

Six-dimensional Einstein--Maxwell compactification on a curved two-sphere
provides precisely this architecture: internal curvature and magnetic flux
jointly stabilize the radion. A modern analysis of this system and its
AdS/Minkowski/dS branches is given by
[Seo](https://arxiv.org/abs/2312.03184).

## Exact Einstein-frame balance

Write the curvature--flux potential as

\[
V(R)=-\frac{B}{R^4}+\frac{An^2}{R^6},
\qquad A>0,\quad B>0.
\]

Here \(n\) is the positive magnitude of the quantized flux; its orientation is
the separate bit \(\sigma=\pm1\).

The finite stationary radius is

\[
R_*^2=\frac{3An^2}{2B}.
\]

On shell,

\[
V''(R_*)=\frac{8B}{R_*^6}>0.
\]

Thus curvature--flux competition supplies the strict radial minimum that no
one-scale Casimir term could provide.

## A conditional absolute magnitude emerges

The signed flux threshold or portal scale is

\[
\Delta_*=\frac{\sigma n}{R_*}
=\sigma\sqrt{\frac{2B}{3A}}.
\]

The flux magnitude cancels. Therefore, once the gauge--gravity ratio \(B/A\)
is fixed, the construction predicts an absolute magnitude rather than merely
a ratio of thresholds.

This is progressive, but conditional: ordinary Einstein--Maxwell theory does
not itself quantize \(B/A\). Two theories with different gauge--gravity
normalizations have the same topology and different predicted magnitudes.

## Orientation remains exactly invisible

The potential contains \(n^2\), so \(\sigma=+1\) and \(\sigma=-1\) have the
same radius, Hessian, energy, and threshold magnitude. Their signed portal
readouts are opposite. Curvature--flux balance therefore repairs WP789's
clock but not WP786's mirror obstruction.

## Vacuum-energy gate

At the strict minimum,

\[
V(R_*)=-\frac{B}{3R_*^4}<0.
\]

The uncompleted branch is AdS. Adding a six-dimensional cosmological term
\(C/R^2\) permits a stationary Minkowski solution only when

\[
R_*^2=\frac{2An^2}{B},
\qquad
C=\frac{B^2}{4An^2}.
\]

Unless the same source derives this relation, uplift introduces another
coefficient tuning.

## Classification

Curvature--flux balance is a genuine radion selector, classical basin
rigidifier, and conditional absolute-magnitude selector. It is not:

- a flux-orientation selector;
- a derivation of the gauge--gravity ratio \(B/A\);
- a quantum RG-basin proof;
- a localized threshold-completion theorem;
- a calibrated signed instrument.

The surviving source principle must be a non-mirror-completable
gauge--gravity compactification that fixes \(B/A\) and the flux orientation in
one quantized incidence packet. A chirality-sensitive detector can then read
the sign, while spectroscopy reads the magnitude.

Reproduce with:

    uv run --with sympy python research/flavor/checkers/wp790_curvature_flux_radion_magnitude_selector.py

Generated result:
research/flavor/results/wp790_curvature_flux_radion_magnitude_selector.json
