# Symbolic proofs for the three four-label Ramsey support exceptions

These are conditional consequences of the support-pattern reduction for a hypothetical 23-vertex red graph with no triangle and no independent seven-set. They do not independently enumerate the possible attachment support patterns. In particular, the complete catalog-free upper-bound argument also uses the smaller bounds `R(3,5)=14`, `R(3,6)=18`, `e(3,6,17)>=40` and the exhaustiveness of the 694 support-multiset orbits.

## General support calculus

Assume a red graph `G` is 6-regular, triangle-free, and has independence number at most 6. Choose `v` and let `A=N(v)` have six vertices, labeled `0,...,5`. Write `B=V(G)\(A∪{v})` and label its sixteen vertices `b_0,...,b_15`. Define `T_i=N(b_i)∩A`, and let `x_ij` be 1 if `b_ib_j` is red, and 0 otherwise.

Three necessary rules hold.

1. **Incompatibility:** `x_ij=0` whenever `T_i∩T_j` is nonempty; otherwise `A` would witness a red triangle.
2. **Degree:** `sum_j x_ij=6-|T_i|`.
3. **Hit:** If `F⊆{0,...,15}` and `J=⋃_{i∈F}T_i` satisfy `|F|=|J|+1`, then `sum_{i<j in F; T_i∩T_j=∅}x_ij≥1`. Otherwise `{b_i:i∈F}∪(A\J)` is an independent seven-set.

Additionally no three edge variables of one triangle may simultaneously be 1. All witnesses used below have `|J|≤4`.

Support lists give `T_0,...,T_15`, in that order; for example `04` means `{0,4}`. The labels on edges such as `7-11` refer to **B vertices**, not attachment labels in A.

### Case 249 (t=3): forced triangle `(b_1,b_2,b_14)`

Supports: `0, 1, 2, 3, 4, 04, 05, 12, 15, 23, 24, 35, 45, 012, 034, 135`.

The hit rule forces these five edges; each witness has precisely one eligible pair:

| Hit witness `F` | Forced edge |
|---|---|
| `{1,2,7}` | `1-2` |
| `{2,3,9}` | `2-3` |
| `{0,4,5}` | `0-4` |
| `{2,4,10}` | `2-4` |
| `{4,5,6,12}` | `4-6` |

The remaining deductions consist of three branches, where `1` denotes red and `0` denotes blue.

- From `0-4=2-4=1`, triangle-freeness gives `0-2=0`. Applying the hit rule to `F={0,2,7,13}` forces `0-7=1`.
- From `2-3=2-4=1`, deduce `3-4=0`. The hit on `{3,4,5,14}` forces `3-5=1`, so `2-5=0`; the hit on `{2,5,7,10,13}` forces `5-7=1`, so `3-7=0`; the hit on `{3,7,9,11,15}` forces `7-11=1`.
- From `2-4=4-6=1`, deduce `2-6=0`. From `1-2=2-3=1`, deduce `1-3=0`; the hit on `{1,3,8,15}` forces `3-8=1`, hence `2-8=0`. The hit on `{2,6,7,8,13}` now forces `6-7=1`.

The four edges `0-7`, `5-7`, `6-7`, `7-11` are red. Since `b_7` has prescribed internal degree `6-|T_7|=4`, we obtain `7-14=0`.

Vertex `b_14` has support `034`, hence exactly four eligible neighbors in B: `1,2,7,8`. Its degree is `6-3=3`, and `7-14=0` forces `1-14=2-14=8-14=1`. Together with `1-2=1` this produces a red triangle. Contradiction.

### Case 303 (t=4): degree saturation forces triangle `(b_0,b_1,b_15)`

Supports: `0, 1, 2, 3, 4, 5, 04, 13, 15, 23, 25, 45, 012, 013, 024, 345`.

These five hit witnesses each force the indicated red edge:

| Hit witness `F` | Forced edge |
|---|---|
| `{1,3,7}` | `1-3` |
| `{2,3,9}` | `2-3` |
| `{1,7,9,12,13}` | `1-9` |
| `{1,5,8}` | `1-5` |
| `{2,5,10}` | `2-5` |

Triangle-freeness gives `1-2=5-9=3-5=0`. The hit on `{3,5,9,10}` then forces `3-10=1`; triangle avoidance with `1-3=1` gives `1-10=0`. The hit on `{1,2,8,10}` forces `2-8=1`.

Two more hit inequalities remain (the pair notation denotes the **sum** of their variables):

    x_(2,4)+x_(2,6) >= 1       [F={2,4,6,14}]
    x_(2,7)+x_(2,13) >= 1      [F={2,7,9,12,13}]

The three already-red edges incident to `b_2` are `2-3`, `2-5`, and `2-8`. The two displayed edge groups are disjoint from them and from each other. Thus `b_2` has at least five red edges, exactly its prescribed degree; every remaining incident edge is blue. In particular `0-2=2-15=0`.

Because `1-2=0`, the hit on `{0,1,2,12}` now forces `0-1=1`. Vertex `b_15` has support `345`, degree 3, and exactly four eligible neighbors `0,1,2,12`. Since `2-15=0`, it must connect by red edges to `0,1,12`. Hence `0-1`, `0-15`, `1-15` form a red triangle. Contradiction.

### Case 397 (t=4): edge-packing/degree-cut obstruction

Supports: `0, 1, 2, 3, 4, 5, 03, 12, 15, 23, 34, 45, 012, 013, 045, 245`.

