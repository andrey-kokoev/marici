# Complete finite biclique comparison hierarchy

## One rule through all available dimensions

For each complete K(p,q) block of retained source/target family incidence,
p,q>=2, introduce a cell of dimension p+q-2. Rectangles have four-edge
boundaries. Higher boundaries are alternating source/target deletion faces;
target deletions carry the sign (-1)^p and faces with fewer than two vertices
on a side are omitted. This is the same rule used for the earlier2- and3-cells.

Enumerating all eligible blocks of the137-slot fixture terminates at dimension6.
Every consecutive boundary composite vanishes over the rationals.

| Degree | Cells | Boundary rank | Homology dimension |
|---:|---:|---:|---:|
| 0 | 64 | 0 | 17 |
| 1 | 137 | 47 | 0 |
| 2 | 672 | 90 | 0 |
| 3 | 1304 | 582 | 0 |
| 4 | 1074 | 722 | 0 |
| 5 | 416 | 352 | 0 |
| 6 | 64 | 64 | 0 |

The1074 predicted4-cells fill all722 directions in ker(d3). Their own352
relations are filled by the416 local5-cells. The remaining64 relations are
filled by the64 local6-cells, whose boundary is injective. There are no higher
complete bipartite blocks. The Euler characteristic is17, matching the connected
component count.

## Structural result

The retained relation generates a finite hierarchy of comparisons, comparisons
between comparisons, and their further relations using one boundary rule. Its
positive-degree rational homology vanishes in this fixture. The17 component
classes remain in degree0.

Equivalently, the chain groups give an exact finite resolution of the component
space, with dimensions and maps determined by local incidence. Higher-cell
coefficients and boundaries remain explicit data. This homological calculation
does not remove member records or identify their operational versions.

The generated degrees0 through6 and their cell counts are now available for
comparison with the proposed tower. They supply neither its nine presentation
rungs nor a1,2,4 independent-factor count by themselves. The next selection
question concerns what mathematical object this local comparison complex
presents, and which of its invariants the tower would use.

## Verification

    python research/nima/checkers/check_biclique_comparison_complex.py

The checker enumerates all source subsets within each incidence component and
all target subsets common to them. Componentwise enumeration avoids irrelevant
subsets spanning disconnected state pairs. It constructs each signed boundary,
checks every boundary composite, computes ranks by sparse exact Fraction
elimination, and asserts the full dimension/rank/homology table. Flipping a
single target-face sign of a K(3,3)4-cell produces a nonzero composite, providing
an orientation negative control.

The rational result concerns this fixture. Useful next controls are restoring
the omitted primitive arrow and comparing simpler incidence graphs under the
same rule. Those tests distinguish a general comparison construction from
exactness specific to the chosen input. Integral torsion and general contraction
formulas have not been computed.
