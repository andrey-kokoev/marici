# The flavor stationary point is a CP-ratio relation, not a scalar selector

Entry 2097 found central-value agreement between the observed
\(r=s_{13}/s_{23}\) and the stationary point of \(F_t\). A complete
one-sigma corner audit over the six Yukawa masses, \(V_{us}\), and
\(\gamma\) tests robustness.

Across all 256 corners,

\[
r_*\in[0.07788,0.09852],
\]

whereas the independently propagated one-sigma interval is

\[
r_{\rm obs}\in[0.08607,0.09374].
\]

The stationary interval is 2.69 times wider. Therefore the claim that
\(F_t\) robustly selects one numerical ratio is false.

The motion is almost entirely controlled by the CP phase. Moving
\(\gamma\) by one sigma changes \(r_*\) from \(0.09824\) to
\(0.07808\); the next-largest one-at-a-time span, from \(V_{us}\), is
only \(0.00050\). Mass dependence is negligible at this resolution.

The surviving object is consequently the stationarity curve

\[
\partial_r F_t(r,\gamma)=0.
\]

It may constrain a pair of physical readouts, but it does not independently
predict either one. The next legitimate test is whether the observed
two-dimensional uncertainty region is aligned with this curve beyond
pointwise intersection.

Verification:

    python research/nima/checkers/check_flavor_t_stationarity_robustness.py

The dependency-free checker passes 5/5 falsification gates.
