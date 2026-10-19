# Three composite charts: coordinate boundary residue screen — 2026-10-13

## Iteration 3

Freshly read the mutable net. Its next action was to extend the history-5 local differential residue square across the coordinate faces of all three explicit composite charts, retaining contracted and nonphysical images.

Screened all 24 faces at two positive source/external-Z fixtures: 48 exact face evaluations. Symbolic four-bracket restrictions in source coordinates were evaluated for each external Z. The target-rank and bracket signatures agree across the two fixtures.

## Dispositions per fixture

| History / root | Physical rank-seven | Other rank-seven | Contracted | Constructed local squares | Missing bracket normals |
|---|---:|---:|---:|---:|---:|
| 5 / [1,2] | 3 | 3 | 2 | 5 | 1 |
| 8 / [1,3] | 3 | 3 | 2 | 5 | 1 |
| 9 / [2,3] | 2 | 4 | 2 | 5 | 1 |
| Total | 8 | 10 | 6 | 15 | 3 |

Physical classification uses adjacent-pair target four-brackets and rank seven; it is not assigned by A3 compatibility or root labels. Contracted faces are not counted as divisorial even if their images lie on a physical bracket locus.

These numbers describe selected coordinate charts, NOT the invariant full-atlas 5/6/5 physical facet counts. The difference is retained rather than repaired by relabeling nonphysical or contracted faces.

## Thirty exact local residue-square controls

For each rank-seven face with a regular bracket normal, choose a target normal defined by an identically vanishing bracket. Verify nonzero transverse slope, seven-dimensional tangent Jacobian, and a full ordinary normal-chart Jacobian.

Compare:

    source deletion residue -> local seven-form pushforward

against

    top eight-form pushforward -> residue at the target normal.

All 15 branch squares per fixture agree exactly, giving 30 local equalities. For every square, deliberately reversing the source deletion sign produces a nonzero discrepancy. Physical and nonphysical bracket-defined squares both retain their explicit target normal and localization data.

The original history-5 alpha2-to-<Y1234> result is reproduced without changing its predecessor receipt.

## Three missing nonlinear normals

For all three charts, the face alpha4=0 has tangent rank seven but no identically vanishing target four-bracket. Crucially, the full ordinary target differential has rank eight at both boundary samples. Thus the tested local map is regular transversely; this is not evidence of a fold or contracted face.

The source normal should therefore admit a local inverse-branch target realization, but this checker does not construct that inverse or its defining nonlinear normal. A linear tangent covector alone is insufficient: it would only vanish to first order along the boundary, not define its image.

These three faces remain explicitly marked missing regular bracket normals rather than being counted as completed residue squares or silently dropped.

## Scope boundary and next task

Established: selected coordinate-face ranks and bracket identities, thirty oriented local differential residue squares, and regularity at the three missing bracket-normal images.

Still absent: invariant-atlas completeness, common-chart cross-history cancellation, global source-chain orientation/degree, target supercomponent boundary extraction, and the normalized nine-to-twenty comparison. The original canonical admission and simple-root difference gates are unchanged.

Next nonredundant test: construct an actual local inverse-branch target normal for alpha4=0 in one composite chart and verify its residue square. Alternatively, a common-target comparison of shared composite source facets is actionable. Neither continuation licenses calling the selected chart screen the complete BCFW boundary bundle.

## Reproduction

    python research/benincasa/checkers/check_three_composite_boundary_residues.py

Result: `research/benincasa/results/three_composite_boundary_residues.json`.

Eight grouped checks pass. Direct predecessor source/checker pins are verified. Scientific evidence is fresh symbolic bracket restriction for two fixed Z and exact finite differential algebra, not a kernel proof or global theorem. No owner producer or missing atlas receipt was regenerated.
