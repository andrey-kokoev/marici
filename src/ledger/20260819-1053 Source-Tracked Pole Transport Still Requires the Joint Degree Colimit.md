# 1053 — Source-Tracked Pole Transport Still Requires the Joint Degree Colimit

## Question

Entry 1050 rejected transport of raw pivot-producing relations.  Repair that
defect by carrying the complete degree-plus-one connection image through the
same source elimination that constructs the thirteen-dimensional depth-three
exact-valuation object.

## Construction

For every one of the 16,284 stage-two source relations and both triangle-wall
tangents, a binary sidecar records its length-three normal-jet connection
image in the depth-four ambient module.  Paired Gaussian elimination then
acts simultaneously on

\[
(\text{source relation jet},\text{connection image}).
\]

This produces exactly thirteen normalized transported representatives per
tangent.  Hence the raw-generator defect of Entry 1050 is repaired without
choosing a source splitting.

## Same-window descent test

All twenty-six representatives were reduced against the complete
K-depth-four, ambient-degree-ten target.  Every remainder is nonzero:

\[
\boxed{26/26\text{ source-tracked images fail same-window descent}.}
\]

The failure is not evidence against the unbounded connection.  External
differentiation raises polynomial degree as well as Cayley--Menger pole depth.
The fixed degree-ten target omits higher-degree relation primitives required
by Entry 1018's exact unbounded commutator identity.

Therefore the filtered connection cannot be constructed by completing pole
depth while freezing ambient degree:

\[
\boxed{
\text{connection-stable completion requires the joint pole/degree colimit.}
}
\]

## Next finite falsifier

Before computing another connection matrix, test whether the new one-plus-five
pole grade survives the honest ambient-degree inclusion from ten to eleven.
If it dies, the apparent pole tower is a cutoff-boundary phenomenon.  If it
injects, construct a cofinal staircase increasing both filtrations and repeat
the transported descent there.

## Durable artifacts

- sidecar exporter:
  `research/benincasa/export_triangle_wall_pole_connection_sidecar.py`;
- paired transport support:
  `research/benincasa/marici-gm/src/bin/triangle_wall_dual_rank.rs`;
- source transport rank packet:
  `research/benincasa/triangle-wall-depth3-transport-source-rank.json`;
- target reduction packet:
  `research/benincasa/triangle-wall-depth3-transport-target-reduction.json`;
- transported probes:
  `research/benincasa/triangle-wall-depth3-transported-connection-probes.txt`;
- allocator claim: `seqclaim-d9c8c36ede643ad4133df012`.
- epistemic graph event:
  `ev-000000000693-56c46c28-25a0-49dd-8c8d-370e2f89dc74`.
