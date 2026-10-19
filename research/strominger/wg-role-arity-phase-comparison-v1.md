# WG role, packet boundary, and phase are different indices

## Scoped result

Comparing the actual Composer role trace, native recursive table signature, arity square, and Layer3 transport shows that the four role names cannot simply be substituted for the four arity vertices. The interfaces index different data. This is a source-interface comparison and bounded schedule check, not yet an adapter realizing the operator's proposed primitive packet.

The useful working structure is a retained WG package with separately declared role views, active input/output boundaries, execution phase and history. This does not claim every combination of those indices is inhabited or physically realized.

## 1. Role versus boundary

The prior role trace fixes G:Layer1 and exposes its generate, next and edge interfaces. These are available in both request and answered phases of Composer.WG.

The arity skeleton instead classifies boundaries:

| Boundary | Interpretation in the arity source | Role restriction actually proved |
|---|---|---|
| (1,1) | unary source/state | none identifying it exclusively as object or identity |
| (1,*) | expansion/coaction | none identifying it exclusively as generator |
| (*,1) | synthesis/trace | none identifying it exclusively as operator |
| (*,*) | relation/channel interaction | none identifying it exclusively as transport |

A unary operation is already a generator/operator in the checked WG example. A many-input operation can itself be a retained object. The word transport requires endpoints and witnesses, not a particular number of boundary ports.

There is therefore no source-supported four-role/four-corner bijection. This does not disprove that a particular phase-specific interpretation can be supplied.

## 2. Arity needs a selected level of presentation

`IndexedConstructorTables.table-node` has a declaration h, active port domain Arity(h), typed child nodes, and one resulting Node(Result(h)). NativeTableRules independently specifies

    Arity : Rule -> Type
    input : (r:Rule) -> Arity(r) -> Package
    output : Rule -> Package.

For example, E and Pi have premise index I, comparison and composition have two premise ports, and identity has one. Every rule nevertheless returns ONE complete package. That package can contain a whole family of outputs or comparisons.

Consequently, counting outer return packages makes all these rules appear to have one output; inspecting their internal retained families can expose many positions. Neither choice is intrinsically wrong, but an arity assignment must state which boundary it measures.

The source also allows zero and infinite premise arities. The binary unary/many square is a restricted/coarse classification, not a proved exhaustive classification of all native rules. Empty domains and retained declarations may not be discarded to force every rule into a nonempty four-corner scheme.

This is the same kind of level distinction as terminal137 comparison leaves versus primitive factors. It is not an assertion that their numerical counts coincide.

## 3. A generated edge versus actual payload transport

This distinction is already handled by `TypedGeneratorTransport.Layer3`:

    Payload : State -> Type
    move : Witness(s,t) -> Payload(s) -> Payload(t).

The movement action is SUPPLIED over the fixed lower WG/history layers. The source constructs execution over retained histories, proves execute-compose, and retains history, input, output and agreement. Its Stack3 recovers the original lower WG/history pair.

Thus the richer transport role does not require replacing the underlying WG, but it does require the declared payload/action context. An arbitrary Witness is not automatically an equality path with unrestricted dependent transport. The path specialization supplies the latter where its hypotheses hold.

This is existing performed work, not a new requirement to invent an executor. The proposed primitive packet must identify its payload family and action with one such interface.

## 4. The operator's phase order is not the source Gray perimeter

The conversation's earlier stage order was

    (1,1) -> (1,*) -> (*,1) -> (*,*),

followed by realization as a new identity. In bits this is

    00 -> 01 -> 10 -> 11 -> [00 of the next cycle].

The prior arity-square Gray perimeter is

    00 -> 01 -> 11 -> 10 -> 00.

Both visit the same four boundary signatures. They are different routes. The operator-order boundary transitions have bit distances1,2,1,2, versus1,1,1,1 for the Gray perimeter. The transition from expansion to synthesis crosses a diagonal; the closing signature transition also changes both bits. A square symmetry preserves adjacency and cannot turn these into the same elementary-edge schedule.

This is NOT a contradiction or proof that the operator's phase order is invalid. Diagonal composites/comparisons are already part of the retained geometry. The next adapter must identify those composites and their witnesses, rather than reorder the intended phases to match the drawing. Returning to boundary signature00 does not prove return to the same state; the terminal identity can be new.

The four-role names do not settle which diagonal realization is intended. Likewise the two cube conventions (operation-order comparison versus polarity) must remain distinct until explicitly related.

## 5. Minimal adapter contract for the intended packet

The missing comparison can now be stated without choosing an arbitrary new model:

1. Fix a complete packet P and a declared phase/context index.
2. Name its active input/output port families and selected values. Keep the underlying retained package and inactive provenance separately recoverable.
3. Assign each intended stage its boundary signature at that chosen level; handle zero/many explicitly.
4. Identify the actual native rule or retained sequence implementing the stage. For the two diagonal signature changes, supply the relevant composite and comparison witness rather than a mere relabelling.
5. Specify Payload and move if transport means execution on a dependent payload, using the existing Layer3 laws.
6. Show that the terminal package is available as a next input, without identifying its new state with the previous state or erasing its construction.

The id/Q2/Q3/Q4 labels additionally need an independently specified degree/formation rule. Arity alone supplies no polynomial grading: even a unary operation need not be identity or linear.

## Net consequence

The role/arity/phase interface audit is complete at its stated scope. The broad phase-relative-role conjecture and primitive-packet-Type binding remain open. Their next task is an actual native port-and-payload adapter for the operator's phase order, not another generic four-role example, a fabricated polynomial assignment, or a new transport executor.

## Verification and evidence

Executed `python research/strominger/checkers/check_wg_role_arity_schedule.py`. It reads the existing checker's literal arity vertices and verifies five finite incidence claims, rejecting two schedule substitutions. Receipt: `research/strominger/results/wg-role-arity-schedule-v1.json`.

Sources inspected:

- `research/nima/binary-arity-square-is-the-duoidal-skeleton.md`;
- `research/nima/native-table-equivalence.md`;
- `research/nima/agda/NativeTableRules.agda` (Arity/input/output declarations);
- `research/nima/agda/IndexedConstructorTables.agda` (header/port/node declarations);
- `research/nima/whole-package-generators.md`;
- `research/nima/typed-generator-layer-3.md`;
- `research/nima/agda/TypedGeneratorTransport.agda` (Layer3/Stack3).

The source notes report their formal verification; those larger source suites were not freshly rerun in this comparison. The preceding role trace's fresh Composer closure remains distinct evidence. The finite incidence checker is not a proof of the proposed primitive-packet adapter.
