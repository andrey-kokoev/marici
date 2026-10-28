# Previous-level triangular perimeter belt

The current viewer replaces the small internal-carrier display with the operator's six-dots-per-side triangular perimeter: 15 distinct dots (6 + 5 + 4, without counting corners twice).

`research/realization-tower/perimeter-belt.mjs` derives the positions from the existing shared ESD7 face, not a new volume mesh. Its 21 octahedral face ports form the previous-level triangular array; selecting its boundary leaves 15. Each side contains exactly six positions. Each displayed point is the centroid of an actual shared triangular face, with both original and clone owner IDs retained.

The perimeter is a declared **face-port graph**, not a newly proven tetrahedral volume subdivision. Each selected original/clone seam edge is replaced in this presentation by two owner-to-port links; the ports also form a 15-cycle. Thus each belt port has four incident links (two lateral and two parent). No all-to-many rim fan-out is used. Parent colours and particle accounting remain unchanged. Graph mode has 350 parent references plus 15 port nodes; ordinary mode also shows the 15 dots and triangular outline.

Local transition function:

- N → P
- E + |N| → P
- E + |P| → N

The source octahedral ports are N, so initialization applies N → P. The two conditional E transitions are implemented and unit-tested, but no incoming N/P signal schedule is invented; there is no claim that an E-driven circulation has been executed.

Visibility buttons independently control original ESD7, clone ESD7, and the perimeter belt. Hidden owners hide their incident graph links. All visibility combinations and reload persistence are tested.

Verification:

```
node --test tests/perimeter-belt.test.mjs tests/complex-visibility.test.mjs
node scripts/prepare-normal-ray.mjs
node scripts/test-neutron-belt.mjs
node scripts/test-double-esd7.mjs
```
