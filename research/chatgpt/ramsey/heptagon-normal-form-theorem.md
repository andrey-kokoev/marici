# A computer-assisted normal-form theorem for parity-closed heptagons

## Result

Let G be a simple graph on **22 vertices**, with

1. no triangle;
2. no independent seven-set; and
3. an induced seven-cycle S such that every vertex has an even number of neighbors in S.

Then **G is 6-regular and its adjacency matrix over F₂ has rank 16**. Consequently its minimum Pauli realization uses **exactly eight qubits**. Moreover, G belongs to one of **two isomorphism classes**, specified by the accompanying finite certificates. Each has four parity-closed induced seven-cycles.

**Proof status:** computer-assisted finite proof, using a mathematical reduction to CNF, independently checked DRAT refutations, and exact algebraic certificates. This is not a short human-only proof or a proof-assistant formalization. No claim of novelty is made.

The core proof does **not** read the 191-graph catalogue and does **not** assume any previously known Ramsey number. Earlier strengthened probes used R(3,4)=9 and R(3,6)=18, but those cuts were removed from both final core computations.

## 1. An elementary reduction

Triangle-freeness makes every neighborhood independent, so every vertex has degree at most six. For a vertex outside S, its neighbors on S are independent and have even cardinality. Since α(C7)=3, the possible neighborhoods are exactly the empty set or a nonadjacent pair of cycle vertices.

If z outside vertices have empty neighborhood on S, counting cross-edges gives

    2(15−z) = Σ_{v∈S}(deg(v)−2) ≤ 28.

Thus z≥1. Label S cyclically by 0,...,6. Sort the outside vertices by their neighborhood type, with the empty type first. Fixing vertex 7 to have empty type loses no graph.

The SAT encoding includes precisely:

- the fixed induced C7;
- a negative three-edge clause for each possible triangle;
- a positive 21-edge clause for each possible independent seven-set;
- exactly one of the fifteen allowed cycle-neighborhood types at each outside vertex;
- degree at most six, a redundant consequence of the original hypotheses;
- sorting of the outside types;
- lex-leader comparisons within equal-type blocks.

### Why the lex symmetry reduction is safe

Within an equal-type block, permute the outside vertices and choose a labeling with the lexicographically least upper-triangle adjacency string. Swapping two adjacent vertices in that block cannot decrease this string. This gives the encoded lexicographic comparison of their adjacency rows, omitting the two swapped positions. Cycle incidences agree within a type, so they can be omitted from the comparison. Every graph therefore has a labeling satisfying the comparisons.

The encoding implements these conditional comparisons with auxiliary prefix variables. It does not assume that this symmetry reduction produces a unique labeling.

## 2. The attachment pattern is forced

Up to rotation and reflection of the distinguished cycle, there is **one** surviving outside-neighborhood multiplicity pattern:

| Number of outside vertices with this neighborhood | Neighborhoods on C7 |
|---:|---|
| 1 | empty |
| 2 each | {0,5}, {1,4}, {2,6}, {3,6} |
| 1 each | {0,3}, {0,4}, {1,3}, {1,5}, {2,4}, {2,5} |
| 0 | {0,2}, {1,6}, {3,5}, {4,6} |

There are seven distinct rotations/reflections of this multiplicity vector. The `other-profile` formula excludes all seven. It is **UNSAT**.

This exclusion was checked independently, not accepted merely from the SAT solver:

- CNF: **2,450 variables, 101,992 clauses**;
- CaDiCaL 1.9.5 via python-sat 1.9.dev22 produced the DRAT proof;
- dratify 0.1.11 checked **1,965,698 proof steps**, deriving the empty clause;
- receipt: `heptagon-other-profile-lex-cadical-probe.json`.

Hence there is exactly one vertex missing the cycle, and every cycle vertex has degree six. The remaining edges are not yet assumed fixed.

## 3. Only four labeled completions remain

Fix the canonical pattern above and retain the same Ramsey constraints and safe symmetry reduction. Enumerating **edge assignments**, rather than auxiliary SAT assignments, produces four completions.

A fresh solver invocation takes the original fixed-profile formula plus four clauses blocking those complete edge assignments. Its independently checked UNSAT proof establishes exhaustion:

- CNF with blockers: **102,004 clauses**;
- independent checker: **6,093 proof steps**;
- receipt and all four graphs: `heptagon-profile-completions.json`.

No rank bound or regularity assumption was imposed on the completions. Each independently passes triangle-freeness and independent-set checks; each is 6-regular and has four parity-closed induced seven-cycles.

