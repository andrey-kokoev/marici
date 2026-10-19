# The current path machinery completes three rooted spokes

## Constructive result

For three paths AB, AC, AD with a common origin A, the existing inverse/composition laws construct the missing branch edges:

    BC = inverse(AB) followed by AC,
    BD = inverse(AB) followed by AD,
    CD = inverse(AC) followed by AD.

Cancellation constructs the three root-incident faces ABC, ABD and ACD. The already present `MarkedTetrahedronCoherence.unique123` supplies BCD and its tetrahedral coherence filler, keeping all six edges and those three faces fixed.

Thus the current **path completion** produces a complete tetrahedral package: four vertices, six retained edge paths, four face witnesses and a filler. There is no need to supply a leaf rotation or select leaf distances for that constructor.

The original three spokes are preserved definitionally in the completed edge record. The derived branch edges retain their explicit inverse/composite expressions.

## Correct the previous answer

The raw endpoint-continuation matrix of AB,AC,AD is still zero. That reader cannot add branches. But it is not the entire existing completion machinery: the path specialization includes inverses, composition, cancellation and marked horn filling. The earlier suggestion that no existing completion rule can add branch comparisons was too broad.

The constructor does not select a Euclidean metric. A tetrahedral path/coherence package and a regular spatial tetrahedron are different outputs.

## Formal verification

New adapter: `research/strominger/agda/RootedSpokePathCompletion.agda`.
It reuses the existing source theorem rather than adding a postulate.

A deliberate negative module, `SpokeBadDirectedCompletion.agda`, declares only a directed three-star and attempts to provide BC using AB. Agda rejects it. This preserves the actual input distinction: paths have the adopted inverse/composition operations; an arbitrary primitive directed relation need not.

Fresh safe Cubical execution with `--ignore-interfaces` passed the adapter and rejected the negative control. The receipt includes commands, return codes, source/compiler hashes and logs:

`research/strominger/results/rooted_spoke_path_completion.json`.

```sh
python research/strominger/checkers/check_rooted_spoke_path_completion.py
```

The earlier compiler launch mismatch and Windows output-encoding failure were resolved by the matching Agda 2.8.0 executable and `--transliterate`. The final verification reran the entire imported closure rather than relying on the earlier interface files.
