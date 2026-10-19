# Tower comparison and an independently specified rotation/realization square

## Disposition

The revised plan yields three distinctions supported by explicit source types
and exact field calculations:

1. The P field really decorates the twelve directed arrows of the earlier
   primitive carrier: three complex vector components per directed arrow.
   Forgetting that decoration matches the existing primitive support, but does
   not transport the field through the generating or pinned T9 interface.
2. Ordered-corner coefficients and spatial patch vectors admit an exact,
   independently specified rotation-compatible realization. It is invertible:
   this step is a coordinate realization, not a new coherence degree.
3. Forgetting the geometric C3 action admits a projector-role-exchanging PN
   isomorphism; restoring that action is obstructed. The obstruction has rank
   two on the alignment sector and disappears under the common return readout.

No rung is assigned to the current field solely from these results.

## Which tower is which?

| Construction | Objects and maps | What changes or survives | Status for our field |
|---|---|---|---|
| Earlier label/from/to recurrence | Row types E; dependent totals of selected-column fibers | Each total recovers E; nested selector provenance retained | Can organize records; does not derive gauge groups or new coordinates |
| Confirmed 12/11/10 and 6/5/4 diagram | Raw/source-/target-indexed presentations; 9/8/7 are horizontal operation roles | Both squares must commute on declared semantic data; route histories remain distinct | Relevant target architecture; our field is not yet bound to its whole operation |
| Generating horizontal candidate | Twelve primitive directed arrows plus a supplied Context -> retained comparison families | Introduces 121 arrow-pair and 16 state-pair slots inside G9/G8/G7 | P directed-arrow SUPPORT matches exactly; field-to-Context preparation is absent |
| Pinned software T9 | The specified 137 records -> 32 -> 32 families | Preserves full leaves, masses, endpoints and the exact 977-pair domain | Implemented software, not a direct input interface for a 36-vector |
| Gram restriction tower | Positive-metric coefficient spaces and metric-adjoint projections | Reduces live rank; discarded orthogonal data can be retained separately | Conditional Hamiltonian models exist; these projections are not retained-total equivalences |
| Coherence-filler tower | R_(k+1)=Sigma(r:R_k) Fill_k(r) | Adds a witness over a specified lower boundary; fiber may be empty or forced | Formal tetrahedral/dg examples exist; current field must supply its own typed boundary |
| Realization-fiber comparison | Implementations with named actions, observations and forms | Isomorphisms must preserve the declared structure; characters can obstruct them | Directly relevant to the PN geometric-action failure |
| Postnikov tower | Homotopy truncations of a specified space | Higher homotopy and attaching invariants determine extensions | No identification of the above numerical rung labels has been supplied |

The current interpretation of the operator-confirmed diagram is

```
12 --9--> 6
 |        |
11 --8--> 5
 |        |
10 --7--> 4
```

It is not the earlier eight-successor retained-total recurrence. The older
U(1)/SU(2)/SU(3) assignments with multiplicities 1,2,4 remain proposed
correspondences, not derived gauge groups. In particular, the four in a rung
label, a coefficient rank or an event dimension has a different type each time.

Source entrypoints:

- `research/nima/label-from-to-fibration-tower.md`
- `research/nima/rung-transport-diagram-and-fixed-reference.md`
- `research/strominger/generating-horizontal-schedule-v1.md`
- `research/nima/pinned-T9-software-contract.md`
- `research/nima/carrier-gram-restriction-tower.md`
- `research/nima/coherence-realization-depth-is-a-dependent-filler-tower-not-a-source-cutoff.md`
- `research/kitaev/realization-fiber-coherence-rung.md`
- `research/strominger/hamiltonian-descent-wg-and-postnikov-clues.md`

These source interpretations were audited, not all their implementation suites
freshly executed in this task.

## Actual connection to the primitive carrier

The existing generator declares

```
full_edges = tuple((i,j) for i in range(4) for j in range(4) if i != j).
```

The checker evaluates that isolated declaration from
`check_two_block_leaf_generation.py`, without executing its dependency chain.
With A,B,C,D mapped to 0,1,2,3, these are exactly the P patch labels. Every patch
has its three native x/y/z components, and the correspondence commutes with all
proper vertex permutations. This is an endpoint-labelled correspondence, not
merely the arithmetic identity 36=12*3.

