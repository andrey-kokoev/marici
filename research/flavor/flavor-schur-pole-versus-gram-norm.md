# Schur matching uses pole inverses, not an aggregate Gram norm: WP1030

## Question

Can the rank-17 tight frame proposed after WP1029 physically realize the
WP1028 replacement \(M=\sqrt{17}f\) in the WP90 threshold matching?

## Exact heavy block

Take seventeen degenerate orthogonal heavy mediators with mass operator

\[
H=mI_{17}.
\]

For normalized aligned entrance and exit ports
\(u=(1,\ldots,1)/\sqrt{17}\), the exact Schur response is

\[
u^T H^{-1}u=\frac1m.
\]

For unnormalized equal ports it is \(17/m\). By contrast, the Frobenius mass
of the block is

\[
\|H\|_F=\sqrt{17},m.
\]

Replacing the inverse pole response by \(1/\|H\|_F\) would give
\(1/(\sqrt{17}m)\), which is neither exact contraction. For normalized ports
the exact nonzero discrepancy is

\[
\frac1m-\frac1{\sqrt{17}m}
=\frac{17-\sqrt{17}}{17m}.
\]

## Consequence for WP1028

Mediator multiplicity changes the source and readout port contraction. It does
not replace a physical pole mass by the aggregate norm of all poles. Therefore
a rank-17 projector, tight frame, gauge Gram, or seventeenfold degenerate
messenger family cannot realize the WP1028 threshold ratio merely by rank.

The only surviving interpretation is narrower: one physical mediator pole
whose own mass-squared receives seventeen independently normalized positive
contributions,

\[
m_{\rm pole}^2=17f^2.
\]

That additive single-pole law still lacks a source derivation.

## Instrument and falsifier

The required instrument is pole spectroscopy with residues. It must distinguish
one composite pole from seventeen degenerate poles and calibrate the entrance
and exit port vectors. The smallest exact falsifier is the normalized
seventeen-pole response \(1/m\), which disagrees with
\(1/(\sqrt{17}m)\).

## Claim boundary

This closes rank-17 mediator-frame and tight-frame realizations of WP1028. It
does not close a genuinely derived single-pole additive mass-squared
constructor.

## Disposition

Negative correction. The next source search must target one mediator whose
mass-squared coefficient is structurally seventeen, not seventeen mediator
directions.

Verification: uv run --with sympy python
research/flavor/checkers/wp1030_schur_pole_vs_gram_norm.py
