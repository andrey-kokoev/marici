# Rotational balance and the six exceptional contact types for R(3,7)

## Setup and scope

Assume a triangle-free 6-regular graph `G` on 23 vertices with independence number at most 6. Fix `v`, put `L=N(v)` (six labels), `X=V(G)\(L∪{v})` (16 vertices), and `C(x)=N(x)∩L`. Each label occurs in five contacts. The preceding analytic contact reductions supply sizes 1–3 and singleton count `s∈{4,5,6}`, with `n2=18−2s` and `n3=s−2`.

Write `s_i`, `d_ij`, `t_ijk` for contacts `{i}`, `{i,j}`, `{i,j,k}`. A contact label in common forbids an A-edge between the corresponding exterior vertices. For any exterior set `T` with `|⋃_{x∈T}C(x)|<|T|`, the set `T` must contain an eligible A-edge; otherwise its vertices together with unused labels in `L` form a B-clique of size at least seven. Any two forced A-edges with a common endpoint forbid the third edge of the corresponding A-triangle.

## Rotational balance (exact global identity)

Let `s(v)` count nonneighbors `w` of `v` with exactly one common A-neighbor. Let `r(v)` count pairs of neighbors of `v` whose only common A-neighbor is `v`. Every pair of nonadjacent vertices with exactly one common neighbor contributes twice to `sum_v s(v)` and once to `sum_v r(v)`. Therefore

`sum_v (s(v)−2r(v))=0`.

For each `v`, the five contacts containing any label `i∈L` form a B5-clique; they cannot collectively miss two other labels, so missing co-occurrence pairs form a matching and `r(v)≤3`. Therefore `s(v)−2r(v)≤0` is possible only at `(s,r)=(4,2),(4,3),(5,3),(6,3)`.

If `r=3`, the missing-pair matching is perfect. The possible two-label contacts are edges of an octahedron (12 edges), and the three-label contacts are its triangular facets (eight faces). If `r=2`, the possible supports are the edges and triangles of `K6` with two independent edges removed (13 edges, 12 triangles). These restricted supports, label degree equations, singleton closure, contact-fiber Hall constraints, and permutations of the missing matching yield exactly six incidence types. The check is performed independently in `ramsey_small_score_incidence_classifier.py`.

## Two repeated-triple types

If a triple contact `{i,j,k}` occurs twice and `s_i,s_j,s_k` all exist, then for each pair `a,b∈{i,j,k}`, the four vertices `s_a,s_b,t_ijk^(1),t_ijk^(2)` have contact union of size three. The only eligible A-edge is `s_a s_b`, so all three singleton-pair edges are A, giving an A-triangle. This excludes the single `(5,3)` type and one of the two `(6,3)` types.

## Four residual local contradiction certificates

**Type I: `(4,2)`.** Singleton labels `0,1,2,3`; triple contacts `014`, `235`; double contacts `01,03,05,12,15,23,24,34,45,45`. The five exterior vertices

`{t_014,d_05,d_15,d_45^(1),d_45^(2)}`

have pairwise intersecting contacts with union `{0,1,4,5}`. They are a B5-clique B-adjacent to both labels `2,3`, producing B7 directly.

**Type II: first `(4,3)` form.** Singletons `0,1,2,3`, triples `014,235`, doubles

`03,04,05,12,14,15,24,25,34,35`.

The deficient sets

`{s0,s3,d03}`, `{s1,s2,d12}`, `{s1,t014,d04,d14}`, `{s2,t235,d25,d35}`, `{s3,d03,d04,d34}`

respectively force A-edges

`s0–s3`, `s1–s2`, `s1–d04`, `s2–d35`, `s3–d04`.

The two A-paths `s1–d04–s3` and `s1–s2–d35` prohibit `s1–s3` and `s1–d35`. Consequently the deficient set `{s1,s3,d15,d35}`, whose only eligible edges are `s1–s3`, `s1–d35`, `s3–d15`, forces `s3–d15` to be A. This in turn prohibits `d04–d15` via the A-path `d04–s3–d15`. The deficient set `{s0,t014,d04,d05,d15}` then forces `s0–d15` to be A. Together with `s0–s3` and `s3–d15`, this is an A-triangle.

**Type III: second `(4,3)` form.** Singletons `0,1,2,3`, triples `014,235`, doubles

`03,04,05,12,13,14,24,25,35,45`.

The deficient sets

`{s0,t014,d04,d14}`, `{s0,d03,d05,d35}`, `{s1,s2,d12}`, `{s1,t014,d04,d14}`, `{s2,d12,d14,d24}`, `{t235,d24,d25,d35,d45}`

respectively force A-edges

`s0–d14`, `s0–d35`, `s1–s2`, `s1–d04`, `s2–d14`, `d24–d35`.

The A-paths `s0–d14–s2` and `s2–s1–d04` prohibit `s0–s2` and `s2–d04`. The deficient set `{s0,s2,d04,d24}` then forces `s0–d24`, but `s0–d35–d24` is already an A-path, giving an A-triangle.

**Type IV: `(6,3)` without repeated triples.** Singleton labels `0,…,5`; triples `012,013,245,345`; doubles `03,05,12,14,25,34`.

The deficient sets `{s0,s3,d03}`, `{s0,s5,d05}`, `{s1,s4,d14}`, `{s3,s4,d34}` force `s0–s3`, `s0–s5`, `s1–s4`, `s3–s4` to be A. Their A-wedges forbid `s0–s4`, `s3–s5`, and `s1–s3`.

The deficient set `{s1,s3,t013,d03}` then forces `s1–d03`, which forbids `s4–d03`. The deficient set `{s0,s4,d03,d34}` forces `s0–d34`, which forbids `s5–d34`. But `{s3,s5,t345,d34}` is deficient and its only eligible edges, `s3–s5` and `s5–d34`, have both been forbidden. Contradiction.

## Conclusion and limits

Every six-label contact configuration satisfying `s−2r≤0` is one of six classified incidence types, and all six have explicit forbidden B7 or A-triangle certificates. Hence `s(v)−2r(v)>0` for every vertex of a hypothetical 6-regular graph, contradicting the global identity `sum_v (s(v)−2r(v))=0`. Thus the 6-regular branch is impossible.

The classification of the six incidence types remains a finite edge/face enumeration rather than a uniform non-enumerative theorem. Excluding hypothetical degree-five vertices is a separate argument, not proved by this document.
