# Oscillator cut: decorated FCC-cell representation

## Interpretation decision

The conjecture says the domain is **represented** as FCC or equivalent tetrahedral structure. Requiring the oscillator itself to be a physical spatial crystal would add a different claim. The representation-level test can be performed without that addition.

The existing `fcc_gaussian_boundary_recursion.md` defines the canonical FCC cell T_1 with vertices (0,0,0), (1,1,0), (1,0,1), (0,1,1). Its substantive boundary objects retain kernels and normalization, not bare cell shape. This supplies a prior example of the relevant distinction between a geometric carrier and its retained data. Its Gaussian operator is not imported into the oscillator model.

## Explicit representation

Assign the four roles of the already constructed oscillator cone to T_1, retaining:

- the promoted whole and the three certified focus views at vertices;
- the six typed comparisons and their source/target roles;
- the four face incidences and inherited coherence convention;
- the nested member data carrying the bath contribution.

All four coordinates belong to the even-sum FCC lattice. Every edge has squared length two; the cell volume is 1/3. These are chart geometry, not measured oscillator lengths.

For each of the 24 bijections from typed roles to chart vertices, the decoder recovers the same cone. Extracting the opposite-apex face by its retained roles recovers the same promoted packet and oscillator readout. Checked for both inherited-key and common-target promotion policies: 48 charts in total. The numeric chart test uses the exact existing resonant fixture; symbolic response preservation belongs to the preceding cone check.

Vertex permutations are passive chart changes with all decorations transported. They are not a derived S4 physical symmetry of the oscillator.

## Tests and limits

Deleting an edge incidence is rejected. Keeping all geometry while removing the nested bath coefficient gives a different decorated object with the same shape: its noise readout is zero instead of -4/5. Thus bare tetrahedral shape is not a faithful representation, while the full decorated chart is.

The map is a faithful representation of the constructed cone on its image. It is not an equivalence with all possible FCC data, a derivation of a physical metric, or a construction of an infinite FCC tiling. The generic cone construction also means this result alone does not establish that tetrahedral presentation is uniquely necessary.

## Disposition

**The bounded oscillator instance passes the representation-level interpretation:** its promoted domain has a typed tetrahedral cone, a recoverable triangle, and a faithful decorated realization on the canonical FCC tetrahedral cell. No further literal-crystal requirement is imposed on this branch.

This completes the initial single-mode Markov test, not the full thermal fluctuation-dissipation theorem or the all-laws conjecture. The next untouched independent example is anomaly inflow. It must retain its quantized level and relative orientation under the same discipline; do not repeat the oscillator representation check.

Verification: `uv run --with sympy python research/strominger/checkers/check_oscillator_fcc_representation.py`, exit zero, execution `structured_command_execution:e_42200_1792520836494598000_36`. Receipt: `research/strominger/results/oscillator-fcc-representation/verification.json`. Historical FCC Gaussian calculations and the generic Agda proof were not rerun.
