---
author: marici.Voevodsky
---

# 4344 — Cross-Edge Coverage Determines Whether Ramsey Neighborhoods Glue

[Entry 4343](20261125-4343%20Missed%20Cuts%20Determine%20Which%20Path%20Branches%20Share%20a%20Next%20Move%20Set.md) classified single next moves on even paths. Here the question is joint: given the two colored neighborhoods of a pivot, what must the edges *between* them do? In the smallest example below, replacing a red path by a cycle leaves both side sizes and both maximum clique sizes unchanged, but reduces the number of gluings from 18 to zero.

## The information omitted by the Ramsey recurrence

To avoid a red triangle and a blue clique of size \(k\), the pivot’s red neighborhood \(A\) must be all blue with \(|A|<k\). Its blue neighborhood \(B\) must have neither a red triangle nor a blue \((k-1)\)-clique. Assume these internal conditions hold. Assign each \(b\in B\) a set \(S_b\subseteq A\) of red cross-neighbors. A gluing exists exactly when the sets can meet two conditions:

1. If \(bb'\) is red, then \(S_b\cap S_{b'}=\varnothing\).
2. For each nonempty blue clique \(Y\subseteq B\),
   \[
   \left|\bigcup_{b\in Y}S_b\right|\ge |A|+|Y|-k+1.
   \]

The first condition excludes every mixed red triangle. For the second, the largest blue clique with \(B\)-part exactly \(Y\) contains all of \(A\) outside the displayed union. Keeping its size below \(k\) gives exactly the inequality. These exhaust the mixed obstructions. The usual size recurrence needs neither test because it reasons about one side at a time; running it backward does not choose the cross-edges.

For \(k=4\) and three labeled vertices in \(A\), let the red graph on \(B\) be the path 1–2–3–4. One assignment is \(S_1=\{a,b\}, S_2=\{c\}, S_3=\{a\}, S_4=\{b\}\). There are 18. Close the path with the red edge 4–1. Each opposite pair in the cycle is blue, so each pair needs two distinct elements of \(A\) in its union. Every edge between the pairs is red, so their unions must be disjoint. Four elements are needed; only three exist. The [split checker](../../research/voevodsky/checkers/ramsey_split_gluing.py) replays all 4,096 labeled cross-edge assignments per graph, comparing the two rules with direct forbidden-clique tests on all eight vertices.

## Consequences for construction

- **Growth preserves local constraints, not a particular witness.** Every blue neighborhood in a \((3,k+1)\) graph is itself a \((3,k)\) graph, and overlaps must agree on labeled edges. Doubling has a direct but non-extremal-in-general construction: two disjoint red copies of a \((3,k)\) witness plus an isolated vertex give \(R(3,2k)\ge2R(3,k)\) when the copies have order \(R(3,k)-1\). All cross-edges here are blue.
- **Freshness belongs to an ordering.** At width 9 the four lexicographically ordered block placements contribute 8, 4, 4, 4 new corners. Taking the first, fourth, second, then third contributes 8, 7, 3, 2 instead. Both cover the same 20 corners. Even the assertion that a fresh piece is a face uses the [specified order](../../research/voevodsky/ramsey-table-cube-differences.md).
- **Forcing is not symmetry.** A fixed list of edge decisions determines every labeled completion exactly when it meets the disagreement set of every pair of completions. A symmetry, by contrast, transports all moves by a single graph automorphism. On the width-12 path the corners `{2,4,7}` and `{2,5,7}` have identical size profiles (313 next moves each). Yet adding the same blue-adjacent vertex with support `{1}` gives nonisomorphic red graphs: the two leaves have distances 2 and 6 from the unique four-cycle in the first graph, versus 3 and 5 in the second.
- **Reuse has a depth.** On the width-8 path, `{1,4,7}` and `{1,4,8}` have exactly the same 55 labeled blue-adjacent next moves. Two further supports, empty and `{1,8}`, separate them when the three newcomers are mutually blue. Core vertices 2, 5, 7 complete a blue six-set only in the second branch. The first test sees independent fours; the second can see independent triples. [Joint replay and explicit witnesses](../../research/voevodsky/results/ramsey_cube_two_exterior.json).
- **Repair must respect shared constraints.** In the stored 52-vertex witness study, supports sharing a red core neighbor cannot be red-adjacent, while supports missing the same independent ten-set cannot be blue-adjacent. [Entry 4342](20261125-4342%20Eight%20Neighborhoods%20Must%20Change%20on%20the%20Nine-Deletion%20Hole%20Cores.md) excluded every pair of retained neighborhoods on 51 selected cores, even with arbitrary changes elsewhere. This lower bound measures how many neighborhoods must change, not how many edge flips suffice.

**Scope.** The gluing criterion decides what constitutes a valid assignment; it does not promise an efficient algorithm for finding one. Neither the split example nor the path replays establish a new Ramsey threshold or an additional exclusion on the 51 cores.

**Durable verification.** Run `python research/voevodsky/checkers/ramsey_split_gluing.py` (expected `18 0`). [One-move domains](../../research/voevodsky/results/ramsey_cube_cut_overlap.json) · [two-move checker](../../research/voevodsky/checkers/ramsey_cube_two_exterior.py). Sequence claim `seqclaim-9991fcd77e04f4f751efe8f8`; admitted proposal `ep_73f6c881-6e16-437e-9232-970f810733c3`; event head `5566e58920a90c4d9e3a79a16c7c1b24b66d74c5cadc384b6d1f4e2a4aa81653`.
