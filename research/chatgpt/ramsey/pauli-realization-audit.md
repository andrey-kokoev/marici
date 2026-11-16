# Ramsey–Pauli realization-cost audit

Exact arithmetic over F₂. Anticommutation is adjacency; commutation is nonadjacency. Each graph is checked for triangle-freeness and absence of an independent s-set. Every Pauli realization is checked against every matrix entry. W denotes XZ.

By Sarkar–Yoder, arXiv:2302.07966v2, Theorem 5.4, the minimum qubits for a **fixed** commutation matrix C are rank_F₂(C)/2. Rank is computed independently of the constructive factorization.

## Catalogue results

| Constraints | Vertices | Catalogue scope | Records | Minimum-qubit histogram | Swapped-relation histogram |
|---|---:|---|---:|---|---|
| (3,4) | 8 | all | 3 | {3: 1, 4: 2} | {3: 2, 4: 1} |
| (3,5) | 13 | all | 1 | {6: 1} | {6: 1} |
| (3,6) | 17 | all | 7 | {7: 2, 8: 5} | {6: 1, 7: 2, 8: 4} |
| (3,7) | 22 | source-listed extremal catalogue | 191 | {8: 2, 9: 13, 10: 115, 11: 61} | {9: 11, 10: 114, 11: 66} |

## R(3,7): edge counts versus register cost

| Edges | Qubits: number of records |
|---:|---|
| 60 | {10: 1} |
| 61 | {9: 2, 10: 2, 11: 2} |
| 62 | {9: 2, 10: 24, 11: 4} |
| 63 | {9: 1, 10: 25, 11: 34} |
| 64 | {9: 3, 10: 36, 11: 20} |
| 65 | {9: 3, 10: 21, 11: 1} |
| 66 | {8: 2, 9: 2, 10: 6} |

## One-edge deletions

Tried 12127 parent/edge pairs; 618 preserve (3,7) avoidance, yielding 618 distinct labelled graph6 records.
Minimum-qubit histogram: **{9: 31, 10: 378, 11: 209}**.
Qubit-cost changes relative to the first encountered parent: **{-1: 153, 0: 287, 1: 178}**.
Identical graph6 records are deduplicated; isomorphic relabellings are not. These are perturbations of the supplied catalogue, not a claim of new isomorphism classes.

## Lowest-cost catalogue records

- A 8-qubit record with degree range 6–6: 0 valid edge deletions; 66 deletions create a commuting seven-set. Explicit witnesses are stored in the JSON.
- A 8-qubit record with degree range 6–6: 0 valid edge deletions; 66 deletions create a commuting seven-set. Explicit witnesses are stored in the JSON.

## Scope and interpretation

- Vertex count, graph edge count, and minimum qubit count are different invariants.
- Complementing the graph swaps the meanings of the two binary outcomes. It preserves the Ramsey avoidance statement with parameters swapped, but need not preserve realization cost.
- Deleting an edge removes an anticommutation requirement **and adds a commutation requirement**. It is not merely dropping a constraint; rank need not be monotone.
- Catalogue completeness/isomorphism classification is attributed to the source, not independently proved here. The source heading says ‘maximal’, but this must not be read as edge-maximal: 18 of 191 records are triangle-free edge-saturated; 173 are not. These are largest-order (22-vertex) examples.
- No new Ramsey upper bound, unrestricted minimum-dimension theorem, or connection to ESD7 geometry is established.

## Reproduce

```sh
python research/chatgpt/ramsey/pauli_realization_audit.py
python -m unittest discover -s tests -p "test_pauli_realization_audit.py"
```

Input graph6 files are cached under `pauli-realization-catalogues/`. Source URLs, SHA-256 hashes, per-record ranks, and explicit minimum-register Pauli strings are in `pauli-realization-audit.json`.

Source catalogue: https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
