# B-mixing-forced pole hierarchy and loss of width closure

## Full likelihood inversion

WP515 asks what the calibrated \(B_s\) instrument forces after WP513 closes
the aligned quark-only width branch. It uses the complete one-dimensional
`flavio` response, not only the local Jacobian.

Along the real correlated WET ray, \((\Delta M_s)^2\) is a positive quadratic
in \(x_s\). WP515 reconstructs this quadratic, then solves the full executable
response for the outer negative endpoint of the frozen 1.96-standard-deviation
interval. Experimental and WP511 theory variances remain combined in the same
frame.

The endpoint is

\[
x_s^{\mathrm{outer}}=-3.5575963\mathbin{\cdot}10^{-11}
\ \mathrm{GeV}^{-2}.
\]

Every negative aligned source coefficient compatible with this interval has
magnitude no larger than this value, including the second allowed segment on
the far side of the quadratic minimum.

## Entrance-ratio consequence

The exact aligned matching relation is

\[
x_s=-{1\over4v_{\mathrm{phys}}^2}\left({b\over a}\right)^2.
\]

At \(v_{\mathrm{phys}}=246\ \mathrm{GeV}\), the likelihood therefore requires

\[
{b\over a}<0.002934563.
\]

Equivalently,

\[
{a^2\over b^2}>116121.63.
\]

This is an experimentally induced source-domain restriction, not a dynamical
selection of the entrance ratio.

## Forced spectral hierarchy

The two relevant cubic sectors obey the exact source identity

\[
{\prod_{i=1}^3m_{a,i}^2\over\prod_{i=1}^3m_{b,i}^2}
={a^2\over b^2}.
\]

If \(R\) denotes the global squared-mass spread, the ratio of two products of
three roots cannot exceed \(R^3\). Hence the calibrated current constraint
forces

\[
R>48.7870.
\]

WP510's sufficient quark-only width certificate required \(R<4\). The two
domains are disjoint by more than an order of magnitude in squared-mass spread.

## Width disposition

WP515 proves loss of the sufficient closure certificate. It does not infer a
decay merely from kinematics: a physical width additionally requires a nonzero
source vertex and an allowed pair of daughter species. Consequently it would
be invalid either to retain WP510's quark-only total widths or to invent an
extra width from pole positions alone.

The next calculation must diagonalize a \(B_s\)-compatible hierarchical gauge
spectrum, transport the nonabelian and scalar vertices into that mass basis,
and enumerate every kinematically allowed channel. Only those nonzero vertices
may be added to WP509's already frozen quark widths.

The smallest falsifier is the joint pair

\[
{b\over a}<0.002935,
\qquad
R>48.78.
\]
