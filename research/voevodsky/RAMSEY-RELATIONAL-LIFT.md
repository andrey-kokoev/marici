# Ramsey relational lift and single reduction — conjecture net

**Root: open.** [Contract](contracts/ramsey-relational-lift-conjecture-net.v1.json) · [checker](checkers/ramsey_relational_lift_net.py) · [receipt](results/ramsey-relational-lift-check.json) · [attempt log](results/ramsey-relational-lift-attempts.jsonl). This is a separate inquiry from the [tetrahedral–octahedral net](RAMSEY-TETRAHEDRAL-OCTAHEDRAL.md).

## Question and success condition

Are the two parameters coordinates of a relational arithmetic? Find one source operation that realizes the proposed four- or eight-dimensional lift under rotation, reflection and duality. Find one reduction that identifies redundant linkages, recovers the two parameters up to color exchange, and derives the signed correction to their product. Steps describe composition, rather than time. For (3,7) success explains the two extra cells and why the readout is a threshold. The root seeks a general principle. Each route proposes its own domain. Derive a correction by identifying additional cells or justified cancellations, then predict the order by adding the correction to the baseline. Reading a threshold first and subtracting the baseline fails this requirement. Duality and the choice of trace or span belong to each proposal; four or eight labels alone prove neither dimension.

Define a cell before counting it. State the equivalence on linkages before consulting the answer. Distinguish: ambient vector dimension, actual linear span, number of orbit positions, number of cells, size of an avoiding coloring, and first forbidden order. When counting cells by signed inversion, also supply the theorem identifying the signed result with the correction. Input labels passed unchanged through the output do not constitute intrinsic coordinate recovery.

## Map

| Node or branch | Question or decision |
|---|---|
| `clock` | Scoped pilot: characters at frequencies ±7 and ±3 on the cyclic group of order 21 are distinct and orthogonal. Each conjugate pair spans its real sine/cosine plane. Chinese remaindering gives all 21 positions. Reflection reverses time-index sign; exchanging the factors exchanges the parameters. |
| `positions-only`, `root-only` | Scoped counterexamples: taking a quotient cannot turn 21 positions into 23; merging fixed-root states can destroy a different root's distinction. Neither control refutes the root. |
| `cells` | Define a finite linkage generator independent of the desired readout. An edge, occurrence, and equivalence class are three different possible objects. |
| `phase`, `inversion`, `boundary`, `weights`, `brackets` | Rival constructions: linked phase orbits; incidence inversion; equivalence under all attachment contexts; shared pair coefficients; equality of bracketed assembly histories. Each has its own falsifier in the contract. |
| `pair-types` | Optional side experiment for `weights`; the primary task specifies both source operations. |
| `quotient` → `readout` → `threshold` | Select at least one viable branch. Prove compatibility under reflection, color exchange, change of viewpoint, and composition. Recover the coordinates; give both a witness at C−1 and an obstruction at C. Retain the same lift and reduction throughout. |

The candidate edges are alternatives. A successful numerical screen enables work on its branch. The root requires separate review. Exact finite controls use known thresholds only as external checks. Negative, zero, and positive corrections occur at (3,5), (3,6), and (3,7). The 39-role (3,10) witness establishes a lower bound; it is a separate type of control.

## Tested priors (revision 4)

Six scoped nodes constrain candidate design. `prior-fourier` distinguishes four phases from dimension; `prior-cone14` requires a source-derived cutting rule before using a numerical match; `prior-seed-uniqueness` exhibits two admissible decoders up to isomorphism. `prior-interface` distinguishes the two C5 boundary colors. `prior-weight-order` separates the order of a coefficient from its type; `prior-local-pair` rules out every coarsening of the specific 21-type partition on residual 1253 for the six-port certificate. Each contract entry identifies its source, scope, receiving nodes and verification level. The seed census and interface polynomial ran again at import. For the incidence hierarchy and 1253 dual the net pins the report; the full certificate bundle was unavailable for replay.

`frontier` shows constraints for each work card; `show --node weights` displays the two coefficient results. At route freeze add `prior_response` keyed by each prior applying to `cells` or to the named branch. Each response specifies `relation` (`respects`, `different_scope`, or `challenges`) and a reason. Record a concrete scope difference or counterevidence when departing from a prior. These are research constraints, not proof dependencies or votes on the root.

