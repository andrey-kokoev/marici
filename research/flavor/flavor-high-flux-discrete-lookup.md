# High-flux discrete lookup audit (WP318)

## Question

The high branch of the quantized WP314 ratio is

\[
t_m=\sqrt{m^2+1}+m,
\qquad m\in\mathbb Z_{>0}.
\]

Could the fitted hierarchy be explained by allowing a larger flux magnitude?
This is a selector question only if the source chooses the magnitude before
the flavor readout. Merely locating the closest lattice point afterward is a
discrete fit.

## Result

The complete fitted range intersects exactly one tested lattice orbit:

\[
m=64.
\]

The neighboring predictions at magnitudes 63 and 65 lie outside the entire
ensemble range. No fitted sheet equals the magnitude-64 value at the declared
numerical tolerance. More importantly, the admitted energy from WP316 selects
magnitude 1, not magnitude 64.

Thus quantization has reduced a continuous parameter to a discrete lookup
table, but has not supplied the missing selector. Inferring magnitude 64 from
the measured hierarchy reverses the required source-to-readout arrow.

## Falsifier and gate

The smallest exact falsifier of selector authority is already upstream:

\[
\operatorname*{argmin}_{m\geq1}m^2=1\neq64.
\]

A progressive successor needs an independently derived topology or action
whose minimum selects magnitude 64 without inspecting flavor data. Detector
resolution can test that prediction but cannot authorize it.

Run `uv run --with numpy --with scipy --with sympy python
research/flavor/checkers/wp318_high_flux_discrete_lookup.py` to regenerate the
audit.
