# The oriented boundary of the complete n=8 history chain

## Question

After refining coarse matroid matches by positive sign chamber, what is the exact boundary of the twenty-cell history chain?

## Construction

Each of the twenty certified positroid charts carries eight coordinate facets. Local residue incidence is

\[
\operatorname{Res}_{\alpha_e=0}
\bigwedge_{j=1}^8d\log\alpha_j
=
(-1)^{e-1}
\bigwedge_{j\ne e}d\log\alpha_j.
\]

A signed constraint graph determines one orientation sign for each top history. Coarse boundary keys are refined by real positive-chart overlap. The unique coarse collision between history 7 and history 11 splits because its exact transition sends positive coordinates to negative coordinates.

## Result

Among 160 coordinate-boundary occurrences:

- 54 occurrences form 27 internal pairs;
- every internal pair cancels after global orientation;
- 106 occurrences remain in the oriented source boundary.

Thus

\[
\partial\Gamma_8=\Gamma_{8,\mathrm{ext}}^{\mathrm{source}}
\]

with explicit 106-term support and coefficients stored in the result JSON.

## Claim boundary

“External” here means unmatched in the complete twenty-chart source chain after positive-chamber refinement. It does not yet prove that every term pushes forward to a nonzero exterior facet of the amplituhedron. Some source facets may be contracted or have zero pushforward residue. That classification requires the map `Phi_Z` on each boundary chart.

Verification:

- `research/nima/checkers/check_n8_full_history_boundary_cancellation.py`
- `research/nima/results/n8-full-history-boundary-cancellation.json`
- `research/nima/checkers/check_n8_GE_boundary_transition.py`
- `research/nima/results/n8-GE-boundary-transition.json`
