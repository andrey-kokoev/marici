# Main-shape boundary inventory for L1/L1′ attachment

The current separated-parent presentation replaces 49 former shared seam triangles. These give 49 actual face candidates per parent, 98 owner-face records total. Each record retains the owner ID, owner face index, native vertices, paired opposite-side face, displayed coordinates, world centroid, outward normal and face area.

Both sets have source owner roles 25 proton, 23 neutron and 1 electron. Those are particle-role labels from folded occurrences, **not** declarations of sector-space P/E transport. They must not be used to assign belt headings.

The belt boundary has 16 demands per parent: four minority centres receiving three flux units each from the belt and twelve majority satellites supplying one unit each to the belt. Thus each parent requires 12 units in each direction under the audit normalization. All 32 demand records retain the actual belt node, star, arm, position and direction.

## Assignment gate

The inspected parent occurrence/face records do not specify per-face allowed transport directions, flux capacities, or full-fiber boundary maps. These are stored as null, not guessed from geometry, particle roles or face area. A capacity-compatible assignment therefore cannot yet be certified. No parent links have been installed, and the 74-link belt remains unchanged.

The missing input is a boundary transport adapter on these actual face IDs: allowed directions, capacities in a declared normalization, and the retained fiber map. Once supplied, attachment assignments can be checked against all 32 demands, derived across the parent correspondence, and audited using their actual slanted paths instead of axial boundary stubs. Geometric partner identity alone does not establish a field transport map.

## Reproduce

- `node scripts/audit-belt-parent-ports.mjs`
- `node --test tests/belt-parent-port-inventory.test.mjs`
- Receipt: `results/belt-parent-port-inventory.json`
- Implementation: `../realization-tower/belt-parent-port-inventory.mjs`

Tests verify all 98 native owner faces, reciprocal seam pairing, geometry validity, four balanced stars per side, correct P/E demands and explicit blocking rather than speculative attachment.
