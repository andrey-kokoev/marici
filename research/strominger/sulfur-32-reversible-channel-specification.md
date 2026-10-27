# Sulfur-32: reversible channel specification

Status: operator-directed interpretation and construction target. The [global periodic wiring candidate](sulfur-32-global-wiring-v1.md) now constructs 16 N channels with four wires each and reversible 2-by-2 endpoint presentations. Its closure hypothesis and remaining native-phase/physical bindings are explicit.

## Retained carrier

Use the Single octahedron at edge units 3: 51 whole cells, geometrically labelled 16 P, 19 N and 16 E.

Group the six tip N cells into three opposite-end pairs:

- +P / −P: `neutron:2,2,0,-1` and `neutron:0,0,2,1`;
- +N / −N: `neutron:2,0,2,-1` and `neutron:0,2,0,1`;
- +E / −E: `neutron:2,0,0,1` and `neutron:0,2,2,-1`.

Each tip has exactly one N-cell owner, and geometric inversion exchanges each pair. Keep both endpoints and their incidences. The resulting grouping has 16 N-channel identities: 12 other surface N cells, one central N cell and three paired-tip groups. This grouping does not delete geometry.

## Operator's channel interpretation

Treat these as 16 dual-directional channels for wires. The same N channels must serve either P-to-E or E-to-P presentation; reversing the presentation must not require a different N-channel inventory.

P, N and E cells jointly organize wiring that enters as a 2-by-2 arrangement and leaves as a 2-by-2 arrangement, reversibly in the P|E sense. P/E distinguish the opposite-end presentations of that wiring. Do not introduce a transformation of wire contents merely to explain N.

Retain the complete wire identities, path information, endpoint groupings and histories. A forward/reverse comparison must recover that retained wiring, not merely its counts. This specification supplies no particular permutation or scattering matrix. The subsequent global candidate derives the path correspondence from its periodic incidence and uses the four coordinate axes as its declared 2-by-2 port indexing.

## Operator refinement: two primitives

At the current abstraction level use only:

1. A P/E pair, considered without choosing its reading orientation because the pair is dual.
2. An N tube segment.

The operator proposes viewing the N tube segment as a **double-twist of the P/E pair**. This is a geometric/wiring identification to construct, not an established result of the existing periodic quotient. Do not assign a rotation angle, twist operator, phase action or change of wire contents merely from the phrase “double-twist.” The next comparison should exhibit the pair and tube presentations and their retained port correspondence. Orientation is set aside at this abstraction level, rather than counted as another primitive.

## Operator refinement: signed pair bundle and four-tube entry

This supersedes the preceding incoming-PNE-triple description.

The arriving wire is `(P+ E+) | (P− E−)`, carried in **one N tube**. The signs distinguish directions; they are not assigned electrical-charge or amplitude meanings here.

1. **Layer 1:** connect the incoming wire's N tube to the shape's selected incoming N tube. This is the shared-body attachment, not a separate N signal leg.
2. **Layer 2:** separate the two pairs by direction, giving `+(PE)` and `−(PE)`.
3. **Layer 3:** lay the four pairings through its four N tubes: `+(PE)`, `−(PE)`, `+P−E`, and `−P+E`.

Equivalently, the four layer-3 tube assignments are indexed by the direction of P and the direction of E:

| P direction / E direction | +E | −E |
|---|---|---|
| +P | +(PE) | +P−E |
| −P | −P+E | −(PE) |

This specifies the pairings and their layer order. It does not yet specify how shared incoming records are retained across the pairings; do not silently duplicate independent payloads, sum them, or introduce a transformation of their contents.

The tip layers 1 and 9 still have no intrinsic source/destination semantics: all six vertices are N. A chosen direction supplies the incoming attachment role. The opposite-end pattern is in layers 8–7.

This is the operator's revised construction specification. The existing periodic quotient's four coordinate-axis slots have not been identified with these four signed pairings; the two 2-by-2 presentations must not be equated by count alone.

## Layer-4 recombination locations

Fresh shared-face enumeration, on all three slicing axes and from both ends, separates layer 4's twelve charged cells into:

- Eight outer cells: four P/E pairs, each pair adjacent to exactly one layer-3 N tube.
- Four central cells: two P and two E, each adjacent to two layer-3 N tubes.

For each central cell, its two incoming N tubes share exactly one layer-2 charged-cell reference. The two central P cells correspond to shared E references; the two central E cells correspond to shared P references.

With layer-3 channels labelled by `(P direction, E direction)`, the central incidence supports these comparisons:

- Compare `(+,+)` with `(−,+)`, or `(+,-)` with `(−,-)`: compare the two P directions at a shared E reference.
- Compare `(+,+)` with `(+,-)`, or `(−,+)` with `(−,-)`: compare the two E directions at a shared P reference.

Thus the central four cells locate the two kinds of additional comparison, each with two reference choices. If the intended six outputs enumerate all unordered pairings of the four signed input strands, the missing two are `P+ / P−` and `E+ / E−`, complementing the four cross-P/E pairings. This combinatorial interpretation is not yet an implemented routing law or an identification of these outputs with oriented P/E pairs. Geometry alone does not select a pairing of the four central cells into two output pairs.

## Middle-layer six-channel feasibility

Layer 5 contains nine N cells: four non-tip peripheral cells, four transverse tips and one central cell. The established opposite-tip grouping turns the four transverse tips into two channels. Thus the middle plane has **six peripheral channel groups plus one central cell**.

`checkers/check_sulfur32_middle_layer.mjs` exhaustively assigns layer-4 P and E cells to the six peripheral channel groups using actual shared faces. It finds two complete P assignments and two complete E assignments, giving four joint assignments. Each channel receives one P and one E, with all twelve charged cells used exactly once. Reflection through the middle plane fixes every middle N cell and supplies an exact corresponding assignment to layer 6 with geometric P/E roles exchanged. No central-cell passage is required for these assignments.

All three slicing axes and both directions pass. Full assignments are retained in `results/sulfur-32-middle-layer/verification.json`. This establishes six-channel sufficiency at shared-face incidence level when regrouping is allowed. It does not select the assignment of the six signed pairings, establish that the center is exclusively ground, or impose the earlier periodic model's coordinate-axis wire rule.

## Construction discipline

Follow `global-coherence-standing-assumption.md`: construct the complete wiring from global coherence conditions, then use local reader rules only as verification constraints. Opposite-tip pairing supplies the proposed channel grouping, not yet proof that every grouped pair carries identical paths.

Current implementation: `../realization-tower/sulfur-32-process.mjs` offers initial geometry and global-fibration stages. Original geometric colours and all 51 source cells remain; the second stage exposes 48 cell fibers and reversible channel tables. No wire-content transformation is introduced.
