# Review: does the native-query physical-realization net reflect current knowledge?

Verdict: no. Revision 5 is a valid pinned historical snapshot, but its frontier and some scope statements lag completed work. This review does not mutate the pinned net or its current pointers. The quartic experiment is excluded from this review and from the recommended next work.

## Fresh verification performed

- `python research/strominger/checkers/check_native_query_physical_realization_net_v5.py`: pass; all 57 file pins match, all 17 corruption controls rejected. Recorded frontier remains mathematical-realization-moduli and freeze-physical-model.
- `python research/strominger/checkers/check_mathematical_realization_moduli.py`: pass. Fresh Agda positive closure with ignored interfaces exits 0; intended negative reset control exits 42. All-word native binding passes; source snapshot remains stable across the run. Exact checks cover 132 ordered separating pairs and 9,216 coefficientwise generator equations.
- `python research/strominger/checkers/check_endpoint_continuation_cells.py`: pass, 256 alphabets and 70,656 paired-state searches.
- `python research/strominger/checkers/check_port_access_sufficiency.py`: pass for all four source inputs and all twelve routing permutations.

The net validator's pass is snapshot integrity, not a search for later evidence. Its expected frontier is explicitly hard-coded to the v5 frontier; it cannot discover the later completion artifact.

## Findings

### 1. Output A is complete at its stated conditional scope, not open

Net node `mathematical-realization-moduli` says the assembled classification and exact native-fragment comparison remain unproved. The later `mathematical-realization-moduli-v1.md` and freshly rerun receipt supply:

- H=cI, c>0, and normalized H=I/3 for each supplied -1<eta<1;
- necessity and sufficiency for all eight generators and their finite words;
- uniqueness under the frozen labelled factor-preserving equivalence;
- actual finite/native all-word semantic binding.

Evidence split must remain explicit: general real pairing classification is a written proof with exact coefficient/separation support; Agda checks the finite/native all-word binding, not real inner-product analysis.

Recommended successor disposition: resolve this node as constructed, attach the completed artifact and receipt, preserve eta as supplied and physical validation as false.

### 2. Several inherited scope statements lag the same completion

`freeze-source-fragment` still says the finite embedding and all-word comparison are outstanding. `source-authorized-physical-recording` still recommends assembling Output A. Those are no longer current instructions. Preserve their historical context but update successor scopes/actions.

The frozen source-fragment JSON also contains an old proof-boundary statement about obligations not newly proved there. Do not silently edit that pinned source artifact merely to make prose current: a successor can explicitly cite its later discharge and retain the original specification.

### 3. Current-pointer discovery is inconsistent

- `contracts/native-query-physical-realization-net.current.json` points to revision 1.
- `contracts/native-query-physical-realization-net.v5.current.json` points to revision 5.

A reader using the generic pointer can receive an even older frontier. A reviewed successor needs an explicit canonical discovery policy and a current pointer directed at that successor, while preserving version-specific historical pointers and pins.

### 4. New task-restriction results are absent

The alphabet atlas and port-access quotient are later mathematical results. They add useful candidate-model information:

- full-language distinguishability does not imply all eight controls are necessary for separation;
- endpoint-restricted task quotients depend on which operations remain accessible;
- ideal routing with a fixed source induces the vertex-image quotient;
- output-side operations preserve it, while moving input access can break it.

These are candidate-model/task-restriction results, not completion of the original all-generator compiler. Register them as a scoped side branch or candidate-audit input. Do not merge their smaller task with the frozen full task.

### 5. The physical blockers remain correctly open

The inspected artifacts do not supply a frozen accepted physical model, a full physical protocol compiler, complete comparison witness types, the four face witnesses, or tetrahedral coherence. The scoped six-pulse oscillator linear obstruction remains unaffected. A four-port ideal routing calculation is not an operation-preserving implementation of the entire carrier/pointer task.

The KrakenSDR adaptation is an inventory/capability plan. It does not close `freeze-physical-model` or establish apparatus readiness.

## Corrected automatic frontier

With the existing dependency graph unchanged and only the verified Output-A completion registered, the actionable frontier becomes:

    [freeze-physical-model]

`freeze-comparison-witness-types` remains blocked by freeze-physical-model. The compiler and face/coherence nodes remain blocked. Opening a separate abstract witness-type task would require an explicit graph redesign rather than silently bypassing this dependency.

The next scientific action is therefore to disposition one concrete physical model, informed by the oscillator obstruction and the new port-access analysis. The next bookkeeping action is a reviewed v6 snapshot with the completed Output-A evidence, corrected scopes, scoped side-branch evidence, updated validator/pins and unambiguous current discovery.

No automatic claim of a physical realization, spatial coherence cell, or new experiment priority follows from this correction.
