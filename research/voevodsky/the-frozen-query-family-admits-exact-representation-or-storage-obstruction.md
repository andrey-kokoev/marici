# The frozen query family admits exact representation or storage obstruction

## Source and admission

Use Nima's already declared source/tail zero-frame family: a retained finite set J of queried even coordinates has frames y_n<=0; a read-only query asks whether y_n>=1/2 is compatible. The independently verified owning spike witnesses and Farkas contradictions establish that the query is feasible exactly when n is absent from J.

The existing source state, marked history answer, optimizer, optimum and positive objective certificate remain identical across these refinements. The owning independent verifier runs freshly before the new synthesis test.

## Frozen construction

For a declared finite query set Q with H coordinates, retain the membership mask J intersect Q. A code with H bits answers every declared query. Repeated frames and order have no effect on these queries.

If the offered history-dependent storage budget b is below H, select b+1 queried coordinates and exhibit all subsets of them. There are 2^(b+1) admitted carriers. Any two are separated by a query at a coordinate in their symmetric difference. They cannot fit into 2^b distinguishable retained codes.

All retained information used to recover the answers counts against the budget, as in the owning contract. There is no hidden journal or special per-history program.

## Exact exhaustive test

Freeze all 1,024 query subfamilies of the ten owning coordinates and budgets 0 through 10, before constructing results. The checker exercises 11,264 language/budget combinations:

- 6,144 admit the sufficient membership representation;
- 5,120 have an exact storage obstruction.

It validates 1,048,576 history/query-signature instances and 110,930 separating-difference instances. The xor separator proof covers every pair in each obstruction family. For ten probes and an eight-bit budget, nine of the probes already supply 512 distinct source-backed answer functions, exceeding 256 available codes.

## General restricted-family theorem

For any H distinct admissible even probe coordinates in this zero-frame family, H bits are necessary and sufficient. The analytic spike and Farkas constructions apply to each such coordinate, so the argument extends beyond the tested ten-coordinate horizon. A uniform finite budget for arbitrary finite-support queries is impossible.

Restriction of the query language projects the membership mask. Enlarging it can split existing equivalence classes; the new bits require retained evidence or a new source-authorized input. A finite current certificate does not supply them.

This gives a complete representation-or-obstruction result for this restricted family, rather than a universal decision procedure for arbitrary source languages. Finite descriptions alone do not imply effective finite minimization or decidable representability.

## Structural meaning

A cross-cut representation bound measures the number of distinctions exposed by the declared query language. In this family, the residual space is exactly a Boolean cube of membership distinctions, and its faces are the restricted-language representations. The same source and current objective coexist with arbitrarily large residual cubes when the query language grows.

## Reproduction

    python research/voevodsky/checkers/check_representation_or_obstruction.py

Artifacts:

- `results/representation-or-obstruction-contract.json`
- `results/representation-or-obstruction.json`
