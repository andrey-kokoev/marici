# Ramsey construction from fixed relations: results and research targets

**Finding.** For target (3,7), a six-point incidence system specifies a 22-vertex witness without a catalogue or an offset search. Its labels explain the order 22. It does not explain the upper bound 23. A separate incidence argument excludes 23. No single transport law in this investigation gives both results from the target integers alone.

## 1. Objective and standard of proof

Treat a binary matrix as a description of a fixed relation. A row and a column are two roles of one vertex, not two vertices. Off the diagonal, 1 means red and 0 means blue. A valid (3,k) matrix has no red triangle and no blue clique of size k. A construction at order n proves only that R(3,k) is greater than n.

The construction objective is a rule that can specify new witnesses without consulting a completed graph. The explanation objective is stronger: identify which relations require or forbid a continuation. Search can test a rule or find a counterexample. It cannot by itself show why the carrier supplies that rule. The [Deutsch–Popperian conjecture](deutsch_popperian_conjecture.md) sets a transfer test: state the rule for one target and apply it to another without changing it to fit the answer.

Keep three operations distinct. Transpose reverses the endpoint roles. Complement exchanges the colors. A vertex permutation preserves the graph only if it preserves the entries. In particular, color duality of a Ramsey statement does not imply rotational symmetry of its witnesses.

## 2. Main construction: one point, six singletons, fifteen pairs

Use the ground set X = {0,1,2,3,4,∞}. Rotate the first five elements modulo five and fix ∞. The vertex labels are the empty set, the singletons of X, and the unordered pairs in X. Thus the order is 1 + 6 + 15 = 22. The use of this ground set and these label types is a construction choice, not a consequence of the target integers.

Join the empty label to every singleton. Join a singleton to each pair that contains it. For disjoint pair labels, use the following exception rule. A partition of X into three pairs has one distinguished pair. Omit the edge between the other two. The three rows below, with all five rotations of each row, specify the whole rule:

| Distinguished pair | Other pair | Other pair |
|---|---|---|
| 12 | ∞0 | 34 |
| 13 | ∞0 | 24 |
| ∞0 | 14 | 23 |

Here `12` denotes the unordered pair {1,2}. A partition orbit has one representative with ∞ next to 0. The three rows give exactly the three pairings of the remaining four points. The distinguished pairs run once through pentagon sides, diagonals, and pairs containing ∞. Thus every partition and every distinguished pair occurs exactly once.

**Why it works.** Three mutually disjoint pairs would use all six ground points. The exception rule omits one edge in each such triangle. Other triangle types are excluded by incidence. For independence, the one omission per partition and per complementary four-set bounds a blue set of pair labels by five. Together with the incidence of singletons this bounds every blue set by six; the six singletons attain six. See the [six-edge lemma and proof by vertex type](ramsey_pair_incidence_coherence_22_to_23_2026-11-09.md). The resulting graph is 6-regular with 66 red edges.

[Direct generator](ramsey_37_pair_rotation_rule.py) · [verified matrix](ramsey_3_7_pair_rotation_22.csv). This specializes an existing pair-incidence construction. It is not a claim of a new Ramsey value or a unique choice of witness.

## 3. What rotation and path transport explain

| Setting | Result | Limit |
|---|---|---|
| (3,3), five-cycle | Both colors have a unique continuation if immediate reversal is forbidden. | Counting header paths alone does not exclude larger examples. |
| (3,4), eight-vertex square-frame graph | Two reflections specify an eight-cycle; their half-turn joins opposite vertices. The matching blocks both alternating independent four-sets. | Other eight-vertex witnesses need not have this symmetry. [Offset proof](ramsey_quarter_turn_overlay.py) |
| (3,5), 13-vertex cyclic graph | Each blue triple has two fourth vertices, joined by red. Replacing one with the other excludes any proposed 14th neighborhood by decreasing overlap. | This proves terminality of this graph. The slot permutations describe roles, not automorphisms of the full graph. [Exchange proof](ramsey_exchange_extension_barrier.py) · [role transport](ramsey_blue_four_slot_group.py) |
| (3,6) to (3,7) | A quarter-turn specifies four neighborhoods on a 13-vertex core to give a 17-vertex witness. A different five-vertex attachment gives a 22-vertex witness. | Repeating the four-cycle attachment did not give 22. [Construction and failed transfer](ramsey_quarter_turn_to_bipartite_sector_2026-11-08.md) |

A quotient must retain relative transport. For example, parallel and crossed matches between two reflected pairs are different even though both connect the same base labels. [The half-turn verifier](ramsey_antipodal_obstruction.py) retains mixed selections: a forbidden set can use both copies of some labels and only one copy of others. In one joined-center model a seven-label tree forces an odd sign product on a rectangle. The local argument is short; the proof that a suitable tree exists still uses finite cases. [Tree proof](ramsey_erased_sign_cycle.py) · [matrix deductions](ramsey_tree_propagation.py).

## 4. A second construction method: two cyclic rings

