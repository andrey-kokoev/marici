# Unit-flux ensemble falsifier (WP317)

## Test

WP316 predicts the exchange orbit of the reciprocal hierarchy ratios

\[
\left\{\sqrt{2}-1,\sqrt{2}+1\right\}.
\]

WP317 rebuilds the weak-basis-invariant ordered singular spectra of every
canonical WP20 record and compares its hierarchy ratio with both orientations
of this orbit. The comparison uses log-ratio distance, so reciprocal scale
errors are treated symmetrically.

## Interpretation

Passing the checker is a falsification result: no fitted sheet lies within the
declared tolerance of either branch. Adding an orientation port cannot help,
because the test already admits both orientations. The selector remains a
valid conditional theorem on its declared topological domain, but it does not
describe the fitted flavor ensemble.

The orbit prediction is exact. The ensemble comparison is an IEEE
double-precision reconstruction with an explicit tolerance and a gap more than
eight orders of magnitude larger than that tolerance; it is not presented as
a symbolic exact comparison.

Changing the flux energy or the flux-to-hierarchy matching would define a new
source model. Those changes cannot be inferred from the failed readout without
returning numerical authority to the target data.

Run `uv run --with numpy --with scipy --with sympy python
research/flavor/checkers/wp317_unit_flux_ensemble_falsifier.py` to regenerate
the complete-ensemble audit.
