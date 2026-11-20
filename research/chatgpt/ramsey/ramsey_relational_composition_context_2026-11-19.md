# What composition preserves in a relational Ramsey carrier

2026-11-19 · Context handoff · [Ledger 4335](../../../src/ledger/20261119-4335%20Ramsey%20Composition%20over%20a%20Shared%20Pair.md). The [earlier handoff](ramsey_constructor_and_sector_return_handoff.md) indexes the layout, Fourier, Pauli, modular-form and sector experiments. This note records the change in question, not a new Ramsey-number proof.

## Starting convention

Only relations are primitive. A “stage” is a step in a derivation, not a physical visit. Count positions up to the stated equivalence: equal external neighborhoods do not merge two positions when their mutual link and multiplicity still affect clique size. Ordinary matrix multiplication sums over a middle index. Joining two views instead keeps shared roles identified long enough to check all their incidences. A representation of an existing matrix is not a constructor unless its inputs and wiring are independently specified.

## Strongest composition test

Fix red as adjacency. Take two induced copies of the five-cycle, the sole largest red/blue triangle-avoiding coloring up to isomorphism. Identify exactly two distinct roles, preserving the color of their mutual link. Each copy has three private roles, so there are nine free cross-links and eight distinct roles in the union. Enumerate all 512 binary completions for each interface color; reject any red triangle or blue four-set. Canonicalize only after that test.

| Shared relation | Valid labeled fillings for the fixed interface | Unlabelled outputs |
|---|---:|---:|
| Red | 12 | 3 (multiplicities 2, 3, 7) |
| Blue | 0 | 0 |

These are exactly the three largest (eight-role) admissible (3,4) graphs, checked against the catalogue **after** generation. The seed and overlap size were chosen. The viability of red rather than blue and the three outputs were not. Inputs symmetric under relabeling can yield a family, not a privileged single matrix. [Checker](ramsey_c5_relational_amalgams.py) · [Result](ramsey_c5_relational_amalgams_run.txt).

## Other reusable operations

- **Exponents with memory.** Start with one empty selection; append a fresh role only if it is linked in the required color to *all* previously selected roles. The red layer at depth l and blue layer at k must both have **zero selections**. This is clique extension, not an ordinary adjacency power counting walks. It explains the exact border rule: a new red neighborhood must be red-independent and hit every old blue (k−1)-clique.
- **Multiplicity has a cost.** Replace role v by a blue family of size w_v, preserving all external links. The red clique number is unchanged and the new blue clique number is the maximum of sum(w_v for v in C) over old blue cliques C. On the 35-circle the maximum (3,10) extension by pure copies has 37 positions. All these maximal choices are terminal even for unrestricted bordering. [Weight test](ramsey_clique_power_blowup.py) · [Terminality check](ramsey_twin_family_borders_run.txt).
- **Symmetric distinction is stronger than copying.** Replace v by twins a,b and add the red path a–x–y–b; x and y have no red links outside that path. This adds three positions to any triangle-free graph without introducing a red triangle and increases the largest blue clique by exactly one. A blue clique cannot use both x,y, and deleting the twin red-linked to either recovers a copy of the old graph. If neither is used, at most one extra copy contributes. The bound is attained by one new position plus a maximum clique of the copy it sees entirely in blue. On the 36-position one-twin core, all eight pure-copy next borders stopped at 37; 23,586 non-copy profiles reached 38. [Census and explicit witness](ramsey_one_twin_continuations_run.txt). This does not reach Exoo's 39 or exclude 40.

## Geometry: what transfers, what does not

On the side-7 tetrahedron the three opposite-edge pairs give three symmetry-related middle-band tests. They leave 40, 16, then 4 lattice sites: the permutations of (1,2,2,2), jointly bounding T184. This identifies a cell; it does not add a physical step or show when address 22 first appeared in a convolution. For side n=4q+r the four most balanced corner distances give the coordinates q·1+1_S with |S|=r. Side 6/10 gives an octahedron, 7/9 a tetrahedron, 8 a point. The divisor four comes from *four tetrahedral corners*, not from a demonstrated law of R(3,n). [Middle bands](ramsey_esd7_opposite_edge_middle_run.txt) · [Four-corner reconstruction](ramsey_t184_four_views.py). Relative binary marks on a triple also give four edge readings, but the [switch test](ramsey_triangle_four_switches_run.txt) ruled out nonidentity triangle-free switches on the tested extremal examples. Matching counts do not identify the carriers.

The barycenter is fixed by frame action; it is not the identity matrix or an extra integer site. Reflection through it gives a dual reading, whereas the [reciprocal lattice check](ramsey_t184_reciprocal_incidence_run.txt) preserves neighbor incidence by **switching centers**. The 12-sector tour realizes all three equatorial comparisons only with a specified reflect-on-closure rule. [Native packet test](ramsey_fcc_packet_edge_binding_run.txt): the stationary C1 reference is not the moving site tracing the square. No independent sector-to-Ramsey link law was established. The [earlier comparison-interface conjecture](ramsey_37_comparison_interface_conjecture.md) remains distinct from these results.

## Where to resume

The open problem is **selection of the overlap**, not producing more layouts of a known output. Two eight-role inputs meeting on exactly two roles would have 14 distinct roles. Since R(3,5)=14, zero legal (3,5) completions are possible at that size: the literal two-role successor rule cannot simply be iterated. A sharper test is to take the three eight-role input classes, enumerate their common induced interfaces by isomorphism, and compare the admissible unions. A three-role overlap gives 13 roles, but choosing three *because* 13 is the known target is fitting, not selection. Report both which unions exist and whether any source-side criterion predicted the overlap before enumeration. Keep failed interfaces and distinguish labeled counts from isomorphism classes.