## Three open conjectures from the Fourier-extraction comparison (revision 5)

[Theorem 5.1 of Bostanci, Nehoran and Zhandry](../../references/2411.00529v2.pdf) motivates the distinction between extracting a representation and discarding a component. The theorem concerns quantum representations. The following are independent Ramsey conjectures:

1. `pentagon-8d-continuations`: test the 8D operator against attachment families for all four admissible masks, using the same seed symmetry. Restricted square traces 20 and 12 distinguish two examples; the continuation claim remains open.
2. `pentagon-summand-duality`: compare exchange of the side and diagonal contrast spaces before reduction with an independently specified coordinate exchange after reduction.
3. `component-elimination-37`: characterize removable components by preservation of every attachment, then recover both coordinates and the two literal extra cells from one reduced object. The two mean coordinates discarded in the pentagon example are distinct from these cell witnesses.

## T184 and the pentachoron star (revision 6)

Two distinct conjectures concern the same four vertices. `t184-port-readings` asserts that the native links recover the four attempt readings. `t184-opposite-face-star` asserts that the whole cell supplies one dual center and its native links match the four branches to the opposite faces. Either claim can be tested independently of the other. Together they identify the four branches with the four ports.

The sign map (a,b) ↦ (a,b,ab) gives an abstract regular tetrahedron. For a facet V of a pentachoron with opposite vertex p, the four neighboring facets are {p} ∪ (V minus {v}), one per v in V. These identities define the comparison. The earlier [middle-band check](../chatgpt/ramsey/ramsey_esd7_opposite_edge_middle.py) locates T184. The new claims concern what its Ramsey links themselves determine. Freeze the native link signature and role readings before testing; until then both nodes retain an open verdict.

## Tetrahedral foam recognition (revision 7)

`tetrahedral-foam-37` asserts the existence of a 22-cell foam and an intrinsic pair rule that reads a (3,7) witness from it. Count the interior bubbles; the container boundary supplies geometry. Freeze the model and rule before comparison with Ramsey graphs. Treat 23 as the order at which Ramsey's theorem forces a monochromatic obstruction for every such reading. Direct red film contact already produces a red triangle where three distinct cells meet at an ordinary Plateau border. Center-to-vertex transport offers a separate candidate reading.

## Ramsey's formal-logic lens (revision 8)

[Ramsey, pp. 280–281](../../references/1930-ramsey.pdf) records both directions of a binary predicate. Exchanging the arguments fixes two readings. Exchanging the attempt aim fixes zero ports. An identification of these actions requires more than relabeling. A second control separates arities: changing an independent ternary value can preserve every binary reading.

| Node | Role in the net |
|---|---|
| `logical-boundary-reconstruction` | Open template for unique reconstruction from compatible boundaries. [Hackney, Theorem 25](../../references/2607.24476v1.pdf) supplies hypotheses to test, rather than a Ramsey result. |
| `logical-component-descent` | Open template for a proper component reduction on whose fibers the forbidden-clique formula has constant truth value. [Bostanci–Nehoran–Zhandry, Theorem 5.1](../../references/2411.00529v2.pdf) motivates distinguishing extraction from erasure. |
| `extremal-forcing-stress` | Necessary external check on a route's predictions. [Hefty et al.](../../references/2510.19718v3.pdf) supply avoiding orders in their asymptotic regime. |

These entries organize research directions. The two templates require frozen definitions before a mathematical verdict. The stress check compares a prediction against independent witnesses after generation.

## Blue five-set pair coverage (revision 9)

`blue-five-set-pair-coverage` asserts that every blue pair belongs to a blue five-set on every 16-vertex triangle-free red graph with independence number at most five. The [witness-index checker](checkers/ramsey_witness_index_tower.py) and [finite result](results/ramsey_witness_index_tower.txt) support the separate prior `prior-five-set-coverage` on the 39 residuals with 33 red edges and the two tested 34-edge controls. Both controls also admit six compatible ports: the coverage test and the port test answer different questions. The next test checks every pair in each of the 2,576 catalogue records and saves the first uncovered pair and its graph if one occurs.

