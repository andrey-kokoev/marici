# Native belt-to-parent gluing

Obligation: forward realization / geometric attachment, separate from field transport.

## Current construction

At the operator's request, remove **one unit tetrahedral N tip per parent**, not a two-layer cap. Keep the complete tip records in `parentCutAudit.caps[].retainedCell`; underlying native parent/fiber records remain unchanged. The viewer excludes these two cells and their labels/wireframes in both geometry and wiring modes.

`research/realization-tower/belt-N-cap-docking.mjs` finds the exposed face of each neighboring whole octahedron and rigidly matches it to slot 3, the central unit triangle of the corresponding four-triangle belt patch. Translation and roll suffice; there is no scaling. Maximum vertex mismatch is below 2e-15. All remaining parent vertices lie in the exterior supporting half-space; all belt vertices lie in the opposite half-space. Consequently their cell interiors cannot overlap. Each displayed parent has 174 cells, with its removed tip retained separately as data.

The N terminal glyph now anchors at the exposed face centre, rather than the removed N vertex. Complete native fiber records and symbolic belt wiring are retained. This is geometric attachment, not certification of field transport or global lattice phase registration.

Belt triangle borders are white, 3.5 screen pixels wide, marking the declared **inside-N / N-less sector**. This visual convention does not establish a new field law.

## Earlier intact-parent obstruction

`belt-parent-gluing-audit.mjs` remains a counterfactual check on intact parents: the 196 exposed unit triangles have outward-normal dot products 1/3 (147 triangles) and −1 (49 triangles) relative to the outward N axis. None faces axially toward the belt. It also records an unused two-layer cap alternative (four tetrahedra and one octahedron); that larger cut was NOT selected.

## Verification

- `node --test tests/belt*.test.mjs tests/central-belt*.test.mjs tests/complex-visibility.test.mjs`: 48 passing.
- `node scripts/prepare-normal-ray.mjs && node scripts/test-neutron-belt.mjs`: built viewer and browser checks pass.
- `tests/belt-N-cap-docking.test.mjs`: direct face-coordinate, half-space non-overlap, record preservation and rendered cell-count checks.
