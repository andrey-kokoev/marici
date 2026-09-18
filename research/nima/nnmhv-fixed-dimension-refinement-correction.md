# NNMHV completion is fixed-dimensional refinement

## Correct geometric hierarchy

For every `n >= 6`, the tree NNMHV positive geometry is

\[
\mathcal A_{n,2,4}\subset G(2,6),
\qquad \dim \mathcal A_{n,2,4}=8.
\]

Increasing `n` adds positive external data and refines the available cellulations. It does not add dimensions to the amplituhedron.

The exact representation chain is

\[
\mathcal A_{n,2,4}
\longleftarrow
\text{positive cells}
\longleftarrow
\text{coherence histories}
\longrightarrow
\text{endpoint kernel}
\longrightarrow
\text{polarized shell flux}
\longrightarrow
\text{scalar coefficient}.
\]

At six points, the unique history is the top cell of `G_+(2,6)`. At seven points, all six sourced histories match complete parity-dual simplex canonical forms with ratio one. They form a different triangulation from the standard anchored NMHV BCFW triangulation.

## Correct interpretation of cutoff completion

The cutoff coordinate `n` parametrizes refinement of a fixed-dimensional geometry. The insertion/reflow pair records how one cellulation changes under refinement:

\[
\Delta S_n=J_n^{\rm insertion}+J_n^{\rm reflow}.
\]

The observed asymptotics

\[
S_n=L+c_2n^{-2}+c_3n^{-3}+\cdots
\]

belong to the refinement system, not to growth of physical dimension.

## Status of the holonomy picture

Boundary transport supplies projective `2 by 2` matrices after complexification. The invertible rank-two stratum lies in `PGL(2,C)` and admits a local Lorentz/rotor interpretation. Null dual edges also produce rank-one matrices, so the complete carrier is the projective matrix semigroup `P(Mat_2)`, not an `SL(2,C)` group. Its singular determinant boundary is the Segre quadric `P^1 x P^1`, recording image and kernel lines. No global category-valued connection over all cells has yet been constructed.

Consequently:

- the amplituhedron is fundamental in the established positive-geometric description;
- decorated permutations and permutahedra are combinatorial shadows of its cells;
- history kernels are triangulation-dependent resolutions of its canonical form;
- Lorentz holonomy and `4 pi` spin phase remain candidate coherence structures only on invertible transition patches;
- rank-one patches require projective correspondences rather than group holonomy.

## Retractions

The following earlier interpretations are withdrawn:

1. increasing `n` as an increase of amplituhedron dimension;
2. identifying dimension growth itself with polarity creation;
3. calling the `SL(2,C)` holonomy the complete transport representation;
4. treating the `4 pi` phase as established global amplitude dynamics.

The exact finite history formulas, boundary updates, six- and seven-point canonical-form matches, cyclicity, pole cancellation, and full-history asymptotic data are unaffected.
