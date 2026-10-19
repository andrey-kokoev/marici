# One composite boundary: local target residue square — 2026-10-13

## Iteration 2: fresh state and selected test

Freshly read the recommended composite-normalization node and the three-composite receipt. The next action was a source-boundary-to-target differential map with rank/normal/residue checks, without assuming A3 labels identify physical channels.

For history 5/root [1,2], the fixed twisted H chart has a boundary alpha2=0 mapping to normalized <Y1234>=0 under Y=CZ. The bracket is physical by the declared adjacent-pair convention (12)(34), not by its A3 root label.

## Symbolic divisor and local target chart

For each of the two prior positive external-Z fixtures, expand the raw bracket using Cauchy-Binet:

    det([CZ; Z1; Z2; Z3; Z4])
      = sum_{i<j} Delta_ij(C) det([Zi; Zj; Z1; Z2; Z3; Z4]).

It factors exactly as alpha2 times a nonzero quotient independent of alpha2. This proves the source divisor relation symbolically in all eight source coordinates for those Z fixtures.

Normalize target columns 1,2 to identity. The target boundary normal b is the raw bracket divided by that pivot determinant. At the tested positive boundary points, both the pivot and db/dalpha2 are nonzero, and the seven free source directions map with rank seven. Select the lexicographically first nonzero seven-coordinate target minor; its determinant fixes the local boundary density without a fitted coefficient.

The result constructs a regular local target boundary chart (b,x_selected), with all numerical matrices and determinants retained in the receipt. It does not prove a global inverse-fiber degree or all-Z classification.

## Exact residue square

The source eight-dlog orientation gives deletion sign -1 at alpha2=0.

Route A takes the source residue and then pushes its seven-form forward:

    density_A = -1 / det(d x_selected / d log alpha_free).

Route B pushes the top form into (b,x_selected) first. If D is that chart's ordinary Jacobian in all eight source variables, its top density is

    1 / [prod(alpha) det D].

Since b=alpha2*slope+O(alpha2^2), the target b-residue is

    density_B = slope / [prod(alpha_free) det D_boundary].

Both densities agree exactly at both boundary points. The derivative of b vanishes along all seven tangent directions, is nonzero transversely, and supplies the cofactor sign accounting for source deletion parity.

Reversing the source residue orientation produces a nonzero discrepancy at both points. This is an actual local bosonized differential residue/pushforward square, not only the earlier top-generator scalar extraction.

## Coordinate-chart coverage warning

The eight coordinate faces of this selected H chart were independently screened at both target fixtures. Vanishing four-bracket identities were checked symbolically in source coordinates, not merely by evaluating a bracket at a point.

For the first fixture:

- alpha2, alpha3, alpha6: rank-seven images on physical adjacent-pair brackets 1234, 2345, 1256;
- alpha1, alpha4, alpha5: rank-seven nonphysical or nonlinear images (1235, no identically vanishing four-bracket, 1258 respectively);
- alpha7, alpha8: rank-six contracted images.

A contracted image may lie in a physical bracket locus; that does not turn it into a physical divisorial pushforward. These eight coordinate faces do not recover the five physical facets attributed to history 5 in the full invariant atlas. Additional exposing charts/strata are still required. No physical facet count is changed to fit this local screen.

## Scope and surviving gates

Established: a source-defined normal, rank-seven target boundary chart and commuting oriented differential residue square for one history-5 branch and two positive Z fixtures.

Still missing: its global BCFW orientation anchor/covering degree, complete physical-facet provenance, boundary supercomponent extraction, the nine-to-twenty map, and shared weighted codimension-two cancellation. The scalar component map from superfunctions remains a different typed arrow and is not silently applied to this seven-form.

## Next nonredundant continuation

Extend this differential face/rank/residue screen across all three explicit composite charts. Retain contracted and nonphysical faces and distinguish coordinate-chart coverage from the missing invariant atlas. Source-owner bundle recovery/global transition witnesses remain separate requirements.

## Reproduction

    python research/benincasa/checkers/check_composite_boundary_residue_square.py

Receipt: `research/benincasa/results/composite_boundary_residue_square.json`.

Six grouped exact controls pass. Prior source/checker hashes are verified; no owner producer or missing historical atlas was regenerated. Verification is symbolic divisor algebra for the selected external Z and exact local differential residue limits, not a kernel or global theorem.
