# Reciprocal tetrahedra: known-constraint numerology

Exploration requested by the operator, not a nuclear prediction or completion of
the separate unfinished flag-family iteration. Calculator:
`checkers/explore_reciprocal_tetrahedral_numerology.py`; arithmetic output:
`results/reciprocal-tetrahedral-numerology/arithmetic.json`.

## 1. The requested triangular planes already occur exactly

Use A translations(0,2,2),(2,0,2),(2,2,0), B=A+(1,1,1), and height
h=x+y+z. The actual orthonormal height is h/sqrt(3). Then A planes are h=4k
and B planes h=4k+3. Occupied layers are

    A0 --3-- B3 --1-- A4 --3-- B7 --1-- A8 ...

Within each plane, vectors(-2,2,0),(-2,0,2) have squared lengths8 and dot4:
an exact equilateral triangular lattice. Same-family planes have ABC stacking.
This is the(111) description of the existing diamond-type network, not a second
lattice imposed on it. Seven exact arithmetic assertions passed.

The four center-to-vertex moves have heights3,-1,-1,-1. Thus one tetrahedron has
three corners in a base plane and one in another plane; its barycenter sits one
quarter of the height from the base. The opposite family reverses this. The3:1
spacing is forced by a tetrahedral centroid, not fitted. Coordinates are discrete;
physical spacetime or a preferred physical axis has not been derived.

P is an A-corner tetrahedron centered on B; N is a B-corner tetrahedron centered
on A. Site labels in the diagram refer to centers as well as opposite corners,
not to extra pointlike nucleons in addition to whole tetrahedra.

## 2. Shell numerology: promising prefix, decisive mismatch

A triangular pile has tetrahedral site counts C(k+2,3):

    1,4,10,20,35,56,84,...

Doubling gives2,8,20,40,70,112,168,... . The first three match the familiar
nuclear magic counts2,8,20, but the next magic count is28, not40; subsequent
major magic counts50,82,126 also do not follow this formula. This doubled
sequence is also the ordinary spin-doubled3D harmonic-oscillator shell sequence,
so its prefix is not distinctive evidence for tetrahedral nucleons.

Doubling is itself an EXTRA assumption: our lattice sites currently locate whole
nucleons, not orbitals into which two opposite-spin nucleons can be placed.
Do not silently change the meaning of a site. These are nuclear counts, not
electronic shell capacities2n^2, and layers are not automatically energy levels.
A spectrum/occupation mechanism would be needed to improve the sequence; choosing
new grouping boundaries after observing magic numbers is not a prediction.

## 3. Isotope imbalance constrains the boundary

If each occupied center has four potential reciprocal links, with E realized
P-N links, bP=4P-E and bN=4N-E. Therefore

    bN-bP=4(N-P),
    (bP+bN)/(4(P+N)) >= |N-P|/(P+N).

For iron56(P26,N30), calcium48(P20,N28), lead208(P82,N126), uranium238(P92,N146),
the LOWER BOUNDS on unused slot fractions are7.14%,16.67%,21.15%,22.69%.
They are not calculated physical bond deficits, and achievability is not proved.
A closed fully saturated region demands P=N and fails for these neutron-rich
examples. Boundaries, vacancies or additional interfaces are indispensable if
this occupancy rule is retained. A neutron-rich termination is a concrete
candidate to examine, not yet a derived neutron-skin or stability mechanism.

## 4. Light nuclei and approximate masses are sharper controls

The source center graph is bipartite, four-coordinate and has shortest loops6.
It naturally permits a nearest-neighbor P-N pair, consonant with using deuterium
as a first binding test. This does not establish binding: no energy law exists.

For helium4, a connected induced network of2P and2N has only three such links,
a length3 path: no triangle,4-cycle or tetrahedral K4 can occur. Consequently
'alpha is stable because four nucleons form a complete nearest-neighbor
tetrahedron' is NOT available in this source. Geometry of each nucleon must
not be confused with the graph formed by several nucleon centers. Real nn and
pp nuclear interactions also prevent interpreting the bipartite links as all
possible physical interactions without extra structure.

Approximate familiar empirical inputs mp=938.272, mn=939.565, me=0.511 MeV/c^2
give mn-mp~1.293 MeV/c^2 (~0.1378% of mp) and free-neutron beta Q~0.782 MeV.
A/B geometric equivalence is compatible with near-equal P/N masses as an
unbroken leading approximation; exact duality plus a duality-invariant dynamics
would give identical paired spectra. A selected symmetry-breaking dynamics is
needed for the split. Opposite tetrahedral orientations do not explain charges
+1 and0, and the electron is not already an eight-corner cube by this arithmetic.
Masses here are rounded illustrative empirical inputs, not newly verified data.

## Productive next experiment

Enumerate occupied patches of THIS two-family lattice under predeclared compact
boundary rules, recording(P,N), boundary slots, layer terminations, and source
adjacency. Start with deuterium and helium4; then compare equal-count and
neutron-rich patches at fixed size. This tests whether the boundary geometry can
even supply the proposed isotope bookkeeping before choosing any force law.
Do not fit a different shape independently to each target nucleus, and do not
call a count-matching patch stable without a specified energy/response model.
