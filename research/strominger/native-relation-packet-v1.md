# Iteration4: exact finite relation case encoded as a native WG

## Fresh obligation and result

Read the35-node net and current handoff. The recommended relation task required encoding the actual finite products/cuts as native Complete/Layer1 packages rather than just naming Python dataclasses WGs.

That encoding is now implemented and freshly checked. It exports one actual eight-term five-event balancing case (singly retained a, forgotten middle, forgotten b), its two distinct cuts, and the separate four-event attachment evidence. The exporter reruns the previous exact source checks and consumes their live objects, not a hand-copied count or digest.

## Native signature

`RelationPacketEncoding.agda` defines typed records for path terms, arrows, factor packets, requests, certified cases and retained answers. A factor packet carries its two arrows, product, raw and balanced seam data, endpoint-composability and product-boundary equalities.

A Case contains both factor packets, the original a/middle/b request, attachment data, equality of the two exported products, equality of the balanced seams, and a nonzero leading-magnitude certificate. Raw and balanced seam keys have a tagged inductive-tree encoding; marks, word labels, coefficient signs and magnitudes are retained.

`ActualRelationPacketCase.agda` contains the literal exported objects, independently serialized for both cuts. Agda checks their equality certificates by reduction. It also proves `different-raw-cuts` by the actual cut-address detector: the two raw cut records cannot be equal even though their balanced outputs are.

The case-to-answer transition uses the existing Layer1 signature. The answered state retains the whole certified case and its selected product, with an actual reconciliation witness. `complete-answer` packages that Answer as an atom in the existing Complete universe. The request, both factors/cuts and attachment data recover definitionally. Existing reification makes the complete answer available as a next input, with exact recovery.

The generator consumes a certified case; it does not infer unknown source identities. The particular input certificates here are checked on the source-generated literals, not postulated. Both factorizations remain inside the answer, rather than being replaced by their common balanced value.

## Verification split: what is and is not proved in Agda

The new runner first invokes `export_relation_packet_case.py --check`. That reruns all eight finite source-algebra cases and four negative controls, regenerates the expected Agda text in memory, and rejects a mismatch with the on-disk source. It then runs a fresh safe Cubical Agda closure with ignored interfaces and stable source/compiler/checker inventories.

The kernel checks endpoint typing, literal coefficient-vector and balanced-data equalities, the leading coefficient magnitude, raw-cut distinction, generated-step typing and complete-package recovery. The Python source checker supplies multiplication, terminal observation, seam differentiation/boundary, canonical sparse-vector normalization and computation of the actual local source action. No end-to-end formalization of that algebra or of the general nonsplit extension is claimed. In particular a leading term proves source nonzero here because the executable source verifies canonical nonzero coefficients; it is not a general noncancellation theorem for arbitrary term lists.

The four-event attachment is retained as exact data, including both computed actual and disconnected-graded action matrices. It is not yet an executable Agda module-action interface. Therefore this iteration does not close the parent relation-layer binding: a complete-source action cannot be replaced merely by storing an uninterpreted matrix.

## Next nonredundant step

Expose the actual local right action a->ab as a typed operation on the native retained packet, with source-action preservation and the disconnected-direct-sum hostile checked at that operation interface. Reuse the existing finite source receipt and known nonsplitting theorem; do not recompute another product count or claim a global module from one stored matrix.

## Verification

    python research/strominger/checkers/export_relation_packet_case.py
    python research/strominger/checkers/check_native_relation_packet.py

Passed: live-source export comparison, source finite tests and fresh Agda closure. Existing nonfatal owner import warning remains. Receipt: `research/strominger/results/native-relation-packet-agda-v1.json`.

New source files: `RelationPacketEncoding.agda`, generated `ActualRelationPacketCase.agda` under `research/strominger/agda/`.

No owner source implementation was changed. No global source reconstruction, physical137 adapter, complete phase law, arbitrary witness synthesis or universal Type claim is made.
