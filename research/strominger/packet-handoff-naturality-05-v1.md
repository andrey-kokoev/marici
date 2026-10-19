# Packet handoff ground naturality — iteration 5/10

Owner: `marici.Strominger`. **Iteration complete; objective in progress.**

[Live net](contracts/packet-handoff-naturality-conjecture-net.v1.json) · [contract](contracts/packet-handoff-naturality-05.v1.json) · [checker](checkers/check_packet_handoff_naturality_05.py) · [receipt](results/packet-handoff-naturality-05-v1.json).

## Question, rivals and disposition

Can the native geometric boundary modules turn the capacity-based M/C convention into a source-derived geometric main/codimension grading for the three proposed words?

The risky conjecture is that the actual coherent packet fields are geometric boundary cycles and that the relevant native preparation is their bulk/boundary transfer. Rivals are ordinary untwisted cycles, the **already supplied** transported body-frame connection, an open rim/relative chain rather than a closed surface, and noninvertible spinor-code restrictions rather than ordinary local-system transport. These alternatives have different chain, metric, action and reader tests; a fitted connection is not admitted.

**Disposition:** one exact proton relative-bulk bridge is constructed, with neutron and electron obstructions to the corresponding identifications. This grounds distinct source geometries, not a common physical grading or a selected indexed handoff. The previous entry-phase obstruction remains binding.

## 1. Actual geometric bases, not channel counts

Reconstruct oriented simplices directly from the retained sources. Electron here means its **native four-face spinor attachment tetrahedron**, not the separate five-cell geometric carrier. Native operations preserve all boundary maps and the source port grouping: two proton generators, one neutron generator and all 24 electron operations. The native coefficient-to-geometric-field embeddings also intertwine these operations and preserve their declared metrics.

| Source base | Vertices / edges / triangles | Rational Betti numbers | Relative cone H3 / H2, scalar coefficients |
|---|---|---|---|
| Proton subdivided boundary | 8 / 18 / 12 | 1, 0, 1 | 1 / 0 |
| Neutron subdivided belt | 12 / 30 / 18 | 1, 1, 0 | 0 / 1 |
| Electron attachment boundary | 4 / 6 / 4 | 1, 0, 1 | 1 / 0 |

Every local L port is a disk of **piecewise geometric dimension 2**, of codimension 1 in its supplied three-dimensional ambient carrier: twelve proton triangles, three neutron six-triangle sector patches and four electron faces. The neutron patches have counts 6/11/6 each. A folded patch's affine hull may be three-dimensional; that does not make the patch a three-dimensional cell. Geometric base dimension, complex coefficient-fiber rank and stage-image dimension are kept separate.

For each source, let K_N encode its active return in the actual geometric coefficient fibers. Its ordinary boundary residual is

    (B2 tensor I_fiber) K_N.

This has rank **1 / 1 / 2**, respectively: every nonzero active packet has a nonzero ordinary untwisted boundary. Native projector closure is therefore not automatically geometric boundary-zero.

## 2. Proton: native alignment really is a twisted geometric cycle projector

Use the twelve actual supplied orthogonal body frames R_t, not frames inferred from the desired packet. Set

    U = diag(R_t),
    D2_native = (B2 tensor I_3) U*,
    A_body = U (1_12 tensor I_3).

Exact calculation gives

    ker(D2_native) = Image(G),
    dim ker(D2_native) = 3,
    G = (1/12) A_body A_body*,
    D2_native N = 0.

Thus **G is exactly the original metric orthogonal projector onto the native-frame twisted surface cycles**. N selects the local cyclic line within them. This is stronger than the iteration4 marked-evaluation family: the source's own alignment operation now has an actual chain-theoretic meaning. The body-valued cycle module is not the unmarked ambient spatial representation excluded in iteration4.

Cone the actual twelve triangles to their supplied center. Extend the same flat gauge to cone tetrahedra and outer faces, using identity gauges on interior faces. This is an explicit trivializable coefficient-system extension; its presentation can be changed by gauge. It introduces no fitted holonomy. Relative H3 of this cone pair with vector coefficients has dimension 3. The boundary of its coherent bulk class is A_body times the body vector, with all interior faces cancelling.

The checker verifies both native-generator equivariance squares and, on **all raw inputs**, that bulk filling, surface restriction and then L equal the native N operator. This yields a typed boundary/bulk/boundary realization with retained source frames and filling archive. It does **not** make filling a given primitive command, select the observation origin, identify a body fiber with an unmarked spatial vector, or derive physical time/codimension.