## Database index-design conjectures (revision 10)

Three open nodes separate **coverage**, **physical cost**, and **one logical output**. First freeze the residual-graph corpus and the query contract: recover pair colors, enumerate disjoint five-sets, and decide six-port compatibility with witness identities. Include empty intersections and controls where six ports do fit. One query workload serves all three comparisons.

- `olap-ramsey-index-coverage`: use cube dimensions and aggregation levels to select materialized views; require drill-through to actual witnesses. Equal counts can hide different witness sets. Charge the underlying detail if the query uses it.
- `vertipaq-ramsey-storage`: test the strongest efficiency claim only within a fixed competitor class and cost model. Compare Power BI Import/VertiPaq, row-store SQL, and bitsets using the same answers. The DAX formula engine and storage engine contribute different costs to end-to-end latency.
- `ramsey-single-matrix-optimizer`: freeze a finite set of block layouts and choose one by cost subject to query budgets. For a baseline let B index vertices by blue five-sets, with B[v,S]=1 for membership; use a square matrix indexed by their disjoint union, with B and its transpose off diagonal. Vertex-to-vertex two-step walks retrieve common five-set witnesses; five-set-to-five-set walks retrieve shared vertices. If some blue pair belongs to zero five-sets, incidence alone cannot justify decoding an empty result as red. Compare a layout that retains the original color block. Axis types and identifiers belong to the representation and count towards its cost. This is a starting layout, not an optimality verdict.

The index designer can emit a matrix as a SQL relation of row ID, column ID and value with declared zero semantics. Merely pivoting an adjacency table, calling an execution plan, or storing a serialized database in one entry does not resolve these conjectures. The engineering claims concern indexes on supplied structures; the root still asks for a source-derived lift and reduction.

## Joint reconstruction as a redundancy criterion (revision 11)

Freeze a readout, the retained data, and the constraints. Hide the proposed links **together**. Require at least one compatible reconstruction. If every reconstruction agrees on the readout, those links are redundant for that readout. Two reconstructions with different answers witness lost information. For exact graph recovery the readout is the entire labeled color vector.

`redundant-links-by-joint-reconstruction` conjectures that the bare blue-five-set index passes this criterion on the full 16-vertex (3,6) domain. [Record 36](results/ramsey_index_ambiguity36.json) passed despite lacking a direct witness for one blue pair. Test the remaining 21 patch cases first. Family-wide closure requires excluding alternative reconstructions even for inputs on which direct lookup happened to agree with the source. This is a storage criterion, independent of query speed and of the root's two additional cells.

## Database indexing literature as a constructor (revision 12)

`db-literature-ramsey-constructor` is an existential literature hypothesis. Its distinctive claim concerns **index construction**, upstream of the existing matrix optimizer and reconstruction tests. Translate the forbidden red and blue patterns into a relational query workload. Look for a published builder that generates intermediate witness relations and a reduction that retains precisely the requested readouts. Decide whether the database method supplies the actual linkage and elimination rules or merely executes rules supplied by a Ramsey specialist.