Explicit vertex bijections partition the four labeled completions into two isomorphism classes. Their binary-kernel weight enumerators differ, ruling out an isomorphism even if it moves the distinguished cycle to another cycle. These witnesses are in `heptagon-completion-classification.json`.

## 4. The algebraic compression is certified

For each completion the packet gives:

- six explicitly listed, independent even-neighborhood supports;
- a nonsingular principal 16×16 adjacency submatrix;
- a checked eight-qubit Pauli realization.

The six supports give nullity at least six, hence rank at most 22−6=16. The principal minor gives rank at least 16. These two bounds certify equality without relying solely on a full-matrix rank calculation.

The tests independently verify support independence by enumerating their 64 subset sums and verify the principal minor's independence through its 65,536 subset sums. All Pauli pairings are checked directly from the saved strings.

## 5. A more concrete mechanism: a single square switch

Representatives of the two classes can be chosen to differ by just one degree-preserving two-edge switch. In the canonical labels of the saved packet, change

    remove: {10,19}, {14,21}
    add:    {10,21}, {14,19}.

The vertices are all outside the distinguished heptagon. Both sides preserve Ramsey avoidance and the eight-qubit cost. Their kernel spaces share **five independent relations**; the sixth relation changes. Explicit supports for the five shared relations and each alternative sixth relation are saved with the switch certificate.

Thus the conclusion is more specific than “these matrices happen to have low rank”: Ramsey avoidance plus the parity-closed heptagon forces a rigid incidence pattern, and the surviving nonisomorphic possibilities differ by a single switch that changes a relation but not the six-dimensional dependency space's dimension.

The four canonical completions also share the same four heptagon supports. Their three independent cycle relations plus the all-vertices relation give four common dependencies. The remaining relations are checked explicitly; this argument still uses the finite completion proof, not a new purely local derivation of those identities.

## Scope and trust boundary

- This establishes the **exact 22-vertex conditional claim**, not merely a statement about supplied catalogue records.
- The 21-vertex circulant counterexample remains valid: parity closure and regularity alone do not force eight qubits. Exact order is essential.
- The proof is finite and computer-assisted. The semantic reduction, correctness of cardinality encoding, and symmetry argument remain outside a proof assistant. An independent checker verifies the DRAT traces against the exact generated CNFs.
- The Rust frontend has positive and negative fixtures, including rejection of a false empty-clause proof and rejection of a proof lacking an empty clause.
- The result is not a proof of the unrestricted Ramsey upper bound R(3,7)≤23: it assumes the parity-closed heptagon.

## Follow-up: growth requires repair

`ramsey-extension-repair.md` gives the subsequent construction analysis. The 21-vertex circulant admits 24,476 Ramsey-valid deletion configurations, but none enables a one-vertex extension. Allowing old-edge additions as well gives an optimal eleven-change repair to 22 vertices; preserving 6-regularity requires thirteen. The analysis provides an exact independent-set blocker criterion, explicit safe edit paths, and independently checked lower-bound proofs. Those repair minima are specific to that starting graph, not universal consequences of this normal-form theorem.

## Reproduction

Core computation (no earlier Ramsey bounds or catalogue needed):

```sh
uv run --with python-sat==1.9.dev22 -- python research/chatgpt/ramsey/heptagon_forcing_probe.py --mode other-profile --lex --solver cadical195 --conflicts 1000000
uv run --with python-sat==1.9.dev22 -- python research/chatgpt/ramsey/heptagon_profile_completions.py
cargo build --release --manifest-path research/chatgpt/ramsey/drat-checker/Cargo.toml
python research/chatgpt/ramsey/verify_heptagon_proof.py research/chatgpt/ramsey/heptagon-other-profile-lex-cadical-probe.json research/chatgpt/ramsey/heptagon-profile-completions.json
python research/chatgpt/ramsey/heptagon_completion_classification.py
uv run --with python-sat==1.9.dev22 -- python -m unittest discover -s tests -p "test_heptagon*py"
python -m unittest discover -s tests -p "test_pauli_*py"
```

Conflict-budget exhaustion is recorded as UNKNOWN, never UNSAT. A run that exhausts its budget must be rerun with a larger budget before making a conclusion.

Large CNF/DRAT files are local replay artifacts under the ignored `results/heptagon-proofs/` directory. The compact JSON receipts bind them by SHA-256 to the checker output and checker executable/source/lockfile. `Cargo.lock` pins the independent checker dependency. Regenerating SAT outputs resets their checked status until the independent checker is rerun.
