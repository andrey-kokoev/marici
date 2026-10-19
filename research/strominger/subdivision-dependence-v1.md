# Fixed-root octahedral subdivision comparison

## Outcome

**None of the three uniform octahedral diagonal choices yields neutral N-14
through realization origin 10 under the existing local reference rules.**

The representation is strongly subdivision-dependent, however. The existing
diagonal permits N->N realization advances and a growing geometric universe.
Both alternatives suppress all such advances in the generated universe and
reach only five distinct cells through the tested bounds.

This tests the subdivision conjecture without changing the root marking,
contact rules, packet operators, electron quota or particle-volume definition.
It does not exclude mixed site-dependent subdivisions or larger origin bounds.

## Controlled transformation

The [prospective protocol](subdivision-dependence-protocol-v1.md) fixes three
opposite-vertex diagonals of every octahedron:

- `02|13`: the existing subdivision;
- `01|23`: induced by coordinate permutation `[0,2,1,3]` within each item;
- `03|12`: induced by `[0,1,3,2]` within each item.

The transformations change only the four component permutation lists in
`simplex-components.mjs` and `lattice-items.mjs`, consistently in the assembled
space and local neighbor constructor. Item origins and the proton root are
not permuted. The generator, PN/NE/reader/NN phase maps, branch conventions,
reference-only-P policy and every solver constraint are byte-identical across
isolated source snapshots.

Checks on all 175 original items establish:

- the same 343 primitive-component count;
- identical untriangulated item vertices and external triangular boundaries;
- the same regular tetrahedral cells and exact root coordinates;
- four positive unit-volume components per octahedron, preserving total volume;
- agreement between assembled and locally generated octahedral components.

Each alternative is a coherent coordinate-permuted version of the known
four-tetrahedron triangulation inside each unchanged octahedron, so no extra
volume or overlapping cap is introduced. Physical equivalence of native
operations under these different supplied subdivisions is not assumed.

Production files and other-owner sources were copied, never edited. Source
hashes were checked before/after; changed snapshot modules and complete search
artifacts are retained under the owner-local result directory.

## Local windows with root held fixed

For all three subdivisions, the full 24-marking sweep still gives eight native
PN/NE packets with an external regular E endpoint and sixteen with an internal
split E endpoint. But which ordered markings produce those outcomes changes.

For the **exact unchanged canonical root binding**:

| Diagonal | Is root NE face on whole-octahedron boundary? |
|---|---|
| `02|13` | No |
| `01|23` | **Yes** |
| `03|12` | No |

Thus the earlier local root obstruction can be removed by one subdivision,
but not both alternatives. Root roles were not recolored to obtain this result.
An exterior root E endpoint is only a local condition, not an isotope packing.

## Neutral N-14 target results

For each subdivision, complete packet universes were generated for every
maximum origin D=3,4,5,6,7,8,9,10. The existing targeted solver imposed exact
7P/7N/7e body counts, compatibility of all selected packet roles, rooted
construction, actual transport witnesses for every physical face contact and
E-exit reachability from every selected record.

All **24** queries returned UNSAT. No packet resource cap or solver timeout was
reached. Universe sizes differ markedly:

| Diagonal | Packets at D=3 | Packets at D=10 | Distinct reachable cells at D=10 | N->N advance operations at D=10 |
|---|---:|---:|---:|---:|
| `02|13` | 87 | 3,651 | 225 | 847 |
| `01|23` | 12 | 33 | 5 | 0 |
| `03|12` | 12 | 33 | 5 | 0 |

The five alternative-subdivision cells comprise one possible P, two possible N
and two possible E body sites. These are the union of reachable possibilities,
not automatically a jointly compatible five-body state. They cannot contain
seven protons. Additional packet records at higher origins through D=10 only
reread that small geometric region.

The original subdivision's 225-cell universe has 105 possible P, 105 possible
N and 116 possible E body records; N/E alternatives can occupy the same cell,
so their sum is not the number of distinct geometric cells. Its neutral failure
is not a simple shortage of ambient sites.

The disappearance of NN advances is a result of the unchanged native-reference
and geometry rules on the new split cells—not an added prohibition. Both
alternatives have PN, inverse-PN, NE and same-carrier reader advances, but no
valid NN-phase-advance operation in the completed finite universes.

## Solver crosschecks

Each snapshot's targeted encoding was checked against **all composition
profiles** in its own complete origin-1 configuration enumeration:

| Diagonal | Explicit configurations | Target queries including impossible controls |
|---|---:|---:|
| `02|13` | 108 | 28 |
| `01|23` | 12 | 8 |
| `03|12` | 12 | 8 |

All agree. SAT control selections are found in the corresponding explicit
list and pass the original whole-state contact/exit auditor. The old fixed
expectation of 108 origin-1 configurations was generalized in the crosscheck:
108 is a baseline result, not a requirement on different geometry.

Large-bound UNSAT remains a solver result for a finite supplied universe, not
a formal independently checked UNSAT proof or an unbounded theorem. No global
cross-branch field sewing is asserted.

## Interpretation and next boundary

The simple conjecture “choose another uniform diagonal and neutral N-14 will
work” is not supported within these bounds. But the test confirms that the
current generative capacity depends on a geometric choice that was not itself
derived as physical mechanics.

One alternative solves the local exterior-electron issue at the price of
losing growth branches. Therefore neither “make E exterior” nor “preserve a
nice whole-octahedron volume” is sufficient. A productive further hypothesis
would involve **site-dependent diagonal choices**, preserving growth where
needed and exposing valid E windows elsewhere. Such a search must make shared
item/subdivision choices globally consistent and retain exact context, phase
and incidental-contact checks; it cannot switch the same octahedron's diagonal
independently for different readers.

That mixed-diagonal search was **not** performed. Nor was a whole-octahedron
particle identity or physical binding law added. The viewer remains unchanged.

## Reproduction

```sh
node research/strominger/checkers/check_subdivision_dependence.mjs
```

The runner creates temporary complete source snapshots and removes them after
saving evidence. It reruns the target solver and small explicit-family
crosscheck separately in each snapshot. Requires Node and `uv`/Python with the
solver dependency specified by the existing target-search script.

Evidence: `results/subdivision-dependence/verification.json`, per-diagonal
`comparison.json`, source snapshots, solver inputs/results and crosscheck
receipts. The root packet's actual bindings and window histories are retained
for each alternative.
