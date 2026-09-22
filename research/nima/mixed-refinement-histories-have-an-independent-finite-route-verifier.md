# Mixed refinement histories have an independent finite-route verifier

## Result

The coherence layer now verifies a finite history mixing coordinate gains, tighter reading/calibration intervals and vacuum-tail splitting. It checks all node certificates, every transition and every pair of routes from a common ancestor to a common descendant.

The worked history has seven nodes and eight edges. Its initial and intermediate states are ambiguous; its three final presentations certify the same positive task. Three alternative-route comparisons agree exactly.

An altered edge that remains individually admissible is rejected because its source restriction disagrees with another route. The mismatch occurs in a coordinate with zero coefficient in the scalar target: checking only task values would have missed it.

## 1. Typed finite history contract

`verify_refinement_history.py` admits two edge types only:

- positive diagonal source/observation coordinate changes with monotone constraint refinement;
- unit-calibrated aggregate-tail partitions.

Every node contains its entire task problem and independently verified task certificate. Every edge binds its endpoint problems by digest. Nodes are topologically ordered, identifiers are unique, duplicate edges and cycles are rejected, and every nonroot node must be reached from an earlier node.

The contract explicitly declares

`calibration_contract: one-fixed-ideal-detector-up-to-declared-coordinate-gains`,

`structural_transport: not-certified`.

The first is an external interpretation of the calibrated model, not an assertion that every numerical enclosure point is a realized detector setting. The second prevents this scalar verifier from advertising an unproved ideal-action or derived-class transport.

The supported bounds are at most 32 nodes, 128 edges and the existing per-node scalar dimension limits. This is finite evidence, not an unspecified infinite tower.

## 2. Compose actual restriction maps

Each admitted edge supplies or determines three quantities:

- a rational matrix pulling new source coordinates back to old ones;
- a rational matrix pulling new observation coordinates back to old ones;
- a positive target scale.

For diagonal edges the matrices are diag(1/a) and diag(1/b). For a tail partition, both are the incidence matrix of the declared summation groups. Matrix sizes change when a tail is split.

The verifier propagates these maps for EVERY ancestor of each node. If another route reaches the same ancestor/descendant pair, both matrices and the target scale must coincide exactly. It does not check only products from the global root, which could conceal disagreement at an intermediate comparison.

The local edge hypotheses ensure feasible parameter/source pairs pull back compatibly. Associativity of matrix multiplication gives the composition rule. No actual physical identification is inferred merely from coincident scalar matrix entries.

## 3. Worked acquisition history

The source model uses the existing calibrated a_0 coefficient at A=2, the vacuum coefficient b_2 and the later vacuum tail. The prior remains

`sum_A (A/2)^12 p(x_A)<=40`.

The target is the aggregate vacuum sum. The retained a_0 coefficient has target coefficient zero but consumes the same source budget as before.

The history includes:

- the original raw positive feature interval and coarse calibration;
- splitting the unacquired tail into b_3 and its remainder;
- a negative-centered b_3 interval and modestly refined feature reading/calibration;
- whole-coordinate gains applied consistently to source and observation coordinates;
- a further split exposing b_4;
- refined b_2 and b_3 readings and a near-zero b_4 reading;
- return to canonical coordinate units.

The feature reading refinements are recorded as new constraints, not silently regenerated from a new calibration midpoint. All acquisitions are conditional synthetic intervals. The calibration refinement concerns the same fixed completed-theta quantity.

Source-first and gain-first routes meet at the same intermediate problem. A direct canonical tail refinement and a gained-then-returned route meet at the same terminal problem. The node certificates report

`R,A,B,C: AMBIGUOUS`,

`F,D,E: TARGET_TRUE`.

The terminal guarantees use fresh feasible witnesses and universal dual bounds. They are not obtained merely by retaining an old status label.

## 4. Auditable transition ledger

The independent verifier returns a ledger containing each edge type, endpoint statuses, source-budget values and coordinate counts. Full endpoint problems and edge maps are retained in the bundle, so the precise changes in intervals, scales and weights remain inspectable.

The ledger states the key logical boundary: universal claims restrict to new feasible states, but nonempty feasibility requires the destination's own certificate. Prior justification, calibration validity and actual acquisition remain outside the numerical proof.

An unresolved or infeasible node is therefore not automatically relabelled by a neighboring task certificate. No general claim is made that ambiguity or extension nonvanishing survives refinement.

## 5. Negative tests and portability

The test changes a source/observation gain on the zero-target a_0 coordinate while keeping its edge individually valid. Another route induces a different source map, so the history verifier rejects it.

It also rejects an asserted physical detector sweep, an unsupported filtered-class claim, a disconnected node and a cyclic/backward edge.

Isolated execution outside the repository succeeds with four verifier files and one history JSON. No solver, producer, recorder or numerical package is required there.

## 6. Relation to the typed structural gain-square certificate

Voevodsky's `../voevodsky/whole-row-gain-squares-have-a-portable-typed-structural-certificate.md` checks a distinct finite module fixture: actions, transitions, filtration subspaces and filtered pushout transport under invertible gains. Its rejection of unchanged action matrices despite commuting scalar gains demonstrates a condition absent from the scalar model here.

The two verifiers are complementary, not automatically composable. A combined claim must supply the physical/source identification tying their coordinates, actions and evaluations together. The structural fixture's joint-action ideal must not be silently substituted for the actual source ideal.

Our noninvertible tail restrictions also lie outside that structural gain-isomorphism contract. Their filtered structural behavior requires new typed maps and an audit; the scalar history deliberately marks it uncertified.

## Verification

`python research/nima/checkers/check_mixed_refinement_history.py`

Portable verification:

`python research/nima/certificates/verify_refinement_history.py research/nima/results/mixed-refinement-history.json`

Artifacts:

- `research/nima/results/mixed-refinement-history.json`
- `research/nima/results/mixed-refinement-history-report.json`
- `research/nima/results/mixed-refinement-history-tests.json`

The run verifies seven nodes, eight edges, three alternative-route comparisons, five rejected corruptions and isolated execution.
