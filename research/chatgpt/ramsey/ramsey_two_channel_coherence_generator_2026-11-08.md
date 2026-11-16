# A two-channel exact update law for Ramsey vertex extensions

Date: 2026-11-08  
Scope: exact combinatorial characterization, finite exact regression; no closed-form formula for general Ramsey numbers.

## 1. Ramsey model

Represent the red edges by a finite simple graph `G`. The condition for avoiding a red triangle and a blue `K_k` is

- `G` triangle-free;
- `alpha(G) <= k-1`.

Let `G + v_S` add a new vertex `v` whose red neighborhood among old vertices is `S`.

For every finite graph `G`:

`alpha(G + v_S) = max(alpha(G), 1 + alpha(G - S))`.

Triangle-freeness of `G + v_S` holds exactly when `S` is an independent set in `G`. Thus define

`E_k(G) = {S subset V(G) : S independent and alpha(G - S) <= k-2}`.

Then `S in E_k(G)` is necessary and sufficient for the new graph to be Ramsey-admissible, assuming `G` was admissible. The empty set is allowed when its independence-number bound permits it.

## 2. The complete two-channel theorem

**Theorem.** Suppose `G` is triangle-free with `alpha(G) <= k-1`, and choose `S in E_k(G)`. Set `H=G+v_S`. Then

```
E_k(H)
 = {R in E_k(G) : alpha(G - (R union S)) <= k-3}
   union
   {{v} union R : R in E_k(G), R intersect S = empty}.
```

The two displayed families are disjoint because the first excludes the new vertex and the second includes it.

**Proof.** Let `T` be the red neighborhood of a proposed second new vertex. If `v` is not in `T`, then `T=R`, where `R` is independent in `G`. Deleting `R` from `H` leaves an old copy of `G-R` plus `v`, now adjacent to `S-R`. Hence

`alpha(H-R)=max(alpha(G-R), 1+alpha(G-(S union R)))`.

This is at most `k-2` if and only if `R in E_k(G)` and `alpha(G-(S union R)) <= k-3`.

If `v in T`, then `T={v} union R`. It is independent in `H` if and only if `R` is independent in `G` and `R intersect S=empty`; deleting it leaves `G-R`. The bound is exactly `R in E_k(G)`. This proves both inclusions. QED.

## 3. Pairwise compatibility matrices and branch extinction

Index the rows and columns by `E_k(G)` and define the Boolean matrices

```
D[S,R] = 1 if S intersect R = empty, else 0
Q[S,R] = 1 if alpha(G-(S union R)) <= k-3, else 0.
```

The number of **labeled next neighborhoods** available after first choosing `S` is

`f_k(G,S) = sum_{R in E_k(G)} (D[S,R] + Q[S,R])`.

This counts different neighborhoods for the second vertex, not nonisomorphic graph extensions. Exactly,

`G+v_S is locally unextendable <=> f_k(G,S)=0`.

An automorphism `phi` of `G` preserves both matrices:

`D[phi S,phi R]=D[S,R]`, `Q[phi S,phi R]=Q[S,R]`.

Thus row-fertility and complete pair orbitals are exact symmetry-reducible observables. Quotienting only by row totals generally loses the pair-incidence data. These matrices determine immediate next-stage fertility, but do not, by themselves, constitute a complete state for arbitrarily many future steps.


### The channels are the two possible colors between the new vertices

Suppose the first new vertex has red neighborhood `S` in `G` and the second has red neighborhood `R` in `G`.

- **Channel D:** the edge between the two new vertices is **red**. Triangle-freeness forces `S intersect R=empty`. The two singleton independent-set constraints are already enforced by `S,R in E_k(G)`.
- **Channel Q:** the edge between the two new vertices is **blue**. Their two-vertex set is independent, so an old independent set disjoint from `S union R` could join both. The exact additional requirement is `alpha(G-(S union R))<=k-3`.

Both matrices are symmetric. Exchanging the order in which these two vertices were added yields the same red graph up to swapping the two new-vertex labels. This supplies an exact two-step interchange, not an assumed noncommutative braid relation.

## 4. Higher-arity coherence: the full finite assembly law

Add `m` new vertices. Let `H` be the red graph on those vertices and give each new vertex `i` an old red neighborhood `S_i` in `G`.

The resulting graph is triangle-free exactly when:

1. `G` and `H` are triangle-free;
2. every `S_i` is independent in `G`;
3. `S_i intersect S_j=empty` whenever `ij` is a red edge of `H`.

For each independent subset `J` of the new vertices, put `S(J)=union_{i in J} S_i`. Then the *exact* independence-number identity is

`alpha(G_extended) = max_{J independent in H} (|J| + alpha(G - S(J)))`.

**Proof:** every independent set in the extended graph decomposes uniquely into an independent new-vertex subset `J` and an independent old-vertex subset avoiding all its red neighborhoods. Maximizing the old part independently yields the expression. QED.

Consequently the complete Ramsey compatibility condition is

`|J| + alpha(G-S(J)) <= k-1` **for every independent `J` in `H`**.

The two-channel theorem is its exact `m=2` instance.

### Three-way obstruction despite all valid pairs

Fix `k=4`, take three old mutually blue vertices `a,b,c`, and add three new mutually blue vertices `u,v,w`. Give all three the same old red neighborhood `{a,b}`.

