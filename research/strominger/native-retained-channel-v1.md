# First executable retained channel and assembler

## Constructed, not just specified

The [channel contract](contracts/native-retained-channel.v1.json) and [incremental assembler](checkers/native_retained_channel.mjs) now replay the existing native joint-field fixture from one ordered stream.

The decoder receives **no completed packet, chart, cell or readout tables**, and no esd7 census. It starts from the four marked seed vertices, invokes the unchanged native constructors, and derives geometry, contexts, coefficient permutations and field-frame words as records arrive.

This completes the bounded `channel-contract-and-first-assembly-step` task. It does not construct the full proposed1+4x28+1 channel.

## Actual stream

[The generated stream](results/native-retained-channel.json) has23 typed records:

| Record type | Count | Meaning |
|---|---:|---|
| open |1|Seed, root reference and contextual witness|
| begin |2|Start a named retained history at the root|
| execute |14|A distinct native operation occurrence and its local context witness|
| witness |4|An additional interface between already retained packets; not another execution|
| compare |1|Two retained history positions; compute their relative coefficient frame|
| close |1|Require both exits and complete retained-interface coverage|

The output reconstructs14 packet presentations,18 interfaces, two P bodies, two N bodies, one E body and two terminal histories. The order-five coefficient comparison is computed from the reconstructed packets, not supplied as its answer.

The supplied operation words are known retained histories. They are not claimed to emerge from a clock. These23 records are not relabelled as114 records, and the opening/closing rules here do not settle the meanings of the two additional1 terms in the global conjecture.

## One whole survives serialization

Packet references are shared across histories. Reusing a packet does not merge its execution occurrences. The decoder retains both ordered histories and the complete serialized record log.

Every prefix is an admissible retained native assembly. Interfaces whose witness records have not arrived are listed explicitly as pending obligations. Closing requires zero pending interface witnesses and certified exits. This is incremental construction with visible obligations, not a claim that every unfinished prefix is already a closed coherence object.

Transmitting the two independent histories in the other order reconstructs the same labelled assembly, while retaining a different serialization log. Swapping dependent operations within a history is rejected.

## Independent reconstruction and field verification

The encoder/checker can inspect the original fixture to produce and compare the stream. The decoder cannot: it only uses the stream and the native rules. Comparison ignores allocation-dependent integer IDs and checks actual marks, geometry, origins, permutations, interfaces and ordered histories.

The full [44-channel sewing checker](checkers/check_joint_field_assembly_sewing.py) was extended to accept a separately reconstructed fixture and write a separate receipt. It then recomputed every field/readout equation on the decoder output:

    R_target U_edge = Pi_edge R_source.

All18 interfaces pass on the full field. Both E exits retain the two E directions plus three baryon directions, with all five coefficients recoverable. The original fixture receipt was also freshly replayed; it was not overwritten by the reconstructed-fixture result.

## Negative controls

The assembler rejects dropped or forged context, swapped dependent occurrences, duplicate occurrence IDs, unknown references, rebound identities, missing incidental interface witnesses, invalid comparison positions, absent closing records, records after close, and injection of a completed target table into the opening.

A failed replay is fail-closed: it cannot resume from partially mutated state or return a completed assembly. A fresh replay is required.

## Reproduction

```sh
node research/strominger/checkers/check_native_retained_channel.mjs
python research/strominger/checkers/check_joint_field_assembly_sewing.py \
  --fixture research/strominger/results/channel-assembled-native-fixture.json \
  --output research/strominger/results/channel-assembled-field-sewing.json
```

The reusable decoder API is `NativeChannelAssembler.feed(record)` followed by `finish()`, or `decodeChannel(records)`. Encoding is a separate function; no target fixture is an argument to decoding.

Results:

- [20 channel checks](results/native-retained-channel-verification.json).
- [Derived native fixture](results/channel-assembled-native-fixture.json), including prefix obligations and full occurrence log.
- [18 exact field checks on that derived fixture](results/channel-assembled-field-sewing.json).

## Next construction

The [single-channel esd7 conjecture](single-channel-esd7-assembly-conjecture.md) remains open. The next interface is the source-bound esd7 attachment grammar and channel producer: determine which records introduce, identify or compare cells and witnesses, then assemble the intended full channel without reading the completed census as an answer. The native fixture is now an executable regression case for that extension, not a substitute for it.
