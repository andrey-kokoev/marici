# Prior clues after the source–action–observation counterexample

## Search disposition

The counterexample remains valid: a path from the A image to the B image cannot support the requested global discrete endpoint decoder, and equivariance into the fixed-point-free vertex permutation is also impossible.

Prior work supplies a more precise alternative than an unconditional existence conjecture: **retain transitions and fibre transport; characterize which observations descend, with explicit refusal when they do not.** Some of the necessary theorems already exist for this exact six-arrow source.

This packet records inspected notes and source code. Their old verification claims were not freshly rerun here. No net verdict, native rule, completed theorem or pin was changed.

## 1. Exact-source positive construction: geometric response states

Sources:

- `../nima/seed-geometric-response-state.md`
- `../nima/agda/SeedGeometricResponseInterpretation.agda` (implementation inspected)
- `../nima/geometric-fixture-representation.md`

The existing response state at vertex v is

    State(v) = (node A = node v).

An occurrence e acts by right concatenation with its actual realized edge. This is an equivalence between State(source e) and State(target e), not an identification of their discrete endpoint labels. Both forward and return seam discrepancies survive. In particular, the separately supplied BA occurrence is not identified with the geometric inverse of AB.

The prior construction also retains the raw directed word and compiles arbitrary supplied typed words using a one-seed unary transport discipline. It already proves agreement between the current compiled state and the path-effect interpreter. Reconstructing a reversible state from scratch would repeat completed work.

The observation interface is dependent. Given response types X(v), edge equivalences and an initial response, `SeedGeometricResponseInterpretation.Interpret` constructs a family over the free realization using univalence. Its readout transports the initial response along the current based path. Primitive, inverse, route and native-execution comparison squares are proved.

**Why this avoids our contradiction:** it does not define a global map from the realized graph into the fixed discrete vertex type. Its readings live in fibres, and edge traversal changes a reading by transport. Endpoint identity can remain in the discrete indexing of the operational state or in retained provenance, without becoming a global homotopy-invariant reader on the geometric support.

**Important limits:** the response types, edge interpretation and initial response are explicit inputs, not source-selected physical data. The native execution uses the explicitly declared `RetainedTransportResolution.Extension`, not silently the current net's original twelve-rule calculus. Geometric inverses are not newly authorized directed executions.

## 2. Descent is already a conditional theorem, not a universal promise

Sources:

- `../voevodsky/observer-relative-computation/set-valued-image-descent.md`
- `../voevodsky/observer-relative-computation/groupoid-descent-equivalence.md`
- `../voevodsky/observer-relative-computation/groupoid-witness-regression.md`

For R:S->Y and a set-valued observation o:S->O, the prior set-descent theorem gives the exact condition for a factor through the admissible image of R:

    R(s)=R(t)  implies  o(s)=o(t).

Necessity does not require a set target; sufficiency in that theorem does. No selection of an origin from a truncated fibre is used.

Our failed decoder is an immediate hostile instance: R is the vertex-to-realization map, o is the native vertex label, AB supplies a collision of R, and o separates it. The admissible factor type is empty. This diagnoses incompatibility rather than promising a replacement observation.

For groupoid-valued outputs, the later full-data theorem identifies witnessed image factors with coherent fibre data retaining links and triangle squares. It is not a theorem for arbitrary higher targets or a uniqueness theorem for all witnesses. A concrete regression has identical visible postprocessors but distinct coherent comparison data, distinguished by transport in a double cover.

**Clue for a successor contract:** make admissibility/descent certificates part of the proposed source–action–observation interface. A faithful representation of values alone need not preserve comparison-sensitive observations.

## 3. Dependent observations do not erase the anchor problem

Sources:

- `../voevodsky/observer-relative-computation/anchored-dependent-records.md`
- `../voevodsky/observer-relative-computation/coherent-anchor-change.md`

These packets retain a reply, an actual path from an anchor to that reply, and a value in the reply's fibre. Normalization is an equivalence relative to the anchor. Change of anchor respects transport and has checked identity/composition laws.

But a loop can flip the normalized Boolean. Forgetting the comparison path can leave the same visible reply/value pair with different anchored readings. No anchor-independent factor then recovers all those readings.

