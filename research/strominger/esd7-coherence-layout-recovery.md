# Recovered coherence-pyramid layout for the seven-stage block

## Executable recovery

[Seven-stage handoff audit](esd7-seven-stage-handoff-v1.md): 19 fresh exact checks on all1807 cells, four actual conductor paths, and24 central flag bridges through T184. One central bridge is `V051 -> E270 -> F403 -> T184 -> F538 -> E368 -> V072`, with incidence-rank profile1,2,3,4,3,2,1. This supplies a concrete central candidate rather than a count-fitted boundary loop.

The resource is also indexed prominently in the [Realization Tower research home](../realization-tower/README.md#coherence-pyramid--esd7-full-layout-and-seven-stage-transport).

## What was recovered

The existing coherence-pyramid research already provides the geometric layout and analytical comparison registry. The next experiment should consume these, rather than replace the pyramid with a fresh Bool-square or binary-tree toy.

### Complete geometric incidence

`research/voevodsky/results/esd7_explicit_analytical_census.json` is present locally. Its builder is `research/voevodsky/checkers/check_esd7_explicit_analytical_census.py`. Stable IDs cover:

- V000--V119:120 source-labelled transfer-history objects;
- E000--E559:560 whiskered parent transfers;
- F000--F783:784 face homotopies with ordered transfer blocks;
- T000--T342:343 signed parent tetrahedral modifications.

Each tetrahedron references its six edges and four faces. Every shared boundary is one common indexed object. The source manifest builder `research/nima/build_esd7_source_manifest.py` additionally defines cyclic barycentric action rho, reversal omega, and orientation signs. Its generated result is absent in this checkout; the builder and its geometric input are available. No regeneration or fresh validation was performed in this source search.

### Explicit coherence prototype

`research/voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md` supplies six typed d_ij maps, four face comparisons, and the tetrahedral equation

    H_ACD (d24 * H_ABC) = H_ABD (H_BCD * d13).

These compare two reductions of the same three-step route to the direct arrow. Polarity transports the entire equation and reverses the edge types. This is the actual higher-coherence layout, not merely endpoint agreement.

### Full analytical layout registry

`research/voevodsky/eight-node-lattice-analytical-form-coverage-ledger.md` records the completed finite signed/relative census and its later common-cofinal-exhaustion extension. Its geometric registry references H123,H124,H134,H234 on every tetrahedron. The four face roles retain naturality residuals, endpoint coordinates, Hermitian/skew placement data, and finite-part/residue data respectively.

It also records seven semantic transitions: A amplification, J canonical-dual comparison, P polarization, C cutoff, T trace/finite part, E endpoint completion, F filler. P and E in this table are ANALYTICAL OPERATION LABELS, not the particle/window labels of the current conjecture. Their dependency poset has18 ideals and28 legal maximal schedules. Those28 are alternative seven-transition schedules, not a derived28-stage trace. Some geometric edge paths repeat semantic ideals or combine transitions, so row indices alone do not identify the desired convolution-depth stages.

The aggregate checker is `research/voevodsky/checkers/check_complete_eight_node_analytical_coverage.py`; the source ledger reports13 passing integrity checks. This report was inspected, not freshly replayed.

## The existing quarter-turn handoff

`research/voevodsky/a-clean-universal-category-for-the-eight-lattice-four-chart-suspension-system.md` gives

    q u = rho(u) q,
    rho^4 = 1,
    q^4 = Sigma.

Here u is an incidence map, rho rotates the tetrahedral coordinates, and q advances the chart together with the retained grade. `research/nima/full-esd7-graded-tate-torus-realization.md` describes the full all-cell realization under its maximal designation profile.

These equations provide the correct starting interface: advance a presentation through an incidence and then change chart, or change chart and use the rotated incidence. Compare the full signed boundaries, not just the final corner.

## Correct stage granularity for the operator's latest proposal

The operator now proposes FOUR SEVEN-STAGE BLOCKS, with a quarter-turn after each block. This supersedes the earlier speculative seven four-stage cycles and the statement that every individual post-initial stage must itself be a quarter/half turn.

With q bound to that BLOCK handoff,28 elementary stages correspond to four q applications:

    [seven-stage block; q]^4,
    four chart advances give Sigma, not seven suspensions.

The earlier observation q^28=Sigma^7 is algebraically valid but counts28 chart advances, a different stage convention. Neither formula alone identifies the P/E window readout. The first-stage/orientation convention and signed block action must be carried explicitly.

## Concrete next construction

Recover a seven-segment conductor factorization from the existing layout, retain its full source/target presentations and face data, and test the block handoff against q u=rho(u) q. Use the four face comparisons and tetrahedral equation to check shared-interface transport. Then align the block stages with the proposed depth profile1,2,3,4,3,2,1 and its common center. An outer conductor path must not simply be renamed a center-to-vertex path.

This is now an extraction-and-binding problem on an existing coherence complex, not a request to invent seven steps or a new tetrahedral filling.
