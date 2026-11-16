# Ramsey extension obstruction: exact Bonferroni depth and overlap tails

Date: 2026-11-08

## Scope

We evaluate the proposed third-order inclusion–exclusion certificate on the complete extremal graph6 lists for `R(3,4)` (three eight-vertex graphs), `R(3,5)` (one thirteen-vertex graph), and `R(3,6)` (seven seventeen-vertex graphs). The complete graph6 strings and a dependency-free exact checker are in `check_ramsey_bonferroni_depth.py`. These are **the complete families at maximal admissible order**, not all smaller admissible graphs. Each graph is independently verified triangle-free, with independence number `k−1`, and independently terminal under the one-vertex extension criterion.

## 1. Exact coverage formula and Bonferroni truncation

For a triangle-free graph `G` with `alpha(G)=k−1`, write `M` for its maximum independent sets, `N=|M|`. A candidate red neighborhood `S` must be independent. It is admissible for adding one vertex iff `S` intersects every `I in M`.

For `T` a vertex subset, set `m_T = #{I in M:T subset I}`. For odd `d`, define

`U_d(S) = sum_{j=1}^d (-1)^(j+1) sum_{T subset S, |T|=j} m_T`.

Let `h_I=|S intersection I|`. Then the binomial identity gives

`U_d(S) = sum_{I in M, h_I>0} [1 + choose(h_I−1,d)]`.

Writing `C(S)=#{I in M:h_I>0}`, `D(S)=N−C(S)`, `E_d(S)=sum_{I:h_I>0} choose(h_I−1,d)`, we obtain

`U_d(S)=C(S)+E_d(S)`, and **`U_d(S)<N iff E_d(S)<D(S)`**.

Thus `U_d` is an upper bound on covered maximum independent sets, and third-order certification works if for **every** independent `S`, the unseen-disjointness count `D(S)` strictly exceeds the overlap-tail correction `E_3(S)`.

The summand `1+choose(h−1,d)` is monotone nondecreasing in `h` for odd `d`; testing inclusion-maximal independent `S` is sufficient to maximize `U_d`. Exact terminality, in contrast, requires only `D(S)>0` for every independent `S`.

## 2. Complete extremal-family census

The numerical columns are maxima over all inclusion-maximal independent neighborhoods `S`, independently enumerated.

| k | Graph ID | n | N=number of maximum independent sets | max U1 | max U3 | max U5 | Third order certifies? |
|---:|---:|---:|---:|---:|---:|---:|---|
| 4 | 1 | 8 | 10 | 14 | 9 | — | Yes |
| 4 | 2 | 8 | 12 | 14 | 9 | — | Yes |
| 4 | 3 | 8 | 8 | 9 | 5 | — | Yes |
| 5 | 1 | 13 | 39 | 48 | 29 | — | Yes |
| 6 | 1 | 17 | 82 | 146 | **82** | 74 | **No** |
| 6 | 2 | 17 | 80 | 143 | 79 | 70 | Yes |
| 6 | 3 | 17 | 90 | 146 | 83 | 74 | Yes |
| 6 | 4 | 17 | 82 | 130 | 76 | 68 | Yes |
| 6 | 5 | 17 | 90 | 150 | 86 | 78 | Yes |
| 6 | 6 | 17 | 70 | 114 | 66 | 58 | Yes |
| 6 | 7 | 17 | 74 | 117 | 68 | 60 | Yes |

First order certifies none of these 11 graphs; third order certifies 10; fifth order certifies all seven of the `k=6` graphs. Fifth order is an **exact inclusion–exclusion count here because every maximum independent set has only five vertices**; its success does not establish a deeper five-dimensional obstruction.

## 3. Exact third-order failure on an extremal graph

Graph 1 at `k=6` has graph6 string:

`P??GaOo\`XMGsIcT?pSLaGuA?`

It contains 82 maximum independent sets and 83 inclusion-maximal independent sets. Exactly three independent candidate neighborhoods fail third-order certification, though all are in fact inadmissible:

| S (zero-based vertices) | Actual sets intersected | Sets disjoint (`D`) | Intersections of size 4 | Intersections of size 5 | Overlap-tail `E3` | `U3` |
|---|---:|---:|---:|---:|---:|---:|
| `{0,1,2,3,5}` | 73 | 9 | 5 | 1 | 5+4=9 | 82 |
| `{0,1,2,4,6}` | 73 | 9 | 5 | 1 | 5+4=9 | 82 |
| `{0,1,2,5,6}` | 74 | 8 | 4 | 1 | 4+4=8 | 82 |

There is no admissible red neighborhood in this graph. The truncated bound's failure is precisely **cancellation of the true disjointness obstruction by its positive overlap-tail error**. It is not a newly established nonzero homology class or a braid defect.

## 4. Uniform third-order failure: three disjoint five-cycles

Let `G_t` be the disjoint union of `t` copies of `C5`. It is triangle-free, has `alpha(G_t)=2t`, and is terminal for `k=2t+1`: every independent neighborhood in each component is disjoint from some maximum independent set in that component, and these choices assemble to a maximum independent set in `G_t`.

Fix `S` to be the union of a chosen maximum independent set in each `C5`. Among the five maximum independent sets of one `C5`, the overlap with `S` is 0 in two cases, 1 in two cases, and 2 in one case. Across `t` components the overlap generating polynomial is exactly

`P_t(z)=(2+2z+z^2)^t`.

Thus `N=5^t`, `D(S)=2^t`, and the exact covered count is `5^t−2^t`. The odd-order upper bound is the coefficient sum

`U_d(S)=sum_{h>=1} [z^h]P_t(z) * (1 + choose(h−1,d))`.

| t | k=2t+1 | n=5t | N | Actual coverage | U3 | U5 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 5 | 5 | 3 | 3 | 3 |
| 2 | 5 | 10 | 25 | 21 | 22 | 21 |
| 3 | 7 | 15 | 125 | 117 | **169** | 118 |
| 4 | 9 | 20 | 625 | 609 | **1580** | 710 |

Already `3 C5` is terminal for `k=7` while its third-order Bonferroni bound is 169, greater than the 125 maximum independent sets. This example is **not** extremal for `R(3,7)`.

For every fixed odd `d`, the same family eventually defeats the `d`th-order upper bound. Let `H` be the overlap between the fixed `S` and a uniformly chosen maximum independent set of `G_t`. Then `E H=4t/5`, `0<=H<=2t`, so `P(H>=t/2)>=1/5`. Therefore

`E_d(S) >= 5^(t−1) choose(ceil(t/2)−1,d)`,

which eventually exceeds `D(S)=2^t`. Thus `U_d(S)>=N` for sufficiently large `t`.

This rules out a universal **fixed-order odd Bonferroni certificate** for terminal triangle-free graphs. It does **not** rule out every conceivable low-order structural or symmetry-based certificate, nor does it prove unbounded order is necessary in extremal graphs.

## 5. Research disposition

1. The third-order bound is effective on ten of eleven extremal graphs at `k=4..6` but fails at one actual `k=6` extremal witness.
2. The failure is completely quantified by the overlap-tail identity `U_d=C+E_d`. The difference between third and fifth order may be a truncation artifact rather than irreducible higher coherence.
3. The direct extension criterion remains the independent-transversal condition. Minimal incompatible families and their transport are stronger research objects than a fixed-order Bonferroni approximation.
4. A potentially productive follow-up is to identify *source-derived inequalities controlling `E_3(S)/D(S)`*, and determine whether any such inequalities hold uniformly near the extremal Ramsey frontier. That is narrower and falsifiable.

Reproduce:

`python check_ramsey_bonferroni_depth.py`
