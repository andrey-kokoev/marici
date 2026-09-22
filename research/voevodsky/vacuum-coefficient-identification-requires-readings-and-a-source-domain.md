# Vacuum coefficient identification requires readings and a source domain

## Result

The actual old retained readings plus the acquired canonical vacuum reading do NOT identify the triple-interaction coordinate on a general source in the forgotten three-diamond slice. The ambiguity persists even if the source is known to lie in I^2.

There are three different answers, depending on the question:

- With a certified I^3 prior: no extra reading is needed for the specified minimal cubic coefficient.
- For a general source in the fixed ideal slice: one new primitive cubic vacuum reading identifies the specified target coordinate; alternatively three primitive lower-order readings suffice and are necessary within that row family.
- To reconstruct the whole seven-dimensional ideal slice from the existing vacuum reading: six additional independent scalar readings are necessary and a concrete source-derived set is verified sufficient.

All statements concern exact source records. No physical acquisition is asserted.

## 1. An actual indistinguishable pair

In each of the three consecutive prime-pair blocks, let P_i be the sorted forgotten path, Q_i the reversed one, and H_i=Q_i-P_i. Use the fixed background-two six-event corner 2->60060.

Compare

    k=(P_1-Q_1)(P_2-Q_2)(P_3-Q_3),
    x=(P_1-Q_1)(P_2-Q_2)P_3.

The first lies in I^3. The second lies in I^2 but not I^3.

Every actual old cubic seed in the declared private/sector/matched union has retained degree two. Both inputs have degree zero and already occupy the full six-event corner, so no external cubic context can add the missing marks. The shorter old stages cannot fit them. Thus all old retained readings, including all 449 separately retained matched inputs and row 76, are zero on both sources.

The acquired canonical vacuum row reads the coefficient of the all-P path. Its value is one on BOTH sources.

But their coefficients on H_1 H_2 H_3 in the specified P/H basis are respectively -1 and 0. Equivalently, their coefficients on the pure cubic k in that basis are 1 and 0.

This is a source-level counterexample to inferring the target coordinate from those observations alone, not merely a dimension argument.

## 2. Why the source prior changes the answer

On the eight-path cube, a certified I^3 source has only the triple-interaction mode. The lower-order contamination is then excluded by the source hypothesis, not by the old measurements.

More strongly, on all 90 minimal all-forgotten cubic products in the complete six-event packet, the reversed and canonical vacuum readings satisfy

    reversed_vacuum = -canonical_vacuum.

The checker verifies every product. Positive-retained-degree products contribute to neither vacuum row. Thus the earlier pure-cubic witness interpretation remains valid on its stated minimal I^3 domain.

There is no contradiction: the ambiguous comparison source above belongs to I^2, not I^3.

This distinction must be retained at handoffs. A certified filtration prior is information. Forgetting it, or applying an I^3 interpretation to a general I source, changes the inference problem.

Also, outside the pure top layer, the phrase “triple-interaction coefficient” refers here to the specified P/H coordinate convention. It is not a canonical splitting of the full filtered source extension. The frame/section convention is part of the target definition.

## 3. One extra cubic row identifies the target

The reversed vacuum row has forgotten seams

    2->6, 12->84, 420->5460,

outer corner 2->60060 and vacuum buffers. It selects the all-Q path. On the fixed cube this is exactly the coordinate m_123.

This existing labelled record coordinate is source-derived and requires no arithmetic feature normalization. It is a NEW acquisition relative to the old retained readings. It cannot be computed from the ambiguous old observations.

Zero extra readings cannot suffice because of the displayed pair. One primitive row does suffice. This is minimal for target identification when an additional cubic row is allowed.

It is not full reconstruction: on the seven-dimensional ideal slice, the canonical and reversed readings have joint rank two, leaving five source directions undetermined.

## 4. If only lower-order primitive rows may be added

Three two-seam, all-vacuum rows give another exact solution. All have outer corner 2->60060, not the shorter support of the old stage-two detector.

| Row | Forgotten seams |
|---|---|
| R1 | 12->60 and 420->4620 |
| R2 | 2->6 and 420->4620 |
| R3 | 2->6 and 12->84 |

For path coefficients a_b, with bit i indicating reversal of block i,

    R1=a_000+a_001,
    R2=a_001+a_011,
    R3=a_011+a_111.

If v=a_000 is the already acquired canonical vacuum reading, then

    m_123 = R1-R2+R3-v.

The checker enumerates all 18 distinct primitive two-seam row vectors on the cube. Every one-seam row vector already occurs among them; the zero-seam row vanishes on the ideal slice. It tests all 172 subsets of size zero, one or two and proves none identifies the target alongside v. The displayed three rows do.

Thus three primitive lower-order rows are minimal in this family. Their signed sum is one scalar OUTPUT but is not one primitive acquisition. Under the lossless-retention rule, computing that sum does not authorize discarding the three acquired inputs without a reconstructive residual.

For error bounds, the identity gives the ordinary estimate

    target error <= |error_R1|+|error_R2|+|error_R3|+|error_v|.

This is conditional error propagation, not a certificate that such acquisition precision has been achieved.

## 5. Full reconstruction without an archive

Restrict to the declared seven-dimensional space I intersect the eight-path cube. Its known constraint is sum_b a_b=0.

Starting with v and the reversed row, the checker selects five further actual two-seam rows that complete a rank-seven measurement matrix on the basis path_b-path_000, b!=000.

The artifact contains the seven row definitions, exact matrix and rational inverse. A decoder reconstructs the entire source from those seven measured values and the public typed source model. No original-source capsule, stored source coefficients or producer lookup is used.

This is dimension-minimal among linear retained data on this domain: the existing vacuum has rank one, so six additional independent scalars are required. The seven readings are not asserted faithful outside that domain. Sources outside the cube require a new separation audit rather than reuse of this inverse.

## Understanding gained

A nonzero vacuum measurement answers a coordinate question, not automatically a source-classification question. Its interpretation depends on three items kept together:

1. the actual acquired readings;
2. the admissible source domain and certified filtration membership;
3. the coordinate/frame convention defining the target.

With these specified, the required retention can be computed exactly. Without them, the same numerical measurement can support incompatible cubic interpretations.

## Verification

    python research/voevodsky/checkers/check_vacuum_coefficient_identifiability.py

This freshly runs the residual-cube checks, verifies invisibility against the actual old manifest/support, constructs the indistinguishable pair, checks all 90 minimal forgotten cubic products, exhausts the insufficient lower-row subsets, and performs exact serialized source reconstruction.

Artifact: `results/vacuum-coefficient-identifiability.json`.

All checks pass. Scope: finite exact source algebra and unit-vacuum records, not a global observer equivalence or physical deployment.
