# Neutrino seed hypotheses: arrow-first assembly consequences

## Scope

Keep the existing cycle-isometry and facet/cone assembly rules. Do not add a spin lift, charge assignment or particle-specific filling rule. A seed is a labelled arrow-occurrence record; a listed cycle acts on the labels, fixing unlisted vertices unless a simultaneous action is explicitly stated. Cycles are required to act as isometries, as in the existing proton metric-closure control. A common squared seed-edge length of eight fixes only the overall scale convention.

The earlier `neutrino-geometric-candidate.md` spin decoration is **parked**. It is not an input to this experiment. This packet supersedes it as the active neutrino hypothesis.

## Exact numbered results

| # | Arrow seed | Occurrences | Incidence kernel dimension | Metric/assembly consequence |
|---|---|---:|---:|---|
| 1 | AB, BC, CA | 3 | 1 | All three distances close; equilateral triangle, affine rank 2 |
| 2 | AC, CB, BA | 3 | 1 | Same metric as #1, reversed arrow history |
| 3 | Both orientations | 6 | 4 | Same triangle, additional retained directed-arrow relations |
| 4 | AB, BC, CA; AD, DE, EA | 6 | 2 | Generated permutation group has order 60 and one orbit on all ten pairs; regular four-simplex, affine rank 4 |
| 5 | AB, BC, CA; DE, EF, FD | 6 | 2 | Two components; nine cross-pair distances unspecified; not a belt without additional placement/interface data |
| 6 | AB, BC, CD, DA | 4 | 1 | Adjacent distances fixed, diagonals initially unspecified; proper-orientation admission matters |
| 7 | AB, BC, CD, DE, EA | 5 | 1 | Adjacent/diagonal pairs form two separate orbits; a regular pentachoron is not forced |

The incidence kernel refers to the boundary map from retained directed occurrences to labelled vertices. It is not the dimension of a spin space. An undirected support graph and the directed occurrence complex are different records: #3 has the same support as #1 but a larger occurrence kernel.

Under the existing supporting-facet/center-cone rule, #1 realizes a triangular disk with three center-cone triangles. The arrow graph alone is an unfilled loop; filling is an existing processor operation, not inferred simply from a closed traversal.

## Why the higher cycles need care

### Four-cycle

With adjacent squared lengths eight, both of these metrics are Euclidean and invariant under the cyclic permutation:

- diagonals squared eight: regular tetrahedron, affine rank three;
- diagonals squared sixteen: square, affine rank two.

However, the tetrahedral four-cycle reverses orientation on its affine span and is rejected by the current assembler's **proper-isometry** rule. The square cycle preserves orientation and is admitted. Thus dropping that rule would change the candidate set. The checker retains both as a scope control; it does not claim the tetrahedron passes the current assembler.

### Five-cycle

Fix adjacent squared lengths eight and common diagonal squared length t. Exact principal-minor tests admit t=4,8,16, all with affine rank four and orientation-preserving cycle action. Their Gram determinants are respectively 80,1280,1280. Equal determinants do not make their labelled metrics equal: the diagonal distances differ.

Therefore a five-cycle alone does not select the regular four-simplex (t=8). The existing electron fixture supplies a complete metric; its geometric construction remains valid, but must not be reclassified as an arrow-only consequence of its five-cycle.

### Disjoint three-cycles

The neutron control retains the source's simultaneous order-three action on both rims. Its orbit closure supplies no cross-rim edges. The existing neutron source additionally supplies their relative placement, metric and reserved-cap roles. Running that complete source recovers the belt; deleting those inputs does not derive it from six arrows alone.

## Modes derived from the candidate arrows

Reuse the existing triangle-coordinate action

    C(a,b,c)=(b,c,a).

Its characteristic polynomial is lambda^3-1. Exact eigenvectors are

    (1,1,1), (1,omega,omega^2), (1,omega^2,omega),
    omega=(-1+sqrt(-3))/2.

These are consequences of the cyclic arrow action, not an independently attached representation. Reversal interchanges the two nontrivial character labels. All three modes are available; no selection is supplied. Crucially, **C^3=I, not -I**: this computation does not manufacture a spinorial full-turn sign.

The proton already has nontrivial triangle characters, so finding such a character is not sufficient to distinguish a neutrino. Nor are three modes three physical flavors.

## Active conjecture and next gate

**#1 remains the smallest candidate in this numbered family:** a retained oriented three-cycle, realized by the existing processor as an equilateral triangular disk. This is not a global minimality theorem or a physical neutrino identification.

The next scientific obligation is to reuse a source-admitted mode-selection/attachment operation and test whether it distinguishes this standalone cycle from the proton's existing face cycles. Preserve the actual arrows and return history. Do not assign neutrality, chirality, weak couplings or mass as decorations to make the candidate look like a neutrino.

## Reproduction

```sh
python research/strominger/checkers/check_neutrino_arrow_seed_science.py
python research/strominger/checkers/build_neutrino_seed_candidates.py
```

Both exact executions pass. Results:

- `research/strominger/results/neutrino_arrow_seed_science.json`: arrow closures, incidence ranks/kernels, metric counterexamples and derived cyclic modes;
- `research/strominger/results/neutrino_seed_candidates.json`: all seven explicit realization fixtures run through the unchanged `assemble_relative_geometry.py`.

The fixture outputs are distinguished from arrow-forced consequences. Browser/gallery verification is outside this scientific packet and was not completed.
