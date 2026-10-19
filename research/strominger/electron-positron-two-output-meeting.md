# Electron/positron meeting into two retained outputs

## Constructed meeting

Keep the complete electron ABCDEA and positron AEDCBA histories as separately owned arrow occurrences. Meet them at registered labels A and C and cross-pair their complementary paths:

| Output | Electron part | Positron part |
|---|---|---|
| 1: A -> C | A -> B -> C | A -> E -> D -> C |
| 2: C -> A | C -> D -> E -> A | C -> B -> A |

Each output contains five occurrences, two from one source and three from the other. Together they retain every one of the ten input occurrences exactly once. The complementary outputs are reversed route comparisons, not two independent truncated seeds.

## Exhaustive same-label test

Ten unordered meeting-label pairs and two piece matchings give twenty meetings. Five endpoint pairs use the requested 2/3 cuts; five use 1/4 cuts as a control.

Crosswise pairing gives two five-occurrence parallel-route outputs for every meeting. Pairing each path with its own reverse instead gives unequal-sized backtracking outputs: four and six occurrences for the 2/3 cuts, or two and eight for 1/4 cuts.

All six exact accounting/classification checks pass.

## What has not emerged

The constructed outputs have pentagonal supports and parallel path orientations. For the 2/3 example, each endpoint-continuation operator has characteristic polynomial lambda^5. None of the twenty meetings produces two outputs carrying the prior conjugate C3 photon modes. Nor are these the previous six-occurrence shared-edge two-triangle seeds.

Thus this constructs a lossless two-output meeting, not a two-photon interaction. The missing operation is an explicit, common comparison/interaction rule that maps each retained path pair into the same photon output object. Endpoint matching by itself supplies no such map.

The unchanged affine generators still complete to the original electron four-simplex. No particle-dependent stop, new filling, spin assignment or arrow deletion was installed.

## Verification

```sh
python research/strominger/checkers/check_electron_positron_two_output_meeting.py
```

Result: `research/strominger/results/electron_positron_two_output_meeting.json`.
All meeting records, owner-labelled occurrence manifests, continuation matrices and source hashes are retained.
