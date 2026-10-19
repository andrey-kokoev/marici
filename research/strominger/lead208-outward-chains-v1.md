# Explicit Pb-208 P–N–e loadout

**Window-transfer audit:** the current layout passes its geometric checks but
0/82 chains preserves the C1/M1 edge required by the recovered marked-carrier
protocol. It is not a window-compatible construction. See
[the prior-research recovery](window-transfer-prior-research-recovery.md).

The user-specified incidence rule is implemented in `lead208-model.mjs`:
82 proton items each connect across a face to an outward neutron item,
which connects across another face to a further-outward electron item.
The existing 44 reserved witnesses are assigned the remaining neutron roles.
Thus the loadout contains **82 P + 126 N + 82 e = 290 distinct particle shapes**.
There is no longer an overlapping P/N capacity assignment in the Pb viewer.

## Construction

- Keep the original 1/4/44/126 assembly unchanged: 175 items, 343 primitive cells.
- Use the 82 non-reserved outer items as proton shapes. All 82 have exposed faces.
- Across each exposed triangular face, enumerate the unique adjacent item in
  the same integer-coordinate tetrahedron–octahedron honeycomb.
- Electrons must be regular tetrahedra. Enumerate an outward tetrahedral
  endpoint and fill the intervening face-connected lattice items as its neutron.
  For 74 chains this is one octahedron. For the eight octahedral protons it is
  a tetrahedron plus an octahedron; the electron sits across their next face.
- Select one chain per proton, requiring all constituent lattice items to be
  distinct, including constituents of composite neutron shapes. Constraint
  search chooses the most constrained unassigned proton first; address
  ordering breaks ties among admissible chains.

This adds 82 neutron and 82 electron bodies (172 lattice items, 418 primitive
cells), for 761 primitive cells in the extended space. It does **not** alter the resolution,
subdivide existing cells, reflect tetrahedral caps off-lattice, or reinterpret
a cavity as a particle. Octahedral groups retain their four-cell subdivision.
The 49 earlier inner items remain structural context, not extra particles.

Each neutron exactly fills its selected local connector gap. This is not a
claim that every global void is filled or that a closed outer shell is derived.
The rule constrains connections and outward order but does not select a unique
embedding. Tie-breaking is an explicit realization convention, not a physical
law. The construction does not establish particle masses, orbital states, or
the stronger assertion that every extension witnesses the previous whole.

## Viewer

Select Lead-208. Protons, Neutrons, and Electrons independently show actual
positive shapes. Electron faces are semi-transparent (opacity 0.22), with
dotted edges; nuclear faces remain opaque. Transparency changes rendering,
not occupied volume. Witness links are annotations only and do not change particle
occupancy. Click a particle in an outward chain to highlight its P/N/e partners.
No layer-item, fiber-control, or context-control cards have been reintroduced.
H/D/He keep their local views; the added Pb geometry is hidden there. Their
electrons now occupy native tetrahedral primitive cells sharing a full nuclear
face, rather than cells two hops away. These small-preset primitives can be
nonregular octahedral-subdivision tetrahedra; Pb electron items are regular.

## Verification

`node research/strominger/checkers/check_lead208_model.mjs` verifies:

- 82 P, 126 N, 82 e, with 44 witness neutrons;
- 82 face-connected chains with strictly outward centroid ordering;
- 82 regular tetrahedral Pb electrons, each sharing a full neutron face;
- eight composite neutron volumes exactly filling their connected local gaps;
- unchanged base coordinates and integer coordinates summing to one;
- positive volume and no duplicate primitive cells;
- all 289,180 primitive pairs: no positive-volume overlap or containment;
- triangular-face incidence at most two.

`node research/strominger/checkers/check_fiber_space.mjs` also checks rendered
counts, species toggles, click selection, isotope isolation, and responsive
layout. Evidence: `results/lead208-loadout/verification.json` and
`results/fiber-space/` screenshots.
