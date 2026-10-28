# Central belt: declarative six-layer model

## Source of truth

`research/realization-tower/belt-layer-model.mjs` declares the six layers in physical order from the first ESD7 toward the second:

| Layer | Geometry | Local transport pattern | Rotation |
|---|---|---|---|
| L1 | four stars, each central P + three E | EEEE / EPPE / EPPE / EEEE | 0° |
| L2 | node star, central P | retained addresses: PE / EE | 0° |
| L3 | three stars, each central P + three E | EEE / EEE / EEE / PPP | 0° |
| L3′ | three stars, each central E + three P | PPP / PPP / PPP / EEE | 0° |
| L2′ | node star, central E | retained addresses: PP / PE | 0° |
| L1′ | four stars, each central E + three P | PPPP / PEEP / PEEP / PPPP | 180° |

Layer names count inward from each main shape: L1/L1′ four-star arrays, L2/L2′ node stars, L3/L3′ three-star arrays. Unprimed names are on the first ESD7 side. Controls are paired in that order; stable physical indices remain for IDs and visibility persistence. Geometry is unchanged by renaming.

P/E denote sector-space transport directions, not ordinary particle assignments. All 64 nodes have null particle roles. L1/L2 and L1′/L2′ each have 16 symbolic links. The PPP triangle of L3 has three links to the single P of L2; the EEE triangle of L3′ has three links to the single E of L2′. The remaining three E nodes of L2 interleave across all three EEE triangles of L3; the three P nodes of L2′ likewise interleave across the PPP triangles of L3′. Each triangle receives one branch from each source bundle. Central exchange adds nine E links from L3 to L3′ and nine P links from L3′ to L3. Every source star connects to all three opposite stars: satellite arm k feeds opposite minority centre k, in both directions. Each destination centre receives one branch from each source star. Links retain symbolic `(group,vertex)` witnesses plus explicit source-star/arm and destination-star addresses. Internal total: 74 links, coloured to match their endpoints. Two same-sign N terminal bundles now add 32 parent connections (106 total): original +N supplies L1's twelve E satellites and receives its four P centres; clone −N supplies L1′'s twelve P satellites and receives its four E centres. Each terminal retains its parent's occurrence records. Native field fibration remains unbound and parent orientation is unchanged; see `belt-N-terminal-wiring.md`. Port capacities and full bus mappings remain unspecified.

## Placement

All centres lie on the same normal axis. For zero-based index `i`, the plane offset is `(2.5 - i) * spacing`, with spacing **1.05 world units**. Thus all five gaps are equal and the six-layer stack is centred between the parents. The spacing parameter is 0.8. L1/L1′ each contain four stars with centres on a square of side 1.2. Each star has one minority arrow at its centre and three majority satellites at radius 0.32, spaced 120° apart. The old 4×4 row/column records are retained as symbolic addresses, not displayed grid positions. Each star contains one satellite from each of the three existing majority bundles, preserving every link. Grid rows descend from +y; columns ascend along +x. Each central layer contains three four-arrow stars, with centres at radius 1.2, 120° apart. Every L3 star has a central P and three E satellites; L3′ reverses those directions. Satellite radius is 0.32, matching the corresponding L1/L2 stars in both size and orientation. The retained `(group,vertex)` records now group visually by vertex: each star receives one minority centre and one satellite from each majority group. The L3 support retains its 180° offset relative to L3′. All 64 node identities and the total of 74 links are preserved; central exchange endpoints now implement complete star-to-star wiring. L2 and L2′ use matching four-node stars: minority P/E at the centre, majority nodes at radius 0.32, spaced 120° apart. Their size and orientation match the individual stars in L1/L1′ respectively. This replaces their earlier alignment to the larger L3/L3′ support centres; symbolic wiring is unchanged. The original 2×2 row/column addresses remain symbolic identities, not display positions. Explicit bundle-slot addresses preserve all pre-existing wiring independently of these new positions. No triangle perimeter edges or other interlayer connections are inferred.

The old triangular alignment references, independent plane corrections and named first/second/etc. audit fields are removed. Adding or changing a layer is a data-model operation, not a renderer patch.

## Presentation and rendering

`central-belt-layout.mjs` adapts model world positions to viewer coordinates and the common node presentation contract. Its version-2 audit exposes one ordered `layers` array. Parent transforms are unchanged: original ESD7 120° CCW viewed from below toward V2, clone 120° CW viewed from V6 into the shape. Parent offset remains 3.2.

`examples/normal-ray/belt-renderer.js` supplies the same transport-node arrow renderer to solid and graph modes, including picking in both modes. Each arrow is centred at its existing node position, points along the belt normal for P (toward the first ESD7) and opposite it for E (toward the second), and retains the direction colour. This is the declared glyph convention. The renderer does not calculate layer geometry or infer wiring. Layer controls are generated from the same layer records; explanatory summaries are omitted from the UI; settings use the model's layer count. Visibility filtering is render-only.

## Symbolic L1/L2 and L1′/L2′ wiring

`belt-wiring.mjs` connects each outer grid's central 2×2 minority block to its L2/L2′ star centre. The twelve perimeter nodes are traversed from the top-left across the top edge, then down the right, along the bottom and up the left, split into three consecutive groups of four. These map to the three retained outer star slots. The oriented fine-grid address, bundle and branch are retained for recovery. The earlier generic quadrant encoder remains available but is not used for these centred patterns. Each fine node has one connection, and each coarse node has four separately identified branches. P edges follow increasing normal coordinate, E edges decreasing normal coordinate.

The instantiated relation has an explicit reversal which exchanges source/target and transport heading; reversing twice returns the complete record. For star arrays, the constructor uses unrotated symbolic arm addresses: displayed rotation must not regroup transport bundles. This corrects the primed outer half-turn mismatch. Legacy grid inputs still use oriented grid addresses. Both star pairs are tested for arm alignment and weighted geometric balance. The same constructor is applied to both pairs. Links render in both modes and disappear when either endpoint layer is hidden. No UI explanatory text was added.

The central triangle rule retains three vertex branch addresses and explicit square-bundle slot identities, independently of the star geometry. Minority routes keep the direct triangle connection. Majority routes use `three-bundle-transpose`: source bundle k, branch j goes to triangle j, vertex k. The bundle order comes from retained slot identities, preserving the reflected construction. Source and destination addresses are retained and mutually recoverable. The minority PPP/P and EEE/E routes point outward; the majority E/EEE and P/PPP routes point inward. The central exchange retains `(source group, vertex)` on each link. Directional reversal preserves this witness, and reversing twice restores the full relation.

## Verification

- `tests/belt-layer-model.test.mjs`: immutable definitions, patterns, rotations, equal spacing at several scales, renderer positions and colours.
- `tests/central-belt-layout.test.mjs`: actual presented centroids, all five equal gaps, common normal, parent rotations and accounting, only the requested links on both outer pairs.
- `tests/complex-visibility.test.mjs`: all 64 layer masks and parent visibility.
- `scripts/test-neutron-belt.mjs`: six controls, absence of explanatory dumps, spacing and wiring audit, solid/graph modes and persistence.
- `scripts/test-double-esd7.mjs`: parent process regressions.

Viewer rebuilt and these checks passed after the rewrite.
