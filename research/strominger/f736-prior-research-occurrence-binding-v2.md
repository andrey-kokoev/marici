# F736 deeper search: separate the disjoint-occurrence square from H234

## Freshly inspected sources

- `research/voevodsky/results/esd7_explicit_analytical_census.json` and its builder: actual fine incidences and barycentric words.
- `research/voevodsky/the-eight-node-pyramid-is-the-seventh-edgewise-subdivision-and-should-be-proved-coherent-by-one-simplicial-extension-not-343-independent-checks.md`: independent transfer types and shared-boundary coherence strategy.
- `research/voevodsky/the-signed-suzuki-divisor-cell-propagates-to-the-entire-eight-level-lattice-by-edgewise-subdivision-functoriality.md`: explicit status correction separating formal propagation from actual parent identification and fine-stage alignment.
- `research/voevodsky/interior-pyramid-nodes-must-refine-a-homotopy-coherent-diagram-of-four-realization-functors-not-mix-the-presentations-barycentrically.md`: common Hermitian-form target and full factorization/regularization data.
- `research/voevodsky/correction-the-hardy-defect-realization-is-not-the-elementary-conductor-tetrahedron.md`: a valid Hardy dilation does not automatically supply the conductor comparison edges.
- `research/voevodsky/checkers/check_esd7_cofinal_diagonal_convergence_coverage.py`: exact strength of the all-cell convergence attachment.
- `research/nima/esd7-source-manifest.md`: geometric designation is explicit input, not proof of intended analytical designation.

This is source inspection and exact extraction, not a new analytical verification. The search continues the target in `f736-prior-research-binding-search-v1.md`.

## 1. The increments are not three unspecified analytical operations

For cumulative coordinates z=(z1,z2,z3), the source barycentric convention is

    alpha=(z1,z2-z1,z3-z2,7-z3).

A positive increment in cumulative coordinate r therefore moves one barycentric unit from chart r+1 to chart r:

    increment1: 2 -> 1,
    increment2: 3 -> 2,
    increment3: 4 -> 3.

This is a combinatorial chart-direction statement, not identification with semantic operations A,J,P,C,T,E,F.

The actual sorted seven-letter words are:

| vertex | word |
|---|---|
| V104 | 1,1,1,1,2,4,4 |
| V105 | 1,1,1,1,2,3,4 |
| V110 | 1,1,1,1,1,4,4 |
| V111 | 1,1,1,1,1,3,4 |
| V113 | 1,1,1,1,1,2,4 |

All occurrence numbers below are zero based. These retain the same convention as the correlated-word construction.

## 2. E514 is a disjoint-occurrence square

T324 factors E514 as

    V104 --increment3--> V105 --increment1--> V111.

T325 factors it as

    V104 --increment1--> V110 --increment3--> V111.

Increment3 changes occurrence5 from4 to3. Increment1 changes occurrence4 from2 to1. They do NOT apply two different analytical operators to the same occurrence.

Thus the underlying comparison has the diagram

    (chart2 at occurrence4, chart4 at occurrence5)
             |3                         |1
    (chart2, chart3)             (chart1, chart4)
             |1                         |3
                       (chart1, chart3).

For source-chart maps C_ij=S_j R_i on correlated images, both paths have the same component maps C21 at occurrence4 and C43 at occurrence5. This is a disjoint-coordinate naturality square, not a claim that physical cutoff and observer operators commute on one Hilbert factor.

Analytical interpretation must still preserve the shared observer label d and the links between occurrences. Treating the two coordinates as independent observers or independently completed Hilbert factors is not justified.

## 3. The same-occurrence face is the reverse H234 triangle

E539 changes occurrence5 from3 to2. The direct E515 changes occurrence4 from2 to1 and occurrence5 from4 to2. Hence, in geometric orientation:

    E514: (occurrence4 C21, occurrence5 C43),
    E539: (occurrence4 identity, occurrence5 C32),
    E515: (occurrence4 C21, occurrence5 C42).

All other occurrences are unchanged. The only nontrivial same-occurrence triangular comparison is

    C32 C43  ==>  C42,

