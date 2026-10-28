# Native query physical realization — revision 2

Revision 2 separates mathematical realization selection from physical implementation and adds four typed coherence faces and one tetrahedral coherence obligation. No new physical or higher-coherence result is claimed. All seven resolved revision-1 nodes and their scopes are unchanged.

## Two outputs

### A. Mathematical realization moduli

Freeze G=A4, its two triangle left actions, six native transition functions and controlled-XOR recorders. On R^G tensor R^2, use positive product pairing H tensor R_eta, where

    R_eta = [[1,eta],[eta,1]], -1 < eta < 1.

Eta is supplied, not selected. The exact finite generator fragment and its native semantic comparison must be declared explicitly; this is not all native WG or automatically the original endpoint-typed route language.

Output A consists of invariant pairings and operation interpretations modulo isometries preserving named operations and readings. The classification target is H=cI, c>0; unit feature normalization sets c=1/3. Necessity follows from the existing conditional recording/translated-query arguments; sufficiency follows from the counting carrier metric and pointer-swap invariance. Assembling the precise moduli interface and native-fragment binding remains an open deliverable, rather than silently promoting those component proofs.

No physical orthogonality, absolute unit or pointer-overlap selection follows merely from constructing this mathematical output.

### B. Physical protocols in one frozen model

Before asserting existence, name ONE physical model M with a primitive interaction grammar, controls, preparations, readout, auxiliary systems, timing, resource-return rules and operational equivalence. Choose exact correctness or explicitly quantified approximation; neither is silently interchangeable.

Then the implementation conjecture is:

> There exists a compositional compiler of every finite word in the declared generator fragment into finite protocols of M, whose execution realizes a member of Output A and satisfies the declared record and resource contracts.

A failed search is not a refutation. A source invariant excluding the required coupling, or unavoidable violation of return/continuation requirements, is a scoped falsifier. Enlarging M after failure creates a new conjecture version.

M has NOT been selected by this revision. In particular neither a pairing-preserving controlled reflection nor an arbitrary nondemolition recorder may be inserted as an unexplained primitive simply to satisfy the conjecture.

## Tetrahedron

Vertices:

- S: frozen source processes;
- N: native constructions;
- P: permitted physical protocols;
- R: interpreted transformations, records and auxiliary/continuation semantics.

Edges:

    a:S->N   b:N->P   c:P->R
    d:S->P   e:N->R   f:S->R

Faces:

| Face | Cell | Obligation |
|---|---|---|
| S-N-P | alpha: b a => d | Direct and native-mediated compilation agree in the declared protocol equivalence |
| S-N-R | beta: e a => f | Native-mediated and direct source interpretation agree |
| N-P-R | gamma: c b => e | Physical execution realizes the native operation |
| S-P-R | delta: c d => f | Direct source compilation has the required execution semantics |

The tetrahedral obligation compares the two pastings from c b a to f:

    (c whisker alpha);delta = (gamma whisker a);beta.

This requires actual types for the face witnesses and their higher comparison. It is not established by four scalar equalities or by four unrelated passing checks. Every comparison must retain preparation, named pointer readings, successor states, auxiliary return, and authorized continuations. The direct arrows may be related by construction, but tautological definitions are not independent evidence of physical implementation.

All four faces and the tetrahedral witness remain OPEN. The native recorder theorem supports part of the source/native construction, not the entire tetrahedron.

## Actionable frontier

1. **mathematical-realization-moduli:** assemble Output A with its exact fragment and equivalence relation.
2. **freeze-physical-model:** name M and freeze its allowed operations and resource/accuracy contract.

Physical compilation, four face comparisons, tetrahedral coherence and final assembly are blocked open obligations. There are 16 nodes: four rejected candidates, three established scoped constructions (two conditional), and nine open obligations. The physical root remains open.

## Versioning and audit

- Contract: `contracts/native-query-physical-realization-net.v2.json`
- Revision-specific pointer: `contracts/native-query-physical-realization-net.v2.current.json`
- Receipt: `results/native-query-physical-realization-net/verification.v2.json`

The revision-1 contract, pointer, packet, checker, pins and receipt are preserved. Its pointer is a pinned revision-1 artifact; revision 2 uses its own explicitly named pointer. The completed WG parent is unchanged. This is owner-local registration, not graph-service publication.

    python research/strominger/checkers/check_native_query_physical_realization_net_v2.py --freeze
    python research/strominger/checkers/check_native_query_physical_realization_net_v2.py

The checker validates historical verdict preservation, two-output typing, all face/edge boundaries, the higher pasting, DAG connectivity, actionable frontier, scope guards, evidence receipts, native proof provenance and immutable pins. Corruption controls reject erased faces, false physical promotion, wrong pasting and an asserted frozen model. It does not rerun Agda or prove any new coherence claim.
