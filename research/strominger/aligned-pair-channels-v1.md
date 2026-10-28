# An explicit 28-channel, 14-stage communication atlas

## What is now constructed

The retained eight-reference bank supplies **28 distinct unordered pair channels**. A declared marked-chart scheduling rule covers them in **seven forward stages**, four disjoint pairs per stage, then performs **seven reverse-order contravariant returns**.

This is an executable protocol, not a renaming of the earlier 28 sequential LRRR events. It does not derive particle attachments or the surface-filling words. All 28 channel identities are retained; four are active in each stage.

## Step definition and operational machinery

The definition is `aligned-pair-channel-steps-v1.json`. It declares:

1. form all unordered pairs of the retained references;
2. project through seven disjoint matchings, retaining source and provenance;
3. return through the dual maps in reverse matching order;
4. require agreement of all occurrences of each shared reference;
5. never add repeated presentations together as if they were independent values.

`aligned-pair-channel-model.mjs` executes the definition. The reference bank is freshly constructed by the preceding native-context model, not a new set of fitted points.

## Seven matching presentations

Index the marked reference bank by the three-bit values 0..7. For each nonzero direction d, pair i with `i XOR d`. Every pair appears once, because its unique direction is `i XOR j`.

| Forward stage | Direction | Four active channels | Reverse stage |
|---:|---:|---|---:|
| 1 | 1 | 01, 23, 45, 67 | 14 |
| 2 | 2 | 02, 13, 46, 57 | 13 |
| 3 | 3 | 03, 12, 47, 56 | 12 |
| 4 | 4 | 04, 15, 26, 37 | 11 |
| 5 | 5 | 05, 14, 27, 36 | 10 |
| 6 | 6 | 06, 17, 24, 35 | 9 |
| 7 | 7 | 07, 16, 25, 34 | 8 |

These are **reference-slot numbers**, not the viewer's V1..V5 vertex labels. The marked three-bit indexing and direction order are explicit scheduler choices, not an inferred physical clock.

There are 56 endpoint occurrences across 28 channels, but only eight independent reference values. Each reference appears in seven channel occurrences. Inconsistent copies are rejected rather than averaged.

## Actual covariance and contravariance

For one matching d, let

```
P_d : V^8 -> direct-sum of four V^2 channel packets
```

select and order the matching's endpoint values. Since the pairs are disjoint and cover the bank, P_d is a permutation presentation and reconstructs the entire bank.

The reverse operation on dual packets is the actual adjoint/pullback

```
P_d* : dual channel packets -> (V^8)*.
```

The checker tests the evaluation law on independently supplied complex dual weights:

```
< P_d x, phi > = < x, P_d* phi >.
```

This is not silent inversion of a noninvertible face inclusion. It is an explicit dual map for the chosen matching projection. With a coherent retained dual bank, each return reconstructs that same bank; the seven returns remain seven provenance-bearing presentations, not seven times the value.

Every channel transport carries its endpoint order and orientation. All eight native-context frame actions permute complete matchings and the full 28-channel atlas covariantly. The direction schedule must be transported along with the frame, not reset to numerical order after relabelling.

## What is—and is not—aligned

Each channel has a stable identity, two source references, an oriented endpoint reading, a forward occurrence, and the corresponding dual-return occurrence. Shared-reference agreement and full source recovery are checked. This is the sense in which the 28 channels are aligned across the 14-stage protocol.

The channel atlas includes non-nearest-neighbour pairs. It is a communication/comparison structure, not a claim that all 28 pairs are elementary lattice edges. A physical or native attachment realization needs actual routes and comparison witnesses for those pairs.

This protocol's 14-stage clock is separate from:

- the three-splits/four-actions seven-event LRRR block;
- its four-block, 28-event history with q^4=Sigma;
- the proposed 1+[4x28]+1 assembly stream.

No identification between those clocks is asserted by counting. Likewise, the three extra context preparation values remain unspecified, and no P/N/E surface pattern has been inferred.

## Native attachment follow-up

The [executed growth binding](aligned-native-growth-v1.md) now selects PN at stage 3 and NE at stage 5 by their coefficient-pair support. The resulting three-cell assembly is native-certified. Stage-indexed transport is required before channel values can glue; the reverse stages are genuine dual returns, not native reverse growth. Reference-changing NN continuation and multiple-frontier surface growth remain unbound.

## Verification

```
node research/strominger/checkers/check_aligned_pair_channels.mjs
```

**11 exact check groups pass**: unique channels; disjoint coverage; fourteen-stage pairing; every basis-vector reconstruction; complex dual evaluation; global shared-value gluing; no sevenfold overcount; rejection of missing/duplicated/relabelled/inconsistent packets; full context-frame covariance; transported schedule order; and the nonlocal-edge control.

`results/aligned-pair-channels-v1.json` retains all channels, all stages, the frame/direction correspondences, an exact execution trace, source hashes, and the scope boundaries. The current Three.js filling is unchanged.
