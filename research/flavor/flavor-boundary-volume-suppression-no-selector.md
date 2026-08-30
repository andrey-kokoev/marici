# Boundary volume suppression is not selection: WP940

## Question

Can a large bulk inverse coupling or naive-dimensional-analysis hierarchy make
WP939's finite boundary coefficient irrelevant strongly enough to count as a
source selector?

## Exact response family

For the exchange-even boundary packet, write the effective gauge coupling as

\[
g_{\mathrm{eff}}^2(C,\tau)=\frac{1}{C+\tau},
\qquad C>0,
\]

where `C` is the bulk inverse-coupling contribution and `tau` is the common
boundary coefficient.  For every finite `C`,

\[
\frac{\partial g_{\mathrm{eff}}^2}{\partial\tau}
=-\frac{1}{(C+\tau)^2}\ne0.
\]

Thus the map remains injective on every positive admissible `tau` interval.
Increasing `C` suppresses the response norm but does not create a quotient or
select a distinguished boundary value.

At `C = 100`, the legal packets `tau = 0, 1` give

\[
g_0^2=\frac{1}{100},
\qquad
g_1^2=\frac{1}{101},
\]

with exact separation `1/10100`.  A finite-resolution instrument may fail to
distinguish them, but that is an observational kernel, not source selection.

## Singular limit

In the formal limit `C -> infinity`, both responses approach zero.  This does
not select a finite flavor normalization; it decouples the gauge interaction.
The limit therefore changes the physical readout rather than explaining the
observed nonzero coupling.

Conversely, a strong five-dimensional coupling decreases the simple bulk
term `C = ell/g5^2`; it does not by itself create volume dominance.  Any NDA
claim that boundary coefficients are small must specify the cutoff, volume,
operator normalization, and complete UV matching.  Parametric smallness is
not an exact boundary law.

These statements compare parameterized source objects.  `C` is not a time
coordinate, and no causal interpretation is attached to the limit.

## Classification

Volume dominance is neither a selector nor a presentation rigidifier.  It is
an approximate contraction of readout sensitivity.  Its contextual partition
depends on an admitted detector resolution; with exact readout every finite
`C` separates the two packets.

The smallest exact falsifier is `C = 100`, `tau = 0, 1`.  The remaining
source gate is unchanged: a UV law must compute or eliminate the finite
exchange-even coefficient while retaining a nonzero physical coupling and
surviving the complete matter spectrum.  WP770 must separately establish the
actual detector resolution and response rank.

Reproduce with:

    uv run python research/flavor/checkers/wp940_boundary_volume_suppression_no_selector.py

Generated result:
`research/flavor/results/wp940_boundary_volume_suppression_no_selector.json`.
