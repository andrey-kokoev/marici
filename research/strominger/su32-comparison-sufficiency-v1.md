# Minimal sufficient account of layer-4 comparison

## Result

The supported account is **reference-checked reconciliation of independent records**, with construction provenance retained separately. It makes previously separate views jointly available at a common reference; it does not currently specify a transformation of their contents.

There are three different tasks, not one interchangeable notion of “same state”:

1. Recover the contents and their directional labels.
2. Recover their native occurrence/reference attachment.
3. Recover the actual construction derivation.

Equality for task 1 does not imply equality for tasks 2 or 3. Conversely, a distinction needed for provenance is not automatically a dynamical effect.

## Requirements and provenance

The requirements come from `sulfur-32-reversible-channel-specification.md`: four independent directional records; the four cross-P/E views; actual shared-reference incidences; no invented content transformation; retention of identities, paths and histories. The specification does not define an additional numerical comparison result, scattering law, or phase action.

The implemented `su32-layer4-comparison.mjs` explicitly calls itself a **set-valued candidate**. Its validator is evidence about that implementation, not an independent source of physical requirements. In particular, rejection of a history-free JSON object would not prove that history is necessary for recovering contents.

## Adequacy: what the join accomplishes

At a fixed occurrence and sign binding, a channel contains `(P_s,E_t)`. A shared-E comparison admits

```
(P+, E_t) and (P-, E_t) -> (P+, P-, E_t)
```

only when the shared E record agrees in reference identity and payload. The shared-P case is symmetric. Reconciling the two E-reference results, or the two P-reference results, recovers all four records; overlapping records must again agree.

Thus the operation supplies compatibility checking and joint availability. It neither identifies the two independent P records nor calculates a relation such as their difference or ordering. If “comparison” is intended to produce such a further result, that requirement is not yet specified.

For arbitrary valid JSON payloads, the construction consists only of checked copying and union. The general sufficiency argument is structural: each required projection selects entries from the common registry; each join recovers their union after agreement on intersections. The finite replay tests this argument's implementation, rather than proving arbitrary-payload behavior by exhaustive testing.

## Necessity and redundancy

| Information | Finding |
|---|---|
| Each of the four independent records | Necessary for exact recovery. Deleting any one identifies two Boolean inputs whose required outputs differ. |
| Directional labels | Must remain recoverable. Swapping P+ and P− preserves the multiset of contents but changes channel assignments. Labels may be encoded implicitly in a known layout; their literal strings are not sacred. |
| Occurrence/chart and sign binding | Necessary for native attachment, though not for returning a bare four-value registry. Equal values can refer to different charged cells or occurrences. |
| Repeated `referenceCell` fields | Redundant when the complete layout and binding are already available; the encoder reconstructs them. Their semantic information is not dispensable. |
| Shared-record consistency | Necessary when operands arrive independently: individually valid operands can disagree on their shared record. A single authoritative registry enforces consistency by construction. |
| Full repeated child trees | Not necessary storage for the two canonical constructor outputs. Anchor + registry + route reconstructs either exact tree. This is not a compression theorem for arbitrary histories. |
| Which canonical route was taken | Not needed for content recovery. Needed to distinguish those two derivations when provenance is part of the task, as the specification requires. No downstream dynamical consequence is established. |

These are task-relative necessity claims, not a proof of a globally smallest bit encoding. For four independent Boolean records, exact recovery already requires distinguishing all 16 assignments; arbitrary payloads have no fixed four-bit bound.

## Fresh checks

`checkers/check_su32_comparison_sufficiency.mjs` passed:

- 36 charts × 4 bindings × 16 Boolean registries = **2,304 cases**;
- **4,608 exact canonical-history reconstructions** from compact state;
- **9,216 record-deletion counterexample instances**;
- **576 incompatible shared-record pairs rejected**;
- **144 equal-content/different-reference binding examples**;
- directional-label and occurrence-erasure counterexamples.

The examples and source hashes are in `results/su32-comparison-sufficiency-v1/verification.json`. Native operation implementations were not modified. The checker constructs no new wiring and imposes no local-to-global extension rule: charts are tested separately, not asserted to define a globally coherent signed assignment.

## Residual and conclusion

No unmet content-retention or local shared-reference requirement was found in this task. That supports the lossless join as the current information-level account, not as derived particle dynamics.

Still outside its scope:

- a globally compatible carrier/reference assignment and cross-chart transport;
- the six-output signed routing choice;
- the proposed double-twist pair/tube identification;
- a specified further comparison result or downstream dynamical law.

The next useful requirement is whichever of these the native construction actually demands—not an invented hidden-effect detector. In particular, provenance retention already has a clear purpose without treating it as an extra physical state transformation.

Replay:

```sh
node research/strominger/checkers/check_su32_comparison_sufficiency.mjs
node research/strominger/checkers/check_su32_layer4_comparison.mjs
```
