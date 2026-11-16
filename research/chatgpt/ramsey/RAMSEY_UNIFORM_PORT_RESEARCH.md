# Uniform port-circuit capacity: verified reductions

Date: 2026-11-05. All inequalities below are necessary conditions; **none settles** `R(3,10)`, which remains 40 or 41. Claims of mathematical novelty are not made.

## 1. Degree-defect ports

Let `G` be triangle-free with `alpha(G)<=k`. Choose a vertex `v` with degree `d<=k`, put `A=N(v)`, `B=V(G)\N[v]`, and for `b in B` set `P_b=N(b)∩A`. Every independent `T⊆B` satisfies

    |union_{b in T}P_b| + (k-d) >= |T|,    |T|<=k-1.

Conversely these two inequalities for all independent `T`, together with triangle-freeness, are equivalent to `alpha(G)<=k`. Add `k-d` universal *virtual ports*, and truncate the transversal matroid to rank `k-1`. Every circuit of that matroid must contain an edge of `G[B]`, and this condition is equivalent to the two independent-set inequalities. Eligible red edges must join disjoint **real** port sets.

## 2. Two-fiber perfect matching theorem

In a `k`-regular admissible graph with `alpha(G)=k`, each port fiber `Q_a={b:a in P_b}` has exactly `k-1` vertices, hence is a maximum independent set of `H=G[B]`. For two labels `a,b`, write `X=Q_a\Q_b`, `Y=Q_b\Q_a`, `J=Q_a∩Q_b`. The bipartite subgraph of `H` between `X,Y` has a perfect matching: otherwise König's theorem gives an independent set in `X∪Y` larger than `|X|`, which together with `J` exceeds `alpha(H)=k-1`. Thus the **eligible-pair graph**, with pairs `xy` allowed only if `P_x∩P_y=∅`, must itself admit a perfect matching. This uses no choice of red edges.

A check of the 1,967 balanced six-port support patterns from the earlier exhaustive calculation showed that this necessary test excludes 9 patterns which had passed the three-label Hall test (3 with two triple-port vertices, 4 with three, and 2 with four). It is not sufficient for Ramsey admissibility.

## 3. The weighted circuit dual

Let `C` be the circuits of the truncated port matroid and `E0` the eligible exterior red edges. For each circuit give a nonnegative weight `w_C` and for each exterior vertex a nonnegative price `lambda_x`. Assume, for every eligible pair `e=xy`,

    sum_{C:e⊆C} w_C <= lambda_x + lambda_y.

Every admissible red graph then obeys

    sum_C w_C <= sum_x lambda_x*(k-|P_x|).

Proof: choose a red edge in every circuit, sum weighted edge-cover inequalities, and bound the resulting edge coefficient by the endpoint prices. The last step uses `deg_H(x)<=k-|P_x|`. Triangle budgets and individual `e<=1` inequalities can be added to make a stronger dual.

## 4. Exact compact six-port certificate

The 16 supports are:

    {0},{1},{2},{0,1,2},
    {i,j} for i in {0,1,2}, j in {3,4,5},
    {3,4},{3,5},{4,5}.

Every label occurs exactly five times, as required for a hypothetical 6-regular `(3,7;23)` graph. Let `X` be the three singleton-support vertices. Their combined exterior red-degree budget is `3*(6-1)=15`.

* 9 circuits of the form `{ {i},{i,j},{i,l},{j,l} }` force the 9 distinct edges from `{i}` to `{j,l}`, with `i in {0,1,2}` and `{j,l}⊆{3,4,5}`.
* 9 circuits of the form `{ {i},{0,j},{1,j},{2,j},{0,1,2} }` each require one of two further red edges from `{i}` to `{i',j}` with `i' != i`; the nine candidate-edge groups are pairwise disjoint and disjoint from the first nine edges.
* The circuit `{ {0},{1},{2},{0,1,2} }` requires an edge among the three singleton vertices. That edge consumes two degrees in `X`.

