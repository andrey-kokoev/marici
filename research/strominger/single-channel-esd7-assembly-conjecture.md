# Single-channel assembly of esd7

Status: operator-proposed conjecture; no assembly operator or reconstruction theorem is established yet.

## Statement

If the retained `1 + 4 x 28 + 1` construction is serialized into one ordered channel, there exists an operator that assembles the full coherence presentation of `esd_7(Delta^3)` from that channel.

Write S for serialization and A for assembly. For the proposed retained construction W,

    A(S(W)) ~= esd_7(Delta^3),

where the comparison preserves the intended markings, interfaces and coherence data, not merely the geometric shape or cell counts.

The two additional `1` records are retained as the opening and closing parts of the proposed construction. Their precise types and roles remain to be specified; they are not silently identified with particular vertices, physical particles or extra global time steps.

## Meaning of the single channel

The channel is one ordered stream carrying the construction's retained information. It need not be one scalar amplitude. Branch identity, occurrence order, contextual references, frame/orientation information and shared-interface witnesses may be encoded in its records rather than supplied as four independent channels.

The expression has114 record occurrences under the proposed counting convention:112 branch-step occurrences plus the two additional records. This is not a claim of114 esd7 vertices or cells, or114 global evolution steps. An assembly operation may introduce or identify multiple cells from one record.

## What assembly must accomplish

The operator should reconstruct the four-branch organization and their shared whole, including the appropriate cell incidences and face/tetrahedral coherence witnesses. Shared data must be identified consistently without collapsing distinct retained histories.

The channel should come from the retained transport construction. Simply embedding the already completed esd7 census in a record and reading it back would demonstrate generic serialization, not the proposed assembly law. The existing census is an independent verification target, not an answer to insert into the operator.

## First constructive test

Specify the record types and serialization for the proposed construction, then implement assembly using explicit transport/gluing rules. Compare its output with the actual esd7 incidence and coherence registry. Record what information is derived, retained by reference, or supplied as an additional rule.

A discriminating failure would be two allowed retained constructions with indistinguishable channel encodings but incompatible required assemblies. Failure of one chosen decoder alone would reject that decoder, not the existence conjecture.

A stronger version would assemble incrementally as records arrive, with coherent intermediate interfaces. Incremental operation is an extension to test, not assumed by the basic statement.

## Net registration and stronger synthesis

Registered as `single-channel-esd7-assembly` in revision6 of the [maintained conjecture net](contracts/persistent-seam-pe-conjecture-net.v1.json), with open status and no formal outcome.

A separate node, `assembler-as-global-evolution`, records the assistant-proposed stronger synthesis: the incremental assembler's intermediate retained states also realize the global evolution, with native transport-compatible readouts. This is not silently included in the operator's basic assembly-existence conjecture.

Revision6 recommended `channel-contract-and-first-assembly-step`. That bounded task is now [implemented](native-retained-channel-v1.md):23 records recover the native fixture and its18 interface equations. Revision7 records its conditional completion and recommends `esd7-channel-attachment-construction` next. Full114-record/esd7 reconstruction and the evolution interpretation remain separate, open gates. Revision8 additionally records [full geometric reconstruction through345 source-rule records](esd7-attachment-channel-v1.md). The114-record convention, analytical fillers and full-complex field transport remain unbound, so the same attachment task stays open with a narrower residual. Revision9 binds the [analytical-prototype registry](esd7-analytical-binding-v1.md) to actual generated cells through an explicit sorting bridge. Its294 H123/H234 and294 same-role shared-face comparisons remain open; prototype labels do not supply analytical maps. This is a work-plan recommendation, not evidence that either full conjecture is true.

## Relation to prior work

- [Global28-stage P/E conjecture](global-28-stage-pe-fibration-conjecture.md): the four branches are views of one retained whole;112 branch occurrences are not112 global steps.
- [Native joint-field assembly sewing](joint-field-assembly-sewing-v1.md): a bounded example of consistent native interface gluing while retaining history-dependent frames.
- [Marked table fibration](../nima/table-fibration.md) and [arrow/history windows](../nima/arrow-history-window.md): prior lossless presentation and provenance machinery, not yet this esd7 assembler.
- [Recovered esd7 layout](esd7-coherence-layout-recovery.md): the existing target registry and its verification scopes.