This is directly relevant to the earlier rebasing-loop calculation: a fixed-A path state must not be asserted to carry a strict source involution after rebasing without accounting for the AB;BA loop. A moving-anchor or two-endpoint path interface is a candidate to investigate, not an already proved assembly in this search.

**Do not replace the false global reader claim with the equally unsupported claim that every dependent reader descends after forgetting its frame.**

## 4. Operational quotients require the whole authorized context language

Sources:

- `../nima/seed-composition-port-quotient.md`
- `../nima/contextual-equivalence-needs-stabilized-congruence.md`
- `../nima/contextual-faithfulness-falsifier.md`
- `observation-kernel-equality-is-not-source-state-identity.md`

The exact-source port theorem proves a positive result for all nonempty typed directed paths: the source/final-arrival summary preserves binary composition and is exactly characterized by all typed prefix/suffix arrival observations. Source/target indices remain explicit; retained words remain outside the quotient. This does not license history-length or other queries to descend.

The general contextual notes sharpen the scope:

- present readout equality need not be a continuation congruence;
- a fixed finite horizon can miss delayed separation;
- finite-state partition refinement certifies all-context equivalence only after stabilization on a closed transition system;
- permanent aliasing can survive every authorized context;
- faithfulness on the contextual quotient is automatic by definition, not evidence of faithfulness on the original source.

The source-specific geometric-state packet already proves that its finer reversible response does not factor through the arrival quotient. These two results are compatible because the observation tasks differ. No new probe may be smuggled into the arrival-only language to claim that it was faithful all along.

## 5. Keep directed execution distinct from geometric comparison

Source: `../voevodsky/observer-relative-computation/execution-observation-bridge.md`.

An actual directed machine run maps into a static HIT support whose edges are comparison paths. Those paths can be reversed; a halted machine has no reverse run. The prior checked converse obstruction rules out recovering every directed execution from every support path.

This identifies another hidden premise in a universal correspondence: interpreting operations as paths may add inverses not licensed by the execution grammar. A realization must retain directed admissibility separately rather than calling every geometric inverse executable.

## 6. Physical clue: future probes, with an explicit authority boundary

Source: `../nima/physical-coyoneda-future-probe-conjecture.md`.

The inspected bounded instrument model has equal one-use probabilities for different successor capability rays; controlled X/Y/Z future analyzers distinguish and reconstruct those rays. It illustrates why a present observation is not the full operational interface.

The packet explicitly does not derive those analyzers from the Carrier. Restricted, record-valued probe families are not the unrestricted Hom-functor, so Yoneda alone supplies no physical separation theorem. This is a model-based clue, not new experimental validation or a source-selected detector construction.

The matrix-fixture representation supplies a similar warning on the mathematical side: it reproduces all 137 target values conditionally, but imports the fixture coefficients, labels and weights. Its reader can forget geometric states. Reproduction of fitted values is not physical source determination.

## Proposed bounded continuation

Do not restate the refuted universal existence assertion. Instead investigate a **transport-compatible partial correspondence** with separate obligations:

1. Bind the existing exact-source path-state/retained-word construction to an explicitly chosen native execution signature. Resolve the extension-versus-original-calculus boundary rather than treating the signatures as interchangeable.
2. Specify the observation language and prove descent or exhibit a separating collision. Reuse the already completed arrival quotient and its known failure for the finer reversible state; do not repeat them as new results.
3. Preserve frame/anchor comparisons and distinguish directed operations from geometric inverses. Prove the requested action and product laws at those actual interfaces.
4. For a physical receiver, independently authorize its probes, demonstrate joint separation at the claimed scope, and supply calibration and empirical tests separately.

The concrete missing bridge is an assembly of these existing typed interfaces—not another circle constructor and not a proof that every observation task is realizable. Neither this search nor the prior conditional theorems establish the full successor correspondence.

## Implemented successor

[Transport-observation partial correspondence](transport-observation-partial-correspondence-v1.md) now binds actual unary-extension executions to certified observation descent and collision refusal, including an all-word BA-parity interpreter. The extension signature is explicit; original-rule admission, action/product assembly and physical validation remain separate.
