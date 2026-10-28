# Two assembly approaches: bounded geometry and retained transport tests

## Common question

Can a marked four-channel inner/outer construction determine its intervening
assembly, rather than assign P/N/E to shortest paths after building a lattice?
The two experiments deliberately start from different data. No viewer, particle
assignment, native transport law or research-graph verdict is changed.

## A — geometry-first

Use actual A4 chambers in the sum-zero hyperplane of R5:

    C(k) = k + Delta(5,q), q = -sum(k), k integral.

Start at k=(0,0,-1,0,0). Mark coordinate 4 (zero-based). The face x4=0 has
four vertices; the opposite apex has x4=1. Their four connecting edges have
squared length 2. This constructs four labelled incidence ports, not a particle
transport law.

The unique neighbor across that face *in this fixed tessellation* is
k'=(0,0,-1,0,-1), a rectified 4-simplex. The shared section is a tetrahedron;
the opposite section x4=-1 is an octahedron. The ordinary 4-simplex has five
tetrahedral facets. The rectified neighbor has five tetrahedral and five
octahedral facets.

Global negation sends floors k to -k-1 and q to 5-q. It exchanges the marked
pair with its complementary q=4,3 pair exactly, retaining incidence and the
marked coordinate. This is an actual symmetry, not a particle-role assignment.

### Local closure test

Take the triangle x0=x1=0 in the seed. Its four incident chambers have floors
k, k-e0, k-e1, k-e0-e1 and levels 1,2,2,3. Their facet-adjacency link is a
four-cycle, with two tetrahedral and two octahedral shared facets.

All 15 nonempty subsets were tested for absence of exposed facets containing
that triangle. **Only the full four-cell star closes.** Omitting any member
fails. Duplicating a cell is explicitly rejected as fake closure.

The ridge has one regular and three rectified 4-simplices, not two of each.
Its angles are two arccos(1/4) and two arccos(-1/4), summing to 2*pi. Incidence
and closure are exact integer checks; the angle sum is a floating-point control.
All 120 coordinate permutations on all four chambers (480 checks) preserve
the construction without a cell-ID path tie-breaker.

**Disposition:** marked-interface continuation and ridge closure are forced
within the supplied A4 honeycomb. This does not establish a unique global
completion among arbitrary complexes, generate the initial honeycomb, identify
P/E/N, or prove that four geometric ports are the native transport channels.
The full star still has an external boundary away from the selected triangle.

## B — transport-first

Import and audit the owner's current `selectPhaseAssembly('helium4')` reference.
It has six carriers, ten reader charts and eighteen directed chart edges.
No coordinates or interface maps are substituted.

Enumerate *all chart-simple directed paths* from its fixed root to an electron,
stopping at the first electron. There are four, in this bounded path class:

| Chart sequence | Electron cell | Phase-origin advance | Five-slot permutation |
| --- | ---: | ---: | --- |
| 2,3,4 | 16 | 0 | 3,4,2,0,1 |
| 2,3,6,7 | 14 | 1 | 3,2,4,1,0 |
| 2,0,1,9,8,5,6,7 | 14 | 3 | 2,0,3,4,1 |
| 2,0,1,9,8,5,6,3,4 | 16 | 4 | 2,3,0,1,4 |

Chart IDs are reader IDs, not carrier IDs. In particular charts 3 and 6 are
readings of the same neutron cell 13. Charts 1 and 9 read neutron cell 7.

**Both pairs ending at the same electron have different coefficient maps and
different phase origins.** The calculated invertible coefficient comparisons
between them are retained in the receipt; they are not supplied native higher
comparisons. Equality of endpoint, shape, or carrier is insufficient to identify
these histories. Arbitrary walks can revisit charts and are not enumerated here.
Four paths in this bounded enumeration are not identified with four local ports.

### A correctly typed comparison square

Use the NE edges from charts 3->4 and 6->7 and the actual neutron reader advance
3->6. In the common five-slot representation, write the NE map C, the neutron
reader R, and the sought electron comparison X:

    N2[a] --C--> E1
      |           |
      R           X ?
      |           |
    N2[b] --C--> E2

The unique coefficient solution is X=C R C^-1. In stored zero-based slot order:

    C = [0,4,2,3,1]
    R = [0,3,4,1,2]
    X = [0,2,1,4,3].

The square passes on all five basis vectors. Identity X fails, and merely
copying R onto the electron side fails. However, there is no native E1->E2
edge. Calling the existing phase-advance constructor on these electron charts
is rejected: that constructor accepts P/N reader advances, not E advances.
There are no outgoing electron edges in this reference at all. Thus X is an
algebraic candidate with a missing native occurrence/history lift, not a newly
licensed physical E operation or reverse electron realization.

Two forward neutron reader advances return to the same chart with identity
coefficient permutation but phase-origin advance 2. The full state does not
return to its initial origin.

PN, NE and neutron reader advance have **no common fixed coefficient slot**.
Although the composite P/E comparison alone fixes C1, reader advance moves it.
Consequently one cannot simply discard a universally inert fifth coordinate
to obtain the four channels. This does not prohibit four channels carrying
richer data; their binding remains to be constructed.

**Disposition:** the coefficient square has a unique solution after its existing
maps are fixed. Native transport/history completion is not supplied. This does
not prove that no extension exists. The same-endpoint path discrepancies need
retained comparison data, not silent identification or arbitrary recoloring.

## Comparison and next discriminating question

A forces local geometric closure but supplies no field/phase map. B supplies a
coefficient comparison but not its admissible spatial/occurrence realization.
Neither establishes a complete isotope construction, nor selects particle
counts. Their apparent fourfold structures have different types.

The next bridge test should ask whether an actual marked geometric operation
can realize the derived X while preserving its complete five-slot field,
channel labels and phase history. Compare against the identity and copied-R
controls. Do not declare X to be a geometric symmetry merely because it is an
involution, or call the rectified cell N because it fills a gap. If no binding
is supplied, keep the two scoped results separate.

## Reproduction

    node --test tests/assembly-approaches.test.mjs
    node research/realization-tower/check_assembly_approaches.mjs

Five regression groups pass, including the negative controls. The receipt is
`results/assembly-approaches-v1.json`, with complete local cell vertices,
interfaces, reader maps, path records and comparison candidates. Hashes cover
the experiment, tests and two direct native sources, not a full dependency
closure. No proof-assistant or physical validation is claimed.

Sources: `ramsey-plane-lattice-realization-v1.md` under Voevodsky for the prior
A3 geometry; `phase-first-assembly-v2.md` and the actual phase assembly/advance
modules under Strominger; `check_shared_neutron_duality.mjs` and
`native-phase-lift-audit-v1.md` in this directory for the retained-duality context.