Partition B into

    P = {0,1,2,3,6,7,9,12,13},
    Q = {4,5,8,10,11,14,15}.

The degree sums are `38` on P and `28` on Q, so the handshake identity is

    e(P)-e(Q)=(38-28)/2=5.

Only four pairs in Q have disjoint supports: `4-5`, `4-8`, `5-10`, `8-10`. Thus `e(Q)≤4` and `e(P)≤9`.

Now apply the hit condition to ten subsets F of P. Each row has `|F|=1+|⋃_{i∈F}T_i|`, so at least one of the eligible pairs shown must be red:

| F | Eligible red pairs within F |
|---|---|
| `{1,2,7}` | `1-2` |
| `{0,2,7,12}` | `0-2`, `0-7` |
| `{0,3,6}` | `0-3` |
| `{0,1,6,13}` | `0-1`, `1-6` |
| `{2,3,9}` | `2-3` |
| `{1,3,7,9}` | `1-3`, `1-9`, `3-7` |
| `{0,6,9,12,13}` | `0-9` |
| `{2,6,9,12,13}` | `2-6`, `2-13` |
| `{3,6,9,12,13}` | `3-12` |
| `{6,7,9,12,13}` | `6-7` |

All eligible-pair sets in the right column are disjoint, so **ten distinct red edges** are necessary inside P. Hence `10≤e(P)≤9`, contradiction.

## General edge-packing inequality

For any graph with a prescribed degree vector and a partition `P⊔Q`, suppose q is an upper bound on the number of edges internal to Q, and k hit constraints force edges in P from pairwise-disjoint admissible edge sets. Then

    k ≤ q + (sum_{v∈P}d(v)-sum_{v∈Q}d(v))/2.

This is just the handshake identity plus edge packing. Case 397 violates it by exactly one edge. Cases 249 and 303 are instead resolved by repeated application of the hit, triangle and degree rules.

## Reproducibility and scope

Run `python ramsey_r37_three_symbolic_proofs.py` to check all support lists and every claimed inference using exact Boolean assertions. The program does not load a Ramsey graph catalog, invoke a solver, or read JSON certificates.

These **three exceptions** are now described symbolically; the proof that the support-class enumeration is exhaustive remains a separate finite computation. The four-label statements do not constitute a universal fourth-coherence law and are not consequences of Stokes' theorem.

## One additional general forbidden-support lemma: red-square obstruction

**Lemma (cross-rectangle).** Let `A` be an independent set of size `s≥5` in a triangle-free red graph with `alpha(G)≤s`. For five distinct labels `p,i,j,k,l` of `A`, assume that the graph has **distinct** vertices outside `A` with supports exactly

    p, i, j, k, l,
    ik, il, jk, jl,
    pij, pkl.

Then these eleven support types are impossible.

**Proof.** Each pair support `ik`, `il`, `jk`, `jl`, along with its two singleton vertices, forces a red edge between those singleton vertices. Hence the four vertices for `i,j,k,l` form a red `K_{2,2}` between `{i,j}` and `{k,l}`. Triangle-freeness makes both internal edges `ij` and `kl` blue. The independent-set hit for the vertices with supports `p,i,j,pij` forces `x_{p,i}+x_{p,j}≥1`. Similarly the hit for `p,k,l,pkl` forces `x_{p,k}+x_{p,l}≥1`. The pivot singleton vertex `p` therefore has red neighbors on both sides of the red `K_{2,2}`. Those neighbors are red-adjacent; together with `p` they form a red triangle. QED.

The lemma invokes only hit constraints involving **two or three attachment labels per witness**, though the motif itself has five distinct labels. It does not require degree regularity.

### Complete audit after adding this lemma

I reran the exact support enumeration, this time replacing **every** numerical LP test and every Farkas multiplier by Boolean bound propagation of the preceding rules. With at most four attachment labels in each hit constraint:

| Method | Support patterns excluded |
|---|---:|
| Immediate degree-capacity or forced-independent-set contradiction | 1,322 |
| Bound propagation using hit constraints, triangle inequalities, degree equalities, and `0≤x≤1` | 638 |
| Cross-rectangle lemma | 1 |
| **Total** | **1,961** |

The only case that survives propagation is `t=4`, pattern index 203, with supports

    0,1,2,3,4,5,14,15,24,25,34,35,012,013,023,045.

It contains the cross-rectangle motif with `p=0`, sides `{1,2}` and `{4,5}`. The motif excludes this final case.

The script `ramsey_r37_symbolic_exhaustion.py` independently regenerates all 1,961 attachment-support patterns, generates all necessary local constraints, performs sound 0/1 bound propagation, and checks this final motif. **It is self-contained and uses only Python's standard library.** It was also cross-checked, pattern by pattern and constraint by constraint, against the earlier independent exact-arithmetic inequality generator.

### Scope of the result

The exhaustive support-pattern reduction remains finite and computational, not a universal symbolic theorem. The graph-independent *lemmas* here are the hit rule, forced-edge/degree rules, edge-packing inequality, and red-square lemma. The classification-free computation uses no Ramsey graph catalog, numerical LP solver, or Farkas proof object, but still enumerates the 1,961 attachment-support patterns. It depends on the external smaller Ramsey numbers and `e(3,6,17)≥40` theorem.

For direct verification run:

    python ramsey_r37_three_symbolic_proofs.py
    python ramsey_r37_symbolic_exhaustion.py

The first verifies the three explicit symbolic arguments. The second verifies the complete support-pattern exclusion.