## 3. Neutron: real rim boundary; the tempting 3-to-12 boundary is not native G

Let J send the three sector amplitudes to the sums of their six oriented geometric triangles. This is an injective, C3-equivariant **declared amplitude-to-chain adapter**, not an identification of the actual plane-vector mode field with a scalar chain. Its Gram is 6I. Its geometric boundary B2 J has rank **3**; the equal-sector sum has six nonzero rim-edge coefficients. There is no scalar relative bulk H3 class for the uncapped belt; its surviving relative cone class is instead in degree 2.

Each sector disk has four boundary edges, yielding twelve **sector-marked edge occurrences**. The count matches the native larger alignment image, but the representations do not:

| Full interface | Transfer rank from three-sector M | C3-fixed dimension of twelve-dimensional target |
|---|---:|---:|
| Geometric patch boundary occurrences | 3 | 4 |
| Actual native M-to-C preparation | 1 | 12 |

Consequently no invertible native-operation/reader adapters can identify these two 3-to-12 maps. Restricting to the invariant active line discards precisely the moving-sector tests that expose the mismatch.

Adding the **actual two omitted caps** changes the base to a sphere, with Betti numbers 1,0,1. It adds geometric faces and requires their coefficient/readout data; it is not the same native preparation task. The unchecked cap fields or radial boundary readers cannot be silently supplied to remove the rim.

## 4. Electron: coherent code closure is not ordinary local-system top-cycle closure

The retained rank-two spinor code evaluates at each face through a rank-one projector P_f. For every face f, the checker constructs an exact nonzero z with

    P_f z = 0,       K z != 0.

The native code section vanishes at that face but not globally.

For an ordinary surface top-cycle with **invertible face-to-edge comparison maps**, vanishing at one face propagates to every adjacent face through the edge boundary equation. The tetrahedral dual graph is connected, so evaluation at any face must be injective on the whole cycle space. The native doublet violates this condition. No change of invertible fiber frames can turn its entire code into such a top-cycle space; this obstruction does not depend on selecting the trivial connection or even assuming flatness first.

This does not exclude a general cellular sheaf, noninvertible restriction system or coherent frame code. It identifies the missing type: the native face projectors are lossy restrictions whose joint family is faithful, not invertible transports of one common local state. The Pauli/Cartan bridges from iteration4 remain valid but do not restore their erased coherent sign.

## 5. A source-defined locality distinction and the next executable test

For the **active-return task with the source encoder retained**, restrict to actual primitive geometric faces and solve exact reconstruction ranks:

| Source | Active rank | Rank at every single face | Minimum faithful face count | Number of minimal covers |
|---|---:|---:|---:|---:|
| Proton | 1 | 1 | 1 | 12 |
| Neutron | 1 | 1 | 1 | 18 |
| Electron | 2 | 1 | 2 | 6 |

This is a faithful coordinate statement for the specified code, not recovery of arbitrary raw inputs, physical tomography, or a count invariant under changing the primitive port presentation. The six electron pairs are actual pairs of tetrahedral faces; each shares a geometric edge. No pair is selected as a preferred entry chart.

**Iteration6 frontier:** `minimal-geometric-reconstruction-cover-atlas`. Construct all six electron two-face/edge-associated chart readers and decoders, their transported metrics and all native spin/face transition squares, including the central sign. Compare with baryon singleton active-packet recovery. Test whether the resulting overlap context actually supplies a source-natural role/event-boundary constructor for the proposed words. Require full-reader and history compatibility; a derived inverse decoder is not automatically a primitive operation. This continues from a newly constructed source object, not from a missing-authority request.

## Verification and scope

**23 exact groups pass**, as does a same-checker frozen challenge, at prospective fingerprint `329b8c7ce7a9b20aa65bb9b408cb0d073478c66c5356cd7b30a59bf96b33be88`. This is bounded executable validation, not independent review or proof-assistant certification. The first registration audit caught a nonexistent continuation-source filename; it was corrected to the existing `check_electron_packet_extraction.py` without changing any scientific acceptance test.

```text
python research/aspect/scc/scc.py check packet-handoff-naturality-05-v1
python research/aspect/scc/scc.py check packet-handoff-naturality-net-v1
python research/aspect/scc/scc.py check port-incidence-net-v1
python research/aspect/scc/scc.py check packet-assembly-bridge-net-v1
```

No native producer entrypoint, other-owner fixture edit, proof-assistant run, commit, push, publication or deployment is performed. Physical particle assignment, common physical M/C grading and the indexed event-boundary law remain unverified.
