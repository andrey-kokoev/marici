# Pre-Ne-20 authored wiring

Scope: the 17 catalog rows Hydrogen-1 through Fluorine-19. Operator selected the named drawings in `examples/isotope-wiring/index.html` as the visual reference and rejected retaining the first four non-editable green drafts. Ne-20 source, routing rules, saved-edit migrations and Morse cancellation are unchanged.

This is **forward realization of authored diagram data**, not a physical derivation from proton/neutron counts or a recovery of legacy graph identities. Every endpoint and alias is explicitly declared. Source coordinates are layout, not an identity-matching mechanism. Reuse follows named drawing recipes, not an algorithm that generates geometry from isotope inventory.

## Reference and adaptation

- H-1/H-2: legacy `hydrogenSketch`, open/closed upper triangle. New red arrow goes top → left, blue goes right → top; H-2 has an undirected base. H-1 starts on blue so the two-edge path can be traversed.
- He-3: operator correction supersedes the legacy outer triangles: central diamond with a single horizontal undirected green bar, left → right. The four existing colored arrows remain red top → left → bottom and blue bottom → right → top. There are no outer triangle vertices or center junction.
- He-4: legacy crossed diamond, four colored sides and two green diagonals. Their crossing is not a vertex.
- **H/He colors and directions are new authored choices**, not claims that the legacy all-green reference specified arrows.
- Li-6: legacy Li-6 upper diamond and horizontally reflected lower triangle. Preserve the local red/blue directions and horizontal connectors.
- Li-7: add two vertical side connectors to Li-6.
- Be-9: retain Li-7 rails; add the doubly reflected lower colored legs.
- B-10: explicitly reflect only the Li-6 base and append the unreflected upper diamond. Its endpoint map is written out, not inferred by coordinates.
- B-11/C-13: add the respective recipe's rails; C-12 completes B-10's lower triangle.
- N-14: append the lower triangle to C-12; N-15 adds the long rails.
- O-16: complete that lower triangle; O-17 adds long rails. O-18 instead adds two upper rails and two bent lower wrappers.
- F-19: append the last triangle and replace the lower wrappers with the recipe's longer straight connections.
- Legacy green arrow marks are not retained: all green bands use the current **undirected connector** convention. No direction is inferred from a rendered marker.

Only named endpoints join. In particular, F-19's long rails pass intermediate vertices without acquiring incidence there. O-18's wrapper bends are layout points, not graph vertices. Generic route eligibility and angular rules apply; a blocked run is not replaced by a fitted or forced tour.

## Finite acceptance table

| Isotope | Vertices | Edges | Red / blue |
| ------- | -------: | ----: | ---------: |
| H-1     |        3 |     2 |      1 / 1 |
| H-2     |        3 |     3 |      1 / 1 |
| He-3    |        4 |     5 |      2 / 2 |
| He-4    |        4 |     6 |      2 / 2 |
| Li-6    |        6 |     8 |      3 / 3 |
| Li-7    |        6 |    10 |      3 / 3 |
| Be-9    |        7 |    12 |      4 / 4 |
| B-10    |        9 |    13 |      5 / 5 |
| B-11    |        9 |    15 |      5 / 5 |
| C-12    |       10 |    15 |      6 / 6 |
| C-13    |       10 |    17 |      6 / 6 |
| N-14    |       12 |    18 |      7 / 7 |
| N-15    |       12 |    20 |      7 / 7 |
| O-16    |       13 |    20 |      8 / 8 |
| O-17    |       13 |    22 |      8 / 8 |
| O-18    |       13 |    24 |      8 / 8 |
| F-19    |       15 |    27 |      9 / 9 |

`pnpm check:diagrams` checks this table, isotope inventory, declared directions, color/direction editing and restoration, independent document instances, reference pin isolation and all 17 Morse constructions. It also tests the He-4 crossing, O-18 wrapper bends and F-19 non-junction intermediate point. The browser scenario covers every row at two device scales. These are construction and UI checks, not nuclear-model validation.

The prior four drafts retain their diagram namespace, but their new endpoints/arrows are explicit replacements. Existing storage is not cleared or rewritten by this change. Incompatible old edits or named snapshots are rejected and retained by the existing compatibility checks rather than silently reinterpreted.
