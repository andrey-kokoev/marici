# Full-path response bound to record endpoints; T9 selection witness

## Fresh result

The full geometric response representation now binds to the EXISTING flat record-port attachment, not just to its decoded matrix values. All137 labelled leaf records and all977 admitted common-target compositions have exact operation squares. Both existing two-round promotion policies retain these decorated inputs and the original J4.

This resolves a conditional record-endpoint binding: record ports, labels, member weights and flat reference attachments are supplied inputs. It does not derive those inputs from bare seed vertices or select intended T9.

## The correct source interface

Each reconstructed word is a based geometric A-to-A loop. The fixture has multiple distinct source and target record ports. A vertex-only functor cannot send the single vertex A to all those ports. Thus a literal bare-seed endpoint identification using these representatives is impossible.

Instead use the explicit source packet

    (label, record-source, record-target, geometric-word, mass).

The packet preserves all137 labels, including distinct labels with identical geometric representatives. Its port decorations are input data, not consequences of the word. This is the precise additional structure required by the binding; it must not be hidden by calling every loop a record arrow.

## Typed response map

Reuse the frames P_v, physical reference d=2I, and the existing flat reference attachments. The full-path representation gives rho(word). Bind the packet to

    actual : V_s -> V_t = P_t rho(word) P_s^-1,
    reference : V_s -> V_t = P_t P_s^-1,
    return : V_t -> V_s = P_s P_t^-1.

The original decoder d P_t^-1 actual P_s recovers the unchanged fixture value. Checks cover both the existing frames and their existing passive changes.

For a:s_a->t and b:s_b->t, the actual reference-return chain is

    s_a --a--> t --return_b--> s_b --b--> t.

The resulting map is

    P_t rho(word_b) rho(word_a) P_s_a^-1,

which is exactly the attachment of chronological geometric concatenation word_a followed by word_b, retaining a's source and their shared target. Its decoded value is C_b r C_a. All977 supported ordered leaf pairs are checked against both formulas.

No products between different record target ports are silently admitted. A response value alone cannot provide their missing connector.

## T9 now tested with the bound source packets

Both existing candidates use the original `incoming_promotion`, twice, unchanged:

| Contract | First families | Final families | Supported final ordered leaf pairs |
|---|---:|---:|---:|
| inherited target keys |32|32|977|
| common next target |32|1|18769|

For each candidate the checker verifies exact recovery of every original label, endpoint and response word, total original mass137, and the unchanged member-weighted J4. Therefore the new full-path and endpoint binding does NOT remove the previous constructor ambiguity.

A concrete selection witness is retained in the result JSON: two leaf labels with different original target ports. Their connection is excluded by inherited-key promotion and admitted by common-target promotion. This difference is wiring, not a change of coordinates or scalar normalization.

## What is required to name the intended T9

The current declarations do not state which of these incompatible next-port relations is intended. To choose between the existing candidates, the additional operational contract must say whether unlike original target fibres may share a next comparison port:

- If distinct target fibres must remain distinct next endpoint keys, inherited-key promotion satisfies that requirement and common-target promotion does not.
- If all incoming families must share one next comparison port, common-target promotion satisfies that requirement and inherited-key promotion does not.

These are conditional selection rules, NOT newly authorized requirements. Matching J4, reconstructing history, preserving primitive response or imposing flat coordinate transport selects neither.

The source audit also freshly read `native-promotion-constructor-trace.md`: the alternative actual `Feedback.run` constructor generates comparisons of outer routes, not incoming-family means. That note explicitly leaves its native table label/from/to interpretation and intended-T9 identification unbound. This result does not relabel one of the matrix promotions as `Feedback.run`.

Consequently the requested objective is not marked complete. There is executable continuation: test how much the existing response task distinguishes these endpoint policies, and inspect whether an existing source-authorized successor/table contract imposes one of the required next-port relations. No physical constructor is selected by assertion.

## Verification

    uv run research/nima/checkers/check_geometric_record_endpoint_binding.py

3495 exact checks pass. Dependencies freshly rerun the full-path representation, its native proof-receipt/hash validation, the original matrix rung chain and the flat attachment audit including nonflat holonomy controls. No new Agda module was added or fresh Agda closure claimed in this step.

Artifacts:

- `checkers/check_geometric_record_endpoint_binding.py`
- `results/geometric-record-endpoint-binding.json`

References freshly inspected:

- `rung-descent-endpoint-binding.md`
- `checkers/check_rung_transport_diagram.py`
- `flat-reference-attachment-and-holonomy-gate.md`
- `checkers/check_flat_reference_attachment.py`
- `native-promotion-constructor-trace.md`