For two copies of Z/n, let A and B be symmetric red offset sets inside the rings. Let D be the offsets from the first ring to the second. A triangle is absent exactly when (A+A) misses A, (B+B) misses B, and (D−D) misses A∪B. For a red-independent set X on the first ring, remove X+D from the second ring. The largest blue set using exactly X there has size |X| plus the independence number of the remaining second-ring graph.

These conditions are exact. The [target-only generator](ramsey_target_two_rings.py) uses them in a finite search. With k=7 it finds 22 vertices. With k=8 it finds 26; equal rings cannot represent the known 27-vertex witness. The three offset sets are outputs of the search, not a closed formula. Keeping previously successful offsets and changing the circumference fails already at k=8. Reducing all offsets modulo the old circumference gives a valid [quotient lift](ramsey_two_ring_transfer_law.py), but that rule still needs the old graph.

## 5. The upper bound is a separate problem

A valid extension column must be a red-independent neighborhood N that meets every old blue (k−1)-set. The extension test is exact, but failure for one seed is not a universal upper bound. On the 191 catalogued (3,7) witnesses, every graph has a starting blue six-set from which some sequence of exchanges reaches a six-set disjoint from each proposed N. The start can be fixed; the route depends on N. Strict overlap decrease suffices in only 52 records. Allowing steps at constant overlap suffices in all 191. [Catalogue audit](ramsey_exchange_monotone.py).

The [rooted incidence reconstruction](R37_Automated_Incidence_Proof.md) reduces a hypothetical 23-vertex counterexample to a six-regular graph. At a vertex, its six neighbors attach to a 16-vertex residual graph H. An independent five-set of H can miss at most one attachment; otherwise two neighbors and that set give an independent seven. If nonnegative weights on the five-sets have total W, and each permitted attachment misses weight at least m, compatibility requires **6m ≤ W**. [Verified signed-pair certificates](ramsey_signed_pair_conservation_2026-11-09.md) violate this bound for all 39 relevant residual graphs. The inequality is uniform. The coefficients are not: each residual has its own certificate. The certificate argument needs the completeness of the residual classification.

## 6. Limits and negative controls

- **The unsigned 3×7 seed:** the unmodified seven nonempty supports have no completion in the tested reflected matching model. One changed mark admits a witness. This is a conditional obstruction, not a proof that every interpretation of the table fails. [Forward seed test](ramsey_forward_marks.py).
- **Spectral data:** a change in odd nullity can rank repairs but cannot certify them. Two moves with the same spectral change can cover different independent sets. [Repair experiment](ramsey_spectral_repair_trial.py).
- **Extension counts:** many valid next columns need not permit another extension. One 24-vertex seed for (3,9) has 103,800 ordered three-column extensions and no four-column extension. [Exact counter](ramsey_24_fourth.py).
- **(3,10):** [Exoo’s 39-vertex matrix](ramsey_3_10_witness_39.csv) has a compact [pentagon description](exoo39_symbolic_relations.py). Its offsets were recovered from the witness. The target-only cyclic search reaches 38 and excludes 39 within that class. [Cyclic test](ramsey_target_only_cyclic.py). Three 13-rings with simultaneous rotation also fail at 39. These exclusions do not resolve the 40-vertex case. The bound used in this investigation is 40 ≤ R(3,10) ≤ 41.

## 7. Further research targets, in priority order

1. **Derive a pairing rule for another target.** State the ground labels, incidence relation, and exception rule before importing a graph. Explain which independent sets the rule controls. Test the same rule at a target other than (3,7). If six-point partitions are essential, state that limit instead of adding a fitted exception.
2. **Explain the offset choice.** Derive A, B, and D from an incidence or arithmetic identity. Prove both difference avoidance and the blue capacity bound. Use k=8 as a transfer test; reproducing a saved k=7 offset table is not sufficient.
3. **Explain constant-overlap steps.** Given N and a blue six-set, identify a relation that selects an exchange or a family of equivalent exchanges. Prove that the rule must eventually reduce overlap. A catalogue search for a route is a check, not the rule.
4. **Derive the residual weights.** Specify one rule on H for signed pair coefficients. Prove nonnegativity on five-sets and a strict margin 6m−W. Test first on the residuals for which nonnegative pair coefficients alone fail. Do not use the existing certificate coefficients as inputs.
5. **Test (3,10) without Exoo’s offsets.** Specify a multi-orbit construction and its transport relations before checking it. A valid 39-vertex output tests transfer. A valid 40-vertex output would settle the threshold at 41; excluding one construction family would not.

**Recommended next step:** explain the three distinguished-pair choices in §2 as an incidence principle that transfers, or prove the proposed principle is specific to six points. This is a smaller and more decisive test than another search at 40 vertices.

## Reproduce the main checks

From the repository root, use Python 3. These commands use the standard library and local modules or catalogues:

```sh
python research/chatgpt/ramsey/ramsey_37_pair_rotation_rule.py
python research/chatgpt/ramsey/ramsey_37_dihedral_rings.py
python research/chatgpt/ramsey/ramsey_target_two_rings.py 7
python research/chatgpt/ramsey/ramsey_exchange_monotone.py
```

The first command regenerates the pair-incidence CSV. The third searches the two-ring class and writes a different CSV. Neither command proves the general upper bound. The reports linked in §5 describe the separate upper-bound checks.
