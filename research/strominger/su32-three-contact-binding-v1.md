# Native test of the proposed three-contact placement

## Question and result

Does the proposed three-step rotation/translation act on the actual native registry, and does it realize three blocks meeting only at three distinct contact vertices?

The rotation **does** extend to the existing typed geometric port graph. The two tested whole-window interpretations **do not** give the proposed contacts. The abstract five-vertex 4-simplex blocks still lack a source realization; neither window is silently identified with those simplices.

## Native rotation, including representative corrections

The coordinate permutation is

\[
R(q_0,q_1,q_2,q_3)=(q_2,q_0,q_1,q_3).
\]

Direct checks against the existing source verify:

- permutation of all 51 physical cells, preserving their P/N/E roles;
- a well-defined action on all 256 quotient ports, including both lifts of grouped tip cells;
- preservation of all 192 edges and their kinds;
- permutation of all 64 complete wires;
- axis action `0→1→2→0`, with axis 3 fixed.

The port action needs its actual representative correction. Write `r(p)` for the rotated quotient port and define `h_p` by

\[
F_{r(p)}=R(F_p)+L(h_p).
\]

Every edge transport is checked against the corresponding transformed transport, including this endpoint correction. The full lifted action for the proposed increment `k=(1,-1,0)` is

\[
U(p,a)=\bigl(r(p),R_a(a)+h_p+k\bigr),
\qquad R_a(a_0,a_1,a_2)=(a_2,a_0,a_1).
\]

Under the source convention `F_p-L(a)`, this is the physical affine map

\[
x\longmapsto R(x)-d,\qquad d=g_0-g_1.
\]

The minus sign is therefore intentional: a positive deck increment is a negative displacement of the represented physical face. The abstract drawing convention can instead use the opposite placement; central inversion exchanges the two whole-window placements and preserves their intersection counts.

The full lifted port returns under three applications. For each port, the checker tests the zero coordinate and three basis coordinates: 1,024 checks. Because the specified map is affine and its linear part is the explicit three-cycle, these checks determine its translation defect; this is not extrapolation from arbitrary sampled nonlinear maps.

This constructs a geometric graph automorphism, **not a contact edge, release operation, or admitted payload/history transport**. The three-step word remains recorded; no native comparison identifying it with an identity history is supplied.

## Actual intersections of the tested source windows

Apply `U` to the complete radius-one and radius-two source windows. Each whole window is invariant under the centered rotation, so their placements have offsets

\[
0,\quad -d,\quad -(d+Rd).
\]

All physical vertices and whole cells are retained and intersected by their exact coordinates and identities.

| Tested block interpretation | Each pair shares | All three share |
|---|---|---|
| Entire edge-three, 51-cell window | No vertices or cells | Nothing |
| Entire edge-five, 245-cell window | 22 vertices and 13 whole cells | 7 vertices and 2 whole cells |

For edge three, each pair has a strict separating coordinate interval with gap one, so the blocks are geometrically disjoint, not merely missing a shared vertex in a sampled registry.

For edge five, the shared whole cells already refute point-only contact and empty triple intersection. This is not the declared abstract complex of three 4-simplices with pairwise single-vertex intersections.

## First missing object and stopping condition

The three-contact note provides an abstract simplicial complex, not a map from its five-vertex blocks and contact vertices to actual native occurrences. The inspected native cell/wire constructors likewise supply no such binding. If the blocks instead live in a witness or operation space, their realization must name that space and its contact maps; a spatial whole-window test cannot refute that different interpretation.

Until the block realization and its typed contacts are supplied, there are no native arrows `f`, `g`, and `h` to compare. The branch stops at that missing input. The valid graph symmetry does not authorize point gluing, choose monodromy, or fill the central loop.

## Verification

```sh
node research/strominger/checkers/check_su32_three_contact_binding.mjs
python research/aspect/scc/scc.py check strominger-su32-three-contact-binding-v1
```

Receipt: `results/su32-three-contact-binding-v1/verification.json`. It retains the complete port and wire actions, representative corrections, all actual intersections, separating bounds, and the unreduced three-step word. A wrong increment `(1,0,0)` gives the predicted nonzero three-step discrepancy `(1,1,1)`.

`nativeThreeContactConstructionAdmitted` remains false. The external note and existing source implementations were not modified. No native contact composite, higher filler, physical monodromy or proof-assistant result is claimed.