on occurrence5. Reversing orientation gives

    C34 C23  ==>  C24,

which is the parent H234 type, as found by the retained-word checker. The local H134 labels on T324/T325 identify local omitted-vertex positions; they do not contradict this occurrencewise parent type.

This improves the earlier target: it is not necessary to invent an arbitrary semantic meaning for all three increments before locating the triangle. Their chart directions and actual occurrences are determined by existing data. What remains is the comparison between the parent analytical witness in its own target and this correlated-word/anchored presentation.

## 4. A reversed witness requires more than reversing a scalar residual

The imported analytical source supplies H234 for C34 C23 versus C24 in the signed asymptotic realization category. A reverse-oriented modification for C32 C43 versus C42 can be obtained by taking mates only when the relevant edge equivalences and their units/counits are supplied in that SAME target.

The source-chart profile supplies formal inverses on correlated essential images. This does not by itself identify those formal inverses with inverses of physical cutoff or trace operations. In particular:

- H124 has an inverse in the rapid-decay quotient, not as a finite-cutoff scalar equality;
- a physical scalar trace is not inverted to recover an observer;
- the complete represented observer anchor must be retained;
- the finite analytical remainder is part of the representative even if its asymptotic class vanishes.

Therefore assigning minus the H234 scalar remainder to the geometric triangle without defining the mate and its whiskers would not finish the binding.

## 5. Correction evidence prevents two tempting shortcuts

### Formal subdivision does not establish an unrelated overlay

The Suzuki propagation note now explicitly says its formal implication does not prove that its proposed overlay is the established signed simplex and does not construct canonical fine-stage alignment on all six analytical edges. It requires the parent overlay simplex first.

The same logical discipline applies here: esd7 propagation is available, but its comparison into the retained correlated-word realization must be given, rather than inferred from cell counts or a generic shared face label.

### A Hardy feature is not automatically the conductor tetrahedron

The Hardy-defect correction shows the proposed cross edge would require T M_Theta=D_Theta, which does not follow from contractivity (M_Theta=0 already disproves the implication). Thus the exact eight-leg Hardy feature remains an analytical ingredient, not an automatic identification of each conductor vertex and edge.

## 6. What the convergence attachment really says

The cofinal-diagonal coverage builder attaches one common mode to every incidence record. Its declared mode is a cofinal simultaneous relative limit along an admissible diagonal, with a stationary Hilbert--Schmidt difference row and divergent common-row provenance retained. It explicitly sets all_path_uniform=false.

Its checks establish coverage and boundary-reference counts. They do not compute E514 operators, the disjoint square, or a mate of H234. They also do not prove all-path simultaneous convergence, raw common-row norm convergence, or an ordinary positive Hilbert terminal object.

This limits the use of prior census evidence without dismissing the underlying analytical convergence result.

## 7. Smallest constructive continuation

Use the existing explicit source remainder modification, not a new generic regulator toy.

1. Specify the parent signed analytical target together with its full represented-observer anchor and retained endpoint/placement coordinates.
2. Give a realization comparison into the seven-occurrence correlated/anchored objects for the five words above. Include the links between adjacent occurrences.
3. Transport C21,C43,C32,C42 and their required equivalence data through that comparison. This supplies domains and the mate convention for the reversed H234 witness.
4. Use disjoint-occurrence naturality to identify the T324/T325 factorizations of E514, without commuting a cutoff through an observer on one factor.
5. Whisker the parent H234 mate by the occurrence4 C21 map and unchanged occurrences. Retain the finite remainder, endpoints and both ordered placements under those whiskers.
6. Check that this is the same shared witness in both local presentations; invoke asymptotic/trace-ideal results only with the actual inherited regulator and localized operator hypotheses.

The new concrete reduction is steps3--5: a disjoint-occurrence square plus a specified reverse H234 mate, rather than an undifferentiated local H134 search. This is a conditional construction plan extracted from prior sources and exact incidence data, not a claim that the requested analytical F736 binding has already been completed.
