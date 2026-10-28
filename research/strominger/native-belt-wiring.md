# Wiring derived from the current native cellulation

## Superseded presentation

The displayed wiring no longer uses 64 abstract P/E port arrows, 74 internal links, 32 terminal links or two synthetic terminal-bundle nodes. Those constructors and tests remain as historical/experimental reference models; they do not define the current viewer graph.

## Native graph

`examples/normal-ray/native-belt-wiring.js` consumes the same posed parent cellulations and extended belt used by Geometry view, before diagram expansion:

| Part | P tetrahedral nodes | N octahedral nodes | E tetrahedral nodes | All nodes |
|---|---:|---:|---:|---:|
| Two parents | 166 | 112 | 72 | 350 |
| Extended belt | 10 | 14 | 10 | 34 |
| Total | 176 | 126 | 82 | 384 |

Every node retains its native cell ID and kind. P/E node roles use the native tetrahedral orientation, with the two explicit E-tip overrides. Every whole octahedron is an N filler. These are whole-cell node counts, not counts of exposed triangular faces.

- One undirected link per shared complete triangular face: 728 within the parents and 64 within the belt, **792 total**.
- Two separately typed `native-tip-contact` links at the actual E-tip/belt-pole vertex coincidences.
- **794 total links, zero directed transport links, zero synthetic terminal nodes.**

The graph is connected. No full-facet link is fabricated across a vertex-only contact. Contact coordinates are checked in the geometric pose, then all node centres are moved into an exploded diagram. Parent node positions are translated rigidly; belt positions are expanded axially and transversely for readability. V-labels use the same parent transform.

The nine belt node planes are derived from projected native cell centres. Their node counts are **1,4,4,6,4,6,4,4,1**. The settings use a separate nine-plane mask so saved masks from the historical six-layer arrow diagram cannot silently hide unrelated native cells. Hidden nodes remove all incident links.

## Readout and scope

The bottom-right table labels wiring counts as **nodes**. Geometry continues to show exposed P/E faces and octahedral filler counts. Neither readout has been identified with a physical particle inventory. In particular, N=126 and E=82 in the native dual do not resolve P=176 versus the Pb-208 target 82.

This establishes source-backed graph adjacency and vertex-contact incidence, not a transport direction, capacity, native field map, common global lattice phase or mechanical/physical binding.

## Verification

- `tests/belt-wiring-layout.test.mjs`: cell IDs, counts, one shared facet per ordinary link, explicit tip witnesses, connectedness, absence of directed links, geometry unit edges/contact, native-plane masks and parent visibility.
- `scripts/test-neutron-belt.mjs`: built viewer counts, native-plane controls, node-count table, Geometry/Wiring distinction, V-label anchors, visibility, saved settings and mode changes.
- `scripts/test-native-belt-publication.mjs`: published route, native graph counts, table, navigation and reload.
- Existing historical port-model tests remain separate and retain their original 64-node/106-link contracts.