But bare `Primitive` records retain only label/source/target. Different fields
on the same twelve arrows have the same bare support. The generator's Context
additionally specifies an excluded mark, state roots, numerical assignment and
policy. Nothing tested here derives that numerical preparation from the field.
The pinned T9 has yet another input domain: already formed comparison records.
These missing interfaces cannot be replaced by silently dropping the field.

## Independent square

For each P patch g, let X_g have its ordered triangle corners as columns. Set
B=direct-sum X_g. It maps the 36 ordered-corner coefficients to the 36 spatial
patch-vector components. The source metric is K=B*B; the target metric is I.
Every X_g is invertible, and the checker verifies both block inverse identities.

For a proper tetrahedral isometry p:

- V_p permutes the ordered patches in corner-coefficient coordinates;
- U_p permutes the patches and rotates their spatial vector components by the
  rotation obtained independently from the tetrahedron vertices.

Neither action is manufactured by conjugating the other through B. Exactly,

```
U_p B = B V_p,
U_p* U_p = I,
V_p* K V_p = K.
```

All twelve squares and all 144 group-composition comparisons pass. Ordered
corner cycles and native target L/G are preserved. Only two of these proper
symmetries also preserve the fixed body C/M partition; no native path admission
is inferred for the full group.

Two controls fail for each of the eleven nonidentity rotations:

- permute patches but omit rotation of the vector components;
- replace every actual patch frame by one repeated reference frame.

The second control has the same source metric and remains invertible. Thus
metric agreement alone would not detect its lost attachment information.

## A precise forgetful comparison and its obstruction

Consider a coarse category of positive-metric spaces with two named commuting
orthogonal projectors. For the target N object exchange the names of its L/G
roles. The source and target then have equal joint-sector dimensions
(1,11,2,22). Metric-unitary coarse isomorphisms exist by sectorwise isometry.

In the decorated category also retain the independently defined geometric C3
action, and require morphisms to intertwine it. Forgetting this action defines
a comparison to the coarse category. The lift fiber over every PN coarse
isomorphism is empty: the corresponding three-dimensional sectors have rotation
characters 3 and 0.

The fresh calculation locates the discrepancy more precisely. Write N_P and
N_N for the native rank-one return projectors, not the carrier spaces. For
any metric-unitary S satisfying both projector-role exchanges, let

```
E = (U_N S - S U_P) G_P.
```

The source geometric C3 fixes G_P pointwise. On the N local sector the C3
average is exactly N_N. Therefore

```
E^sharp E = 3 (G_P - N_P),
rank(E) = 2,
N_N E = 0.
```

The target identity checked directly is

```
[(U_N-I)L_N]^sharp [(U_N-I)L_N] = 3 (L_N-N_N).
```

It holds for both N geometric order-three actions; the source identity holds
for all eight P order-three actions. The universal statement about S follows
algebraically from the two role exchanges and metric unitarity, not from one
chosen complement frame.

Thus the common return readout hides exactly this relative-sector obstruction.
It does not make the full rotation/conversion square commute. This is an
obstruction to restoring named geometric structure, not a computed Postnikov
k-invariant or permission to add an unspecified higher filler.

## Verification and stopping point

```
python research/strominger/checkers/check_rotation_realization_square.py
python research/aspect/scc/scc.py check rotation-realization-square-v1
python research/aspect/scc/scc.py categorical research/strominger/contracts/rotation-realization-square-v1.json
python research/aspect/scc/scc.py inverse research/strominger/contracts/rotation-realization-square-v1.json field_is_rung12
```

The checker freshly reruns the prior native field-rigidity audit. Its receipts
are `results/rotation-realization-square/verification.json` and
`categorical-verification.json`. The SCC contract hashes independently evaluated
composite matrices: SCC compares those tokens, while the exact matrix proof is
in the checker. Unsupported numbered-tower binding remains unsupported even
when the twelve coordinate squares pass.

The inverse result leaves `field_to_T9_input_adapter` and
`operation_preserving_binding` missing. The broader registry discovery commands
returned nonzero status; the owner-local model check passed. No unrelated
registry repairs were attempted.

The precise next construction is a field-to-comparison preparation on the
matched twelve-arrow support, preserving enough relative-sector data to test
operations. Choosing only the common return would already erase a demonstrated
obstruction. No 4D spacetime readout, physical time, gauge multiplicity,
Postnikov identification or production/viewer change is claimed.
