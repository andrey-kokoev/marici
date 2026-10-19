# Identifying the proposed torus circles with M and C

## Direct occurrence-index test

Tracked maximal M and C occurrence indices on all 24 native PNE seed markings
through two P-reader advances. Two readouts were checked separately: active
windows only and active windows plus context.

| Native step | Active-window (delta M, delta C) | Context-inclusive |
|---|---|---|
| PN | (1,0) | (0,1) |
| NE | (0,1) | (1,0) |
| Two P-reader advances | (2,2) | (2,2) |

There are distinct local M/C changes, but native realization advances shift
the two occurrence indices together. Including context exchanges which local
step appears to advance which channel; neither readout makes the two global
cycles independent.

## The two proposed cycle generators

For the periodic realization-chart generator the lifted change is (2,2).
For an exact same-origin P->N->E->P reference return the changes telescope to
(0,0). The candidate winding matrix is therefore

```
[2 0]
[2 0]
```

Its rank is 1, not 2. Merely relabelling the two previously constructed torus
circles as M and C would not supply two independent channel windings.

A hypothetical seam from E(r) to P(r+1) matches the channel-index maxima and
gives total change (1,1) per PNE passage. That alternative remains proportional
to the two-step realization generator and still gives rank 1. This is index
bookkeeping only; vertex identifications and a native E->P transfer are not
supplied by it. Native electrons remain terminal.

Six combinations of geometric phase (0/1) and reader (P/N/E) map to only four
M/C parity pairs. Parity coordinates alone lose reader distinctions. The actual
reader label and absolute origin must remain in the state.

## Disposition

The constructed realization/link torus remains a valid abstract prototype.
Its direct identification with independent M and C circles fails this explicit
occurrence-index test. What the source currently supports is two local channel
moves tied into one diagonal progression of absolute indices.

An independent relative M-versus-C winding would require an additional source
operation or a different coordinate construction with a checked seam. Neither
is inferred from the torus picture. This does not exclude every possible M/C
geometry; it narrows the tested index-based interpretation.

Production/viewer unchanged.

```sh
node research/strominger/checkers/check_MC_cycle_identification.mjs
```

Evidence: `results/MC-cycle-identification/verification.json`.
