# Ramsey growth as an extension-and-repair problem

## Results at a glance

For the 21-vertex circulant G with jumps ±1, ±4, ±6:

1. **Deletion alone cannot enable growth**, however many edges are deleted while preserving Ramsey avoidance.
2. There are nevertheless **24,476 valid labeled deletion configurations**, characterized by a simple cyclic conflict rule.
3. A 22-vertex Ramsey graph is reachable by **11 old-edge changes**: eight deletions and three additions, followed by attaching the new vertex. Every intermediate 21-vertex graph preserves avoidance.
4. **Eleven is minimal**, even allowing arbitrary 22-vertex destinations and not requiring the intermediate edits to preserve avoidance. A separately checked UNSAT certificate excludes ten or fewer changes.
5. If the destination must remain **6-regular**, the minimum rises to **13 old-edge changes**. Both bounds have explicit constructive paths and independently checked lower-bound certificates.

These numerical minima concern this particular starting graph. They are not universal Ramsey edit costs. The general result is the extension-and-repair criterion below.

**Metric:** an old-edge change toggles adjacency between two of the original 21 vertices. Incidences of the new vertex are not included in this edit count. The displayed constructions each add six such incidences.

## 1. The general extension law

Assume H is triangle-free and has no independent s-set. Adding a new vertex with neighborhood N preserves these properties exactly when

- N is independent in H; and
- N meets every independent (s−1)-set of H.

The first condition prevents a triangle through the new vertex. The second prevents an independent s-set containing it. All forbidden configurations not containing it were already excluded in H.

This separates local compatibility from global coverage. Having vertices of spare degree does not guarantee a neighborhood satisfying both.

### The repair version

Start with a graph G, delete a set D of old edges, and write H0=G−D. Choose added old edges P and a proposed new neighborhood N. Let H=H0+P. Define

    F_old = all independent s-sets of H0,
    F_new = all independent (s−1)-sets of H0 disjoint from N.

The repaired extension is Ramsey-valid exactly when:

1. H is triangle-free;
2. N is independent in H; and
3. every member of F_old ∪ F_new contains both endpoints of some edge of P.

**Proof:** adding edges cannot create independent sets. An independent set of H0 survives in H exactly when it contains no added edge. Condition 3 therefore removes precisely the old and new-vertex independent-set obstructions. Conditions 1–2 exclude the two possible kinds of triangle.

This is a constrained edge-covering problem on dangerous independent sets. It handles simultaneous repairs too: H0 need not itself be Ramsey-valid. In the explicit optimal construction below it is valid, so F_old is empty and only seventeen new-vertex blockers need covering.

## 2. A frozen-core obstruction to deletion-only growth

Call an edge frozen when deleting it creates an independent seven-set. Further deletions cannot destroy that set. Consequently every Ramsey-valid deletion-only modification must retain all frozen edges.

For G:

- the 42 edges of cyclic differences ±4 and ±6 are frozen;
- the 21 edges of cyclic difference ±1 are individually deletable.

Let F be the frozen core, containing just the ±4 and ±6 edges. Any neighborhood used after deletion-only repair must be independent in F and have at most six vertices. It must also meet every independent six-set of the original G, since deleting edges preserves those sets.

The original graph has 112 independent six-sets. Exhaustive finite certificates check **all 4,572 independent subsets of F of size at most six**. Every candidate misses an original independent six-set. In fact:

| Candidate neighborhood size | Minimum number of missed original six-sets |
|---:|---:|
| 0 | 112 |
| 1 | 80 |
| 2 | 48 |
| 3 | 29 |
| 4 | 16 |
| 5 | 7 |
| 6 | 2 |

Thus no deletion-only repair can enable the extension. The JSON gives a disjoint original independent six-set for every candidate, and the tests independently enumerate the complete candidate family.

This obstruction survives after degree-six saturation has been relieved: it is not just a degree-count argument.

## 3. Safe deletions themselves have a simple geometry

Label the flexible cycle edges by e_i={i,i+1}, with indices modulo 21. A subset D of these edges preserves Ramsey avoidance **if and only if**

    D never contains both e_i and e_(i+10).

The conflict graph on the deletion choices is a 21-cycle, because gcd(10,21)=1. Therefore the valid deletion configurations are exactly its independent sets: **24,476 configurations**, with at most ten deleted edges.

The certificate for this equivalence is small compared with enumerating graph completions:

- the frozen core has exactly 210 independent seven-sets;
- every such set requires deletion of at least one conflicting edge pair;
- each of the 21 conflicting pairs itself suffices to expose an independent seven-set.

For example, deleting e_0 and e_10 exposes {0,1,3,8,10,11,13}; rotations supply the other twenty pair witnesses. Exhaustive verification of the 210 core seven-sets supplies the converse. This is a finite certified characterization, not a claimed human-only derivation of the converse.

**Important distinction:** there are thousands of ways to make the graph sparser without breaking avoidance, yet none makes it extendable by deletion alone.

## 4. An optimal constructive repair

All vertex labels here are zero-based. Start with G on 0,...,20.

### Delete eight old edges

    {0,20}, {2,3}, {3,4}, {4,5},
    {6,7}, {7,8}, {8,9}, {11,12}.

These deletions obey the cyclic conflict rule, so they can be performed in any order while preserving avoidance.

### Add three old edges

    {3,6}, {3,8}, {5,8}.

These can then be added in the displayed order. Every intermediate graph is triangle-free and has no independent seven-set.

