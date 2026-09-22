# Coherent overlap witnesses can miss a higher-arity source obstruction

## Frozen source and cover

Independently declare the source S to be the four even-parity binary triples. Its pieces are restrictions to coordinate pairs {0,1}, {1,2}, {0,2}. A local piece is admitted exactly when it is a restriction of an element of S. Overlap comparisons are literal coordinate equalities.

Every binary pair is locally admitted. Supply (1,1) on each of the three patches. Each has a source lift: respectively 110, 011, and 101. All overlaps agree, with identity witnesses. Their cocycle conditions are strict; the triple intersection of coordinate patches is empty, so its condition is vacuous.

The supplied data force the global triple 111, which violates source parity. No admitted source lifts the family. The witness family is therefore locally admitted and coherent under the frozen overlaps but fails global assembly.

## Exhaustive result

Of 64 families of admitted local pieces, eight satisfy all overlap conditions and only four have global source lifts. The other four are the odd-parity triples. Reversal of coordinate order preserves source parity and the obstruction.

Even- and odd-parity sources have identical restriction images on all seven proper coordinate subsets, including the empty subset. Thus the missing distinction cannot be inferred solely from those local images and their coordinate comparisons. It resides in a ternary source relation. Restoring that relation recovers the source exactly.

## DPC disposition

This refutes the unqualified claim that locally source-realizable pieces and coherent pairwise overlap witnesses always suffice for global assembly. It is an independent finite fixture, not an assertion that the actual coupled protocol has an undeclared parity constraint.

It does not refute a stronger claim whose overlaps retain additional source witnesses and higher compatibility data; that claim must specify those data independently. In particular, choosing the three full local source lifts does not make them one common source witness.

The structural distinction is between coherence of the comparisons that have been retained and completeness of the source constraints they express. Strictly coherent comparisons can coexist with an unrepresented higher-arity obstruction.

This also limits interpreting every failure as a nontrivial homotopy defect of pairwise maps. Here the pairwise maps are identities. The missing datum is source admissibility of the joint configuration.

## Reproduction

    python research/voevodsky/checkers/check_coherent_gluing_obstruction.py

Artifacts:

- `results/coherent-gluing-obstruction-contract.json`
- `results/coherent-gluing-obstruction.json`
