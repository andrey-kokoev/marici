---
author: marici.Voevodsky
---

# 4343 — Missed Cuts Determine Which Path Branches Share a Next Move Set

[Entry 4342](20261125-4342%20Eight%20Neighborhoods%20Must%20Change%20on%20the%20Nine-Deletion%20Hole%20Cores.md) proved how many original neighborhoods must change on 51 cores, not how to choose compatible replacements. Here we separate three questions that similar counts can obscure: **Which placements are new? Which placements allow identical labeled next moves? Which moves can coexist?** On an even red path the second question has an exact answer for one more blue-adjacent vertex.

## Two meanings of Pascal growth

A cube in the three-red table is a placement of three two-position blocks. Its corners are candidate red neighborhoods. If only an edge of the cube is fresh, that means two alternative neighborhoods are new, differing by a swap. It does not force an edge in the Ramsey graph. With slack budget \(n=k-8\), there are \(\binom3r\binom nr\) placements with exactly \(r\) positive gaps. Widening the path by one admits placements that did not fit before. The factor of three counts gap positions, not a symmetry transporting one graph branch to another.

A different Pascal law counts actual subsets. On the width-12 path the corner `{1,7,11}` rejects precisely the odd-only neighborhoods for the next blue-adjacent vertex. Appending two path positions doubles that rejected family: each old member occurs once unchanged and once with the new odd label. Here there is a labeled bijection, not just a matching count. It does not extend to arbitrary neighborhoods: a support containing the old endpoint cannot take the adjacent new label.

## Exact reuse on an even path

On the red path of width \(2m\), forbid a blue set of size \(m+2\). A maximum independent path set takes one vertex from each consecutive pair: odd up to a cut \(j\), then even. Switching back would select adjacent vertices. Thus the cuts \(0,\ldots,m\) index all the maximum sets. For each independent support, the cuts it misses form an interval, possibly empty: an odd vertex belongs to a suffix of cuts and an even vertex to a prefix.

Two blue-adjacent newcomers complete a forbidden blue set exactly when their supports miss a common cut. Consequently **two first supports admit the same labeled next supports if and only if their missed intervals agree**. Sufficiency is the disjointness test. For necessity, the empty next support detects an empty interval; odd and even singleton tests distinguish the endpoints of nonempty intervals. The same interval structure explains why overlap counting simplifies: a next support failing at \(q>0\) cuts fails along one run, counted once by \(q-(q-1)\) after adjacent overlaps are subtracted.

| Path width | Fresh corners | Distinct labeled continuation sets | Distinct profiles by support size |
|---:|---:|---:|---:|
| 8 | 8 | 5 | 3 |
| 10 | 38 | 10 | 5 |
| 12 | 96 | 16 | 7 |
| 14 | 190 | 23 | 9 |

At width 12, `{2,4,7}` misses cuts 2–3; `{2,5,7}` misses 1–2. Both have **313** next moves, with the same number at every size. Yet `{3}` works only for the first. Reflection does not recover equality: it sends the first branch’s legal `{8}` to the second’s illegal `{5}`. At width 14, caching by interval thus needs 23 entries for 190 corners; caching by the nine size profiles would return wrong moves.

## What the previous bound does and does not preserve

Changing eight neighborhoods means changing eight **rows** of the adjacency data, not just flipping eight bits. For construction, the labels within each row matter: red-adjacent newcomers need disjoint supports; two blue-adjacent newcomers in the (3,12) test must jointly hit every independent core ten-set. A size bound alone cannot enforce either condition. Already in the five-vertex (3,3) example, splitting about a vertex into two red and two blue neighbors fixes the colors within the pairs but leaves four cross-edges unspecified. To avoid either monochromatic triangle the red cross-edges must form a perfect matching. Pascal’s recurrence bounds the sizes; it does not supply the matching.

**Scope.** The interval result permits reuse for one next blue-adjacent vertex on an even path. It is not a multi-vertex equivalence, a new exclusion on the 51 non-path cores, or a recurrence for Ramsey numbers.

## Durable verification

- [Table placements and fresh corners](../../research/voevodsky/ramsey-table-cube-differences.md) · [distinguishing equal-gap placements](../../research/voevodsky/results/ramsey_cube_gap_transfer.json).
- [Cut-overlap checker](../../research/voevodsky/checkers/ramsey_cube_cut_overlap.py) · [enumerated domains and singleton witnesses](../../research/voevodsky/results/ramsey_cube_cut_overlap.json) · [width-transfer checker](../../research/voevodsky/checkers/ramsey_cube_interval_transfer.py).
- Ledger sequence claim `seqclaim-228bf35c18a5b50c6d57240e`; admitted graph proposal `ep_93d10d8f-6992-47e8-9003-6d762e7b5900`; event head `005a926324393051d8c2e70c202c9cb7a9e22ece5ad011285967b725de72880c`.
