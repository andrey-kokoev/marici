# Robust calibrated domain selector (WP287)

## Interval gate

WP286's nominal local criterion is not yet an experimental certificate. Let
each source bias and wall tension have an independently calibrated interval.
For vertex $i$, define the worst admitted selector margin

\[
m_i=\underline h_i-\sum_j\overline J_{ij}.
\]

The domain selector is uniformly strict over the complete interval packet if
and only if $m_i>0$ at every vertex. This condition compares quantities in
one local source frame and includes their declared support.

## Exact hostile completion

On the WP286 weighted triangle, the central values of the nominal-only packet
pass every local inequality. Nevertheless, the admitted corner containing all
lower biases and all upper wall tensions traps the wrong uniform state. Central
values therefore create false authority when uncertainty crosses a local
threshold.

The robust packet has worst-case margins $1/5$ at all three vertices. The
checker enumerates all 64 independent interval corners and all eight spin
configurations per corner. Every minus flip lowers energy and every reverse
flip raises it throughout that packet.

## Classification

This is an exact robust certificate for the declared interval model, not yet a
physical flavor selector. A real instrument must supply a joint calibrated
uncertainty set, including correlations and support. That set must then be
propagated through the physical dynamics and branch-to-`physical16` map.

Run `uv run --with sympy python
research/flavor/checkers/wp287_robust_calibrated_domain_selector.py` to
regenerate the corner audit.
