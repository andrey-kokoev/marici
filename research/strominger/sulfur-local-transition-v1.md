# Su-32 local transition reproduction v1

## Result

Reproduced all 16 observed passages through the eight upper mixing edges of the
existing Sulfur-32 incoming-bundle wiring. Every record exits on its actual next
reference edge, with identity, colour, polarity tuple and opaque payload intact.
Reversal recovers every input. No source route or layer geometry was changed.

This reproduces an existing candidate wiring. It does not derive its globally
chosen rim/interior middle matching from the eight-layer construction.

## The local carrier rule

Each examined carrier edge has two arrivals and two departures. Its two records
agree on three polarity bits and differ on one. Within that fixed context, one
bit distinguishes the two lanes; erasing it leaves two possible departures.
The carrier is proposed as an analogue of a white connector; its two native wires
retain their original colours, rather than being recoloured white.

- When a=+, the varying bit is p and the held bit is e.
- When a=−, the varying bit is e and the held bit is p.
- Number ports 0,1 by numeric lexicographic native coordinates, separately at
  each endpoint. In this convention, input slot = 0 for selector +, 1 for −.
- Output slot = input slot XOR [held sign is +]. Thus held + swaps slots;
  held − preserves them. This is coordinate-convention dependent.
- On reverse traversal use the inverse switch, preserving the selector value
  and the complete record. Strand ID is not consulted to choose an exit.

The same rule is learned from the other seven motifs and predicts both passages
of each held-out motif. This is an internal generalization check on this reference,
not a proof of a universal rule or independent physical validation.

| Motif | Retained strand | Colour | Carried selector | Held bit | Input → output slot |
|---|---|---|---|---|---|
| 1 | `wire:++++` | white | p=+ | e=+ | 0 → 1 |
| 1 | `wire:++-+` | red-white | p=- | e=+ | 1 → 0 |
| 2 | `wire:+-++` | white | p=+ | e=+ | 0 → 1 |
| 2 | `wire:+--+` | red-white | p=- | e=+ | 1 → 0 |
| 3 | `wire:-+++` | white | e=+ | p=+ | 0 → 1 |
| 3 | `wire:-++-` | blue-white | e=- | p=+ | 1 → 0 |
| 4 | `wire:--++` | white | e=+ | p=+ | 0 → 1 |
| 4 | `wire:--+-` | blue-white | e=- | p=+ | 1 → 0 |
| 5 | `wire:+++-` | blue-white | p=+ | e=- | 0 → 0 |
| 5 | `wire:++--` | blue | p=- | e=- | 1 → 1 |
| 6 | `wire:+-+-` | blue-white | p=+ | e=- | 0 → 0 |
| 6 | `wire:+---` | blue | p=- | e=- | 1 → 1 |
| 7 | `wire:-+-+` | red-white | e=+ | p=- | 0 → 0 |
| 7 | `wire:-+--` | blue | e=- | p=- | 1 → 1 |
| 8 | `wire:---+` | red-white | e=+ | p=- | 0 → 0 |
| 8 | `wire:----` | blue | e=- | p=- | 1 → 1 |

## First reproduced neighbourhood

Shared directed carrier: (-1,1,1,0) → (-1,2,0,0).
The rows below are exact consecutive reference vertices, not new routes.

| Strand | Previous → carrier tail → carrier head → next |
|---|---|
| `wire:++++` | (-1,0,1,1) → (-1,1,1,0) → (-1,2,0,0) → (0,1,0,0) |
| `wire:++-+` | (-1,0,2,0) → (-1,1,1,0) → (-1,2,0,0) → (-1,2,1,-1) |

## Comparison with the eight layers

There are 168 complete white-edge neighbourhoods in the layers,
grouped into 4 decorated states. Both endpoints have three
coplanar arms 120° apart.

The eight upper native motifs instead have:

- Tail arm-angle set: **60°, 120°, 180°**.
- Head arm-angle set: **60°, 60°, 90°** or **60°, 90°, 120°**.
- Head normalized Gram determinant: **1/2**, hence not coplanar.

An exhaustive scan of the occupied reference edges finds 16
co-oriented, two-record, two-input/two-output candidate carriers. **None** has the
120° three-star at both ends. The angles were also checked independently using
the viewer's actual 3D world-coordinate map.

Therefore this reproduces the **local transport**, but not a rigid geometric
identification with a single white segment of the planar layers. A specified
folding or a larger, multi-edge neighbourhood could change the comparison; this
check does not rule those out. No octahedral gluing is inferred from equal counts.

## Verification

- Implementation: research/realization-tower/sulfur-local-transition.mjs
- Tests: node --test tests/sulfur-local-transition.test.mjs
- Fresh checker: node scripts/check-sulfur-local-transition.mjs
- Full coordinates, port IDs, packets, angle evidence and source hashes:
  results/sulfur-local-transition-v1/verification.json
