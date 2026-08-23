# The two middle sign bands carry the asymmetric block failure

For the exchange orbit `{(1,2),(2,1)}` at `(a,b)=(1,8)`, decompose the exact
three-chart integral into the canonical quarter-period bands

\[
 [0,\pi/16],\ [\pi/16,\pi/8],\ [\pi/8,3\pi/16],\
 [3\pi/16,\pi/4].
\]

The chart-and-label sums in the endpoint bands are positive. The two middle
bands are negative, and their combined magnitude dominates the endpoints,
leaving the full block near `-8.568e-6` with the correct `(S,D)` Jacobian
normalization.

Each chart separately is also negative, but only after substantial
cross-band cancellation. Therefore the rigorous enclosure should not certify
charts independently. It should sum both exchange labels and all three charts
inside each fixed trigonometric band, then combine the four band intervals.
This preserves every source label and canonical band while retaining the
correlations responsible for the sign.

The calculation remains floating-point reconnaissance. It determines the
grouping for the interval certificate; it does not itself certify the sign.

## Durable verification

- Diagnostic: `checkers/theta_adjacent_block_chart_band_diagnostic.py`
- Result: `results/theta-adjacent-block-chart-band-diagnostic.json`