Every one-new-vertex extension is valid: the largest independent set has size three. Every two-new-vertex extension is also valid, with independence number three. But the full six-vertex graph contains the blue `K_4` on `{c,u,v,w}` and has independence number four.

A proposed red edge between any two of `u,v,w` is also illegal, since they share red neighbors `a` and `b`, creating a red triangle. Hence the failure cannot be fixed by changing just their mutual color.

Exhaustive enumeration of all `8^3=512` choices of the three old red neighborhoods and all eight red/blue patterns on the three new vertices (4,096 assembled graphs) confirms the general identity. Of the all-blue-new-vertex cases, **39 ordered neighborhood triples** have every singleton and pair Ramsey-admissible but the complete triple forbidden. These 39 are a finite count for this specified fixture, not a Ramsey threshold.

## 5. Concrete branch: `R(3,3)`

Let `G=P3`, the path `0-1-2`. It is triangle-free and has independence number two. The complete admissible-neighborhood family is

`E_3(P3) = { {0}, {2}, {0,2} }`.

The matrix pair, indexed in that order, is

```
D = [0 1 0]       Q = [0 0 0]
    [1 0 0]           [0 0 0]
    [0 0 0]           [0 0 0]
```

The row-fertility vector is `(1,1,0)`.

- Choosing `S={0}` creates `P4`, with one further admissible neighborhood. Choosing `S={2}` is symmetric.
- Choosing `S={0,2}` creates `C4`, with no further admissible neighborhood.
- For `P4`, `E_3(P4)={{0,3}}`. Its only extension is `C5`, which has `E_3(C5)=empty`.

Among all nonisomorphic triangle-free graphs with `alpha<=2`, there are exactly three on four vertices: `2K2`, `C4`, `P4`. The first two cannot extend; `P4` extends to the unique five-vertex member `C5`. No six-vertex member exists, so `R(3,3)=6`.

This illustrates why **the earliest locally terminal branch cannot determine the global threshold**.

## 6. A correction to the compatibility-spiral interpretation

When `alpha(G)=k-1`, let `M(G)` be its maximum independent sets, and define the simplicial complex

`C(G)={T subset M(G) : some independent S intersects every I in T}`.

Then

`E_k(G) nonempty <=> C(G) is the full simplex on M(G)`.

Indeed, any independent hitting set of the full family witnesses every subfamily, while the top face of the full simplex supplies an independent hitting set of all maximum independent sets.

Consequently a nontrivial reduced homology class in `C(G)` certifies that `G` is locally unextendable. The converse fails: a locally unextendable compatibility complex can be acyclic. Moreover, **an extendible saturated graph's compatibility complex is necessarily a full simplex**, so nontrivial holes cannot gradually accumulate within it along an admissible fixed-`k` extension chain.

The caveat `alpha(G)=k-1` is essential: below saturation, the Ramsey extension test has slack and does not require hitting all maximum independent sets of `G`.

### Explicit topology changes at the terminal step

- `P3 -> C4`: the compatibility complex changes from one vertex (contractible) to two isolated vertices (`reduced beta_0=1`).
- `P4 -> C5`: it changes from the complete triangle (contractible) to a five-vertex complex with `f=(1,5,10,5)` (empty face, vertices, edges, triangles) and `reduced beta_1=1` over `F_2`.

The homology appears when the chosen branch becomes terminal, not as a progressive accumulation of nonzero homology throughout an extendible branch.

The inherited-core transport previously examined between distinct Ramsey parameters `k` and `k+1` changes the independence-number threshold and the constraint universe. It is not the same operation as a vertex extension at fixed `k`.

## 7. Exhaustive finite regression

Run:

```sh
python ramsey_two_channel_extension.py
```

The checker derives `alpha(G-W)` exactly by integer-mask dynamic programming for all vertex-deletion subsets, generates every admissible `S`, evaluates both channels, constructs `H=G+v_S`, then independently enumerates `E_k(H)` and compares the two sets.

Its input is every unlabeled simple graph with at most seven vertices in NetworkX's graph atlas, restricted to triangle-free `G` with `alpha(G)<=k-1`, for `k=3,4,5`.

Results:

| k | Distinct admissible atlas graphs | Verified labeled vertex extensions |
|---:|---:|---:|
| 3 | 10 | 16 |
| 4 | 46 | 221 |
| 5 | 130 | 2,595 |
| **Total** | **186** | **2,832** |

Every predicted complete neighborhood family equals the directly computed family. The same checker also runs 4,096 exact three-new-vertex assembly tests, with 39 pairwise-compatible but jointly forbidden all-blue-new-vertex cases. This is a finite regression of separately proved general theorems; it is not an exhaustive construction of `R(3,5)` or beyond.

## 8. Research target after the theorem

The two matrices define an exact immediate-extension compatibility field. To progress toward Ramsey thresholds:

1. Generate all admissible states at a fixed `k`, retaining branches that are still extendible. This is necessary because sterile branches can occur before the threshold.
2. Quotient each pair-compatibility field under the actual graph automorphisms, preserving the full pair orbitals and their multiplicities.
3. Test whether a smaller recursively sufficient state can update the pair fields without reconstructing all vertex subsets. A sufficient state must distinguish all future viability, not merely the current row-fertility vector.
4. Certify extinction only after **every** isomorphism class at a given vertex count has no surviving extension.

The formulation uses no assumed braid, spinor, Mathieu group, or fitted Ramsey increment. Its relationship to those symmetry constructions can now be tested by explicit equivariance maps.
