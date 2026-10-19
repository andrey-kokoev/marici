# Presentation naturality: two admitted finite comparisons

## Scope

Fresh work-net read: `typed-event-control-interface` remains the official frontier. Earlier Sontag packets are owner-local evidence, not admitted net resolutions. This packet constructs comparison squares for one existing WG presentation change and one energy chart; it does not bypass the unresolved assembly prerequisites or infer arbitrary WG transport.

## WG nested/flattened comparison

Fresh source inspection: `research/nima/agda/ComposableWitnessSpecialization.agda`, lines 18–111. Fix `F:Refinement L` and `G:Refinement(compile F)`; these choices and their actual sources remain fixed. Write N=compile G and K=compile(compose F G).

`Composite.flatten` maps `((s,p),q)` to `(s,p,q)`; `unflatten` is its inverse. The maps on actual edge witnesses are `((r,e),f) ↔ (r,e,f)`. They preserve the dependent payload f, not merely the endpoints. `Composite.correct` supplies state and full-step isomorphisms, endpoint compatibility and generated-step compatibility. Its fields prove the squares

`flatten(next_N x) = next_K(flatten x)`

`flatten-edge(edge_N x) = edge_K(flatten x)`

with the indicated endpoint transport. Induction on a finite generated history gives replay compatibility and the mapped final state. Likewise, a full-step history transports by the step isomorphism and endpoint path; this is not permission to invent a generator for arbitrary witnessed edges.

Choose the flattened-state observation as identity, and the nested observation as flatten. Then the observation square commutes. Alternatively any explicitly supplied observer o on K pulls back to `o∘flatten` on N. This includes observers of retained proof payloads when they are supplied at valid dependent types. `recover-first-source` and `recover-second-source` preserve the fixed input sources. No resource-cost model is claimed; only admission and witness obligations are transported.

A next refinement H over N is transported by `Composite.rebase`. Its Admit is pulled back through unflatten; its Extra uses unflatten-edge, preserving the witness indices. Thus the enabled-admission square commutes by construction. This handles the proof-dependent continuation hostile for this PARTICULAR presentation isomorphism. Source identity/task success is pulled back along the same map, not reconstructed from terminal values.

Policies on matching observations transport only when their events/choices have the supplied step/refinement transport. The base generated WG has one declared generated next step, not an invented choice of physical controls. Arbitrary WG-equivalence transport remains outside scope. Inverse composition is identity on the actual paired data; repeated history transport respects concatenation by induction. Source-level Agda certificates were inspected, not freshly compiled this turn.

## Energy chart

Let U={(a,b):a,b≥0}, V={(H,A):0≤A≤H}. Define

`φ(a,b)=(a+b,a)` and `ψ(H,A)=(A,H−A)`.

These are inverse charts retaining provenance separately. They are derived from the source's energy observation, not a new actuator. Transfer the SAME gain q∈[0,1] to

`Tq(H,A)=(q⁴H+(q²−q⁴)A, q²A)`.

Then `φ(gain_q(a,b))=Tq(φ(a,b))`; readout is H in V and a+b in U. Composition satisfies `Tr∘Tq=T(rq)` because the original component law does and φ is invertible. Resource effect, defined only as visible model energy change, is preserved by the readout square. Provenance histories are retained rather than identified by chart equality.

The total-only first decision is unchanged under φ. After the recorded probe, the exact readout transcript is identical; reconstruct `(a,b)` through ψ and use the existing `target_gain` on the CURRENT components. This is policy conjugation, not replacement of the source controller. Domain inequalities and admissible q are preserved.

A rival chart keeping only H is not invertible and cannot define a gain update for all compatible states: `(8,0)` and `(0,8)` map to the same H but give different next H for q=1/2. Equal terminal observations alone therefore do not suffice for policy/event transport.

## Verification and disposition

Checker: `research/sontag/checkers/presentation_naturality_v1.py`; result: `research/sontag/results/presentation-naturality-v1.json`.

Symbolic energy inverse, transition, observation and composition identities and source-controller policy checks are executed. WG paired-data roundtrips are only an illustration; dependent correctness rests on the inspected Agda `Realization` and `rebase` definitions, not the Python tuples. No fresh Agda receipt or universal WG-equivalence proof is asserted.

Constructed at these two declared comparison scopes: state/event/observer squares and finite-history composition compatibility. This also supplies a specific nontrivial WG transport candidate for the history-congruence gate. Source relation-module attachment comparisons are separate: no claim identifies this nested/flattened refinement with the marked path-algebra derived receiver. Owner review is required before resolving net nodes or assembling mathematical realization.
