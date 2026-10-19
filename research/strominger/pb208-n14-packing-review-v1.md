# Pb-208 packing: what transfers to N-14?

## Summary

Pb-208 successfully separates its geometric electron endpoints without an E/E
face contact. It does so in a **different whole-item particle representation**,
not through a better realization of the current primitive marked-carrier
rules. Its global resource solver is reusable; its particle shapes and contact
rules cannot be silently imported.

A concrete transfer of the resource-solving idea was tested for strict N-14:
exact nonadjacent-electron allocation on all 2,384 typed cores. Every core has
maximum capacity below seven. The obstacle is not greedy electron placement.

## Pb mechanism, freshly audited

`fiber-space-model.mjs` pairs 44 layer-2 items to 44 outer witness items using
augmenting-path matching. The other 82 outer items supply proton bodies.
`lead208-model.mjs` then enumerates outward full-item chains from exposed faces:

1. Enumerate integer-honeycomb neighbors across complete boundary faces.
2. Walk outward until reaching a regular tetrahedral electron endpoint.
3. Fill the intervening one or two items with a single neutron connector body.
4. Choose one option per proton jointly, using most-constrained-first search
   and rejecting reused constituent resources.

The selected solution requires only 83 recursive solver visits, including its
root. This is not an exhaustive count of possible assignments or a physical
preference law. Resource uniqueness prevents occupied-volume duplication; it
does not itself forbid every undesired contact.

Actual particle shapes:

| Species | Shape | Bodies | Primitive components per body |
|---|---|---:|---:|
| P | regular tetrahedron | 74 | 1 |
| P | octahedron | 8 | 4 |
| N | octahedron | 118 | 4 |
| N | composite tetrahedron + octahedron gap | 8 | 5 |
| E | regular tetrahedron | 82 | 1 |

The 118 octahedral neutrons include the 44 reserved witnesses. Composite gaps
retain their actual constituent volumes; they are not single split cells.
The extended space has 761 primitive components including retained structural
context, not 761 particles.

The complete body-boundary contact audit finds:

- **0 E/E** triangular-face contacts;
- 193 E/N faces and 242 N/P faces;
- **32 P/P** faces, forbidden in the strict assembly model;
- 11 N/N faces.

These are boundary-face counts, not necessarily distinct body-pair counts.
There are many additional contacts beyond the 82 designated chain links;
nonoverlapping chains alone are not an all-contact phase certificate.

## Why it is not already an N-14 phase-construction recipe

The marked protocol requires PN and NE attachment faces to share the retained
C1/M1 edge—two vertices. In Pb's actual chains, 17 pairs of faces share no
vertex and 65 share only one. **0/82 passes even that necessary window test.**
Fresh geometry verification still passes positive volumes, manifold incidence,
resource uniqueness and all 289,180 primitive nonoverlap pairs. That success
must not be promoted to marked-window or transport admission.

Pb also permits octahedral protons and volumetric composite neutrons. The strict
N-14 compiler expects four-vertex MMCC carriers, one regular cell per proton
and one split cell per neutron. Its reader/phase/coefficient maps have no
established binding to these larger bodies. Representing an octahedron as four
existing tetrahedra does not automatically make it one native neutron, nor
justify counting four native neutron carriers as one particle.

The regular-electron restriction and an outward boundary role are useful
architectural clues. But simply permitting regular electron cells in the
existing N-14 search was already tested and did not add eligible placements.
The larger connector geometry and marked-window conditions must be considered
together; regularity alone is not the missing switch.

## Actual transfer test: exact joint E allocation

The Pb solver's important reusable idea is global resource coordination rather
than independently chosen endpoints. To test that idea without altering the
particle grammar, regenerate all 5,632 geometry-only N-14 electron combinations
with E/E contact temporarily permitted for diagnostics. Group them into their
2,384 fixed nuclear-role cores, recover each core's full eligible electron
pool, then solve an exact maximum independent-set problem on E/E adjacency.
The solver branches on the most constrained cell and explores both occupying
and excluding it; no heuristic cutoff is used.

| Maximum simultaneous nonadjacent electrons | Typed N-14 cores |
|---|---:|
| 4 | 224 |
| 5 | 464 |
| 6 | 1,696 |
| 7 or more | **0** |

Eligible pools still reproduce the established 1,920 seven-cell and 464
eight-cell histograms. Joint optimization cannot produce a neutral strict
N-14 reference because none of these pools supports seven compatible cells.
This result remains limited to the existing finite ansatz.

## Useful next direction

The transferable research hypothesis is **a neutron connector need not equal
one primitive tetrahedron**. To test it responsibly, first supply a common
marked-carrier binding for a whole octahedron or composite gap:

- its particle-count identity, ordered active window and context;
- its PN/NE faces retaining the actual shared edge;
- transport of every existing coefficient and provenance of extra context;
- compatibility witnesses for every incidental boundary contact;
- a boundary/continuation interpretation independent of neutral electron quota.

Only after that exists should Pb-style chain candidate enumeration and joint
resource solving be used for a new N-14 search. A geometry-only connector trial
could be informative, but must be labelled a new representation—not a passing
result under the unchanged phase rules. Making an N-14-specific larger neutron
solely to obtain the desired particle count would not be justified.

## Verification

```sh
node research/strominger/checkers/check_pb208_n14_packing_transfer.mjs
node research/strominger/checkers/check_lead208_model.mjs
```

Both passed. Receipts:
- `results/pb208-n14-packing-transfer/verification.json`
- `results/lead208-loadout/verification.json`

The review receipt records source fingerprints, actual Pb shapes and contacts,
window-face intersection counts, the N-14 capacity histogram and representative
maximum independent electron sets. No production or viewer rule changed.
