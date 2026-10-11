# From source arrows to electron/proton local selections

## Source-level result

Freshly inspected the original proton geometry generator and electron spinor generator, then reconstructed their local selectors against the stored artifacts. Their common structure is a tetrahedral symmetry action with two different placement resolutions, not a demonstrated early/late particle sequence.

The original seed cycles ABC and BAD generate the twelve proper tetrahedral rotations. Acting on the reference directed edge AB gives all twelve directed edges. Acting on its owning oriented face gives the four faces. The source ownership is:

| Face | Three directed-edge placements |
|---|---|
| ABC | AB, BC, CA |
| ABD | AD, BA, DB |
| ACD | AC, CD, DA |
| BCD | BD, CB, DC |

Opposite directions on one undirected edge belong to its two different incident oriented faces. A face center here records a subdivision of the outer face; it is not the identity-arrow vertex or the projected fifth vertex of the later electron visualization.

## Four common questions, with different actual answers

| Constructive question | Proton source | Electron source |
|---|---|---|
| What indexes local placements? | Directed edge with source-determined face ownership: twelve placements | Whole face: four placements |
| What local operation selects coefficients? | Three-cycle on the centroid-edge triangle; retain its omega character | Normal/Pauli operator on a two-component spinor; retain negative polarization |
| How are placements related? | Transport one reference triangle and its vector through the proper tetrahedral rotations | Transport face spinors through the binary lift of those rotations |
| What is the global retained state? | One co-rotating common complex amplitude | Two-component logical spinor encoded across four faces |

The electron generator does not first run the proton's triangle-character code and stop early. It explicitly introduces Pauli spinor coefficients and computes P_i=(I-n_i.sigma)/2. Conversely the proton generator introduces a centroid-edge reference triangle and its cyclic character before taking its rotation orbit. Both start with supplied geometric/coefficient realizations; neither is currently derived from AA alone.

## Exact common indexing map

The directed-edge action is free and transitive: its stabilizer has size one. The face stabilizer has size three. Forgetting the edge position while retaining its owning face is an equivariant three-to-one map. Thus twelve versus four is not an unrelated count: it is the difference between a face with a distinguished cyclic edge position and the face without that distinction.

For arbitrary scalar placement amplitudes, the face-sum map has rank four and an eight-dimensional kernel. A retained record may keep all three members of every fiber, but collapsing them to one scalar loses their contrasts. This indexing map alone is not a coefficient-space equivalence or a physical operation.

An especially useful control: ordinary scalar symmetry averaging has rank one on BOTH the twelve-edge and four-face permutation spaces. Therefore the electron's doublet cannot be explained merely by using four placements instead of twelve. It comes from the spinor representation and its equivariant encoder, not the placement count.

## Local coefficient constructions checked

For every stored proton triangle, form X from its centroid and edge endpoint columns and C from the cyclic permutation. The retained vector is

    v=X(1,omega,omega^2),
    (X C X^-1)v=omega v.

The checker reconstructs this at all twelve placements. For each stored electron normal it independently reconstructs the Pauli selector and verifies agreement with the stored projector; their sum is 2I, giving the doublet encoder normalization.

The full-turn central element acts by +I on the old vector realization and -I on the spinor realization. Any linear intertwiner between them that preserves this action must be zero. This familiar representation obstruction does not exclude nonlinear, enlarged-record or explicitly representation-changing constructions; it does exclude treating the current difference as mere relabeling.

## Three meanings of arrow must remain separate

1. Seed arrows such as AB and BA are directed endpoint relations.
2. Rotating the reference placement indexes twelve local triangle records by those labels.
3. The later 1836 proton and 144 electron transfers are nonzero coefficient-map entries between typed protocol stages.

The third counts do not count geometric edges and do not explain the twelve-versus-four placement difference. Likewise a sequence of source/target regroupings does not become volume growth just because it can be displayed as a shape.

## Consequence for the proposed phase picture

There is a clean common relational core to study: the face-indexed family with its three cyclic edge positions and retained transports. There is not yet a source-derived operation that turns its outgoing presentation into the electron coefficient system and its completed presentation into the proton coefficient system.

The next discriminating construction would keep that common incidence fixed and explicitly compare coefficient lifts on it, including the stabilizer's action on the local line. That would test whether the two selectors can arise from a single retained construction rather than assuming that capping a picture changes vector coefficients into spinors or vice versa.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_arrow_to_selection_comparison.py

Receipt: `results/arrow_to_selection_comparison.json`. Exact checks cover source hashes, group closure, all placement fibers, equivariance, stabilizer sizes, scalar grouping rank/kernel, both scalar invariant ranks, all twelve local character equations and all four source Pauli selections. No particle assignment to the four proposed arity phases is asserted.
