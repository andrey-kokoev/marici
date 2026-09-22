# Relational membership does not supply a coherent live witness

## Result

The actual compressed local views now have a bounded admission checker and a separately witnessed update kernel. The experiment exposes a sharper failure than incompatible local snapshots:

> Every projected step can have a source witness while their composition has no coherent source execution.

Of 115,412 tuples of locally valid view values, only 61 have a common source realization. Of those, 52 determine one refined behavioral state and nine permit two. A single source-origin bit distinguishes the alternatives. It is necessary for faithful execution at the double fibers and sufficient for this frozen protocol.

The finite runtime packet carries the admitted tuple relation, one-bit lifted tuples and behavioral transitions. It contains no original concrete-state identifiers or source-history words. The relation and transition tables are explicitly counted as retained verification information; the one-bit claim is not a claim of a one-bit total verifier.

## 1. Frozen membership and lift contracts

The views are the actual source-only, acquisition-only and recipient-only current-language continuation quotients on the shared admitted carrier. Their local carrier sizes are 43, 44 and 61.

The frozen extension language includes the two origin audits. The runtime budget is structural:

- 61 admitted local-view tuple rows;
- no additional per-query membership witness bits;
- at most one live selector bit;
- 70 lifted behavioral rows;
- 1,260 transition cells for the eighteen labels.

Membership means that some common same-state realization exists. It does not assert that a chosen realization is the actual execution. The selector bit means `origin_is_01`, initialized truthfully from the known source prefix and retained faithfully. It is not an arbitrary identifier ranging over all source states.

Compilation uses the verified source-bound carrier. Subsequent runtime admission and updates consult only the compiled relation and transition packet, not a hidden record of the concrete source state. This is a closed-family compilation, not a uniform bound for arbitrary future protocols.

## 2. Complete admission check

All 43*44*61=115,412 local tuples are checked against the source fibers. The packet admits exactly 61 and rejects 115,351. The source/task/run context must also match.

This is relational information beyond common-summary equality. The finite admitted-tuple table is the extra joint compatibility information made available to the verifier. Zero attached membership-witness bits do not mean joint admission was recovered from independent local summaries alone.

For a lifted tuple, admission additionally checks whether its origin bit has a source realization in that fiber. Both bits are admitted at each of the nine double fibers. Consequently successful existential admission cannot authenticate which bit belongs to the actual run.

## 3. A concrete false projected path

Take an ambiguous tuple with no record distinguishing its two origins. In the projected relation:

    audit-origin(0), accepted

has a compatible source realization with origin zero. Likewise,

    audit-origin(1), accepted

has a compatible source realization with origin one. Each is a self-loop on the same compressed tuple.

Their projected relations therefore admit the two-step path in which both audits are accepted. There are nine such false diagonal paths.

But the source origin is invariant. No actual source state admits both accepted audits in succession. The concrete accepted composition is empty.

The error is witness switching: the first step chooses one realization and the second silently chooses another. Symbolically, the existence of a witness separately for each obligation is weaker than the existence of one coherent witness for their joint execution.

## 4. Relation projection preserves transpose but can lose composition

Let p forget the origin distinction, and write p_* for direct image of a relation. On the actual carrier:

    p_*(R^op) = p_*(R)^op,

but in general only

    p_*(G composed with F) subseteq p_*(G) composed with p_*(F).

There are 36 accepted/rejected relation strata: two for each of eighteen labels. Exhausting all 1,296 ordered stratum pairs finds **12 strict composition failures** after existential projection.

This does not contradict Voevodsky's coherent two-direction transport. Those decomposition comparisons are bijective source-coordinate changes and preserve the shared middle state. The present map is information-losing. Its projected composition joins steps at an equal compressed tuple, which need not mean an equal source witness.

## 5. The bounded live repair

Retain the same origin bit across updates. A lifted transition takes

    (local-view tuple, origin bit)

and returns admission/rejection together with the next tuple and unchanged bit. Every compiled entry is checked against the owning transition system. All 1,260 runtime cases agree.

After accepting audit-origin(0), the origin remains zero; audit-origin(1) is therefore rejected. A proposed transition that silently changes the bit is rejected by the update checker even if both endpoint lifted tuples independently pass existential admission.

Known initialization and these one-step checks establish preservation for arbitrary finite executions. All 1,296 stratum-pair compositions and all 36 transpose identities commute with the witnessed encoding.

The nine double fibers contain behaviorally distinguishable refined states. Thus any faithful deterministic representation must supply at least a binary distinction there. The one-bit witness meets that lower bound for this frozen family.

Views plus the bit determine the 70-state minimal behavior. They necessarily do: preserving all eighteen labels cannot identify two states already separated by a declared continuation. They do not reconstruct the 638 concrete histories, nor is avoiding determination of the minimal behavioral state a coherent additional compression demand.

## 6. Backward compatibility still is not inverse execution

Some witnessed opposite relations still have two predecessors. For example, delivery can reach an already-received state either from a pending first delivery or through an idempotent repeat. The origin bit does not recover which concrete past occurred.

The packet preserves the whole predecessor relation. It never selects a backward branch and does not authorize reverse execution. Its witness repairs the specific behavioral ambiguity lost by the local-view projection, not every information loss in forward dynamics.

If the actual selector is unknown, an observer may instead retain and update a set of possible lifted states. It must not reset that set to the entire compatible fiber after every step; that is exactly how the false audit sequence arises. No such knowledge-state implementation or new storage bound is claimed by this test.

## 7. What remains assumed

A fabricated selector can pass existential membership if it describes another possible state. Correct live selection therefore still requires truthful known initialization and faithful retention. The packet does not establish authenticated provenance, journal completeness or crash recovery.

The existing atomic, source-authorized operation contract remains in force. No delayed-network implementation or physical acquisition guarantee is inferred. Nor is an unrelated analytical calibration family silently coupled to these source paths.

## Verification

    python research/nima/checkers/check_relational_membership_and_live_witness.py
    python research/nima/checkers/verify_relational_membership_live_witness.py

The producer freshly replays the causal-interface verifier. The independent checker reconstructs source fibers, exhausts admission completeness and rejection, validates every compiled transition, verifies the fiber cardinality lower bound, and independently performs relation composition and transpose. Both pass.

Artifacts:

- `research/nima/results/relational-membership-live-witness-contract.json`
- `research/nima/results/relational-live-witness-runtime.json`
- `research/nima/results/relational-membership-live-witness.json`
- `research/nima/results/relational-membership-live-witness-verification.json`

The structural advance is the separation of three obligations: same-state realizability of local views, coherent witness preservation across a path, and truthful selection of the actual execution. None is supplied merely by the others.
