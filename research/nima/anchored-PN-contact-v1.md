# Anchored PN contact comparisons preserve the relative obstruction

## Result

A recoverable, typed contact-comparison packet is now implemented. It retains the entire P and N input fields—including all three neutron sectors—and distinguishes the two routes of the named geometric-C3 square.

It does **not** make that square commute. Exact field recovery reconstructs a rank-two difference whose weighted Gram matrix is3I2. Native neutron return and sector averaging erase the difference; the full comparison packet does not.

## What the packet retains

The contact label is the saved final-assembly P reader2/N reader6 interface on cells0/2. Complete marked reader records, origins, coefficient permutations and native witness IDs remain attached metadata. The field coordinate conventions are declared source conventions, not a derived physical face attachment.

| Port family | Patches | Components per patch |
|---|---:|---:|
|P|12|3|
|N|18, arranged in3 sectors|2|

P fields are expressed in their retained co-moving patch frames. N fields keep their source internal plane labels and positive weights, all affine reader charts and their transition/loop records. They are not averaged into a12-component reader, and their components are not silently declared Euclidean tangent vectors of the target tetrahedron.

For every ordered pair of patch ports, retain

`C_ji = q_j q_i* H_i`.

The source metric H_i is part of the typed operator. Counts are144 P/P blocks,324 N/N blocks,216 N←P blocks and216 P←N blocks: **900 total**. Cross blocks really have dimensions2×3 or3×2; no legacy2×2 multiplication is used.

These are comparisons between entire source coordinate fields tagged by one marked contact. We have not identified a physical shared-face restriction or imposed equality of the two fibers.

## Recovery and phases

One nonzero complex amplitude anchors the common phase of the combined P/N input. The anchor column reconstructs every coordinate by exact division, including its retained source metric factor. Recovery then regenerates and verifies **every block**. All-zero data use a separate no-anchor case. Exact radical inversion uses sign conjugations and a bounded square-class basis; an excessive inversion basis raises an explicit error rather than approximating.

- Multiplying both fields by a common phase preserves every block but changes the anchor.
- Changing only N's phase preserves both self-comparison families but changes the cross blocks.
- If either entire carrier is zero, the other carrier's anchor still permits recovery.

The anchor is chosen input/reference data, not a derived physical calibration. Keeping a phase in a record does not establish a unique physical phase convention.

## The retained rotation discrepancy

Use the native orthonormal contrast frame K and the saved PN metric-unitary candidate S. Compute its source preimages `Q=S^sharp K`. Fresh checks show Q is orthonormal, belongs to the P alignment sector, and is fixed by an actual geometric P C3 action.

The competing outputs for each of the two inputs are K and U_N K. Here U_N is constructed from the actual native belt vertex/patch permutation, not chosen to fit the desired mismatch. The equality S Q=K uses the saved PN unitary identity; it is not a fresh dense inverse-product calculation.

Prepare and recover both complete P/N packets. Their reconstructed difference D satisfies:

- `D^sharp D = 3 I2`, so its rank is exactly2;
- native neutron return sends both competing output fields to zero;
- averaging their three sectors also sends both output fields to zero;
- their full operator-comparison packets differ.

This gives an explicit recoverable witness of the obstruction, not a new proof that a geometric PN intertwiner exists or a new permission to fill its failed square.

## Checks

-11 exact recovery cases, including zero, one-carrier-zero, dense fields, common/relative phase changes and the native obstruction routes.
-900 block covariance checks for the independently sourced P/N carrier rotations; these actions are not newly admitted native reader moves.
-Eight malformed packets rejected: missing N sector, missing cross block, wrong anchor magnitude, wrong metric, erased chart transition, truncated rectangular map, false zero stratum and forged non-anchor block.
-Source inputs checked unchanged over execution. No source-owner receipt or implementation is rewritten.

An initial checker error compared the weighted N isometry against the Euclidean identity. It was corrected to check `U_N* M_N U_N = M_N`; the retained source metric is not the identity.

## API and reproduction

`anchored_contact_comparisons.py` exports `prepare(descriptor, values)` and `recover(packet, expected_descriptor)`. Values are full patch-coordinate vectors in the declared conventions. The checker supplies the native frame adapters and demonstrates inverse recovery to the original spatial P/internal N coordinates.

```sh
python research/nima/checkers/check_anchored_pn_contact.py
python research/aspect/scc/scc.py check anchored-PN-contact
```

[Protocol](anchored-PN-contact-protocol-v1.md) · [Receipt](results/anchored-PN-contact/verification.json) · [Full comparison packets, gzip JSON](results/anchored-PN-contact/packets.json.gz)

## Next boundary

We now have an interface that can carry—not erase—the failed square. The next construction is to type the additional seam data or relative comparison witness required by a proposed geometric attachment. Any relaxation of named C3 compatibility must be explicit. This packet alone supplies neither physical sewing nor the missing historical T9/state-root preparation.
