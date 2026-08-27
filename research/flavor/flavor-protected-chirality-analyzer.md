# Protected chirality analyzer: WP672

## Source-derived ideal ports

For one open protected decay, write the two nonnegative chiral strengths as

\[
u=|y|^2,
\qquad
v=|z|^2.
\]

The same decay supplies an ordinary total-rate coordinate and, if a signed
chirality analyzer exists, a moment

\[
W=u+v,
\qquad
N=\alpha(u-v),
\]

where \(\alpha\) is the independently calibrated analyzing power. The exact
response determinant is

\[
\det\frac{\partial(W,N)}{\partial(u,v)}=-2\alpha.
\]

Thus every nonzero calibrated analyzer gives rank two. The WP670 loop erosion
is then reconstructed directly:

\[
u^2+v^2=\frac12\left[W^2+\left(\frac{N}{\alpha}\right)^2\right].
\]

## Confusion gate

For symmetric helicity misclassification probability \(e\), the analyzing
power is \(\alpha=1-2e\). Rank collapses exactly at \(e=1/2\), when the two
helicity records coincide. The hostile width-equivalent pair from WP671 is
separated for every nonzero ideal analyzer.

## Instrument typing

The chiral vertices make \((W,N)\) a source-derived amplitude-level probe
family. They do not by themselves provide a physical polarimeter. Detector
authority requires a declared daughter decay or angular correlation, its
analyzing power, finite-mass transfer, acceptance, backgrounds, resolution,
and covariance in the same likelihood as the total rate.

## Disposition

An ideal calibrated chirality moment repairs constructor-magnitude and
loop-erosion identification in the one kinematically open decay. It measures
free source values; it does not select them or a physical16 point. No current
instrument is admitted by this packet.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp672_protected_chirality_analyzer.py

Generated result: results/wp672_protected_chirality_analyzer.json.
