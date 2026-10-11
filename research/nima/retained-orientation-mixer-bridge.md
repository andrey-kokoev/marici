# Restart iteration 1: retained orientation is not yet the mixer's fiber orientation

Freshly inspected the local-frame checker, the actual reference-context orientation checker, and `tetrahedral-hidden-readout-frames.md`. Tested the proposed recovered orientation attachment rather than assuming that two sign representations describe the same source.

## Positive finite construction

S4 acts on the three pair partitions of four vertices. Their two-dimensional sum-zero contrast plane, with its counting metric, carries a representation whose determinant equals the vertex-permutation sign. Exact tests cover all 24 permutations and all 576 compositions. In a rational contrast basis the metric is [[2,-1],[-1,2]]; this is not a declaration that the basis is orthonormal.

Thus there is a genuine finite representation-theoretic route from tetrahedral orientation to a two-dimensional determinant line. It is more than a numerical coincidence of signs, but it is not an identification with the existing Boolean edge fibers.

For two orientation coordinates transforming as (a,b)->(s*a,t*b), the required relative line transforms by s*t. There is no nonzero linear equivariant map from the direct sum to that line. The homogeneous quadratic maps are exactly kappa*a*b. Given actual nonzero oriented records, their product can therefore provide a relative orientation after the line identification; covariance alone leaves kappa unspecified. A vector space carrying orientations does not itself supply a nonzero oriented record.

## Filling does not erase a retained orientation witness

The tetrahedral boundary has rank(boundary2)=3. Adding its 3-cell gives rank(boundary3)=1 and H2=0. Nevertheless its nonzero oriented boundary remains a retained exact chain. It would be wrong to infer that filling automatically destroys every usable orientation record.

The oriented faces ABC and ADB consistently extend to -boundary(ABCD). This is a conditional selector from actual oriented-face data; it is not an invariant orientation of an unmarked tetrahedron.

## The decisive actual-adapter control

The existing ordinary/twisted adapter changes the Boolean basis at diagram vertex 1 while leaving the four diagram vertices and their face orderings unchanged. Under this change:

    topological diagram orientation: unchanged,
    required mixer attachment: multiplied by det(Q2)det(Q1)=-1.

Consequently a function ONLY of those unchanged topological orientations cannot provide a nonzero attachment for this actual fiber-frame action. Multiplying two such records does not repair the mismatch. The new contrast-plane representation would require a new source identification; matching determinant signs under a different group action is insufficient.

This is a bounded obstruction to the proposed orientation-only adapter, not a claim that the full retained package is fixed by the Boolean frame change. Its edge actions and potentially marked state/witness data must still be inspected separately.

## Selection status and next executable gate

The recovered topology does not yet select the mixer's physical reference. Neither physical metric nor gravitational normalization has been derived, and the free coefficient in the bilinear orientation formula must not be identified with G.

Next inspect the actual retained Boolean state and higher-witness ports: do they contain an ordered frame/preparation that transforms under the Boolean fiber flip, rather than only under relabelling of diagram vertices? If such data exists, test the resulting attachment and whether its response differs from the already-trivial self-edge determinant. If it does not, classify the attachments obtainable from the existing flat edge network before adding another physical source law.

This is nonredundant source inspection left open, so this turn does not stop the iteration loop.

## Verification

`python research/nima/checkers/check_retained_orientation_mixer_bridge.py` passes. Receipt: `results/retained-orientation-mixer-bridge.json`. Checks use exact rational matrix arithmetic and polynomial coefficient constraints; no physical field equation or Agda closure is claimed. Historical checkers and receipts were not modified.
