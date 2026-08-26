# Dual-Jacobian selector and instrument gate (WP306)

## Opposite arrows

Factor the typed pipeline as

\[
\theta\longmapsto x_*(\theta)\longmapsto y(x_*),
\]

where $\theta$ denotes surviving source moduli, $x_*$ is the selected
`physical16` image, and $y$ is the calibrated detector record.

The source-predictivity Jacobian is

\[
J_{\mathrm{src}}=\frac{\partial x_*}{\partial\theta}.
\]

After admitted source redundancies are quotiented, numerical prediction needs
rank zero. The detector-faithfulness Jacobian is

\[
J_{\mathrm{det}}=\frac{\partial y}{\partial x}.
\]

Identification needs full column rank, or equivalently

\[
\det(J_{\mathrm{det}}^T WJ_{\mathrm{det}})>0
\]

for an independently calibrated positive detector metric $W$.

## Independence theorem

The gates are compatible because they apply to opposite arrows. The exact
two-coordinate audit realizes all four possibilities:

- zero source rank and full detector rank: prediction and identification;
- zero source rank and singular detector response: prediction without an
  identifying instrument;
- nonzero source rank and full detector response: faithful readout without
  prediction;
- nonzero source rank and singular detector response: neither.

This resolves the apparent conflict between WP305 and the detector-rank gate.
Algebraic selection and experimental identification must both pass, but one
cannot substitute for the other.

## Flavor consequence

WP298 addresses the second arrow on its declared chart. WP305 shows the first
arrow still has responsive source moduli in current candidate normalizations.
The progressive target is therefore a zero-rank source image followed by a
full-rank calibrated detector map on the same support domain.

Run `uv run --with sympy python
research/flavor/checkers/wp306_dual_jacobian_selector_instrument.py` to
regenerate the exact four-case audit.