Therefore `sum_{x in X} deg_H(x) >= 9+9+2=20 > 15`. No triangle-freeness of `H` is used beyond the port disjointness restriction already inherited from `G`.

This is an **exact integer dual certificate**. The supplied Python script verifies all 19 circuits, their minimal Hall dependence, edge sets, dual coefficients and degree contradiction without a SAT solver.

### Uniform three-singleton fan inequality

Suppose a `k`-port system has three singleton supports `{0},{1},{2}`, a support `{0,1,2}`, all three mixed supports `{i,j}` for each `i in {0,1,2}` and each of `r` other labels `j`, and a support `{j,l}` for every pair of those `r` labels. Then the same disjoint circuit classes imply

    3*binom(r,2) + 3*r + 2 <= 3*(k-1).

If this is violated, the whole port pattern is impossible. For `k=9`, `r>=4` is excluded, independently of all remaining port supports. It does not exclude every nine-port design.

## 5. A universal two-neighborhood/codegree bound

More generally, if `G` has `n` vertices and `alpha(G)<=k`, let `v` have degree `d`, let `b` be nonadjacent to `v`, and put `p=|N(v)∩N(b)|`. The common non-neighbors outside the closed neighborhoods of both `v` and `b` form a graph with independence number at most `k-2`, hence have at most `R(3,k-1)-1` vertices. The exact number of such common non-neighbors is `n-d-deg(b)-2+p`. (The two closed neighborhoods overlap in exactly `p` vertices.)

Therefore

    p <= R(3,k-1)+deg(v)+deg(b)+1-n.

In particular, using `deg(b)<=k` gives the weaker one-sided estimate `p <= R(3,k-1)+deg(v)+k+1-n`.

This is a necessary size/codegree inequality at **every vertex**, not only at saturated vertices.

For a hypothetical triangle-free 40-vertex graph with `alpha(G)<=9`, using `R(3,8)=28`,

    |N(v)∩N(b)| <= deg(v)+deg(b)-11 <= deg(v)-2

for every nonedge `vb`. Thus any two vertices of degree at most five must be adjacent, and at most two such vertices can exist in a triangle-free candidate. At a degree-nine center, every exterior port support has size at most seven. If its size is seven, its exterior degree is exactly two and that vertex is itself degree nine.

## 6. A rigid seven-port contact in the 9-regular case

Suppose moreover that the 40-vertex graph is 9-regular. For a degree-nine center `v`, `A` has 9 vertices, `B` has 30, `H=G[B]` has 99 edges, and each port fiber has size eight. For an exterior vertex `b` with `p=7`, let `C=N_H(b)`, `R=B\N_H[b]`. The codegree bound forces `|C|=2`, `|R|=27`, `alpha(R)=7`. Every neighbor `c in C` has support in the two labels outside `P_b`, so `deg_H(c)>=7`.

The published value `e(3,8,27)=85` implies

    99 = e(R)+sum_{c in C}deg_H(c) >= 85+7+7 = 99.

Hence equality holds everywhere: `e(R)=85` and both neighbors have **exactly** the complementary two-port support. The residual is one of the four minimum-edge `(3,8;27)` graphs. This is a necessary rigidity statement, **not** an exclusion of the 9-regular 40-vertex case.

References: Goedgebeur and Radziszowski (2013), *New Computational Upper Bounds for Ramsey Numbers R(3,k)*; McKay's Ramsey graph catalogue; House of Graphs minimal Ramsey data; Angeltveit (2025), *R(3,10) <= 41*.

## 7. Reproduction

Run:

    python ramsey_uniform_port_certificate.py

It checks the exact rational circuit contradiction, the fan arithmetic and the 40-vertex contact equality. The broader 1,967-pattern matching audit also needs `port_pair_matching_audit.py` and `ramsey_port_circuit_proof.py` from the existing research project.