### Attach vertex 21 to

    N={0,2,9,11,12,20}.

After the deletion stage, N is independent but misses seventeen independent six-sets. The repair edges eliminate them as follows:

| Stage | Remaining six-sets disjoint from N |
|---|---:|
| After the eight deletions | 17 |
| Add {3,6} | 10 |
| Add {3,8} | 4 |
| Add {5,8} | 0 |

The packet lists all seventeen sets and the repair edges contained in each. Since adding edges cannot create new independent sets, the three-edge covering certificate and triangle checks suffice to justify the final extension.

### What the construction trades

The resulting 22-vertex graph has two degree-four vertices, 4 and 7, and twenty degree-six vertices. Its binary adjacency rank is 18, so it still fits in **nine qubits**, just like the starting graph. It has no parity-closed induced seven-cycle.

The repair therefore grows the graph by allowing an uneven degree distribution and eliminating specific independent-set obstructions. It does not preserve the seven-cycle mechanism responsible for the separate eight-qubit classification.

## 5. Why eleven changes are optimal

A CNF encodes every possible final graph on the old 21 labeled vertices plus the new vertex, requiring:

- triangle-freeness and no independent seven-set;
- degree at most six, a redundant consequence of those conditions;
- at most ten old-edge differences from G.

The only symmetry reduction says: if the new vertex has a neighbor, rotate the circulant so that 0 is a neighbor. The encoding explicitly retains the isolated-new-vertex case, so this reduction needs no assumed Ramsey number or degree lower bound.

The formula is UNSAT. An independent checker verified:

- **180,452 input clauses**;
- **2,726,402 DRAT proof steps**;
- receipt: `ramsey-unrestricted-repair-10.json`.

Together with the eleven-change path, this proves the exact minimum under the stated edit metric. No catalogue or prescribed destination is used.

## 6. Keeping regularity costs more

For a 6-regular destination, let a and d count added and deleted old edges. The initial graph has 63 edges. The destination has 66, six incident to the new vertex, so

    63−d+a=60, hence d=a+3,
    old-edge changes = a+d = 2a+3.

A separate CNF excludes every 6-regular destination with a≤4. Its UNSAT proof was independently checked against **181,288 clauses**, using **750,869 proof steps**. Receipt: `ramsey-regular-repair-4-addition-at-most.json`.

A saved witness uses a=5 and d=8, hence thirteen old-edge changes. A sequence of thirteen single-edge changes preserves avoidance throughout before the new vertex is attached. The endpoint has binary rank 20 (ten qubits). The lower bound is on regular growth, not on the qubit cost of all optimal regular destinations.

## What this contributes toward a construction theory

The reusable mechanism is:

1. **Identify frozen relations:** deletion witnesses reveal which edges cannot be removed in isolation or by deletion alone.
2. **Characterize compatible deletions:** here they form the independent sets of a simple conflict cycle.
3. **Choose a prospective neighborhood and list its blockers:** independent six-sets it misses.
4. **Repair by covering those blockers with admissible edges**, while checking triangles and retaining independence of the proposed neighborhood.
5. Attach the new vertex only after both compatibility and coverage hold.

This is more informative than counting available degrees or computing binary rank. Degree headroom is local; growth depends on the incidence structure of independent sets. Binary rank measures the cost of representing the resulting relations, not whether the construction can grow.

The next generalization would be to find graph families whose frozen cores and blocker hypergraphs admit similarly compact descriptions. Nothing here establishes that all Ramsey constructions have such a description.

## Reproduce and audit

```sh
# Constructive and deletion certificates: standard library only.
python research/chatgpt/ramsey/ramsey_extension_repair.py

# Generate the lower-bound proofs and upper-bound examples.
uv run --with python-sat==1.9.dev22 -- python research/chatgpt/ramsey/ramsey_unrestricted_repair_search.py --budget 10
uv run --with python-sat==1.9.dev22 -- python research/chatgpt/ramsey/ramsey_unrestricted_repair_search.py --budget 11
uv run --with python-sat==1.9.dev22 -- python research/chatgpt/ramsey/ramsey_regular_repair_search.py --additions 4 --at-most
uv run --with python-sat==1.9.dev22 -- python research/chatgpt/ramsey/ramsey_regular_repair_search.py --additions 5
cargo build --release --manifest-path research/chatgpt/ramsey/drat-checker/Cargo.toml
python research/chatgpt/ramsey/verify_heptagon_proof.py research/chatgpt/ramsey/ramsey-unrestricted-repair-10.json research/chatgpt/ramsey/ramsey-regular-repair-4-addition-at-most.json
python research/chatgpt/ramsey/ramsey_extension_repair.py
uv run --with python-sat==1.9.dev22 -- python -m unittest discover -s tests -p "test_ramsey_extension_repair.py"
```

SAT witnesses are not unique. The displayed labels and stage counts refer to the saved witness; replay asserts those particular structural properties rather than silently treating an arbitrary new solver witness as the same construction. Conflict-budget exhaustion is UNKNOWN, not a lower-bound proof.

Compact packets are in `ramsey-extension-repair.json` and the search/verification receipts. Large CNF/DRAT files live in the ignored `results/ramsey-repair-proofs/` directory. The independently checked traces establish UNSAT of exact CNFs; the mathematical interpretation of the encoding remains outside a proof assistant. No new unrestricted Ramsey-number bound or novelty claim is made.
