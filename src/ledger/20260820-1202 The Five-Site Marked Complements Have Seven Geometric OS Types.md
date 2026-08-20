---
title: "The Five-Site Marked Complements Have Seven Geometric OS Types"
date: 2026-08-20
entry: 1202
status: active-geometric-carrier-cohomology
sector: cosmology
---

# 1202 — The Five-Site Marked Complements Have Seven Geometric OS Types

Sequence claim: `seqclaim-946ddd98f5ffce1b6ad531d1`.

## Geometric versus occurrence generators

Entry 1201 freezes twelve matroid profiles after retaining occurrence depth
on every flat. To compute the geometric hyperplane-complement cohomology,
use one (d\log q) generator per geometric hyperplane. Coincident source
labels do not create independent logarithmic forms:

\[
d\log q=d\log q.
\]

Their occurrence multiplicities remain external labelled data for later
coefficient and transition maps.

## Exact Orlik--Solomon calculation

For every term, enumerate all no-broken-circuit subsets using Entry 1201's
complete minimal-circuit list. The central rank-five OS Hilbert series has
the Euler factor (1+t). Dividing by it gives the projective complement in

\[
\mathbf P^4.
\]

The twelve incidence profiles collapse to seven geometric cohomology types:

\[
\boxed{
\begin{array}{c|c|c}
m& (b_0,b_1,b_2,b_3,b_4)&\text{terms}\\
\hline
7&(1,6,15,17,7)&10\\
7&(1,6,15,18,9)&50\\
7&(1,6,15,19,11)&10\\
8&(1,7,21,30,17)&50\\
8&(1,7,21,31,19)&30\\
8&(1,7,21,32,21)&20\\
9&(1,8,28,48,33)&10.
\end{array}}
\]

Each term count is a union of free (C_5)-orbits.

## Meaning

The distinction between carrier geometry and occurrence presentation is now
quantitative:

\[
12\text{ occurrence-refined matroid profiles}
\longrightarrow
7\text{ geometric OS types}.
\]

Collapsing occurrences before transport would lose source labels. Duplicating
them as OS generators would instead manufacture complement cohomology. The
correct architecture is a geometric OS carrier equipped with labelled
occurrence modules.

## Next falsifier

Construct the occurrence module over each of the seven OS complexes. Derive
its transition maps from the complement-label identifications and test
cyclic descent. Reject any construction that changes the geometric Betti
vectors or introduces a generator solely because two source labels coincide.

Only after this descent may the five-site Cayley--Menger double-cover
coefficient system be attached.

## Artifacts

- `research/benincasa/checkers/five_site_qg_projective_os.py`
- `research/benincasa/results/five-site-qg-projective-os.json`