Two bibliographic starting points are [Space-Time Tradeoffs for Conjunctive Queries with Access Patterns](https://doi.org/10.1145/3584372.3588675) (which access patterns determine what to index?) and [Free Join: Unifying Worst-Case Optimal and Traditional Joins](https://doi.org/10.1145/3589295) (which intermediate bindings does the join plan generate?). Both date to 2023. They seed a forward citation search; neither establishes the conjecture. Also search view determinacy and rewriting for a reduction test: do two expansions agreeing on the retained index always agree on the requested answer?

First work product: a dated source-to-operation table naming each paper, input, output, guarantee, required base relations, and any new Ramsey-specific assumption. Reject a proposed translation as a full answer if it needs the target graph or hides the cell generator inside an oracle. A faithful constructor must meet the existing lift, reduction, cell-witness and threshold gates. The record-36 decoder and three-layout matrix pilot supply controls for the weaker task of indexing an already supplied graph.

### Revised conjecture after the join pilot (revision 13)

The join generates colorings. The open conjecture concerns its reduction: a literature-derived index key computed from a partial row and the frozen join plan identifies two rows exactly when they permit the same exterior assignments. Compare rows at the same cut on the same labeled exterior variables. Require a real merger of live rows, retain provenance for distinct interior witnesses, and predict the same first empty order as the full join. Exhaustive completions are a test oracle, not a key-generation method. A shared key with different futures refutes soundness; distinct keys with identical futures refute exactness. The [two-paper audit](ramsey-db-literature-source-map-2026-11-19.md) and [SQLite pilot counts](results/ramsey_db_constructor_join_probe.txt) establish the baseline only. The parent still requires the literal (3,7) cell correction.

## Six database roles as three antipodal pairs (revision 14)

`db-six-antipodal-roles` records the operator's source proposal. Products and customers supply the two endpoint types. Approval versus blocking describes the offer side; interest versus ignoring describes the customer side. For example, approval plus explicit ignoring and blocking plus interest are different bottlenecks even if both yield an empty successful-match query. Missing evidence stays distinct from an explicit negative. These roles can be indexed in six directions or stored in fewer physical tables.

Test logical necessity by axis ablation, rather than by counting tables. Freeze the DB-to-Ramsey translation first. For each axis seek an identical projected state with different legal Ramsey futures. Compare the full representation against the completion oracle for sufficiency. This tests three proposed relational distinctions, not Euclidean dimension or universal SQL optimality.

## System of claims and implications (revision 15)

`system-of-claims-and-implications` distinguishes a forbidden joint assignment from a derived value. The [Boolean SQL control](sql/claim_vs_joint_negation.sql) exhausts four answered pairs: a mixed pair violates equality but remains admissible when conjunction is merely the reported outcome. The [witness-group pilot](results/ramsey_transpose_witness_groups.json) tests immediate implications, not existence of a legal completion. Neither result settles the six-role sufficiency claim.

## Rooted core size crossover (revision 16)

`rooted-core-size-crossover` compares full minus neighborhoods, not arbitrary induced subgraphs. The [root-chain census](results/ramsey_root_chain_envelopes.json) gives a 16-parent with a 13-child versus a largest child of 12 in all seven catalogued 17-parents. The universal comparison uses catalogue completeness. Independently, the [1+4+17 construction](results/ramsey_37_root_glue.json) certifies the lower bound R(3,7) ≥ 23. It proves neither the upper bound nor a size crossover at (3,7).

## First work card: one complete candidate

Freeze one candidate's lift, literal linkage occurrences, single reduction and readout together. Define rotation, reflection and duality, select trace or span, and state the claimed 4D or 8D property. State a domain. The primary route derives literal additional cells. A signed route tests a separate extension. For the latter, justify what each cancellation removes. Pin this specification before calculation. The review sequence is lift → reduction → cell-derived prediction → threshold comparison → scoped closure. Each stage keeps the same frozen specification. Independent labels, a post-hoc subtraction, and a coefficient certificate alone fail at distinct gates.

## Secondary work card: pair types

**Problem:** unconstrained pair coefficients certify all 39 catalogued residual cores; arbitrary vertex coefficients certify 19. Can four intrinsic readings replace the free pair coefficients? [Prior exact result](../chatgpt/ramsey/ramsey_incidence_moment_duality_2026-11-09.md).

**Protocol:** before accessing the certificate values, specify the two-link path or set of intermediate roles, color orientation, reduction of multiple readings, and whether the four coefficients may vary across cores. Record the frozen specification in the attempt log. Build its type-incidence matrix. For each residual graph ask whether it induces nonnegative weights z with Dz ≥ 1 and sum(z) < 6, where D tests disjointness of blue five-sets. Verify rational witnesses, or verify an exact dual certificate for one failing core. Report the full denominator and scope. Success screens the coefficient partition; it leaves the integer cell count open. Failure rejects that partition only. Rival: pair-specific coefficients contain information which four types lose.

## Run and maintain

From the repository root, use `python research/voevodsky/checkers/ramsey_relational_lift_net.py` followed by:

- `verify`: replay the exact controls, validate the dependency graph and evidence paths, and compare the current receipt including evidence hashes.
- `frontier`: list executable claims and their decision criteria. `show --node pair-types`: inspect one node and its history.
- `record --node ID --outcome CODE --summary TEXT --evidence PATH`: append a scoped attempt with a digest of a durable repository file. Use a **fresh immutable evidence file** for a new attempt. The codes distinguish proof, failed proof, refutation, and failed refutation. To freeze a planned experiment, save its protocol before the run; the attempt log records the resulting evidence when the attempt ends.
- `check`: compute the current report without writing. `snapshot`: explicitly save the reviewed current report. A snapshot authenticates local file consistency, not mathematical truth.

### Reviewed route lifecycle (revision 3)

`route-schema` lists required specification and proof fields. Save immutable JSON events under the repository. Use `route-event --evidence PATH` for each; the command validates the entire journal before appending. Supply a unique `route` string in every event. Hashes below are SHA-256 hex digests of file bytes.

1. `freeze`: include `action`, `route`, `contract` (contract digest), `branch` (one of the suggested routes or any fresh nonempty name), and every specification field from `route-schema`. `domain_kind` is `pilot` or `family`; `dimension` is `4` or `8` as text; `geometry` is `trace` or `span`; `correction_kind` is `additional` or `signed`.
The freeze also pins `lift_operation` (the actual map from inputs), `lift_algorithm` (repository path to the trusted implementation), and `implementation_sha256`. The file exposes `lift(l,k)`, `reduce_once(lifted)`, `coordinates(reduced)`, and `witnesses(reduced)`. Only the lift receives the input pair. The runner calls the reduction once and passes separate copies of the same result to both readers. The lifted presentation includes an `occurrences` list of distinct IDs. The reduced presentation includes a `cells` object mapping each surviving ID to its source occurrence IDs. The coordinate reader returns the parameter pair; the witness reader returns two lists: surviving extra cell IDs and cancelled occurrence IDs. These are serialization requirements, not constraints on the internal geometry.

Run `python research/voevodsky/checkers/ramsey_lift_execution.py TRUSTED.py L K RUN.json` and repeat with `--verify` to compare the receipt byte-canonically. Inspect the candidate code first; the journal never evaluates code on its own. Reviewers must check intrinsic generation, including whether the candidate hides benchmark answers in its code or metadata. At `prediction`, submit the run JSON as evidence and its derived `predicted_order` as decimal text. Source accounting, common reduction digest, coordinate recovery, distinct cell identifiers, and baseline size undergo mechanical checks. A referee should replay the candidate and document that check. For the main (3,7) claim, provide two literal extra cells and zero cancelled occurrences. Signed extensions retain separate scoped verdicts.

2. `submit`: include `spec` (freeze digest), `stage`, `author`, `evidence` (repository path), `evidence_sha256`, and that stage's named proof fields. Refer to explicit arguments or witnesses in the evidence file. Pin the intrinsic correction at `prediction` before submitting `threshold` evidence.
3. `review`: include `spec`, `stage`, `submission` (submit digest), `reviewer`, `reason`, and `verdict` (`accept`, `revise`, or `refute`). A reviewer distinct from the submission author assesses the mathematics. `revise` permits a fresh submission at the same stage; `refute` ends that route. A changed specification needs a fresh route id. Replay validates sequencing, references and file integrity; it does not authenticate reviewer names or decide proof validity.
4. An accepted closure settles only its stated domain. Only a literal family with the (3,7) cell witness can enter root review. The operator first enters a separate decision in `contracts/ramsey-relational-lift-scope-grants.json`, pinning `spec`, `domain`, and `closure_review`. The route command cannot write this registry. This is a local operator policy file, not an authenticated signature. The family can then receive a separate `root_review` event containing `spec`, `scope` (exact domain), `closure_review` (final review digest), `reviewer`, `scope_acceptance` (authority and reason to accept this scope), and `reason`. `show` displays branch-specific progress. `frontier` distinguishes active-route decisions from work cards for new routes. The dashboard identifies each closed scope. Finite pilot closure stays separate. No code change is required for these operations. `frontier`, `check`, and `verify` display the derived route states. The older `record` command preserves informal attempt history only.

Run the lifecycle and regression tests with `python research/voevodsky/checkers/test_ramsey_relational_lift_net.py`. Keep the contract, reviewed inputs and journal together when archiving a revision.
